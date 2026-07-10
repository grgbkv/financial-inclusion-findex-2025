"""E5: Is digital-payment usage a leading indicator of account-ownership growth?

"Usage headroom": countries where accounts are used intensively (g20_any close to or
above account level) should convert usage pressure into new accounts 2021->2024.
Pre-registered in RESEARCH_LOG.md.
"""
from harness import Findex, INDICATORS


def run(fx: Findex):
    acc = fx.country_panel(fx.pan_dev, INDICATORS["account"]["headline"], [2021, 2024])
    dp = fx.country_panel(fx.pan_dev, INDICATORS["digital_payment"]["headline"], [2021])

    ratio = (dp[2021] / acc[2021]).rename("usage_ratio")  # usage intensity of the stock
    d_acc = (acc[2024] - acc[2021]).rename("d_acc")
    w = acc["pop"]

    r, n = fx.weighted_corr(ratio, d_acc, w)
    gates = [
        fx.gate_variant("digital_payment", INDICATORS["digital_payment"]["headline"]),
        fx.gate_coverage(fx.pan_dev, INDICATORS["digital_payment"]["headline"], 2021),
        fx.gate_jackknife(ratio, d_acc, w),
    ]

    both = ratio.to_frame().join(d_acc).join(w).dropna()
    both["tercile"] = both["usage_ratio"].rank(pct=True).apply(
        lambda p: "high" if p > 2 / 3 else ("mid" if p > 1 / 3 else "low"))
    terciles = {
        t: round(float((both[both.tercile == t]["d_acc"] * both[both.tercile == t]["pop"]).sum()
                       / both[both.tercile == t]["pop"].sum()), 1)
        for t in ["low", "mid", "high"]}

    print(f"weighted r(usage_ratio_2021, d_acc) = {r:.3f}  (n={n})")
    print("weighted mean d_acc by usage-ratio tercile:", terciles)
    for g in gates:
        print(g)


if __name__ == "__main__":
    run(Findex())
