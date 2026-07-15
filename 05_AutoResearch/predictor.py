"""Prediction stream — P7: for account_t_d, test income-group shrinkage vs the incumbent
region shrinkage (P6). Selection is done entirely pre-2021: cross-validate both variants
(same k=0.1 mechanic) on the fully-<=2021 account_t_d 2017->2021 transition (predict 2021 from
2017 + shrink toward the group's 2017 pop-weighted mean), and adopt whichever basin the CV
prefers. No 2024 information touches the choice.

Saving (fin17a_17a1_d) keeps the P2 damped trend; resilience (fin24aSD_ND) keeps the P5
region-shrinkage (k=0.1). Per-target policy: those two must stay byte-identical to the champion.
"""
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
# account basin chosen by the pre-2021 CV below; resilience always region-shrinks (P5).
ACCOUNT_BASIN = None  # set by _select_account_basin()


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
    """Pre-2021 CV: predict 2021 account from 2017 + shrink; pick region vs income group by MAE."""
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


def predict(fx: Findex, account_basin: str) -> dict:
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
        elif target == "fin24aSD_ND":
            preds[target] = _shrink(train, last, SHRINK_K, "regionwb24_hi")  # P5 champion, fixed
        elif target == "account_t_d":
            preds[target] = _shrink(train, last, SHRINK_K, account_basin)
        else:
            preds[target] = last
    return preds


if __name__ == "__main__":
    fx = Findex()
    basin, cv = _select_account_basin(fx)
    result = fx.evaluate_predictions(predict(fx, basin))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
