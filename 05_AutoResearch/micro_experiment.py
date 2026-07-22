"""U12 (pre-registered): is the "accounts are too expensive" barrier (fin11c) income-graded?
Among unbanked adults (account==0), weighted rate of fin11c==1 by income quintile (inc_q),
poorest (q1) vs richest (q5). Pooled 2024 wave, weighted. Hypothesis: q1 higher (the
cost-of-service barrier binds hardest on the poor).

Motivation: M1 (KEEP) found the "not enough money" barrier is income-graded (+10.3pp q1->q5).
This tests whether the distinct cost-of-service barrier (fees/minimum balances, not the person's
own lack of funds) is similarly income-graded. Complements the barrier map: M1 (money/income),
U9 (documentation/education), U3 (family/gender null), U5 (distance/urbanicity null).

fin11c coding 1=yes/2=no/3=dk/4=refused (asked of unbanked only; 2/3/4 = not citing, NaN dropped).
M2 cell-size gate per quintile. M3 declared n/a -- barrier-among-unbanked split, no country-file
equivalent. Descriptive, single 2024 cross-section -- no trend language.
"""
from micro import Micro


def run(mi: Micro):
    df = mi.df
    # Derived binary: cites "too expensive" (fin11c==1). In-memory only; micro.py fixed.
    df["cites_cost"] = (df["fin11c"] == 1).astype(float)
    # Restrict to unbanked who were asked the barrier (fin11c in {1,2,3,4}).
    unbanked_asked = (df["account"] == 0) & (df["fin11c"].isin([1, 2, 3, 4]))

    print("U12 'too expensive' barrier (fin11c==1) among unbanked, by income quintile "
          "(pooled 2024):")
    rates = {}
    for q in [1, 2, 3, 4, 5]:
        mask = unbanked_asked & (df["inc_q"] == q)
        v, n = mi.rate("cites_cost", where=mask)
        rates[q] = (v, n)
        print(f"U12 inc_q={q}: rate = {v:.1f}pp   n={n}   {mi.gate_cell_size(n)}")

    diff = rates[1][0] - rates[5][0]
    print(f"\nU12 q1 - q5 = {diff:+.1f}pp  (keep threshold: >= +5pp, poorest higher)")
    print("U12 M3 declared n/a (barrier-among-unbanked split, no country-file equivalent)")


if __name__ == "__main__":
    run(Micro())
