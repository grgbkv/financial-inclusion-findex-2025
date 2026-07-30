"""E25 (pre-registered): are the three digitalization rails SAVING-SPECIFIC, or do they also feed
the other deepening margin — formal BORROWING?

The three-rail structure (mobile money E1/E22, digital payments E12/E23, wage digitalization
E10/E24) was built entirely around one destination: the 2021-24 formal-saving surge. E11 logged the
other deepening margin (d_borrow ~ d_sav, r = +0.403, n = 76) but no rail has ever been pointed at
borrowing. P20 supplied the prediction-side hint: formal-borrowing LEVELS mis-partition the saving
panel, i.e. credit may sit on a different axis from the digitalization cuts.

Primary   : weighted corr of d(fin32_acc) with d(fin22a_22a1_22g_d), 2021->2024, dev panel.
            Keep if |r| >= 0.30 and G6 sign-stable with retention >= 0.5 (E4 judgment rule).
Secondary A: destination specificity -- weighted PARTIAL corr of d_wage with d_borrow controlling
            d(fin17a_17a1_d) (formal saving). E5b/E23/E24 construction: pop-weighted LS
            residualization, weighted_corr of residuals, gate_jackknife on the residual pair.
Secondary B: the other two rails (d_g20, d_mm) against d_borrow, on their own samples and on the
            three-rail common sample, so the rails can be ranked against borrowing exactly as E24
            ranked them against saving; E11's d_borrow ~ d_sav benchmark recomputed on each sample.

Declared: contemporaneous delta-on-delta co-movement is descriptive, never causal; the borrowing
headline mixes formal-institution and credit-card borrowing; sample composition differs across the
rails (E23/E24 showed this moves the bivariates a lot), so every benchmark is recomputed on each
common sample. Descriptive association only.
"""
import numpy as np
import pandas as pd

from harness import Findex, INDICATORS

YEARS = [2021, 2024]


def _wresid(y, X, w):
    """Residuals of a pop-weighted least-squares fit of y on X (constant + one or more columns).
    Same construction as E24 (which reproduces E23's single-regressor arithmetic exactly)."""
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
    line = f"E25 r({a}, {b}) = {r:+.3f}  (n={n})   [{label}]"
    if not jack:
        print(line)
        return {"r": r, "n": n}
    gj = fx.gate_jackknife(df[a], df[b], df["pop"])
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(line)
    print(f"E25   G6: {gj}  retention={ret:+.2f}")
    return {"r": r, "n": n, "sign_ok": bool(gj["ok"]), "ret": ret, "r_jack": gj["r_droptop"]}


def _partial(df, focus, ctrls, target, label, fx, jack=True):
    """Weighted partial corr of `focus` with `target` given the control column list `ctrls`."""
    w = df["pop"]
    ry = _wresid(df[target], df[ctrls], w)
    rx = _wresid(df[focus], df[ctrls], w)
    r, n = fx.weighted_corr(rx, ry, w)
    print(f"E25 partial r({focus}, {target} | {'+'.join(ctrls)}) = {r:+.3f}  (n={n})   [{label}]")
    if not jack:
        return {"r": r, "n": n}
    gj = fx.gate_jackknife(rx, ry, w)
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(f"E25   G6 on the residual pair: {gj}  retention={ret:+.2f}")
    return {"r": r, "n": n, "sign_ok": bool(gj["ok"]), "ret": ret, "r_jack": gj["r_droptop"]}


def run(fx: Findex):
    bor = INDICATORS["borrowed_formally"]["headline"]   # fin22a_22a1_22g_d
    sav = INDICATORS["saved_formally"]["headline"]      # fin17a_17a1_d
    g20 = INDICATORS["digital_payment"]["headline"]     # g20_any
    mm = INDICATORS["mobile_money"]["headline"]         # mobileaccount_t_d
    wage = "fin32_acc"                                  # E10/E24's wage-digitalization column

    print("E25 G3:", fx.gate_variant("borrowed_formally", bor),
          fx.gate_variant("saved_formally", sav), fx.gate_variant("digital_payment", g20),
          fx.gate_variant("mobile_money", mm))
    print("E25 G3 note: fin32_acc has no variant choice (E10 precedent)")
    print("E25 G5: n/a -- no official delta-correlation series exists\n")

    d, pop = _deltas(fx, {"d_wage": wage, "d_bor": bor, "d_sav": sav, "d_g20": g20, "d_mm": mm})
    base = pd.DataFrame({**d, "pop": pop})

    # ---------- PRIMARY: d_wage ~ d_borrow ------------------------------------------------------
    main = base[["d_wage", "d_bor", "d_sav", "pop"]].dropna()
    print("E25 G4 (primary estimation sample):",
          fx.gate_coverage(fx.pan_dev[fx.pan_dev["countrynewwb"].isin(main.index)], bor, 2024,
                           min_countries=30, min_pop_share=0.3))
    print(f"E25 primary sample n={len(main)}\n")
    res = _bivariate(main, fx, "d_wage", "d_bor", "PRIMARY: wage rail -> borrowing")
    print()
    _bivariate(main, fx, "d_sav", "d_bor", "E11 logged r=+0.403 (n=76), on this sample", jack=False)
    _bivariate(main, fx, "d_wage", "d_sav", "E10 logged r=+0.791 (n=71), on this sample", jack=False)

    # ---------- SECONDARY A: destination specificity ---------------------------------------------
    print()
    sec = _partial(main, "d_wage", ["d_sav"], "d_bor",
                   "SECONDARY A: wage rail -> borrowing NET of the saving channel", fx)

    # ---------- SECONDARY B: the other two rails -------------------------------------------------
    print("\nE25 secondary B -- each rail against borrowing on its OWN maximal sample:")
    for rail in ["d_g20", "d_mm"]:
        sub = base[[rail, "d_bor", "pop"]].dropna()
        _bivariate(sub, fx, rail, "d_bor", f"own sample n={len(sub)}", jack=False)

    common = base[["d_wage", "d_bor", "d_sav", "d_g20", "d_mm", "pop"]].dropna()
    print(f"\nE25 secondary B -- three-rail COMMON sample (n={len(common)}), "
          "ranking against borrowing (cf. E24's ranking against saving):")
    for rail in ["d_wage", "d_g20", "d_mm"]:
        _bivariate(common, fx, rail, "d_bor", "common sample", jack=False)
    _bivariate(common, fx, "d_sav", "d_bor", "E11 benchmark on the common sample", jack=False)
    print("E25 context -- the same rails against SAVING on this identical sample (E24 replication):")
    for rail in ["d_wage", "d_g20", "d_mm"]:
        _bivariate(common, fx, rail, "d_sav", "common sample", jack=False)

    ok = (abs(res["r"]) >= 0.30) and res["sign_ok"] and (res["ret"] >= 0.50)
    print("\nE25 keep condition: primary |r| >= 0.30 AND G6 sign-stable AND retention >= 0.50")
    print(f"E25   observed primary r={res['r']:+.3f}  jack={res['r_jack']:+.3f} "
          f"ret={res['ret']:+.2f}  -> passes: {ok}")
    print(f"E25   [context] partial net of saving = {sec['r']:+.3f} (n={sec['n']}, "
          f"ret={sec['ret']:+.2f})")


if __name__ == "__main__":
    run(Findex())
