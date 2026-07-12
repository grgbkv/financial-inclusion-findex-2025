"""E9 (pre-registered): G2P payment digitalization (fing2p_acc, 2021 level) vs 2021-24
account growth.

fing2p_acc has no headline/narrow variant choice (single indicator) so G3 is declared
not-applicable rather than checked against INDICATORS.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    acc = fx.country_panel(fx.pan_dev, INDICATORS["account"]["headline"], [2021, 2024])
    d_acc = (acc[2024] - acc[2021]).rename("d_account_2124")

    g2p = fx.pan_dev[(fx.pan_dev["year"] == 2021) & fx.pan_dev["fing2p_acc"].notna()]
    fing2p_acc = g2p.set_index("countrynewwb")["fing2p_acc"] * 100
    fing2p_acc = fing2p_acc.rename("fing2p_acc_2021")

    w = acc["pop"]
    common = d_acc.index.intersection(fing2p_acc.index)
    print(f"E9  countries with fing2p_acc in dev panel 2021: n={len(common)}")

    r9, n9 = fx.weighted_corr(fing2p_acc.reindex(common), d_acc.reindex(common), w.reindex(common))
    print(f"E9  weighted r(fing2p_acc_2021, d_account 21-24) = {r9:.3f}  (n={n9})")

    gcov = fx.gate_coverage(fx.pan_dev.assign(fing2p_flag=fx.pan_dev["fing2p_acc"]),
                             "fing2p_flag", 2021, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(fing2p_acc.reindex(common), d_acc.reindex(common), w.reindex(common))
    print("E9 ", gcov)
    print("E9 ", gjack)


if __name__ == "__main__":
    run(Findex())
