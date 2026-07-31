"""E26 (pre-registered): do the digitalization rails reach the WELFARE margin, or do they stop at
the balance sheet?

E25 extended the three-rail structure from one destination to two: the rails feed the 2021-24
formal-saving surge (E10/E12/E23/E24) AND the formal-borrowing deepening (E25: wage rail +0.605,
+0.419 net of saving). Both are BALANCE-SHEET margins -- where money is stored, where credit came
from. No rail has ever been pointed at the WELFARE margin, self-reported ability to raise emergency
funds (fin24aSD_ND). Two prior discards frame the question without answering it: E2 tested
d_resilience against the MOBILE-MONEY rail (r = 0.189, G6 collapse to -0.005), E15 against the
formal-saving surge itself (discard). The strongest and most jackknife-stable rail -- wage
digitalization, the three-time leader of E10/E24/E25 -- has never been tested against resilience.

Primary   : weighted corr of d(fin32_acc) with d(fin24aSD_ND), 2021->2024, dev panel.
            Keep if |r| >= 0.30 and G6 sign-stable with retention >= 0.5 (E4 judgment rule).
Secondary A: weighted PARTIAL corr of d_wage with d_res controlling d(fin17a_17a1_d) -- the same
            net-of-saving step E25 ran for borrowing.
Secondary B: the other two rails (d_g20, d_mm) against d_res, on their own samples and on the
            three-rail common sample, so the rails rank against resilience exactly as E24 ranked
            them against saving and E25 against borrowing. E2's mobile-money result is re-run here
            as a declared REPLICATION on the current sample, not as a fresh hypothesis.

Declared: contemporaneous delta-on-delta co-movement is descriptive, never causal; fin24aSD_ND is a
SELF-REPORTED hypothetical-shock measure and carries the paper's standing 2021-vs-2024 framing
caveat; the resilience aggregate is flat in this window (dev panel 54.7 -> 54.5pp), which compresses
d variance and works AGAINST finding any association; sample composition differs across the rails
(E23/E24/E25), so every benchmark is recomputed on each common sample.
"""
import numpy as np
import pandas as pd

from harness import Findex, INDICATORS

YEARS = [2021, 2024]


def _wresid(y, X, w):
    """Residuals of a pop-weighted least-squares fit of y on X (constant + one or more columns).
    Same construction as E23/E24/E25."""
    X = pd.DataFrame(X)
    A = np.column_stack([np.ones(len(X)), X.to_numpy(dtype=float)])
    yv = np.asarray(y, dtype=float)
    sw = np.sqrt(np.asarray(w, dtype=float))
    beta, *_ = np.linalg.lstsq(A * sw[:, None], yv * sw, rcond=None)
    return pd.Series(yv - A @ beta, index=X.index)


def _deltas(fx: Findex, cols):
    """Wide 2021->2024 deltas (pp) for each requested column, plus pop weights."""
    out = {}
    pop = None
    for name, col in cols.items():
        t = fx.country_panel(fx.pan_dev, col, YEARS)
        out[name] = (t[2024] - t[2021]).rename(name)
        pop = t["pop"] if pop is None else pop.fillna(t["pop"])
    return out, pop


def _bivariate(df, fx, a, b, label, jack=True):
    r, n = fx.weighted_corr(df[a], df[b], df["pop"])
    line = f"E26 r({a}, {b}) = {r:+.3f}  (n={n})   [{label}]"
    if not jack:
        print(line)
        return {"r": r, "n": n}
    gj = fx.gate_jackknife(df[a], df[b], df["pop"])
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(line)
    print(f"E26   G6: {gj}  retention={ret:+.2f}")
    return {"r": r, "n": n, "sign_ok": bool(gj["ok"]), "ret": ret, "r_jack": gj["r_droptop"]}


def _partial(df, focus, ctrls, target, label, fx, jack=True):
    """Weighted partial corr of `focus` with `target` given the control column list `ctrls`."""
    w = df["pop"]
    ry = _wresid(df[target], df[ctrls], w)
    rx = _wresid(df[focus], df[ctrls], w)
    r, n = fx.weighted_corr(rx, ry, w)
    print(f"E26 partial r({focus}, {target} | {'+'.join(ctrls)}) = {r:+.3f}  (n={n})   [{label}]")
    if not jack:
        return {"r": r, "n": n}
    gj = fx.gate_jackknife(rx, ry, w)
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(f"E26   G6 on the residual pair: {gj}  retention={ret:+.2f}")
    return {"r": r, "n": n, "sign_ok": bool(gj["ok"]), "ret": ret, "r_jack": gj["r_droptop"]}


def run(fx: Findex):
    res = INDICATORS["resilience"]["headline"]          # fin24aSD_ND
    sav = INDICATORS["saved_formally"]["headline"]      # fin17a_17a1_d
    bor = INDICATORS["borrowed_formally"]["headline"]   # fin22a_22a1_22g_d
    g20 = INDICATORS["digital_payment"]["headline"]     # g20_any
    mm = INDICATORS["mobile_money"]["headline"]         # mobileaccount_t_d
    wage = "fin32_acc"                                  # E10/E24/E25's wage-digitalization column

    print("E26 G3:", fx.gate_variant("resilience", res), fx.gate_variant("saved_formally", sav),
          fx.gate_variant("borrowed_formally", bor), fx.gate_variant("digital_payment", g20),
          fx.gate_variant("mobile_money", mm))
    print("E26 G3 note: fin32_acc has no variant choice (E10 precedent)")
    print("E26 G5: n/a -- no official delta-correlation series exists")

    # Context: the flat aggregate the primary is being run against (already published, not a peek).
    agg = fx.series(fx.pan_dev, res, YEARS)
    print(f"E26 context -- dev-panel resilience aggregate: {agg[2021]:.1f} -> {agg[2024]:.1f}pp "
          f"(flat; compresses d variance, works against the hypothesis)\n")

    d, pop = _deltas(fx, {"d_wage": wage, "d_res": res, "d_sav": sav, "d_bor": bor,
                          "d_g20": g20, "d_mm": mm})
    base = pd.DataFrame({**d, "pop": pop})

    # ---------- PRIMARY: d_wage ~ d_resilience --------------------------------------------------
    main = base[["d_wage", "d_res", "d_sav", "pop"]].dropna()
    print("E26 G4 (primary estimation sample):",
          fx.gate_coverage(fx.pan_dev[fx.pan_dev["countrynewwb"].isin(main.index)], res, 2024,
                           min_countries=30, min_pop_share=0.3))
    print(f"E26 primary sample n={len(main)}  (E25's borrowing primary ran on n=71 -- same frame)\n")
    prim = _bivariate(main, fx, "d_wage", "d_res", "PRIMARY: wage rail -> resilience")
    print(f"E26   d_res spread on this sample: sd={main['d_res'].std():.2f}pp, "
          f"d_sav sd={main['d_sav'].std():.2f}pp, d_wage sd={main['d_wage'].std():.2f}pp")
    print()
    _bivariate(main, fx, "d_sav", "d_res", "E15 replication (saving surge -> resilience)", jack=False)
    _bivariate(main, fx, "d_wage", "d_sav", "E10 logged r=+0.791 (n=71), on this sample", jack=False)

    # ---------- SECONDARY A: net of the saving channel -------------------------------------------
    print()
    sec = _partial(main, "d_wage", ["d_sav"], "d_res",
                   "SECONDARY A: wage rail -> resilience NET of the saving channel", fx)

    # ---------- SECONDARY B: the other two rails --------------------------------------------------
    print("\nE26 secondary B -- each rail against resilience on its OWN maximal sample:")
    for rail in ["d_g20", "d_mm"]:
        sub = base[[rail, "d_res", "pop"]].dropna()
        lab = f"own sample n={len(sub)}"
        if rail == "d_mm":
            lab += "  [E2 REPLICATION: logged r=+0.189, G6 -0.005]"
        _bivariate(sub, fx, rail, "d_res", lab, jack=False)

    common = base[["d_wage", "d_res", "d_sav", "d_bor", "d_g20", "d_mm", "pop"]].dropna()
    print(f"\nE26 secondary B -- three-rail COMMON sample (n={len(common)}), ranking against "
          "resilience (cf. E24 vs saving, E25 vs borrowing):")
    for rail in ["d_wage", "d_g20", "d_mm"]:
        _bivariate(common, fx, rail, "d_res", "common sample", jack=False)
    print("E26 the three destinations on this IDENTICAL sample "
          "(saving / borrowing / resilience per rail):")
    for rail in ["d_wage", "d_g20", "d_mm"]:
        rs = {dest: fx.weighted_corr(common[rail], common[dest], common["pop"])[0]
              for dest in ["d_sav", "d_bor", "d_res"]}
        print(f"E26   {rail:7s} -> saving {rs['d_sav']:+.3f} | borrowing {rs['d_bor']:+.3f} | "
              f"resilience {rs['d_res']:+.3f}")

    ok = (abs(prim["r"]) >= 0.30) and prim["sign_ok"] and (prim["ret"] >= 0.50)
    print("\nE26 keep condition: primary |r| >= 0.30 AND G6 sign-stable AND retention >= 0.50")
    print(f"E26   observed primary r={prim['r']:+.3f}  jack={prim['r_jack']:+.3f} "
          f"ret={prim['ret']:+.2f}  -> passes: {ok}")
    print(f"E26   [context] partial net of saving = {sec['r']:+.3f} (n={sec['n']}, "
          f"ret={sec['ret']:+.2f})")


if __name__ == "__main__":
    run(Findex())
