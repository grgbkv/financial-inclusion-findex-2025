"""E29 (pre-registered): is connectivity a PREREQUISITE (threshold) for the digital rails?

The rails series (E1/E10/E12/E23/E24, now promoted to keep-general by E28) has never had an answer
to the obvious objection: are these three margins just measuring internet penetration? The country
file's `internet` column is untouched by 50 experiments and exists for **2024 only** (77 developing
panel economies, 117 all-panel), which makes this a cross-section question and nothing more.

PRIMARY (Program 5.1) — developing panel, 2024 levels. y = g20_any (digital-payment headline),
x = internet.
  (i)   population-weighted correlation r
  (ii)  weighted mean of y within internet terciles
  (iii) nonlinearity: pop-weighted OLS of y on x, linear vs quadratic (increment in weighted R^2),
        and the weighted slope estimated SEPARATELY below and above the weighted median of x.
KEEP the THRESHOLD claim iff |r| >= 0.30 AND the low-half slope exceeds the high-half slope by a
factor >= 2 (prerequisite pattern) or the reverse by >= 2 (takeoff pattern) AND the quadratic term
adds >= 0.05 to weighted R^2. FALLBACK (registered, lesser): if |r| >= 0.30 but the nonlinearity bar
fails, keep only the linear statement, status keep-window, noting that `internet` is single-wave so
B4 promotion is impossible by construction.

SECONDARY (registered, reported regardless) — do the rails survive conditioning on connectivity?
For each rail: weighted PARTIAL correlation of d(rail) with d(fin17a_17a1_d) over 2021->2024,
controlling the 2024 LEVEL of `internet` (both residualized by weighted OLS on internet).
Registered comparison: each rail retains r_partial >= +0.30 or >= 2/3 of its unconditional value.
Declared design mismatch: a LEVEL control imposed on a DELTA design, and a 2024 control on a
2021->2024 change. Stated as a limitation, not fixed.

B6: country bootstrap (2,000 resamples, percentile interval) and Kish neff on the primary and on
every secondary partial. Declared: cross-country level correlations are the weakest design in the
ledger (development level confounds everything), so the primary is a description of the 2024
cross-section, never a mechanism, and carries no trend language.
"""
import numpy as np
import pandas as pd

from harness import Findex

NET = "internet"
DIGPAY = "g20_any"
SAVING = "fin17a_17a1_d"
RAILS = {"mobile_money": "mobileaccount_t_d", "wage_digital": "fin32_acc", "digital_pay": DIGPAY}
BOOT = 2000
SEED = 29


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _wls(y, X, w):
    """Population-weighted least squares; X without intercept. Returns (beta_with_intercept, R2)."""
    y = np.asarray(y, float)
    X = np.column_stack([np.ones(len(y))] + [np.asarray(c, float) for c in X])
    sw = np.sqrt(np.asarray(w, float))
    beta, *_ = np.linalg.lstsq(X * sw[:, None], y * sw, rcond=None)
    fit = X @ beta
    ybar = np.average(y, weights=w)
    ss_res = np.sum(w * (y - fit) ** 2)
    ss_tot = np.sum(w * (y - ybar) ** 2)
    return beta, float(1 - ss_res / ss_tot)


def _resid(y, x, w):
    beta, _ = _wls(y, [x], w)
    return np.asarray(y, float) - (beta[0] + beta[1] * np.asarray(x, float))


def _boot_stat(fn, frame, draws=BOOT, seed=SEED):
    """Country bootstrap of any statistic computed from a country-indexed frame (B6)."""
    rng = np.random.default_rng(seed)
    idx = np.arange(len(frame))
    out = []
    for _ in range(draws):
        s = frame.iloc[rng.choice(idx, size=len(idx), replace=True)]
        v = fn(s)
        if v is not None and pd.notna(v):
            out.append(v)
    if len(out) < draws * 0.9:
        return None, None
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def _levels(fx: Findex, cols, year=2024):
    d = fx.pan_dev
    d = d[d["year"] == year].set_index("countrynewwb")
    out = pd.DataFrame({name: d[c] * 100 for name, c in cols.items()})
    out["pop"] = d["pop_adult"]
    return out


def primary(fx: Findex):
    print("=" * 92)
    print("PRIMARY — 2024 cross-section: digital-payment level vs internet penetration (dev panel)")
    df = _levels(fx, {"y": DIGPAY, "x": NET}).dropna()
    w = df["pop"]
    r, n = fx.weighted_corr(df["x"], df["y"], w)
    neff = _kish(w)
    lo, hi = _boot_stat(lambda s: fx.weighted_corr(s["x"], s["y"], s["pop"])[0], df)
    print(f"  weighted r(g20_any, internet) = {r:+.3f}  (n={n}, Kish neff={neff:.1f})"
          f"  95% CI [{lo:+.3f}, {hi:+.3f}]")
    print("  G4:", fx.gate_coverage(fx.pan_dev, NET, 2024))
    print("  G6:", fx.gate_jackknife(df["x"], df["y"], w))

    ter = pd.qcut(df["x"], 3, labels=["low", "mid", "high"])
    print("\n  internet terciles (weighted means):")
    for lab, g in df.groupby(ter, observed=True):
        print(f"    {lab:4s}  internet {np.average(g['x'], weights=g['pop']):5.1f}pp"
              f"   -> g20_any {np.average(g['y'], weights=g['pop']):5.1f}pp   (n={len(g)},"
              f" internet range {g['x'].min():.0f}-{g['x'].max():.0f}pp)")

    _, r2_lin = _wls(df["y"], [df["x"]], w)
    _, r2_quad = _wls(df["y"], [df["x"], df["x"] ** 2], w)
    print(f"\n  weighted R^2: linear {r2_lin:.3f} -> quadratic {r2_quad:.3f} "
          f"(increment {r2_quad - r2_lin:+.3f}; registered bar >= 0.05)")

    srt = df.sort_values("x")
    cum = srt["pop"].cumsum() / srt["pop"].sum()
    med = float(srt.loc[cum >= 0.5, "x"].iloc[0])  # population-weighted median internet level
    lowh, highh = df[df["x"] <= med], df[df["x"] > med]
    b_lo, _ = _wls(lowh["y"], [lowh["x"]], lowh["pop"])
    b_hi, _ = _wls(highh["y"], [highh["x"]], highh["pop"])
    ratio = abs(b_lo[1]) / abs(b_hi[1]) if b_hi[1] else float("inf")
    print(f"  weighted median internet = {med:.1f}pp")
    print(f"  slope of g20_any on internet BELOW median = {b_lo[1]:+.3f} (n={len(lowh)});"
          f"  ABOVE median = {b_hi[1]:+.3f} (n={len(highh)});  ratio low/high = {ratio:.2f}")

    thresh_ok = abs(r) >= 0.30 and (ratio >= 2 or (ratio and 1 / ratio >= 2)) and \
        (r2_quad - r2_lin) >= 0.05
    linear_ok = abs(r) >= 0.30
    print(f"\n  THRESHOLD claim passes: {thresh_ok}   |   fallback LINEAR claim passes: {linear_ok}")
    print("  (pattern reading: ratio > 1 = steeper where connectivity is scarce = prerequisite;"
          " ratio < 1 = takeoff)")

    print("\n  descriptive — the other two margins against the same x:")
    for name, col in [("account_t_d", "account_t_d"), ("mobileaccount_t_d", "mobileaccount_t_d"),
                      (SAVING, SAVING)]:
        d2 = _levels(fx, {"y": col, "x": NET}).dropna()
        r2_, n2 = fx.weighted_corr(d2["x"], d2["y"], d2["pop"])
        print(f"    r({name}, internet) = {r2_:+.3f}  (n={n2})")
    return {"r": r, "n": n, "neff": neff, "ci": (lo, hi), "thresh_ok": thresh_ok,
            "linear_ok": linear_ok, "ratio": ratio, "dr2": r2_quad - r2_lin}


def secondary(fx: Findex):
    print("\n" + "=" * 92)
    print("SECONDARY — do the 2021->2024 rails survive conditioning on the 2024 internet level?")
    print("  DECLARED MISMATCH: a level control on a delta design; the control is dated 2024 while")
    print("  the change spans 2021->2024. Reported as registered, not defended.\n")
    net = _levels(fx, {"net": NET})
    sav = fx.country_panel(fx.pan_dev, SAVING, [2021, 2024])
    d_sav = (sav[2024] - sav[2021]).rename("dy")
    out = {}
    for name, col in RAILS.items():
        t = fx.country_panel(fx.pan_dev, col, [2021, 2024])
        d_rail = (t[2024] - t[2021]).rename("dx")
        df = pd.concat([d_rail, d_sav, net["net"], net["pop"]], axis=1).dropna()
        r_un, n = fx.weighted_corr(df["dx"], df["dy"], df["pop"])

        def part(s):
            rx = _resid(s["dx"], s["net"], s["pop"])
            ry = _resid(s["dy"], s["net"], s["pop"])
            return fx.weighted_corr(pd.Series(rx), pd.Series(ry), s["pop"].reset_index(drop=True))[0]

        r_p = part(df)
        lo, hi = _boot_stat(part, df, seed=SEED + hash(name) % 100)
        retain = abs(r_p) / abs(r_un) if r_un else float("nan")
        ok = (r_p >= 0.30) or (retain >= 2 / 3)
        ci = f"[{lo:+.3f}, {hi:+.3f}]" if lo is not None else "n/a"
        print(f"  {name:12s} unconditional r = {r_un:+.3f}  ->  partial | internet = {r_p:+.3f}"
              f"  (n={n}, neff={_kish(df['pop']):.1f}, retains {retain:.2f})  95% CI {ci}")
        print(f"      registered condition (partial >= +0.30 OR retains >= 0.67): {ok}")
        out[name] = {"r_un": r_un, "r_p": r_p, "retain": retain, "ok": ok, "n": n,
                     "ci": (lo, hi)}
    return out


if __name__ == "__main__":
    fx = Findex()
    print("E29 — connectivity as prerequisite (Program 5.1/5.2); `internet` is an UNTOUCHED column\n")
    print("G3:", fx.gate_variant("digital_payment", DIGPAY), fx.gate_variant("saved_formally", SAVING),
          fx.gate_variant("mobile_money", RAILS["mobile_money"]))
    print("G3 note: `internet` and `fin32_acc` have no variant choice in the registry — declared")
    print("G5: n/a — no official series for a cross-country correlation\n")
    p = primary(fx)
    s = secondary(fx)
    print("\n" + "=" * 92)
    print(f"VERDICT INPUTS — primary threshold {p['thresh_ok']}, primary linear {p['linear_ok']}"
          f" (r={p['r']:+.3f}, slope ratio {p['ratio']:.2f}, dR^2 {p['dr2']:+.3f});"
          f" secondary all-rails-survive = {all(v['ok'] for v in s.values())}")
