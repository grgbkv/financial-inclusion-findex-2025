"""E12 (pre-registered): digital-payment adoption as a fourth channel of the saving surge.
Delta(g20_any) (any digital payment) 2021->2024 vs delta(fin17a_17a1_d) (formal saving)
2021->2024, dev panel, population-weighted.

g20_any is the declared digital_payment headline and fin17a_17a1_d the saved_formally
headline in INDICATORS, so G3 is checked against the registry (not n/a). A strong positive r
adds digital-payment usage to E1 (mobile money) / E10 (wage rails) / E11 (borrowing) as a
broad-digitalization channel of the 2021-24 formal-saving surge; a null bounds the channel set.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    sav_col = INDICATORS["saved_formally"]["headline"]
    dig_col = INDICATORS["digital_payment"]["headline"]

    # G3: declare both variants against the registry
    print("E12", fx.gate_variant("saved_formally", sav_col))
    print("E12", fx.gate_variant("digital_payment", dig_col))

    sav = fx.country_panel(fx.pan_dev, sav_col, [2021, 2024])
    d_sav = (sav[2024] - sav[2021]).rename("d_saved_formally_2124")

    dig = fx.country_panel(fx.pan_dev, dig_col, [2021, 2024])
    d_dig = (dig[2024] - dig[2021]).rename("d_g20_any_2124")

    w = sav["pop"]
    common = d_sav.dropna().index.intersection(d_dig.dropna().index)
    print(f"E12 dev-panel countries with both indicators in 2021 & 2024: n={len(common)}")

    r12, n12 = fx.weighted_corr(d_dig.reindex(common), d_sav.reindex(common), w.reindex(common))
    print(f"E12 weighted r(d_g20_any, d_saved_formally) 2021-24 = {r12:.3f}  (n={n12})")

    # G4 coverage on the digital-payment change (use 2024 availability)
    flag = fx.pan_dev.assign(dig_flag=fx.pan_dev[dig_col])
    gcov = fx.gate_coverage(flag, "dig_flag", 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(d_dig.reindex(common), d_sav.reindex(common), w.reindex(common))
    print("E12", gcov)
    print("E12", gjack)

    # terciles of digital-payment change vs mean saving change (descriptive shape)
    import pandas as pd
    dfx = pd.DataFrame({"d_dig": d_dig.reindex(common), "d_sav": d_sav.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_dig"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E12  d_g20_any tercile {t:4s}: mean d_saved_formally = {wm:+.1f}pp  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
