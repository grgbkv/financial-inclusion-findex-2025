"""E13 (pre-registered): are institutional and mobile-money account growth complements or
substitutes in the 2021->2024 window? Delta(fiaccount_t_d) vs delta(mobileaccount_t_d),
2021->2024, dev panel, population-weighted.

Both fi_account and mobile_money are declared headlines in INDICATORS (G3 checked, not n/a).
Mobile and FI accounts are distinct components of the headline account_t_d, so a country can
grow one without the other -- this is not tautological. Positive r = co-development
(complements, the broad-digitalization reading behind E1/E10/E11/E12); negative r = leapfrogging
(substitution). Descriptive only.
"""
import pandas as pd

from harness import Findex, INDICATORS


def run(fx: Findex):
    fi_col = INDICATORS["fi_account"]["headline"]
    mm_col = INDICATORS["mobile_money"]["headline"]

    # G3: declare both variants against the registry
    print("E13", fx.gate_variant("fi_account", fi_col))
    print("E13", fx.gate_variant("mobile_money", mm_col))

    fi = fx.country_panel(fx.pan_dev, fi_col, [2021, 2024])
    d_fi = (fi[2024] - fi[2021]).rename("d_fiaccount_2124")

    mm = fx.country_panel(fx.pan_dev, mm_col, [2021, 2024])
    d_mm = (mm[2024] - mm[2021]).rename("d_mobileaccount_2124")

    w = fi["pop"]
    common = d_fi.dropna().index.intersection(d_mm.dropna().index)
    print(f"E13 dev-panel countries with both indicators in 2021 & 2024: n={len(common)}")

    r13, n13 = fx.weighted_corr(d_fi.reindex(common), d_mm.reindex(common), w.reindex(common))
    print(f"E13 weighted r(d_fiaccount, d_mobileaccount) 2021-24 = {r13:.3f}  (n={n13})")

    # G4 coverage on the mobile-money change (use 2024 availability)
    flag = fx.pan_dev.assign(mm_flag=fx.pan_dev[mm_col])
    gcov = fx.gate_coverage(flag, "mm_flag", 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(d_fi.reindex(common), d_mm.reindex(common), w.reindex(common))
    print("E13", gcov)
    print("E13", gjack)

    # terciles of FI-account change vs mean mobile-account change (descriptive shape)
    dfx = pd.DataFrame({"d_fi": d_fi.reindex(common), "d_mm": d_mm.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_fi"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_mm"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E13  d_fiaccount tercile {t:4s}: mean d_mobileaccount = {wm:+.1f}pp  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
