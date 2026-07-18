"""Prediction stream — P12: test a SECOND, orthogonal light shrink for saving. The P11 champion
is damped trend (lambda=0.5) + k=0.1 region-basin shrink. P12 adds a nested income-group-basin
shrink (k2=0.1) on top, motivated by P7's finding that region and income-group basins capture
partly-orthogonal cross-sectional structure. Selection is entirely pre-2021: CV on the
fully-<=2021 saving 2017->2021 transition (persistence base per P10) must prefer the two-stage
(region -> income-group) shrink over the single region shrink before adoption.

Account keeps the P7 income-group shrink (k=0.1); resilience keeps the P5 region shrink
(k=0.1). Per-target policy: those two stay byte-identical to the champion. This is the
transfer-tested shrinkage mechanism (noise correction) applied a second time, not a dynamics
knob (the P9/P10 lesson).
"""
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
ACCOUNT_BASIN = "incomegroupwb24"  # P7 champion, fixed
SAVING_BASIN1 = "regionwb24_hi"    # P11 champion first-stage basin, fixed


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


def _select_two_stage(fx: Findex):
    """Pre-2021 CV: predict 2021 saving from 2017 (persistence base), compare single region
    shrink vs two-stage (region -> income-group) shrink by MAE. Adopt two-stage only if it
    wins on the <=2021 window."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year",
                             values="fin17a_17a1_d") * 100
    truth_2021 = wide.get(2021)
    from_2017 = wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    single = _shrink(train, from_2017, SHRINK_K, SAVING_BASIN1, at_year=2017)
    two_stage = _shrink(train, single, SHRINK_K, ACCOUNT_BASIN, at_year=2017)
    mae_single = float((single.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_two = float((two_stage.reindex(common) - truth_2021.reindex(common)).abs().mean())
    out = {"single_region": round(mae_single, 3), "two_stage": round(mae_two, 3)}
    use_two = mae_two < mae_single
    print(f"P12 pre-2021 CV (saving 2017->2021): {out}  -> two_stage={use_two}")
    return use_two, out


def predict(fx: Findex, use_two_stage: bool) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
            pred = _shrink(train, pred, SHRINK_K, SAVING_BASIN1)     # P11 region shrink
            if use_two_stage:                                        # P12 second stage
                pred = _shrink(train, pred, SHRINK_K, ACCOUNT_BASIN)
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
    use_two, cv = _select_two_stage(fx)
    result = fx.evaluate_predictions(predict(fx, use_two))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
