"""U20 (pre-registered): is the INCOME axis of the access-absorption ruler a WITHIN-COUNTRY
regularity, or a BETWEEN-COUNTRY composition artifact?

U19 took the ruler's largest axis (education) apart into within-country gradient vs between-country
composition and the gradient survived: median within-economy gap +9.4pp, positive in 63/64
economies, composition wedge only ~22% of the pooled figure. Five axes remain pooled-only. This runs
the IDENTICAL test on the second-largest axis, INCOME (U17: conditional q5-q1 = +11.5pp) -- the axis
where the composition worry is a priori strongest in one specific sense: income quintiles are
constructed WITHIN each economy, so a purely between-country story would have to work through
something other than quintile membership, making a collapse here more diagnostic than a collapse on
education would have been.

Primary  : for EACH economy separately, the conditional income gap in digital-payment use --
           weighted rate of anydigpayment == 1 among account == 1 for inc_q >= 4 (richest 40%)
           minus inc_q <= 2 (poorest 40%). An economy qualifies only if BOTH cells have unweighted
           n >= 100 (gate M2 applied PER ECONOMY): 83 of 97 economies qualify (coverage check run
           before registration on non-missing outcome + weight + inc_q, matching M2 as applied --
           no rate computed; this is the fix for U19's disclosed count deviation).
           Statistic = the MEDIAN within-economy gap. Keep if >= 5pp AND >= 2/3 (>= 56/83) of
           qualifying economies show a positive gap.
Secondary: share positive, IQR and extremes; the pooled gap on the same 83 economies and on all
           economies (the pooled-vs-median wedge is the composition estimate); and the like-for-like
           q5-vs-q1 variant (33 economies qualify), the direct within-country counterpart of U17.

Declared caveats: post-treatment conditioning on account holding (as in U6/U8/U10/U14-U19); the
richest-40 vs poorest-40 contrast is COARSER than U17's q5-q1 and is expected to be smaller in pp
for that reason alone -- the q5-vs-q1 variant is the like-for-like comparison; the median weights
each economy equally, by design a different weighting from the pooled statistic; the qualifying set
is SELECTED (economies need sizeable poorest-40 AND richest-40 accountholding populations).
Single 2024 cross-section -- descriptive, no trend language.
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
    print(f"U20 M2 per economy ({hi_label} vs {lo_label}, both cells n >= {MIN_CELL}): "
          f"{len(q)} of {len(t)} economies qualify")
    return t, q


def _describe(q, label, threshold=5.0):
    med = float(q["gap"].median())
    share_pos = float((q["gap"] > 0).mean())
    n_pos = int((q["gap"] > 0).sum())
    print(f"\nU20 {label}:")
    print(f"U20   MEDIAN within-economy gap = {med:+.1f}pp   (n={len(q)} economies)")
    print(f"U20   positive in {n_pos}/{len(q)} economies ({share_pos:.0%})")
    print(f"U20   quartiles: p25={q['gap'].quantile(.25):+.1f}pp  "
          f"p75={q['gap'].quantile(.75):+.1f}pp   mean={q['gap'].mean():+.1f}pp")
    lo3 = q.nsmallest(3, "gap")[["economy", "gap"]].to_records(index=False)
    hi3 = q.nlargest(3, "gap")[["economy", "gap"]].to_records(index=False)
    print("U20   smallest: " + ", ".join(f"{e} {g:+.1f}" for e, g in lo3))
    print("U20   largest:  " + ", ".join(f"{e} {g:+.1f}" for e, g in hi3))
    print(f"U20   share of economies with gap >= {threshold}pp: "
          f"{(q['gap'] >= threshold).mean():.0%}")
    return med, share_pos, n_pos


def _pooled(mi: Micro, lo_mask, hi_mask, economies, label):
    """Pooled conditional gap over a set of economies (micro.py weighting)."""
    df = mi.df
    base = (df["account"] == 1)
    sel = df["economy"].isin(economies) if economies is not None else pd.Series(True, df.index)
    v_lo, n_lo = mi.rate("anydigpayment", where=base & sel & lo_mask)
    v_hi, n_hi = mi.rate("anydigpayment", where=base & sel & hi_mask)
    print(f"U20   pooled {label}: lo={v_lo:.1f}pp (n={n_lo}) hi={v_hi:.1f}pp (n={n_hi})  "
          f"gap={v_hi - v_lo:+.1f}pp")
    return v_hi - v_lo


def run(mi: Micro):
    df = mi.df
    print("U20 M3: n/a -- within-accountholder subgroup split, no country-file equivalent\n")

    lo = df["inc_q"] <= 2         # poorest 40%
    hi = df["inc_q"] >= 4         # richest 40%
    q1 = df["inc_q"] == 1
    q5 = df["inc_q"] == 5

    # ---------- PRIMARY -------------------------------------------------------------------------
    t, q = _gap_table(mi, lo, hi, "poorest-40", "richest-40")
    cover = df[(df["account"] == 1) & df["inc_q"].notna() & df["anydigpayment"].notna()]
    share = cover[cover["economy"].isin(q["economy"])].shape[0] / cover.shape[0]
    print(f"U20 qualifying economies cover {share:.1%} of accountholding respondents")
    med, share_pos, n_pos = _describe(q, "PRIMARY -- within-economy conditional income gap")

    print("\nU20 the pooled-vs-median wedge (the composition estimate):")
    pooled_q = _pooled(mi, lo, hi, q["economy"], f"over the {len(q)} qualifying economies")
    pooled_all = _pooled(mi, lo, hi, None, "over ALL economies")
    print(f"U20   wedge (pooled over qualifiers - median within) = {pooled_q - med:+.1f}pp")

    # ---------- SECONDARY: the U17 like-for-like contrast -----------------------------------------
    print("\n" + "-" * 78)
    t2, q2 = _gap_table(mi, q1, q5, "q1 (poorest)", "q5 (richest)")
    med2, share_pos2, n_pos2 = _describe(
        q2, "SECONDARY -- q5 vs q1 (U17's like-for-like contrast)")
    print("\nU20 the pooled-vs-median wedge, q5-vs-q1 contrast:")
    pooled_q2 = _pooled(mi, q1, q5, q2["economy"], "over the qualifying economies")
    pooled_all2 = _pooled(mi, q1, q5, None, "over ALL economies (U17 logged +11.5pp)")
    print(f"U20   wedge (pooled over qualifiers - median within) = {pooled_q2 - med2:+.1f}pp")

    # ---------- VERDICT ---------------------------------------------------------------------------
    need_pos = int(np.ceil(2 * len(q) / 3))
    ok = (med >= 5.0) and (n_pos >= need_pos)
    print("\n" + "=" * 78)
    print("U20 keep condition: median within-economy gap >= 5pp AND >= 2/3 of qualifying "
          "economies positive")
    print(f"U20   observed median={med:+.1f}pp   positive {n_pos}/{len(q)} "
          f"(need >= {need_pos})  -> passes: {ok}")
    print(f"U20   [context] pooled on the same economies = {pooled_q:+.1f}pp, "
          f"pooled on all = {pooled_all:+.1f}pp")
    print(f"U20   [context] q5-vs-q1 contrast: median={med2:+.1f}pp, "
          f"positive {n_pos2}/{len(q2)}, pooled all={pooled_all2:+.1f}pp (U17 logged +11.5pp)")
    print("U20   [context] U19's education axis for comparison: median +9.4pp, 63/64 positive, "
          "wedge +2.7pp")


if __name__ == "__main__":
    run(Micro())
