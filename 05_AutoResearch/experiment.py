"""E20 (pre-registered): was the 2021->2024 formal-saving surge DISEQUALIZING within countries?
Weighted corr of delta(overall saving) vs delta(income gap in saving) 2021->2024, dev panel,
pop-weighted. Gap = richest 60% minus poorest 40% (country file `group == "income"` slices).
Hypothesis: where saving surged most, the within-country income gap widened most -> POSITIVE
correlation.

Motivation: E1/E10/E12/E14 mapped the CHANNELS of the surge (mobile money, wage digitalization,
digital payments -- one bundled digitalization phenomenon); E16/E17 mapped its LEVEL dynamics
(a depth phenomenon that diverged rather than converged across countries). Its WITHIN-COUNTRY
DISTRIBUTIONAL INCIDENCE has never been tested, and no experiment has ever used the income
slices. U4 (micro, KEEP) shows formal saving is steeply education-graded in the 2024 cross-
section, which makes a disequalizing surge plausible but not implied -- it could equally have
reached the poorest 40% first from a low base.

Declared caveats (pre-registered, not controlled): account growth and common income shocks
plausibly drive both sides, and the poorest-40 series starts from a lower base so identical
proportional gains mechanically widen a pp gap. Descriptive only.
"""
import pandas as pd

from harness import Findex, INDICATORS

RICH, POOR = "richest 60%", "poorest 40%"


def _slice_panel(fx: Findex, col: str, group2: str, years):
    """Wide per-country table (pp) of `col` for one within-country group slice,
    restricted to the developing balanced panel."""
    g = fx.pan_grp
    sub = g[(g["group"] == "income") & (g["group2"] == group2)
            & (g["incomegroupwb24"] != "High income") & (g["year"].isin(years))]
    return sub.pivot_table(index="countrynewwb", columns="year", values=col) * 100


def run(fx: Findex):
    sav = INDICATORS["saved_formally"]["headline"]  # fin17a_17a1_d
    print("E20 G3:", fx.gate_variant("saved_formally", sav))

    inc_frame = fx.pan_grp[(fx.pan_grp["group"] == "income")
                           & (fx.pan_grp["incomegroupwb24"] != "High income")]
    print("E20 G4 (income-slice frame, 2024):",
          fx.gate_coverage(inc_frame, sav, 2024, min_countries=30, min_pop_share=0.3))
    print("E20 G5: n/a -- no official aggregate exists for a within-country gap series")
    print()

    years = [2021, 2024]
    rich = _slice_panel(fx, sav, RICH, years)
    poor = _slice_panel(fx, sav, POOR, years)
    overall = fx.country_panel(fx.pan_dev, sav, years)

    gap21 = (rich[2021] - poor[2021]).rename("gap21")
    gap24 = (rich[2024] - poor[2024]).rename("gap24")
    d_gap = (gap24 - gap21).rename("d_gap")
    d_sav = (overall[2024] - overall[2021]).rename("d_sav")
    w = overall["pop"]

    common = (d_gap.dropna().index
              .intersection(d_sav.dropna().index)
              .intersection(w.dropna().index))

    # ---- descriptive context: dev aggregate levels and gap, pop-weighted
    pop = w.reindex(common)
    for label, tab in (("poorest 40%", poor), ("richest 60%", rich)):
        v21 = (tab[2021].reindex(common) * pop).sum() / pop.sum()
        v24 = (tab[2024].reindex(common) * pop).sum() / pop.sum()
        print(f"E20 dev aggregate saving, {label:12s}: {v21:5.1f} -> {v24:5.1f}pp "
              f"({v24 - v21:+.1f}pp)")
    agg_gap21 = (gap21.reindex(common) * pop).sum() / pop.sum()
    agg_gap24 = (gap24.reindex(common) * pop).sum() / pop.sum()
    print(f"E20 dev aggregate income GAP (rich60-poor40): {agg_gap21:5.1f} -> {agg_gap24:5.1f}pp "
          f"({agg_gap24 - agg_gap21:+.1f}pp)")
    print()

    r, n = fx.weighted_corr(d_sav.reindex(common), d_gap.reindex(common), pop)
    gjack = fx.gate_jackknife(d_sav.reindex(common), d_gap.reindex(common), pop)
    ret = (gjack["r_droptop"] / gjack["r_full"]) if gjack.get("r_full") else float("nan")
    print(f"E20 r(d_saving, d_gap) = {r:+.3f} (n={n})  "
          f"jack {gjack['r_full']:+.3f}->{gjack['r_droptop']:+.3f} (retention {ret:.2f})")
    print("E20 G6:", gjack)
    print()

    # Terciles of delta-saving vs mean delta-gap (dose-response).
    dfx = pd.DataFrame({"d_sav": d_sav.reindex(common), "d_gap": d_gap.reindex(common),
                        "pop": pop}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_sav"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_gap"] * g["pop"]).sum() / g["pop"].sum()
        sm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E20 d_saving tercile {t:4s} (mean d_sav {sm:+5.1f}pp): "
              f"mean d_gap = {wm:+.1f}pp  (n={len(g)})")
    print()
    print("E20 keep condition: r(d_saving, d_gap) >= +0.30 AND jackknife sign-stable + "
          "magnitude-retaining (r_droptop >= 0.5 x r_full)")


if __name__ == "__main__":
    run(Findex())
