"""U2 (pre-registered): digital payment adoption (anydigpayment) by age band, pooled 2024.
"""
import pandas as pd

from micro import Micro

BANDS = [(15, 25), (26, 35), (36, 50), (51, 65), (66, 200)]
LABELS = ["15-25", "26-35", "36-50", "51-65", "65+"]


def run(mi: Micro):
    df = mi.df.copy()
    df["age_band"] = pd.cut(df["age"], bins=[b[0] - 1 for b in BANDS] + [BANDS[-1][1]],
                             labels=LABELS)

    rows = {}
    for label in LABELS:
        sub = df[df["age_band"] == label]
        v, n = mi._wavg(sub, "anydigpayment")
        rows[label] = (v * 100 if v == v else float("nan"), n)
        print(f"U2  age {label:6s}  anydigpayment rate={rows[label][0]:.1f}pp  n={n}")
        print("U2 ", mi.gate_cell_size(n))

    diff = rows["36-50"][0] - rows["65+"][0]
    print(f"U2  rate_36_50 - rate_65plus = {diff:.1f}pp")


if __name__ == "__main__":
    run(Micro())
