"""E19 (pre-registered): did the 2021->2024 formal-saving surge show up as account ACTIVATION?
Weighted corr of delta(inactive_t_d) vs delta(saved_formally) 2021->2024, dev panel,
pop-weighted. Hypothesis: where formal saving surged, account inactivity FELL (idle accounts
put to use) -> NEGATIVE correlation.

Motivation: E16 (DISCARD) found delta(account) is orthogonal to delta(saving) at the pop-weighted
level -- the surge is a depth phenomenon not reducible to raw account expansion, sharpest OUTSIDE
the big account-growth economies. If the surge rides on EXISTING accounts, it should manifest as
dormant accounts being used to save (falling inactive_t_d where saving rose). Distinct from E4
(inactivity as a lagged consequence of past account drives); this is delta-inactive vs
delta-saving co-movement, never run before.

Declared caveat (pre-registered, not controlled): account growth and common income shocks plausibly
drive both sides; a mechanical link (saving requires an active account) is possible but not
tautological -- inactivity is measured over all accountholders, most of whom do not save formally.
Descriptive only.
"""
import pandas as pd

from harness import Findex, INDICATORS


def run(fx: Findex):
    inact_col = INDICATORS["inactive"]["headline"]      # inactive_t_d
    sav_col = INDICATORS["saved_formally"]["headline"]  # fin17a_17a1_d
    print("E19 G3:", fx.gate_variant("inactive", inact_col))
    print("E19 G3:", fx.gate_variant("saved_formally", sav_col))
    print("E19 G4:", fx.gate_coverage(fx.pan_dev, inact_col, 2024,
                                      min_countries=30, min_pop_share=0.3))
    print()

    wide_i = fx.country_panel(fx.pan_dev, inact_col, [2021, 2024])
    wide_s = fx.country_panel(fx.pan_dev, sav_col, [2021, 2024])
    d_inact = (wide_i[2024] - wide_i[2021]).rename("d_inact")
    d_sav = (wide_s[2024] - wide_s[2021]).rename("d_sav")
    w = wide_i["pop"]
    common = (d_inact.dropna().index
              .intersection(d_sav.dropna().index)
              .intersection(w.dropna().index))

    r, n = fx.weighted_corr(d_inact.reindex(common), d_sav.reindex(common), w.reindex(common))
    gjack = fx.gate_jackknife(d_inact.reindex(common), d_sav.reindex(common), w.reindex(common))
    ret = (gjack["r_droptop"] / gjack["r_full"]) if gjack.get("r_full") else float("nan")
    print(f"E19 r(d_inactive, d_saving) = {r:+.3f} (n={n})  "
          f"jack {gjack['r_full']:+.3f}->{gjack['r_droptop']:+.3f} (retention {ret:.2f})")
    print()

    # Terciles of delta-saving vs mean delta-inactive (dose-response).
    dfx = pd.DataFrame({"d_sav": d_sav.reindex(common), "d_inact": d_inact.reindex(common),
                        "pop": w.reindex(common)}).dropna()
    dfx["ter"] = pd.qcut(dfx["d_sav"], 3, labels=["low", "mid", "high"])
    for t, g in dfx.groupby("ter", observed=True):
        wm = (g["d_inact"] * g["pop"]).sum() / g["pop"].sum()
        sm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E19 d_saving tercile {t:4s} (mean d_sav {sm:+5.1f}pp): "
              f"mean d_inactive = {wm:+.1f}pp  (n={len(g)})")
    print()
    print("E19 keep condition: r(d_inactive, d_saving) <= -0.30 AND jackknife sign-stable + "
          "magnitude-retaining (r_droptop >= 0.5 x r_full)")


if __name__ == "__main__":
    run(Findex())
