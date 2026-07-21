"""Prediction stream — P14: does the STAGE ORDER of saving's two-stage shrink matter? The P12/P13
champion fixes saving at region -> income-group (MAE 7.359), an arbitrary order. Because each
stage shrinks values already modified by the previous stage toward that stage's basin mean, the
two orders are not identical. Test the reverse order (income-group -> region) for saving.

Selection entirely pre-2021 (no 2024 anywhere): CV on the fully-<=2021 saving 2017->2021
transition (persistence base, per P10/P12) must prefer income-group -> region over the incumbent
region -> income-group before adoption; then apply that order unchanged to 2021->2024.

Per-target policy (P2's rule): touches saving only. Account (income-group -> region two-stage,
P13) and resilience (region single shrink, P5) stay byte-identical to the current champion.
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
    "fin17a_17a1_d": (REGION_BASIN, INCOME_BASIN),  # P12 incumbent order; P14 may flip it
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
    """Pre-2021 CV (predict 2021 from 2017, persistence base): current single shrink vs two-stage.
    Unchanged from P13; used for account (and, via proxy, resilience is hard-coded off in main)."""
    train, _ = fx.prediction_task()
    cv_target = "account_t_d" if target == "fin24aSD_ND" else target
    wide = train.pivot_table(index="countrynewwb", columns="year", values=cv_target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)
    b1, b2 = BASIN_ORDER[target]
    single = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    two_stage = _shrink(train, single, SHRINK_K, b2, at_year=2017)
    mae_single = float((single.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_two = float((two_stage.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_two = mae_two < mae_single
    print(f"P14 pre-2021 CV {target:16s} (2017->2021): single={mae_single:.3f} "
          f"two_stage={mae_two:.3f}  -> two_stage={use_two}  (n={len(common)})")
    return use_two


def _select_saving_order(fx: Findex):
    """P14 pre-2021 CV: for saving's two-stage shrink, compare the two stage orders on the
    <=2021 saving 2017->2021 transition (persistence base). Return the (b1, b2) order to use."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values="fin17a_17a1_d") * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    orders = {"region->income": (REGION_BASIN, INCOME_BASIN),
              "income->region": (INCOME_BASIN, REGION_BASIN)}
    maes = {}
    for name, (b1, b2) in orders.items():
        s1 = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
        s2 = _shrink(train, s1, SHRINK_K, b2, at_year=2017)
        maes[name] = float((s2.reindex(common) - truth_2021.reindex(common)).abs().mean())
    incumbent = "region->income"
    challenger = "income->region"
    chosen = challenger if maes[challenger] < maes[incumbent] else incumbent
    print(f"P14 pre-2021 CV saving stage-order (2017->2021): "
          f"region->income={maes[incumbent]:.3f} income->region={maes[challenger]:.3f} "
          f"-> chosen={chosen}  (n={len(common)})")
    return orders[chosen], chosen


def predict(fx: Findex, use_two: dict, saving_order) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        b1, b2 = saving_order if target == "fin17a_17a1_d" else BASIN_ORDER[target]

        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
        else:
            pred = last

        pred = _shrink(train, pred, SHRINK_K, b1)          # stage 1
        if use_two.get(target):                            # stage 2 (orthogonal basin)
            pred = _shrink(train, pred, SHRINK_K, b2)
        preds[target] = pred
    return preds


if __name__ == "__main__":
    fx = Findex()
    saving_order, chosen = _select_saving_order(fx)
    # Saving always uses both stages (P12); P14 only chooses the order via pre-2021 CV.
    # Account: two-stage selected on its own pre-2021 CV (P13). Resilience: single region shrink
    # (P5) — the P13 proxied CV mis-selects two-stage for it, so kept hard-coded off (P8/P13).
    use_two = {"fin17a_17a1_d": True, "fin24aSD_ND": False,
               "account_t_d": _select_two_stage(fx, "account_t_d")}
    print(f"P14 saving order adopted: {chosen}")
    result = fx.evaluate_predictions(predict(fx, use_two, saving_order))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
