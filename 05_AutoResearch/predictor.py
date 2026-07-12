"""Prediction stream — P5: region-shrinkage for resilience (current champion for that
target; P2's per-target policy otherwise unchanged).

Persistence for account (P4's logit-space damped trend lost to persistence by 0.02pp);
damped trend (lambda=0.5) for saved_formally (P2, structural break in 2024 that plain
persistence misses); for resilience (fin24aSD_ND), shrink each country's 2021 value
partially toward its region's (regionwb24_hi) population-weighted mean. Shrinkage
intensity k is NOT fit on 2024 — it is selected by cross-validating the same shrink
mechanic on the fully-<=2021 account_t_d 2017->2021 transition (predict 2021 from 2017 +
region-shrink, minimize MAE there), then applied unchanged to resilience. See
RESEARCH_LOG.md P5 for the selection run (k=0.1 minimized 2017->2021 account MAE).
"""
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
SHRINK_TARGET = "fin24aSD_ND"


def _region_shrink(train, last, k):
    region = train[train["year"] == 2021].set_index("countrynewwb")["regionwb24_hi"]
    pop = train[train["year"] == 2021].set_index("countrynewwb")["pop_adult"]
    d = pd.DataFrame({"last": last, "region": region, "pop": pop}).dropna(
        subset=["last", "region"])
    region_mean = d.groupby("region").apply(
        lambda g: (g["last"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    d["region_mean"] = d["region"].map(region_mean)
    shrunk = d["last"] - k * (d["last"] - d["region_mean"])
    return shrunk.reindex(last.index).fillna(last)


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
        elif target == SHRINK_TARGET:
            preds[target] = _region_shrink(train, last, SHRINK_K)
        else:
            preds[target] = last
    return preds


if __name__ == "__main__":
    fx = Findex()
    result = fx.evaluate_predictions(predict(fx))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
