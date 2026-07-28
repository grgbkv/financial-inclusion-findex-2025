"""E24 (pre-registered): is WAGE DIGITALIZATION a third separate rail into the saving surge, or
the account-usage face of the digital-payment channel?

E23 closed the one-FACTOR alternative for mobile money (partial r = +0.509 controlling d_g20, with
the symmetric reverse at +0.574) and left the same design available for E10. E10's bivariate
(d_fin32_acc ~ d_saving, r = +0.791, n = 71) is the STRONGEST single co-movement in the ledger and
also the most plausibly redundant one: wages paid into accounts is mechanically an account-usage
indicator, so it may be measuring the same thing as g20_any.

Primary   : weighted PARTIAL corr of d(fin32_acc) with d(fin17a_17a1_d), 2021->2024, controlling
            d(g20_any). E5b/E23 construction: pop-weighted LS residualization, weighted_corr of
            residuals, gate_jackknife on the residual pair. Keep if r >= +0.30 and G6 sign-stable
            with retention >= 0.5.
Secondary A: the NEW design step -- TWO controls at once, d(g20_any) AND d(mobileaccount_t_d), via
            multivariate pop-weighted LS residualization (mobile money binds the sample). No rail
            in the ledger has yet been asked to survive two simultaneous controls. Descriptive.
Secondary B: symmetric reverse partial (d_g20 ~ d_sav | d_wage), plus every bivariate benchmark
            recomputed on each common sample -- E23 showed sample composition moves these a lot.

Declared: partialling a CONTEMPORANEOUS delta decomposes co-movement, it does not control
confounding -- every control is an outcome of the same 2021-24 period. Account growth and common
income shocks uncontrolled. fin32_acc is an employer-side attribute of wage payment, not an
individual choice (U14's caveat at country level). Descriptive association only, never causal.
"""
import numpy as np
import pandas as pd

from harness import Findex, INDICATORS

YEARS = [2021, 2024]


def _wresid(y, X, w):
    """Residuals of a pop-weighted least-squares fit of y on X (constant + one or more columns).

    Generalizes E5b/E23's single-regressor residualization: with one column it reproduces the
    E23 arithmetic exactly (verified in-run against the E23 logged numbers)."""
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


def _partial(df, focus, ctrls, label, fx, jack=True):
    """Weighted partial corr of `focus` with d_sav given the control column list `ctrls`."""
    w = df["pop"]
    ry = _wresid(df["d_sav"], df[ctrls], w)
    rx = _wresid(df[focus], df[ctrls], w)
    r, n = fx.weighted_corr(rx, ry, w)
    print(f"E24 partial r({focus}, d_sav | {'+'.join(ctrls)}) = {r:+.3f}  (n={n})   [{label}]")
    if not jack:
        return {"r": r, "n": n}
    gj = fx.gate_jackknife(rx, ry, w)
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(f"E24   G6 on the residual pair: {gj}  retention={ret:+.2f}")
    return {"r": r, "n": n, "sign_ok": bool(gj["ok"]), "ret": ret, "r_jack": gj["r_droptop"]}


def _bivariates(df, fx, pairs, tag):
    print(f"E24 bivariate benchmarks on the {tag} common sample (n={len(df)}):")
    for a, b, note in pairs:
        r, n = fx.weighted_corr(df[a], df[b], df["pop"])
        print(f"E24   r({a}, {b}) = {r:+.3f}  (n={n})   [{note}]")


def run(fx: Findex):
    sav = INDICATORS["saved_formally"]["headline"]    # fin17a_17a1_d
    g20 = INDICATORS["digital_payment"]["headline"]   # g20_any
    mm = INDICATORS["mobile_money"]["headline"]       # mobileaccount_t_d
    wage = "fin32_acc"                                # E10's wage-digitalization column

    print("E24 G3:", fx.gate_variant("saved_formally", sav), fx.gate_variant("digital_payment", g20),
          fx.gate_variant("mobile_money", mm))
    print("E24 G3 note: fin32_acc has no variant choice (E10 precedent)")
    print("E24 G5: n/a -- no official partial-correlation series exists\n")

    d, pop = _deltas(fx, {"d_wage": wage, "d_sav": sav, "d_g20": g20, "d_mm": mm})
    base = pd.DataFrame({**d, "pop": pop})

    # ---------- PRIMARY: single control d_g20 (full dev-panel coverage, keeps E10's sample) -----
    main = base[["d_wage", "d_sav", "d_g20", "pop"]].dropna()
    print("E24 G4 (primary estimation sample):",
          fx.gate_coverage(fx.pan_dev[fx.pan_dev["countrynewwb"].isin(main.index)], wage, 2024,
                           min_countries=30, min_pop_share=0.3))
    _bivariates(main, fx, [("d_wage", "d_sav", "E10 logged r=+0.791 (n=71)"),
                           ("d_g20", "d_sav", "E12 logged r=+0.370 (n=76)"),
                           ("d_wage", "d_g20", "control-focus collinearity")], "PRIMARY")
    print()
    res = _partial(main, "d_wage", ["d_g20"], "PRIMARY", fx)
    print()
    rev = _partial(main, "d_g20", ["d_wage"], "secondary B: symmetric reverse, descriptive", fx)

    # ---------- SECONDARY A: TWO controls at once (d_g20 + d_mm) --------------------------------
    print()
    both = base[["d_wage", "d_sav", "d_g20", "d_mm", "pop"]].dropna()
    print("E24 G4 (two-control sample):",
          fx.gate_coverage(fx.pan_dev[fx.pan_dev["countrynewwb"].isin(both.index)], mm, 2024,
                           min_countries=30, min_pop_share=0.3))
    _bivariates(both, fx, [("d_wage", "d_sav", "E10 on this subsample"),
                           ("d_mm", "d_sav", "E1 logged r=+0.719 (n=58)"),
                           ("d_g20", "d_sav", "E12; E23 got +0.751 on its n=58")], "TWO-CONTROL")
    print()
    two = _partial(both, "d_wage", ["d_g20", "d_mm"], "SECONDARY A: two controls at once", fx)
    print()
    # each rail against the other two, same sample -- the full three-way decomposition
    for focus, ctrls in [("d_mm", ["d_g20", "d_wage"]), ("d_g20", ["d_mm", "d_wage"])]:
        _partial(both, focus, ctrls, "secondary A context, descriptive", fx, jack=False)

    ok = (res["r"] >= 0.30) and res["sign_ok"] and (res["ret"] >= 0.50)
    print("\nE24 keep condition: primary partial r >= +0.30 (E10's positive sign) AND G6 "
          "sign-stable AND retention >= 0.50")
    print(f"E24   observed primary r={res['r']:+.3f}  jack={res['r_jack']:+.3f} "
          f"ret={res['ret']:+.2f}  -> passes: {ok}")
    print(f"E24   [context] reverse partial (d_g20 | d_wage) = {rev['r']:+.3f}; "
          f"two-control partial (d_wage | d_g20+d_mm) = {two['r']:+.3f} (n={two['n']}, "
          f"ret={two['ret']:+.2f})")


if __name__ == "__main__":
    run(Findex())
