"""U3 (pre-registered): among unbanked adults (account==0), is the reason "a family member
already has an account" (fin11f==1) cited more by women than by men? Pooled 2024 wave.

fin11f coding: 1=yes, 2=no, 3=don't know, 4=refused, NaN=not asked. The barrier battery is
asked only of the unbanked. We treat 3/4 as not-citing; NaN (not asked) is dropped by the
weighted-mean routine. female coding: 1=female, 2=male (per the U1 fix).
"""
import numpy as np

from micro import Micro


def run(mi: Micro):
    df = mi.df.copy()
    # binary "cited fin11f", NaN where the reason battery was not answered
    df["fin11f_yes"] = np.where(df["fin11f"].isin([1, 2, 3, 4]),
                                (df["fin11f"] == 1).astype(float), np.nan)

    unbanked = df[df["account"] == 0]

    # overall prevalence among the unbanked, for context
    v_all, n_all = mi._wavg(unbanked, "fin11f_yes")
    print(f"U3  fin11f (family member has account) among all unbanked: "
          f"{v_all*100:.1f}pp  (n={n_all})")

    rates = {}
    for code, label in [(1, "women"), (2, "men")]:
        sub = unbanked[unbanked["female"] == code]
        v, n = mi._wavg(sub, "fin11f_yes")
        rates[label] = (v * 100 if v == v else float("nan"), n)
        print(f"U3  unbanked {label:5s}: fin11f rate={rates[label][0]:.1f}pp  n={n}")
        print("U3 ", mi.gate_cell_size(n))

    diff = rates["women"][0] - rates["men"][0]
    print(f"U3  rate_women - rate_men = {diff:+.1f}pp")


if __name__ == "__main__":
    run(Micro())
