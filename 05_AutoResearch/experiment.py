"""E50 (pre-registered 2026-08-17): does the cash co-retreat hold in EVERY window?
Agenda item 7.7 — the promotion route for E48b. Parent: E48b (first descendant).

B14-COMPLIANT: an ALL-WINDOWS design. The registered claim must hold in EVERY tested transition, not
a majority. E48b is currently a single long-difference cell and cannot be promoted without this.

WHY. E48b found that the two counter-moving margins the loop has identified — `fin31d` (E45,
`fin31` module) and `fin34c` (E47, `fin34` module) — RETREAT TOGETHER across the decade:
r(d fin31d, d fin34c) = +0.515 weighted / +0.389 unweighted over 2014->2024, G6 +0.443, with a
partial controlling for d g20_any that STRENGTHENS to +0.597 / +0.383. E39 established that
country-level change does not autocorrelate (consecutive-window Spearman <= +0.07 in all ten pairs,
negative in eight), so a long difference can be carried by a single sub-window. This experiment finds
out whether it is.

DESIGN. r(d fin31d, d fin34c) on the developing panel in 2014->2017, 2017->2021 and 2021->2024, both
lenses, with the 2014->2024 long difference recomputed inside this file FIRST (the E35 rule: every
replication file reproduces its parent's cell before any verdict is read; ABORT if it does not
reproduce within 0.02).

REGISTERED BAR AND SIGN (B15). r >= +0.30 on BOTH lenses in ALL THREE windows -> E48b promoted to
`keep-general` (B4 + B8). Any window failing the bar, or matching in magnitude with a NEGATIVE sign,
-> E48b STAYS `keep-window` and is recorded as having FAILED its promotion test, never as "not
attempted". A lens split (weighted 3/3, unweighted not) -> `discard-weighted` on the promotion, with
E48b left at `keep-window`.

B16 — PATH BEFORE SPAN. The experiment prints the intermediate wave levels for both margins. Known
non-monotonicity (E47): `fin31d` 47.1 -> 34.1 -> 20.5 -> 26.6 and `fin34c` 15.9 -> 11.8 -> 8.0 ->
15.2 — both fall for a decade and REBOUND in the last window (agenda item 7.8). The rebound sits IN
the 2021->24 window this design tests, so that window is the informative one and its result is
registered in advance as such either way.

SECONDARY (registered, no bar, diagnostic): the partial controlling for d g20_any, per window, both
lenses. E48b's partial strengthened on the long difference; the question is whether it does so in
each window. No bar, because E35 established partials are the most weighting-fragile design in the
ledger.

B6/B9/B10/B12 on every cell. DECLARED: delta->delta co-movement inside a window identifies nothing;
both margins may move with a third factor. Item meanings are INFERRED from levels and coverage
(HARNESS_V2_NOTES.md items 6-7), never read from a questionnaire, and that caveat travels with any
claim made here.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 50
WAVES = [2014, 2017, 2021, 2024]
A = "fin31d"
B = "fin34c"
HEAD = "g20_any"

WINDOWS = [(2014, 2017), (2017, 2021), (2021, 2024)]   # the registered all-windows set
LONG = (2014, 2024)                                     # E48b's cell, reproduced first
BAR = 0.30                                              # registered, POSITIVE sign (B15)


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


def boot_ci(df, fn, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        v = fn(df.iloc[rng.choice(idx, size=len(idx), replace=True)])
        if pd.notna(v) and np.isfinite(v):
            out.append(v)
    if len(out) < draws // 4:
        return np.nan, np.nan, np.nan
    a = np.asarray(out)
    return (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)),
            float(2 * min((a <= 0).mean(), (a >= 0).mean())))


def cell(T, a, b, fx, label):
    """One delta->delta cell with the full B6/B9/B10/B12 reporting block."""
    cols = [f"{A}@{a}", f"{A}@{b}", f"{B}@{a}", f"{B}@{b}", f"{HEAD}@{a}", f"{HEAD}@{b}", "pop"]
    sub = T[cols].dropna()
    if len(sub) < 10:
        return None
    d = pd.DataFrame({"x": sub[f"{A}@{b}"] - sub[f"{A}@{a}"],
                      "y": sub[f"{B}@{b}"] - sub[f"{B}@{a}"],
                      "z": sub[f"{HEAD}@{b}"] - sub[f"{HEAD}@{a}"],
                      "w": sub["pop"]})
    rw, n = corr(d["x"], d["y"], d["w"])
    ru, _ = corr(d["x"], d["y"])
    lo, up, pb = boot_ci(d, lambda s: corr(s["x"], s["y"], s["w"])[0])
    g6 = fx.gate_jackknife(d["x"], d["y"], d["w"])
    loo = sorted(((corr(d.drop(i)["x"], d.drop(i)["y"], d.drop(i)["w"])[0] - rw, i)
                  for i in d.index), key=lambda t: -abs(t[0]))[0]
    parts = {}
    for lens, ww in (("w", d["w"]), ("u", None)):
        rxy, _ = corr(d["x"], d["y"], ww)
        rxz, _ = corr(d["x"], d["z"], ww)
        ryz, _ = corr(d["y"], d["z"], ww)
        parts[lens] = (rxy - rxz * ryz) / np.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))
    return {"label": label, "r_w": rw, "r_u": ru, "ci": (lo, up), "p_boot": pb,
            "g6": g6["r_droptop"], "n": n, "neff": kish(d["w"]), "loo": loo,
            "part_w": parts["w"], "part_u": parts["u"],
            "dx": float(np.average(d["x"], weights=d["w"])),
            "dy": float(np.average(d["y"], weights=d["w"]))}


def show(rows):
    print(f"  {'window':16s}{'r_w':>8s}{'[95% CI]':>20s}{'p_boot':>8s}{'G6':>8s}{'r_u':>8s}"
          f"{'n':>5s}{'neff':>7s}  {'wtd dA / dB':>16s}  largest LOO")
    for r in rows:
        ci = f"[{r['ci'][0]:+.3f}, {r['ci'][1]:+.3f}]"
        dd = f"{r['dx']:+.2f} / {r['dy']:+.2f}"
        print(f"  {r['label']:16s}{r['r_w']:>8.3f}{ci:>20s}{r['p_boot']:>8.3f}{r['g6']:>8.3f}"
              f"{r['r_u']:>8.3f}{r['n']:>5d}{r['neff']:>7.1f}  {dd:>16s}  "
              f"{r['loo'][1]} {r['loo'][0]:+.3f}")


def main():
    fx = Findex()
    dev = fx.pan_dev
    d = dev[dev["year"].isin(WAVES)]

    tab = {}
    for c in [A, B, HEAD]:
        w = d.pivot_table(index="countrynewwb", columns="year", values=c) * 100
        for y in WAVES:
            tab[f"{c}@{y}"] = w[y] if y in w.columns else pd.Series(dtype=float)
    T = pd.DataFrame(tab)
    T["pop"] = dev[dev["year"] == 2024].set_index("countrynewwb")["pop_adult"].reindex(T.index)

    print("=" * 130)
    print("E50 — does the fin31d ~ fin34c cash co-retreat hold in EVERY window? "
          "(agenda 7.7; parent E48b; B14 all-windows)")
    print("=" * 130)

    # --------------------------------------------------- B16: path before span
    print("\nB16 — PATH BEFORE SPAN. Weighted developing-panel levels (pp):")
    for c in [A, B, HEAD]:
        s = fx.series(dev, c, WAVES)
        print(f"  {c:10s} " + "  ".join(f"{y}: {s[y]:5.1f}" for y in WAVES if y in s.index))
    print("  NOTE, registered in advance: BOTH cash margins fall for a decade and REBOUND in "
          "2021->24 (agenda 7.8).")
    print("  The rebound sits inside the third window tested below, so that window is the "
          "informative one either way.")

    # --------------------------------------------------- E35 rule: reproduce the parent
    ref = cell(T, *LONG, fx, "2014->2024 E48b")
    print(f"\nE35 RULE — reproduce E48b's published cell before reading anything registered: "
          f"r_w {ref['r_w']:+.3f} (E48b published +0.515), r_u {ref['r_u']:+.3f} "
          f"(published +0.389)")
    assert abs(ref["r_w"] - 0.515) <= 0.02 and abs(ref["r_u"] - 0.389) <= 0.02, "ABORT — no reproduce"
    print("  reproduced within 0.02 — proceeding.")

    # --------------------------------------------------- PRIMARY
    print("\n" + "-" * 130)
    print(f"PRIMARY (registered, B14 all-windows): r(d {A}, d {B}). Bar r >= +{BAR:.2f} on BOTH "
          f"lenses in ALL THREE windows")
    print("-" * 130)
    rows = [cell(T, a, b, fx, f"{a}->{b}") for a, b in WINDOWS]
    rows = [r for r in rows if r]
    show(rows)
    print("  " + "-" * 126)
    show([ref])
    print("  (the last row is E48b's long difference, reproduced — the span, not a fourth window)")

    both = [r for r in rows if r["r_w"] >= BAR and r["r_u"] >= BAR]
    w_only = [r for r in rows if r["r_w"] >= BAR]
    u_only = [r for r in rows if r["r_u"] >= BAR]
    wrong_sign = [r for r in rows if min(r["r_w"], r["r_u"]) <= -BAR]
    print(f"\n  windows clearing +{BAR:.2f} on BOTH lenses: {len(both)}/{len(rows)} "
          f"({', '.join(r['label'] for r in both) if both else 'none'})")
    print(f"  weighted lens alone:   {len(w_only)}/{len(rows)} "
          f"({', '.join(r['label'] for r in w_only) if w_only else 'none'})")
    print(f"  unweighted lens alone: {len(u_only)}/{len(rows)} "
          f"({', '.join(r['label'] for r in u_only) if u_only else 'none'})")
    print(f"  B15 WRONG-SIGN windows (r <= -{BAR:.2f} on a lens): "
          f"{', '.join(r['label'] for r in wrong_sign) if wrong_sign else 'none'}")

    all_pass = len(both) == len(rows)
    lens_split = (len(w_only) == len(rows)) and (len(u_only) < len(rows))

    # --------------------------------------------------- SECONDARY
    print("\n" + "-" * 130)
    print(f"SECONDARY (registered, no bar, diagnostic) — partial controlling for d {HEAD}, "
          f"per window, both lenses")
    print("-" * 130)
    print(f"  {'window':16s}{'r_w':>9s}{'partial_w':>12s}{'r_u':>9s}{'partial_u':>12s}")
    for r in rows + [ref]:
        print(f"  {r['label']:16s}{r['r_w']:>9.3f}{r['part_w']:>12.3f}"
              f"{r['r_u']:>9.3f}{r['part_u']:>12.3f}")
    print("  (E48b's long-difference partial: +0.597 weighted / +0.383 unweighted — it STRENGTHENED "
          "over the span)")

    # --------------------------------------------------- VERDICT
    print("\n" + "=" * 130)
    print("E50 VERDICT (pre-registered)")
    if all_pass:
        print(f"  ALL {len(rows)}/{len(rows)} windows clear +{BAR:.2f} on both lenses "
              f"-> E48b PROMOTED to `keep-general` (B4 + B8)")
        verdict = "keep-general"
    elif lens_split:
        print(f"  LENS SPLIT: weighted {len(w_only)}/{len(rows)}, unweighted "
              f"{len(u_only)}/{len(rows)} -> promotion is `discard-weighted`; "
              f"E48b STAYS `keep-window`")
        verdict = "discard-weighted"
    else:
        print(f"  {len(both)}/{len(rows)} windows clear the bar on both lenses -> promotion FAILS; "
              f"E48b STAYS `keep-window` and is recorded as having FAILED its promotion test")
        verdict = "discard"
    print("  Registered null reading (written before the answer): a failure means the decade-long "
          "co-retreat is")
    print("  a SPAN fact, not a per-window one — the two margins end the decade having moved "
          "together without")
    print("  having moved together in any particular window. That is the same distinction E39's "
          "repeat-mover null")
    print("  and E48's primary both turn on, and it is not a rehabilitation of the digital "
          "headline either way.")
    print("=" * 130)
    return verdict


if __name__ == "__main__":
    main()
