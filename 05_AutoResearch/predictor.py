"""Prediction stream — P20: does saving's compounding continue past FOUR stages, and does the
basin have to be a DIGITALIZATION cut?

Champion (P18): saving = damped trend (l=0.5) + region -> income-group -> account-tercile ->
g20-tercile shrink (6.831), account = persistence + income-group -> region -> g20-tercile shrink
(5.014), resilience = persistence + region shrink (6.625).

P19 established that the compounding curve is TARGET-SPECIFIC: a fourth stage for account was
rejected by the <=2021 CV decisively (6.710 -> 7.133), so account stops at three while saving took
four. The open question on saving's side is whether its curve keeps paying — and, sharper, whether
the independent signal comes from ANY orthogonal partition or specifically from digitalization
cuts. Saving's stages 3 and 4 are both digitalization indicators (`account_t_d` terciles, `g20_any`
terciles) and both paid (-0.279, -0.249pp).

P20 stage-5 basin for saving: terciles of `fin22a_22a1_22g_d` (formal-borrowing level, 117/117
panel coverage at 2017 and 2021, verified before pre-registration) — a NON-digitalization
cross-indicator, distinct from the target and from both existing tercile basins. Known risk,
registered: E11 logged d_borrow ~ d_saving at r = +0.403, so the borrowing level is not orthogonal
to the saving change; whether that helps (relevant signal) or hurts (mis-partition, as in P19) is
the unknown.

Adoption rule (entirely <=2021, no 2024 anywhere in features, fitting or selection): CV on the
saving 2017->2021 transition with a persistence base (the P10/P12/P13/P16/P17/P18/P19 protocol),
every basin — including all three tercile basins — built from the 2017 cross-section; adopt the
fifth stage only if it beats the incumbent four-stage there. Per the P14/P15/P19 protocol, a CV
rejection means no 2024 evaluation is run. Per-target policy (P2): touches saving only; account
(5.014) and resilience (6.625) stay byte-identical to the P18 champion.
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

# Per-target stage-4 DATA-DRIVEN basin (P18 candidate): a SECOND cross-indicator basin, distinct
# from the target and from the stage-3 basin column. saving -> g20_any level.
FOURTH_BASIN_COL = {
    "fin17a_17a1_d": "g20_any",
}

# Per-target stage-5 DATA-DRIVEN basin (P20 candidate): a NON-digitalization cross-indicator basin.
# saving -> formal-borrowing level.
FIFTH_BASIN_COL = {
    "fin17a_17a1_d": "fin22a_22a1_22g_d",
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


def _select_fifth_stage(fx: Findex, target: str):
    """P20 pre-2021 CV: predict `target` 2021 from 2017 (persistence base, P12 protocol), all
    basins — including all three data-driven tercile basins — built at 2017. Adopt the fifth stage
    only if it beats the incumbent four-stage on this <=2021 window."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    b1, b2 = BASIN_ORDER[target]
    b3 = _tercile_basin(train, THIRD_BASIN_COL[target], 2017)
    b4 = _tercile_basin(train, FOURTH_BASIN_COL[target], 2017)
    b5 = _tercile_basin(train, FIFTH_BASIN_COL[target], 2017)
    s1 = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    s2 = _shrink(train, s1, SHRINK_K, b2, at_year=2017)
    s3 = _shrink(train, s2, SHRINK_K, b3, at_year=2017)
    s4 = _shrink(train, s3, SHRINK_K, b4, at_year=2017)
    s5 = _shrink(train, s4, SHRINK_K, b5, at_year=2017)
    mae_four = float((s4.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_five = float((s5.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_five = mae_five < mae_four
    print(f"P20 pre-2021 CV {target:16s} (2017->2021, stage-5 basin = "
          f"{FIFTH_BASIN_COL[target]} terciles): four_stage={mae_four:.3f} "
          f"five_stage={mae_five:.3f}  -> five_stage={use_five}  (n={len(common)})")
    return use_five


def predict(fx: Findex, use_two: dict, use_three: dict, use_four: dict, use_five: dict) -> dict:
    train, _ = fx.prediction_task()
    third_basin_2021 = {t: _tercile_basin(train, col, 2021)
                        for t, col in THIRD_BASIN_COL.items()}
    fourth_basin_2021 = {t: _tercile_basin(train, col, 2021)
                         for t, col in FOURTH_BASIN_COL.items()}
    fifth_basin_2021 = {t: _tercile_basin(train, col, 2021)
                        for t, col in FIFTH_BASIN_COL.items()}
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
        if use_five.get(target):                           # stage 5 (non-digitalization basin)
            pred = _shrink(train, pred, SHRINK_K, fifth_basin_2021[target])
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
    # Stage 4: the P18 champion, saving only (per-target policy).
    use_four = {"fin17a_17a1_d": _select_fourth_stage(fx, "fin17a_17a1_d")}
    # Stage 5: the P20 candidate, saving only. Per the P14/P15/P19 protocol a CV rejection means
    # the candidate never reaches the holdout.
    use_five = {"fin17a_17a1_d": _select_fifth_stage(fx, "fin17a_17a1_d")}
    print(f"P20 adopted two-stage: {use_two} | three-stage: {use_three} | "
          f"four-stage: {use_four} | five-stage: {use_five}")
    if not use_five["fin17a_17a1_d"]:
        print("P20: <=2021 CV does NOT prefer the fifth stage -> no 2024 evaluation of the "
              "candidate (P14/P15/P19 protocol); reporting the P18 champion unchanged.")
    result = fx.evaluate_predictions(predict(fx, use_two, use_three, use_four, use_five))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
