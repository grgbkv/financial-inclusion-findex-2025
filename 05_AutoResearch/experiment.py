"""E3: Did gender gaps in account ownership close faster where mobile money grew?

Pre-registered in RESEARCH_LOG.md. Developing panel countries; gap from group2 rows.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    dev_names = set(fx.pan_dev["countrynewwb"].unique())
    grp = fx.pan_grp[fx.pan_grp["countrynewwb"].isin(dev_names)]

    def gap_for(year):
        men = grp[(grp["group2"] == "men") & (grp["year"] == year)].set_index(
            "countrynewwb")["account_t_d"] * 100
        women = grp[(grp["group2"] == "women") & (grp["year"] == year)].set_index(
            "countrynewwb")["account_t_d"] * 100
        return men - women

    d_gap = (gap_for(2024) - gap_for(2021)).rename("d_gap")
    mm = fx.country_panel(fx.pan_dev, INDICATORS["mobile_money"]["headline"], [2021, 2024])
    d_mm = (mm[2024] - mm[2021]).rename("d_mm")
    w = mm["pop"]

    r, n = fx.weighted_corr(d_gap, d_mm, w)
    gates = [
        fx.gate_coverage(fx.pan_dev, "account_t_d", 2024),
        fx.gate_jackknife(d_gap, d_mm, w),
    ]

    both = d_gap.to_frame().join(d_mm).join(w).dropna()
    both["mm_tercile"] = both["d_mm"].rank(pct=True).apply(
        lambda p: "high" if p > 2 / 3 else ("mid" if p > 1 / 3 else "low"))
    terciles = {
        t: round(float((both[both.mm_tercile == t]["d_gap"] * both[both.mm_tercile == t]["pop"]).sum()
                       / both[both.mm_tercile == t]["pop"].sum()), 2)
        for t in ["low", "mid", "high"]}

    print(f"weighted r(d_gap, d_mm) = {r:.3f}  (n={n})")
    print("weighted mean d_gap by MM-growth tercile:", terciles)
    for g in gates:
        print(g)


if __name__ == "__main__":
    run(Findex())
