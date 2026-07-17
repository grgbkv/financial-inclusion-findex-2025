"""E15 (pre-registered): did the formal-saving surge buy resilience where it landed?
Delta(fin24aSD_ND) vs delta(fin17a_17a1_d), 2021->2024, dev panel, population-weighted.

The paper's headline puzzle: dev-panel resilience flat (54.7->54.5pp) while formal saving
surged. E7 showed the composition of emergency funds shifted toward savings where the surge
landed; E2 found d_resilience does NOT track d_mobile-money (r=0.189, discard). The direct
d_resilience ~ d_saving test has never been run. Both resilience and saved_formally are
declared headlines in INDICATORS (G3 checked). Descriptive only; common income shocks are a
plausible common driver of both sides.
"""
import pandas as pd

from harness import Findex, INDICATORS


def run(fx: Findex):
    res_col = INDICATORS["resilience"]["headline"]
    sav_col = INDICATORS["saved_formally"]["headline"]

    # G3: declare both variants against the registry
    print("E15", fx.gate_variant("resilience", res_col))
    print("E15", fx.gate_variant("saved_formally", sav_col))

    res = fx.country_panel(fx.pan_dev, res_col, [2021, 2024])
    d_res = (res[2024] - res[2021]).rename("d_resilience_2124")

    sav = fx.country_panel(fx.pan_dev, sav_col, [2021, 2024])
    d_sav = (sav[2024] - sav[2021]).rename("d_saving_2124")

    w = sav["pop"]
    common = d_res.dropna().index.intersection(d_sav.dropna().index)
    print(f"E15 dev-panel countries with both indicators in 2021 & 2024: n={len(common)}")

    r15, n15 = fx.weighted_corr(d_sav.reindex(common), d_res.reindex(common), w.reindex(common))
    print(f"E15 weighted r(d_saving, d_resilience) 2021-24 = {r15:.3f}  (n={n15})")

    # G4 coverage on resilience (2024 availability)
    gcov = fx.gate_coverage(fx.pan_dev, res_col, 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(d_sav.reindex(common), d_res.reindex(common), w.reindex(common))
    print("E15", gcov)
    print("E15", gjack)

    # terciles of saving change vs mean resilience change (descriptive shape)
    dfx = pd.DataFrame({"d_sav": d_sav.reindex(common), "d_res": d_res.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_sav"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_res"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E15  d_saving tercile {t:4s}: mean d_resilience = {wm:+.1f}pp  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
