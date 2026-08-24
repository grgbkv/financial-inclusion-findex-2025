"""E57x / E57 (pre-registered 2026-08-24) — the `fin22` borrowing-sources module.

E57x  PART A, EXPLORATORY (peek rule): mapping pass. Weighted developing-panel level by wave and
      economy count for every `fin22*` country column. Meanings INFERRED from levels/coverage only
      (no questionnaire in the repo, HARNESS_V2_NOTES 5-6).

E57   PART B, the registered primary: the four-way orientation screen against `g20_any` in the 2024
      developing-panel cross-section.
          restatement |r|>=0.80 | aligned +0.30<=r<0.80 | counter-moving r<=-0.30 | independent |r|<0.30
          both lenses must agree, else `mixed-lens`.
      Eligibility declared in advance: >=3 waves at >=70 developing-panel economies.
      Excluded in advance: `fin22a_22a1_22g_d` (declared composite / registered headline),
      `fin22h_s` (`_s` conditional column, documented unusable).
      KEEP: >=1 item counter-moving on BOTH lenses, G6 sign intact, 2,000-draw bootstrap interval
      excluding zero, AND surviving BH at q=0.10 over this module's own screen family.
      REGISTERED SIGN: NEGATIVE.
      Denominator diagnostic (agenda 9.1, U26 wording): all-adult r, conditional-rate r
      (item / borrow_any_t_d) and the base factor r(borrow_any_t_d, anchor).
      SECONDARY (no bar): the same screen against `account_t_d`.
"""
import numpy as np
import pandas as pd

from harness import Findex, YEARS

ANCHOR = "g20_any"
ANCHOR2 = "account_t_d"
BASE = "borrow_any_t_d"
MIN_ECON_PER_WAVE = 70
MIN_WAVES = 3
EXCLUDE = {"fin22a_22a1_22g_d", "fin22h_s"}
NDRAW = 2000
Q = 0.10
RNG = np.random.default_rng(20260824)


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def wcorr(x, y, w):
    return Findex.weighted_corr(x, y, w)[0]


def ucorr(x, y):
    m = pd.notna(x) & pd.notna(y)
    return float(np.corrcoef(x[m], y[m])[0, 1]) if m.sum() >= 10 else np.nan


def classify(rw, ru):
    def one(r):
        if pd.isna(r):
            return "na"
        if abs(r) >= 0.80:
            return "restatement"
        if r >= 0.30:
            return "aligned"
        if r <= -0.30:
            return "counter-moving"
        return "independent"
    a, b = one(rw), one(ru)
    return a if a == b else "mixed-lens(%s/%s)" % (a, b)


def boot(x, y, w, ndraw=NDRAW):
    """Percentile interval and p_boot for the weighted correlation; resample economies."""
    m = pd.notna(x) & pd.notna(y) & pd.notna(w)
    xx, yy, ww = x[m].to_numpy(), y[m].to_numpy(), w[m].to_numpy()
    n = len(xx)
    out = []
    for _ in range(ndraw):
        idx = RNG.integers(0, n, n)
        xs, ys, ws = xx[idx], yy[idx], ww[idx]
        if np.average(ws) <= 0:
            continue
        mx, my = np.average(xs, weights=ws), np.average(ys, weights=ws)
        sx = np.sqrt(np.average((xs - mx) ** 2, weights=ws))
        sy = np.sqrt(np.average((ys - my) ** 2, weights=ws))
        if sx <= 0 or sy <= 0:
            continue
        out.append(np.average((xs - mx) * (ys - my), weights=ws) / (sx * sy))
    out = np.array(out)
    lo, hi = np.percentile(out, [2.5, 97.5])
    p = 2 * min((out <= 0).mean(), (out >= 0).mean())
    return float(lo), float(hi), float(min(p, 1.0))


def loo_named(x, y, w):
    """B12: the largest single leave-one-out change in r_w, with the economy named."""
    r0 = wcorr(x, y, w)
    best_name, best_d = None, 0.0
    for e in x.dropna().index:
        keep = [i for i in x.index if i != e]
        r1 = wcorr(x.reindex(keep), y.reindex(keep), w.reindex(keep))
        if pd.notna(r1) and abs(r1 - r0) > abs(best_d):
            best_name, best_d = e, r1 - r0
    return best_name, best_d


def bh(pvals, q=Q):
    """Benjamini-Hochberg: returns the set of indices rejected at level q."""
    order = np.argsort(pvals)
    m = len(pvals)
    rejected, kmax = set(), -1
    for rank, i in enumerate(order, start=1):
        if pvals[i] <= q * rank / m:
            kmax = rank
    if kmax > 0:
        rejected = set(order[:kmax])
    return rejected, [(i, pvals[i], q * (list(order).index(i) + 1) / m) for i in order]


def main():
    fx = Findex()
    dev = fx.pan_dev
    cols = sorted([c for c in dev.columns if c.startswith("fin22")])

    print("=" * 100)
    print("E57x — EXPLORATORY mapping pass: the `fin22` borrowing-sources module (developing panel)")
    print("=" * 100)
    print("%-24s %s" % ("column", "  ".join("%12s" % y for y in YEARS)))
    cover = {}
    for c in cols:
        s = fx.series(dev, c, YEARS)
        counts = {y: int(dev[(dev["year"] == y) & dev[c].notna()]["countrynewwb"].nunique())
                  for y in YEARS}
        cover[c] = counts
        cells = []
        for y in YEARS:
            cells.append("%6s/%3d" % ("%.1f" % s[y] if y in s.index else "--", counts[y]))
        print("%-24s %s" % (c, "  ".join("%12s" % v for v in cells)))
    print("\n(cell = weighted developing-panel level pp / number of economies reporting)")

    for c in cols:
        ok_waves = sum(1 for y in YEARS if cover[c][y] >= MIN_ECON_PER_WAVE)
        print("  %-24s waves at >=%d economies: %d   excluded-in-advance: %s"
              % (c, MIN_ECON_PER_WAVE, ok_waves, c in EXCLUDE))

    eligible = [c for c in cols
                if c not in EXCLUDE
                and sum(1 for y in YEARS if cover[c][y] >= MIN_ECON_PER_WAVE) >= MIN_WAVES]
    print("\nELIGIBLE SCREEN FAMILY (>=%d waves at >=%d economies, exclusions applied): %s"
          % (MIN_WAVES, MIN_ECON_PER_WAVE, eligible))

    # -------------------------------------------------------------- E57 the screen
    d24 = dev[dev["year"] == 2024].set_index("countrynewwb")
    w = d24["pop_adult"]

    for anchor, tag in [(ANCHOR, "PRIMARY vs g20_any"), (ANCHOR2, "SECONDARY vs account_t_d")]:
        print("\n" + "=" * 100)
        print("E57 — four-way orientation screen, 2024 developing-panel cross-section (%s)" % tag)
        print("=" * 100)
        a = d24[anchor] * 100
        base = d24[BASE] * 100
        rows, pv = [], []
        for c in eligible:
            x = d24[c] * 100
            m = pd.notna(x) & pd.notna(a) & pd.notna(w)
            n = int(m.sum())
            rw, ru = wcorr(x, a, w), ucorr(x, a)
            g6 = fx.gate_jackknife(x, a, w)
            lo, hi, p = boot(x, a, w)
            nm, dd = loo_named(x, a, w)
            # denominator diagnostic (agenda 9.1, U26 wording)
            cond = (x / base) * 100
            rw_c, ru_c = wcorr(cond, a, w), ucorr(cond, a)
            rows.append(dict(col=c, n=n, neff=kish(w[m]), rw=rw, ru=ru,
                             cls=classify(rw, ru), g6=g6["r_droptop"], lo=lo, hi=hi, p=p,
                             loo="%s %+.3f" % (nm, dd), rw_c=rw_c, ru_c=ru_c,
                             cls_c=classify(rw_c, ru_c)))
            pv.append(p)
        rej, table = bh(np.array(pv))
        print("%-12s %4s %6s  %7s %7s  %-28s %7s  %-20s %7s  %-26s"
              % ("item", "n", "neff", "r_w", "r_u", "class (all-adult denom)", "G6", "boot [2.5,97.5]",
                 "p_boot", "conditional-rate denom"))
        for i, r in enumerate(rows):
            print("%-12s %4d %6.1f  %+7.3f %+7.3f  %-28s %+7.3f  [%+.3f,%+.3f] %7.3f  %+.3f/%+.3f %-18s"
                  % (r["col"], r["n"], r["neff"], r["rw"], r["ru"], r["cls"], r["g6"],
                     r["lo"], r["hi"], r["p"], r["rw_c"], r["ru_c"], r["cls_c"]))
            print("%-12s     largest LOO (B12): %s" % ("", r["loo"]))
        print("\nBH at q=%.2f over this module's own %d-test family: rejects %d of %d  -> %s"
              % (Q, len(pv), len(rej), len(pv),
                 ", ".join(rows[i]["col"] for i in sorted(rej)) or "none"))
        for i, p, crit in table:
            print("   %-12s p_boot %.4f  vs critical %.4f  %s"
                  % (rows[i]["col"], p, crit, "REJECT" if i in rej else "-"))

        # the base factor, agenda 9.1's analogue of U25's complement factor
        print("\nBASE FACTOR r(%s, %s): weighted %+.3f / unweighted %+.3f"
              % (BASE, anchor, wcorr(base, a, w), ucorr(base, a)))

        cm = [r for r in rows if r["cls"] == "counter-moving"]
        print("\nREGISTERED KEEP CONDITION (%s): counter-moving on BOTH lenses = %d item(s) -> %s"
              % (tag, len(cm), [r["col"] for r in cm] or "NONE"))
    return fx


def depths(fx, d24, w, col, anchor, bar=0.30):
    """B21, computed AFTER the registered primary and carrying no verdict rule:
    fragility depth  = fewest greedy removals of the largest-population economies that drive |r_w|
                       BELOW the bar; ascent depth = fewest greedy removals that drive |r_u| ABOVE it.
    Economies named in removal order."""
    x, a = d24[col] * 100, d24[anchor] * 100
    order = w.sort_values(ascending=False).index.tolist()

    keep = list(x.dropna().index)
    frag = []
    for e in order:
        if e not in keep:
            continue
        r = wcorr(x.reindex(keep), a.reindex(keep), w.reindex(keep))
        if pd.isna(r) or abs(r) < bar:
            break
        keep.remove(e)
        frag.append(e)
        r2 = wcorr(x.reindex(keep), a.reindex(keep), w.reindex(keep))
        if pd.isna(r2) or abs(r2) < bar:
            break

    keep2 = list(x.dropna().index)
    asc = []
    for _ in range(len(keep2)):
        r = ucorr(x.reindex(keep2), a.reindex(keep2))
        if pd.notna(r) and abs(r) >= bar:
            break
        best, bestr = None, abs(r) if pd.notna(r) else 0.0
        for e in keep2:
            k = [i for i in keep2 if i != e]
            rr = ucorr(x.reindex(k), a.reindex(k))
            if pd.notna(rr) and abs(rr) > bestr:
                best, bestr = e, abs(rr)
        if best is None:
            break
        keep2.remove(best)
        asc.append(best)
    r_end_w = wcorr(x.reindex(keep), a.reindex(keep), w.reindex(keep))
    r_end_u = ucorr(x.reindex(keep2), a.reindex(keep2))
    return frag, r_end_w, asc, r_end_u


def post_primary(fx):
    """Diagnostics added AFTER the registered primary printed. No bar, no verdict rule."""
    dev = fx.pan_dev
    d24 = dev[dev["year"] == 2024].set_index("countrynewwb")
    w = d24["pop_adult"]
    print("\n" + "=" * 100)
    print("POST-PRIMARY DIAGNOSTICS (no bar, no verdict rule) — B21 depths and G4 coverage")
    print("=" * 100)
    for col in ["fin22d", "fin22b"]:
        for anchor in [ANCHOR]:
            frag, rw_end, asc, ru_end = depths(fx, d24, w, col, anchor)
            print("%-8s vs %-12s fragility depth %d  [%s]  -> r_w %+.3f"
                  % (col, anchor, len(frag), ", ".join(frag) or "-", rw_end))
            print("%-8s %-15s ascent   depth %d  [%s]  -> r_u %+.3f"
                  % ("", "", len(asc), ", ".join(asc) or "-", ru_end))
    for col in ["fin22d", ANCHOR, BASE]:
        print("G4 %-14s %s" % (col, fx.gate_coverage(dev, col, 2024)))
    print("G3: every fin22 item is an UNREGISTERED narrow variant (declared in the pre-registration).")
    print("G5: no official aggregate series for a cross-sectional correlation — n/a.")
    print("E4 magnitude rule on fin22d: |r_droptop|/|r_full| = %.3f" % (0.358 / 0.557))


if __name__ == "__main__":
    fx_out = main()
    post_primary(fx_out)
