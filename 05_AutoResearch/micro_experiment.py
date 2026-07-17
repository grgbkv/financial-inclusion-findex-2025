"""U8 (pre-registered): depth-side gender gap conditional on access — among accountholders
(account==1), is formal saving at a financial institution (fin17a==1) less common among women
than men? Pooled 2024 wave, weighted.

fin17a coding: 1=yes, 2=no, 3=dk, 4=refused -> 2/3/4 treated as not-saving, NaN (not asked)
dropped. female coding: 1=female, 2=male (per the U1 coding fix). M2 cell-size gate per gender.
M3 declared n/a — within-accountholder subgroup split, no exact country-file equivalent (the
country headline bundles mobile saving and covers all adults). Descriptive, single 2024
cross-section. Complements U6 (usage-margin gender gap among accountholders: 3.4pp, discard).
"""
import numpy as np
import pandas as pd

from micro import Micro


def run(mi: Micro):
    df = mi.df
    fin17a = pd.to_numeric(df["fin17a"], errors="coerce")
    # binary: 1 -> saves formally; 2/3/4 -> does not; NaN stays NaN (not asked)
    df = df.assign(fin17a_bin=np.where(fin17a.isin([1, 2, 3, 4]),
                                       (fin17a == 1).astype(float), np.nan))

    holders = df[df["account"] == 1]
    labels = {1: "women", 2: "men"}
    rates = {}
    print("U8  formal saving (fin17a==1) among accountholders, by gender (pooled 2024):")
    for code, grp in holders.groupby("female", dropna=True):
        sub = grp.dropna(subset=["fin17a_bin", "wgt"])
        v = float(np.average(sub["fin17a_bin"], weights=sub["wgt"])) * 100
        n = len(sub)
        rates[int(code)] = (v, n)
        print(f"U8  female={int(code)} ({labels.get(int(code), '?'):5s}): "
              f"fin17a rate={v:.1f}pp  n={n}")
        print("U8 ", mi.gate_cell_size(n))

    if 1 in rates and 2 in rates:
        diff = rates[2][0] - rates[1][0]
        print(f"U8  rate_men - rate_women = {diff:+.1f}pp  (keep threshold: >= +5pp)")
        print("U8  (compare: U6 usage-margin gap among accountholders was +3.4pp, discard)")


if __name__ == "__main__":
    run(Micro())
