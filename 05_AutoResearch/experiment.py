"""E35 (pre-registered): do the THREE-SEPARATE-RAILS partials (E23/E24/E25) replicate on 2017->2021?

Program 1 (replication debt) + Program 2 items 2.2/2.3 for the PARTIAL family.
Parents: E23, E24, E25 — first replication attempt on any of them (B3 not engaged).

B2 note: this experiment sits on the 2017->2021 transition, not the 2021->2024 shaft; E34 (same
cycle) carries the frame-rotation requirement on the `age_cat` panel.

WHY. E28 and E30 replicated six BIVARIATE co-movements onto 2017->2021 and promoted E1/E10/E11/
E12/E13/E14 to keep-general. No PARTIAL correlation has ever been replicated, and the partials are
what the paper's rail decomposition actually rests on: they are the only evidence that mobile money,
digital payments and wage digitalization are three separate channels rather than one digitalization
factor wearing three hats.

DESIGN, per the pre-registration. Exactly the E23/E24/E25 constructions on 2017->2021, pan_dev,
population weights = 2024 adult population (harness convention, held fixed across windows), with
2021->2024 recomputed in the same file so each replication is read beside its original:

  E23-R  partial r( d mobileaccount_t_d , d fin17a_17a1_d | d g20_any )
  E24-R  partial r( d fin32_acc        , d fin17a_17a1_d | d g20_any )
         + two-control variant (| d g20_any, d mobileaccount_t_d), descriptive
  E25-R  bivariate r( d fin32_acc , d fin22a_22a1_22g_d ) and the partial controlling d fin17a_17a1_d

Residualization is pop-weighted least squares on the control set, then weighted_corr of the
residuals (E5b/E23/E24 construction), with gate_jackknife on the residual pair.

INFERENCE LAYER, registered as part of the test (Program 2, non-delta->delta family). For every
primary cell in both windows: 2,000-draw country bootstrap percentile 95% interval and two-sided
bootstrap p; Kish neff; the UNWEIGHTED partial beside the weighted one; BH at q = 0.10 over the
declared family of SIX primary cells (three designs x two windows) on p_boot.

GATES. G3 (headline concepts declared; fin32_acc has no variant — E10 precedent). G4 per estimation
sample. G6 on every primary residual pair with the E4 magnitude rule (retention >= 0.5) applied —
the rule post-dates E23/E24/E25 and has never been applied to them.

PROMOTION RULE (B4). keep-window -> keep-general only if the 2017->2021 partial has the SAME SIGN,
|r| >= 0.30, and is G6 sign-stable with retention >= 0.5. A sign flip or a collapse below 0.30 means
the rail separation is a 2021-24 window property and the finding stays keep-window with that
recorded. A cell failing BH or the unweighted lens is FLAGGED, not demoted (E13 precedent).

DECLARED. Partialling a contemporaneous delta decomposes co-movement; it does not control
confounding and identifies nothing. Sample composition differs between windows (mobile money binds),
so every benchmark is recomputed on each window's own common sample. Descriptive, never causal.
"""
import numpy as np
import pandas as pd
from scipy import stats

from harness import Findex, INDICATORS

BOOT = 2000
SEED = 35
Q = 0.10
WINDOWS = [(2017, 2021), (2021, 2024)]

SAV = INDICATORS["saved_formally"]["headline"]      # fin17a_17a1_d
G20 = INDICATORS["digital_payment"]["headline"]     # g20_any
MM = INDICATORS["mobile_money"]["headline"]         # mobileaccount_t_d
WAGE = "fin32_acc"                                  # E10/E24 wage digitalization (no variant)
BOR = "fin22a_22a1_22g_d"                           # E11/E25 formal borrowing


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _wresid(y, X, w):
    """Residuals of a pop-weighted LS fit of y on a constant plus the columns of X (E24's helper)."""
    X = pd.DataFrame(X)
    A = np.column_stack([np.ones(len(X)), X.to_numpy(dtype=float)])
    yv = np.asarray(y, dtype=float)
    sw = np.sqrt(np.asarray(w, dtype=float))
    beta, *_ = np.linalg.lstsq(A * sw[:, None], yv * sw, rcond=None)
    return pd.Series(yv - A @ beta, index=X.index)


def _uresid(y, X):
    """Unweighted twin of _wresid (Program 2 item 2.3, applied to the partial family)."""
    X = pd.DataFrame(X)
    A = np.column_stack([np.ones(len(X)), X.to_numpy(dtype=float)])
    yv = np.asarray(y, dtype=float)
    beta, *_ = np.linalg.lstsq(A, yv, rcond=None)
    return pd.Series(yv - A @ beta, index=X.index)


def _ucorr(x, y):
    m = pd.notna(x) & pd.notna(y)
    return float(np.corrcoef(x[m], y[m])[0, 1]) if m.sum() >= 10 else np.nan


def deltas(fx: Findex, cols, t0, t1):
    """Wide per-country deltas (pp) over one window for the requested columns, plus pop weights."""
    out, pop = {}, None
    for name, col in cols.items():
        t = fx.country_panel(fx.pan_dev, col, [t0, t1])
        if t0 not in t.columns or t1 not in t.columns:
            out[name] = pd.Series(dtype=float)
            continue
        out[name] = (t[t1] - t[t0]).rename(name)
        # combine_first, not fillna: the weight series must span the UNION of the panels, or the
        # narrowest column (mobile money) silently shrinks every cell's sample. Each cell then
        # drops to its own common sample in cell(), which is the registered construction.
        pop = t["pop"] if pop is None else pop.combine_first(t["pop"])
    df = pd.DataFrame(out)
    df["pop"] = pop.reindex(df.index)
    return df


def _boot_partial(fx, df, xcol, ycol, ctrls, draws=BOOT, seed=SEED):
    """Country bootstrap of the pop-weighted PARTIAL correlation: the residualization is redone
    inside every draw, so the interval covers the control fit as well as the correlation."""
    rng = np.random.default_rng(seed)
    idx = np.arange(len(df))
    out = []
    for _ in range(draws):
        d = df.iloc[rng.choice(idx, size=len(idx), replace=True)].reset_index(drop=True)
        try:
            rx = _wresid(d[xcol], d[ctrls], d["pop"])
            ry = _wresid(d[ycol], d[ctrls], d["pop"])
            r, _n = fx.weighted_corr(rx, ry, d["pop"])
        except Exception:
            continue
        if pd.notna(r):
            out.append(r)
    if len(out) < draws * 0.9:
        return None, None, None
    a = np.asarray(out)
    tail = min((a <= 0).mean(), (a >= 0).mean())
    return (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)),
            float(max(2.0 * tail, 1.0 / draws)))


def _p_t(r, dof_n):
    if pd.isna(r) or dof_n <= 2.0:
        return np.nan
    df_ = dof_n - 2.0
    t = abs(r) * np.sqrt(df_ / max(1.0 - r ** 2, 1e-12))
    return float(2.0 * stats.t.sf(t, df_))


def benjamini_hochberg(pvals, q=Q):
    p = np.asarray(pvals, dtype=float)
    ok = ~np.isnan(p)
    m = int(ok.sum())
    out = np.zeros(len(p), dtype=bool)
    if m == 0:
        return out
    order = np.argsort(np.where(ok, p, np.inf))[:m]
    thresh = q * np.arange(1, m + 1) / m
    passed = p[order] <= thresh
    if passed.any():
        kmax = int(np.max(np.where(passed)[0]))
        out[order[:kmax + 1]] = True
    return out


def cell(fx: Findex, eid, df, xcol, ycol, ctrls, t0, t1, primary=True, label=""):
    """One partial (or bivariate, ctrls=[]) cell with the full inference layer."""
    use = df[[xcol, ycol, "pop"] + ctrls].dropna()
    w = use["pop"]
    if ctrls:
        rx, ry = _wresid(use[xcol], use[ctrls], w), _wresid(use[ycol], use[ctrls], w)
        ux, uy = _uresid(use[xcol], use[ctrls]), _uresid(use[ycol], use[ctrls])
    else:
        rx, ry, ux, uy = use[xcol], use[ycol], use[xcol], use[ycol]
    r, n = fx.weighted_corr(rx, ry, w)
    r_u = _ucorr(ux, uy)
    neff = _kish(w)
    g6 = fx.gate_jackknife(rx, ry, w)
    jack = g6.get("r_droptop")
    ret = (abs(jack) / abs(r)) if (jack is not None and r) else float("nan")

    lo = hi = p_boot = None
    if primary:
        lo, hi, p_boot = _boot_partial(fx, use, xcol, ycol, ctrls)

    ctrl_txt = ("|" + "+".join(c.replace("d_", "") for c in ctrls)) if ctrls else "(bivariate)"
    ci = f"[{lo:+.3f},{hi:+.3f}]" if lo is not None else "        n/a       "
    print(f"  {eid:7s} {t0}->{t1}  r({xcol.replace('d_','')},{ycol.replace('d_','')}{ctrl_txt})"
          f" = {r:+.3f}  n={n:3d} neff={neff:4.1f}  95%CI {ci}"
          f"  p_boot={p_boot if p_boot is None else round(p_boot, 4)}")
    print(f"          unweighted twin {r_u:+.3f}   G6 r_droptop {jack:+.3f} "
          f"(retention {ret:.2f}, sign_ok={g6['ok']}, E4 rule {'PASS' if ret >= 0.5 else 'FAIL'})"
          f"{('   [' + label + ']') if label else ''}")
    return {"eid": eid, "t0": t0, "t1": t1, "r": r, "n": n, "neff": neff, "r_unwtd": r_u,
            "ci_lo": lo, "ci_hi": hi, "p_boot": p_boot, "p_nom": _p_t(r, float(n)),
            "p_neff": _p_t(r, neff), "r_droptop": jack, "retention": ret,
            "g6_ok": bool(g6["ok"]), "primary": primary}


def run(fx: Findex):
    print("E35 — do the rail-separation PARTIALS replicate on 2017->2021? (dev panel)\n")
    print("G3:", fx.gate_variant("saved_formally", SAV), fx.gate_variant("digital_payment", G20),
          fx.gate_variant("mobile_money", MM))
    print("G3 note: fin32_acc (wages into an account) and fin22a_22a1_22g_d (formal borrowing) have")
    print("         no variant choice — E10/E11 precedent.")
    print("G5: n/a — no official partial-correlation series exists\n")

    cols = {"d_mm": MM, "d_sav": SAV, "d_g20": G20, "d_wage": WAGE, "d_bor": BOR}
    rows = []
    for t0, t1 in WINDOWS:
        d = deltas(fx, cols, t0, t1)
        g4 = fx.gate_coverage(fx.pan_dev, SAV, t1)
        print(f"=== window {t0}->{t1}   G4 n={g4['n_countries']} pop_share={g4['pop_share']} ===")

        rows.append(cell(fx, "E23-R", d, "d_mm", "d_sav", ["d_g20"], t0, t1,
                         label="mobile money net of digital payments"))
        rows.append(cell(fx, "E24-R", d, "d_wage", "d_sav", ["d_g20"], t0, t1,
                         label="wage digitalization net of digital payments"))
        rows.append(cell(fx, "E25-R", d, "d_wage", "d_bor", ["d_sav"], t0, t1,
                         label="wage -> formal borrowing net of saving"))

        # descriptive companions (not in the BH family, no bootstrap)
        print("   descriptive companions:")
        cell(fx, "E24-2c", d, "d_wage", "d_sav", ["d_g20", "d_mm"], t0, t1, primary=False,
             label="two simultaneous controls")
        cell(fx, "E23-rev", d, "d_g20", "d_sav", ["d_mm"], t0, t1, primary=False,
             label="symmetric reverse of E23")
        cell(fx, "E25-biv", d, "d_wage", "d_bor", [], t0, t1, primary=False,
             label="E25 bivariate")

        print("   same-window bivariate benchmarks (each on its own common sample):")
        for a, b in [("d_mm", "d_sav"), ("d_wage", "d_sav"), ("d_g20", "d_sav"),
                     ("d_mm", "d_g20")]:
            u = d[[a, b, "pop"]].dropna()
            r, n = fx.weighted_corr(u[a], u[b], u["pop"])
            print(f"      r({a},{b}) = {r:+.3f} (n={n})")
        print()

    res = pd.DataFrame([r for r in rows if r["primary"]])
    res["bh_boot"] = benjamini_hochberg(res["p_boot"].values)
    res["bh_neff"] = benjamini_hochberg(res["p_neff"].values)

    print("=" * 100)
    print("SUMMARY — six primary cells (three designs x two windows)\n")
    print(f"  {'cell':8s} {'window':11s} {'r_w':>7s} {'r_u':>7s} {'n':>4s} {'neff':>5s} "
          f"{'ret':>5s} {'p_boot':>8s} {'p_nom':>8s} {'p_neff':>8s} {'BHb':>4s} {'BHn':>4s}")
    for _, r in res.iterrows():
        print(f"  {r['eid']:8s} {int(r['t0'])}->{int(r['t1'])}   {r['r']:+7.3f} {r['r_unwtd']:+7.3f} "
              f"{int(r['n']):4d} {r['neff']:5.1f} {r['retention']:5.2f} {r['p_boot']:8.4f} "
              f"{r['p_nom']:8.4f} {r['p_neff']:8.4f} {str(bool(r['bh_boot'])):>4s} "
              f"{str(bool(r['bh_neff'])):>4s}")

    print(f"\n  BH at q={Q:.2f} over the declared family of {len(res)}: "
          f"p_boot rejects {int(res['bh_boot'].sum())}/{len(res)}, "
          f"p_nominal {int((res['p_nom'] <= Q).sum())}/{len(res)} (uncorrected reference), "
          f"p_neff rejects {int(res['bh_neff'].sum())}/{len(res)}")
    print(f"  unweighted lens (|r_u| >= 0.30): "
          f"{int((res['r_unwtd'].abs() >= 0.30).sum())}/{len(res)} cells")

    print("\n=== PROMOTION VERDICTS (pre-registered) ===")
    for eid, parent in [("E23-R", "E23"), ("E24-R", "E24"), ("E25-R", "E25")]:
        e = res[(res["eid"] == eid) & (res["t0"] == 2017)].iloc[0]
        o = res[(res["eid"] == eid) & (res["t0"] == 2021)].iloc[0]
        same = np.sign(e["r"]) == np.sign(o["r"])
        ok = bool(same and abs(e["r"]) >= 0.30 and e["g6_ok"] and e["retention"] >= 0.5)
        print(f"  {parent}: 2021->24 {o['r']:+.3f}  vs  2017->21 {e['r']:+.3f}  "
              f"[same sign {same}, |r|>=0.30 {abs(e['r']) >= 0.30}, "
              f"G6 {e['g6_ok']}, retention {e['retention']:.2f}] -> "
              f"{'PROMOTE to keep-general' if ok else 'STAYS keep-window (2021-24 window property)'}")
        flags = []
        if not bool(e["bh_boot"]):
            flags.append("fails BH on p_boot")
        if abs(e["r_unwtd"]) < 0.30:
            flags.append(f"unweighted twin {e['r_unwtd']:+.3f} < 0.30")
        if flags:
            print(f"       FLAG (not a demotion, E13 precedent): {'; '.join(flags)}")
    return res


if __name__ == "__main__":
    run(Findex())
