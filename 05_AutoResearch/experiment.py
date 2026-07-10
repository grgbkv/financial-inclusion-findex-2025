"""E4 + E6 in one run (both pre-registered; independent tests).

E4: dormancy J-curve — bigger account drives 2014->2017 -> higher inactivity ratio in 2017.
E6: income-gap reversion — bigger poorest-40 jumps 2017->2021 -> bigger gap re-widening 2021->2024.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    # ---------------- E4
    acc = fx.country_panel(fx.pan_dev, INDICATORS["account"]["headline"], [2014, 2017])
    inact = fx.country_panel(fx.pan_dev, INDICATORS["inactive"]["headline"], [2017])
    d_acc = (acc[2017] - acc[2014]).rename("d_acc_1417")
    inact_ratio = (inact[2017] / acc[2017] * 100).rename("inact_ratio_17")
    w = acc["pop"]
    r4, n4 = fx.weighted_corr(d_acc, inact_ratio, w)
    g4 = [fx.gate_coverage(fx.pan_dev, INDICATORS["inactive"]["headline"], 2017),
          fx.gate_jackknife(d_acc, inact_ratio, w)]
    print(f"E4  weighted r(d_acc 14-17, inactive-ratio 17) = {r4:.3f}  (n={n4})")
    for g in g4:
        print("E4 ", g)

    # ---------------- E6
    dev_names = set(fx.pan_dev["countrynewwb"].unique())
    grp = fx.pan_grp[fx.pan_grp["countrynewwb"].isin(dev_names)]

    def series_g2(g2, year):
        return grp[(grp["group2"] == g2) & (grp["year"] == year)].set_index(
            "countrynewwb")["account_t_d"] * 100

    poor17, poor21 = series_g2("poorest 40%", 2017), series_g2("poorest 40%", 2021)
    rich21, poor21b = series_g2("richest 60%", 2021), poor21
    rich24, poor24 = series_g2("richest 60%", 2024), series_g2("poorest 40%", 2024)

    d_poor_1721 = (poor21 - poor17).rename("d_poor")
    gap21 = rich21 - poor21b
    gap24 = rich24 - poor24
    d_gap_2124 = (gap24 - gap21).rename("d_gap")
    r6, n6 = fx.weighted_corr(d_poor_1721, d_gap_2124, w)
    g6 = [fx.gate_coverage(fx.pan_dev, INDICATORS["account"]["headline"], 2024),
          fx.gate_jackknife(d_poor_1721, d_gap_2124, w)]
    print(f"E6  weighted r(d_poor40 17-21, d_gap 21-24) = {r6:.3f}  (n={n6})")
    for g in g6:
        print("E6 ", g)


if __name__ == "__main__":
    run(Findex())
