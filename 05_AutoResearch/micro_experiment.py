"""U22 (pre-registered 2026-08-17): is the CONNECTIVITY gap in digital-payment use a
WITHIN-COUNTRY regularity, or a between-country composition artifact?

Agenda item 5.5. Parent: U21 (first descendant). Micro stream, 2024 wave, cross-sectional.
Rule B17: this experiment pays the micro quota, carried unpaid for two cycles.

WHY. U21 established two POOLED facts over 140 economies: among accountholders the offline-vs-online
gap in `anydigpayment` is +13.6pp, and account holding absorbs 55.5% of the unconditional +30.5pp
connectivity gap — an absorption share unlike any resource axis. Pooled figures over economies that
differ enormously in internet penetration are exactly where a composition artifact hides: economies
with low internet use are also economies with low digital-payment use, so a pooled gap can be large
with no economy showing one. U19 and U20 ran this test on the education and income axes and both
kept. Connectivity is the axis on which economies differ most, so it is the axis where the worry
is largest.

DESIGN (U19/U20's design verbatim, connectivity substituted). For every economy with >= 100
unweighted respondents in BOTH cells (M2) among accountholders (`account == 1`), the weighted gap
  anydigpayment(internet_use == 1) - anydigpayment(internet_use == 0).
Report median, IQR, sign count, range with economy names, the qualifying set's share of
accountholding respondents, the POOLED gap over the SAME qualifying set, and the COMPOSITION WEDGE
(pooled - median).

REGISTERED CLAIMS, both required for a keep:
  C1  median within-economy gap >= +5.0pp (the standing micro gap threshold)
  C2  the gap is positive in >= 80% of qualifying economies (U19 98%, U20 89%)
REGISTERED SIGN (B15): POSITIVE — online accountholders use digital payments MORE. A gap of the
right magnitude and the wrong sign is the opposite pattern, not partial confirmation.

SECONDARY (registered, no bar, diagnostic): the within-country version of U21's ABSORPTION result —
per economy, the connectivity gap among accountholders as a fraction of the connectivity gap among
all adults, reported as a median. It exists so U21's 55.5% is not left as a pooled-only number.

GATES. M1 (weights, enforced by the module). M2 (unweighted n >= 100) on every reported cell.
M3 against the country file on `account` and `anydigpayment`, tolerance 1pp.

DECLARED. `internet_use` is self-reported internet USE, co-determined with digital payment use — a
person may report using the internet BECAUSE they pay digitally, and one cross-section cannot
separate the directions (U21's caveat, carried). Conditioning on account holding is post-treatment.
Single wave: no trend language. A within-country regularity is still an association, not a mechanism.
"""
import numpy as np
import pandas as pd

from micro import Micro

MIN_CELL = 100
MEDIAN_BAR = 5.0        # C1
SHARE_BAR = 0.80        # C2

M3_ECONOMIES = ["India", "Kazakhstan", "Poland", "Estonia", "Uzbekistan", "Brazil", "Nigeria",
                "Indonesia", "Turkiye", "Mexico"]


def per_economy_gap(mi: Micro, col, hi_mask, lo_mask, base):
    """Weighted hi-lo gap on `col` within `base`, per economy, M2 on BOTH cells."""
    df = mi.df
    rows = []
    for econ in sorted(df["economy"].dropna().unique()):
        e = df["economy"] == econ
        v_hi, n_hi = mi.rate(col, where=base & hi_mask & e)
        v_lo, n_lo = mi.rate(col, where=base & lo_mask & e)
        rows.append({"economy": econ, "rate_hi": v_hi, "rate_lo": v_lo,
                     "gap": v_hi - v_lo, "n_hi": n_hi, "n_lo": n_lo,
                     "n_base": int((base & e).sum()),
                     "qualifies": bool(n_hi >= MIN_CELL and n_lo >= MIN_CELL)})
    return pd.DataFrame(rows)


def pooled_gap(mi: Micro, col, hi_mask, lo_mask, base):
    v_hi, n_hi = mi.rate(col, where=base & hi_mask)
    v_lo, n_lo = mi.rate(col, where=base & lo_mask)
    return v_hi - v_lo, n_hi, n_lo


def describe(tab, label):
    q = tab[tab["qualifies"]]
    g = q["gap"]
    pos = int((g > 0).sum())
    print(f"\n  {label}")
    print(f"    qualifying economies (M2 on both cells): {len(q)} of {len(tab)}")
    if not len(q):
        return None
    print(f"    MEDIAN gap {g.median():+.2f}pp | IQR {g.quantile(.25):+.2f} to "
          f"{g.quantile(.75):+.2f} | mean {g.mean():+.2f}")
    print(f"    positive in {pos}/{len(q)} ({pos / len(q):.1%})")
    lo_row, hi_row = q.loc[g.idxmin()], q.loc[g.idxmax()]
    print(f"    range: {lo_row['economy']} {lo_row['gap']:+.1f}  ...  "
          f"{hi_row['economy']} {hi_row['gap']:+.1f}")
    return {"n_qual": len(q), "median": float(g.median()), "pos": pos,
            "share_pos": pos / len(q), "iqr": (float(g.quantile(.25)), float(g.quantile(.75))),
            "mean": float(g.mean())}


def run(mi: Micro):
    df = mi.df
    print("=" * 100)
    print("U22 — is the connectivity gap in digital-payment use a WITHIN-COUNTRY regularity?")
    print("     (agenda 5.5; parent U21; 2024 micro, weighted; B17 quota)")
    print("=" * 100)

    print("\nM3 country-file cross-check:")
    print("  account       ", mi.gate_country_file("account", "account_t_d", M3_ECONOMIES))
    print("  anydigpayment ", mi.gate_country_file("anydigpayment", "g20_any", M3_ECONOMIES))

    online = df["internet_use"] == 1
    offline = df["internet_use"] == 0
    acct = df["account"] == 1
    everyone = pd.Series(True, index=df.index)

    # ------------------------------------------------------------------ PRIMARY
    print("\n" + "-" * 100)
    print("PRIMARY (registered) — per-economy connectivity gap in anydigpayment AMONG ACCOUNTHOLDERS")
    print("-" * 100)
    tab = per_economy_gap(mi, "anydigpayment", online, offline, acct)
    stats = describe(tab, "online - offline | accountholders")
    q = tab[tab["qualifies"]]

    # coverage of the qualifying set, in accountholding respondents
    acct_n_all = int(acct.sum())
    acct_n_qual = int(df[acct & df["economy"].isin(q["economy"])].shape[0])
    print(f"    qualifying economies hold {acct_n_qual}/{acct_n_all} = "
          f"{acct_n_qual / acct_n_all:.1%} of accountholding respondents")

    # pooled over the SAME qualifying set -> composition wedge
    qual_mask = df["economy"].isin(q["economy"])
    pool_q, nh, nl = pooled_gap(mi, "anydigpayment", online, offline, acct & qual_mask)
    pool_all, _, _ = pooled_gap(mi, "anydigpayment", online, offline, acct)
    print(f"    POOLED over the same {len(q)} economies: {pool_q:+.2f}pp (n {nh}/{nl})")
    print(f"    pooled over ALL economies (U21's figure): {pool_all:+.2f}pp")
    print(f"    COMPOSITION WEDGE (pooled_qual - median) = {pool_q - stats['median']:+.2f}pp "
          f"({(pool_q - stats['median']) / pool_q:.1%} of the pooled gap)")

    print("\n    ten largest / ten smallest qualifying gaps:")
    srt = q.sort_values("gap")
    for _, r in pd.concat([srt.head(10), srt.tail(10)]).iterrows():
        print(f"      {r['economy']:28s} online {r['rate_hi']:5.1f}  offline {r['rate_lo']:5.1f}"
              f"   gap {r['gap']:+6.1f}pp   n {r['n_hi']:5d}/{r['n_lo']:5d}")

    # ---------------------------------------------------------------- SECONDARY
    print("\n" + "-" * 100)
    print("SECONDARY (registered, diagnostic, no bar) — the WITHIN-COUNTRY version of U21's "
          "absorption result")
    print("-" * 100)
    tab_all = per_economy_gap(mi, "anydigpayment", online, offline, everyone)
    stats_all = describe(tab_all, "online - offline | ALL ADULTS")
    both = tab.merge(tab_all, on="economy", suffixes=("_acct", "_all"))
    both = both[both["qualifies_acct"] & both["qualifies_all"] & (both["gap_all"] > 0)]
    both["absorbed"] = 1 - both["gap_acct"] / both["gap_all"]
    print(f"\n    economies qualifying on BOTH bases with a positive all-adult gap: {len(both)}")
    if len(both):
        a = both["absorbed"]
        print(f"    MEDIAN absorption by account holding = {a.median():.1%} "
              f"(IQR {a.quantile(.25):.1%} to {a.quantile(.75):.1%}); U21's pooled figure 55.5%")
        print(f"    absorption > 0 in {(a > 0).sum()}/{len(a)} economies")

    # ------------------------------------------------------------------ VERDICT
    print("\n" + "=" * 100)
    print("VERDICT (pre-registered bars)")
    c1 = stats["median"] >= MEDIAN_BAR
    c2 = stats["share_pos"] >= SHARE_BAR
    sign_ok = stats["median"] > 0
    print(f"  C1  median within-economy gap {stats['median']:+.2f}pp "
          f"(bar >= +{MEDIAN_BAR:.1f}pp) -> {'PASS' if c1 else 'FAIL'}")
    print(f"  C2  positive in {stats['share_pos']:.1%} of qualifying economies "
          f"(bar >= {SHARE_BAR:.0%}) -> {'PASS' if c2 else 'FAIL'}")
    print(f"  B15 registered sign POSITIVE -> observed "
          f"{'POSITIVE, agrees' if sign_ok else 'NEGATIVE, DISAGREES'}")
    verdict = "KEEP" if (c1 and c2 and sign_ok) else "DISCARD"
    print(f"  -> U22 {verdict}")
    if verdict == "DISCARD":
        print("     Registered null reading: U21's pooled +13.6pp would then be a between-country")
        print("     composition fact and the connectivity row of the ruler could not be read as a")
        print("     within-economy regularity, unlike education (U19) and income (U20).")
    print("=" * 100)
    return {"stats": stats, "pooled_qual": pool_q, "pooled_all": pool_all,
            "wedge": pool_q - stats["median"], "verdict": verdict,
            "coverage": acct_n_qual / acct_n_all}


if __name__ == "__main__":
    run(Micro())
