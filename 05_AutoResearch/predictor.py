"""Prediction stream — P13: does P12's two-stage (orthogonal-basin) shrink generalize to the
other two targets? The champion is saving = damped trend + region -> income-group shrink
(7.359), account = single income-group shrink (P7, 5.144), resilience = single region shrink
(P5, 6.625). If orthogonal basins compound as a general noise-correction mechanism rather than
a saving-specific accident, adding the OTHER basin as a second stage should help both:
account income-group -> region, resilience region -> income-group, k=0.1 each.

Counter-evidence on record: P8 showed the income-group basin does not transfer to resilience
when used ALONE; this tests it as a second stage on top of region, a different claim.

Adoption rule (entirely pre-2021, no 2024 anywhere): per target independently, CV on the
fully-<=2021 2017->2021 transition (persistence base, per P10/P12) must prefer the two-stage
shrink over that target's current single shrink. Saving stays byte-identical to P12 either way.
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


def _shrink(train, last, k, basin_col, at_year=2021):
    """Shrink `last` toward its group's (basin_col) pop-weighted mean at `at_year`."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    basin = ref[basin_col]
    pop = ref["pop_adult"]
    d = pd.DataFrame({"last": last, "basin": basin, "pop": pop}).dropna(
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


def predict(fx: Findex, use_two: dict) -> dict:
    train, _ = fx.prediction_task()
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
        preds[target] = pred
    return preds


if __name__ == "__main__":
    fx = Findex()
    # Saving is the P12 champion configuration and is not re-selected here.
    use_two = {t: (True if t == "fin17a_17a1_d" else _select_two_stage(fx, t))
               for t in fx.PRED_TARGETS if t in BASIN_ORDER}
    print(f"P13 adopted two-stage: { {k: v for k, v in use_two.items()} }")
    result = fx.evaluate_predictions(predict(fx, use_two))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
