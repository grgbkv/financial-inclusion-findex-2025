"""Prediction stream — P11: add k=0.1 basin shrinkage ON TOP of the champion damped trend for
saving (fin17a_17a1_d), the only target without shrinkage. Basin selection entirely pre-2021:
CV on the fully-<=2021 saving 2017->2021 transition (predict 2021 saving from the 2017 level +
k=0.1 shrink toward the basin's 2017 pop-weighted mean; persistence base per P10's finding that
pre-2021 saving dynamics carry no usable trend), comparing {none, regionwb24_hi,
incomegroupwb24}. Adopt the CV winner only if not "none"; then shrink the 2021->2024
damped-trend prediction vector toward its basin pop-weighted mean.

Account keeps the P7 income-group shrink (k=0.1); resilience keeps the P5 region shrink
(k=0.1). Per-target policy: those two must stay byte-identical to the champion.
"""
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
ACCOUNT_BASIN = "incomegroupwb24"  # P7 champion, fixed


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


def _select_saving_basin(fx: Findex):
    """Pre-2021 CV: predict 2021 saving from 2017 + k=0.1 shrink (persistence base);
    compare none vs region vs income-group by MAE."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year",
                             values="fin17a_17a1_d") * 100
    truth_2021 = wide.get(2021)
    from_2017 = wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)
    out = {}
    for basin in ["none", "regionwb24_hi", "incomegroupwb24"]:
        pred = from_2017 if basin == "none" else _shrink(
            train, from_2017, SHRINK_K, basin, at_year=2017)
        mae = float((pred.reindex(common) - truth_2021.reindex(common)).abs().mean())
        out[basin] = round(mae, 3)
    winner = min(out, key=out.get)
    print(f"P11 pre-2021 CV (saving 2017->2021, k={SHRINK_K}): {out}  -> basin={winner}")
    return winner, out


def predict(fx: Findex, saving_basin: str) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
            if saving_basin != "none":  # P11: shrink the prediction vector
                pred = _shrink(train, pred, SHRINK_K, saving_basin)
            preds[target] = pred
        elif target == "fin24aSD_ND":
            preds[target] = _shrink(train, last, SHRINK_K, "regionwb24_hi")  # P5, fixed
        elif target == "account_t_d":
            preds[target] = _shrink(train, last, SHRINK_K, ACCOUNT_BASIN)  # P7, fixed
        else:
            preds[target] = last
    return preds


if __name__ == "__main__":
    fx = Findex()
    basin, cv = _select_saving_basin(fx)
    result = fx.evaluate_predictions(predict(fx, basin))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
