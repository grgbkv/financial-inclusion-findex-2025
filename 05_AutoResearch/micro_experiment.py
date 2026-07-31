"""U19 (pre-registered): is the access-absorption ruler a WITHIN-COUNTRY regularity, or a
BETWEEN-COUNTRY composition artifact?

The ruler now carries six axes (U6/U10/U15/U16/U17/U18) and every one of them is a POOLED
across-economies statistic. That is the standing caveat on the whole micro ledger
(HARNESS_V2_NOTES #3, re-declared in every U entry): a pooled gradient can be produced entirely by
COMPOSITION -- low-education adults concentrated in low-digitalization economies -- with no
within-country gradient at all. No U experiment has ever separated the two. This tests the ruler's
LARGEST axis, education (U10: +16.8pp conditional on account, ~64% absorbed), the one whose
collapse would do the most damage to the ruler's reading.

Primary  : for EACH economy separately, the conditional education gap in digital-payment use --
           weighted rate of anydigpayment == 1 among account == 1 for educ >= 2 (secondary-or-more)
           minus educ == 1 (primary-or-less). An economy qualifies only if BOTH cells have
           unweighted n >= 100 (gate M2 applied PER ECONOMY, not pooled): 64 economies qualify,
           covering 69.5% of accountholding respondents (verified as a coverage check before
           registration -- no rate computed).
           Statistic = the MEDIAN within-economy gap. Keep if >= 5pp AND >= 2/3 (>= 43/64) of
           qualifying economies show a positive gap.
Secondary: share positive, IQR and extremes; the pooled gap on the same 64 economies and on all
           economies (the pooled-vs-median wedge is the composition estimate); and the stricter
           tertiary-vs-primary variant (educ == 3 vs educ == 1, 31 economies qualify).

Declared caveats: conditioning on account holding conditions on a post-treatment variable (as in
U6/U8/U10/U14-U18); educ >= 2 merges secondary and tertiary, so the primary contrast is COARSER
than U10's tertiary-vs-primary and is expected to be smaller in pp for that reason alone -- the
tertiary variant is the like-for-like comparison; the median across economies weights each economy
equally, a different weighting from the pooled statistic BY CONSTRUCTION (that is the test, not a
flaw); the qualifying set is SELECTED (economies need sizeable primary-educated AND secondary-plus
accountholding populations), so it skews away from both the least- and most-educated economies.
Single 2024 cross-section -- no trend language.
"""
import numpy as np
import pandas as pd

from micro import Micro

MIN_CELL = 100


def _gap_table(mi: Micro, lo_mask, hi_mask, lo_label, hi_label):
    """Per-economy weighted gap in anydigpayment among accountholders, hi minus lo.
    Only economies where BOTH unweighted cells reach MIN_CELL qualify (M2 per economy)."""
    df = mi.df
    base = (df["account"] == 1)
    rows = []
    for econ in sorted(df["economy"].dropna().unique()):
        e = df["economy"] == econ
        v_lo, n_lo = mi.rate("anydigpayment", where=base & e & lo_mask)
        v_hi, n_hi = mi.rate("anydigpayment", where=base & e & hi_mask)
        rows.append({"economy": econ, "rate_lo": v_lo, "n_lo": n_lo,
                     "rate_hi": v_hi, "n_hi": n_hi,
                     "gap": v_hi - v_lo,
                     "qualifies": bool(n_lo >= MIN_CELL and n_hi >= MIN_CELL)})
    t = pd.DataFrame(rows)
    q = t[t["qualifies"] & t["gap"].notna()].copy()
    print(f"U19 M2 per economy ({hi_label} vs {lo_label}, both cells n >= {MIN_CELL}): "
          f"{len(q)} of {len(t)} economies qualify")
    return t, q


def _describe(q, label, threshold=5.0):
    med = float(q["gap"].median())
    share_pos = float((q["gap"] > 0).mean())
    n_pos = int((q["gap"] > 0).sum())
    print(f"\nU19 {label}:")
    print(f"U19   MEDIAN within-economy gap = {med:+.1f}pp   (n={len(q)} economies)")
    print(f"U19   positive in {n_pos}/{len(q)} economies ({share_pos:.0%})")
    print(f"U19   quartiles: p25={q['gap'].quantile(.25):+.1f}pp  "
          f"p75={q['gap'].quantile(.75):+.1f}pp   mean={q['gap'].mean():+.1f}pp")
    lo3 = q.nsmallest(3, "gap")[["economy", "gap"]].to_records(index=False)
    hi3 = q.nlargest(3, "gap")[["economy", "gap"]].to_records(index=False)
    print("U19   smallest: " + ", ".join(f"{e} {g:+.1f}" for e, g in lo3))
    print("U19   largest:  " + ", ".join(f"{e} {g:+.1f}" for e, g in hi3))
    print(f"U19   share of economies with gap >= {threshold}pp: "
          f"{(q['gap'] >= threshold).mean():.0%}")
    return med, share_pos, n_pos


def _pooled(mi: Micro, lo_mask, hi_mask, economies, label):
    """Pooled (economy-equal weighting per micro.py) conditional gap over a set of economies."""
    df = mi.df
    base = (df["account"] == 1)
    sel = df["economy"].isin(economies) if economies is not None else pd.Series(True, df.index)
    v_lo, n_lo = mi.rate("anydigpayment", where=base & sel & lo_mask)
    v_hi, n_hi = mi.rate("anydigpayment", where=base & sel & hi_mask)
    print(f"U19   pooled {label}: lo={v_lo:.1f}pp (n={n_lo}) hi={v_hi:.1f}pp (n={n_hi})  "
          f"gap={v_hi - v_lo:+.1f}pp")
    return v_hi - v_lo


def run(mi: Micro):
    df = mi.df
    print("U19 M3: n/a -- within-accountholder subgroup split, no country-file equivalent\n")

    lo = df["educ"] == 1          # primary or less
    hi = df["educ"] >= 2          # secondary or more
    ter = df["educ"] == 3         # tertiary

    # ---------- PRIMARY -------------------------------------------------------------------------
    t, q = _gap_table(mi, lo, hi, "primary-or-less", "secondary-or-more")
    cover = df[(df["account"] == 1) & df["educ"].notna() & df["anydigpayment"].notna()]
    share = cover[cover["economy"].isin(q["economy"])].shape[0] / cover.shape[0]
    print(f"U19 qualifying economies cover {share:.1%} of accountholding respondents")
    med, share_pos, n_pos = _describe(q, "PRIMARY -- within-economy conditional education gap")

    print("\nU19 the pooled-vs-median wedge (the composition estimate):")
    pooled_q = _pooled(mi, lo, hi, q["economy"], "over the 64 qualifying economies")
    pooled_all = _pooled(mi, lo, hi, None, "over ALL economies")
    print(f"U19   wedge (pooled over qualifiers - median within) = {pooled_q - med:+.1f}pp")

    # ---------- SECONDARY: the U10 like-for-like contrast ----------------------------------------
    print("\n" + "-" * 78)
    t2, q2 = _gap_table(mi, lo, ter, "primary-or-less", "tertiary")
    med2, share_pos2, n_pos2 = _describe(
        q2, "SECONDARY -- tertiary vs primary (U10's like-for-like contrast)")
    print("\nU19 the pooled-vs-median wedge, tertiary contrast:")
    pooled_q2 = _pooled(mi, lo, ter, q2["economy"], "over the qualifying economies")
    pooled_all2 = _pooled(mi, lo, ter, None, "over ALL economies (U10 logged +16.8pp)")
    print(f"U19   wedge (pooled over qualifiers - median within) = {pooled_q2 - med2:+.1f}pp")

    # ---------- VERDICT -------------------------------------------------------------------------
    need_pos = int(np.ceil(2 * len(q) / 3))
    ok = (med >= 5.0) and (n_pos >= need_pos)
    print("\n" + "=" * 78)
    print("U19 keep condition: median within-economy gap >= 5pp AND >= 2/3 of qualifying "
          "economies positive")
    print(f"U19   observed median={med:+.1f}pp   positive {n_pos}/{len(q)} "
          f"(need >= {need_pos})  -> passes: {ok}")
    print(f"U19   [context] pooled on the same economies = {pooled_q:+.1f}pp, "
          f"pooled on all = {pooled_all:+.1f}pp")
    print(f"U19   [context] tertiary contrast: median={med2:+.1f}pp, "
          f"positive {n_pos2}/{len(q2)}, pooled all={pooled_all2:+.1f}pp (U10 logged +16.8pp)")


if __name__ == "__main__":
    run(Micro())
