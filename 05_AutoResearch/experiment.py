"""E22 (pre-registered): is E1 — the strongest kept country-level finding — a GENERAL
developing-world regularity, or a Sub-Saharan Africa story?

E1: the 2021->2024 formal-saving surge co-moves with mobile-money growth, weighted r = 0.719
(n = 58 dev-panel economies), G6-clean (0.72 -> 0.80 drop-top-5). Mobile money is heavily
SSA-concentrated, so an obvious alternative reading is that E1 describes one region and the
population weighting carries it. G6 guards against one-COUNTRY stories, not one-REGION stories.
This is the first regional-split test in the ledger (backlog: "regional heterogeneity of kept
findings E1/E5b/E7").

Test: partition the developing balanced panel into SSA vs the five other developing regions
pooled; run E1's identical construction inside each; report terciles for both.
Keep the GENERAL claim only if |r| >= 0.30 with the same positive sign in BOTH subsamples and G6
is sign-stable with magnitude retention >= 0.5 x r_full in both. If it holds only in SSA, the
general claim is discarded and E1 is re-logged as region-specific — registered in advance as the
informative outcome.

Declared: G4 is run per subsample with min_countries=15 (deviation from the default 30, forced by
SSA having only 26 dev-panel economies; the pooled E1 sample passed at the default). G6 uses the
standard drop_top=5, which at n ~ 20-35 is a stiffer test than for the full sample — noted, not
relaxed. Descriptive association only, never causal; account growth and common income shocks are
uncontrolled in both subsamples, exactly as in E1.
"""
import pandas as pd

from harness import Findex, INDICATORS

SSA = "Sub-Saharan Africa (excluding high income)"
YEARS = [2021, 2024]


def _subsample(fx: Findex, in_ssa: bool):
    d = fx.pan_dev
    return d[(d["regionwb24_hi"] == SSA) if in_ssa else (d["regionwb24_hi"] != SSA)]


def _run_one(fx: Findex, frame, label, mm, sav):
    print(f"--- E22 {label} " + "-" * (46 - len(label)))
    print("E22 G4:", fx.gate_coverage(frame, mm, 2024, min_countries=15, min_pop_share=0.3))

    m = fx.country_panel(frame, mm, YEARS)
    s = fx.country_panel(frame, sav, YEARS)
    d_mm = (m[2024] - m[2021]).rename("d_mm")
    d_sav = (s[2024] - s[2021]).rename("d_sav")
    w = m["pop"]
    common = (d_mm.dropna().index.intersection(d_sav.dropna().index)
              .intersection(w.dropna().index))
    x, y, pop = d_mm.reindex(common), d_sav.reindex(common), w.reindex(common)

    r, n = fx.weighted_corr(x, y, pop)
    gj = fx.gate_jackknife(x, y, pop)
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(f"E22 r(d_mobile_money, d_saving) = {r:+.3f}  (n={n} economies)")
    print(f"E22 G6: {gj}  retention={ret:+.2f}")

    df = pd.DataFrame({"d_mm": x, "d_sav": y, "pop": pop}).dropna()
    df["ter"] = pd.qcut(df["d_mm"], 3, labels=["low", "mid", "high"])
    for t, g in df.groupby("ter", observed=True):
        wm = (g["d_sav"] * g["pop"]).sum() / g["pop"].sum()
        mm_m = (g["d_mm"] * g["pop"]).sum() / g["pop"].sum()
        print(f"E22   d_mm tercile {t:4s} (mean d_mm {mm_m:+5.1f}pp): "
              f"mean d_saving = {wm:+5.1f}pp  (n={len(g)})")
    print()
    return {"label": label, "r": r, "n": n, "ret": ret,
            "sign_ok": bool(gj["ok"]), "r_jack": gj["r_droptop"]}


def run(fx: Findex):
    mm = INDICATORS["mobile_money"]["headline"]      # mobileaccount_t_d
    sav = INDICATORS["saved_formally"]["headline"]   # fin17a_17a1_d
    print("E22 G3:", fx.gate_variant("mobile_money", mm), fx.gate_variant("saved_formally", sav))
    print("E22 G5: n/a -- no official regional Delta-correlation series exists")
    print("E22 G4 declared deviation: min_countries=15 per subsample (SSA has 26 dev-panel "
          "economies); the pooled E1 sample passed G4 at the default 30\n")

    res = [_run_one(fx, _subsample(fx, True), "Sub-Saharan Africa", mm, sav),
           _run_one(fx, _subsample(fx, False), "rest of developing panel", mm, sav)]

    # full-sample replication of E1 for context (same construction, no split)
    full = _run_one(fx, fx.pan_dev, "FULL dev panel (E1 replication)", mm, sav)

    print("E22 keep condition: |r| >= 0.30, same positive sign, G6 sign-stable AND "
          "retention >= 0.50 -- in BOTH subsamples")
    for d in res:
        ok = (d["r"] >= 0.30) and d["sign_ok"] and (d["ret"] >= 0.50)
        print(f"E22   {d['label']:26s} r={d['r']:+.3f} n={d['n']:3d} "
              f"jack={d['r_jack']:+.3f} ret={d['ret']:+.2f}  -> passes: {ok}")
    print(f"E22   [context] {full['label']}: r={full['r']:+.3f} (E1 logged 0.719, n=58)")


if __name__ == "__main__":
    run(Findex())
