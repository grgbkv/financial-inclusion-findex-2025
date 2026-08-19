"""U23 (pre-registered 2026-08-19): is the "last mile" education gradient in DIGITAL PAYMENT MODE
a property of the ADULT or of the PAYER? Three untouched payment streams.

Micro stream, 2024 wave, cross-sectional. Parent: U14 (first descendant).
Rules B2 (breadth cell: three untouched micro columns) and B17 (micro quota) are both paid here.

WHY. U14 found that among accountholding WAGE receivers the share paid into the account rather than
in cash is steeply education-graded, and U10/U15/U17/U18 found the same for self-directed
digital-payment use. Every one of those margins is chosen by the adult or set by an employer. The
three streams here differ in WHO picks the channel: a PENSION is paid by a government or pension
provider, an AGRICULTURAL payment by a buyer of produce, and a UTILITY bill is paid OUT by the adult.
If the gradient belongs to the adult it appears in all three.

CODING (disclosed in the pre-registration; structural check, not an outcome peek). All three columns
are coded identically to `receive_wages`: 1 = through an account, 2 = cash, 3 = other,
4 = did not participate, 5 = DK/RF. `domestic_remittances` was EXCLUDED: its four codes do not match
the family (code 4 has account 0.942 but anydigpayment 0.481) and cannot be read without a codebook.

REGISTERED PRIMARY: gap = rate(educ 3) - rate(educ 1) >= +5.0pp in ALL THREE streams, among
`account == 1` participants. REGISTERED SIGN (B15): POSITIVE.
SECONDARY 1: absorption = 1 - (conditional gap / unconditional gap); registered direction is
absorption BELOW the ruler's ~64%, bar median < 50%.
SECONDARY 2: within-economy median gap; fixed downgrade rule if median < 5pp or positive share < 60%.

GATES. M1 (module-enforced), M2 (n >= 100 on every reported cell), M3 on `account` (the stream
margins have no country-file equivalent at this conditional granularity).
"""
import numpy as np
import pandas as pd

from micro import Micro

MIN_CELL = 100
GAP_BAR = 5.0            # primary, per stream
ABSORB_BAR = 0.50        # secondary 1: median absorption must be BELOW this to confirm
WITHIN_MEDIAN_BAR = 5.0  # secondary 2 downgrade rule
WITHIN_SHARE_BAR = 0.60  # secondary 2 downgrade rule

STREAMS = {
    "receive_pensions":    "pension receipt      (payer: government / pension provider)",
    "receive_agriculture": "agricultural payment (payer: buyer of produce)",
    "pay_utilities":       "utility bill payment (payer: THE ADULT, self-directed)",
}
REFERENCE = ("receive_wages", "wage receipt         (payer: employer)  -- U14's margin, reference")

EDUC = {1: "primary or less", 2: "secondary", 3: "tertiary"}
M3_ECONOMIES = ["India", "Kazakhstan", "Poland", "Estonia", "Uzbekistan", "Brazil", "Nigeria",
                "Indonesia", "Turkiye", "Mexico"]


def digital_rate(mi, stream, base, educ_code=None, economy=None):
    """Weighted share of stream participants whose payment runs THROUGH AN ACCOUNT (code 1),
    within `base`. Returns (rate_pp, unweighted n of the participant cell)."""
    df = mi.df
    m = base & df[stream].isin([1, 2, 3])
    if educ_code is not None:
        m = m & (df["educ"] == educ_code)
    if economy is not None:
        m = m & (df["economy"] == economy)
    sub = df[m].dropna(subset=["wgt"])
    if sub.empty:
        return np.nan, 0
    y = (sub[stream] == 1).astype(float)
    return float(np.average(y, weights=sub["wgt"])) * 100, int(len(sub))


def pooled_block(mi, stream, base, label):
    rows = []
    for code, name in EDUC.items():
        r, n = digital_rate(mi, stream, base, educ_code=code)
        rows.append({"educ": name, "digital_pp": round(r, 2) if pd.notna(r) else np.nan,
                     "n_unweighted": n, "M2_ok": n >= MIN_CELL})
    tab = pd.DataFrame(rows)
    gap = tab.loc[tab["educ"] == "tertiary", "digital_pp"].iloc[0] - \
        tab.loc[tab["educ"] == "primary or less", "digital_pp"].iloc[0]
    print(f"\n  {label}")
    print(tab.to_string(index=False))
    print(f"    gap (tertiary - primary) = {gap:+.2f}pp   M2 all cells: "
          f"{bool(tab['M2_ok'].all())}")
    return float(gap), bool(tab["M2_ok"].all())


def within_economy(mi, stream, base):
    """Per-economy gap, M2 on BOTH education cells."""
    df = mi.df
    rows = []
    for econ in sorted(df["economy"].dropna().unique()):
        hi, n_hi = digital_rate(mi, stream, base, educ_code=3, economy=econ)
        lo, n_lo = digital_rate(mi, stream, base, educ_code=1, economy=econ)
        if n_hi >= MIN_CELL and n_lo >= MIN_CELL and pd.notna(hi) and pd.notna(lo):
            rows.append({"economy": econ, "gap_pp": hi - lo, "n_hi": n_hi, "n_lo": n_lo})
    return pd.DataFrame(rows)


def main():
    mi = Micro()
    df = mi.df
    acct = df["account"] == 1
    everyone = pd.Series(True, index=df.index)

    print("=" * 92)
    print("U23 — the education gradient in DIGITAL PAYMENT MODE across three untouched streams")
    print("=" * 92)

    m3 = mi.gate_country_file("account", "account_t_d", M3_ECONOMIES, tol_pp=1.0)
    print(f"\nM3 (account vs country file, {m3.get('n_economies')} economies): {m3}")

    print("\n--- participant base sizes (accountholders, codes 1/2/3) ---")
    for s in list(STREAMS) + [REFERENCE[0]]:
        _, n = digital_rate(mi, s, acct)
        _, n_all = digital_rate(mi, s, everyone)
        econ = df.loc[acct & df[s].isin([1, 2, 3]), "economy"].nunique()
        print(f"  {s:22s} n(accountholders)={n:6d}  n(all adults)={n_all:6d}  economies={econ}")

    results = {}
    print("\n" + "=" * 92)
    print("PRIMARY — conditional on holding an account")
    print("=" * 92)
    for s, label in STREAMS.items():
        gap, m2 = pooled_block(mi, s, acct, f"{s}: {label}")
        results[s] = {"gap_cond": gap, "m2": m2}
    gap_ref, m2_ref = pooled_block(mi, REFERENCE[0], acct, f"{REFERENCE[0]}: {REFERENCE[1]}")

    print("\n" + "=" * 92)
    print("SECONDARY 1 — unconditional gap and the ACCESS-ABSORPTION share")
    print("=" * 92)
    for s, label in STREAMS.items():
        gap_u, m2_u = pooled_block(mi, s, everyone, f"{s} (ALL adults): {label}")
        results[s]["gap_uncond"] = gap_u
        results[s]["m2_uncond"] = m2_u
        results[s]["absorption"] = 1 - (results[s]["gap_cond"] / gap_u) if gap_u else np.nan
    gap_ref_u, _ = pooled_block(mi, REFERENCE[0], everyone, f"{REFERENCE[0]} (ALL adults)")

    print("\n" + "=" * 92)
    print("SECONDARY 2 — WITHIN-ECONOMY gaps (M2 >= 100 on both education cells)")
    print("=" * 92)
    for s in STREAMS:
        w = within_economy(mi, s, acct)
        if w.empty:
            print(f"\n  {s}: NO economy qualifies on M2 in both cells — within-country test "
                  f"cannot be run.")
            results[s].update({"n_qual": 0, "within_median": np.nan, "within_share": np.nan,
                               "cover": np.nan})
            continue
        base_n = int((acct & df[s].isin([1, 2, 3])).sum())
        qual_n = int(df[df["economy"].isin(w["economy"]) & acct & df[s].isin([1, 2, 3])].shape[0])
        med = float(w["gap_pp"].median())
        share = float((w["gap_pp"] > 0).mean())
        pooled_qual, _ = digital_rate(
            mi, s, acct & df["economy"].isin(w["economy"]) & (df["educ"] == 3))
        pooled_qual_lo, _ = digital_rate(
            mi, s, acct & df["economy"].isin(w["economy"]) & (df["educ"] == 1))
        wedge = (pooled_qual - pooled_qual_lo) - med
        print(f"\n  {s}: {len(w)} economies qualify, holding {qual_n/base_n:.1%} of "
              f"accountholding participants")
        print(f"    median gap {med:+.2f}pp | IQR [{w['gap_pp'].quantile(.25):+.2f}, "
              f"{w['gap_pp'].quantile(.75):+.2f}] | positive in {int((w['gap_pp']>0).sum())}/"
              f"{len(w)} ({share:.1%})")
        print(f"    pooled gap over the SAME qualifying set {pooled_qual - pooled_qual_lo:+.2f}pp"
              f"  ->  composition wedge {wedge:+.2f}pp")
        ext = w.sort_values("gap_pp")
        print(f"    range: {ext.iloc[0]['economy']} {ext.iloc[0]['gap_pp']:+.1f} ... "
              f"{ext.iloc[-1]['economy']} {ext.iloc[-1]['gap_pp']:+.1f}")
        results[s].update({"n_qual": len(w), "within_median": med, "within_share": share,
                           "cover": qual_n / base_n})

    print("\n" + "=" * 92)
    print("VERDICT against the registered bars")
    print("=" * 92)
    print(f"\n  reference (U14's wage margin, not part of the bar): conditional gap "
          f"{gap_ref:+.2f}pp, unconditional {gap_ref_u:+.2f}pp, "
          f"absorption {1 - gap_ref/gap_ref_u:.1%}")
    ok = []
    for s in STREAMS:
        r = results[s]
        passed = (r["gap_cond"] >= GAP_BAR) and r["m2"]
        ok.append(passed)
        down = ""
        if passed and pd.notna(r["within_median"]):
            if r["within_median"] < WITHIN_MEDIAN_BAR or r["within_share"] < WITHIN_SHARE_BAR:
                down = "  [DOWNGRADE: pooled only, composition-suspect]"
        print(f"  {s:22s} gap {r['gap_cond']:+7.2f}pp  {'PASS' if passed else 'FAIL'}"
              f"   (sign {'as registered' if r['gap_cond'] > 0 else 'OPPOSITE to registered'})"
              f"   within-median {r['within_median']:+.2f}pp"
              f" pos {r['within_share']:.0%} on {r['n_qual']} economies{down}")
    absorptions = [results[s]["absorption"] for s in STREAMS]
    med_abs = float(np.nanmedian(absorptions))
    print(f"\n  absorption by stream: " +
          ", ".join(f"{s}={results[s]['absorption']:.1%}" for s in STREAMS))
    print(f"  median absorption {med_abs:.1%} vs registered bar < {ABSORB_BAR:.0%}: "
          f"{'CONFIRMED' if med_abs < ABSORB_BAR else 'REJECTED'}")
    print(f"\n  PRIMARY: {sum(ok)}/3 streams clear +{GAP_BAR}pp  -> "
          f"{'KEEP' if all(ok) else 'DISCARD (registered all-three bar not met)'}")


if __name__ == "__main__":
    main()
