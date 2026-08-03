"""Prediction stream — P25: shrinkage-NEUTRAL empirical-Bayes grading (the variant P24 registered).

P24 tested k_g = neff_g/(neff_g+m) and was CV-rejected on both targets, but its own diagnostic showed
the test was confounded: basin neff runs 1.6-9.5, so at every registered grid point (m >= 50) the
adaptive weight sat an ORDER OF MAGNITUDE below the incumbent 0.1, and the CV was mostly re-rejecting
P9's "less shrinkage is worse" rather than judging the reliability GRADING. Parent: P24.

CANDIDATE — the same shape, renormalized so the LEVEL is held fixed. At every stage:
    k_raw_g = neff_g / (neff_g + m)
    k_g     = 0.1 * k_raw_g / mean_w(k_raw)      clipped to [0, 0.5]
where mean_w is the population-weighted mean of k_raw over the countries being shrunk, so the
population-weighted average shrinkage equals the incumbent constant 0.1 BY CONSTRUCTION and only the
RELATIVE grading across basins varies. The grid now spans grading STRENGTH, not level: as m -> 0 all
k_raw -> 1 and the scheme collapses exactly onto the incumbent constant; as m -> infinity,
k_g is proportional to neff_g (full proportional grading).

ADOPTION RULE (entirely <=2021 — no 2024 in features, fitting or selection). Per target, CV on that
target's 2017->2021 transition with a persistence base and all basins built at 2017 (the
P10/P12/P13/P16-P24 protocol), grid m in {1, 3, 10, 30, 100, 1000}, comparing the best graded stack
against the identical incumbent constant-k stack: account = 3-stage (income -> region -> g20
terciles), saving = 4-stage (region -> income -> account terciles -> g20 terciles). RESILIENCE IS
EXCLUDED BY DESIGN (no pre-2021 transition; the account proxy is twice on record as mis-selecting for
it — P8, P13) and stays byte-identical at 6.625.

KEEP if for any target the <=2021 CV prefers the graded weight AND its 2021->2024 MAE improves on the
champion (account 5.014, saving 6.831), with every untouched target byte-identical. Five CV->holdout
interactions are on record (P8, P9, P13, P23, P24); the CV margin and the holdout delta are both
recorded whatever the verdict. The per-basin k_g table is printed so the grading can be inspected
directly — if this variant also fails, the axis is closed and that is the result.
"""
import numpy as np
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
INCOME_BASIN = "incomegroupwb24"   # P7 champion basin for account
REGION_BASIN = "regionwb24_hi"     # P5/P11 champion basin for resilience & saving stage 1

M_GRID = [1, 3, 10, 30, 100, 1000]  # P25 registered grid: grading STRENGTH (m->0 == incumbent)
K_CLIP = 0.5

BASIN_ORDER = {
    "account_t_d": (INCOME_BASIN, REGION_BASIN),
    "fin24aSD_ND": (REGION_BASIN, INCOME_BASIN),
    "fin17a_17a1_d": (REGION_BASIN, INCOME_BASIN),  # P12, fixed
}

THIRD_BASIN_COL = {
    "fin17a_17a1_d": "account_t_d",
    "account_t_d": "g20_any",
}

FOURTH_BASIN_COL = {
    "fin17a_17a1_d": "g20_any",
}


def _tercile_basin(train, col, at_year):
    """Data-driven basin: terciles of `col`'s level at `at_year`. Built from <=2021 data only."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")[col].dropna()
    if len(ref) < 9:
        return pd.Series(dtype=object)
    return pd.qcut(ref, 3, labels=["ter_low", "ter_mid", "ter_high"]).astype(object)


def _kish(w):
    w = np.asarray(w, dtype=float)
    s = w.sum()
    return float(s * s / (w * w).sum()) if s > 0 else 0.0


def _shrink(train, last, k, basin, at_year=2021, m=None, report=None):
    """Shrink `last` toward its basin's pop-weighted mean at `at_year`.

    k is the incumbent CONSTANT when m is None. When m is given (P25), the per-country weight is
    k_g = k * k_raw_g / mean_w(k_raw) with k_raw_g = neff_g/(neff_g+m) — reliability GRADING at a
    population-weighted average shrinkage of exactly k.
    """
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    basin_s = ref[basin] if isinstance(basin, str) else basin.reindex(ref.index)
    pop = ref["pop_adult"]
    d = pd.DataFrame({"last": last, "basin": basin_s, "pop": pop}).dropna(
        subset=["last", "basin"])
    grp_mean = d.groupby("basin").apply(
        lambda g: (g["last"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    d["grp_mean"] = d["basin"].map(grp_mean)

    if m is None:
        k_vec = pd.Series(k, index=d.index)
    else:
        neff = d.groupby("basin")["pop"].apply(_kish)
        k_raw = (neff / (neff + m)).rename("k_raw")
        d["k_raw"] = d["basin"].map(k_raw)
        norm = float(np.average(d["k_raw"], weights=d["pop"]))
        k_vec = (k * d["k_raw"] / norm).clip(0, K_CLIP)
        if report is not None:
            report.append(pd.DataFrame({
                "n": d.groupby("basin").size(), "neff": neff.round(2),
                "k_g": (k * k_raw / norm).clip(0, K_CLIP).round(4)}))

    shrunk = d["last"] - k_vec * (d["last"] - d["grp_mean"])
    return shrunk.reindex(last.index).fillna(last)


def _stack(train, base, target, at_year, use_two, use_three, use_four, m=None, report=None):
    """The target's full incumbent shrink stack, with m=None reproducing the constant-k champion."""
    b1, b2 = BASIN_ORDER[target]
    pred = _shrink(train, base, SHRINK_K, b1, at_year, m, report)
    if use_two:
        pred = _shrink(train, pred, SHRINK_K, b2, at_year, m, report)
    if use_three:
        b3 = _tercile_basin(train, THIRD_BASIN_COL[target], at_year)
        pred = _shrink(train, pred, SHRINK_K, b3, at_year, m, report)
    if use_four:
        b4 = _tercile_basin(train, FOURTH_BASIN_COL[target], at_year)
        pred = _shrink(train, pred, SHRINK_K, b4, at_year, m, report)
    return pred


def _select_graded(fx: Findex, target, use_two, use_three, use_four):
    """P25 <=2021 CV: 2017->2021, persistence base, all basins at 2017. Compare the incumbent
    constant-k stack against the shrinkage-neutral graded stack over the registered m grid."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    def mae(pred):
        return float((pred.reindex(common) - truth_2021.reindex(common)).abs().mean())

    base_mae = mae(_stack(train, from_2017, target, 2017, use_two, use_three, use_four))
    scores = {}
    for m in M_GRID:
        scores[m] = mae(_stack(train, from_2017, target, 2017, use_two, use_three, use_four, m=m))
    best_m = min(scores, key=scores.get)
    adopt = scores[best_m] < base_mae
    grid = "  ".join(f"m={m}: {v:.3f}" for m, v in scores.items())
    print(f"P25 <=2021 CV {target:16s} (2017->2021)  constant_k={base_mae:.3f}   {grid}")
    print(f"                 best m={best_m} ({scores[best_m]:.3f}), margin vs constant = "
          f"{scores[best_m] - base_mae:+.3f}  ->  adopt_graded={adopt}  (n={len(common)})")
    return adopt, best_m, base_mae, scores[best_m]


def _select_two_stage(fx: Findex, target: str):
    train, _ = fx.prediction_task()
    cv_target = "account_t_d" if target == "fin24aSD_ND" else target
    wide = train.pivot_table(index="countrynewwb", columns="year", values=cv_target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)
    b1, b2 = BASIN_ORDER[target]
    single = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    two_stage = _shrink(train, single, SHRINK_K, b2, at_year=2017)
    mae_single = float((single.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_two = float((two_stage.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_two = mae_two < mae_single
    print(f"P13 pre-2021 CV {target:16s} (2017->2021): single={mae_single:.3f} "
          f"two_stage={mae_two:.3f}  -> two_stage={use_two}  (n={len(common)})")
    return use_two


def _select_third_stage(fx: Findex, target: str):
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)
    b1, b2 = BASIN_ORDER[target]
    b3 = _tercile_basin(train, THIRD_BASIN_COL[target], 2017)
    s1 = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    s2 = _shrink(train, s1, SHRINK_K, b2, at_year=2017)
    s3 = _shrink(train, s2, SHRINK_K, b3, at_year=2017)
    mae_two = float((s2.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_three = float((s3.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_three = mae_three < mae_two
    tag = "P16" if target == "fin17a_17a1_d" else "P17"
    print(f"{tag} pre-2021 CV {target:16s} (2017->2021, stage-3 basin = "
          f"{THIRD_BASIN_COL[target]} terciles): two_stage={mae_two:.3f} "
          f"three_stage={mae_three:.3f}  -> three_stage={use_three}  (n={len(common)})")
    return use_three


def _select_fourth_stage(fx: Findex, target: str):
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)
    b1, b2 = BASIN_ORDER[target]
    b3 = _tercile_basin(train, THIRD_BASIN_COL[target], 2017)
    b4 = _tercile_basin(train, FOURTH_BASIN_COL[target], 2017)
    s1 = _shrink(train, from_2017, SHRINK_K, b1, at_year=2017)
    s2 = _shrink(train, s1, SHRINK_K, b2, at_year=2017)
    s3 = _shrink(train, s2, SHRINK_K, b3, at_year=2017)
    s4 = _shrink(train, s3, SHRINK_K, b4, at_year=2017)
    mae_three = float((s3.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_four = float((s4.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_four = mae_four < mae_three
    print(f"P18 pre-2021 CV {target:16s} (2017->2021, stage-4 basin = "
          f"{FOURTH_BASIN_COL[target]} terciles): three_stage={mae_three:.3f} "
          f"four_stage={mae_four:.3f}  -> four_stage={use_four}  (n={len(common)})")
    return use_four


def predict(fx: Findex, use_two, use_three, use_four, graded) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
        else:
            pred = last
        preds[target] = _stack(train, pred, target, 2021,
                               use_two.get(target, False), use_three.get(target, False),
                               use_four.get(target, False), m=graded.get(target))
    return preds


if __name__ == "__main__":
    fx = Findex()
    use_two = {"fin17a_17a1_d": True, "fin24aSD_ND": False,
               "account_t_d": _select_two_stage(fx, "account_t_d")}
    use_three = {"fin17a_17a1_d": _select_third_stage(fx, "fin17a_17a1_d"),
                 "account_t_d": _select_third_stage(fx, "account_t_d")}
    use_four = {"fin17a_17a1_d": _select_fourth_stage(fx, "fin17a_17a1_d")}

    print("\n--- P25 shrinkage-neutral grading selector (resilience excluded by design) ---")
    graded, cv_report = {}, {}
    for t in ["account_t_d", "fin17a_17a1_d"]:
        adopt, best_m, base_mae, best_mae = _select_graded(
            fx, t, use_two.get(t, False), use_three.get(t, False), use_four.get(t, False))
        cv_report[t] = (adopt, best_m, base_mae, best_mae)
        if adopt:
            graded[t] = best_m

    print("\n--- per-basin grading table at the best m (account stack, stage 1) ---")
    train, _ = fx.prediction_task()
    rep = []
    m_show = cv_report["account_t_d"][1]
    _shrink(train, train[train["year"] == 2021].set_index("countrynewwb")["account_t_d"] * 100,
            SHRINK_K, INCOME_BASIN, 2021, m=m_show, report=rep)
    _shrink(train, train[train["year"] == 2021].set_index("countrynewwb")["account_t_d"] * 100,
            SHRINK_K, REGION_BASIN, 2021, m=m_show, report=rep)
    for t in rep:
        print(t.to_string())
    print(f"(m={m_show}; incumbent constant k = {SHRINK_K}; pop-weighted mean of k_g is 0.1 "
          f"by construction)")

    print(f"\nP25 adopted graded weight: {graded or 'none'}")
    result = fx.evaluate_predictions(predict(fx, use_two, use_three, use_four, graded))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
