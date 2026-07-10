"""E2: Does flat average resilience 2021->2024 hide mobile-money-aligned heterogeneity?

Pre-registered in RESEARCH_LOG.md. Gates: G3, G4, G6.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    res = fx.country_panel(fx.pan_dev, INDICATORS["resilience"]["headline"], [2021, 2024])
    mm = fx.country_panel(fx.pan_dev, INDICATORS["mobile_money"]["headline"], [2021, 2024])

    d_res = (res[2024] - res[2021]).rename("d_res")
    d_mm = (mm[2024] - mm[2021]).rename("d_mm")
    w = res["pop"]

    r, n = fx.weighted_corr(d_res, d_mm, w)
    gates = [
        fx.gate_variant("resilience", INDICATORS["resilience"]["headline"]),
        fx.gate_coverage(fx.pan_dev, INDICATORS["resilience"]["headline"], 2024),
        fx.gate_jackknife(d_res, d_mm, w),
    ]

    both = d_res.to_frame().join(d_mm).join(w).dropna()
    both["mm_tercile"] = both["d_mm"].rank(pct=True).apply(
        lambda p: "high" if p > 2 / 3 else ("mid" if p > 1 / 3 else "low"))
    terciles = {
        t: round(float((both[both.mm_tercile == t]["d_res"] * both[both.mm_tercile == t]["pop"]).sum()
                       / both[both.mm_tercile == t]["pop"].sum()), 1)
        for t in ["low", "mid", "high"]}

    print(f"weighted r(d_res, d_mm) = {r:.3f}  (n={n})")
    print("weighted mean d_res by MM-growth tercile:", terciles)
    for g in gates:
        print(g)


if __name__ == "__main__":
    run(Findex())
