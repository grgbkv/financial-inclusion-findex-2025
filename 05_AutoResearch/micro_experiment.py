"""U9 (pre-registered): among unbanked adults (account==0), is the "lack of necessary
documentation" barrier (fin11d==1) cited more by the least-educated (educ==1) than by the
most-educated (educ==3)? Pooled 2024 wave, weighted.

fin11d coding: 1=yes, 2=no, 3=dk, 4=refused -> 2/3/4 = not citing, NaN (not asked) dropped.
educ coding: 1=primary-or-less, 2=secondary, 3=tertiary. M2 cell-size gate per education
group. M3 declared n/a — barrier-among-unbanked subgroup split, no country-file equivalent.
Descriptive, single 2024 cross-section. Complements M1 (income grades the money barrier fin11a,
+10.3pp) and the U3/U5 barrier nulls.
"""
import numpy as np
import pandas as pd

from micro import Micro


def run(mi: Micro):
    df = mi.df
    fin11d = pd.to_numeric(df["fin11d"], errors="coerce")
    df = df.assign(fin11d_bin=np.where(fin11d.isin([1, 2, 3, 4]),
                                       (fin11d == 1).astype(float), np.nan))

    unbanked = df[df["account"] == 0]
    labels = {1: "primary-", 2: "secondary", 3: "tertiary"}
    rates = {}
    print("U9  documentation barrier (fin11d==1) among unbanked, by education (pooled 2024):")
    for code, grp in unbanked.groupby("educ", dropna=True):
        sub = grp.dropna(subset=["fin11d_bin", "wgt"])
        v = float(np.average(sub["fin11d_bin"], weights=sub["wgt"])) * 100
        n = len(sub)
        rates[int(code)] = (v, n)
        print(f"U9  educ={int(code)} ({labels.get(int(code), '?'):9s}): "
              f"fin11d rate={v:.1f}pp  n={n}")
        print("U9 ", mi.gate_cell_size(n))

    if 1 in rates and 3 in rates:
        diff = rates[1][0] - rates[3][0]
        print(f"U9  rate_primary - rate_tertiary = {diff:+.1f}pp  (keep threshold: >= +5pp)")
        mono = rates[1][0] >= rates[2][0] >= rates[3][0] if 2 in rates else None
        print(f"U9  monotonic (primary>=secondary>=tertiary): {mono}")


if __name__ == "__main__":
    run(Micro())
