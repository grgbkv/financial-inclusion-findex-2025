"""E44 (pre-registered 2026-08-15): did EARLIER growth episodes also reach every demographic slice?

Program 3, item 3.9 — the B4/B8 promotion test for E43. Parent: **E43** (first descendant).

B2 CELL FOR THIS CYCLE (E44's half): the `pan_grp` slice frames have never been used on any wave
transition other than 2021->2024. This runs them on 2011->14, 2014->17 and 2017->21.

WHY. E43's primary is `keep-window`: in 2021->24 the formal-saving surge reached every disadvantaged
half. Under B4 that is a window claim until replicated, and under B8 promotion requires EVERY tested
earlier window to agree. This is its only route to `keep-general`.

DECLARED BEFORE THE RUN. E39 established that 2021->24 is the largest within-country formal-saving
episode of the four transitions (42.1% of economies >= +10pp, all adults, against a 20.8% previous
best). E43's bar (b) may therefore fail in earlier windows on MAGNITUDE alone, saying nothing about
BREADTH. Both statistics are registered up front so the distinction cannot be drawn after the fact.

P1 — the mechanical B4/B8 replication (this decides the promotion). E43's bars verbatim:
  (a) disadvantaged group's population-weighted delta >= +5.0pp
  (b) unweighted share of economies with disadvantaged delta >= +10pp is >= 25%
  dimension passes if both; window passes if >= 4 of 5 dimensions pass.
  PROMOTE E43 to `keep-general` only if ALL THREE earlier windows pass. Per the E35 rule, 2021->24 is
  recomputed inside this file and must reproduce E43's table within 0.1pp before anything else is read.

P2 — the scale-relative claim, a separate keep. "When formal saving grows in a window, it grows for
  the disadvantaged half roughly in proportion to the advantaged half." Reach ratio = (disadvantaged
  weighted delta) / (advantaged weighted delta), computed ONLY where the advantaged delta >= +2.0pp
  (declared now; excluded cells are printed). KEEP if the ratio is >= 0.75 in >= 4 of 5 dimensions in
  EVERY qualifying window.

B6/B9/B12: 2,000-draw country bootstrap (economies resampled carrying all their subgroup rows);
country-level Kish neff per E37's rule (i); the unweighted twin beside every weighted statistic; and
the largest single leave-one-economy-out effect on each window's headline weighted delta, with the
economy NAMED (B12).

DECLARED. A distributional description, not an association — the 0.30 threshold does not apply. No
gap statistic is registered: E43's pp-gap secondary died on its log-odds twin, so this experiment
asks about REACH (each group's own delta, and their ratio), which is scale-relative by construction.
Nothing here is causal, and a group's delta is a change in a cross-sectional rate, not a change
experienced by the same individuals.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 44
BIG_MOVE = 10.0        # E43/E39 "large gain" bar, pp
BAR_A = 5.0            # disadvantaged pop-weighted delta, pp
BAR_B = 25.0           # unweighted share of economies with disadvantaged delta >= +10pp, %
N_DIMS_REQUIRED = 4    # of 5
RATIO_BAR = 0.75       # P2 reach ratio
RATIO_MIN_ADV = 2.0    # advantaged delta floor for a meaningful ratio, pp

SAV = "fin17a_17a1_d"
WINDOWS = [(2011, 2014), (2014, 2017), (2017, 2021), (2021, 2024)]
ORIGINAL = (2021, 2024)

# disadvantaged group named FIRST (E43's declaration, unchanged)
DIMS = {
    "gender":     ("women", "men"),
    "income":     ("poorest 40%", "richest 60%"),
    "education":  ("prim edu or less", "secondary edu or more"),
    "age_cat":    ("ages 15-24", "age 25+"),
    "laborforce": ("out of laborforce", "in laborforce"),
}

# E43's published 2021->24 primary table, for the E35 in-file reproduction check
E43_WD_DIS = {"gender": 12.79, "income": 10.84, "education": 11.57,
              "age_cat": 16.02, "laborforce": 7.40}
E43_SH_DIS = {"gender": 47.3, "income": 32.7, "education": 29.1,
              "age_cat": 56.4, "laborforce": 31.5}


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def slice_panel(fx, dim, col, window):
    """Per-economy table: both groups' levels at both waves, deltas, and the country weight."""
    dis, adv = DIMS[dim]
    g = fx.pan_grp
    d = g[(g["incomegroupwb24"] != "High income") & (g["group"] == dim)
          & (g["year"].isin(window))]
    wide = d.pivot_table(index="countrynewwb", columns=["year", "group2"], values=col) * 100
    need = [(window[0], dis), (window[0], adv), (window[1], dis), (window[1], adv)]
    if any(c not in wide.columns for c in need):
        return pd.DataFrame()
    out = pd.DataFrame({
        "d_dis": wide[(window[1], dis)] - wide[(window[0], dis)],
        "d_adv": wide[(window[1], adv)] - wide[(window[0], adv)],
    }).dropna()
    pop = g[(g["year"] == 2024) & (g["group"] == "all")].set_index("countrynewwb")["pop_adult"]
    out["pop"] = pop.reindex(out.index)
    return out.dropna(subset=["pop"])


def slice_levels(fx, dim, col, window):
    """EXPLORATORY diagnostic support: the same table but carrying LEVELS, for the log-odds twin."""
    dis, adv = DIMS[dim]
    g = fx.pan_grp
    d = g[(g["incomegroupwb24"] != "High income") & (g["group"] == dim)
          & (g["year"].isin(window))]
    wide = d.pivot_table(index="countrynewwb", columns=["year", "group2"], values=col) * 100
    need = [(window[0], dis), (window[0], adv), (window[1], dis), (window[1], adv)]
    if any(c not in wide.columns for c in need):
        return pd.DataFrame()
    lo = lambda s: np.log(np.clip(s, 0.5, 99.5) / (100 - np.clip(s, 0.5, 99.5)))
    out = pd.DataFrame({
        "lo_dis": lo(wide[(window[1], dis)]) - lo(wide[(window[0], dis)]),
        "lo_adv": lo(wide[(window[1], adv)]) - lo(wide[(window[0], adv)]),
    }).dropna()
    pop = g[(g["year"] == 2024) & (g["group"] == "all")].set_index("countrynewwb")["pop_adult"]
    out["pop"] = pop.reindex(out.index)
    return out.dropna(subset=["pop"])


def wmean(df, col):
    return float(np.average(df[col], weights=df["pop"]))


def boot_stat(df, fn, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        v = fn(df.iloc[rng.choice(idx, size=len(idx), replace=True)])
        if pd.notna(v) and np.isfinite(v):
            out.append(v)
    a = np.asarray(out)
    return float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5))


def loo_named(df, col):
    """B12: largest single leave-one-economy-out effect on a weighted mean, and the economy."""
    full = wmean(df, col)
    best, who = 0.0, None
    for c in df.index:
        v = wmean(df.drop(index=c), col)
        if abs(v - full) > abs(best):
            best, who = v - full, c
    return full, best, who


def window_table(fx, window):
    rows = []
    for dim in DIMS:
        t = slice_panel(fx, dim, SAV, window)
        if t.empty or len(t) < 10:
            rows.append({"dim": dim, "n": len(t), "empty": True})
            continue
        wd_dis, wd_adv = wmean(t, "d_dis"), wmean(t, "d_adv")
        sh_dis = float((t["d_dis"] >= BIG_MOVE).mean() * 100)
        sh_adv = float((t["d_adv"] >= BIG_MOVE).mean() * 100)
        lo_a, hi_a = boot_stat(t, lambda d: wmean(d, "d_dis"))
        lo_b, hi_b = boot_stat(t, lambda d: (d["d_dis"] >= BIG_MOVE).mean() * 100)
        a_ok, b_ok = wd_dis >= BAR_A, sh_dis >= BAR_B
        ratio = wd_dis / wd_adv if wd_adv >= RATIO_MIN_ADV else np.nan
        lo_r, hi_r = ((np.nan, np.nan) if pd.isna(ratio) else
                      boot_stat(t, lambda d: (wmean(d, "d_dis") / wmean(d, "d_adv")
                                              if wmean(d, "d_adv") >= RATIO_MIN_ADV else np.nan)))
        rows.append({
            "dim": dim, "n": len(t), "neff": _kish(t["pop"]), "empty": False,
            "wd_dis": wd_dis, "wd_adv": wd_adv, "ci_a": (lo_a, hi_a),
            "sh_dis": sh_dis, "sh_adv": sh_adv, "ci_b": (lo_b, hi_b),
            "a_ok": a_ok, "b_ok": b_ok, "both": a_ok and b_ok,
            "u_dis": float(t["d_dis"].median()), "u_adv": float(t["d_adv"].median()),
            "ratio": ratio, "ci_r": (lo_r, hi_r),
            "u_ratio": (float(t["d_dis"].median() / t["d_adv"].median())
                        if t["d_adv"].median() >= RATIO_MIN_ADV else np.nan),
            "sh_dis_ge_adv": float((t["d_dis"] >= t["d_adv"]).mean() * 100),
            "tab": t,
        })
    return rows


def print_window(window, rows):
    print(f"\n{'-' * 122}")
    print(f"WINDOW {window[0]}->{window[1]}")
    print(f"  {'dimension':11s} {'disadvantaged':21s} {'n':>3s} {'neff':>5s} "
          f"{'wtdD_dis':>9s} {'[95% CI]':>17s} {'wtdD_adv':>9s} "
          f"{'>=10pp dis':>10s} {'[95% CI]':>15s} {'>=10pp adv':>10s}  bars")
    for r in rows:
        if r["empty"]:
            print(f"  {r['dim']:11s} {DIMS[r['dim']][0]:21s} {r['n']:3d}   —  insufficient cells")
            continue
        print(f"  {r['dim']:11s} {DIMS[r['dim']][0]:21s} {r['n']:3d} {r['neff']:5.1f} "
              f"{r['wd_dis']:+9.2f} [{r['ci_a'][0]:+6.2f},{r['ci_a'][1]:+6.2f}] {r['wd_adv']:+9.2f} "
              f"{r['sh_dis']:9.1f}% [{r['ci_b'][0]:5.1f},{r['ci_b'][1]:5.1f}] {r['sh_adv']:9.1f}%  "
              f"a={'Y' if r['a_ok'] else 'N'} b={'Y' if r['b_ok'] else 'N'}")
    print("  unweighted median delta (typical economy), dis vs adv:  " + "   ".join(
        f"{r['dim']}: {r['u_dis']:+.2f}/{r['u_adv']:+.2f}" for r in rows if not r["empty"]))
    ok = [r for r in rows if not r["empty"]]
    n_pass = sum(r["both"] for r in ok)
    print(f"  WINDOW VERDICT: {n_pass}/{len(ok)} dimensions clear both bars "
          f"(required {N_DIMS_REQUIRED}) -> {'PASS' if n_pass >= N_DIMS_REQUIRED else 'FAIL'}")
    return n_pass >= N_DIMS_REQUIRED, n_pass, ok


def run(fx: Findex):
    print("=" * 122)
    print("E44 — did earlier growth episodes also reach every demographic slice? "
          "(pan_grp x three untouched transitions; parent E43, agenda 3.9)")
    print("=" * 122)
    print(f"outcome {SAV}, developing panel economies, five slice dimensions")
    print(f"P1 bars (E43 verbatim): (a) disadvantaged wtd delta >= +{BAR_A}pp   "
          f"(b) share of economies with disadvantaged delta >= +{BIG_MOVE}pp is >= {BAR_B}%; "
          f"window passes at >= {N_DIMS_REQUIRED}/5")
    print(f"P2 bar: reach ratio (wtd dis / wtd adv) >= {RATIO_BAR} in >= {N_DIMS_REQUIRED}/5 dims in "
          f"EVERY window where wtd adv delta >= +{RATIO_MIN_ADV}pp")

    results = {}
    for w in WINDOWS:
        rows = window_table(fx, w)
        passed, n_pass, ok = print_window(w, rows)
        results[w] = {"passed": passed, "n_pass": n_pass, "rows": ok}

    # ---------------------------------------------------- E35 rule: reproduce the original window
    print("\n" + "=" * 122)
    print("E35 RULE — in-file reproduction of E43's original 2021->24 window (must match within 0.1pp)")
    devs = []
    for r in results[ORIGINAL]["rows"]:
        d1 = abs(r["wd_dis"] - E43_WD_DIS[r["dim"]])
        d2 = abs(r["sh_dis"] - E43_SH_DIS[r["dim"]])
        devs += [d1, d2]
        print(f"  {r['dim']:11s} wtdD_dis {r['wd_dis']:+7.2f} vs E43 {E43_WD_DIS[r['dim']]:+7.2f} "
              f"(dev {d1:.3f})   share {r['sh_dis']:5.1f}% vs E43 {E43_SH_DIS[r['dim']]:5.1f}% "
              f"(dev {d2:.3f})")
    repro = max(devs) <= 0.1
    print(f"  reproduction: {'OK' if repro else 'FAILED'} (max deviation {max(devs):.3f}pp) — "
          f"{'earlier windows may be read' if repro else 'STOP, the join is defective'}")

    # ---------------------------------------------------- P1 verdict
    print("\n" + "=" * 122)
    print("P1 — the B4/B8 promotion test for E43")
    earlier = [w for w in WINDOWS if w != ORIGINAL]
    for w in earlier:
        print(f"  {w[0]}->{w[1]}: {results[w]['n_pass']}/5 dims -> "
              f"{'PASS' if results[w]['passed'] else 'FAIL'}")
    promote = repro and all(results[w]["passed"] for w in earlier)
    verdict1 = ("PROMOTE E43 to keep-general" if promote else
                "E43 STAYS keep-window — promotion test FAILED "
                "(recorded as a failure, not as not-attempted)")
    print(f"  P1 VERDICT: {verdict1}")

    # ---------------------------------------------------- P2 verdict: the reach ratio
    print("\n" + "=" * 122)
    print("P2 — the reach ratio: does growth reach the disadvantaged half in proportion?")
    print(f"  {'window':12s} {'dimension':11s} {'wtdD_dis':>9s} {'wtdD_adv':>9s} {'ratio':>7s} "
          f"{'[95% CI]':>17s} {'unwtd ratio':>11s} {'econ dis>=adv':>13s}  bar")
    qualifying = []
    for w in WINDOWS:
        ok_dims = 0
        usable = 0
        for r in results[w]["rows"]:
            if pd.isna(r["ratio"]):
                print(f"  {w[0]}->{w[1]:<7d} {r['dim']:11s} {r['wd_dis']:+9.2f} {r['wd_adv']:+9.2f} "
                      f"{'—':>7s} {'excluded: adv delta < +' + str(RATIO_MIN_ADV) + 'pp':>17s}")
                continue
            usable += 1
            hit = r["ratio"] >= RATIO_BAR
            ok_dims += hit
            print(f"  {w[0]}->{w[1]:<7d} {r['dim']:11s} {r['wd_dis']:+9.2f} {r['wd_adv']:+9.2f} "
                  f"{r['ratio']:7.3f} [{r['ci_r'][0]:7.3f},{r['ci_r'][1]:7.3f}] "
                  f"{r['u_ratio']:11.3f} {r['sh_dis_ge_adv']:12.1f}%  {'Y' if hit else 'N'}")
        if usable:
            qualifying.append((w, ok_dims, usable))
        print()
    p2 = bool(qualifying) and all(k >= N_DIMS_REQUIRED for _, k, _ in qualifying)
    for w, k, u in qualifying:
        print(f"  {w[0]}->{w[1]}: {k}/{u} usable dimensions at ratio >= {RATIO_BAR}")
    print(f"  P2 VERDICT: {'KEEP' if p2 else 'DISCARD'} "
          f"(required >= {N_DIMS_REQUIRED} of 5 in every qualifying window)")

    # ---------------------------------------------------- B12 leave-one-out, by name
    print("\n" + "=" * 122)
    print("B12 — largest single leave-one-economy-out effect on each window's headline weighted "
          "delta (income slice, disadvantaged half)")
    for w in WINDOWS:
        r = next((x for x in results[w]["rows"] if x["dim"] == "income"), None)
        if r is None:
            continue
        full, delta, who = loo_named(r["tab"], "d_dis")
        print(f"  {w[0]}->{w[1]}: wtd delta {full:+6.2f}pp   largest drop = {who} "
              f"({delta:+.2f}pp -> {full + delta:+.2f}pp)   n={r['n']}  neff={r['neff']:.1f}")

    # ---------------------------------------------------- exploratory: the log-odds reach twin
    print("\n" + "=" * 122)
    print("EXPLORATORY DIAGNOSTIC (unregistered, peek rule — no keep hangs on it): the log-odds twin")
    print("  a pp delta is baseline-dependent: under EQUAL proportional (log-odds) growth, a group")
    print("  starting lower gains FEWER pp while both are under 50%. P2's ratio bar inherits that.")
    print(f"  {'window':12s} {'dimension':11s} {'wtdLO_dis':>9s} {'wtdLO_adv':>9s} {'LO ratio':>9s} "
          f"{'unwtd LO ratio':>14s} {'econ dis>=adv':>13s}")
    for w in WINDOWS:
        for dim in DIMS:
            t = slice_levels(fx, dim, SAV, w)
            if t.empty or len(t) < 10:
                continue
            a, b = wmean(t, "lo_dis"), wmean(t, "lo_adv")
            ua, ub = float(t["lo_dis"].median()), float(t["lo_adv"].median())
            rr = a / b if abs(b) > 0.05 else np.nan
            ur = ua / ub if abs(ub) > 0.05 else np.nan
            sh = float((t["lo_dis"] >= t["lo_adv"]).mean() * 100)
            print(f"  {w[0]}->{w[1]:<7d} {dim:11s} {a:+9.3f} {b:+9.3f} "
                  f"{rr:9.3f} {ur:14.3f} {sh:12.1f}%")
        print()

    print("\n" + "=" * 122)
    print(f"SUMMARY  P1 {'PROMOTE' if promote else 'FAIL (E43 stays keep-window)'}  |  "
          f"P2 {'KEEP' if p2 else 'DISCARD'}  |  reproduction {'OK' if repro else 'FAILED'}")
    print("=" * 122)


if __name__ == "__main__":
    run(Findex())
