"""E11 (pre-registered): broad financial deepening vs saving-specific surge.
Delta(fin22a_22a1_22g_d) (formal borrowing) 2021->2024 vs delta(fin17a_17a1_d) (formal
saving) 2021->2024, dev panel, population-weighted.

Both indicators are declared headlines in INDICATORS (borrowed_formally / saved_formally),
so G3 is checked against the registry (not n/a). A strong positive r reads as broad
balance-sheet deepening; a null sharpens the 2021-24 surge as saving-specific.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    sav_col = INDICATORS["saved_formally"]["headline"]
    bor_col = INDICATORS["borrowed_formally"]["headline"]

    # G3: declare both variants against the registry
    print("E11", fx.gate_variant("saved_formally", sav_col))
    print("E11", fx.gate_variant("borrowed_formally", bor_col))

    sav = fx.country_panel(fx.pan_dev, sav_col, [2021, 2024])
    d_sav = (sav[2024] - sav[2021]).rename("d_saved_formally_2124")

    bor = fx.country_panel(fx.pan_dev, bor_col, [2021, 2024])
    d_bor = (bor[2024] - bor[2021]).rename("d_borrowed_formally_2124")

    w = sav["pop"]
    common = d_sav.dropna().index.intersection(d_bor.dropna().index)
    print(f"E11 dev-panel countries with both indicators in 2021 & 2024: n={len(common)}")

    r11, n11 = fx.weighted_corr(d_bor.reindex(common), d_sav.reindex(common), w.reindex(common))
    print(f"E11 weighted r(d_borrowed_formally, d_saved_formally) 2021-24 = {r11:.3f}  (n={n11})")

    # G4 coverage on the borrowing change (use 2024 availability)
    flag = fx.pan_dev.assign(bor_flag=fx.pan_dev[bor_col])
    gcov = fx.gate_coverage(flag, "bor_flag", 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(d_bor.reindex(common), d_sav.reindex(common), w.reindex(common))
    print("E11", gcov)
    print("E11", gjack)

    # terciles of borrowing change vs mean saving change (descriptive shape)
    import pandas as pd
    dfx = pd.DataFrame({"d_bor": d_bor.reindex(common), "d_sav": d_sav.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_bor"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E11  d_borrow tercile {t:4s}: mean d_saved_formally = {wm:+.1f}pp  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
