"""U5 (pre-registered): geographic gradient on a physical-access barrier. Among unbanked
adults (account==0), is "financial institutions are too far away" (fin11b==1) cited more by
rural (urbanicity==1) than urban (urbanicity==2) adults? Pooled 2024 wave.

fin11b coding: 1=yes, 2=no, 3=don't know, 4=refused, NaN=not asked/not applicable. Treat
2/3/4 as not-citing; NaN dropped by the weighted-mean routine (question only asked of the
unbanked). urbanicity: 1=rural, 2=urban (confirmed by account-rate direction: rural 66.3pp <
urban 76.6pp). M3 declared n/a — no country-file equivalent for a within-unbanked reason-split.
Complements M1 (income gradient on the money barrier) and U4 (education gradient on saving depth)
with a geographic gradient on a physical-access barrier.
"""
import numpy as np

from micro import Micro


def run(mi: Micro):
    df = mi.df.copy()
    unb = df[df["account"] == 0].copy()
    # binary "cites too-far-away", NaN where fin11b not answered
    unb["fin11b_yes"] = np.where(unb["fin11b"].isin([1, 2, 3, 4]),
                                 (unb["fin11b"] == 1).astype(float), np.nan)

    # overall prevalence among the unbanked, for context
    v_all, n_all = mi._wavg(unb, "fin11b_yes")
    print(f"U5  'too far away' (fin11b) among unbanked adults: {v_all*100:.1f}pp  (n={n_all})")

    labels = {1: "rural", 2: "urban"}
    rates = {}
    for code in [1, 2]:
        sub = unb[unb["urbanicity"] == code]
        v, n = mi._wavg(sub, "fin11b_yes")
        rates[code] = (v * 100 if v == v else float("nan"), n)
        print(f"U5  urbanicity={code} ({labels[code]:5s}): fin11b rate={rates[code][0]:.1f}pp  n={n}")
        print("U5 ", mi.gate_cell_size(n))

    diff = rates[1][0] - rates[2][0]
    print(f"U5  rate_rural - rate_urban = {diff:+.1f}pp")


if __name__ == "__main__":
    run(Micro())
