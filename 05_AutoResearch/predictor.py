"""Prediction stream — the file the loop edits. Baseline version.

Task (fixed in harness): from panel history <= 2021, predict 2024 per-country values
(pp) for account ownership, resilience, formal saving.

Baseline: persistence — 2024 = 2021 value. The null model every idea must beat.
"""
import pandas as pd

from harness import Findex


def predict(fx: Findex) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        last = train[train["year"] == 2021].set_index("countrynewwb")[target] * 100
        preds[target] = last
    return preds


if __name__ == "__main__":
    fx = Findex()
    result = fx.evaluate_predictions(predict(fx))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
