"""E8 (pre-registered): money-barrier prevalence (fin11a, 2024) vs 2021-24 account growth.

fin11a has no headline/narrow variant choice (single indicator, 2024-only fielding) so G3
is declared not-applicable rather than checked against INDICATORS.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    acc = fx.country_panel(fx.pan_dev, INDICATORS["account"]["headline"], [2021, 2024])
    d_acc = (acc[2024] - acc[2021]).rename("d_account_2124")

    bar = fx.pan_dev[(fx.pan_dev["year"] == 2024) & fx.pan_dev["fin11a"].notna()]
    fin11a = bar.set_index("countrynewwb")["fin11a"] * 100
    fin11a = fin11a.rename("fin11a_2024")

    w = acc["pop"]
    common = d_acc.index.intersection(fin11a.index)
    print(f"E8  countries with fin11a in dev panel: n={len(common)}")

    r8, n8 = fx.weighted_corr(fin11a.reindex(common), d_acc.reindex(common), w.reindex(common))
    print(f"E8  weighted r(fin11a_2024, d_account 21-24) = {r8:.3f}  (n={n8})")

    gcov = fx.gate_coverage(fx.pan_dev.assign(fin11a_flag=fx.pan_dev["fin11a"]),
                             "fin11a_flag", 2024, min_countries=30, min_pop_share=0.3)
    gjack = fx.gate_jackknife(fin11a.reindex(common), d_acc.reindex(common), w.reindex(common))
    print("E8 ", gcov)
    print("E8 ", gjack)


if __name__ == "__main__":
    run(Findex())
