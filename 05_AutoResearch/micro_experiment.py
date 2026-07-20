"""U10 (pre-registered): conditional on holding an account, is digital-payment usage
(anydigpayment) education-graded? Weighted rate of anydigpayment==1 among account==1, split by
educ (1=primary-or-less / 2=secondary / 3=tertiary), pooled 2024 wave.

Motivation: every conditional-on-access result so far is a gender split and all came back small
(U6 usage-side 3.4pp, U8 depth-side 4.96pp), while the unconditional education gradients are the
largest effects in the micro stream (U7 account 41.5pp, U4 formal saving 34.1pp). This tests
whether "conditional on access, gaps are small" is a general property of the access margin
having done the sorting, or is specific to gender.

M2 cell-size gate per education group. M3 declared n/a -- within-accountholder subgroup split,
no exact country-file equivalent. Descriptive, single 2024 cross-section.
"""
import numpy as np

from micro import Micro


def run(mi: Micro):
    df = mi.df
    holders = df[df["account"] == 1]

    labels = {1: "primary-", 2: "secondary", 3: "tertiary"}
    rates = {}
    print("U10 anydigpayment among accountholders, by education (pooled 2024):")
    for code, grp in holders.groupby("educ", dropna=True):
        sub = grp.dropna(subset=["anydigpayment", "wgt"])
        v = float(np.average(sub["anydigpayment"], weights=sub["wgt"])) * 100
        n = len(sub)
        rates[int(code)] = (v, n)
        print(f"U10 educ={int(code)} ({labels.get(int(code), '?'):9s}): "
              f"anydigpayment={v:.1f}pp  n={n}")
        print("U10 ", mi.gate_cell_size(n))

    if 1 in rates and 3 in rates:
        diff = rates[3][0] - rates[1][0]
        print(f"U10 rate_tertiary - rate_primary = {diff:+.1f}pp  (keep threshold: >= +5pp)")
        mono = rates[3][0] >= rates[2][0] >= rates[1][0] if 2 in rates else None
        print(f"U10 monotonic (tertiary>=secondary>=primary): {mono}")

    # Context for the comparison the hypothesis is about: the same gradient unconditionally.
    print("\nU10 context (unconditional, all adults) -- not the pre-registered test:")
    for code, grp in df.groupby("educ", dropna=True):
        sub = grp.dropna(subset=["anydigpayment", "wgt"])
        v = float(np.average(sub["anydigpayment"], weights=sub["wgt"])) * 100
        print(f"U10 educ={int(code)} ({labels.get(int(code), '?'):9s}): "
              f"anydigpayment={v:.1f}pp  n={len(sub)}")


if __name__ == "__main__":
    run(Micro())
