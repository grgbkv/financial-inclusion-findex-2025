"""E52 (pre-registered 2026-08-18): agenda item 7.9 — a B12 weight-structure sweep on the
`fin31d`~`fin34c` cash cell. WHY do the two lenses disagree?

Parent: E48b / E50 (second descendant). THIS IS AN INFERENCE/AUDIT PASS, NOT AN ASSOCIATION
EXPERIMENT, so B14's long-difference-or-all-windows requirement does not bind: no new co-movement is
registered. Every cell touched here is already in the ledger.

WHY. The fin31d~fin34c cash cell is the ledger's clearest STABLE weighted/unweighted disagreement.
E48's primary split weighted 3/3 against unweighted 1/3; E50 reproduced that split EXACTLY on a
different pair of margins in the same two modules (weighted +0.795 / +0.650 / +0.615, unweighted
+0.431 / +0.243 / +0.263). Two designs now agree that something systematic separates the lenses, and
the ledger's standing explanation is the phrase B12 was written to ban: "the big economies decide
it". B12 replaced the guess with a NAMED economy; this experiment replaces the named economy with a
MECHANISM. Two candidates, with different consequences:

  HETEROGENEITY — the association really IS stronger in large economies. Then the weighted statistic
  is correct about the typical PERSON and the unweighted one about the typical ECONOMY (the
  2026-08-13 amendment), and the disagreement is a finding about population size, not a defect.

  LEVERAGE — a handful of enormous weights carry the weighted number with no size gradient
  underneath. Then the weighted statistic is an artifact of the weight distribution and should not be
  reported as a developing-world regularity at all.

DESIGN. Pair (d fin31d, d fin34c) on the developing panel in FOUR cells: 2014->17, 2017->21,
2021->24 and the 2014->2024 long difference. E50's cells are recomputed first (the E35 rule: abort if
the long difference does not reproduce +0.515 / +0.389 within 0.02). Per cell:

  1. WEIGHT-TERCILE UNWEIGHTED correlations. Economies split into terciles by 2024 adult population;
     r_u computed WITHIN each tercile. The heterogeneity test — it uses no weights at all, so it
     cannot be produced by leverage.
  2. WINSORIZED-WEIGHT correlation. r_w recomputed with weights capped at the 90th percentile (a
     second cut at the median is a diagnostic). The leverage test — capping changes only the weight
     vector, never the sample.
  3. FRAGILITY DEPTH. The minimum number of economies whose greedy removal drives r_w below +0.30,
     with the economies NAMED. Searched to a cap of 10.
  4. ASCENT DEPTH. The mirror for the unweighted lens: minimum greedy removals lifting r_u above
     +0.30, named, capped at 10.
  5. B6/B10/B12 on every cell: bootstrap interval and p_boot for each tercile and each capped-weight
     correlation, Kish neff, and the FIVE largest single leave-one-out effects with economies named.

REGISTERED VERDICT RULE (fixed before the run, evaluated over the four cells):
  HETEROGENEITY fires if in >= 3 of 4 cells the TOP-population-tercile r_u >= +0.30 AND the
    BOTTOM-tercile r_u < +0.30.
  LEVERAGE fires if in >= 3 of 4 cells the 90th-percentile-capped r_w < +0.30.
  exactly one fires -> `keep`, claim names that mechanism.
  both fire        -> `keep`, claim names both (they are not mutually exclusive).
  neither fires    -> `inconclusive` (status table: a registered diagnostic whose fixed verdict rule
                      returns neither branch).

REGISTERED SIGN (B15): every correlation in this cell is positive in every lens-window measured so
far, so the heterogeneity branch is registered POSITIVE. A top-tercile r_u at or below -0.30 is the
OPPOSITE pattern, reported separately and never as partial confirmation.

B16 — PATH BEFORE SPAN for the long-difference cell: the file prints the wave levels. Both margins
are NON-MONOTONE, falling for a decade and rebounding in the last window (agenda item 7.8).

DECLARED, and it bounds every branch. Tercile correlations run on ~24 economies each; small-n
correlations are noisy and the intervals will be wide, which is why the verdict rule asks for a
PATTERN ACROSS FOUR CELLS rather than significance in any one. Nothing here is causal. Nothing here
rehabilitates or demotes E48b — its status is fixed at `keep-window`, FAILED promotion. This
experiment explains a disagreement; it does not resolve it in either lens's favour.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 52
WAVES = [2014, 2017, 2021, 2024]
A = "fin31d"
B = "fin34c"

CELLS = [(2014, 2017), (2017, 2021), (2021, 2024), (2014, 2024)]
LONG = (2014, 2024)
BAR = 0.30
CAP_Q = 0.90        # registered winsorization point
DEPTH_CAP = 10      # registered search cap for both depth statistics


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def corr(x, y, w=None):
    m = pd.notna(x) & pd.notna(y)
    if w is not None:
        m &= pd.notna(w)
    x, y = x[m], y[m]
    if len(x) < 10:
        return np.nan, int(len(x))
    ww = np.ones(len(x)) if w is None else np.asarray(w[m], dtype=float)
    mx, my = np.average(x, weights=ww), np.average(y, weights=ww)
    sx = np.sqrt(np.average((x - mx) ** 2, weights=ww))
    sy = np.sqrt(np.average((y - my) ** 2, weights=ww))
    if sx == 0 or sy == 0:
        return np.nan, int(len(x))
    return float(np.average((x - mx) * (y - my), weights=ww) / (sx * sy)), int(len(x))


def boot_ci(d, weighted, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(d)), []
    for _ in range(draws):
        s = d.iloc[rng.choice(idx, size=len(idx), replace=True)]
        v = corr(s["x"], s["y"], s["w"] if weighted else None)[0]
        if pd.notna(v) and np.isfinite(v):
            out.append(v)
    if len(out) < draws // 4:
        return np.nan, np.nan, np.nan
    a = np.asarray(out)
    return (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)),
            float(2 * min((a <= 0).mean(), (a >= 0).mean())))


def greedy_depth(d, weighted, direction, cap=DEPTH_CAP):
    """Minimum greedy removals to push r past the +0.30 bar.
    direction 'down': remove the economy that most REDUCES r, stop when r < BAR.
    direction 'up'  : remove the economy that most RAISES  r, stop when r > BAR.
    Returns (k, names, r_trace). k = None if the bar is not crossed within `cap`."""
    cur = d.copy()
    names, trace = [], []
    for k in range(cap):
        r = corr(cur["x"], cur["y"], cur["w"] if weighted else None)[0]
        if direction == "down" and r < BAR:
            return k, names, trace
        if direction == "up" and r > BAR:
            return k, names, trace
        best = None
        for i in cur.index:
            sub = cur.drop(i)
            if len(sub) < 12:
                continue
            rv = corr(sub["x"], sub["y"], sub["w"] if weighted else None)[0]
            if pd.isna(rv):
                continue
            if best is None or (rv < best[0] if direction == "down" else rv > best[0]):
                best = (rv, i)
        if best is None:
            break
        cur = cur.drop(best[1])
        names.append(best[1])
        trace.append(best[0])
    r = corr(cur["x"], cur["y"], cur["w"] if weighted else None)[0]
    if (direction == "down" and r < BAR) or (direction == "up" and r > BAR):
        return cap, names, trace
    return None, names, trace


def build_cell(T, a, b):
    cols = [f"{A}@{a}", f"{A}@{b}", f"{B}@{a}", f"{B}@{b}", "pop"]
    sub = T[cols].dropna()
    return pd.DataFrame({"x": sub[f"{A}@{b}"] - sub[f"{A}@{a}"],
                         "y": sub[f"{B}@{b}"] - sub[f"{B}@{a}"],
                         "w": sub["pop"]})


def main():
    fx = Findex()
    dev = fx.pan_dev
    d0 = dev[dev["year"].isin(WAVES)]

    tab = {}
    for c in [A, B]:
        w = d0.pivot_table(index="countrynewwb", columns="year", values=c) * 100
        for y in WAVES:
            tab[f"{c}@{y}"] = w[y] if y in w.columns else pd.Series(dtype=float)
    T = pd.DataFrame(tab)
    T["pop"] = dev[dev["year"] == 2024].set_index("countrynewwb")["pop_adult"].reindex(T.index)

    print("=" * 134)
    print("E52 — WHY do the lenses disagree on the fin31d~fin34c cash cell? "
          "(agenda 7.9; parent E48b/E50; inference pass, B12)")
    print("=" * 134)

    # --------------------------------------------------- B16: path before span
    print("\nB16 — PATH BEFORE SPAN. Weighted developing-panel levels (pp):")
    for c in [A, B]:
        s = fx.series(dev, c, WAVES)
        print(f"  {c:10s} " + "  ".join(f"{y}: {s[y]:5.1f}" for y in WAVES if y in s.index))
    print("  BOTH margins are NON-MONOTONE: a decade of decline and a rebound in 2021->24 "
          "(agenda item 7.8, unexplained).")

    # --------------------------------------------------- E35 rule: reproduce the parent
    ref = build_cell(T, *LONG)
    rw_ref = corr(ref["x"], ref["y"], ref["w"])[0]
    ru_ref = corr(ref["x"], ref["y"])[0]
    print(f"\nE35 RULE — reproduce E48b/E50's published long-difference cell first: "
          f"r_w {rw_ref:+.3f} (published +0.515), r_u {ru_ref:+.3f} (published +0.389)")
    assert abs(rw_ref - 0.515) <= 0.02 and abs(ru_ref - 0.389) <= 0.02, "ABORT — no reproduce"
    print("  reproduced within 0.02 — proceeding.")

    # --------------------------------------------------- the sweep
    results = []
    for a, b in CELLS:
        d = build_cell(T, a, b)
        label = f"{a}->{b}" + (" (LONG)" if (a, b) == LONG else "")
        rw, n = corr(d["x"], d["y"], d["w"])
        ru, _ = corr(d["x"], d["y"])

        # 1. weight terciles, UNWEIGHTED correlation within each
        q = d["w"].rank(pct=True)
        terc = {}
        for name, mask in (("bottom", q <= 1 / 3), ("middle", (q > 1 / 3) & (q <= 2 / 3)),
                           ("top", q > 2 / 3)):
            sub = d[mask]
            r_t, n_t = corr(sub["x"], sub["y"])
            lo, up, pb = boot_ci(sub, weighted=False) if n_t >= 10 else (np.nan,) * 3
            terc[name] = {"r": r_t, "n": n_t, "ci": (lo, up), "p": pb,
                          "popmin": float(sub["w"].min()) if len(sub) else np.nan,
                          "popmax": float(sub["w"].max()) if len(sub) else np.nan}

        # 2. winsorized weights
        caps = {}
        for qq, tag in ((CAP_Q, "p90"), (0.50, "median")):
            capv = float(d["w"].quantile(qq))
            dc = d.copy()
            dc["w"] = dc["w"].clip(upper=capv)
            r_c, _ = corr(dc["x"], dc["y"], dc["w"])
            lo, up, pb = boot_ci(dc, weighted=True)
            caps[tag] = {"r": r_c, "cap_m": capv / 1e6, "ci": (lo, up), "p": pb,
                         "neff": kish(dc["w"])}

        # 3/4. depths
        k_down, nm_down, tr_down = greedy_depth(d, weighted=True, direction="down")
        k_up, nm_up, tr_up = greedy_depth(d, weighted=False, direction="up")

        # 5. five largest single leave-one-out effects on r_w
        loo = sorted(((corr(d.drop(i)["x"], d.drop(i)["y"], d.drop(i)["w"])[0] - rw, i)
                      for i in d.index), key=lambda t: -abs(t[0]))[:5]

        results.append({"label": label, "r_w": rw, "r_u": ru, "n": n, "neff": kish(d["w"]),
                        "terc": terc, "caps": caps, "k_down": k_down, "nm_down": nm_down,
                        "tr_down": tr_down, "k_up": k_up, "nm_up": nm_up, "tr_up": tr_up,
                        "loo": loo, "wshare_top5": float(
                            d["w"].nlargest(5).sum() / d["w"].sum())})

    # --------------------------------------------------- reporting
    print("\n" + "-" * 134)
    print("THE CELL, as it stands in the ledger")
    print("-" * 134)
    print(f"  {'cell':18s}{'r_w':>9s}{'r_u':>9s}{'n':>5s}{'neff':>7s}"
          f"{'top-5 weight share':>21s}")
    for r in results:
        print(f"  {r['label']:18s}{r['r_w']:>9.3f}{r['r_u']:>9.3f}{r['n']:>5d}"
              f"{r['neff']:>7.1f}{r['wshare_top5']:>20.1%}")

    print("\n" + "-" * 134)
    print("1. HETEROGENEITY TEST — UNWEIGHTED r within population terciles (no weights used "
          "anywhere in this block)")
    print("-" * 134)
    print(f"  {'cell':18s}{'bottom r_u':>12s}{'n':>4s}{'middle r_u':>12s}{'n':>4s}"
          f"{'top r_u':>12s}{'n':>4s}   top-tercile 95% CI")
    for r in results:
        t = r["terc"]
        ci = (f"[{t['top']['ci'][0]:+.3f}, {t['top']['ci'][1]:+.3f}]"
              if pd.notna(t['top']['ci'][0]) else "n/a")
        print(f"  {r['label']:18s}{t['bottom']['r']:>12.3f}{t['bottom']['n']:>4d}"
              f"{t['middle']['r']:>12.3f}{t['middle']['n']:>4d}"
              f"{t['top']['r']:>12.3f}{t['top']['n']:>4d}   {ci}")
    het = [r for r in results
           if pd.notna(r["terc"]["top"]["r"]) and pd.notna(r["terc"]["bottom"]["r"])
           and r["terc"]["top"]["r"] >= BAR and r["terc"]["bottom"]["r"] < BAR]
    print(f"\n  cells with top-tercile r_u >= +{BAR:.2f} AND bottom-tercile r_u < +{BAR:.2f}: "
          f"{len(het)}/4 ({', '.join(r['label'] for r in het) if het else 'none'})")
    wrong = [r for r in results if pd.notna(r["terc"]["top"]["r"])
             and r["terc"]["top"]["r"] <= -BAR]
    print(f"  B15 WRONG-SIGN cells (top-tercile r_u <= -{BAR:.2f}): "
          f"{', '.join(r['label'] for r in wrong) if wrong else 'none'}")

    print("\n" + "-" * 134)
    print("2. LEVERAGE TEST — r_w with the weight vector WINSORIZED (same sample, capped weights)")
    print("-" * 134)
    print(f"  {'cell':18s}{'r_w full':>10s}{'r_w cap p90':>13s}{'[95% CI]':>20s}{'p_boot':>8s}"
          f"{'neff p90':>10s}{'r_w cap median':>16s}{'neff med':>10s}{'r_u':>9s}")
    for r in results:
        c9, cm = r["caps"]["p90"], r["caps"]["median"]
        ci = f"[{c9['ci'][0]:+.3f}, {c9['ci'][1]:+.3f}]"
        print(f"  {r['label']:18s}{r['r_w']:>10.3f}{c9['r']:>13.3f}{ci:>20s}{c9['p']:>8.3f}"
              f"{c9['neff']:>10.1f}{cm['r']:>16.3f}{cm['neff']:>10.1f}{r['r_u']:>9.3f}")
    lev = [r for r in results if pd.notna(r["caps"]["p90"]["r"])
           and r["caps"]["p90"]["r"] < BAR]
    print(f"\n  cells whose p90-capped r_w falls below +{BAR:.2f}: "
          f"{len(lev)}/4 ({', '.join(r['label'] for r in lev) if lev else 'none'})")

    print("\n" + "-" * 134)
    print("3/4. DEPTH — how many economies decide each lens's verdict (greedy, cap 10, named)")
    print("-" * 134)
    for r in results:
        kd = "none within 10" if r["k_down"] is None else f"{r['k_down']}"
        ku = "none within 10" if r["k_up"] is None else f"{r['k_up']}"
        print(f"  {r['label']:18s}")
        print(f"      fragility depth (weighted r_w -> below +{BAR:.2f}): {kd}"
              f"   removals: {', '.join(f'{n} ({t:+.3f})' for n, t in zip(r['nm_down'], r['tr_down'])) or '—'}")
        print(f"      ascent depth   (unweighted r_u -> above +{BAR:.2f}): {ku}"
              f"   removals: {', '.join(f'{n} ({t:+.3f})' for n, t in zip(r['nm_up'], r['tr_up'])) or '—'}")

    print("\n" + "-" * 134)
    print("5. B12 — the five largest single leave-one-out effects on r_w, economies named")
    print("-" * 134)
    for r in results:
        print(f"  {r['label']:18s}" +
              "   ".join(f"{n} {v:+.3f}" for v, n in r["loo"]))

    # --------------------------------------------------- VERDICT
    het_fires = len(het) >= 3
    lev_fires = len(lev) >= 3
    print("\n" + "=" * 134)
    print("E52 VERDICT (pre-registered rule, evaluated over the four cells)")
    print(f"  HETEROGENEITY branch (top-tercile r_u >= +{BAR:.2f} and bottom < +{BAR:.2f} in "
          f">=3 of 4): {len(het)}/4 -> {'FIRES' if het_fires else 'does not fire'}")
    print(f"  LEVERAGE branch (p90-capped r_w < +{BAR:.2f} in >=3 of 4): "
          f"{len(lev)}/4 -> {'FIRES' if lev_fires else 'does not fire'}")
    if het_fires and lev_fires:
        verdict, mech = "keep", "BOTH mechanisms are present"
    elif het_fires:
        verdict, mech = "keep", "HETEROGENEITY: the association is genuinely size-graded"
    elif lev_fires:
        verdict, mech = "keep", "LEVERAGE: a handful of enormous weights carry the weighted number"
    else:
        verdict, mech = "inconclusive", "neither branch fires"
    print(f"  -> E52 {verdict.upper()} — {mech}")
    print("  Registered reading, written before the answer: this experiment explains the "
          "disagreement, it does")
    print("  not resolve it in either lens's favour, and E48b's status is fixed at "
          "`keep-window`, FAILED promotion.")
    print("=" * 134)
    return verdict


if __name__ == "__main__":
    main()
