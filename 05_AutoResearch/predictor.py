"""Prediction stream — P21: did ACCOUNT stop at three stages, or stop at the wrong BASIN?

Champion (P18): saving = damped trend (l=0.5) + region -> income-group -> account-tercile ->
g20-tercile shrink (6.831), account = persistence + income-group -> region -> g20-tercile shrink
(5.014), resilience = persistence + region shrink (6.625).

P19 and P20 offer competing readings of the same shape. P19 (account's 4th stage rejected by
0.423pp) was written up as "the compounding curve is TARGET-SPECIFIC — saving takes four stages,
account stops at three". P20 (saving's 5th stage rejected by 0.274pp on a formal-borrowing basin)
proposed instead that the BASIN MATERIAL matters: every basin that ever paid is a digitalization
cut, and the first non-digitalization basin was actively harmful. The two readings are confounded
in the record, because P19's rejected account basin was terciles of formal SAVING — a depth
indicator, not a digitalization cut. So account may have stopped at three for P20's reason.

P21 stage-4 basin for account: terciles of `fin32_acc` (wage digitalization, 117/117 panel coverage
at 2017 and 2021, verified before registration) — a digitalization cut distinct from the target and
from stage 3's `g20_any`, and the rail E24 just certified as the strongest and most jackknife-stable
of the three.

Adoption rule (entirely <=2021, no 2024 anywhere in features, fitting or selection): CV on the
account 2017->2021 transition with a persistence base (the P10/P12/P13/P16/P17/P18/P19/P20
protocol), every basin — including both tercile basins — built from the 2017 cross-section; adopt
the fourth stage only if it beats the incumbent three-stage there. Per the P14/P15/P19/P20 protocol
a CV rejection means no 2024 evaluation and a revert to the P18 champion. Per-target policy (P2):
touches account only; saving (6.831) and resilience (6.625) stay byte-identical.
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

# Per-target stage-3 DATA-DRIVEN basin: terciles of another indicator's level.
# saving -> account level ("digitalization stage", P16, fixed).
# account -> g20_any level ("digital-usage stage", P17 candidate).
THIRD_BASIN_COL = {
    "fin17a_17a1_d": "account_t_d",
    "account_t_d": "g20_any",
}

# Per-target stage-4 DATA-DRIVEN basin: a SECOND cross-indicator basin, distinct from the target and
# from the stage-3 basin column. saving -> g20_any level (P18, kept). account -> fin32_acc level
# (P21 candidate: a DIGITALIZATION cut, where P19's rejected candidate was a depth indicator).
FOURTH_BASIN_COL = {
    "fin17a_17a1_d": "g20_any",
    "account_t_d": "fin32_acc",
}


def _tercile_basin(train, col, at_year):
    """Data-driven basin: terciles of `col`'s level at `at_year`. Built from <=2021 data only;
    cuts across region and income group."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")[col].dropna()
    if len(ref) < 9:
        return pd.Series(dtype=object)
    return pd.qcut(ref, 3, labels=["ter_low", "ter_mid", "ter_high"]).astype(object)


def _shrink(train, last, k, basin, at_year=2021):
    """Shrink `last` toward its basin's pop-weighted mean at `at_year`.
    `basin` is either a column name in the train frame or a ready country-indexed Series."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    basin_s = ref[basin] if isinstance(basin, str) else basin.reindex(ref.index)
    pop = ref["pop_adult"]
    d = pd.DataFrame({"last": last, "basin": basin_s, "pop": pop}).dropna(
        subset=["last", "basin"])
    grp_mean = d.groupby("basin").apply(
        lambda g: (g["last"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    d["grp_mean"] = d["basin"].map(grp_mean)
    shrunk = d["last"] - k * (d["last"] - d["grp_mean"])
    return shrunk.reindex(last.index).fillna(last)


def _select_two_stage(fx: Findex, target: str):
    """Pre-2021 CV: predict 2021 from 2017 (persistence base), compare that target's current
    single shrink vs the two-stage version. Adopt two-stage only if it wins on <=2021 data.

    Deviation from the P13 pre-registration, disclosed: fin24aSD_ND exists only in 2021, so it
    has no pre-2021 transition to CV on — the registered per-target rule is infeasible for it.
    Fallback follows the P5 precedent (which picked k=0.1 for resilience off the account
    transition): run the CV on account_t_d while keeping resilience's own basin ORDER
    (region -> income-group). Still no 2024 anywhere. P8 is on record that account-CV basin
    preferences need not transfer to resilience, so this selector is known-weak.
    """
    train, _ = fx.prediction_task()
    cv_target = "account_t_d" if target == "fin24aSD_ND" else target
    if cv_target != target:
        print(f"P13 note: {target} has no pre-2021 history; CV proxied on {cv_target} "
              f"with {target}'s basin order (P5 precedent, disclosed deviation)")
    wide = train.pivot_table(index="countrynewwb", columns="year", values=cv_target) * 100
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
    """P16/P17 pre-2021 CV: predict `target` 2021 from 2017 (persistence base, P12 protocol), all
    basins — including the data-driven tercile basin — built at 2017. Adopt the third stage only
    if it beats the incumbent two-stage on this <=2021 window."""
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
    """P18 pre-2021 CV: predict `target` 2021 from 2017 (persistence base, P12 protocol), all
    basins — including both data-driven tercile basins — built at 2017. Adopt the fourth stage
    only if it beats the incumbent three-stage on this <=2021 window."""
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


def predict(fx: Findex, use_two: dict, use_three: dict, use_four: dict) -> dict:
    train, _ = fx.prediction_task()
    third_basin_2021 = {t: _tercile_basin(train, col, 2021)
                        for t, col in THIRD_BASIN_COL.items()}
    fourth_basin_2021 = {t: _tercile_basin(train, col, 2021)
                         for t, col in FOURTH_BASIN_COL.items()}
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        b1, b2 = BASIN_ORDER[target]

        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
        else:
            pred = last

        pred = _shrink(train, pred, SHRINK_K, b1)          # stage 1 (champion basin)
        if use_two.get(target):                            # stage 2 (orthogonal basin)
            pred = _shrink(train, pred, SHRINK_K, b2)
        if use_three.get(target):                          # stage 3 (data-driven basin)
            pred = _shrink(train, pred, SHRINK_K, third_basin_2021[target])
        if use_four.get(target):                           # stage 4 (2nd data-driven basin)
            pred = _shrink(train, pred, SHRINK_K, fourth_basin_2021[target])
        preds[target] = pred
    return preds


if __name__ == "__main__":
    fx = Findex()
    # Resilience: the P13 run showed the proxied CV adopted two-stage (6.955 < 7.209) but
    # out-of-sample MAE worsened 6.625 -> 6.730, so it reverts to the P5 single region shrink
    # under the per-target policy — the same non-transfer P8 found. Kept hard-coded off rather
    # than re-running a selector already known to mis-select for this target.
    use_two = {"fin17a_17a1_d": True, "fin24aSD_ND": False,
               "account_t_d": _select_two_stage(fx, "account_t_d")}
    # Stage 3: saving is the P16 champion (fixed); account is the P17 candidate under test.
    use_three = {"fin17a_17a1_d": _select_third_stage(fx, "fin17a_17a1_d"),
                 "account_t_d": _select_third_stage(fx, "account_t_d")}
    # Stage 4: saving is the P18 champion (fixed); account is the P21 candidate under test.
    use_four = {"fin17a_17a1_d": _select_fourth_stage(fx, "fin17a_17a1_d"),
                "account_t_d": _select_fourth_stage(fx, "account_t_d")}
    print(f"P21 adopted two-stage: {use_two} | three-stage: {use_three} | "
          f"four-stage: {use_four}")
    result = fx.evaluate_predictions(predict(fx, use_two, use_three, use_four))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
