"""E58 (pre-registered 2026-08-24) — the ALL-WINDOWS promotion test of E22 (rules B14 + B8).

Parent E22 (`keep-window`, chain length 1). E22 claimed that E1 -- the co-movement of
d mobileaccount_t_d with d fin17a_17a1_d -- is a general developing-world regularity and not a
Sub-Saharan Africa story: inside SSA r_w = +0.923 (n=25), outside SSA +0.676 (n=33), 2021->2024.

DESIGN (B14-compliant, an ALL-WINDOWS design): E22's construction run over every transition
mobileaccount_t_d supports -- 2014->2017, 2017->2021, 2021->2024 -- inside each of the two
subsamples of pan_dev partitioned by regionwb24_hi (Sub-Saharan Africa vs the five other developing
regions pooled). Six cells. 2011->2014 is NOT TESTABLE (no 2011 mobileaccount_t_d) and is recorded.

REGISTERED PROMOTION CONDITION (B8: EVERY tested window, not a majority): in all six cells
r_w >= +0.30 -- the original threshold and the original POSITIVE sign (B15) -- AND G6 keeps the sign
AND the E4 magnitude rule |r_droptop| >= 0.5*|r_full| holds. Anything else leaves E22 at
`keep-window` and the failing window is recorded as FAILED, never as not attempted.

REGISTERED COVERAGE RULE: E22's declared G4 deviation min_countries=15 per subsample is carried. A
cell below 15 economies is NOT TESTABLE; any such cell means no promotion, reported as
COVERAGE-LIMITED rather than as a sign disagreement.

REGISTERED LENS RULE (B9/B11): the bar is E22's own weighted lens; the unweighted twin is computed
for all six cells. Both lenses pass all six -> `keep-general`. Weighted only -> `keep-weighted`.
Unweighted only -> `keep-unweighted`. Neither -> discard the promotion.

SECONDARY (no bar): per-window d(mobile money) terciles with mean d(saving) inside each subsample,
plus the pooled pan_dev cell in each window as the E1/E28 reference line.
"""
import numpy as np
import pandas as pd

from harness import Findex

MM = "mobileaccount_t_d"
SAV = "fin17a_17a1_d"
WINDOWS = [(2014, 2017), (2017, 2021), (2021, 2024)]
MIN_ECON = 15          # E22's declared G4 deviation, carried unchanged
BAR = 0.30
E4_RETENTION = 0.5
NDRAW = 2000
RNG = np.random.default_rng(20260824)


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def ucorr(x, y):
    m = pd.notna(x) & pd.notna(y)
    return float(np.corrcoef(x[m], y[m])[0, 1]) if m.sum() >= 3 else np.nan


def boot(x, y, w, ndraw=NDRAW):
    m = pd.notna(x) & pd.notna(y) & pd.notna(w)
    xx, yy, ww = x[m].to_numpy(), y[m].to_numpy(), w[m].to_numpy()
    n = len(xx)
    out = []
    for _ in range(ndraw):
        i = RNG.integers(0, n, n)
        xs, ys, ws = xx[i], yy[i], ww[i]
        mx, my = np.average(xs, weights=ws), np.average(ys, weights=ws)
        sx = np.sqrt(np.average((xs - mx) ** 2, weights=ws))
        sy = np.sqrt(np.average((ys - my) ** 2, weights=ws))
        if sx <= 0 or sy <= 0:
            continue
        out.append(np.average((xs - mx) * (ys - my), weights=ws) / (sx * sy))
    out = np.array(out)
    lo, hi = np.percentile(out, [2.5, 97.5])
    return float(lo), float(hi), float(min(2 * min((out <= 0).mean(), (out >= 0).mean()), 1.0))


def loo_named(fx, x, y, w):
    r0 = fx.weighted_corr(x, y, w)[0]
    nm, d = None, 0.0
    for e in x.dropna().index:
        k = [i for i in x.index if i != e]
        r1 = fx.weighted_corr(x.reindex(k), y.reindex(k), w.reindex(k))[0]
        if pd.notna(r1) and abs(r1 - r0) > abs(d):
            nm, d = e, r1 - r0
    return nm, d


def cell(fx, frame, y0, y1, pop_base):
    """One (subsample, window) cell: the identical E1/E22 construction."""
    a = frame[frame["year"] == y0].set_index("countrynewwb")
    b = frame[frame["year"] == y1].set_index("countrynewwb")
    idx = a.index.intersection(b.index)
    dmm = (b.loc[idx, MM] - a.loc[idx, MM]) * 100
    dsv = (b.loc[idx, SAV] - a.loc[idx, SAV]) * 100
    w = b.loc[idx, "pop_adult"]
    m = pd.notna(dmm) & pd.notna(dsv) & pd.notna(w)
    dmm, dsv, w = dmm[m], dsv[m], w[m]
    n = len(dmm)
    out = {"n": n, "pop_share": float(w.sum() / pop_base) if pop_base else np.nan}
    if n < MIN_ECON:
        out.update(testable=False)
        return out, dmm, dsv, w
    rw = fx.weighted_corr(dmm, dsv, w)[0]
    ru = ucorr(dmm, dsv)
    g6 = fx.gate_jackknife(dmm, dsv, w)
    lo, hi, p = boot(dmm, dsv, w)
    nm, dd = loo_named(fx, dmm, dsv, w)
    ret = abs(g6["r_droptop"]) / abs(rw) if rw else np.nan
    out.update(testable=True, rw=rw, ru=ru, neff=kish(w), g6=g6["r_droptop"],
               sign_ok=bool(np.sign(g6["r_droptop"]) == np.sign(rw)), retention=ret,
               lo=lo, hi=hi, p=p, loo="%s %+.3f" % (nm, dd))
    return out, dmm, dsv, w


def terciles(dmm, dsv):
    if len(dmm) < 6:
        return "n/a"
    q = pd.qcut(dmm.rank(method="first"), 3, labels=["low", "mid", "high"])
    return " / ".join("%s %+.1f" % (g, dsv[q == g].mean()) for g in ["low", "mid", "high"])


def main():
    fx = Findex()
    dev = fx.pan_dev
    ssa = dev[dev["regionwb24_hi"] == "Sub-Saharan Africa"]
    rest = dev[dev["regionwb24_hi"] != "Sub-Saharan Africa"]
    subs = [("SSA", ssa), ("rest-of-developing", rest), ("pooled pan_dev (reference)", dev)]

    print("=" * 104)
    print("E58 — all-windows promotion test of E22 (B14 + B8): d(mobile money) ~ d(formal saving),")
    print("      Sub-Saharan Africa vs the five other developing regions pooled")
    print("=" * 104)
    print("regions in `rest`: %s" % sorted(rest["regionwb24_hi"].dropna().unique()))
    print("2011->2014 is NOT TESTABLE: %s reporting economies in 2011 = %d\n"
          % (MM, int(dev[(dev["year"] == 2011) & dev[MM].notna()]["countrynewwb"].nunique())))

    results = {}
    for name, frame in subs:
        print("-" * 104)
        print("SUBSAMPLE: %s" % name)
        print("-" * 104)
        for (y0, y1) in WINDOWS:
            base = frame[frame["year"] == y1]["pop_adult"].sum()
            res, dmm, dsv, w = cell(fx, frame, y0, y1, base)
            key = (name, y0, y1)
            results[key] = res
            if not res["testable"]:
                print("  %d->%d  n=%2d  NOT TESTABLE (< %d economies)" % (y0, y1, res["n"], MIN_ECON))
                continue
            print("  %d->%d  n=%2d (%.1f%% of subsample adult pop)  neff %5.1f   r_w %+.3f  r_u %+.3f"
                  % (y0, y1, res["n"], 100 * res["pop_share"], res["neff"], res["rw"], res["ru"]))
            print("           G6 %+.3f (sign %s, E4 retention %.2f)   boot [%+.3f,%+.3f] p_boot %.3f   largest LOO %s"
                  % (res["g6"], "kept" if res["sign_ok"] else "LOST", res["retention"],
                     res["lo"], res["hi"], res["p"], res["loo"]))
            print("           d(mobile money) terciles -> mean d(saving): %s" % terciles(dmm, dsv))
        print()

    print("=" * 104)
    print("REGISTERED PROMOTION CONDITION (B8: every one of the six cells)")
    print("=" * 104)
    cells = [k for k in results if k[0] in ("SSA", "rest-of-developing")]
    not_testable = [k for k in cells if not results[k]["testable"]]
    fails_w, fails_u = [], []
    for k in sorted(cells):
        r = results[k]
        if not r["testable"]:
            continue
        ok_w = (r["rw"] >= BAR) and r["sign_ok"] and (r["retention"] >= E4_RETENTION)
        ok_u = r["ru"] >= BAR
        if not ok_w:
            fails_w.append(k)
        if not ok_u:
            fails_u.append(k)
        print("  %-20s %d->%d   weighted bar %s (r_w %+.3f, G6 sign %s, retention %.2f)   unweighted bar %s (r_u %+.3f)"
              % (k[0], k[1], k[2], "PASS" if ok_w else "FAIL", r["rw"],
                 "kept" if r["sign_ok"] else "LOST", r["retention"],
                 "PASS" if ok_u else "FAIL", r["ru"]))
    print("\n  not testable: %s" % (not_testable or "none"))
    print("  weighted-lens failures:   %s" % (sorted(fails_w) or "none"))
    print("  unweighted-lens failures: %s" % (sorted(fails_u) or "none"))

    if not_testable:
        verdict = "NO PROMOTION — COVERAGE-LIMITED (a registered cell is not testable)"
    elif not fails_w and not fails_u:
        verdict = "PROMOTE E22 to `keep-general` (both lenses pass all six cells)"
    elif not fails_w:
        verdict = "PROMOTE as `keep-weighted` (weighted lens passes all six, unweighted does not)"
    elif not fails_u:
        verdict = "PROMOTE as `keep-unweighted` (unweighted lens passes all six, weighted does not)"
    else:
        verdict = "DISCARD the promotion — E22 stays `keep-window`; the failing windows are recorded as FAILED"
    print("\n  ==> %s" % verdict)


if __name__ == "__main__":
    main()
