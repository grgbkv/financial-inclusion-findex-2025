"""Prediction stream — P6: extend the P5 region-shrinkage (k=0.1) to account_t_d as well
as resilience.

Damped trend (lambda=0.5) for saved_formally (P2, structural break in 2024 that plain
persistence misses). For resilience (fin24aSD_ND) AND account_t_d, shrink each country's
2021 value partially toward its region's (regionwb24_hi) population-weighted 2021 mean.
Shrinkage intensity k is NOT fit on 2024 — it is the same value selected by cross-validating
the shrink mechanic on the fully-<=2021 account_t_d 2017->2021 transition (k=0.1 minimized
2017->2021 account MAE, 7.498->7.217; see RESEARCH_LOG.md P5). P6 applies that CV evidence to
its native target: account. P5 champion for resilience is unchanged (same k, same mechanic).
"""
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
SHRINK_TARGETS = {"fin24aSD_ND", "account_t_d"}


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
        elif target in SHRINK_TARGETS:
            preds[target] = _region_shrink(train, last, SHRINK_K)
        else:
            preds[target] = last
    return preds


if __name__ == "__main__":
    fx = Findex()
    result = fx.evaluate_predictions(predict(fx))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
