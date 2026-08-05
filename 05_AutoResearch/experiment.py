"""E32 (pre-registered): does the ledger's association family survive false-discovery control,
and how much of it is the population weighting?

Program 2 — the inference debt (agenda items 2.2 and 2.3), named by the 2026-08-03 addendum as this
cycle's Program-2 slot. Parent: the association ledger as a whole (a meta-experiment, no single
parent finding, so rule B3's lineage cap is not engaged).

THE FAMILY (declared in the pre-registration BEFORE computation). The homogeneous same-construction
family: population-weighted correlation of two 2021->2024 changes on `pan_dev`, group == "all".
Sixteen tests. Partial-correlation designs (E5b/E23/E24), level->change designs (E5/E9/E17), gap
designs (E3/E20/E21), replications (E22/E28/E30), the 2024 cross-section (E29), the trajectory
design (E31) and the micro stream are EXCLUDED and named as excluded, so the family cannot be
gerrymandered after the answer.

WHAT IS COMPUTED per test: population-weighted r (harness), UNWEIGHTED r, nominal n, Kish
neff = (sum w)^2 / sum(w^2), a country bootstrap (2,000 draws, percentile 95% CI), and three
p-values -- p_boot (2 x the smaller bootstrap tail mass at 0, floored at 1/draws), p_nominal (t on
n-2 df) and p_neff (the same t on neff-2 df). Benjamini-Hochberg at q = 0.10 over the sixteen, on
p_boot (primary) and p_neff (secondary).

PRE-REGISTERED CLAIM. Kept iff BOTH (a) >= 80% of the family's kept rows (7 of 8: E1, E7, E10, E11,
E12, E13, E14, E25) survive BH at q = 0.10 on p_boot, AND (b) >= 80% of those same rows retain
|r_unweighted| >= 0.30.

DECLARED. This computes no new association; it recomputes existing ones under two extra lenses. Not
subject to B4 and it adds no new keep. The BH family is the delta->delta family only -- a
ledger-wide FDR would be more punishing, not less.
"""
import numpy as np
import pandas as pd
from scipy import stats

from harness import Findex

BOOT = 2000
SEED = 32
Q = 0.10
WINDOW = (2021, 2024)

# ledger id -> (x column, y column, r reported in findings.tsv, ledger status)
# Declared in the pre-registration; the column pairs are the ones the original experiments used.
FAMILY = [
    ("E1",  "mobileaccount_t_d",   "fin17a_17a1_d",     +0.719, "keep-general"),
    ("E2",  "mobileaccount_t_d",   "fin24aSD_ND",       +0.189, "discard"),
    ("E7",  "fin17a_17a1_d",       "fin24sav",          +0.541, "keep-window"),
    ("E10", "fin32_acc",           "fin17a_17a1_d",     +0.791, "keep-general"),
    ("E11", "fin22a_22a1_22g_d",   "fin17a_17a1_d",     +0.403, "keep-general"),
    ("E12", "g20_any",             "fin17a_17a1_d",     +0.370, "keep-general"),
    ("E13", "fiaccount_t_d",       "mobileaccount_t_d", +0.435, "keep-general"),
    ("E14", "mobileaccount_t_d",   "g20_any",           +0.600, "keep-general"),
    ("E15", "fin24aSD_ND",         "fin17a_17a1_d",     +0.031, "discard"),
    ("E16", "account_t_d",         "fin17a_17a1_d",     +0.198, "discard"),
    ("E18", "fin24bor",            "fin17a_17a1_d",     +0.069, "discard"),
    ("E19", "inactive_t_d",        "fin17a_17a1_d",     +0.160, "discard"),
    ("E25", "fin32_acc",           "fin22a_22a1_22g_d", +0.605, "keep-window"),
    ("E26", "fin32_acc",           "fin24aSD_ND",       +0.294, "discard"),
    ("E27", "fin17c",              "fin17a_17a1_d",     +0.696, "discard"),
    ("E27b", "fin17b",             "fin17a_17a1_d",     +0.531, "secondary"),
]

# The family's kept rows, declared before computation (claim (a) and (b) are evaluated on these).
KEPT_ROWS = ["E1", "E7", "E10", "E11", "E12", "E13", "E14", "E25"]


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _unweighted_corr(x, y):
    m = pd.notna(x) & pd.notna(y)
    if m.sum() < 10:
        return np.nan
    return float(np.corrcoef(x[m], y[m])[0, 1])


def delta_frame(fx: Findex, xcol, ycol):
    """Per-country 2021->2024 change in both columns, plus the 2024 population weight."""
    y0, y1 = WINDOW
    wx = fx.country_panel(fx.pan_dev, xcol, [y0, y1])
    wy = fx.country_panel(fx.pan_dev, ycol, [y0, y1])
    df = pd.DataFrame({
        "dx": wx[y1] - wx[y0],
        "dy": wy[y1] - wy[y0],
        "pop": wx["pop"],
    }).dropna()
    return df


def _boot(fx: Findex, df, draws=BOOT, seed=SEED):
    """Country bootstrap of the population-weighted r: percentile CI plus a two-sided
    bootstrap p-value (2 x the smaller tail mass at zero, floored at 1/draws)."""
    rng = np.random.default_rng(seed)
    idx = np.arange(len(df))
    out = []
    for _ in range(draws):
        d = df.iloc[rng.choice(idx, size=len(idx), replace=True)]
        r, _n = fx.weighted_corr(d["dx"], d["dy"], d["pop"])
        if pd.notna(r):
            out.append(r)
    if len(out) < draws * 0.9:
        return None, None, None
    a = np.asarray(out)
    lo, hi = float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5))
    tail = min((a <= 0).mean(), (a >= 0).mean())
    p = max(2.0 * tail, 1.0 / draws)
    return lo, hi, float(p)


def _p_t(r, dof_n):
    """Two-sided p from the correlation t-statistic with dof_n - 2 degrees of freedom."""
    if pd.isna(r) or dof_n <= 2.0:
        return np.nan
    df_ = dof_n - 2.0
    denom = max(1.0 - r ** 2, 1e-12)
    t = abs(r) * np.sqrt(df_ / denom)
    return float(2.0 * stats.t.sf(t, df_))


def benjamini_hochberg(pvals, q=Q):
    """Return a boolean array: True where the hypothesis is rejected under BH at level q."""
    p = np.asarray(pvals, dtype=float)
    ok = ~np.isnan(p)
    m = int(ok.sum())
    out = np.zeros(len(p), dtype=bool)
    if m == 0:
        return out
    order = np.argsort(np.where(ok, p, np.inf))[:m]
    thresh = q * (np.arange(1, m + 1)) / m
    passed = p[order] <= thresh
    if passed.any():
        kmax = np.max(np.nonzero(passed)[0])
        out[order[:kmax + 1]] = True
    return out


def run(fx: Findex):
    print("=" * 104)
    print("E32 — BH false-discovery accounting + unweighted replication over the delta->delta "
          "family (2021->2024, pan_dev)")
    print("=" * 104)

    rows = []
    for eid, xcol, ycol, r_ledger, status in FAMILY:
        df = delta_frame(fx, xcol, ycol)
        if len(df) < 10:
            print(f"  {eid:5s} insufficient coverage (n={len(df)})")
            continue
        r_w, n = fx.weighted_corr(df["dx"], df["dy"], df["pop"])
        r_u = _unweighted_corr(df["dx"], df["dy"])
        neff = _kish(df["pop"])
        lo, hi, p_boot = _boot(fx, df)
        g6 = fx.gate_jackknife(df["dx"], df["dy"], df["pop"])
        cov = fx.gate_coverage(fx.pan_dev, ycol, 2024)
        rows.append({
            "id": eid, "status": status, "x": xcol, "y": ycol,
            "r_ledger": r_ledger, "r_w": r_w, "r_u": r_u, "n": n, "neff": neff,
            "ci_lo": lo, "ci_hi": hi, "p_boot": p_boot,
            "p_nom": _p_t(r_w, float(n)), "p_neff": _p_t(r_w, neff),
            "g6_ok": g6["ok"], "r_droptop": g6.get("r_droptop"),
            "n_countries": cov["n_countries"], "pop_share": cov["pop_share"],
        })

    res = pd.DataFrame(rows).set_index("id")

    # ---- reproduction check: does this file reproduce the ledger's own numbers? -------------
    res["repro_dev"] = (res["r_w"] - res["r_ledger"]).abs()
    max_dev = res["repro_dev"].max()
    print(f"\nREPRODUCTION CHECK — max |r_recomputed - r_ledger| = {max_dev:.4f} "
          f"over {len(res)} tests  -> {'OK' if max_dev <= 0.02 else 'MISMATCH — investigate'}")
    bad = res[res["repro_dev"] > 0.02]
    if len(bad):
        print(bad[["r_ledger", "r_w", "n"]].to_string())

    # ---- BH ---------------------------------------------------------------------------------
    res["bh_boot"] = benjamini_hochberg(res["p_boot"].values, Q)
    res["bh_neff"] = benjamini_hochberg(res["p_neff"].values, Q)
    res["bh_nom"] = benjamini_hochberg(res["p_nom"].values, Q)

    print("\n" + "-" * 104)
    print("PER-TEST TABLE  (r_w = population-weighted, r_u = UNWEIGHTED, neff = Kish effective n)")
    print("-" * 104)
    hdr = (f"{'id':5s} {'status':13s} {'r_w':>7s} {'r_u':>7s} {'d':>7s} {'n':>4s} {'neff':>5s} "
           f"{'95% CI':>18s} {'p_boot':>8s} {'p_nom':>8s} {'p_neff':>8s} {'BHb':>4s} {'BHn':>4s}")
    print(hdr)
    for eid, r in res.iterrows():
        ci = f"[{r['ci_lo']:+.3f},{r['ci_hi']:+.3f}]" if r["ci_lo"] is not None else "  n/a "
        print(f"{eid:5s} {r['status']:13s} {r['r_w']:+7.3f} {r['r_u']:+7.3f} "
              f"{r['r_u'] - r['r_w']:+7.3f} {int(r['n']):4d} {r['neff']:5.1f} {ci:>18s} "
              f"{r['p_boot']:8.4f} {r['p_nom']:8.4f} {r['p_neff']:8.4f} "
              f"{'Y' if r['bh_boot'] else 'n':>4s} {'Y' if r['bh_neff'] else 'n':>4s}")

    # ---- pre-registered claim ---------------------------------------------------------------
    kept = res.loc[[k for k in KEPT_ROWS if k in res.index]]
    n_kept = len(kept)
    a_pass = kept["bh_boot"].sum()
    b_pass = (kept["r_u"].abs() >= 0.30).sum()
    a_ok = a_pass >= 0.80 * n_kept
    b_ok = b_pass >= 0.80 * n_kept

    print("\n" + "=" * 104)
    print(f"PRE-REGISTERED CLAIM — evaluated on the {n_kept} KEPT rows of the family "
          f"({', '.join(kept.index)})")
    print("=" * 104)
    print(f"  (a) survive BH at q={Q:.2f} on p_boot : {a_pass}/{n_kept} "
          f"({a_pass / n_kept:.0%})  bar = 80%  -> {'PASS' if a_ok else 'FAIL'}")
    if a_pass < n_kept:
        print(f"      FAILING ROWS: {', '.join(kept.index[~kept['bh_boot']])}")
    print(f"  (b) retain |r_unweighted| >= 0.30     : {b_pass}/{n_kept} "
          f"({b_pass / n_kept:.0%})  bar = 80%  -> {'PASS' if b_ok else 'FAIL'}")
    if b_pass < n_kept:
        drop = kept[kept["r_u"].abs() < 0.30]
        print("      FAILING ROWS: " + ", ".join(
            f"{i} (r_w {r['r_w']:+.3f} -> r_u {r['r_u']:+.3f})" for i, r in drop.iterrows()))
    verdict = "KEEP" if (a_ok and b_ok) else "DISCARD"
    print(f"\n  JOINT VERDICT: {verdict}  (both (a) and (b) required)")

    # ---- context the claim does not capture -------------------------------------------------
    print("\n" + "-" * 104)
    print("CONTEXT (reported, not part of the pre-registered claim)")
    print("-" * 104)
    print(f"  BH survivors over the WHOLE family of {len(res)}: "
          f"p_boot {int(res['bh_boot'].sum())}/{len(res)}, "
          f"p_nominal {int(res['bh_nom'].sum())}/{len(res)}, "
          f"p_neff {int(res['bh_neff'].sum())}/{len(res)}")
    print(f"  Kish neff across the family: min {res['neff'].min():.1f}, "
          f"median {res['neff'].median():.1f}, max {res['neff'].max():.1f} "
          f"(nominal n {int(res['n'].min())}-{int(res['n'].max())})")
    shrink = res["r_u"].abs() - res["r_w"].abs()
    print(f"  |r| change when the population weighting is REMOVED: median {shrink.median():+.3f}, "
          f"{int((shrink < 0).sum())}/{len(res)} tests weaker unweighted")
    print(f"  Sign flips weighted -> unweighted: "
          f"{', '.join(res.index[np.sign(res['r_u']) != np.sign(res['r_w'])]) or 'none'}")
    print(f"  G6 sign-stable: {int(res['g6_ok'].sum())}/{len(res)}; "
          f"E4 magnitude rule (|r_droptop| >= 0.5|r_full|) held by: "
          f"{', '.join(res.index[(res['r_droptop'].abs() >= 0.5 * res['r_w'].abs())])}")
    print(f"  Coverage (G4) on the destination column: "
          f"n_countries {int(res['n_countries'].min())}-{int(res['n_countries'].max())}, "
          f"pop share {res['pop_share'].min():.2f}-{res['pop_share'].max():.2f}")

    # BH threshold detail, so the boundary is auditable
    m = len(res)
    ranked = res.sort_values("p_boot")
    print("\n  BH ladder on p_boot (q=0.10): rank  p_boot  threshold=q*rank/m  reject?")
    for k, (eid, r) in enumerate(ranked.iterrows(), start=1):
        thr = Q * k / m
        print(f"    {k:2d}  {eid:5s} {r['p_boot']:8.4f}  {thr:8.4f}  "
              f"{'Y' if r['bh_boot'] else 'n'}")
    return res


if __name__ == "__main__":
    fx = Findex()
    run(fx)
