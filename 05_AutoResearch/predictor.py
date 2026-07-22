"""Prediction stream — P15: a multi-indicator weighted RIDGE for account_t_d.

Every prior experiment (P1-P14) used persistence, damped trend, or basin shrinkage of a single
indicator's own history. P15 tests whether cross-indicator structure helps account: a weighted
ridge on the 2021 levels of three full-coverage features -- account_t_d, g20_any (digital
payment), fin17a_17a1_d (formal saving), all 117/117 panel coverage (mobile money dropped, only
~62/117).

Adoption rule (entirely <=2021, no 2024 anywhere): fit the ridge to predict account_2021 from the
SAME three features at 2017, weighted by 2021 adult population; select alpha by leave-one-out CV
(weighted MAE) on that 2017->2021 transition. Adopt the ridge for account ONLY IF it beats the
incumbent (persistence + two-stage income-group->region shrink, P13) on that <=2021 CV. Then apply
the fitted model to the 2021 feature levels to predict 2024.

Per-target policy (P2's rule): touches account only -- saving (damped trend + two-stage
region->income-group shrink, P12) and resilience (single region shrink, P5) stay byte-identical to
the P13 champion. Known risk: the P8/P9/P10/P13 lesson is that <=2021 model choices often fail to
transfer across the 2021 regime change, and a multi-feature fit has more parameters to overfit on
n~117.
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge

from harness import Findex

DAMP = 0.5
SHRINK_K = 0.1
INCOME_BASIN = "incomegroupwb24"
REGION_BASIN = "regionwb24_hi"

# P13 champion two-stage basin orders (stage-1, stage-2)
BASIN_ORDER = {
    "account_t_d": (INCOME_BASIN, REGION_BASIN),   # account: two-stage adopted in P13
    "fin24aSD_ND": (REGION_BASIN, INCOME_BASIN),   # resilience: single region (stage-2 off)
    "fin17a_17a1_d": (REGION_BASIN, INCOME_BASIN), # saving: two-stage adopted in P12
}
USE_TWO = {"account_t_d": True, "fin24aSD_ND": False, "fin17a_17a1_d": True}

RIDGE_FEATURES = ["account_t_d", "g20_any", "fin17a_17a1_d"]
ALPHA_GRID = [0.0, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0]


def _shrink(train, last, k, basin_col, at_year=2021):
    ref = train[train["year"] == at_year].set_index("countrynewwb")
    basin, pop = ref[basin_col], ref["pop_adult"]
    d = pd.DataFrame({"last": last, "basin": basin, "pop": pop}).dropna(subset=["last", "basin"])
    grp_mean = d.groupby("basin").apply(
        lambda g: (g["last"] * g["pop"]).sum() / g["pop"].sum(), include_groups=False)
    d["grp_mean"] = d["basin"].map(grp_mean)
    shrunk = d["last"] - k * (d["last"] - d["grp_mean"])
    return shrunk.reindex(last.index).fillna(last)


def _incumbent_account(train, at_year=2021):
    """P13 champion account predictor at `at_year` -> next wave: persistence + two-stage
    income-group->region shrink."""
    wide = train.pivot_table(index="countrynewwb", columns="year", values="account_t_d") * 100
    last = wide.get(at_year)
    b1, b2 = BASIN_ORDER["account_t_d"]
    pred = _shrink(train, last, SHRINK_K, b1, at_year=at_year)
    pred = _shrink(train, pred, SHRINK_K, b2, at_year=at_year)
    return pred


def _feature_matrix(train, year):
    """Wide feature levels (pp) at `year` for the three ridge features, indexed by country."""
    cols = {}
    for f in RIDGE_FEATURES:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=f) * 100
        cols[f] = wide.get(year)
    return pd.DataFrame(cols)


def _loo_cv_mae_ridge(X, y, w, alpha):
    """Leave-one-out weighted MAE for a ridge at fixed alpha (no standardization; features are
    all in pp on a common scale)."""
    idx = X.index.to_list()
    errs, wts = [], []
    Xv, yv, wv = X.values, y.values, w.values
    for i in range(len(idx)):
        tr = [j for j in range(len(idx)) if j != i]
        m = Ridge(alpha=alpha)
        m.fit(Xv[tr], yv[tr], sample_weight=wv[tr])
        pred_i = m.predict(Xv[i:i + 1])[0]
        errs.append(abs(pred_i - yv[i]))
        wts.append(wv[i])
    return float(np.average(errs, weights=wts))


def _ridge_account(fx: Findex):
    """Fit/select the account ridge on <=2021 only; return (cv_ridge, cv_incumbent, pred_2024,
    best_alpha)."""
    train, _ = fx.prediction_task()
    pop2021 = train[train["year"] == 2021].set_index("countrynewwb")["pop_adult"]

    # --- <=2021 CV: predict account_2021 from 2017 features ---
    X17 = _feature_matrix(train, 2017)
    y21 = (train.pivot_table(index="countrynewwb", columns="year", values="account_t_d") * 100
           ).get(2021)
    common = X17.dropna().index.intersection(y21.dropna().index).intersection(pop2021.dropna().index)
    X, y, w = X17.loc[common], y21.loc[common], pop2021.loc[common]

    cv = {a: _loo_cv_mae_ridge(X, y, w, a) for a in ALPHA_GRID}
    best_alpha = min(cv, key=cv.get)
    cv_ridge = cv[best_alpha]

    # incumbent (P13) CV on the same 2017->2021 transition, same countries
    inc_pred21 = _incumbent_account(train, at_year=2017).reindex(common)
    cv_incumbent = float(np.average((inc_pred21 - y).abs().values, weights=w.values))

    print("P15 <=2021 LOO-CV weighted MAE by alpha:",
          {a: round(v, 3) for a, v in cv.items()})
    print(f"P15 ridge best alpha={best_alpha} (CV {cv_ridge:.3f})  vs  incumbent two-stage "
          f"shrink (CV {cv_incumbent:.3f})  -> ridge_preferred={cv_ridge < cv_incumbent}")

    # --- fit on full <=2021 data, apply to 2021 features for 2024 prediction ---
    model = Ridge(alpha=best_alpha)
    model.fit(X.values, y.values, sample_weight=w.values)
    print("P15 fitted coefs", dict(zip(RIDGE_FEATURES, np.round(model.coef_, 3))),
          "intercept", round(float(model.intercept_), 3))
    X21 = _feature_matrix(train, 2021)
    Xpred = X21.dropna()
    pred_2024 = pd.Series(model.predict(Xpred.values), index=Xpred.index).clip(0, 100)
    return cv_ridge, cv_incumbent, pred_2024, best_alpha


def predict(fx: Findex, account_pred: pd.Series) -> dict:
    train, _ = fx.prediction_task()
    preds = {}
    for target in fx.PRED_TARGETS:
        if target == "account_t_d":
            preds[target] = account_pred
            continue
        wide = train.pivot_table(index="countrynewwb", columns="year", values=target) * 100
        last = wide.get(2021)
        b1, b2 = BASIN_ORDER[target]
        if target == "fin17a_17a1_d":
            prev = wide.get(2017)
            trend = (last - prev).fillna(0.0) if prev is not None else 0.0
            pred = (last + DAMP * trend).clip(0, 100).fillna(last)  # P2 damped trend
        else:
            pred = last
        pred = _shrink(train, pred, SHRINK_K, b1)          # stage 1
        if USE_TWO.get(target):                            # stage 2 (orthogonal basin)
            pred = _shrink(train, pred, SHRINK_K, b2)
        preds[target] = pred
    return preds


if __name__ == "__main__":
    fx = Findex()
    cv_ridge, cv_incumbent, ridge_pred, best_alpha = _ridge_account(fx)

    # Adoption is decided entirely on the <=2021 CV (no 2024). If the ridge does not beat the
    # incumbent there, account stays byte-identical to the P13 champion.
    if cv_ridge < cv_incumbent:
        account_pred = ridge_pred
        print(f"P15 adopting RIDGE for account (alpha={best_alpha})")
    else:
        account_pred = _incumbent_account(fx.prediction_task()[0], at_year=2021)
        print("P15 CV does NOT prefer ridge -> account stays P13 incumbent (byte-identical)")

    result = fx.evaluate_predictions(predict(fx, account_pred))
    for t, r in result.items():
        print(f"{t:20s} MAE = {r['mae']} pp  (n={r['n']})")
