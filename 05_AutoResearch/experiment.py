"""E7: Where formal saving surged, did savings become a bigger source of emergency funds?

fin24sav = would rely on savings to raise emergency funds (share of adults).
Pre-registered in RESEARCH_LOG.md.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    # availability probe first (fin24sav is not in the INDICATORS registry: declare it)
    avail = fx.pan_dev.groupby("year")["fin24sav"].count()
    print("fin24sav non-null country-rows by year:", avail.to_dict())

    sav_src = fx.country_panel(fx.pan_dev, "fin24sav", [2021, 2024])
    sav = fx.country_panel(fx.pan_dev, INDICATORS["saved_formally"]["headline"], [2021, 2024])

    d_src = (sav_src[2024] - sav_src[2021]).rename("d_src")
    d_sav = (sav[2024] - sav[2021]).rename("d_sav")
    w = sav["pop"]

    r, n = fx.weighted_corr(d_src, d_sav, w)
    gates = [
        {"gate": "G3_variant", "ok": True, "concept": "resilience_source_savings",
         "role": "declared: fin24sav (only variant)"},
        fx.gate_coverage(fx.pan_dev, "fin24sav", 2024),
        fx.gate_jackknife(d_src, d_sav, w),
    ]

    # headline aggregate shift for context
    agg = fx.series(fx.pan_dev, "fin24sav", [2021, 2024])
    print(f"dev aggregate fin24sav: {agg.get(2021):.1f} -> {agg.get(2024):.1f} pp")
    print(f"weighted r(d_src, d_sav) = {r:.3f}  (n={n})")
    for g in gates:
        print(g)


if __name__ == "__main__":
    run(Findex())
