"""E27 (pre-registered): did the 2021-24 formal-saving surge CREATE savers, or RELABEL them?

Eleven experiments have traced where the surge came from (E1/E10/E12/E23/E24: three digitalization
rails) and where it went (E7 resilience composition, E11/E25 borrowing, E26 the balance-sheet
boundary). The accounting question underneath all of it has never been asked: the rails story reads
very differently if formal saving grew by pulling EXISTING informal savers across a mode boundary
(a composition shift inside an unchanged saving population) than if it grew on top of unchanged
informal saving (net new saving).

The country file carries the disjoint saving modes needed to separate the two:
  fin17c        -- saved using OTHER methods (the informal margin, 76 dev-panel countries)
  fin17b        -- saved via a savings club / person outside the family (semiformal, 58)
  save_any_t_d  -- saved any money (76), which NESTS the headline
against fin17a_17a1_d (saved at an FI or via mobile money), the E1/E10 headline.

Primary    : pop-weighted corr of d(fin17c) with d(fin17a_17a1_d), 2021->2024, dev panel.
             Registered direction: NEGATIVE (displacement). Keep if r <= -0.30 AND G6 sign-stable
             with retention >= 0.5. Opposite sign at |r| >= 0.30 = discard of the registered
             direction with the reverse reported (E5/E9/E17 precedent).
Secondary A: the same test on the semiformal margin d(fin17b).
Secondary B: dev-panel aggregates of all four columns at 2021 and 2024 -- the accounting.
Secondary C: pop-weighted LS slope of d(save_any_t_d) on d(fin17a_17a1_d). Slope ~1 = every point
             of formal saving is a point of NEW saving; ~0 = pure relabelling. Declared PARTLY
             MECHANICAL (formal is nested inside any-saving), so it is context, never the test.

Declared: contemporaneous delta-on-delta co-movement, descriptive only, never causal; fin17b/fin17c
are narrow variants with no headline status under G3 and are declared as such; sample composition
differs across comparators, so every correlation prints its own n and only the primary is gated.
"""
import numpy as np
import pandas as pd

from harness import Findex, INDICATORS

YEARS = [2021, 2024]


def _wslope(y, x, w):
    """Pop-weighted least-squares slope of y on x (with intercept)."""
    A = np.column_stack([np.ones(len(x)), np.asarray(x, dtype=float)])
    sw = np.sqrt(np.asarray(w, dtype=float))
    beta, *_ = np.linalg.lstsq(A * sw[:, None], np.asarray(y, dtype=float) * sw, rcond=None)
    return float(beta[1])


def _deltas(fx: Findex, cols):
    """Wide 2021->2024 deltas (pp) for each requested column, plus pop weights."""
    out, pop = {}, None
    for name, col in cols.items():
        t = fx.country_panel(fx.pan_dev, col, YEARS)
        out[name] = (t[2024] - t[2021]).rename(name)
        pop = t["pop"] if pop is None else pop.fillna(t["pop"])
    return out, pop


def _bivariate(df, fx, a, b, label, jack=True):
    r, n = fx.weighted_corr(df[a], df[b], df["pop"])
    print(f"E27 r({a}, {b}) = {r:+.3f}  (n={n})   [{label}]")
    if not jack:
        return {"r": r, "n": n}
    gj = fx.gate_jackknife(df[a], df[b], df["pop"])
    ret = (gj["r_droptop"] / gj["r_full"]) if gj.get("r_full") else float("nan")
    print(f"E27   G6: {gj}  retention={ret:+.2f}")
    return {"r": r, "n": n, "sign_ok": bool(gj["ok"]), "ret": ret, "r_jack": gj["r_droptop"]}


def run(fx: Findex):
    sav = INDICATORS["saved_formally"]["headline"]      # fin17a_17a1_d
    informal, semiformal, any_sav = "fin17c", "fin17b", "save_any_t_d"

    print("E27 G3:", fx.gate_variant("saved_formally", sav))
    print("E27 G3 note: fin17c (other-method saving), fin17b (savings club) and save_any_t_d have "
          "no headline/narrow variant choice in the registry -- declared as used")
    print("E27 G5: n/a -- no official delta-correlation series exists\n")

    # ---------- SECONDARY B: the accounting (levels first, so the deltas read in context) --------
    print("E27 secondary B -- dev-panel pop-weighted aggregates (pp):")
    aggs = {}
    for name, col in [("formal (fin17a_17a1_d)", sav), ("any saving (save_any_t_d)", any_sav),
                      ("other-method (fin17c)", informal), ("savings club (fin17b)", semiformal)]:
        s = fx.series(fx.pan_dev, col, YEARS)
        aggs[col] = s
        print(f"E27   {name:28s} {s[2021]:5.1f} -> {s[2024]:5.1f}pp   (d = {s[2024]-s[2021]:+.1f}pp)")
    d_formal_agg = aggs[sav][2024] - aggs[sav][2021]
    d_any_agg = aggs[any_sav][2024] - aggs[any_sav][2021]
    print(f"E27   aggregate share of the formal gain visible in TOTAL saving: "
          f"{d_any_agg / d_formal_agg:+.2f}  ({d_any_agg:+.1f}pp of {d_formal_agg:+.1f}pp)\n")

    d, pop = _deltas(fx, {"d_formal": sav, "d_informal": informal,
                          "d_semiformal": semiformal, "d_any": any_sav})
    base = pd.DataFrame({**d, "pop": pop})

    # ---------- PRIMARY -------------------------------------------------------------------------
    main = base[["d_formal", "d_informal", "pop"]].dropna()
    print("E27 G4 (primary estimation sample):",
          fx.gate_coverage(fx.pan_dev[fx.pan_dev["countrynewwb"].isin(main.index)], sav, 2024,
                           min_countries=30, min_pop_share=0.3))
    print(f"E27 primary sample n={len(main)}\n")
    prim = _bivariate(main, fx, "d_formal", "d_informal",
                      "PRIMARY: formal surge vs the OTHER-METHOD saving margin")
    print(f"E27   spreads: d_formal sd={main['d_formal'].std():.2f}pp, "
          f"d_informal sd={main['d_informal'].std():.2f}pp")

    # ---------- SECONDARY A: the semiformal margin ------------------------------------------------
    print()
    semi = base[["d_formal", "d_semiformal", "pop"]].dropna()
    _bivariate(semi, fx, "d_formal", "d_semiformal",
               f"SECONDARY A: savings-club margin, own sample n={len(semi)}")

    # ---------- SECONDARY C: pass-through ---------------------------------------------------------
    print()
    thru = base[["d_formal", "d_any", "pop"]].dropna()
    slope = _wslope(thru["d_any"], thru["d_formal"], thru["pop"])
    r_any, n_any = fx.weighted_corr(thru["d_formal"], thru["d_any"], thru["pop"])
    print(f"E27 SECONDARY C -- pass-through slope d(any saving) on d(formal saving) = {slope:+.3f}  "
          f"(r={r_any:+.3f}, n={n_any})")
    print("E27   reading: 1.0 = every point of formal saving is a NEW saver; 0.0 = pure "
          "relabelling. PARTLY MECHANICAL (formal is nested in any-saving) -- context, not the test")

    # descriptive: how the same countries' informal margin moved, by tercile of the formal surge
    print("\nE27 descriptive -- mean d(other-method saving) by tercile of the formal surge:")
    t = main.copy()
    t["ter"] = pd.qcut(t["d_formal"], 3, labels=["low", "mid", "high"])
    for lab, g in t.groupby("ter", observed=True):
        print(f"E27   d_formal {lab:4s} (mean {g['d_formal'].mean():+5.1f}pp, n={len(g)}): "
              f"mean d_informal = {g['d_informal'].mean():+.1f}pp")

    # ---------- VERDICT ---------------------------------------------------------------------------
    ok = (prim["r"] <= -0.30) and prim["sign_ok"] and (prim["ret"] >= 0.50)
    print("\n" + "=" * 78)
    print("E27 keep condition: primary r <= -0.30 (REGISTERED sign: displacement) AND G6 "
          "sign-stable AND retention >= 0.50")
    print(f"E27   observed primary r={prim['r']:+.3f}  jack={prim['r_jack']:+.3f} "
          f"ret={prim['ret']:+.2f}  -> passes: {ok}")


if __name__ == "__main__":
    run(Findex())
