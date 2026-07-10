"""E5b: Does the negative usage-ratio effect survive controlling for account level?

Weighted partial correlation: residualize usage_ratio and d_acc on account_2021
(weighted least squares), then correlate the residuals. Pre-registered.
"""
import numpy as np

from harness import Findex, INDICATORS


def wls_residuals(y, x, w):
    """Residuals of weighted regression y ~ 1 + x."""
    X = np.column_stack([np.ones(len(x)), x])
    W = np.diag(w / w.sum())
    beta = np.linalg.solve(X.T @ W @ X, X.T @ W @ y)
    return y - X @ beta


def run(fx: Findex):
    acc = fx.country_panel(fx.pan_dev, INDICATORS["account"]["headline"], [2021, 2024])
    dp = fx.country_panel(fx.pan_dev, INDICATORS["digital_payment"]["headline"], [2021])

    df = acc.rename(columns={2021: "acc21", 2024: "acc24"}).join(
        dp[2021].rename("dp21")).dropna()
    df["ratio"] = df["dp21"] / df["acc21"]
    df["d_acc"] = df["acc24"] - df["acc21"]

    w = df["pop"].values
    # plain convergence benchmark
    r_conv, _ = fx.weighted_corr(df["acc21"], df["d_acc"], df["pop"])

    res_ratio = wls_residuals(df["ratio"].values, df["acc21"].values, w)
    res_dacc = wls_residuals(df["d_acc"].values, df["acc21"].values, w)
    import pandas as pd
    res_ratio = pd.Series(res_ratio, index=df.index)
    res_dacc = pd.Series(res_dacc, index=df.index)
    r_partial, n = fx.weighted_corr(res_ratio, res_dacc, df["pop"])

    gates = [
        fx.gate_coverage(fx.pan_dev, INDICATORS["digital_payment"]["headline"], 2021),
        fx.gate_jackknife(res_ratio, res_dacc, df["pop"]),
    ]

    print(f"convergence benchmark r(acc21, d_acc) = {r_conv:.3f}")
    print(f"PARTIAL weighted r(ratio, d_acc | acc21) = {r_partial:.3f}  (n={n})")
    for g in gates:
        print(g)


if __name__ == "__main__":
    run(Findex())
