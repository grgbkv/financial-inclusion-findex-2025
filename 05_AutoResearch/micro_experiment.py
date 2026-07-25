"""U15 (pre-registered): conditional on holding an account, does the AGE gradient in
digital-payment use persist (like education) or collapse (like gender)?

The strongest micro thread is an asymmetry in what access equalizes. Conditional on an account,
gender gaps collapse (U6 3.4pp, U8 4.96pp) while education gaps persist (U10 +16.8pp, ~64% of the
unconditional gap absorbed; U14 +35.3pp, only 31% absorbed). U2 established the UNCONDITIONAL age
profile of `anydigpayment` (45.0 / 59.7 / 56.8 / 53.5 / 48.1pp across 15-25 / 26-35 / 36-50 /
51-65 / 65+, inverted-U peaking at 26-35). Whether that gradient is an access artifact — older
adults simply being less banked — or survives conditioning is unknown, and answering it completes
the gender / education / age triad on one common outcome.

Primary  : weighted rate of anydigpayment == 1 among account == 1, by the five U2 age bands;
           statistic = (26-35) - (65+). Keep if >= +5pp.
Secondary: the U10-style absorption decomposition against U2's unconditional 11.6pp gap for the
           same pair (recomputed here unconditionally so both sides use identical construction).

Declared caveats: age correlates with education, employment and account tenure, none controlled —
descriptive association, not an age effect; conditioning on account holding conditions on a
post-treatment variable (as in U6/U8/U10/U14); economy-equal pooling per micro.py
(HARNESS_V2_NOTES caveat #3) affects the exact pooled pp, not the direction. Single 2024
cross-section — no trend language.
"""
import pandas as pd

from micro import Micro

BANDS = [("15-25", 15, 25), ("26-35", 26, 35), ("36-50", 36, 50),
         ("51-65", 51, 65), ("65+", 66, 200)]
PEAK, LOW = "26-35", "65+"          # U2's peak band vs its low band


def _profile(mi: Micro, base_mask, title):
    """Weighted anydigpayment rate by age band over `base_mask`."""
    print(title)
    rates = {}
    for name, lo, hi in BANDS:
        mask = base_mask & (mi.df["age"] >= lo) & (mi.df["age"] <= hi)
        v, n = mi.rate("anydigpayment", where=mask)
        rates[name] = v
        print(f"U15   age {name:6s}: rate = {v:5.1f}pp   n={n:6d}   {mi.gate_cell_size(n)}")
    diff = rates[PEAK] - rates[LOW]
    print(f"U15   ({PEAK}) - ({LOW}) = {diff:+.1f}pp")
    return diff, rates


def run(mi: Micro):
    df = mi.df
    age_ok = pd.to_numeric(df["age"], errors="coerce").notna()
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    diff_cond, rates_cond = _profile(
        mi, age_ok & (df["account"] == 1),
        "U15 PRIMARY -- digital-payment use by age band, among ACCOUNTHOLDERS:")

    print()
    diff_uncond, rates_uncond = _profile(
        mi, age_ok,
        "U15 secondary (descriptive) -- same split, UNCONDITIONAL on account holding:")

    absorbed = (1 - diff_cond / diff_uncond) * 100 if diff_uncond else float("nan")
    print(f"\nU15 access absorbs {absorbed:.0f}% of the unconditional age gradient "
          f"({diff_uncond:+.1f}pp -> {diff_cond:+.1f}pp)")
    print("U15 comparisons: gender collapses (U6 3.4pp), education persists "
          "(U10 +16.8pp | account, ~64% absorbed; U14 +35.3pp, 31% absorbed)")
    print(f"U15 keep condition: ({PEAK} - {LOW} | accountholder) >= +5pp  -> "
          f"observed {diff_cond:+.1f}pp")
    print("U15 M3 declared n/a (within-accountholder split, no country-file equivalent)")


if __name__ == "__main__":
    run(Micro())
