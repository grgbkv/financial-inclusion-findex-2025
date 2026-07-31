"""Prediction stream — P22: is the shrinkage gain a genuine basin location, or a BIG-COUNTRY PULL?

Champion (P18): saving = damped trend (l=0.5) + region -> income-group -> account-tercile ->
g20-tercile shrink (6.831), account = persistence + income-group -> region -> g20-tercile shrink
(5.014), resilience = persistence + region shrink (6.625).

The shrinkage-stacking seam is mined out: five consecutive experiments (P14, P15, P19, P20, P21)
failed to move the champion, three of them rejected at the CV gate without reaching the holdout,
and P21 settled that saving stops at four stages and account at three. Adding a sixth stage is not
the experiment.

What has never been varied is the shrinkage TARGET itself. Every stage since P5 shrinks a country
toward its basin's POPULATION-WEIGHTED MEAN -- a location statistic dominated, inside each basin, by
the same handful of giant countries (India, China, Indonesia, Nigeria, Pakistan) that gate G6 exists
to guard against on the hypothesis side. If the gains since P11 are genuine noise correction they
should survive -- or improve -- under a ROBUST basin center; if they are partly a big-country pull,
a robust center will hurt.

P22 candidate: replace the basin center with the UNWEIGHTED MEDIAN of the basin's member values, at
EVERY stage, per target. Nothing else changes: k = 0.1, the damped trend (l = 0.5), the basin
sequences and the adopted stage counts all stay exactly as in the P18 champion.

Adoption rule (entirely <=2021, no 2024 in features, fitting or selection): per target, CV on that
target's 2017->2021 transition with a persistence base, all basins built at 2017 (the
P10/P12/P13/P16/P17/P18/P19/P20/P21 protocol), comparing the incumbent mean-centered stack against
the identical median-centered stack. Per the P14/P15/P19/P20/P21 protocol, a target whose CV does
not prefer the candidate is not evaluated on 2024 and keeps its champion prediction byte-identical.
RESILIENCE IS EXCLUDED BY DESIGN and stays byte-identical at 6.625: its CV is infeasible
(fin24aSD_ND exists only in 2021) and the account-transition proxy is twice on record as
mis-selecting for it (P8, P13).

Declared: this is an estimator-robustness experiment, not a search for a new stage; the unweighted
median deliberately discards the population weighting INSIDE the basin, so it is the opposite
extreme from the incumbent rather than a mild variant -- a middle option (weighted median) is left
untested and noted as a follow-up if the extreme rejects narrowly.
"""
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
INCOME_BASIN = "incomegroupwb24"   # P7 champion basin for account
REGION_BASIN = "regionwb24_hi"     # P5/P11 champion basin for resilience & saving stage 1

# Per-target basin order: (stage-1 basin, candidate stage-2 basin)
BASIN_ORDER = {
    "account_t_d": (INCOME_BASIN, REGION_BASIN),
    "fin24aSD_ND": (REGION_BASIN, INCOME_BASIN),
    "fin17a_17a1_d": (REGION_BASIN, INCOME_BASIN),  # P12, fixed
}

# Per-target stage-3 DATA-DRIVEN basin: terciles of another indicator's level (P16/P17, fixed).
THIRD_BASIN_COL = {
    "fin17a_17a1_d": "account_t_d",
    "account_t_d": "g20_any",
}

# Per-target stage-4 DATA-DRIVEN basin: a SECOND cross-indicator basin (P18, fixed for saving).
FOURTH_BASIN_COL = {
    "fin17a_17a1_d": "g20_any",
}

# P22: which targets may have their basin CENTER re-selected. Resilience is excluded by design
# (no pre-2021 transition; the account proxy mis-selects for it -- P8, P13).
CENTER_CANDIDATES = ["account_t_d", "fin17a_17a1_d"]


def _tercile_basin(train, col, at_year):
    """Data-driven basin: terciles of `col`'s level at `at_year`. Built from <=2021 data only;
    cuts across region and income group."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")[col].dropna()
    if len(ref) < 9:
        return pd.Series(dtype=object)
    return pd.qcut(ref, 3, labels=["ter_low", "ter_mid", "ter_high"]).astype(object)


def _shrink(train, last, k, basin, at_year=2021, center="mean"):
    """Shrink `last` toward its basin's center at `at_year`.
    `basin` is either a column name in the train frame or a ready country-indexed Series.
    `center` is the P22 axis: "mean" = population-weighted mean (the P5-P18 incumbent),
    "median" = unweighted median of the basin's member values (the robust candidate)."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    basin_s = ref[basin] if isinstance(basin, str) else basin.reindex(ref.index)
    pop = ref["pop_adult"]
    d = pd.DataFrame({"last": last, "basin": basin_s, "pop": pop}).dropna(
        subset=["last", "basin"])
    if center == "median":
        grp_center = d.groupby("basin")["last"].median()
    else:
        grp_center = d.groupby("basin").apply(
            lambda g: (g["last"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    d["grp_center"] = d["basin"].map(grp_center)
    shrunk = d["last"] - k * (d["last"] - d["grp_center"])
    return shrunk.reindex(last.index).fillna(last)


def _stack(train, base_pred, target, at_year, center, use_two, use_three, use_four,
           third_basin, fourth_basin):
    """Apply the target's ADOPTED shrink stages, in order, with the given basin center.
    Stage membership is the P18 champion's and is not re-selected here — P22 varies only the
    center statistic."""
    b1, b2 = BASIN_ORDER[target]
    pred = _shrink(train, base_pred, SHRINK_K, b1, at_year=at_year, center=center)
    if use_two.get(target):
        pred = _shrink(train, pred, SHRINK_K, b2, at_year=at_year, center=center)
    if use_three.get(target):
        pred = _shrink(train, pred, SHRINK_K, third_basin[target], at_year=at_year, center=center)
    if use_four.get(target):
        pred = _shrink(train, pred, SHRINK_K, fourth_basin[target], at_year=at_year, center=center)
    return pred


def _select_two_stage(fx: Findex, target: str):
    """Pre-2021 CV (P13): single vs two-stage shrink on the 2017->2021 transition."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    b1, b2 = BASIN_ORDER[target]
    single = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    two_stage = _shrink(train, single, SHRINK_K, b2, at_year=2017)
    mae_single = float((single.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_two = float((two_stage.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_two = mae_two < mae_single
    print(f"P13 pre-2021 CV {target:16s} (2017->2021): single={mae_single:.3f} "
          f"two_stage={mae_two:.3f}  -> two_stage={use_two}  (n={len(common)})")
    return use_two


def _select_third_stage(fx: Findex, target: str):
    """P16/P17 pre-2021 CV: two-stage vs three-stage, all basins built at 2017."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    b1, b2 = BASIN_ORDER[target]
    b3 = _tercile_basin(train, THIRD_BASIN_COL[target], 2017)
    s1 = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    s2 = _shrink(train, s1, SHRINK_K, b2, at_year=2017)
    s3 = _shrink(train, s2, SHRINK_K, b3, at_year=2017)
    mae_two = float((s2.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_three = float((s3.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_three = mae_three < mae_two
    tag = "P16" if target == "fin17a_17a1_d" else "P17"
    print(f"{tag} pre-2021 CV {target:16s} (2017->2021, stage-3 basin = "
          f"{THIRD_BASIN_COL[target]} terciles): two_stage={mae_two:.3f} "
          f"three_stage={mae_three:.3f}  -> three_stage={use_three}  (n={len(common)})")
    return use_three


def _select_fourth_stage(fx: Findex, target: str):
    """P18 pre-2021 CV: three-stage vs four-stage, both tercile basins built at 2017."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    b1, b2 = BASIN_ORDER[target]
    b3 = _tercile_basin(train, THIRD_BASIN_COL[target], 2017)
    b4 = _tercile_basin(train, FOURTH_BASIN_COL[target], 2017)
    s1 = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    s2 = _shrink(train, s1, SHRINK_K, b2, at_year=2017)
    s3 = _shrink(train, s2, SHRINK_K, b3, at_year=2017)
    s4 = _shrink(train, s3, SHRINK_K, b4, at_year=2017)
    mae_three = float((s3.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_four = float((s4.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_four = mae_four < mae_three
    print(f"P18 pre-2021 CV {target:16s} (2017->2021, stage-4 basin = "
          f"{FOURTH_BASIN_COL[target]} terciles): three_stage={mae_three:.3f} "
          f"four_stage={mae_four:.3f}  -> four_stage={use_four}  (n={len(common)})")
    return use_four


def _select_center(fx: Findex, target: str, use_two, use_three, use_four):
    """P22 pre-2021 CV: the target's ADOPTED stage stack, mean-centered vs median-centered,
    on the 2017->2021 transition with a persistence base and every basin built at 2017.
    Adopt the median center only if it beats the incumbent mean center on this <=2021 window."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    third = {t: _tercile_basin(train, c, 2017) for t, c in THIRD_BASIN_COL.items()}
    fourth = {t: _tercile_basin(train, c, 2017) for t, c in FOURTH_BASIN_COL.items()}
    maes = {}
    for center in ("mean", "median"):
        p = _stack(train, from_2017, target, 2017, center, use_two, use_three, use_four,
                   third, fourth)
        maes[center] = float((p.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_median = maes["median"] < maes["mean"]
    n_stages = 1 + int(bool(use_two.get(target))) + int(bool(use_three.get(target))) \
        + int(bool(use_four.get(target)))
    print(f"P22 pre-2021 CV {target:16s} (2017->2021, {n_stages}-stage stack): "
          f"mean_center={maes['mean']:.3f} median_center={maes['median']:.3f}  "
          f"-> median_center={use_median}  (n={len(common)})")
    return use_median


def predict(fx: Findex, use_two, use_three, use_four, use_median) -> dict:
    train, _ = fx.prediction_task()
    third_basin_2021 = {t: _tercile_basin(train, col, 2021)
                        for t, col in THIRD_BASIN_COL.items()}
    fourth_basin_2021 = {t: _tercile_basin(train, col, 2021)
                         for t, col in FOURTH_BASIN_COL.items()}
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)

        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            base = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
        else:
            base = last

        center = "median" if use_median.get(target) else "mean"
        preds[target] = _stack(train, base, target, 2021, center, use_two, use_three, use_four,
                               third_basin_2021, fourth_basin_2021)
    return preds


if __name__ == "__main__":
    fx = Findex()
    # Stage membership: unchanged from the P18 champion (resilience two-stage hard-coded off —
    # the proxied CV adopted it at P13 but the holdout worsened 6.625 -> 6.730).
    use_two = {"fin17a_17a1_d": True, "fin24aSD_ND": False,
               "account_t_d": _select_two_stage(fx, "account_t_d")}
    use_three = {"fin17a_17a1_d": _select_third_stage(fx, "fin17a_17a1_d"),
                 "account_t_d": _select_third_stage(fx, "account_t_d")}
    use_four = {"fin17a_17a1_d": _select_fourth_stage(fx, "fin17a_17a1_d")}

    # P22: the basin CENTER, re-selected per target on <=2021 data. Resilience excluded by design.
    use_median = {t: _select_center(fx, t, use_two, use_three, use_four)
                  for t in CENTER_CANDIDATES}
    print(f"P22 adopted median center: {use_median}  (resilience excluded by design, stays mean)")
    result = fx.evaluate_predictions(predict(fx, use_two, use_three, use_four, use_median))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
