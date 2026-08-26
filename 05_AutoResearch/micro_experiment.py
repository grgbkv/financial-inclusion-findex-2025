"""U28 (registered 2026-08-26, after U28x's structural pass and before any gradient was computed).

Parent E57 (subject: the same item at the individual level); design ancestor U24. Stream micro,
design micro-cross-section, 2024 SINGLE WAVE -- cross-sectional description, no trend language.
Frame: the 98-economy `fin22` module set, pooled, weighted (`wgt`), M1 by construction.

HYPOTHESIS. E57 found `fin22d` counter-moving with digital payment ACROSS economies; E59 (this
cycle) found no within-economy delta counterpart. The remaining reading of E57's composition fact is
INDIVIDUAL-LEVEL SUBSTITUTION: a non-formal borrowing source is what an adult uses when formal
access is absent, so within economies the `fin22d` user should have FEWER resources and NO account.

DECLARED CODING: outcome is fin22d == 1; codes 2/3/4 stay in the denominator as "not this source" --
this is the country file's own construction and is why the item is M3-exact at 0.000pp.

REGISTERED SIGN (B15): NEGATIVE on every leg. A positive gradient is the OPPOSITE pattern.

REGISTERED KEEP -- all three legs:
  1 education gap (educ in {2,3} minus educ == 1) <= -5pp AND log-odds twin <= -0.20 (B13)
  2 access gap (account==1 minus account==0)      <= -5pp AND log-odds twin <= -0.20
  3 within-country: >= 75% of M2-qualifying economies (>=100 unweighted in both education cells)
    show a NEGATIVE education gap
Any leg failing is a DISCARD and the failing leg is named.

SECONDARY 1 (signs registered NEGATIVE, no bar): the same two gradients on fin22b, fin22e, fin22f.
SECONDARY 2 (no bar): absorption = 1 - (account-conditional educ gap / unconditional educ gap),
  beside U24's 56.9% (usage) and 8.6% (welfare). Negative absorption on a negative gap is
  AMPLIFICATION and is reported with that word.
SECONDARY 3 (no bar): anydigpayment on the SAME sample, the ruler's usage anchor (U10).

Inference: 2,000-draw ECONOMY-CLUSTER percentile bootstrap on every gap and on absorption; Kish
neff of the pooled respondent weights beside the nominal n (B10). M2 >=100 on every reported cell;
M3 carried from U28x. Pooled-weighting caveat (HARNESS_V2_NOTES item 3) is why leg 3 is a keep leg.
"""
import numpy as np
import pandas as pd

from micro import Micro

BASE_ITEM = "fin22d"
FAMILY = ["fin22b", "fin22e", "fin22f"]
REFERENCE = "anydigpayment"
PP_BAR = -5.0
LO_BAR = -0.20
WITHIN_BAR = 0.75
DRAWS = 2000
RNG = np.random.default_rng(20260826)


def wrate(sub, col):
    """weighted share (pp) of col == 1 within sub; denominator = all non-missing rows."""
    s = sub.dropna(subset=[col, "wgt"])
    if len(s) == 0 or s["wgt"].sum() == 0:
        return np.nan
    return 100 * float(np.average(s[col].eq(1).astype(float), weights=s["wgt"]))


def logodds(p_pp):
    p = min(max(p_pp / 100.0, 1e-6), 1 - 1e-6)
    return float(np.log(p / (1 - p)))


def gap(sub, col, hi_mask, lo_mask):
    """(pp gap, log-odds gap, rate_hi, rate_lo) for hi minus lo."""
    r_hi = wrate(sub[hi_mask.reindex(sub.index).fillna(False)], col)
    r_lo = wrate(sub[lo_mask.reindex(sub.index).fillna(False)], col)
    if pd.isna(r_hi) or pd.isna(r_lo):
        return np.nan, np.nan, r_hi, r_lo
    return r_hi - r_lo, logodds(r_hi) - logodds(r_lo), r_hi, r_lo


def boot_gap(df, col, hi_mask, lo_mask, draws=DRAWS):
    """2,000-draw ECONOMY-CLUSTER percentile bootstrap on (pp gap, log-odds gap)."""
    econs = df["economy"].unique()
    by = {e: idx for e, idx in df.groupby("economy").groups.items()}
    pp, lo = [], []
    for _ in range(draws):
        pick = RNG.choice(len(econs), len(econs))
        idx = np.concatenate([by[econs[i]].to_numpy() for i in pick])
        s = df.loc[idx]
        g, l, _, _ = gap(s, col, hi_mask, lo_mask)
        if pd.notna(g):
            pp.append(g)
            lo.append(l)
    f = lambda a: (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)))
    return f(pp), f(lo)


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def report(df, col, hi, lo, label, boot=True):
    g, l, r_hi, r_lo = gap(df, col, hi, lo)
    n_hi = int(hi.reindex(df.index).fillna(False).sum())
    n_lo = int(lo.reindex(df.index).fillna(False).sum())
    m2 = "M2 ok" if min(n_hi, n_lo) >= 100 else "M2 FAIL"
    line = ("  %-34s %6.2f vs %6.2f pp   gap %+6.2fpp   log-odds %+6.3f   n %6d/%6d  %s"
            % (label, r_hi, r_lo, g, l, n_hi, n_lo, m2))
    if boot:
        (plo, phi), (llo, lhi) = boot_gap(df, col, hi, lo)
        line += "\n  %-34s boot pp [%+6.2f,%+6.2f]   boot log-odds [%+6.3f,%+6.3f]" % ("", plo, phi, llo, lhi)
    print(line)
    return g, l


def main():
    mi = Micro()
    df = mi.df
    base = df[df[BASE_ITEM].notna()].copy()
    econs = sorted(base["economy"].unique())
    print("=" * 104)
    print("U28 — the SUBSTITUTION prediction on `fin22d` (registered sign NEGATIVE on every leg)")
    print("=" * 104)
    print("module base: %d respondents, %d economies   Kish neff of pooled wgt = %.0f"
          % (len(base), len(econs), kish(base["wgt"])))
    print("B10: no significance language attaches to the nominal %d — neff is the figure that binds.\n"
          % len(base))
    print("pooled weighted rate of %s: %.2f%%   (%s ruler reference computed below)"
          % (BASE_ITEM, wrate(base, BASE_ITEM), REFERENCE))

    educ_hi = df["educ"].isin([2, 3])
    educ_lo = df["educ"].eq(1)
    acct_hi = df["account"].eq(1)
    acct_lo = df["account"].eq(0)

    print("\n" + "=" * 104)
    print("PRIMARY — the three registered keep legs")
    print("=" * 104)
    print("\nLEG 1 — education gradient (secondary-or-more minus primary-or-less)")
    g1, l1 = report(base, BASE_ITEM, educ_hi, educ_lo, "%s, all module adults" % BASE_ITEM)
    print("\nLEG 2 — access gradient (accountholders minus non-accountholders)")
    g2, l2 = report(base, BASE_ITEM, acct_hi, acct_lo, "%s, all module adults" % BASE_ITEM)

    print("\nLEG 3 — within-country sign of the education gap, M2-qualifying economies only")
    signs, gaps = [], []
    for e, grp in base.groupby("economy"):
        n_hi = int(educ_hi.reindex(grp.index).fillna(False).sum())
        n_lo = int(educ_lo.reindex(grp.index).fillna(False).sum())
        if min(n_hi, n_lo) < 100:
            continue
        g, _, _, _ = gap(grp, BASE_ITEM, educ_hi, educ_lo)
        if pd.notna(g):
            signs.append(g < 0)
            gaps.append(g)
    share = float(np.mean(signs)) if signs else np.nan
    print("  qualifying economies: %d of %d   negative education gap in %d (%.1f%%)   median gap %+.2fpp"
          % (len(signs), len(econs), int(np.sum(signs)), 100 * share, float(np.median(gaps))))

    ok1 = (g1 <= PP_BAR) and (l1 <= LO_BAR)
    ok2 = (g2 <= PP_BAR) and (l2 <= LO_BAR)
    ok3 = share >= WITHIN_BAR
    print("\n" + "-" * 104)
    print("  LEG 1 education  %s  (gap %+.2fpp vs bar %.1f, log-odds %+.3f vs bar %.2f)"
          % ("PASS" if ok1 else "FAIL", g1, PP_BAR, l1, LO_BAR))
    print("  LEG 2 access     %s  (gap %+.2fpp vs bar %.1f, log-odds %+.3f vs bar %.2f)"
          % ("PASS" if ok2 else "FAIL", g2, PP_BAR, l2, LO_BAR))
    print("  LEG 3 within     %s  (%.1f%% negative vs bar %.0f%%)"
          % ("PASS" if ok3 else "FAIL", 100 * share, 100 * WITHIN_BAR))
    failed = [n for n, ok in [("1 education", ok1), ("2 access", ok2), ("3 within-country", ok3)] if not ok]
    print("\n  ==> %s" % ("KEEP — all three registered legs fire with the registered NEGATIVE sign"
                          if not failed else
                          "DISCARD — failing leg(s): %s" % ", ".join(failed)))

    print("\n" + "=" * 104)
    print("SECONDARY 1 (no bar; registered sign NEGATIVE for all three) — the rest of the all-module family")
    print("=" * 104)
    fired = 0
    for c in FAMILY:
        sub = df[df[c].notna()]
        print("\n  %s  (asked of %d respondents, %d economies; pooled rate %.2f%%)"
              % (c, len(sub), sub["economy"].nunique(), wrate(sub, c)))
        ge, le = report(sub, c, educ_hi, educ_lo, "education gap", boot=False)
        ga, la = report(sub, c, acct_hi, acct_lo, "access gap", boot=False)
        hit = (ge <= PP_BAR and le <= LO_BAR and ga <= PP_BAR and la <= LO_BAR)
        fired += hit
        print("       both gradients at the primary's bars with the registered sign: %s" % ("YES" if hit else "no"))
    print("\n  items firing on both gradients: %d of %d (descriptive; cannot rescue a failed primary)"
          % (fired, len(FAMILY)))

    print("\n" + "=" * 104)
    print("SECONDARY 2 (no bar) — agenda item 4.7: `fin22d` on the access-absorption ruler")
    print("=" * 104)
    cond = base[acct_hi.reindex(base.index).fillna(False)]
    g_cond, l_cond, _, _ = gap(cond, BASE_ITEM, educ_hi, educ_lo)
    absorb = 1 - (g_cond / g1) if g1 else np.nan
    word = ("AMPLIFICATION — the account-conditional gap is LARGER in magnitude"
            if absorb < 0 else "absorption")
    print("  unconditional education gap            %+.2fpp   (log-odds %+.3f)" % (g1, l1))
    print("  account-conditional education gap      %+.2fpp   (log-odds %+.3f)  n=%d" % (g_cond, l_cond, len(cond)))
    print("  absorption = 1 - cond/uncond           %.1f%%   [%s]" % (100 * absorb, word))
    print("  ruler so far: U10/U24 usage 56.9%%  ·  U24 welfare 8.6%%  ·  U28 liability %.1f%%" % (100 * absorb))

    print("\n" + "=" * 104)
    print("SECONDARY 3 (no bar) — the reference usage margin on the SAME 98-economy sample")
    print("=" * 104)
    report(base, REFERENCE, educ_hi, educ_lo, "%s education gap" % REFERENCE, boot=False)
    report(base, REFERENCE, acct_hi, acct_lo, "%s access gap" % REFERENCE, boot=False)
    ref_cond = gap(cond, REFERENCE, educ_hi, educ_lo)[0]
    ref_unc = gap(base, REFERENCE, educ_hi, educ_lo)[0]
    print("  %s absorption on this sample: %.1f%%" % (REFERENCE, 100 * (1 - ref_cond / ref_unc)))


if __name__ == "__main__":
    main()
