"""Prediction stream — P1: damped-trend predictor.

2024 = 2021 + lambda * (2021 - 2017), lambda = 0.5, clipped to [0, 100].
Countries missing 2017 fall back to persistence.
"""
import pandas as pd

from harness import Findex

DAMP = 0.5


def predict(fx: Findex) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        prev = wide.get(2017)
        trend = (last - prev).fillna(0.0) if prev is not None else 0.0
        pred = (last + DAMP * trend).clip(0, 100)
        preds[target] = pred.fillna(last)
    return preds


if __name__ == "__main__":
    fx = Findex()
    result = fx.evaluate_predictions(predict(fx))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
