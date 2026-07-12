"""E10 (pre-registered): wage digitalization as a distinct channel for the 2021-24
formal-saving surge. Delta(fin32_acc) 2021->2024 vs delta(fin17a_17a1_d) 2021->2024,
dev panel, population-weighted.

fin32_acc (share of adults receiving private-sector wages into an account) has no
headline/narrow variant in INDICATORS (single indicator), so G3 is declared n/a rather
than checked against the registry -- same handling as E8 (fin11a) and E9 (fing2p_acc).
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    sav = fx.country_panel(fx.pan_dev, INDICATORS["saved_formally"]["headline"], [2021, 2024])
    d_sav = (sav[2024] - sav[2021]).rename("d_saved_formally_2124")

    wage = fx.country_panel(fx.pan_dev, "fin32_acc", [2021, 2024])
    d_wage = (wage[2024] - wage[2021]).rename("d_wagedigital_2124")

    w = sav["pop"]
    common = d_sav.dropna().index.intersection(d_wage.dropna().index)
    print(f"E10 dev-panel countries with fin32_acc in both 2021 & 2024: n={len(common)}")

    r10, n10 = fx.weighted_corr(d_wage.reindex(common), d_sav.reindex(common), w.reindex(common))
    print(f"E10 weighted r(d_wagedigital, d_saved_formally) 2021-24 = {r10:.3f}  (n={n10})")

    # G4 coverage on the wage-digitalization change (use 2024 availability)
    flag = fx.pan_dev.assign(fin32_flag=fx.pan_dev["fin32_acc"])
    gcov = fx.gate_coverage(flag, "fin32_flag", 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(d_wage.reindex(common), d_sav.reindex(common), w.reindex(common))
    print("E10", gcov)
    print("E10", gjack)

    # terciles of wage-digitalization change vs mean saving change (descriptive shape)
    import pandas as pd
    dfx = pd.DataFrame({"d_wage": d_wage.reindex(common), "d_sav": d_sav.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_wage"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E10  d_wage tercile {t:4s}: mean d_saved_formally = {wm:+.1f}pp  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
