"""U27 (registered 2026-08-23) — agenda item 4.6: is the SOURCE of emergency funds
education-graded, and does account holding absorb that gradient?

Parent U24. Stream micro. Design micro-cross-section, 2024, SINGLE WAVE — cross-sectional
description, no trend language. Sample: the 98-economy emergency-fund module set U24x opened,
`fin24` (main source) over its own non-missing denominator, DK/RF codes 8/9 excluded.

REGISTERED SIGNS (B15), gap = share(educ >= 2) - share(educ == 1) in pp:
    code 1 savings          POSITIVE   (the balance-sheet prediction)
    code 2 family/friends   NEGATIVE
    code 5 selling assets   NEGATIVE
    code 7 not possible     NEGATIVE
    codes 3 (working) and 4 (borrowing): NO SIGN PREDICTED — descriptive only, cannot count
    toward the keep.

REGISTERED KEEP: all four directional signs correct AND savings gap >= +5pp AND family/friends
gap <= -5pp. Signs correct with magnitudes under 5pp is a DISCARD as registered.

SECONDARY 1 (no bar): absorption = 1 - (account-conditional savings gap / unconditional savings
gap), beside U24's 56.9% (usage) and 8.6% (welfare).
SECONDARY 2 (no bar): the same composition split poorest 40% (inc_q in {1,2}) vs richest 60%.
SECONDARY 3 (no bar): within-country — share of qualifying economies with a positive savings gap,
and the median economy gap.
Inference: 2,000-draw ECONOMY-CLUSTER percentile bootstrap on every gap and on absorption; Kish
neff of the pooled respondent weights beside the nominal respondent count. Pooled-weighting caveat
(HARNESS_V2_NOTES item 3) carried: pooled `wgt` weights economies roughly equally.
"""
import numpy as np
import pandas as pd

from micro import Micro

SOURCES = {1: "savings", 2: "family/friends", 3: "money from working", 4: "borrowing",
           5: "selling assets", 6: "other", 7: "not possible"}
REGISTERED_SIGN = {1: +1, 2: -1, 5: -1, 7: -1}       # 3, 4, 6 carry no registered sign
HEADLINE_BAR = 5.0
DRAWS = 2000
RNG = np.random.default_rng(20260823)


def wshare(sub, code):
    """weighted share (pp) of fin24 == code within `sub`."""
    if len(sub) == 0 or sub["wgt"].sum() == 0:
        return np.nan
    return 100 * np.average(sub["fin24"].eq(code).astype(float), weights=sub["wgt"])


def gaps(sub, hi_mask, lo_mask, codes):
    hi, lo = sub[hi_mask], sub[lo_mask]
    return {c: wshare(hi, c) - wshare(lo, c) for c in codes}


def cluster_boot(sub, hi_col, lo_col, codes, draws=DRAWS):
    """percentile bootstrap over ECONOMIES (respondents are clustered inside economies;
    a respondent-level resample would understate the interval — U23's rule)."""
    econs = sub["economy"].unique()
    by = {e: g for e, g in sub.groupby("economy")}
    out = {c: [] for c in codes}
    for _ in range(draws):
        take = RNG.choice(len(econs), len(econs), replace=True)
        d = pd.concat([by[econs[i]] for i in take])
        hi, lo = d[d[hi_col]], d[d[lo_col]]
        for c in codes:
            out[c].append(wshare(hi, c) - wshare(lo, c))
    return {c: (float(np.nanpercentile(out[c], 2.5)), float(np.nanpercentile(out[c], 97.5)))
            for c in codes}


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def composition(sub, mask, label):
    print("  %-22s n=%6d  " % (label, int(mask.sum())) + "  ".join(
        "%s %5.1f%%" % (SOURCES[c][:12], wshare(sub[mask], c)) for c in sorted(SOURCES)))


def main():
    mi = Micro()
    df = mi.df
    sub = df[df["fin24"].isin(list(SOURCES))].dropna(subset=["wgt"]).copy()
    sub["hi_ed"] = sub["educ"] >= 2
    sub["lo_ed"] = sub["educ"] == 1
    sub["hi_inc"] = sub["inc_q"].isin([3, 4, 5])
    sub["lo_inc"] = sub["inc_q"].isin([1, 2])

    print("=" * 100)
    print("U27 — agenda item 4.6: the SOURCE of emergency funds, education-graded? (parent U24)")
    print("=" * 100)
    print("sample: fin24 in 1..7 (DK/RF 8/9 dropped) — %d respondents, %d economies"
          % (len(sub), sub["economy"].nunique()))
    print("Kish neff of the pooled respondent weights: %.0f against a nominal n of %d"
          % (kish(sub["wgt"]), len(sub)))
    print("pooled composition (weighted, all respondents):")
    composition(sub, pd.Series(True, index=sub.index), "ALL")
    composition(sub, sub["hi_ed"], "educ >= 2 (sec+)")
    composition(sub, sub["lo_ed"], "educ == 1 (prim-)")

    # ---------------------------------------------------------------- PRIMARY
    codes = sorted(SOURCES)
    g = gaps(sub, sub["hi_ed"], sub["lo_ed"], codes)
    ci = cluster_boot(sub, "hi_ed", "lo_ed", codes)
    n_hi, n_lo = int(sub["hi_ed"].sum()), int(sub["lo_ed"].sum())
    print("\n" + "-" * 100)
    print("PRIMARY — education gap per source, gap = share(educ>=2) - share(educ==1), pp")
    print("M2: n(educ>=2) = %d, n(educ==1) = %d — both cells >> 100" % (n_hi, n_lo))
    print("%-20s %9s %9s %9s  %-22s %10s %s"
          % ("source", "hi", "lo", "gap", "bootstrap CI (2,000)", "reg. sign", "verdict"))
    ok_signs = True
    for c in codes:
        hi, lo = wshare(sub[sub["hi_ed"]], c), wshare(sub[sub["lo_ed"]], c)
        rs = REGISTERED_SIGN.get(c)
        if rs is None:
            v = "no sign registered"
        else:
            good = np.sign(g[c]) == rs
            ok_signs &= bool(good)
            v = "sign OK" if good else "SIGN WRONG"
        print("%-20s %+9.2f %+9.2f %+9.2f  [%+6.2f, %+6.2f]      %-9s %s"
              % (SOURCES[c], hi, lo, g[c], ci[c][0], ci[c][1],
                 {1: "POS", -1: "NEG"}.get(rs, "—"), v))

    sav, fam = g[1], g[2]
    bar_sav, bar_fam = sav >= HEADLINE_BAR, fam <= -HEADLINE_BAR
    print("\nREGISTERED KEEP CONDITION:")
    print("  (i)   savings gap %+.2fpp >= +5.0        -> %s" % (sav, "PASS" if bar_sav else "FAIL"))
    print("  (ii)  family/friends gap %+.2fpp <= -5.0 -> %s" % (fam, "PASS" if bar_fam else "FAIL"))
    print("  (iii) all four registered signs correct  -> %s" % ("PASS" if ok_signs else "FAIL"))
    print("  VERDICT: %s" % ("KEEP" if (bar_sav and bar_fam and ok_signs)
                             else "DISCARD as registered"))

    # ------------------------------------------------- SECONDARY 1: absorption
    print("\n" + "-" * 100)
    print("SECONDARY 1 (no bar) — does account holding absorb the savings-source gradient?")
    acc = sub[sub["account"] == 1]
    g_c = gaps(acc, acc["hi_ed"], acc["lo_ed"], [1, 2, 7])
    ci_c = cluster_boot(acc, "hi_ed", "lo_ed", [1, 2, 7])
    print("  M2: n(acc & educ>=2) = %d, n(acc & educ==1) = %d"
          % (int(acc["hi_ed"].sum()), int(acc["lo_ed"].sum())))
    for c in (1, 2, 7):
        absorb = 100 * (1 - g_c[c] / g[c]) if g[c] != 0 else np.nan
        print("  %-16s unconditional %+6.2f  account-conditional %+6.2f  CI [%+6.2f, %+6.2f]"
              "  ABSORPTION %6.1f%%" % (SOURCES[c], g[c], g_c[c], ci_c[c][0], ci_c[c][1], absorb))
    # bootstrap the absorption ratio itself for the savings source
    econs = sub["economy"].unique()
    by_all = {e: gg for e, gg in sub.groupby("economy")}
    ratios = []
    for _ in range(DRAWS):
        take = RNG.choice(len(econs), len(econs), replace=True)
        d = pd.concat([by_all[econs[i]] for i in take])
        gu = wshare(d[d["hi_ed"]], 1) - wshare(d[d["lo_ed"]], 1)
        a = d[d["account"] == 1]
        gc = wshare(a[a["hi_ed"]], 1) - wshare(a[a["lo_ed"]], 1)
        if gu and np.isfinite(gu) and np.isfinite(gc):
            ratios.append(100 * (1 - gc / gu))
    print("  ABSORPTION of the savings-source gradient: %.1f%%  CI [%.1f%%, %.1f%%] "
          "(2,000 economy draws)" % (100 * (1 - g_c[1] / g[1]),
                                     np.nanpercentile(ratios, 2.5), np.nanpercentile(ratios, 97.5)))
    print("  benchmarks on the SAME 98-economy sample (U24): usage margin 56.9%, "
          "welfare margin 8.6%")

    # ------------------------------------------------- SECONDARY 2: income axis
    print("\n" + "-" * 100)
    print("SECONDARY 2 (no bar) — the income axis: richest 60% (inc_q 3-5) minus poorest 40%")
    inc = sub[sub["hi_inc"] | sub["lo_inc"]]
    g_i = gaps(inc, inc["hi_inc"], inc["lo_inc"], codes)
    ci_i = cluster_boot(inc, "hi_inc", "lo_inc", codes)
    print("  M2: n(rich60) = %d, n(poor40) = %d" % (int(inc["hi_inc"].sum()),
                                                    int(inc["lo_inc"].sum())))
    for c in codes:
        rs = REGISTERED_SIGN.get(c)
        v = ("sign OK" if np.sign(g_i[c]) == rs else "SIGN WRONG") if rs else "—"
        print("  %-20s gap %+6.2f  CI [%+6.2f, %+6.2f]  reg %-4s %s"
              % (SOURCES[c], g_i[c], ci_i[c][0], ci_i[c][1],
                 {1: "POS", -1: "NEG"}.get(rs, "—"), v))

    # ------------------------------------------------- SECONDARY 3: within-country
    print("\n" + "-" * 100)
    print("SECONDARY 3 (no bar) — within-country: is the pooled savings gap a composition artifact?")
    per = []
    for e, gg in sub.groupby("economy"):
        nh, nl = int(gg["hi_ed"].sum()), int(gg["lo_ed"].sum())
        if nh >= 100 and nl >= 100:
            per.append((e, wshare(gg[gg["hi_ed"]], 1) - wshare(gg[gg["lo_ed"]], 1),
                        wshare(gg[gg["hi_ed"]], 2) - wshare(gg[gg["lo_ed"]], 2)))
    p = pd.DataFrame(per, columns=["economy", "gap_sav", "gap_fam"])
    print("  qualifying economies (both education cells n >= 100): %d of %d in the module"
          % (len(p), sub["economy"].nunique()))
    print("  savings-source gap:       positive in %d of %d (%.1f%%), median %+.2fpp, "
          "IQR [%+.2f, %+.2f]" % ((p["gap_sav"] > 0).sum(), len(p),
                                  100 * (p["gap_sav"] > 0).mean(), p["gap_sav"].median(),
                                  p["gap_sav"].quantile(.25), p["gap_sav"].quantile(.75)))
    print("  family/friends gap:       negative in %d of %d (%.1f%%), median %+.2fpp"
          % ((p["gap_fam"] < 0).sum(), len(p), 100 * (p["gap_fam"] < 0).mean(),
             p["gap_fam"].median()))
    pooled_same = (wshare(sub[sub["hi_ed"] & sub["economy"].isin(p["economy"])], 1)
                   - wshare(sub[sub["lo_ed"] & sub["economy"].isin(p["economy"])], 1))
    print("  pooled savings gap over the SAME qualifying set: %+.2fpp vs median economy %+.2fpp "
          "-> composition wedge %+.2fpp" % (pooled_same, p["gap_sav"].median(),
                                            pooled_same - p["gap_sav"].median()))
    print("\n  three largest and three smallest economy savings gaps:")
    for _i, r in p.sort_values("gap_sav", ascending=False).head(3).iterrows():
        print("    %-24s %+6.2f" % (r["economy"], r["gap_sav"]))
    for _i, r in p.sort_values("gap_sav").head(3).iterrows():
        print("    %-24s %+6.2f" % (r["economy"], r["gap_sav"]))


if __name__ == "__main__":
    main()
