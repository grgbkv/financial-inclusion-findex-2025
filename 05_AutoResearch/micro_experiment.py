"""U14 (pre-registered): among adults who ALREADY HOLD AN ACCOUNT and receive wages, is the share
whose wages arrive IN the account (rather than in cash) education-graded?

The individual-level counterpart of E10 (country-level wage digitalization co-moves with the
formal-saving surge, r=0.791, KEEP), and an extension of the strongest micro thread: conditional
on access, gender gaps collapse (U6 3.4pp, U8 4.96pp) but education gaps do not (U10, digital
payment | account, +16.8pp). Whether that asymmetry survives on the WAGE-RECEIPT margin — where
the employer, not the adult, picks the payment mode — is the open question. First use of
`receive_wages`.

CODING DISCLOSURE (structural inference, not an outcome peek). `receive_wages` sits in micro.py's
BINARY_OUTCOMES but is a 5-code categorical, and no codebook ships with the microdata zip, so the
coding was inferred before registration:
    1 = received into an account (anydigpayment = 1.00, account_fin = 0.93 within the cell)
    2 = received in cash        (account_fin = 0.36, no better than non-receivers)
    3 = other / in-kind (n=833)   4 = did not receive (n=63,640)   5 = DK/refused (n=202)
The same check killed the obvious design: `receive_transfers == 1` implies `account == 1` in
7,184/7,184 cases, so any wage/transfer-receipt -> account-ownership test is circular by
construction. The registered outcome — the education gradient — was unknown at registration.

Declared caveats: wage-receipt mode is largely an employer/sector attribute, so this is a
descriptive association with education, not an individual choice or an education effect; the
account-holding restriction conditions on a post-treatment variable; formal-vs-informal sectoral
composition is an obvious uncontrolled confound. Single 2024 cross-section — no trend language.
"""
from micro import Micro

EDUC_LABEL = {1: "primary or less", 2: "secondary      ", 3: "tertiary       "}
WAGE_RECEIVERS = [1, 2, 3]   # excludes 4 (did not receive) and 5 (DK/refused)


def _gradient(mi: Micro, base_mask, title):
    """Weighted rate of digital wage receipt by education over `base_mask`."""
    print(title)
    rates = {}
    for e in [1, 2, 3]:
        mask = base_mask & (mi.df["educ"] == e)
        v, n = mi.rate("wage_digital", where=mask)
        rates[e] = v
        print(f"U14   educ={e} ({EDUC_LABEL[e]}): rate = {v:5.1f}pp   n={n:6d}   "
              f"{mi.gate_cell_size(n)}")
    diff = rates[3] - rates[1]
    print(f"U14   tertiary - primary = {diff:+.1f}pp")
    return diff


def run(mi: Micro):
    df = mi.df
    # Derived binary: wages arrive in an account rather than cash/in-kind.
    # In-memory only; micro.py is fixed.
    df["wage_digital"] = (df["receive_wages"] == 1).astype(float)

    receivers = df["receive_wages"].isin(WAGE_RECEIVERS)
    v_all, n_all = mi.rate("wage_digital", where=receivers)
    print(f"U14 base rate: among wage receivers (codes 1/2/3, n={n_all}), "
          f"{v_all:.1f}pp receive wages into an account\n")

    diff_cond = _gradient(
        mi, receivers & (df["account"] == 1),
        "U14 PRIMARY — digital wage receipt by education, among ACCOUNTHOLDING wage receivers:")

    print()
    diff_uncond = _gradient(
        mi, receivers,
        "U14 secondary (descriptive only) — same split, UNCONDITIONAL on account holding:")

    absorbed = (1 - diff_cond / diff_uncond) * 100 if diff_uncond else float("nan")
    print(f"\nU14 access absorbs {absorbed:.0f}% of the unconditional education gradient "
          f"({diff_uncond:+.1f}pp -> {diff_cond:+.1f}pp)   [U10 comparison: 46.7 -> 16.8pp, ~64%]")
    print(f"U14 keep condition: (tertiary - primary | accountholder) >= +5pp  -> "
          f"observed {diff_cond:+.1f}pp")
    print("U14 M3 declared n/a (conditional within-accountholder wage-receipt split, no "
          "country-file equivalent at this granularity)")


if __name__ == "__main__":
    run(Micro())
