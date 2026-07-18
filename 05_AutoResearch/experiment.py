"""E16 (pre-registered): does the 2021->2024 formal-saving surge co-move with account-ownership
growth itself? Delta(account_t_d) vs delta(fin17a_17a1_d), 2021->2024, dev panel, pop-weighted.

Every kept digitalization-bundle finding (E1 mobile money, E10 wage digitalization, E11 formal
borrowing, E12 digital payments, E13 fi/mm, E14 mm/g20) carries the standing caveat "account
growth a plausible common driver (noted, not controlled)." That common driver has never been
tested directly. Both account and saved_formally are declared INDICATORS headlines (G3).
Descriptive only; account growth and saving depth share income-shock and digitalization
drivers (noted, not controlled).
"""
import pandas as pd

from harness import Findex, INDICATORS


def run(fx: Findex):
    acc_col = INDICATORS["account"]["headline"]
    sav_col = INDICATORS["saved_formally"]["headline"]

    print("E16", fx.gate_variant("account", acc_col))
    print("E16", fx.gate_variant("saved_formally", sav_col))

    acc = fx.country_panel(fx.pan_dev, acc_col, [2021, 2024])
    d_acc = (acc[2024] - acc[2021]).rename("d_account_2124")

    sav = fx.country_panel(fx.pan_dev, sav_col, [2021, 2024])
    d_sav = (sav[2024] - sav[2021]).rename("d_saving_2124")

    w = sav["pop"]
    common = d_acc.dropna().index.intersection(d_sav.dropna().index)
    print(f"E16 dev-panel countries with both indicators in 2021 & 2024: n={len(common)}")

    r16, n16 = fx.weighted_corr(d_acc.reindex(common), d_sav.reindex(common), w.reindex(common))
    print(f"E16 weighted r(d_account, d_saving) 2021-24 = {r16:.3f}  (n={n16})")

    gcov = fx.gate_coverage(fx.pan_dev, acc_col, 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(d_acc.reindex(common), d_sav.reindex(common), w.reindex(common))
    print("E16", gcov)
    print("E16", gjack)
    if gjack.get("r_droptop") is not None:
        rf, rd = gjack["r_full"], gjack["r_droptop"]
        print(f"E16 magnitude-retention (E4 lesson): r_droptop/r_full = "
              f"{rd/rf:.3f}  (need >= 0.5)")

    dfx = pd.DataFrame({"d_acc": d_acc.reindex(common), "d_sav": d_sav.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_acc"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E16  d_account tercile {t:4s}: mean d_saving = {wm:+.1f}pp  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
