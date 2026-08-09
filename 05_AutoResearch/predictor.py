"""Prediction stream — P28: a BASIN-LEVEL DRIFT term, the first change to the base predictor
since P2.

Parent: P27 (the error diagnostic). ADMISSIBILITY, addressed up front because P27's decision rule
demands it: the next mechanism had to be estimable from <=2021 data ALONE and must not be fitted to
P27's residuals. A basin drift satisfies both — it is the standard alternative to the country-level
damped trend P10 tested, it was named as an open direction in the 2026-08-05 agenda addendum
("the trend term, untouched since P2 and never basin-varying") BEFORE P27 ran, and every quantity it
uses is a pre-2021 change.

MECHANISM. Every predictor since P5 is a CROSS-SECTIONAL operator: shrink a level toward a basin
mean. Nothing in the stack carries GROUP-LEVEL MOMENTUM. P28 adds, to the base prediction and before
any shrinkage stage,

    pred_i <- base_i + gamma * drift_{g(i)},
    drift_g = pop-weighted mean of (level_2021 - level_2017) over the countries of basin g

with g = the target's stage-1 basin (income group for account, region for saving), and gamma chosen
by <=2021 CV: predict 2021 from 2017 with the persistence base and the drift built from the
2014->2017 change, over the grid gamma in {0, 0.25, 0.50, 0.75, 1.00}. gamma = 0 nests the incumbent
EXACTLY, so the CV comparison is nested by construction.

ADOPTION RULE, with the P26 screening rule attached. Adopt only if BOTH:
  (i)  the CV strictly prefers some gamma > 0 by a margin >= 0.05pp over gamma = 0, and
  (ii) the CV curve over the grid is SINGLE-PEAKED with an INTERIOR minimum (monotone on each side).
A thin margin, or a win at a secondary local minimum, does NOT trigger a holdout evaluation — that
is the rule P26 wrote after five CV->holdout non-transfers. If the rule blocks adoption on both
targets, the stream CLOSES on the benchmark ladder, which is what P27's write-up and the agenda both
recommend as the default.

SCOPE. account_t_d and fin17a_17a1_d only. fin24aSD_ND exists in 2021 alone, so no drift is
computable for it at any date; per the P2 per-target policy it stays at the P5 champion (6.625),
byte-identical.

Incumbent champion (P18): account 5.014 / resilience 6.625 / saving 6.831.

--- P18 stack, unchanged below this line ---
Champion (P17): saving = damped trend (l=0.5) + region -> income-group -> account-tercile shrink
(7.080), account = persistence + income-group -> region -> g20-tercile shrink (5.014), resilience =
persistence + region shrink (6.625). P18 adds a fourth, cross-indicator basin to saving.
"""
import numpy as np
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
INCOME_BASIN = "incomegroupwb24"   # P7 champion basin for account
REGION_BASIN = "regionwb24_hi"     # P5/P11 champion basin for resilience & saving stage 1

# Per-target basin order: (stage-1 basin, candidate stage-2 basin)
BASIN_ORDER = {
    "account_t_d": (INCOME_BASIN, REGION_BASIN),
    "fin24aSD_ND": (REGION_BASIN, INCOME_BASIN),
    "fin17a_17a1_d": (REGION_BASIN, INCOME_BASIN),  # P12, fixed
}

# Per-target stage-3 DATA-DRIVEN basin: terciles of another indicator's level.
# saving -> account level ("digitalization stage", P16, fixed).
# account -> g20_any level ("digital-usage stage", P17 candidate).
THIRD_BASIN_COL = {
    "fin17a_17a1_d": "account_t_d",
    "account_t_d": "g20_any",
}

# Per-target stage-4 DATA-DRIVEN basin (P18 candidate): a SECOND cross-indicator basin, distinct
# from the target and from the stage-3 basin column. saving -> g20_any level.
FOURTH_BASIN_COL = {
    "fin17a_17a1_d": "g20_any",
}


def _tercile_basin(train, col, at_year):
    """Data-driven basin: terciles of `col`'s level at `at_year`. Built from <=2021 data only;
    cuts across region and income group."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")[col].dropna()
    if len(ref) < 9:
        return pd.Series(dtype=object)
    return pd.qcut(ref, 3, labels=["ter_low", "ter_mid", "ter_high"]).astype(object)


def _shrink(train, last, k, basin, at_year=2021):
    """Shrink `last` toward its basin's pop-weighted mean at `at_year`.
    `basin` is either a column name in the train frame or a ready country-indexed Series."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    basin_s = ref[basin] if isinstance(basin, str) else basin.reindex(ref.index)
    pop = ref["pop_adult"]
    d = pd.DataFrame({"last": last, "basin": basin_s, "pop": pop}).dropna(
        subset=["last", "basin"])
    grp_mean = d.groupby("basin").apply(
        lambda g: (g["last"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    d["grp_mean"] = d["basin"].map(grp_mean)
    shrunk = d["last"] - k * (d["last"] - d["grp_mean"])
    return shrunk.reindex(last.index).fillna(last)


def _select_two_stage(fx: Findex, target: str):
    """Pre-2021 CV: predict 2021 from 2017 (persistence base), compare that target's current
    single shrink vs the two-stage version. Adopt two-stage only if it wins on <=2021 data.

    Deviation from the P13 pre-registration, disclosed: fin24aSD_ND exists only in 2021, so it
    has no pre-2021 transition to CV on — the registered per-target rule is infeasible for it.
    Fallback follows the P5 precedent (which picked k=0.1 for resilience off the account
    transition): run the CV on account_t_d while keeping resilience's own basin ORDER
    (region -> income-group). Still no 2024 anywhere. P8 is on record that account-CV basin
    preferences need not transfer to resilience, so this selector is known-weak.
    """
    train, _ = fx.prediction_task()
    cv_target = "account_t_d" if target == "fin24aSD_ND" else target
    if cv_target != target:
        print(f"P13 note: {target} has no pre-2021 history; CV proxied on {cv_target} "
              f"with {target}'s basin order (P5 precedent, disclosed deviation)")
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
    """P16/P17 pre-2021 CV: predict `target` 2021 from 2017 (persistence base, P12 protocol), all
    basins — including the data-driven tercile basin — built at 2017. Adopt the third stage only
    if it beats the incumbent two-stage on this <=2021 window."""
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
    """P18 pre-2021 CV: predict `target` 2021 from 2017 (persistence base, P12 protocol), all
    basins — including both data-driven tercile basins — built at 2017. Adopt the fourth stage
    only if it beats the incumbent three-stage on this <=2021 window."""
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


# ---------------------------------------------------------------- P28: basin drift
DRIFT_GRID = [0.0, 0.25, 0.50, 0.75, 1.00]
DRIFT_MARGIN = 0.05          # minimum <=2021 CV improvement over gamma = 0 to consider adoption


def _basin_drift(train, target, basin, y0, y1, at_year):
    """Country-indexed pop-weighted mean change in `target` over y0->y1 within each basin.

    Basin membership and population weights are read at `at_year`; both endpoints are <=2021 by
    construction of every caller. Returned in pp, aligned to the basin frame's index."""
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    if y0 not in wide.columns or y1 not in wide.columns:
        return pd.Series(dtype=float)
    chg = (wide[y1] - wide[y0]).dropna()
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    d = pd.DataFrame({"chg": chg, "basin": ref[basin], "pop": ref["pop_adult"]}).dropna(
        subset=["chg", "basin", "pop"])
    grp = d.groupby("basin").apply(
        lambda g: (g["chg"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    return ref[basin].map(grp)


def _select_drift(fx: Findex, target: str):
    """P28 pre-2021 CV: predict `target` 2021 from 2017 (persistence base, the P12/P16/P17
    protocol), adding gamma * (2014->2017 basin drift) before the shrinkage stack. Returns the
    adopted gamma (0.0 = incumbent) and prints the whole CV curve, because the registered rule is
    about the SHAPE of the curve and not only its argmin."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    b1, b2 = BASIN_ORDER[target]
    drift = _basin_drift(train, target, b1, 2014, 2017, at_year=2017).reindex(
        from_2017.index).fillna(0.0)
    b3 = _tercile_basin(train, THIRD_BASIN_COL[target], 2017) if target in THIRD_BASIN_COL else None
    b4 = _tercile_basin(train, FOURTH_BASIN_COL[target], 2017) if target in FOURTH_BASIN_COL else None

    curve = []
    for gamma in DRIFT_GRID:
        p = from_2017 + gamma * drift
        p = _shrink(train, p, SHRINK_K, b1, at_year=2017)
        p = _shrink(train, p, SHRINK_K, b2, at_year=2017)
        if b3 is not None:
            p = _shrink(train, p, SHRINK_K, b3, at_year=2017)
        if b4 is not None:
            p = _shrink(train, p, SHRINK_K, b4, at_year=2017)
        curve.append(float((p.reindex(common) - truth_2021.reindex(common)).abs().mean()))

    base = curve[0]
    j = int(np.argmin(curve))
    margin = base - curve[j]
    # unimodal = non-increasing to the argmin then non-decreasing; the registered rule additionally
    # requires the minimum to be INTERIOR (not at a grid boundary).
    unimodal = (all(curve[i] >= curve[i + 1] for i in range(j))
                and all(curve[i] <= curve[i + 1] for i in range(j, len(curve) - 1)))
    interior = 0 < j < len(curve) - 1
    adopt = bool(margin >= DRIFT_MARGIN and unimodal and interior)

    print(f"P28 <=2021 CV {target:16s} (2017->2021, drift = 2014->2017 {b1} means):")
    print("      gamma  " + "  ".join(f"{g:5.2f}" for g in DRIFT_GRID))
    print("      MAE    " + "  ".join(f"{c:5.3f}" for c in curve) + f"   (n={len(common)})")
    print(f"      argmin gamma={DRIFT_GRID[j]:.2f} margin vs gamma=0 = {margin:+.3f}pp "
          f"(bar {DRIFT_MARGIN:.2f}) | unimodal={unimodal} interior_min={interior} -> "
          f"ADOPT={adopt}")
    if margin >= DRIFT_MARGIN and unimodal and not interior:
        print("      NOTE: minimum sits at a grid boundary — the registered rule requires an "
              "interior minimum, so this does NOT trigger a holdout evaluation.")
    return DRIFT_GRID[j] if adopt else 0.0


def predict(fx: Findex, use_two: dict, use_three: dict, use_four: dict,
            gammas: dict) -> dict:
    train, _ = fx.prediction_task()
    third_basin_2021 = {t: _tercile_basin(train, col, 2021)
                        for t, col in THIRD_BASIN_COL.items()}
    fourth_basin_2021 = {t: _tercile_basin(train, col, 2021)
                         for t, col in FOURTH_BASIN_COL.items()}
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        b1, b2 = BASIN_ORDER[target]

        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
        else:
            pred = last

        gamma = gammas.get(target, 0.0)
        if gamma:                                          # P28 basin drift, before any shrinkage
            drift = _basin_drift(train, target, b1, 2017, 2021, at_year=2021).reindex(
                pred.index).fillna(0.0)
            pred = (pred + gamma * drift).clip(0, 100)

        pred = _shrink(train, pred, SHRINK_K, b1)          # stage 1 (champion basin)
        if use_two.get(target):                            # stage 2 (orthogonal basin)
            pred = _shrink(train, pred, SHRINK_K, b2)
        if use_three.get(target):                          # stage 3 (data-driven basin)
            pred = _shrink(train, pred, SHRINK_K, third_basin_2021[target])
        if use_four.get(target):                           # stage 4 (2nd data-driven basin)
            pred = _shrink(train, pred, SHRINK_K, fourth_basin_2021[target])
        preds[target] = pred
    return preds


if __name__ == "__main__":
    fx = Findex()
    # Resilience: the P13 run showed the proxied CV adopted two-stage (6.955 < 7.209) but
    # out-of-sample MAE worsened 6.625 -> 6.730, so it reverts to the P5 single region shrink
    # under the per-target policy — the same non-transfer P8 found. Kept hard-coded off rather
    # than re-running a selector already known to mis-select for this target.
    use_two = {"fin17a_17a1_d": True, "fin24aSD_ND": False,
               "account_t_d": _select_two_stage(fx, "account_t_d")}
    # Stage 3: saving is the P16 champion (fixed); account is the P17 candidate under test.
    use_three = {"fin17a_17a1_d": _select_third_stage(fx, "fin17a_17a1_d"),
                 "account_t_d": _select_third_stage(fx, "account_t_d")}
    # Stage 4: the P18 candidate, saving only (per-target policy).
    use_four = {"fin17a_17a1_d": _select_fourth_stage(fx, "fin17a_17a1_d")}
    print(f"P18 adopted two-stage: {use_two} | three-stage: {use_three} | "
          f"four-stage: {use_four}")
    # P28: basin drift, account and saving only (resilience has no pre-2021 history).
    gammas = {t: _select_drift(fx, t) for t in ["account_t_d", "fin17a_17a1_d"]}
    print(f"P28 adopted gammas: {gammas}")
    result = fx.evaluate_predictions(predict(fx, use_two, use_three, use_four, gammas))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
