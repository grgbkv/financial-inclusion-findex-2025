"""U1 (pre-registered): gender gap in account ownership, poorest vs richest income quintile.
"""
from micro import Micro


def run(mi: Micro):
    df = mi.df

    # raw questionnaire coding: female==1 -> female, female==2 -> male
    rows = {}
    for f in (1, 2):
        for q in (1, 5):
            sub = df[(df["female"] == f) & (df["inc_q"] == q)]
            v, n = mi._wavg(sub, "account")
            rows[(f, q)] = (v * 100 if v == v else float("nan"), n)
            label = "female" if f == 1 else "male"
            print(f"U1  {label} inc_q={q}  account rate={rows[(f,q)][0]:.1f}pp  n={n}")
            print("U1 ", mi.gate_cell_size(n))

    gap_q1 = rows[(2, 1)][0] - rows[(1, 1)][0]
    gap_q5 = rows[(2, 5)][0] - rows[(1, 5)][0]
    print(f"U1  gender gap (male-female) q1={gap_q1:.1f}pp  q5={gap_q5:.1f}pp")
    print(f"U1  gap_q1 - gap_q5 = {gap_q1 - gap_q5:.1f}pp")


if __name__ == "__main__":
    run(Micro())
