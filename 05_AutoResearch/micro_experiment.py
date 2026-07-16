"""U7 (pre-registered): does education stratify the ACCESS margin (account ownership) as well as
the depth margin (U4's 34.1pp education gradient on formal saving), but less sharply? Weighted
rate of account==1 by educ (1=primary-or-less, 2=secondary, 3=tertiary), pooled 2024 wave.

account is coded 0/1 in the labelled CSV (BINARY_OUTCOMES). M2 cell-size gate per educ group.
M3 declared n/a -- this is a within-education subgroup split; the pooled economy-equal by-group
rate has no exact country-file equivalent. Descriptive, single 2024 cross-section.
"""
from micro import Micro


def run(mi: Micro):
    labels = {1: "primary-", 2: "secondary", 3: "tertiary"}

    tab = mi.rate_by("account", "educ")
    print("U7  account ownership by education (pooled 2024):")
    rates = {}
    for _, row in tab.iterrows():
        code = int(row["educ"])
        rates[code] = (row["rate_pp"], int(row["n_unweighted"]))
        print(f"U7  educ={code} ({labels.get(code, '?'):9s}): account rate={row['rate_pp']:.1f}pp"
              f"  n={int(row['n_unweighted'])}")
        print("U7 ", mi.gate_cell_size(int(row["n_unweighted"])))

    if 3 in rates and 1 in rates:
        diff = rates[3][0] - rates[1][0]
        print(f"U7  rate_tertiary - rate_primary = {diff:+.1f}pp")
        print(f"U7  (compare: U4 depth gradient on formal saving was +34.1pp)")


if __name__ == "__main__":
    run(Micro())
