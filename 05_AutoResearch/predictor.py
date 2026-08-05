"""Prediction stream — P26: is the TERCILE the right RESOLUTION for the data-driven basins?

Champion (P18, 1bb3f78): account 5.014 = persistence + income-group -> region -> g20-tercile shrink;
saving 6.831 = damped trend (l=0.5) + region -> income-group -> account-tercile -> g20-tercile
shrink; resilience 6.625 = persistence + region shrink. k = 0.1 at every stage.

MOTIVATION. P24/P25 closed the adaptive-`k` axis; P22/P23 closed the basin CENTER; P9 closed the
global constant. The 2026-08-03 agenda addendum records the one live direction as the BASINS
THEMSELVES. Every data-driven basin in the champion is a TERCILE — a number never chosen, only
inherited from P16. Bin count trades bias (coarse basins pool unlike countries) against variance
(fine basins have unreliable means), and unlike `k` it is a property of the PARTITION, which is the
part of the operator that has kept paying (P16 -0.279pp, P17 -0.091pp, P18 -0.249pp).

DESIGN. One shared bin count B applied to ALL data-driven basins of a target, selected per target by
the established <=2021 CV (2017->2021, persistence base, every basin built from the 2017
cross-section). Grid B in {2, 3, 4, 5, 6}, with B = 3 the incumbent, EXACTLY NESTED (as P25's m->0
nested the constant k). Administrative basins (region, income group) are unchanged — they have no
bin count. Per-target policy (P2): resilience has no data-driven stage and stays byte-identical.

ADOPTION RULE. Adopt B != 3 for a target only if the <=2021 CV STRICTLY PREFERS it; then, and only
then, evaluate the 2024 holdout, and keep only if the holdout MAE also improves (the P11/P16/P17
condition — CV AND holdout, given the four CV->holdout non-transfers on record: P8, P9, P13, P23).
If CV does not prefer any B != 3, adoption fails at the first gate, no 2024 evaluation is run
(P14/P15/P19/P20/P21 protocol) and predictor.py reverts to the P18 champion.

No 2024 data anywhere in features, fitting or selection.

REGISTERED QUESTION. Is the tercile a TUNED choice or an ARBITRARY one that happens to work?
"""
import pandas as pd

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
INCOME_BASIN = "incomegroupwb24"   # P7 champion basin for account
REGION_BASIN = "regionwb24_hi"     # P5/P11 champion basin for resilience & saving stage 1

INCUMBENT_BINS = 3                 # P16/P17/P18 inherited default
BIN_GRID = [2, 3, 4, 5, 6]         # P26 candidate grid; B=3 nests the incumbent exactly

# Per-target basin order: (stage-1 basin, stage-2 basin)
BASIN_ORDER = {
    "account_t_d": (INCOME_BASIN, REGION_BASIN),
    "fin24aSD_ND": (REGION_BASIN, INCOME_BASIN),
    "fin17a_17a1_d": (REGION_BASIN, INCOME_BASIN),  # P12, fixed
}

# Data-driven basin columns, in stage order, per target (P16/P17/P18 champions).
DATA_BASIN_COLS = {
    "fin17a_17a1_d": ["account_t_d", "g20_any"],   # stage 3, stage 4
    "account_t_d": ["g20_any"],                    # stage 3
}


def _tile_basin(train, col, at_year, bins=INCUMBENT_BINS):
    """Data-driven basin: `bins`-quantile tiles of `col`'s level at `at_year`. Built from <=2021
    data only; cuts across region and income group. bins=3 reproduces P16/P17/P18's tercile."""
    ref = train[train["year"] == at_year].set_index("countrynewwb")[col].dropna()
    if len(ref) < 3 * bins:
        return pd.Series(dtype=object)
    q = pd.qcut(ref, bins, labels=False, duplicates="drop")
    return q.map(lambda i: f"tile{int(i)}_of{bins}").astype(object)


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


def _stack(train, base, target, at_year, bins, n_data_stages):
    """The target's full champion shrink stack applied to `base`, with the data-driven stages cut
    into `bins` tiles. Administrative stages are unchanged."""
    b1, b2 = BASIN_ORDER[target]
    out = _shrink(train, base, SHRINK_K, b1, at_year=at_year)
    out = _shrink(train, out, SHRINK_K, b2, at_year=at_year)
    for col in DATA_BASIN_COLS[target][:n_data_stages]:
        basin = _tile_basin(train, col, at_year, bins)
        out = _shrink(train, out, SHRINK_K, basin, at_year=at_year)
    return out


def _select_bins(fx: Findex, target: str):
    """P26 pre-2021 CV: predict `target` 2021 from 2017 (persistence base, the P12/P16/P17/P18
    protocol), every basin built at 2017, the target's full champion stack, sweeping the shared
    bin count over BIN_GRID. Returns (chosen_bins, table)."""
    train, _ = fx.prediction_task()
    wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
    truth_2021, from_2017 = wide.get(2021), wide.get(2017)
    common = truth_2021.dropna().index.intersection(from_2017.dropna().index)
    n_stages = len(DATA_BASIN_COLS[target])

    table = {}
    for b in BIN_GRID:
        pred = _stack(train, from_2017, target, 2017, b, n_stages)
        table[b] = float((pred.reindex(common) - truth_2021.reindex(common)).abs().mean())

    best = min(table, key=table.get)
    incumbent = table[INCUMBENT_BINS]
    # Adopt a non-incumbent B only on a STRICT CV improvement.
    chosen = best if table[best] < incumbent else INCUMBENT_BINS
    grid = "  ".join(f"B={b}: {v:.3f}" for b, v in table.items())
    print(f"P26 pre-2021 CV {target:16s} (2017->2021, {n_stages} data-driven stage(s), "
          f"basins at 2017, n={len(common)})")
    print(f"    {grid}")
    print(f"    incumbent B={INCUMBENT_BINS}: {incumbent:.3f}  best B={best}: {table[best]:.3f}  "
          f"margin {table[best] - incumbent:+.3f}  -> adopted B={chosen}"
          f"{'' if chosen != INCUMBENT_BINS else '  (incumbent retained)'}")
    return chosen, table


def predict(fx: Findex, bins: dict) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)

        if target == "fin24aSD_ND":
            # P5 champion: persistence + single region shrink. No data-driven stage, no bin count.
            preds[target] = _shrink(train, last, SHRINK_K, REGION_BASIN)
            continue

        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            base = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
        else:
            base = last

        preds[target] = _stack(train, base, target, 2021, bins[target],
                               len(DATA_BASIN_COLS[target]))
    return preds


if __name__ == "__main__":
    fx = Findex()
    bins = {t: _select_bins(fx, t)[0] for t in ("account_t_d", "fin17a_17a1_d")}
    print(f"\nP26 adopted bin counts: {bins}  (incumbent = {INCUMBENT_BINS} on both)")
    if all(b == INCUMBENT_BINS for b in bins.values()):
        print("P26: CV prefers the incumbent tercile on BOTH targets — adoption fails at the "
              "first gate. Holdout below is the P18 champion, re-run to confirm it is unchanged.")
    result = fx.evaluate_predictions(predict(fx, bins))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
