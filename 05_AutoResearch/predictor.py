"""Prediction stream — P4 attempt: logit-space damped trend for account_t_d.

Champion policy (P2) otherwise: persistence for resilience (no pre-2021 wave to
trend from); damped trend (lambda=0.5) in pp-space for saved_formally, where 2024
has a structural break that persistence badly misses. P4 tries a logit-space damped
trend for account_t_d only, since P1's pp-linear trend overshot there (growth
mechanically decelerates near the 100% ceiling) -- logit space bakes in that
deceleration without using any 2024 information.
"""
import numpy as np
import pandas as pd

from harness import Findex

DAMP = 0.5
EPS = 1e-3


def _logit(p):
    p = p.clip(EPS, 100 - EPS) / 100
    return np.log(p / (1 - p))


def _inv_logit(z):
    return 100 / (1 + np.exp(-z))


def predict(fx: Findex) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100)
            preds[target] = pred.fillna(last)
        elif target == "account_t_d":
            prev = wide.get(2017)
            z_last = _logit(last)
            z_prev = _logit(prev) if prev is not None else z_last
            z_trend = (z_last - z_prev).fillna(0.0)
            z_pred = z_last + DAMP * z_trend
            pred = pd.Series(_inv_logit(z_pred.values), index=z_pred.index)
            preds[target] = pred.fillna(last)
        else:
            preds[target] = last
    return preds


if __name__ == "__main__":
    fx = Findex()
    result = fx.evaluate_predictions(predict(fx))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
