"""U6 (pre-registered): a usage-side gender gap conditional on access. Among adults who already
hold an account (account==1), is digital-payment adoption (anydigpayment) lower among women
(female==1) than men (female==2)? Pooled 2024 wave.

Complements the access-margin gender nulls (U1) by moving to the usage margin conditional on
having the account. anydigpayment is coded 0/1 in the labelled CSV (BINARY_OUTCOMES). female:
1=female, 2=male (per the U1 coding fix). M3 declared n/a -- this is a within-accountholder
usage subgroup split with no exact country-file equivalent (country g20_any is over all adults,
not conditional on account ownership).
"""
from micro import Micro


def run(mi: Micro):
    df = mi.df
    acc = df[df["account"] == 1]

    # overall usage among accountholders, for context
    v_all, n_all = mi._wavg(acc, "anydigpayment")
    print(f"U6  anydigpayment among accountholders (all): {v_all*100:.1f}pp  (n={n_all})")

    labels = {1: "women", 2: "men"}
    rates = {}
    for code in [1, 2]:
        sub = acc[acc["female"] == code]
        v, n = mi._wavg(sub, "anydigpayment")
        rates[code] = (v * 100 if v == v else float("nan"), n)
        print(f"U6  female={code} ({labels[code]:5s}): anydigpayment rate={rates[code][0]:.1f}pp  n={n}")
        print("U6 ", mi.gate_cell_size(n))

    diff = rates[2][0] - rates[1][0]
    print(f"U6  rate_men - rate_women = {diff:+.1f}pp")


if __name__ == "__main__":
    run(Micro())
