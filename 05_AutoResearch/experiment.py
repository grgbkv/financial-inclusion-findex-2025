"""E28 (pre-registered): do the three digitalization rails co-move with formal saving BEFORE 2021?

Under rule B4 every rails keep in the ledger is a WINDOW claim, because all three were measured on
the 2021->2024 surge window only:

    E1   d(mobileaccount_t_d) ~ d(fin17a_17a1_d)   r = +0.719  (n = 58)
    E10  d(fin32_acc)         ~ d(fin17a_17a1_d)   r = +0.791  (n = 71)
    E12  d(g20_any)           ~ d(fin17a_17a1_d)   r = +0.370  (n = 76)

This runs each construction unchanged on the two earlier transitions that carry all four columns --
2014->2017 and 2017->2021 -- with 2021->2024 recomputed as the reference row. Promotion rule
(pre-registered): a rail becomes `keep-general` iff at least one earlier window reaches r >= +0.30
with the same sign, G6 sign-stable, and r_droptop >= 0.5 * r_full (the E4 judgment rule). Otherwise
it stays `keep-window` and the 2021-24 result is relabelled window-specific.

Rule B6 inference on every cell: country bootstrap (2,000 resamples, percentile 95% interval) and
the Kish effective sample size neff = (sum w)^2 / sum(w^2) beside the nominal n.

Declared: contemporaneous delta-on-delta co-movement in every window -- descriptive, never causal.
Composition differs by rail and window (mobile money is thin at 57-61 countries); each cell prints
its own n, neff and interval. A null in a calm window is not proof the mechanism is absent, so the
per-window SD of both deltas and the dev-panel aggregate move are printed to let a
variance-collapse reading be checked.
"""
import numpy as np
import pandas as pd

from harness import Findex

TRANSITIONS = [(2014, 2017), (2017, 2021), (2021, 2024)]
RAILS = {
    "mobile_money": "mobileaccount_t_d",   # E1
    "wage_digital": "fin32_acc",           # E10 (no variant choice)
    "digital_pay": "g20_any",              # E12
}
SAVING = "fin17a_17a1_d"
BOOT = 2000
SEED = 28


def _delta(fx: Findex, col, t0, t1):
    """Per-country delta in pp between two waves on the developing panel, plus 2024 pop weight."""
    t = fx.country_panel(fx.pan_dev, col, [t0, t1])
    if t0 not in t.columns or t1 not in t.columns:
        return None, None
    return (t[t1] - t[t0]).dropna(), t["pop"]


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _boot_ci(fx, x, y, w, draws=BOOT, seed=SEED):
    """Country bootstrap: resample countries with replacement, percentile 95% interval (B6)."""
    rng = np.random.default_rng(seed)
    xs, ys, ws = x.to_numpy(), y.to_numpy(), w.to_numpy()
    idx = np.arange(len(xs))
    out = []
    for _ in range(draws):
        s = rng.choice(idx, size=len(idx), replace=True)
        r, _n = fx.weighted_corr(pd.Series(xs[s]), pd.Series(ys[s]), pd.Series(ws[s]))
        if pd.notna(r):
            out.append(r)
    if len(out) < draws * 0.9:
        return None, None
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def _terciles(dx, dy):
    q = pd.qcut(dx, 3, labels=["low", "mid", "high"], duplicates="drop")
    means = dy.groupby(q, observed=True).mean()
    return " / ".join(f"{k}={v:+.1f}pp" for k, v in means.items())


def cell(fx: Findex, rail_name, rail_col, t0, t1):
    dr, pop_r = _delta(fx, rail_col, t0, t1)
    ds, pop_s = _delta(fx, SAVING, t0, t1)
    if dr is None or ds is None:
        print(f"  {rail_name:12s} {t0}->{t1}: column absent in one wave — skipped")
        return None
    df = pd.DataFrame({"x": dr, "y": ds}).dropna()
    df["w"] = pop_r.reindex(df.index).fillna(pop_s.reindex(df.index))
    df = df.dropna(subset=["w"])

    r, n = fx.weighted_corr(df["x"], df["y"], df["w"])
    g6 = fx.gate_jackknife(df["x"], df["y"], df["w"])
    g4 = fx.gate_coverage(fx.pan_dev, rail_col, t1)
    lo, hi = _boot_ci(fx, df["x"], df["y"], df["w"])
    neff = _kish(df["w"])
    jack = g6.get("r_droptop")
    ret = (abs(jack) / abs(r)) if (jack is not None and r) else float("nan")
    ci = f"[{lo:+.3f}, {hi:+.3f}]" if lo is not None else "n/a"

    print(f"  {rail_name:12s} {t0}->{t1}:  r = {r:+.3f}  (n={n}, neff={neff:.1f})  95% CI {ci}")
    print(f"      G6 r_droptop = {jack:+.3f} (retention {ret:.2f}, sign_ok={g6['ok']})"
          f" | G4 n={g4['n_countries']} pop_share={g4['pop_share']}"
          f" | SD d(rail)={df['x'].std():.1f}pp  SD d(saving)={df['y'].std():.1f}pp")
    print(f"      terciles of d(rail) -> mean d(saving): {_terciles(df['x'], df['y'])}")
    return {"rail": rail_name, "t0": t0, "t1": t1, "r": r, "n": n, "neff": neff,
            "ci_lo": lo, "ci_hi": hi, "r_droptop": jack, "retention": ret,
            "g6_ok": bool(g6["ok"]), "sd_x": float(df["x"].std()), "sd_y": float(df["y"].std())}


def main():
    fx = Findex()
    print("E28 — the three rails vs the formal-saving margin, three windows, developing panel\n")
    print("G3 declarations:",
          fx.gate_variant("saved_formally", SAVING),
          fx.gate_variant("mobile_money", RAILS["mobile_money"]),
          fx.gate_variant("digital_payment", RAILS["digital_pay"]))
    print("G3 note: fin32_acc (wages into an account) has no variant choice — E10 precedent")
    print("G5: n/a — no official delta-correlation series exists\n")

    rows = []
    for rail_name, rail_col in RAILS.items():
        for t0, t1 in TRANSITIONS:
            got = cell(fx, rail_name, rail_col, t0, t1)
            if got:
                rows.append(got)
        print()

    tab = pd.DataFrame(rows)
    print("=" * 92)
    print("SUMMARY — weighted r(d rail, d formal saving)\n")
    print(tab.pivot(index="rail", columns="t0", values="r").round(3).to_string())
    print()
    print("nominal n / Kish neff per cell:")
    for _, row in tab.iterrows():
        print(f"  {row['rail']:12s} {int(row['t0'])}->{int(row['t1'])}: "
              f"n={int(row['n']):3d}  neff={row['neff']:5.1f}  "
              f"CI [{row['ci_lo']:+.3f}, {row['ci_hi']:+.3f}]")

    print("\nPROMOTION VERDICTS (pre-registered: an earlier window with r >= +0.30,")
    print("                    G6 sign-stable, retention >= 0.50)")
    for rail_name in RAILS:
        early = tab[(tab["rail"] == rail_name) & (tab["t0"] < 2021)]
        ok = early[(early["r"] >= 0.30) & (early["g6_ok"]) & (early["retention"] >= 0.50)]
        windows = ", ".join(f"{int(a)}->{int(b)}" for a, b in zip(ok["t0"], ok["t1"]))
        verdict = f"PROMOTE to keep-general (replicated on {windows})" if len(ok) \
            else "stays keep-window — 2021-24 result is window-specific"
        best = early.loc[early["r"].idxmax()] if len(early) else None
        extra = (f"\n      best earlier: r = {best['r']:+.3f} in "
                 f"{int(best['t0'])}->{int(best['t1'])} (retention {best['retention']:.2f})"
                 ) if best is not None else ""
        print(f"  {rail_name:12s} -> {verdict}{extra}")

    print("\nContext for any earlier-window null — the saving margin's own movement by window:")
    for t0, t1 in TRANSITIONS:
        ds, _ = _delta(fx, SAVING, t0, t1)
        lvl = fx.series(fx.pan_dev, SAVING, [t0, t1])
        print(f"  {t0}->{t1}: dev aggregate {lvl[t0]:.1f} -> {lvl[t1]:.1f}pp "
              f"({lvl[t1]-lvl[t0]:+.1f}pp), country-level SD of delta = {ds.std():.1f}pp")


if __name__ == "__main__":
    main()
