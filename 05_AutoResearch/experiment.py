"""E1: Is the 2021->2024 formal-saving surge concentrated where mobile money grew?

Pre-registered in RESEARCH_LOG.md. Developing panel countries, weighted by adult
population. Gates: G3, G4, G6.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    sav = fx.country_panel(fx.pan_dev, INDICATORS["saved_formally"]["headline"], [2021, 2024])
    mm = fx.country_panel(fx.pan_dev, INDICATORS["mobile_money"]["headline"], [2021, 2024])

    d_sav = (sav[2024] - sav[2021]).rename("d_sav")
    d_mm = (mm[2024] - mm[2021]).rename("d_mm")
    w = sav["pop"]

    r, n = fx.weighted_corr(d_sav, d_mm, w)
    gates = [
        fx.gate_variant("saved_formally", INDICATORS["saved_formally"]["headline"]),
        fx.gate_variant("mobile_money", INDICATORS["mobile_money"]["headline"]),
        fx.gate_coverage(fx.pan_dev, INDICATORS["saved_formally"]["headline"], 2024),
        fx.gate_jackknife(d_sav, d_mm, w),
    ]

    # context: the surge split by MM-growth terciles (unweighted description)
    both = d_sav.to_frame().join(d_mm).join(w).dropna()
    both["mm_tercile"] = both["d_mm"].rank(pct=True).apply(
        lambda p: "high" if p > 2 / 3 else ("mid" if p > 1 / 3 else "low"))
    terciles = {
        t: round(float((both[both.mm_tercile == t]["d_sav"] * both[both.mm_tercile == t]["pop"]).sum()
                       / both[both.mm_tercile == t]["pop"].sum()), 1)
        for t in ["low", "mid", "high"]}

    print(f"weighted r(d_sav, d_mm) = {r:.3f}  (n={n})")
    print("weighted mean d_sav by MM-growth tercile:", terciles)
    for g in gates:
        print(g)


if __name__ == "__main__":
    run(Findex())
