"""E40 (pre-registered): a LEDGER-WIDE false-discovery and de-weighting audit.

Program 2, items 2.2 / 2.3 / 2.5; rule B7 ("report a Benjamini-Hochberg-adjusted view over the
association ledger before the next distillation into the paper draft"). The distillation happens
in this cycle, so the debt is due.

Parent: the association ledger as a whole (a meta-experiment, no single parent, rule B3's lineage
cap not engaged -- the E32 precedent). Lands on no new coverage cell by construction and is NOT
counted toward B2; E41 carries the breadth requirement this cycle.

WHAT E32 AND E35 LEFT OPEN. E32 paid items 2.2/2.3 for the sixteen-test delta->delta family and
E35 for six partial cells in 2017->2021. Never audited under either lens: the level->change family
(E5/E9/E17), the gap-change designs (E3/E20), the 2024 cross-section (E29), the regional split
(E22), the six earlier-window replication cells (E28/E30), and the original-window partials
(E5b/E23/E24). And no BH has ever been run across the ledger as ONE family, which is what B7 asks
for -- a per-family BH is exactly the gerrymander B7 exists to stop.

THE FAMILY, declared in the pre-registration before computation: 33 tests in six blocks, listed in
TESTS below. Excluded and named as excluded: statistics that are not correlations (E21/E34 mean
log-odds gaps, E31/E36 share-of-economies counts, E39 distributional shares), E33's nine `fh` cells
(correlations, but kept as a family with its own internal agreement rule), E37/E38's pooled and
per-window cells (already reported with intervals, already discarded), and the whole micro stream.

PER TEST: population-weighted r, the UNWEIGHTED twin, nominal n, Kish neff = (sum w)^2/sum(w^2),
a 2,000-draw country bootstrap (percentile 95% interval + two-sided p_boot), p_nominal (t on n-2),
p_neff (the same t on neff-2), and the G6 drop-top-5 jackknife with the E4 retention ratio.
BH at q = 0.10 over all 33 on p_boot (primary) and p_neff (secondary). Every cell carries a
REPRODUCTION CHECK against the r on record; deviation > 0.02 is printed and the cell is reported as
unreproduced rather than quietly used.

PRE-REGISTERED CLAIMS.
  A  >= 50% of the ledger's currently-keep* association rows survive ledger-wide BH at q=0.10 on
     p_boot.
  B  >= 80% of those same rows retain |r_unweighted| >= 0.30.
  C  At most ONE currently-discard row has |r_unweighted| >= 0.30 while its weighted |r| < 0.30
     (E32 identified E16 as that case).

REGISTERED ALTERNATIVE OUTCOME. A large-scale failure of A is the informative result and is logged
as a keep in the negative direction.

DECLARED. Computes no new association; recomputes existing ones under three extra lenses. Adds no
keep of its own, is not subject to B4, and changes no status by itself -- status changes happen in
the distillation step.
"""
import numpy as np
import pandas as pd
from scipy import stats

from harness import Findex

BOOT = 2000
SEED = 40
Q = 0.10

SAV = "fin17a_17a1_d"
G20 = "g20_any"
MM = "mobileaccount_t_d"
FI = "fiaccount_t_d"
ACC = "account_t_d"
WAGE = "fin32_acc"
BOR = "fin22a_22a1_22g_d"
SSA = "Sub-Saharan Africa (excluding high income)"


# --------------------------------------------------------------------------- helpers
def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _ucorr(x, y):
    m = pd.notna(x) & pd.notna(y)
    return float(np.corrcoef(x[m], y[m])[0, 1]) if m.sum() >= 10 else np.nan


def _wresid(y, X, w):
    """Residuals of a pop-weighted LS fit of y on a constant plus the columns of X.
    reset_index discipline from E37: bare arrays misalign against a sliced weight index."""
    X = pd.DataFrame(X).reset_index(drop=True)
    A = np.column_stack([np.ones(len(X)), X.to_numpy(dtype=float)])
    yv = np.asarray(y, dtype=float)
    sw = np.sqrt(np.asarray(w, dtype=float))
    beta, *_ = np.linalg.lstsq(A * sw[:, None], yv * sw, rcond=None)
    return pd.Series(yv - A @ beta, index=X.index)


def _uresid(y, X):
    X = pd.DataFrame(X).reset_index(drop=True)
    A = np.column_stack([np.ones(len(X)), X.to_numpy(dtype=float)])
    yv = np.asarray(y, dtype=float)
    beta, *_ = np.linalg.lstsq(A, yv, rcond=None)
    return pd.Series(yv - A @ beta, index=X.index)


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
    passed = p[order] <= q * np.arange(1, m + 1) / m
    if passed.any():
        out[order[:np.max(np.nonzero(passed)[0]) + 1]] = True
    return out


# --------------------------------------------------------------------------- frame builders
def _delta(fx, frame, col, t0, t1):
    w = fx.country_panel(frame, col, [t0, t1])
    if t0 not in w.columns or t1 not in w.columns:
        return pd.Series(dtype=float), pd.Series(dtype=float)
    return (w[t1] - w[t0]), w["pop"]


def dd(fx, xcol, ycol, t0=2021, t1=2024, region=None, exclude_region=None):
    """Block 1/6: change-vs-change on pan_dev, optionally restricted by region."""
    frame = fx.pan_dev
    if region is not None:
        frame = frame[frame["regionwb24_hi"] == region]
    if exclude_region is not None:
        frame = frame[frame["regionwb24_hi"] != exclude_region]
    dx, pop = _delta(fx, frame, xcol, t0, t1)
    dy, _ = _delta(fx, frame, ycol, t0, t1)
    return pd.DataFrame({"dx": dx, "dy": dy, "pop": pop}).dropna().reset_index(drop=True)


def lvl_change(fx, xcol, ycol, t=2021, t1=2024):
    """Block 3: level of xcol at t vs change in ycol over t->t1."""
    lx = fx.country_panel(fx.pan_dev, xcol, [t, t1])[t]
    dy, pop = _delta(fx, fx.pan_dev, ycol, t, t1)
    return pd.DataFrame({"dx": lx, "dy": dy, "pop": pop}).dropna().reset_index(drop=True)


def usage_intensity(fx, t=2021, t1=2024):
    """E5/E5b: g20_any(t)/account_t_d(t) vs change in account_t_d; account level at t as control."""
    g = fx.country_panel(fx.pan_dev, G20, [t, t1])
    a = fx.country_panel(fx.pan_dev, ACC, [t, t1])
    return pd.DataFrame({
        "dx": g[t] / a[t],
        "dy": a[t1] - a[t],
        "c0": a[t],
        "pop": a["pop"],
    }).dropna().reset_index(drop=True)


def gap_delta(fx, col, group, hi, lo, t0=2021, t1=2024):
    """Per-country change in the (advantaged - disadvantaged) pp gap, on pan_grp."""
    g = fx.pan_grp[(fx.pan_grp["group"] == group)
                   & (fx.pan_grp["incomegroupwb24"] != "High income")]
    out = {}
    for lab in (hi, lo):
        s = g[g["group2"] == lab]
        w = s[s["year"].isin([t0, t1])].pivot_table(
            index="countrynewwb", columns="year", values=col) * 100
        out[lab] = w[t1] - w[t0] if (t0 in w.columns and t1 in w.columns) else pd.Series(dtype=float)
    return (out[hi] - out[lo]).dropna()


def gap_design(fx, xcol, gap_col, group, hi, lo, t0=2021, t1=2024):
    """Block 4: change in a margin (pan_dev, all) vs change in that/another margin's gap."""
    dx, pop = _delta(fx, fx.pan_dev, xcol, t0, t1)
    dy = gap_delta(fx, gap_col, group, hi, lo, t0, t1)
    return pd.DataFrame({"dx": dx, "dy": dy, "pop": pop}).dropna().reset_index(drop=True)


def cross_2024(fx, xcol, ycol):
    """Block 5: 2024 level cross-section (E29)."""
    x = fx.country_panel(fx.pan_dev, xcol, [2024])
    y = fx.country_panel(fx.pan_dev, ycol, [2024])
    return pd.DataFrame({"dx": x[2024], "dy": y[2024], "pop": x["pop"]}).dropna().reset_index(drop=True)


def partial_dd(fx, xcol, ycol, ctrl, t0=2021, t1=2024):
    """Block 2: change-vs-change with one change control, kept RAW (residualized at scoring time
    so the bootstrap can redo the control fit inside every draw)."""
    dx, pop = _delta(fx, fx.pan_dev, xcol, t0, t1)
    dy, _ = _delta(fx, fx.pan_dev, ycol, t0, t1)
    dc, _ = _delta(fx, fx.pan_dev, ctrl, t0, t1)
    return pd.DataFrame({"dx": dx, "dy": dy, "c0": dc, "pop": pop}).dropna().reset_index(drop=True)


# --------------------------------------------------------------------------- scoring
def score(fx, df, partial):
    """Weighted r (partial if a control column c0 is present) and its unweighted twin."""
    if partial:
        rx = _wresid(df["dx"], df[["c0"]], df["pop"])
        ry = _wresid(df["dy"], df[["c0"]], df["pop"])
        r, n = fx.weighted_corr(rx, ry, df["pop"])
        ru = _ucorr(_uresid(df["dx"], df[["c0"]]), _uresid(df["dy"], df[["c0"]]))
        return r, n, ru, rx, ry
    r, n = fx.weighted_corr(df["dx"], df["dy"], df["pop"])
    return r, n, _ucorr(df["dx"], df["dy"]), df["dx"], df["dy"]


def boot(fx, df, partial, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        d = df.iloc[rng.choice(idx, size=len(idx), replace=True)].reset_index(drop=True)
        try:
            r, _n, _ru, _a, _b = score(fx, d, partial)
        except Exception:
            continue
        if pd.notna(r):
            out.append(r)
    if len(out) < draws * 0.9:
        return np.nan, np.nan, np.nan
    a = np.asarray(out)
    tail = min((a <= 0).mean(), (a >= 0).mean())
    return (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)),
            float(max(2.0 * tail, 1.0 / draws)))


# --------------------------------------------------------------------------- the declared family
def TESTS(fx):
    D = lambda *a, **k: (lambda: dd(fx, *a, **k))
    return [
        # id, block, ledger status, r on record, builder, partial?
        ("E1",   "1 dd21", "keep-general", +0.719, D(MM, SAV), False),
        ("E2",   "1 dd21", "discard",      +0.189, D(MM, "fin24aSD_ND"), False),
        ("E7",   "1 dd21", "keep-window",  +0.541, D(SAV, "fin24sav"), False),
        ("E10",  "1 dd21", "keep-general", +0.791, D(WAGE, SAV), False),
        ("E11",  "1 dd21", "keep-general", +0.403, D(BOR, SAV), False),
        ("E12",  "1 dd21", "keep-general", +0.370, D(G20, SAV), False),
        ("E13",  "1 dd21", "keep-general", +0.435, D(FI, MM), False),
        ("E14",  "1 dd21", "keep-general", +0.600, D(MM, G20), False),
        ("E15",  "1 dd21", "discard",      +0.031, D("fin24aSD_ND", SAV), False),
        ("E16",  "1 dd21", "discard",      +0.198, D(ACC, SAV), False),
        ("E18",  "1 dd21", "discard",      +0.069, D("fin24bor", SAV), False),
        ("E19",  "1 dd21", "discard",      +0.160, D("inactive_t_d", SAV), False),
        ("E25",  "1 dd21", "keep-window",  +0.605, D(WAGE, BOR), False),
        ("E26",  "1 dd21", "discard",      +0.294, D(WAGE, "fin24aSD_ND"), False),
        ("E27",  "1 dd21", "discard",      +0.696, D("fin17c", SAV), False),
        ("E27b", "1 dd21", "secondary",    +0.531, D("fin17b", SAV), False),

        ("E5b",  "2 part", "keep-window",  -0.595, lambda: usage_intensity(fx), True),
        ("E23",  "2 part", "keep-window",  +0.509, lambda: partial_dd(fx, MM, SAV, G20), True),
        ("E24",  "2 part", "keep-window",  +0.583, lambda: partial_dd(fx, WAGE, SAV, G20), True),

        ("E5",   "3 lvl",  "discard",      -0.590,
         lambda: usage_intensity(fx).drop(columns=["c0"]), False),
        ("E9",   "3 lvl",  "discard",      -0.410, lambda: lvl_change(fx, "fing2p_acc", ACC), False),
        ("E17",  "3 lvl",  "discard",      +0.480, lambda: lvl_change(fx, SAV, SAV), False),

        ("E3",   "4 gap",  "discard",      +0.008,
         lambda: gap_design(fx, MM, ACC, "gender", "men", "women"), False),
        ("E20",  "4 gap",  "discard",      +0.179,
         lambda: gap_design(fx, SAV, SAV, "income", "richest 60%", "poorest 40%"), False),

        ("E29",  "5 xs24", "keep-window",  +0.707, lambda: cross_2024(fx, "internet", G20), False),

        ("E22a", "6 repl", "keep-window",  +0.923, D(MM, SAV, region=SSA), False),
        ("E22b", "6 repl", "keep-window",  +0.676, D(MM, SAV, exclude_region=SSA), False),
        ("E28a", "6 repl", "keep",         +0.454, D(MM, SAV, t0=2017, t1=2021), False),
        ("E28b", "6 repl", "keep",         +0.678, D(WAGE, SAV, t0=2017, t1=2021), False),
        ("E28c", "6 repl", "keep",         +0.685, D(G20, SAV, t0=2017, t1=2021), False),
        ("E30a", "6 repl", "keep",         +0.616, D(BOR, SAV, t0=2017, t1=2021), False),
        ("E30b", "6 repl", "keep",         +0.509, D(FI, MM, t0=2017, t1=2021), False),
        ("E30c", "6 repl", "keep",         +0.871, D(MM, G20, t0=2017, t1=2021), False),
    ]


def run(fx: Findex):
    print("=" * 118)
    print("E40 — LEDGER-WIDE Benjamini-Hochberg + de-weighting audit (rule B7; Program 2 items "
          "2.2 / 2.3 / 2.5)")
    print("=" * 118)

    rows = []
    for eid, block, status, r_led, build, partial in TESTS(fx):
        df = build()
        if len(df) < 10:
            print(f"  {eid:5s} SKIPPED — insufficient coverage (n={len(df)})")
            continue
        r, n, ru, rx, ry = score(fx, df, partial)
        lo, hi, pb = boot(fx, df, partial)
        g6 = fx.gate_jackknife(rx, ry, df["pop"])
        rd = g6.get("r_droptop")
        neff = _kish(df["pop"])
        rows.append({
            "id": eid, "block": block, "status": status, "r_led": r_led, "r_w": r, "r_u": ru,
            "n": int(n), "neff": neff, "lo": lo, "hi": hi, "p_boot": pb,
            "p_nom": _p_t(r, float(n)), "p_neff": _p_t(r, neff),
            "r_droptop": rd,
            "retention": (abs(rd) / abs(r)) if (rd is not None and pd.notna(rd) and abs(r) > 1e-9)
                         else np.nan,
        })

    res = pd.DataFrame(rows).set_index("id")
    res["dev"] = (res["r_w"] - res["r_led"]).abs()
    res["repro"] = res["dev"] <= 0.02

    res["bh_boot"] = benjamini_hochberg(res["p_boot"].values, Q)
    res["bh_neff"] = benjamini_hochberg(res["p_neff"].values, Q)
    res["bh_nom"] = benjamini_hochberg(res["p_nom"].values, Q)

    print(f"\nREPRODUCTION CHECK — {int(res['repro'].sum())}/{len(res)} cells reproduce the ledger "
          f"within 0.02; max deviation {res['dev'].max():.4f}")
    bad = res[~res["repro"]]
    if len(bad):
        print("  UNREPRODUCED (reported, not used in the claims):")
        print(bad[["block", "status", "r_led", "r_w", "n"]].to_string())

    print("\n" + "-" * 118)
    print("PER-TEST TABLE — r_w population-weighted, r_u UNWEIGHTED, neff = Kish effective n, "
          "BH at q=0.10 over all 33")
    print("-" * 118)
    print(f"{'id':5s} {'block':8s} {'status':13s} {'r_w':>7s} {'r_u':>7s} {'du':>7s} {'n':>4s} "
          f"{'neff':>5s} {'95% CI':>17s} {'p_boot':>7s} {'p_neff':>7s} {'ret':>5s} "
          f"{'BHb':>3s} {'BHn':>3s} {'rep':>3s}")
    for eid, r in res.iterrows():
        ci = f"[{r['lo']:+.2f},{r['hi']:+.2f}]" if pd.notna(r["lo"]) else "n/a"
        ret = f"{r['retention']:.2f}" if pd.notna(r["retention"]) else "  . "
        print(f"{eid:5s} {r['block']:8s} {r['status']:13s} {r['r_w']:+7.3f} {r['r_u']:+7.3f} "
              f"{r['r_u']-r['r_w']:+7.3f} {r['n']:4d} {r['neff']:5.1f} {ci:>17s} "
              f"{r['p_boot']:7.4f} {r['p_neff']:7.4f} {ret:>5s} "
              f"{'Y' if r['bh_boot'] else 'n':>3s} {'Y' if r['bh_neff'] else 'n':>3s} "
              f"{'ok' if r['repro'] else 'XX':>3s}")

    # ---------------------------------------------------------------- pre-registered claims
    ok = res[res["repro"]]
    kept = ok[ok["status"].str.startswith("keep")]
    disc = ok[ok["status"].isin(["discard", "secondary"])]

    a_pass = int(kept["bh_boot"].sum())
    b_pass = int((kept["r_u"].abs() >= 0.30).sum())
    boundary = disc[(disc["r_u"].abs() >= 0.30) & (disc["r_w"].abs() < 0.30)]

    print("\n" + "=" * 118)
    print("PRE-REGISTERED CLAIMS")
    print("=" * 118)
    print(f"  A  ledger-wide BH (p_boot) survival among kept rows: {a_pass}/{len(kept)} "
          f"= {a_pass/len(kept):.1%}   bar >= 50%   -> {'PASS' if a_pass >= 0.5*len(kept) else 'FAIL'}")
    print(f"  B  kept rows retaining |r_unweighted| >= 0.30:       {b_pass}/{len(kept)} "
          f"= {b_pass/len(kept):.1%}   bar >= 80%   -> {'PASS' if b_pass >= 0.8*len(kept) else 'FAIL'}")
    print(f"  C  discards with |r_u| >= 0.30 but |r_w| < 0.30:     {len(boundary)}"
          f"   bar <= 1   -> {'PASS' if len(boundary) <= 1 else 'FAIL'}")
    if len(boundary):
        print(boundary[["block", "r_w", "r_u", "n", "neff"]].to_string())

    print("\n  secondary — BH on p_neff (true degrees of freedom): "
          f"{int(ok['bh_neff'].sum())}/{len(ok)} of all tests, "
          f"{int(kept['bh_neff'].sum())}/{len(kept)} of kept rows")
    print(f"  secondary — BH on p_nominal:                        "
          f"{int(ok['bh_nom'].sum())}/{len(ok)} of all tests, "
          f"{int(kept['bh_nom'].sum())}/{len(kept)} of kept rows")
    print(f"  median Kish neff across the family: {ok['neff'].median():.1f} "
          f"(range {ok['neff'].min():.1f}-{ok['neff'].max():.1f}); median nominal n "
          f"{ok['n'].median():.0f}")
    print(f"  median |r_u| - |r_w| (de-weighting shift): "
          f"{(ok['r_u'].abs()-ok['r_w'].abs()).median():+.3f}")

    print("\n  KEPT ROWS FAILING ledger-wide BH on p_boot:")
    fail = kept[~kept["bh_boot"]]
    print("    " + (", ".join(f"{i} (p={kept.loc[i,'p_boot']:.3f})" for i in fail.index)
                    if len(fail) else "none"))
    print("  KEPT ROWS FAILING the E4 retention rule (retention < 0.5):")
    lowret = kept[kept["retention"] < 0.5]
    print("    " + (", ".join(f"{i} ({kept.loc[i,'retention']:.2f})" for i in lowret.index)
                    if len(lowret) else "none"))
    print("  KEPT ROWS FAILING the unweighted lens (|r_u| < 0.30):")
    lowu = kept[kept["r_u"].abs() < 0.30]
    print("    " + (", ".join(f"{i} ({kept.loc[i,'r_u']:+.3f})" for i in lowu.index)
                    if len(lowu) else "none"))

    print("\n  TRIPLE-CLEAN kept rows (BH on p_boot AND |r_u| >= 0.30 AND retention >= 0.5):")
    clean = kept[kept["bh_boot"] & (kept["r_u"].abs() >= 0.30) & (kept["retention"] >= 0.5)]
    print("    " + (", ".join(clean.index) if len(clean) else "none"))

    return res


if __name__ == "__main__":
    fx = Findex()
    run(fx)
