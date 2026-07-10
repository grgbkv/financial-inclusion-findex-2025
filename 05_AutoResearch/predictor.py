"""Prediction stream — P3: mobile-money-informed saving predictor.

Persistence for account & resilience. For saved_formally: growth model fit on the
2017->2021 transition (weighted OLS: d_sav ~ 1 + mm_level + d_mm), applied to the
2021 state. Only <=2021 data used for both fitting and features.
"""
import numpy as np
import pandas as pd

from harness import Findex


def _wols(y, X, w):
    Xd = np.column_stack([np.ones(len(y))] + X)
    W = np.diag(w / w.sum())
    return np.linalg.solve(Xd.T @ W @ Xd, Xd.T @ W @ y)


def predict(fx: Findex) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    wide = lambda col: train.pivot_table(index="countrynewwb", columns="year", values=col) * 100
    pop = train[train["year"] == 2021].set_index("countrynewwb")["pop_adult"]

    for target in fx.PRED_TARGETS:
        tw = wide(target)
        last = tw.get(2021)
        if target != "fin17a_17a1_d":
            preds[target] = last
            continue
        mm = wide("mobileaccount_t_d")
        fit = pd.DataFrame({
            "d_sav": tw[2021] - tw[2017],
            "mm_lvl": mm[2017],
            "d_mm": mm[2021] - mm[2017],
            "w": pop,
        }).dropna()
        beta = _wols(fit["d_sav"].values,
                     [fit["mm_lvl"].values, fit["d_mm"].values], fit["w"].values)
        # apply to the 2021 state: assume mm keeps its 2017->2021 growth
        app = pd.DataFrame({"mm_lvl": mm[2021], "d_mm": mm[2021] - mm[2017]})
        growth = beta[0] + beta[1] * app["mm_lvl"] + beta[2] * app["d_mm"]
        pred = (last + growth.reindex(last.index).fillna(0)).clip(0, 100)
        preds[target] = pred.fillna(last)
    return preds


if __name__ == "__main__":
    fx = Findex()
    result = fx.evaluate_predictions(predict(fx))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
