"""E21 (pre-registered, with a disclosed partial peek): was the 2021->2024 widening of the
within-country income gap in formal saving GENUINE disequalization, or the mechanical arithmetic
of a lower poorest-40 base?

E20 found the pp gap widened 14.4 -> 20.5pp (poorest 40% +10.8pp, richest 60% +16.9pp) but logged
that as descriptive context, not a keep, precisely because "identical proportional gains from a
lower base mechanically widen a pp gap" — and left the scale-free re-test as an explicit candidate
for its own pre-registration. This is that experiment.

PEEK DISCLOSURE (amendment #1): E20's logged aggregate levels make the AGGREGATE ratio comparison
derivable by arithmetic (x1.59 vs x1.52) without touching the data, so the aggregate-scale
direction was not unknown at registration. The aggregate ratio is therefore reported as
exploratory context and any keep here is recorded as keep-exploratory. The registered statistics
are country-level and were genuinely unknown: the pop-weighted mean within-country change in the
LOG-ODDS gap, its sign share, and its dose-response against the overall surge.

Primary   : pop-weighted mean dL, where L_y = logit(rich60_y) - logit(poor40_y); keep if >= +0.20
            log-odds, level-jackknife sign-stable, and >= 60% of economies sharing the sign.
Secondary : weighted r(d_saving_overall, dL) — the scale-free version of the dose-response E20
            rejected on the pp scale (r=+0.179); keeps separately if r >= +0.30 with G6 clean.

Declared caveats: log-odds is scale-free but not confound-free (account growth and common income
shocks move both slices); the poor40/rich60 cut is coarse; rates are clipped to [0.5, 99.5]pp as a
continuity correction since logit is undefined at 0/1. Descriptive only, never causal.
"""
import numpy as np
import pandas as pd

from harness import Findex, INDICATORS

RICH, POOR = "richest 60%", "poorest 40%"
CLIP_LO, CLIP_HI = 0.5, 99.5   # pp, declared continuity correction for the logit


def _slice_panel(fx: Findex, col: str, group2: str, years):
    """Wide per-country table (pp) of `col` for one within-country income slice,
    restricted to the developing balanced panel. Identical construction to E20."""
    g = fx.pan_grp
    sub = g[(g["group"] == "income") & (g["group2"] == group2)
            & (g["incomegroupwb24"] != "High income") & (g["year"].isin(years))]
    return sub.pivot_table(index="countrynewwb", columns="year", values=col) * 100


def _logit_pp(s: pd.Series) -> pd.Series:
    """logit of a rate given in pp, with the declared clip."""
    p = s.clip(CLIP_LO, CLIP_HI) / 100.0
    return np.log(p / (1 - p))


def run(fx: Findex):
    sav = INDICATORS["saved_formally"]["headline"]  # fin17a_17a1_d
    print("E21 G3:", fx.gate_variant("saved_formally", sav))

    inc_frame = fx.pan_grp[(fx.pan_grp["group"] == "income")
                           & (fx.pan_grp["incomegroupwb24"] != "High income")]
    print("E21 G4 (income-slice frame, 2024):",
          fx.gate_coverage(inc_frame, sav, 2024, min_countries=30, min_pop_share=0.3))
    print("E21 G5: n/a -- no official aggregate exists for a within-country gap series")
    print()

    years = [2021, 2024]
    rich = _slice_panel(fx, sav, RICH, years)
    poor = _slice_panel(fx, sav, POOR, years)
    overall = fx.country_panel(fx.pan_dev, sav, years)

    L21 = (_logit_pp(rich[2021]) - _logit_pp(poor[2021])).rename("L21")
    L24 = (_logit_pp(rich[2024]) - _logit_pp(poor[2024])).rename("L24")
    dL = (L24 - L21).rename("dL")
    d_sav = (overall[2024] - overall[2021]).rename("d_sav")
    w = overall["pop"]

    common = (dL.dropna().index
              .intersection(d_sav.dropna().index)
              .intersection(w.dropna().index))
    pop = w.reindex(common)
    print(f"E21 estimation sample: n={len(common)} dev-panel economies with both income "
          f"slices in 2021 and 2024 (E20 used the same construction, n=55)")
    print()

    # ---- exploratory context (peek-disclosed): aggregate levels and the RATIO scale
    for label, tab in (("poorest 40%", poor), ("richest 60%", rich)):
        v21 = (tab[2021].reindex(common) * pop).sum() / pop.sum()
        v24 = (tab[2024].reindex(common) * pop).sum() / pop.sum()
        print(f"E21 [exploratory] dev aggregate saving, {label:12s}: {v21:5.1f} -> {v24:5.1f}pp "
              f"({v24 - v21:+.1f}pp, ratio x{v24 / v21:.3f})")
    print("E21 [exploratory] the ratio comparison above was derivable from E20's logged "
          "aggregates -> context only, cannot support a clean pre-registered keep")
    print()

    # ---- PRIMARY: pop-weighted mean change in the log-odds gap
    mean_dL = float((dL.reindex(common) * pop).sum() / pop.sum())
    agg_L21 = float((L21.reindex(common) * pop).sum() / pop.sum())
    agg_L24 = float((L24.reindex(common) * pop).sum() / pop.sum())
    share_pos = float((dL.reindex(common) > 0).mean() * 100)

    keep_idx = pop.sort_values(ascending=False).index[5:]   # level-jackknife: drop top-5 pop
    pop_j = pop.reindex(keep_idx)
    mean_dL_jack = float((dL.reindex(keep_idx) * pop_j).sum() / pop_j.sum())

    print(f"E21 PRIMARY pop-weighted log-odds gap: {agg_L21:+.3f} -> {agg_L24:+.3f}  "
          f"mean dL = {mean_dL:+.3f} (odds ratio x{np.exp(mean_dL):.3f})")
    print(f"E21 level jackknife (drop top-5 pop): mean dL = {mean_dL_jack:+.3f}  "
          f"(sign-stable: {np.sign(mean_dL_jack) == np.sign(mean_dL)})")
    print(f"E21 share of economies with dL > 0: {share_pos:.1f}%  (n={len(common)})")
    print("E21 primary keep condition: mean dL >= +0.20 AND jackknife sign-stable AND "
          "share sharing sign >= 60%")
    print()

    # ---- SECONDARY: scale-free dose-response (association -> G6 applies)
    r, n = fx.weighted_corr(d_sav.reindex(common), dL.reindex(common), pop)
    gjack = fx.gate_jackknife(d_sav.reindex(common), dL.reindex(common), pop)
    ret = (gjack["r_droptop"] / gjack["r_full"]) if gjack.get("r_full") else float("nan")
    print(f"E21 SECONDARY r(d_saving, dL) = {r:+.3f} (n={n})  "
          f"jack {gjack['r_full']:+.3f}->{gjack['r_droptop']:+.3f} (retention {ret:.2f})")
    print("E21 G6:", gjack)
    print("E21 secondary keep condition: r >= +0.30 AND jackknife sign-stable + "
          "magnitude-retaining (r_droptop >= 0.5 x r_full)")
    print()

    # ---- descriptive: terciles of the overall surge vs mean dL (scale-free dose-response)
    dfx = pd.DataFrame({"d_sav": d_sav.reindex(common), "dL": dL.reindex(common),
                        "pop": pop}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_sav"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["dL"] * g["pop"]).sum() / g["pop"].sum()
        sm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E21 d_saving tercile {t:4s} (mean d_sav {sm:+5.1f}pp): "
              f"mean dL = {wm:+.3f}  (n={len(g)})")


if __name__ == "__main__":
    run(Findex())
