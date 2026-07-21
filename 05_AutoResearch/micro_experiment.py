"""U11 (pre-registered): does mobile money reach the poor? Among accountholders, are mobile-only
accountholders (account_mob==1 & account_fin==0) drawn more from the poorest two income quintiles
(inc_q in {1,2}) than bank-only accountholders (account_fin==1 & account_mob==0)? Pooled 2024
wave, weighted.

Motivation: M2 (KEEP) found mobile-only accountholders are younger and less educated than
bank-only -- an on-ramp for the underserved on the age/education margins. The income margin was
never tested and is the sharpest test of the "mobile money reaches the poor" policy claim.

M2 cell-size gate per group. M3 declared n/a -- within-accountholder composition split, no exact
country-file equivalent. Descriptive, single 2024 cross-section -- no trend language.
"""
from micro import Micro


def run(mi: Micro):
    df = mi.df
    # Derived binary: bottom-two income quintiles (poorest 40%). In-memory only; micro.py fixed.
    df["poor2"] = (df["inc_q"].isin([1, 2])).astype(float)

    groups = {
        "mobile-only": (df["account_mob"] == 1) & (df["account_fin"] == 0),
        "bank-only": (df["account_fin"] == 1) & (df["account_mob"] == 0),
    }

    rates = {}
    print("U11 share in poorest-two income quintiles, by accountholder type (pooled 2024):")
    for label, mask in groups.items():
        v, n = mi.rate("poor2", where=mask)
        rates[label] = (v, n)
        print(f"U11 {label:12s}: poor2_share = {v:.1f}pp   n={n}")
        print("U11 ", mi.gate_cell_size(n))

    diff = rates["mobile-only"][0] - rates["bank-only"][0]
    print(f"\nU11 mobile-only - bank-only = {diff:+.1f}pp  (keep threshold: >= +5pp, "
          f"mobile-only higher)")

    # Full quintile profile for context (not a keep condition).
    print("\nU11 context -- full income-quintile profile of each group (weighted share):")
    for label, mask in groups.items():
        parts = []
        for q in [1, 2, 3, 4, 5]:
            df["_q"] = (df["inc_q"] == q).astype(float)
            v, _ = mi.rate("_q", where=mask)
            parts.append(f"q{q}={v:.0f}")
        print(f"U11 {label:12s}: " + " ".join(parts))


if __name__ == "__main__":
    run(Micro())
