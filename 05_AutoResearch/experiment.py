"""E18 (pre-registered): did the 2021->2024 formal-saving surge displace BORROWING as an
emergency-funds source? Weighted corr of delta(fin24bor) vs delta(saved_formally) 2021->2024,
dev panel, pop-weighted. Mirror of E7 (which found savings became a bigger source, r=0.541);
this tests WHICH source gave way.

Declared caveat (pre-registered, not controlled): emergency-fund composition shares are roughly
complementary, so some source must fall on average where savings rises -- the empirical content
is whether BORROWING SPECIFICALLY is the displaced source. The other composition sources
(fin24fam, fin24sell, fin24work) are reported descriptively for context. Descriptive only.
"""
import pandas as pd

from harness import Findex, INDICATORS


def _corr_vs_saving(fx: Findex, name: str, col: str, tag: str, sav_col: str):
    wide_x = fx.country_panel(fx.pan_dev, col, [2021, 2024])
    wide_s = fx.country_panel(fx.pan_dev, sav_col, [2021, 2024])
    dx = (wide_x[2024] - wide_x[2021]).rename(f"d_{tag}")
    ds = (wide_s[2024] - wide_s[2021]).rename("d_sav")
    w = wide_x["pop"]
    common = dx.dropna().index.intersection(ds.dropna().index).intersection(w.dropna().index)
    r, n = fx.weighted_corr(dx.reindex(common), ds.reindex(common), w.reindex(common))
    gjack = fx.gate_jackknife(dx.reindex(common), ds.reindex(common), w.reindex(common))
    ret = (gjack["r_droptop"] / gjack["r_full"]) if gjack.get("r_full") else float("nan")
    print(f"E18 {tag:10s}: r(d_{tag}, d_saving) = {r:+.3f} (n={n})  "
          f"jack {gjack['r_full']:+.3f}->{gjack['r_droptop']:+.3f} (retention {ret:.2f})")
    return r, common, dx, ds, w


def run(fx: Findex):
    sav_col = INDICATORS["saved_formally"]["headline"]
    print("E18 G3:", fx.gate_variant("saved_formally", sav_col),
          "| fin24bor: emergency-fund composition indicator, no variant choice -> declared n/a")
    print("E18 G4:", fx.gate_coverage(fx.pan_dev, "fin24bor", 2024,
                                      min_countries=30, min_pop_share=0.3))
    print()

    # Primary pre-registered test: borrowing vs saving surge.
    r_bor, common, d_bor, d_sav, w = _corr_vs_saving(fx, "fin24bor", "fin24bor", "borrow", sav_col)

    # Descriptive context: the other displaceable sources.
    for col, tag in [("fin24fam", "family"), ("fin24sell", "sell"), ("fin24work", "work")]:
        _corr_vs_saving(fx, col, col, tag, sav_col)

    print()
    # Terciles of delta-saving vs mean delta-borrow (dose-response on the primary test).
    dfx = pd.DataFrame({"d_sav": d_sav.reindex(common), "d_bor": d_bor.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_sav"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_bor"] * g["pop"]).sum() / g["pop"].sum()
        sm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E18 d_saving tercile {t:4s} (mean d_sav {sm:+5.1f}pp): "
              f"mean d_borrow = {wm:+.1f}pp  (n={len(g)})")
    print()
    print(f"E18 keep condition: r(d_borrow, d_saving) <= -0.30 AND jackknife sign-stable + "
          f"magnitude-retaining (r_droptop >= 0.5 x r_full)")


if __name__ == "__main__":
    run(Findex())
