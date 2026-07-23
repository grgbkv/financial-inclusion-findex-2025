"""U13 (pre-registered): is account ownership labour-force-status-graded?
Weighted rate of account==1 by emp_in (1=in workforce, 2=out of workforce), pooled 2024 wave.
Hypothesis: in-workforce adults hold accounts at a higher rate (wage receipt is a first-order
account on-ramp).

Motivation: emp_in is the one demographic in micro.py's DEMOGRAPHICS list no experiment has
used. The gradient map so far runs on income (M1 +10.3pp money barrier; U12 flat cost barrier),
education (U4 saving +34.1pp, U7 account +41.5pp, U9 documentation +8.2pp, U10 digital payment
| account +16.8pp), gender (U1/U3/U6/U8, small or null) and urbanicity (U5, null). Labour-force
attachment is the natural remaining stratifier and its size relative to education is unknown.

Secondary, descriptive only (not the pre-registered test): formal saving (fin17a==1) among
accountholders by emp_in -- the depth margin.

emp_in coding 1=in workforce / 2=out of workforce (NaN dropped). M2 cell-size gate per group.
M3 declared n/a for the split (the country file carries `group == "laborforce"` slices, but a
country-level version of this split is a different experiment). Declared caveat: "out of
workforce" is compositionally heterogeneous (students, retirees, homemakers, discouraged
workers) and correlates with age, gender and education -- descriptive association, not an
employment effect. Single 2024 cross-section -- no trend language.
"""
from micro import Micro

LABEL = {1: "in workforce   ", 2: "out of workforce"}


def run(mi: Micro):
    df = mi.df
    # Derived binary: saves formally (fin17a==1). In-memory only; micro.py fixed.
    df["saves_formally"] = (df["fin17a"] == 1).astype(float)

    print("U13 account ownership by labour-force status (pooled 2024):")
    rates = {}
    for e in [1, 2]:
        mask = df["emp_in"] == e
        v, n = mi.rate("account", where=mask)
        rates[e] = (v, n)
        print(f"U13 emp_in={e} ({LABEL[e]}): rate = {v:.1f}pp   n={n}   {mi.gate_cell_size(n)}")

    diff = rates[1][0] - rates[2][0]
    print(f"\nU13 in-workforce - out-of-workforce = {diff:+.1f}pp  "
          f"(keep threshold: >= +5pp, in-workforce higher)")

    print("\nU13 secondary (descriptive only): formal saving (fin17a==1) among ACCOUNTHOLDERS "
          "by labour-force status:")
    for e in [1, 2]:
        mask = (df["emp_in"] == e) & (df["account"] == 1) & (df["fin17a"].isin([1, 2, 3, 4]))
        v, n = mi.rate("saves_formally", where=mask)
        print(f"U13 emp_in={e} ({LABEL[e]}): rate = {v:.1f}pp   n={n}   {mi.gate_cell_size(n)}")

    print("\nU13 M3 declared n/a (within-emp_in subgroup split, no country-file equivalent "
          "at this granularity)")


if __name__ == "__main__":
    run(Micro())
