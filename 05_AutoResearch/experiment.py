"""E23 (pre-registered): is E1 a SEPARATE RAIL into the saving surge, or the SSA-flavoured face
of one common digitalization factor?

Every country-level association in the ledger is bivariate, and the digitalization indicators are
demonstrably collinear: d_mm ~ d_saving r = +0.719 (E1), d_g20 ~ d_saving r = +0.370 (E12),
d_fin32_acc ~ d_saving r = +0.791 (E10), d_mm ~ d_g20 r = +0.600 (E14). E22 closed the
one-REGION alternative to E1; E23 tests the one-FACTOR alternative.

Test: weighted PARTIAL correlation of d(mobileaccount_t_d) with d(fin17a_17a1_d), 2021->2024,
controlling d(g20_any), on the developing balanced panel. Construction follows E5b: pop-weighted
least-squares residualization of both variables on the control, then weighted_corr of the
residuals; gate_jackknife on the residual pair.

Keep if partial r >= +0.30, same positive sign as E1, and G6 sign-stable with retention >= 0.5.
Registered alternative outcome: a collapse below 0.30 means E1 and E12 are two readings of one
digitalization factor, and E1 is re-logged with that caveat.

Declared: partialling a CONTEMPORANEOUS delta is not a control for confounding -- d_g20 is itself
an outcome of the same period, so this decomposes co-movement, it does not identify anything.
Descriptive association only, never causal.
"""
import pandas as pd

from harness import Findex, INDICATORS

YEARS = [2021, 2024]


def _wresid(y, x, w):
    """Residuals of a pop-weighted least-squares fit of y on x (E5b construction)."""
    xm = (x * w).sum() / w.sum()
    ym = (y * w).sum() / w.sum()
    b = (w * (x - xm) * (y - ym)).sum() / (w * (x - xm) ** 2).sum()
    return y - (ym - b * xm) - b * x


def _deltas(fx: Findex, cols):
    """Wide 2021->2024 deltas (pp) for each requested column, plus pop weights."""
    out = {}
    pop = None
    for name, col in cols.items():
        t = fx.country_panel(fx.pan_dev, col, YEARS)
        out[name] = (t[2024] - t[2021]).rename(name)
        if pop is None:
            pop = t["pop"]
        else:
            pop = pop.fillna(t["pop"])
    return out, pop


def _partial(df, focus, ctrl, label, jack=True, fx=None):
    """Weighted partial corr of `focus` with d_sav given `ctrl`, on the frame's common sample."""
    w = df["pop"]
    ry = _wresid(df["d_sav"], df[ctrl], w)
    rx = _wresid(df[focus], df[ctrl], w)
    r, n = fx.weighted_corr(rx, ry, w)
    print(f"E23 partial r({focus}, d_sav | {ctrl}) = {r:+.3f}  (n={n} economies)   [{label}]")
    if not jack:
        return {"r": r, "n": n}
    gj = fx.gate_jackknife(rx, ry, w)
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(f"E23   G6 on the residual pair: {gj}  retention={ret:+.2f}")
    return {"r": r, "n": n, "sign_ok": bool(gj["ok"]), "ret": ret, "r_jack": gj["r_droptop"]}


def run(fx: Findex):
    mm = INDICATORS["mobile_money"]["headline"]      # mobileaccount_t_d
    sav = INDICATORS["saved_formally"]["headline"]   # fin17a_17a1_d
    g20 = INDICATORS["digital_payment"]["headline"]  # g20_any
    wage = "fin32_acc"                               # E10's wage-digitalization column

    print("E23 G3:", fx.gate_variant("mobile_money", mm), fx.gate_variant("saved_formally", sav),
          fx.gate_variant("digital_payment", g20))
    print("E23 G3 note: fin32_acc has no variant choice (E10 precedent)")
    print("E23 G5: n/a -- no official partial-correlation series exists\n")

    d, pop = _deltas(fx, {"d_mm": mm, "d_sav": sav, "d_g20": g20, "d_wage": wage})
    base = pd.DataFrame({**d, "pop": pop})

    # ---- primary: control = d_g20 (full dev-panel coverage, keeps E1's estimation sample) ----
    main = base[["d_mm", "d_sav", "d_g20", "pop"]].dropna()
    print("E23 G4 (primary estimation sample):",
          fx.gate_coverage(fx.pan_dev[fx.pan_dev["countrynewwb"].isin(main.index)], mm, 2024,
                           min_countries=30, min_pop_share=0.3))
    print(f"E23 primary sample: n={len(main)} economies\n")

    print("E23 bivariate benchmarks recomputed on the SAME common sample:")
    for a, b, tag in [("d_mm", "d_sav", "E1 logged r=+0.719"),
                      ("d_g20", "d_sav", "E12 logged r=+0.370"),
                      ("d_mm", "d_g20", "E14 logged r=+0.600")]:
        r, n = fx.weighted_corr(main[a], main[b], main["pop"])
        print(f"E23   r({a}, {b}) = {r:+.3f}  (n={n})   [{tag}]")
    print()

    res = _partial(main, "d_mm", "d_g20", "PRIMARY", fx=fx)
    print()
    rev = _partial(main, "d_g20", "d_mm", "symmetric reverse, descriptive", fx=fx)

    # ---- secondary: control = d_wage (E10's strongest bivariate competitor, smaller sample) ----
    print()
    alt = base[["d_mm", "d_sav", "d_wage", "pop"]].dropna()
    print(f"E23 secondary sample (wage-digitalization control): n={len(alt)} economies")
    sec = _partial(alt, "d_mm", "d_wage", "secondary, descriptive", jack=False, fx=fx)

    ok = (res["r"] >= 0.30) and res["sign_ok"] and (res["ret"] >= 0.50)
    print("\nE23 keep condition: partial r >= +0.30 (same positive sign as E1) AND G6 sign-stable "
          "AND retention >= 0.50")
    print(f"E23   observed partial r={res['r']:+.3f}  jack={res['r_jack']:+.3f} "
          f"ret={res['ret']:+.2f}  -> passes: {ok}")
    print(f"E23   [context] reverse partial (d_g20 | d_mm) = {rev['r']:+.3f}; "
          f"wage-control partial = {sec['r']:+.3f} (n={sec['n']})")


if __name__ == "__main__":
    run(Findex())
