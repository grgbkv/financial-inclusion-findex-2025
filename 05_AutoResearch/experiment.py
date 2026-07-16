"""E14 (pre-registered): are the digitalization on-ramps bundled? Delta(mobileaccount_t_d) vs
delta(g20_any), 2021->2024, dev panel, population-weighted.

E1 linked Delta(mobile-money) to the saving surge (r=0.719); E12 linked Delta(digital-payment)
to the same surge (r=0.370), treating them as separate channels. If Delta(mobile-money) and
Delta(g20) are themselves strongly correlated, the "four distinct channels" framing is better
read as one bundled digitalization phenomenon. Both mobile_money and digital_payment are declared
headlines in INDICATORS (G3 checked). Distinct from E13 (FI vs mobile) and E5 (g20/account ratio).
Descriptive only; account growth is a plausible common driver of both sides.
"""
import pandas as pd

from harness import Findex, INDICATORS


def run(fx: Findex):
    mm_col = INDICATORS["mobile_money"]["headline"]
    g20_col = INDICATORS["digital_payment"]["headline"]

    # G3: declare both variants against the registry
    print("E14", fx.gate_variant("mobile_money", mm_col))
    print("E14", fx.gate_variant("digital_payment", g20_col))

    mm = fx.country_panel(fx.pan_dev, mm_col, [2021, 2024])
    d_mm = (mm[2024] - mm[2021]).rename("d_mobileaccount_2124")

    g20 = fx.country_panel(fx.pan_dev, g20_col, [2021, 2024])
    d_g20 = (g20[2024] - g20[2021]).rename("d_g20_2124")

    w = mm["pop"]
    common = d_mm.dropna().index.intersection(d_g20.dropna().index)
    print(f"E14 dev-panel countries with both indicators in 2021 & 2024: n={len(common)}")

    r14, n14 = fx.weighted_corr(d_mm.reindex(common), d_g20.reindex(common), w.reindex(common))
    print(f"E14 weighted r(d_mobileaccount, d_g20) 2021-24 = {r14:.3f}  (n={n14})")

    # G4 coverage on g20 (2024 availability)
    flag = fx.pan_dev.assign(g20_flag=fx.pan_dev[g20_col])
    gcov = fx.gate_coverage(flag, "g20_flag", 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(d_mm.reindex(common), d_g20.reindex(common), w.reindex(common))
    print("E14", gcov)
    print("E14", gjack)

    # terciles of mobile-money change vs mean digital-payment change (descriptive shape)
    dfx = pd.DataFrame({"d_mm": d_mm.reindex(common), "d_g20": d_g20.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_mm"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_g20"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E14  d_mobileaccount tercile {t:4s}: mean d_g20 = {wm:+.1f}pp  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
