"""Prediction stream — P24: should a basin's RELIABILITY set how hard it pulls? (empirical-Bayes k)

Champion (P18, commit 1bb3f78): account = persistence + income-group -> region -> g20-tercile shrink
(5.014); saving = damped trend (l=0.5) + region -> income-group -> account-tercile -> g20-tercile
shrink (6.831); resilience = persistence + region shrink (6.625).

`k = 0.1` has been a hard constant at every stage of every stack since P5. P9 tuned it as a single
GLOBAL constant (CV picked 0.2, holdout worsened 5.144 -> 5.186) and the basin-CENTER axis is closed
by P22/P23 (unweighted median CV-rejected; population-weighted median CV-preferred by the largest
margins in the series but holdout-neutral). Untested: whether k should vary BY BASIN.

P24 candidate: replace the constant with an empirical-Bayes shape

    k_g = neff_g / (neff_g + m),   neff_g = (sum w)^2 / sum(w^2) over the basin's member countries

where w is the country's adult population. A basin whose weighted mean rests on many economies of
comparable size is a more reliable shrinkage target and should pull harder; a basin dominated by one
economy (its own weighted mean is essentially that economy) should pull less. m is a constant chosen
by CV; m -> infinity gives no shrinkage, m -> 0 gives full pooling. The incumbent constant 0.1 is NOT
in this family, so it is carried as the explicit baseline rather than as a grid point. This also
reuses the Kish machinery rule B6 just made mandatory on the hypothesis side.

Adoption rule (entirely <=2021 — no 2024 in features, fitting or selection): per target, CV on that
target's 2017->2021 transition with a persistence base and every basin built at 2017 (the
P10/P12/P13/P16-P23 protocol), grid m in {50, 150, 500, 1500, 5000}, comparing the best adaptive
stack against the identical incumbent constant-k stack at the SAME adopted stage count (account
3-stage, saving 4-stage). **Resilience is excluded by design** (no pre-2021 transition; the account
proxy is twice on record as mis-selecting for it — P8, P13) and stays byte-identical at 6.625.
Keep if for any target the <=2021 CV prefers the adaptive weight AND its 2021->2024 MAE improves on
the champion (account 5.014, saving 6.831), with every untouched target printing byte-identical.
With four CV->holdout non-transfers on record (P8, P9, P13, P23), the CV margin and the holdout delta
are both recorded whatever the verdict.
"""
import numpy as np
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
INCOME_BASIN = "incomegroupwb24"   # P7 champion basin for account
REGION_BASIN = "regionwb24_hi"     # P5/P11 champion basin for resilience & saving stage 1
M_GRID = [50, 150, 500, 1500, 5000]   # P24 candidate: k_g = neff_g / (neff_g + m)

# Per-target basin order: (stage-1 basin, candidate stage-2 basin)
BASIN_ORDER = {
    "account_t_d": (INCOME_BASIN, REGION_BASIN),
    "fin24aSD_ND": (REGION_BASIN, INCOME_BASIN),
    "fin17a_17a1_d": (REGION_BASIN, INCOME_BASIN),  # P12, fixed
}

# Per-target stage-3 DATA-DRIVEN basin: terciles of another indicator's level.
THIRD_BASIN_COL = {
    "fin17a_17a1_d": "account_t_d",   # P16
    "account_t_d": "g20_any",         # P17
}

# Per-target stage-4 DATA-DRIVEN basin (P18 champion): a SECOND cross-indicator basin.
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


def _shrink(train, last, k, basin, at_year=2021, m=None):
    """Shrink `last` toward its basin's pop-weighted mean at `at_year`.
    `basin` is either a column name in the train frame or a ready country-indexed Series.
    If `m` is given (P24), the constant k is replaced per basin by the empirical-Bayes weight
    k_g = neff_g / (neff_g + m) with neff_g the Kish effective n of the basin's population
    weights; k is then unused. Everything is computed from `at_year` <= 2021 data only."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    basin_s = ref[basin] if isinstance(basin, str) else basin.reindex(ref.index)
    pop = ref["pop_adult"]
    d = pd.DataFrame({"last": last, "basin": basin_s, "pop": pop}).dropna(
        subset=["last", "basin"])
    grp_mean = d.groupby("basin").apply(
        lambda g: (g["last"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    d["grp_mean"] = d["basin"].map(grp_mean)
    if m is None:
        kk = k
    else:
        neff = d.groupby("basin")["pop"].apply(
            lambda w: float(w.sum() ** 2 / (w ** 2).sum()))
        kk = d["basin"].map(neff / (neff + m))
    shrunk = d["last"] - kk * (d["last"] - d["grp_mean"])
    return shrunk.reindex(last.index).fillna(last)


def _stack(train, base, target, use_two, use_three, use_four, at_year, m=None):
    """Apply this target's adopted shrinkage stages to `base`, all basins built at `at_year`.
    `m=None` = incumbent constant k; `m` set = P24 adaptive weight at EVERY stage."""
    b1, b2 = BASIN_ORDER[target]
    out = _shrink(train, base, SHRINK_K, b1, at_year=at_year, m=m)
    if use_two:
        out = _shrink(train, out, SHRINK_K, b2, at_year=at_year, m=m)
    if use_three:
        b3 = _tercile_basin(train, THIRD_BASIN_COL[target], at_year)
        out = _shrink(train, out, SHRINK_K, b3, at_year=at_year, m=m)
    if use_four:
        b4 = _tercile_basin(train, FOURTH_BASIN_COL[target], at_year)
        out = _shrink(train, out, SHRINK_K, b4, at_year=at_year, m=m)
    return out


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

    s2 = _stack(train, from_2017, target, True, False, False, 2017)
    s3 = _stack(train, from_2017, target, True, True, False, 2017)
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

    s3 = _stack(train, from_2017, target, True, True, False, 2017)
    s4 = _stack(train, from_2017, target, True, True, True, 2017)
    mae_three = float((s3.reindex(common) - truth_2021.reindex(common)).abs().mean())
    mae_four = float((s4.reindex(common) - truth_2021.reindex(common)).abs().mean())
    use_four = mae_four < mae_three
    print(f"P18 pre-2021 CV {target:16s} (2017->2021, stage-4 basin = "
          f"{FOURTH_BASIN_COL[target]} terciles): three_stage={mae_three:.3f} "
          f"four_stage={mae_four:.3f}  -> four_stage={use_four}  (n={len(common)})")
    return use_four


def _select_adaptive_k(fx: Findex, target: str, use_two, use_three, use_four):
    """P24 pre-2021 CV: same protocol, same adopted stage count, constant k vs the empirical-Bayes
    weight k_g = neff_g/(neff_g+m) at every stage. Returns the winning m, or None to keep the
    incumbent constant."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)

    def mae(pred):
        return float((pred.reindex(common) - truth_2021.reindex(common)).abs().mean())

    base = mae(_stack(train, from_2017, target, use_two, use_three, use_four, 2017))
    scores = {m: mae(_stack(train, from_2017, target, use_two, use_three, use_four, 2017, m=m))
              for m in M_GRID}
    best_m = min(scores, key=scores.get)
    grid = "  ".join(f"m={m}:{v:.3f}" for m, v in scores.items())
    adopt = scores[best_m] < base
    print(f"P24 pre-2021 CV {target:16s} (2017->2021, adaptive k_g=neff_g/(neff_g+m) at every "
          f"stage): constant_k={base:.3f}  |  {grid}")
    print(f"P24   -> best m={best_m} ({scores[best_m]:.3f}), margin vs constant k = "
          f"{scores[best_m] - base:+.3f}  -> adopt={adopt}  (n={len(common)})")
    return best_m if adopt else None


def predict(fx: Findex, use_two: dict, use_three: dict, use_four: dict, adaptive_m: dict) -> dict:
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

        preds[target] = _stack(train, pred, target, use_two.get(target), use_three.get(target),
                               use_four.get(target), 2021, m=adaptive_m.get(target))
    return preds


def _report_neff(fx: Findex):
    """Descriptive: how unequal the basins actually are, which is what P24 is betting on."""
    train, _ = fx.prediction_task()
    ref = train[train["year"] == 2021].set_index("countrynewwb")
    for basin in (INCOME_BASIN, REGION_BASIN):
        stats = ref.groupby(basin)["pop_adult"].apply(
            lambda w: (len(w), float(w.sum() ** 2 / (w ** 2).sum())))
        print(f"P24 basin reliability, {basin} (n_countries, Kish neff):")
        for g, (n, ne) in stats.items():
            print(f"P24   {str(g)[:34]:36s} n={n:3d}  neff={ne:5.2f}  "
                  f"k(m=500)={ne/(ne+500):.4f}")


if __name__ == "__main__":
    fx = Findex()
    # Resilience: the P13 run showed the proxied CV adopted two-stage (6.955 < 7.209) but
    # out-of-sample MAE worsened 6.625 -> 6.730, so it reverts to the P5 single region shrink
    # under the per-target policy — the same non-transfer P8 found. Kept hard-coded off rather
    # than re-running a selector already known to mis-select for this target.
    use_two = {"fin17a_17a1_d": True, "fin24aSD_ND": False,
               "account_t_d": _select_two_stage(fx, "account_t_d")}
    use_three = {"fin17a_17a1_d": _select_third_stage(fx, "fin17a_17a1_d"),
                 "account_t_d": _select_third_stage(fx, "account_t_d")}
    use_four = {"fin17a_17a1_d": _select_fourth_stage(fx, "fin17a_17a1_d")}
    print()
    _report_neff(fx)
    print()
    # P24: resilience excluded by design (no pre-2021 transition to CV on — P8/P13 precedent).
    adaptive_m = {t: _select_adaptive_k(fx, t, use_two.get(t), use_three.get(t), use_four.get(t))
                  for t in ["account_t_d", "fin17a_17a1_d"]}
    print(f"\nP24 adopted two-stage: {use_two} | three-stage: {use_three} | "
          f"four-stage: {use_four} | adaptive m: {adaptive_m}")
    result = fx.evaluate_predictions(predict(fx, use_two, use_three, use_four, adaptive_m))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
