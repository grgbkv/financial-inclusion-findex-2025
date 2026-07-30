"""U18 (pre-registered): does LABOUR-FORCE STATUS gate digital-payment use conditional on access,
or is U13's large access gap the whole story?

Five axes are on the access-absorption ruler for one outcome (anydigpayment) and one conditioning
step: education +16.8pp (U10), income +11.5pp (U17), age +10.3pp (U15), urbanicity +3.7pp (U16),
gender +3.4pp (U6). Labour-force status is the one demographic in micro.py's DEMOGRAPHICS list never
placed on it, and it carries the largest logged ACCESS gap of any binary split: U13 found account
ownership 76.7 vs 61.7pp in/out of the workforce (+15.0pp). The prior is two-sided: digital payments
are heavily wage- and transfer-driven (U14, E24), arguing employment persists; but out-of-workforce
adults include students and pensioners in high-digitalization economies, arguing it collapses like
gender and urbanicity.

Primary  : weighted rate of anydigpayment == 1 among account == 1, by emp_in (1 = in workforce,
           2 = out of workforce); statistic = (in - out). Keep if >= +5pp.
Secondary: same split unconditional on account, and the access margin itself (account == 1 by
           emp_in) -- the U10/U15/U16/U17 absorption decomposition, reported in RESIDUAL pp (U17's
           method lesson: the absorption share does not sort the axes).

Disclosure: the access margin used in the absorption arithmetic is ALREADY logged (U13, +15.0pp) --
that half is a known quantity, not a fresh look; the primary conditional residual is genuinely
unknown at registration.

Declared caveats: emp_in is a coarse binary pooling students, homemakers, pensioners and the
unemployed into "out of workforce"; employment correlates with age, education and income, none
controlled; conditioning on account holding conditions on a post-treatment variable
(U6/U8/U10/U14/U15/U16/U17). Single 2024 cross-section -- no trend language.
"""
from micro import Micro

STATUS = {1: "in workforce ", 2: "out of workfc"}


def _split(mi: Micro, outcome, base_mask, title):
    """Weighted rate of `outcome` by labour-force status over `base_mask`."""
    print(title)
    rates = {}
    for code, label in STATUS.items():
        mask = base_mask & (mi.df["emp_in"] == code)
        v, n = mi.rate(outcome, where=mask)
        rates[code] = v
        print(f"U18   {label} (emp_in={code}): rate = {v:5.1f}pp   n={n:6d}   {mi.gate_cell_size(n)}")
    diff = rates[1] - rates[2]
    print(f"U18   (in - out) = {diff:+.1f}pp")
    return diff, rates


def run(mi: Micro):
    df = mi.df
    emp_ok = df["emp_in"].isin(STATUS)
    print(f"U18 pooled sample with emp_in coded: n={int(emp_ok.sum())} of {len(df)} respondents "
          f"({int(df.loc[emp_ok, 'economy'].nunique())} economies)\n")

    diff_cond, _ = _split(
        mi, "anydigpayment", emp_ok & (df["account"] == 1),
        "U18 PRIMARY -- digital-payment use by labour-force status, among ACCOUNTHOLDERS:")

    print()
    diff_uncond, _ = _split(
        mi, "anydigpayment", emp_ok,
        "U18 secondary (descriptive) -- same split, UNCONDITIONAL on account holding:")

    print()
    diff_access, _ = _split(
        mi, "account", emp_ok,
        "U18 secondary (descriptive) -- the ACCESS margin itself (U13 logged +15.0pp):")

    absorbed = (1 - diff_cond / diff_uncond) * 100 if diff_uncond else float("nan")
    print(f"\nU18 access absorbs {absorbed:.0f}% of the unconditional employment gradient "
          f"({diff_uncond:+.1f}pp -> {diff_cond:+.1f}pp); access margin itself {diff_access:+.1f}pp")
    print("U18 ruler (residual pp, conditional on account): education +16.8 (U10) > income +11.5 "
          "(U17) > age +10.3 (U15) > urbanicity +3.7 (U16) > gender +3.4 (U6)")
    print(f"U18 keep condition: (in - out | accountholder) >= +5pp  -> observed {diff_cond:+.1f}pp")
    print("U18 M3 declared n/a (within-accountholder split, no country-file equivalent)")


if __name__ == "__main__":
    run(Micro())
