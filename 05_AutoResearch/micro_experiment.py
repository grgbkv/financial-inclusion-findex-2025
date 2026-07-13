"""U4 (pre-registered): did formal saving reach the least-educated? Among all adults in the
2024 wave, is saving at a financial institution (fin17a==1) less common among primary-or-less-
educated adults (educ==1) than tertiary-educated adults (educ==3)? Pooled 2024 wave.

fin17a coding: 1=yes, 2=no, 3=don't know, 4=refused, NaN=not asked. Treat 2/3/4 as not-saving;
NaN (not asked) dropped by the weighted-mean routine. educ coding: 1=primary-or-less,
2=secondary, 3=tertiary. M3 declared n/a — the country headline fin17a_17a1_d bundles
institutional (fin17a) and mobile (fin17a1) saving, and this is a within-education subgroup split.
"""
import numpy as np

from micro import Micro


def run(mi: Micro):
    df = mi.df.copy()
    # binary "saved at a financial institution", NaN where the question was not asked
    df["fin17a_yes"] = np.where(df["fin17a"].isin([1, 2, 3, 4]),
                                (df["fin17a"] == 1).astype(float), np.nan)

    # overall prevalence, for context
    v_all, n_all = mi._wavg(df, "fin17a_yes")
    print(f"U4  formal saving (fin17a) among all adults: {v_all*100:.1f}pp  (n={n_all})")

    labels = {1: "primary-", 2: "secondary", 3: "tertiary"}
    rates = {}
    for code in [1, 2, 3]:
        sub = df[df["educ"] == code]
        v, n = mi._wavg(sub, "fin17a_yes")
        rates[code] = (v * 100 if v == v else float("nan"), n)
        print(f"U4  educ={code} ({labels[code]:9s}): fin17a rate={rates[code][0]:.1f}pp  n={n}")
        print("U4 ", mi.gate_cell_size(n))

    diff = rates[3][0] - rates[1][0]
    print(f"U4  rate_tertiary - rate_primary = {diff:+.1f}pp")


if __name__ == "__main__":
    run(Micro())
