"""Prediction stream — P10: tune the saving (fin17a_17a1_d) damped-trend lambda via a pre-2021
cross-validation, instead of the fixed lambda=0.5 (P2). CV: predict 2021 saving = 2017 +
lambda*(2017-2014) on the fully-<=2021 saving history (all 117 panel countries have 2014/2017/2021),
grid lambda in {0.0, 0.25, 0.5, 0.75, 1.0}, pick the CV-min lambda, apply that fixed lambda to the
2024 prediction (2024 = 2021 + lambda*(2021-2017), clipped [0,100]). No 2024 information touches
the selection. Adopt only if CV picks a lambda AND out-of-sample saving MAE improves on 8.448 (P2).

Account (income-group shrink k=0.1, P7) and resilience (region shrink k=0.1, P5) are untouched:
per-target policy requires them byte-identical to the champion.
"""
import pandas as pd

from harness import Findex

SHRINK_K = 0.1
LAMBDA_GRID = [0.0, 0.25, 0.5, 0.75, 1.0]
# saving damped-trend lambda chosen by the pre-2021 CV below.
SAVING_LAMBDA = None  # set by _select_saving_lambda()


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


def _select_account_basin(fx: Findex):
    """Pre-2021 CV: predict 2021 account from 2017 + shrink; pick region vs income group (P7)."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values="account_t_d") * 100
    truth_2021 = wide.get(2021)
    from_2017 = wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)
    out = {}
    for basin in ["regionwb24_hi", "incomegroupwb24"]:
        pred = _shrink(train, from_2017, SHRINK_K, basin, at_year=2017)
        mae = float((pred.reindex(common) - truth_2021.reindex(common)).abs().mean())
        out[basin] = round(mae, 3)
    winner = min(out, key=out.get)
    print(f"P7 pre-2021 CV (account 2017->2021, k={SHRINK_K}): {out}  -> basin={winner}")
    return winner, out


def _select_saving_lambda(fx: Findex):
    """Pre-2021 CV: predict 2021 saving = 2017 + lambda*(2017-2014); pick CV-min lambda. No 2024."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(
        index="countrynewwb", columns="year", values="fin17a_17a1_d") * 100
    y14, y17, y21 = wide.get(2014), wide.get(2017), wide.get(2021)
    common = y14.dropna().index.intersection(y17.dropna().index).intersection(y21.dropna().index)
    out = {}
    for lam in LAMBDA_GRID:
        pred = (y17 + lam * (y17 - y14)).clip(0, 100)
        mae = float((pred.reindex(common) - y21.reindex(common)).abs().mean())
        out[lam] = round(mae, 3)
    winner = min(out, key=out.get)
    print(f"P10 pre-2021 CV (saving 2014/2017->2021): {out}  -> lambda={winner} (n={len(common)})")
    return winner, out


def predict(fx: Findex, account_basin: str, saving_lambda: float) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + saving_lambda * trend).clip(0, 100)
            preds[target] = pred.fillna(last)
        elif target == "fin24aSD_ND":
            preds[target] = _shrink(train, last, SHRINK_K, "regionwb24_hi")  # P5 champion, fixed
        elif target == "account_t_d":
            preds[target] = _shrink(train, last, SHRINK_K, account_basin)   # P7 champion, fixed
        else:
            preds[target] = last
    return preds


if __name__ == "__main__":
    fx = Findex()
    basin, _ = _select_account_basin(fx)
    lam, _ = _select_saving_lambda(fx)
    result = fx.evaluate_predictions(predict(fx, basin, lam))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
