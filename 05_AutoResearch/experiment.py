"""E17 (pre-registered): is the 2021->2024 formal-saving surge a catch-up phenomenon? Weighted
corr of the 2021 formal-saving LEVEL vs delta(saving) 2021->2024, dev panel, pop-weighted, with
the same test on account_t_d as a comparison benchmark (depth margin vs access margin).

Motivation: E16 found the biggest account-growth economies are where saving surged least
(drop-top-5 r=0.741), and the prediction stream's two biggest wins (P11, P12) both work by
shrinking countries toward basin means -- both point at convergence structure in the 2021
levels. E5/E9 found the same catch-up shape on the access margin.

Declared confound (pre-registered, not controlled): level-vs-change regressions mechanically
inherit regression-to-the-mean from sampling error in the 2021 level, so a negative r is an
upper bound on true catch-up. The account benchmark shares that mechanical footing.
Descriptive only, no causal claim.
"""
import pandas as pd

from harness import Findex, INDICATORS


def _level_vs_change(fx: Findex, name: str, col: str, tag: str):
    print(f"E17 {tag}", fx.gate_variant(name, col))
    wide = fx.country_panel(fx.pan_dev, col, [2021, 2024])
    lvl = wide[2021].rename(f"{tag}_2021")
    chg = (wide[2024] - wide[2021]).rename(f"d_{tag}_2124")
    w = wide["pop"]

    common = lvl.dropna().index.intersection(chg.dropna().index)
    print(f"E17 {tag}: dev-panel countries with 2021 & 2024: n={len(common)}")

    r, n = fx.weighted_corr(lvl.reindex(common), chg.reindex(common), w.reindex(common))
    print(f"E17 {tag}: weighted r(level_2021, d_{tag}) = {r:.3f}  (n={n})")

    print(f"E17 {tag}", fx.gate_coverage(fx.pan_dev, col, 2024,
                                         min_countries=30, min_pop_share=0.3))
    gjack = fx.gate_jackknife(lvl.reindex(common), chg.reindex(common), w.reindex(common))
    print(f"E17 {tag}", gjack)
    if gjack.get("r_droptop") is not None and gjack.get("r_full"):
        rf, rd = gjack["r_full"], gjack["r_droptop"]
        print(f"E17 {tag}: magnitude-retention (E4 lesson): r_droptop/r_full = "
              f"{rd / rf:.3f}  (need >= 0.5)")

    dfx = pd.DataFrame({"lvl": lvl.reindex(common), "chg": chg.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["lvl"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["chg"] * g["pop"]).sum() / g["pop"].sum()
        lm = (g["lvl"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E17 {tag}:  2021-level tercile {t:4s} (mean lvl {lm:5.1f}pp): "
              f"mean change = {wm:+.1f}pp  (n={len(g)})")
    return r


def run(fx: Findex):
    sav_col = INDICATORS["saved_formally"]["headline"]
    acc_col = INDICATORS["account"]["headline"]

    r_sav = _level_vs_change(fx, "saved_formally", sav_col, "saving")
    print()
    r_acc = _level_vs_change(fx, "account", acc_col, "account")
    print()
    print(f"E17 comparison: depth-margin r={r_sav:.3f} vs access-margin r={r_acc:.3f}")
    print("E17 keep condition: saving r <= -0.30 AND jackknife sign-stable + "
          "magnitude-retaining")


if __name__ == "__main__":
    run(Findex())
