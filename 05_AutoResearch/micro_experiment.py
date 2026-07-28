"""U17 (pre-registered): does the INCOME gradient in digital-payment use persist conditional on
access (like education/age), or collapse (like gender/urbanicity)?

Four axes are on the access-absorption ruler for one outcome (anydigpayment) and one conditioning
step: gender collapses (U6, 3.4pp), urbanicity collapses (U16, 3.7pp, 66% absorbed), education
persists large (U10, 16.8pp, ~64% absorbed), age barely moves (U15, 10.3pp, 10% absorbed). INCOME
QUINTILE is the one major demographic axis never placed on it -- conspicuous, because income has the
strongest prior evidence on the BARRIER side (M1: money barrier among the unbanked income-graded by
+10.3pp) and a genuinely ambiguous prior on the usage side (U11: mobile-only holders are not poorer
than bank-only; U12: the cost barrier is flat across income).

Primary  : weighted rate of anydigpayment == 1 among account == 1, by inc_q (1=poorest..5=richest);
           statistic = q5 - q1. Keep if >= +5pp.
Secondary: same split unconditional (absorption decomposition, U10/U15/U16 style), and the access
           margin itself (account == 1 rate by inc_q); full five-band shape for monotonicity.

Declared caveats: inc_q is a WITHIN-ECONOMY RELATIVE quintile, so economy-equal pooling mixes
economies (HARNESS_V2_NOTES caveat #3) -- a relative-rank axis, not an absolute-income axis, which
distinguishes it from education/age; income correlates with education, employment and urbanicity,
none controlled; conditioning on account holding conditions on a post-treatment variable
(U6/U8/U10/U14/U15/U16). Single 2024 cross-section -- no trend language.
"""
from micro import Micro

QUINTILES = [1, 2, 3, 4, 5]


def _split(mi: Micro, outcome, base_mask, title):
    """Weighted rate of `outcome` by income quintile over `base_mask`."""
    print(title)
    rates = {}
    for q in QUINTILES:
        mask = base_mask & (mi.df["inc_q"] == q)
        v, n = mi.rate(outcome, where=mask)
        rates[q] = v
        print(f"U17   q{q}: rate = {v:5.1f}pp   n={n:6d}   {mi.gate_cell_size(n)}")
    diff = rates[5] - rates[1]
    shape = "/".join(f"{rates[q]:.1f}" for q in QUINTILES)
    mono = all(rates[q] <= rates[q + 1] for q in QUINTILES[:-1])
    print(f"U17   q5 - q1 = {diff:+.1f}pp   shape {shape}   monotone_increasing={mono}")
    return diff, rates


def run(mi: Micro):
    df = mi.df
    inc_ok = df["inc_q"].isin(QUINTILES)
    print(f"U17 pooled sample with inc_q coded: n={int(inc_ok.sum())} of {len(df)} respondents "
          f"({int(df.loc[inc_ok, 'economy'].nunique())} economies)\n")

    diff_cond, _ = _split(
        mi, "anydigpayment", inc_ok & (df["account"] == 1),
        "U17 PRIMARY -- digital-payment use by income quintile, among ACCOUNTHOLDERS:")

    print()
    diff_uncond, _ = _split(
        mi, "anydigpayment", inc_ok,
        "U17 secondary (descriptive) -- same split, UNCONDITIONAL on account holding:")

    print()
    diff_access, _ = _split(
        mi, "account", inc_ok,
        "U17 secondary (descriptive) -- the ACCESS margin itself, account rate by income quintile:")

    absorbed = (1 - diff_cond / diff_uncond) * 100 if diff_uncond else float("nan")
    print(f"\nU17 access absorbs {absorbed:.0f}% of the unconditional income gradient "
          f"({diff_uncond:+.1f}pp -> {diff_cond:+.1f}pp); access margin itself {diff_access:+.1f}pp")
    print("U17 ruler: gender collapses (U6 3.4pp), urbanicity collapses (U16 3.7pp, 66% absorbed), "
          "education persists (U10 +16.8pp, ~64% absorbed), age barely moves (U15 +10.3pp, 10%)")
    print(f"U17 keep condition: (q5 - q1 | accountholder) >= +5pp  -> observed {diff_cond:+.1f}pp")
    print("U17 M3 declared n/a (within-accountholder split, no country-file equivalent)")


if __name__ == "__main__":
    run(Micro())
