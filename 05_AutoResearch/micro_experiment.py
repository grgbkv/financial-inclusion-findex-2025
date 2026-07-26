"""U16 (pre-registered): does the RURAL-URBAN gradient in digital-payment use persist conditional
on access (like education/age), or collapse (like gender)?

U15 completed a gender / education / age triad on one outcome and one conditioning step: gender
collapses (U6, 3.4pp residual), education shrinks ~64% but stays large (U10, 46.7 -> 16.8pp), age
barely moves (U15, 11.6 -> 10.3pp, 10% absorbed). Urbanicity is the one major demographic axis not
yet on that ruler, and U5 supplies a real prior tension: the "too far away" barrier among the
unbanked was FLAT across rural/urban (36.0 vs 36.8pp), which would predict a small access gap --
but says nothing about the usage margin.

Primary  : weighted rate of anydigpayment == 1 among account == 1, by urbanicity (1=rural/2=urban);
           statistic = urban - rural. Keep if >= +5pp.
Secondary: same split unconditional (absorption decomposition, U10/U15 style), and the access
           margin itself (account == 1 rate by urbanicity), so both sides are reported.

Declared caveats: urbanicity correlates with education, income and employment, none controlled --
descriptive association, not a place effect; conditioning on account holding conditions on a
post-treatment variable (as in U6/U8/U10/U14/U15); urbanicity is missing for some economies, so the
pooled sample is the subset where it is coded; economy-equal pooling per micro.py
(HARNESS_V2_NOTES caveat #3) affects the exact pooled pp, not the direction. Single 2024
cross-section -- no trend language.
"""
from micro import Micro

GROUPS = [("rural", 1), ("urban", 2)]


def _split(mi: Micro, outcome, base_mask, title):
    """Weighted rate of `outcome` by urbanicity over `base_mask`."""
    print(title)
    rates = {}
    for name, code in GROUPS:
        mask = base_mask & (mi.df["urbanicity"] == code)
        v, n = mi.rate(outcome, where=mask)
        rates[name] = v
        print(f"U16   {name:6s}: rate = {v:5.1f}pp   n={n:6d}   {mi.gate_cell_size(n)}")
    diff = rates["urban"] - rates["rural"]
    print(f"U16   urban - rural = {diff:+.1f}pp")
    return diff, rates


def run(mi: Micro):
    df = mi.df
    urb_ok = df["urbanicity"].isin([1, 2])
    print(f"U16 pooled sample with urbanicity coded: n={int(urb_ok.sum())} of {len(df)} "
          f"respondents ({int(df.loc[urb_ok, 'economy'].nunique())} economies)\n")

    diff_cond, _ = _split(
        mi, "anydigpayment", urb_ok & (df["account"] == 1),
        "U16 PRIMARY -- digital-payment use by urbanicity, among ACCOUNTHOLDERS:")

    print()
    diff_uncond, _ = _split(
        mi, "anydigpayment", urb_ok,
        "U16 secondary (descriptive) -- same split, UNCONDITIONAL on account holding:")

    print()
    diff_access, _ = _split(
        mi, "account", urb_ok,
        "U16 secondary (descriptive) -- the ACCESS margin itself, account rate by urbanicity:")

    absorbed = (1 - diff_cond / diff_uncond) * 100 if diff_uncond else float("nan")
    print(f"\nU16 access absorbs {absorbed:.0f}% of the unconditional rural-urban gradient "
          f"({diff_uncond:+.1f}pp -> {diff_cond:+.1f}pp); access margin itself "
          f"{diff_access:+.1f}pp")
    print("U16 ruler: gender collapses (U6 3.4pp | account), education persists (U10 +16.8pp, "
          "~64% absorbed), age barely moves (U15 +10.3pp, 10% absorbed)")
    print(f"U16 keep condition: (urban - rural | accountholder) >= +5pp  -> "
          f"observed {diff_cond:+.1f}pp")
    print("U16 M3 declared n/a (within-accountholder split, no country-file equivalent)")


if __name__ == "__main__":
    run(Micro())
