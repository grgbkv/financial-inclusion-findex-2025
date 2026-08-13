"""E43 (pre-registered 2026-08-13): did the 2021-24 formal-saving surge reach EVERY demographic
slice, or only the advantaged half?

Program 3, item 3.6. Parent: **E39** (the balance-sheet reframing) — second descendant after E41,
inside rule B3's cap.

B2 BREADTH CELL FOR THIS CYCLE: the `pan_grp` slice frames. Four of the five usable dimensions sit
at <=1 ledger mention (education 1, age_cat 1, laborforce 1, gender ~1). `urbanicity` is EXCLUDED,
not skipped: it exists for 2024 only and admits no delta.

WHY. E39 established that 2021->24 is a within-country balance-sheet episode — 42.1% of developing
panel economies gained >= +10pp in formal saving against a 20.8% previous best. That is the loop's
largest surviving finding and it is entirely a `group == "all"` statement. Whether the episode
reached the poor, the unschooled, the young and the out-of-workforce is a different question.

OUTCOME: `fin17a_17a1_d` (formal saving — the E39/E1/E10/E12 headline), delta 2021->2024.

PRIMARY STATISTIC, chosen under E31's lesson (population-weighted slice means are dominated by a
handful of economies while a minority of economies move with them): the UNWEIGHTED SHARE OF
ECONOMIES meeting each bar. The population-weighted mean is secondary.

REGISTERED KEEP CLAIM — the surge was broad-based. Per dimension, two bars:
  (a) the DISADVANTAGED group's population-weighted delta >= +5.0pp; and
  (b) the unweighted share of economies where the disadvantaged group gained >= +10pp is >= 25%.
KEEP if both hold in >= 4 of the 5 dimensions; DISCARD otherwise, naming the failures.

SECONDARY, registered and reported either way: did the episode widen or narrow within-country gaps?
Per dimension, the unweighted share of economies where the (advantaged - disadvantaged) pp gap
NARROWED, against a 50% coin-flip reference, plus the population-weighted gap change with G6.

WEIGHT DECLARATION. `pop_adult` on a subgroup row is the COUNTRY's adult population, not the
subgroup's (verified before the run), so "population-weighted" here means each country's subgroup
delta weighted by that country's adult population. That is the only weight the frame carries and it
is the same weight the rest of the ledger uses; stated so it is not read as a subgroup-population
weighting.

B6: 2,000-draw country bootstrap (economies resampled with all their subgroup rows) for every
reported share and weighted mean; Kish neff on the COUNTRY-level weights per E37's rule (i).

DECLARED. A distributional description of one window across five slices, not an association — the
0.30 correlation threshold does not apply and is not used. Under B4 this is a `keep-window` claim at
best. Nothing here is causal, and a group's delta is a change in a cross-sectional rate, not a change
experienced by the same individuals.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 43
BIG_MOVE = 10.0        # E39's "large gain" bar, in pp
BAR_A = 5.0            # disadvantaged group's pop-weighted delta, pp
BAR_B = 25.0           # unweighted share of economies with disadvantaged delta >= +10pp, %
N_DIMS_REQUIRED = 4    # of 5

SAV = "fin17a_17a1_d"
WINDOW = (2021, 2024)

# disadvantaged group named FIRST, before the run
DIMS = {
    "gender":     ("women", "men"),
    "income":     ("poorest 40%", "richest 60%"),
    "education":  ("prim edu or less", "secondary edu or more"),
    "age_cat":    ("ages 15-24", "age 25+"),
    "laborforce": ("out of laborforce", "in laborforce"),
}


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def slice_panel(fx, dim, col, window):
    """Per-economy table: disadvantaged/advantaged levels at both waves, deltas, gaps, weight."""
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
        "gap0": wide[(window[0], adv)] - wide[(window[0], dis)],
        "gap1": wide[(window[1], adv)] - wide[(window[1], dis)],
    }).dropna()
    pop = g[(g["year"] == 2024) & (g["group"] == "all")].set_index("countrynewwb")["pop_adult"]
    out["pop"] = pop.reindex(out.index)
    return out.dropna(subset=["pop"])


def boot_stat(df, fn, draws=BOOT, seed=SEED):
    """Country bootstrap percentile interval for any statistic of the per-economy table."""
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        v = fn(df.iloc[rng.choice(idx, size=len(idx), replace=True)])
        if pd.notna(v):
            out.append(v)
    a = np.asarray(out)
    return float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5))


def wmean(df, col):
    return float(np.average(df[col], weights=df["pop"]))


def run(fx: Findex):
    print("=" * 116)
    print("E43 — did the 2021-24 formal-saving surge reach every demographic slice? "
          "(pan_grp, the cycle's B2 cell; parent E39)")
    print("=" * 116)
    print(f"outcome {SAV}, window {WINDOW[0]}->{WINDOW[1]}, developing panel economies")
    print(f"BARS: (a) disadvantaged pop-weighted delta >= +{BAR_A}pp   "
          f"(b) share of economies with disadvantaged delta >= +{BIG_MOVE}pp is >= {BAR_B}%")
    print(f"KEEP if both hold in >= {N_DIMS_REQUIRED} of 5 dimensions\n")

    rows, sec = [], []
    for dim in DIMS:
        dis, adv = DIMS[dim]
        t = slice_panel(fx, dim, SAV, WINDOW)
        if t.empty:
            print(f"  {dim}: no usable cells"); continue

        wd_dis, wd_adv = wmean(t, "d_dis"), wmean(t, "d_adv")
        sh_dis = float((t["d_dis"] >= BIG_MOVE).mean() * 100)
        sh_adv = float((t["d_adv"] >= BIG_MOVE).mean() * 100)
        lo_a, hi_a = boot_stat(t, lambda d: wmean(d, "d_dis"))
        lo_b, hi_b = boot_stat(t, lambda d: (d["d_dis"] >= BIG_MOVE).mean() * 100)

        a_ok, b_ok = wd_dis >= BAR_A, sh_dis >= BAR_B
        rows.append({"dim": dim, "n": len(t), "neff": _kish(t["pop"]),
                     "wd_dis": wd_dis, "wd_adv": wd_adv, "sh_dis": sh_dis, "sh_adv": sh_adv,
                     "ci_a": (lo_a, hi_a), "ci_b": (lo_b, hi_b),
                     "a_ok": a_ok, "b_ok": b_ok, "both": a_ok and b_ok,
                     "med_dis": float(t["d_dis"].median()), "med_adv": float(t["d_adv"].median())})

        # ---- secondary: did the within-country gap narrow?
        narrowed = float((t["gap1"] < t["gap0"]).mean() * 100)
        lo_n, hi_n = boot_stat(t, lambda d: (d["gap1"] < d["gap0"]).mean() * 100)
        wgap0, wgap1 = wmean(t, "gap0"), wmean(t, "gap1")
        big = t.nlargest(5, "pop").index
        s = t.drop(index=big)
        sec.append({"dim": dim, "narrowed": narrowed, "ci": (lo_n, hi_n),
                    "wgap0": wgap0, "wgap1": wgap1, "wgap_d": wgap1 - wgap0,
                    "g6_gap_d": wmean(s, "gap1") - wmean(s, "gap0"),
                    "u_gap_d": float((t["gap1"] - t["gap0"]).mean())})

    print("PRIMARY — the disadvantaged half's own surge")
    print(f"  {'dimension':11s} {'disadvantaged':21s} {'n':>3s} {'neff':>5s} "
          f"{'wtdD_dis':>9s} {'[95% CI]':>18s} {'wtdD_adv':>9s} "
          f"{'>=10pp dis':>10s} {'[95% CI]':>16s} {'>=10pp adv':>10s}  bars")
    for r in rows:
        print(f"  {r['dim']:11s} {DIMS[r['dim']][0]:21s} {r['n']:3d} {r['neff']:5.1f} "
              f"{r['wd_dis']:+9.2f} [{r['ci_a'][0]:+6.2f},{r['ci_a'][1]:+6.2f}] {r['wd_adv']:+9.2f} "
              f"{r['sh_dis']:9.1f}% [{r['ci_b'][0]:5.1f},{r['ci_b'][1]:5.1f}] {r['sh_adv']:9.1f}%  "
              f"a={'Y' if r['a_ok'] else 'N'} b={'Y' if r['b_ok'] else 'N'}")

    print("\n  unweighted median delta (typical economy), disadvantaged vs advantaged:")
    for r in rows:
        print(f"    {r['dim']:11s} {r['med_dis']:+6.2f}pp   vs {r['med_adv']:+6.2f}pp")

    n_pass = sum(r["both"] for r in rows)
    keep = n_pass >= N_DIMS_REQUIRED
    print(f"\n  PRIMARY VERDICT: {'KEEP' if keep else 'DISCARD'} — {n_pass}/5 dimensions clear both "
          f"bars (required {N_DIMS_REQUIRED})")
    fails = [r["dim"] for r in rows if not r["both"]]
    if fails:
        print(f"  dimensions failing at least one bar: {', '.join(fails)}")

    print("\n" + "-" * 116)
    print("SECONDARY (registered, no keep hangs on it) — did the episode widen or narrow gaps?")
    print(f"  {'dimension':11s} {'narrowed':>9s} {'[95% CI]':>16s} {'wtd gap 2021':>13s} "
          f"{'wtd gap 2024':>13s} {'wtd change':>11s} {'G6 change':>10s} {'unwtd change':>13s}")
    for s in sec:
        print(f"  {s['dim']:11s} {s['narrowed']:8.1f}% [{s['ci'][0]:5.1f},{s['ci'][1]:5.1f}] "
              f"{s['wgap0']:13.2f} {s['wgap1']:13.2f} {s['wgap_d']:+11.2f} {s['g6_gap_d']:+10.2f} "
              f"{s['u_gap_d']:+13.2f}")
    print("\n  (a share whose CI straddles 50% is a coin flip; a weighted change whose G6 twin "
          "reverses sign is a big-country artifact — E31's and E36's lesson)")

    print("\n" + "=" * 116)
    print(f"SUMMARY  primary {'KEEP' if keep else 'DISCARD'} ({n_pass}/5)  |  "
          f"E39's all-adults reference: 42.1% of economies >= +10pp")
    print("=" * 116)


if __name__ == "__main__":
    run(Findex())
