"""E59 (pre-registered 2026-08-26) — the ALL-WINDOWS delta->delta on `fin22d` (agenda item 11.2).

Parent E57 (`keep`, chain length 1). E57 found a THIRD counter-moving country margin and the first
that is not a payment-mode item: r(fin22d, g20_any) = -0.557 weighted / -0.400 unweighted in the
2024 developing-panel cross-section, surviving G6, a bootstrap interval excluding zero and BH over
its own six-item family. That is a CROSS-SECTIONAL COMPOSITION statement; E48/E50 is the standing
proof that cross-section and delta come apart. This experiment asks whether the counter-movement is
also a WITHIN-economy dynamic.

DESIGN (B14-compliant, ALL-WINDOWS): r(d fin22d, d g20_any) over every transition both items
support -- 2014->2017, 2017->2021, 2021->2024. 2011->2014 is NOT TESTABLE (module empty in 2011).

REGISTERED SIGN (B15): NEGATIVE. A cell at r >= +0.30 is the OPPOSITE pattern, not partial support.

REGISTERED KEEP CONDITION (B8's every-window form): in ALL THREE windows r <= -0.30 on BOTH lenses,
G6 keeps the sign, the E4 magnitude rule |r_droptop| >= 0.5*|r_full| holds, and the 2,000-draw
country bootstrap interval excludes zero. Weighted lens only -> `keep-weighted`; unweighted only ->
`keep-unweighted`; neither -> DISCARD the delta claim, leaving E57 exactly as it stands.

REGISTERED DENOMINATOR RULE (B20, declared before the run): the PRIMARY runs on a SINGLE FIXED
economy set -- economies reporting both fin22d and g20_any in ALL FOUR waves 2014/17/21/24. The
per-window pairwise-complete set is printed beside it; where they disagree the fixed set is the
primary and the difference is reported as reporting-set movement. Dropped economies are NAMED.

SECONDARY 1 (no bar): the 2014->2024 long difference with B16's intermediate wave levels.
SECONDARY 2 (no bar): the same all-windows design against d account_t_d (the E47/E57 anchor split).
SECONDARY 3 (no bar): agenda item 12.2 -- the denominator re-check owed on fin31d and fin34c.
  Declared bases: fin32 (wage receipt) for fin34c; for fin31d the only candidate base IS the anchor
  g20_any, so the conditional twin is NOT IDENTIFIED and is reported as such, never computed
  circularly. The published `_s` twins are NOT used (HARNESS_V2_NOTES item 10: different items).
"""
import numpy as np
import pandas as pd

from harness import Findex

ITEM = "fin22d"
ANCHOR = "g20_any"
ACCESS = "account_t_d"
WAVES = [2014, 2017, 2021, 2024]
WINDOWS = [(2014, 2017), (2017, 2021), (2021, 2024)]
BAR = -0.30
E4_RETENTION = 0.5
NDRAW = 2000
RNG = np.random.default_rng(20260826)


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


def depths(fx, x, y, w, bar=BAR):
    """B21: fragility depth (greedy removals of LARGEST economies driving r_w above the bar, i.e.
    out of the counter-moving region) and ascent depth (greedy removals driving r_u below the bar,
    i.e. into it). Economies named. Returns two (depth, [names]) pairs; depth 0 = already there."""
    def greedy(weighted, want_below):
        idx = list(x.dropna().index)
        names = []
        for step in range(len(idx)):
            cur = (fx.weighted_corr(x.reindex(idx), y.reindex(idx), w.reindex(idx))[0]
                   if weighted else ucorr(x.reindex(idx), y.reindex(idx)))
            if pd.isna(cur):
                return None, names
            if (cur <= bar) == want_below:
                return step, names
            best, bestv = None, None
            for e in idx:
                k = [i for i in idx if i != e]
                v = (fx.weighted_corr(x.reindex(k), y.reindex(k), w.reindex(k))[0]
                     if weighted else ucorr(x.reindex(k), y.reindex(k)))
                if pd.isna(v):
                    continue
                if bestv is None or ((v <= bestv) if want_below else (v >= bestv)):
                    best, bestv = e, v
            if best is None:
                return None, names
            idx.remove(best)
            names.append(best)
        return None, names
    frag = greedy(True, False)    # weighted: how many removals until r_w is NOT past the bar
    asc = greedy(False, True)     # unweighted: how many removals until r_u IS past the bar
    return frag, asc


def cell(fx, panel, y0, y1, item, anchor, label):
    """One window on a given (already fixed or pairwise) economy set."""
    di = panel[(item, y1)] - panel[(item, y0)]
    da = panel[(anchor, y1)] - panel[(anchor, y0)]
    w = panel[("pop", "pop")]
    m = pd.notna(di) & pd.notna(da) & pd.notna(w)
    di, da, w = di[m], da[m], w[m]
    n = len(di)
    if n < 10:
        return {"label": label, "n": n, "testable": False}
    rw = fx.weighted_corr(di, da, w)[0]
    ru = ucorr(di, da)
    g6 = fx.gate_jackknife(di, da, w)
    lo, hi, p = boot(di, da, w)
    nm, dd = loo_named(fx, di, da, w)
    ret = abs(g6["r_droptop"]) / abs(rw) if rw else np.nan
    return {"label": label, "n": n, "testable": True, "rw": rw, "ru": ru, "neff": kish(w),
            "g6": g6["r_droptop"], "sign_ok": bool(np.sign(g6["r_droptop"]) == np.sign(rw)),
            "retention": ret, "lo": lo, "hi": hi, "p": p, "loo": "%s %+.3f" % (nm, dd),
            "x": di, "y": da, "w": w}


def wide(fx, frame, cols, waves=WAVES):
    """Wide per-economy table of cols x waves (pp), plus 2024 adult population."""
    sub = frame[frame["year"].isin(waves)]
    out = {}
    for c in cols:
        p = sub.pivot_table(index="countrynewwb", columns="year", values=c) * 100
        for y in waves:
            out[(c, y)] = p[y] if y in p.columns else np.nan
    d = pd.DataFrame(out)
    d[("pop", "pop")] = frame[frame["year"] == 2024].set_index("countrynewwb")["pop_adult"]
    return d


def show(r, extra=""):
    if not r["testable"]:
        print("  %-28s n=%2d  NOT TESTABLE" % (r["label"], r["n"]))
        return
    print("  %-28s n=%2d  neff %5.1f   r_w %+.3f  r_u %+.3f   G6 %+.3f (sign %s, E4 ret %.2f)"
          % (r["label"], r["n"], r["neff"], r["rw"], r["ru"], r["g6"],
             "kept" if r["sign_ok"] else "LOST", r["retention"]))
    print("  %-28s boot [%+.3f,%+.3f]  p_boot %.3f   largest LOO %s%s"
          % ("", r["lo"], r["hi"], r["p"], r["loo"], extra))


def main():
    fx = Findex()
    dev = fx.pan_dev
    print("=" * 108)
    print("E59 — all-windows delta->delta on `fin22d` (agenda item 11.2). Parent E57.")
    print("      registered sign NEGATIVE; bar r <= -0.30 in ALL THREE windows on BOTH lenses")
    print("=" * 108)

    # ------------------------------------------------ B20: the fixed economy set, declared first
    w_all = wide(fx, dev, [ITEM, ANCHOR, ACCESS])
    both = w_all[[(ITEM, y) for y in WAVES] + [(ANCHOR, y) for y in WAVES]]
    fixed = both.dropna().index
    print("\nB20 DENOMINATOR (declared before the run: economies reporting BOTH items in ALL FOUR waves)")
    for y in WAVES:
        n_i = int(w_all[(ITEM, y)].notna().sum())
        n_a = int(w_all[(ANCHOR, y)].notna().sum())
        print("  %d: %s reported by %d economies, %s by %d" % (y, ITEM, n_i, ANCHOR, n_a))
    pop = w_all[("pop", "pop")]
    ever = both.notna().any(axis=1)
    dropped = sorted(set(w_all.index[ever]) - set(fixed))
    dshare = pop.reindex(dropped).sum() / pop.reindex(w_all.index[ever]).sum()
    print("  FIXED SET: %d economies (of %d ever reporting). Dropped %d = %.1f%% of that adult population."
          % (len(fixed), int(ever.sum()), len(dropped), 100 * dshare))
    print("  dropped economies NAMED: %s" % (", ".join(dropped) if dropped else "none"))
    pf = w_all.loc[fixed]

    # ------------------------------------------------------------------ B16: the wave path first
    print("\nB16 PATH (population-weighted developing-panel level, pp, on the FIXED %d-economy set)"
          % len(fixed))
    for c in [ITEM, ANCHOR, ACCESS]:
        lv = [float(np.average(pf[(c, y)], weights=pf[("pop", "pop")])) for y in WAVES]
        mono = "monotone rising" if all(b > a for a, b in zip(lv, lv[1:])) else "NON-MONOTONE"
        print("  %-12s %s   [%s]" % (c, "  ".join("%d %5.1f" % (y, v) for y, v in zip(WAVES, lv)), mono))

    # --------------------------------------------------------------------------- the PRIMARY
    print("\n" + "=" * 108)
    print("PRIMARY — r(d %s, d %s), all three windows, FIXED economy set" % (ITEM, ANCHOR))
    print("=" * 108)
    primary = {}
    for (y0, y1) in WINDOWS:
        r = cell(fx, pf, y0, y1, ITEM, ANCHOR, "%d->%d fixed set" % (y0, y1))
        primary[(y0, y1)] = r
        show(r)
        rp = cell(fx, w_all, y0, y1, ITEM, ANCHOR, "%d->%d pairwise" % (y0, y1))
        if rp["testable"]:
            print("  %-28s n=%2d  r_w %+.3f  r_u %+.3f   [reporting-set movement vs fixed: "
                  "dr_w %+.3f, dr_u %+.3f]"
                  % (rp["label"], rp["n"], rp["rw"], rp["ru"], rp["rw"] - r["rw"], rp["ru"] - r["ru"]))
        print()

    print("REGISTERED KEEP CONDITION (all three windows, both lenses)")
    fails_w, fails_u = [], []
    for k in WINDOWS:
        r = primary[k]
        ok_w = (r["rw"] <= BAR) and r["sign_ok"] and (r["retention"] >= E4_RETENTION) and (r["hi"] < 0)
        ok_u = r["ru"] <= BAR
        (fails_w if not ok_w else []).append(k) if not ok_w else None
        (fails_u if not ok_u else []).append(k) if not ok_u else None
        print("  %d->%d  weighted bar %s (r_w %+.3f, sign %s, ret %.2f, boot excl 0 %s)   "
              "unweighted bar %s (r_u %+.3f)"
              % (k[0], k[1], "PASS" if ok_w else "FAIL", r["rw"], "kept" if r["sign_ok"] else "LOST",
                 r["retention"], "yes" if r["hi"] < 0 else "no", "PASS" if ok_u else "FAIL", r["ru"]))
    if not fails_w and not fails_u:
        verdict = "KEEP the delta claim (both lenses clear all three windows)"
    elif not fails_w:
        verdict = "KEEP-WEIGHTED (weighted lens clears all three, unweighted does not)"
    elif not fails_u:
        verdict = "KEEP-UNWEIGHTED (unweighted lens clears all three, weighted does not)"
    else:
        verdict = ("DISCARD the delta claim — E57's CROSS-SECTIONAL keep stands unchanged "
                   "(registered in advance; E48/E50 precedent)")
    print("\n  weighted-lens failures:   %s" % (fails_w or "none"))
    print("  unweighted-lens failures: %s" % (fails_u or "none"))
    print("\n  ==> %s" % verdict)

    # B21 depths where the lenses disagree against the bar
    print("\nB21 DEPTHS (computed only where the two lenses disagree against the bar)")
    any_disagree = False
    for k in WINDOWS:
        r = primary[k]
        if (r["rw"] <= BAR) == (r["ru"] <= BAR):
            continue
        any_disagree = True
        frag, asc = depths(fx, r["x"], r["y"], r["w"])
        print("  %d->%d  fragility depth %s %s" % (k[0], k[1], frag[0], frag[1][:6] or ""))
        print("         ascent depth    %s %s" % (asc[0], asc[1][:6] or ""))
    if not any_disagree:
        print("  no window has the lenses disagreeing against the bar — not computed (as registered)")

    # ------------------------------------------------------------------- SECONDARY 1: long diff
    print("\n" + "=" * 108)
    print("SECONDARY 1 (no bar) — the 2014->2024 long difference, fixed set")
    print("=" * 108)
    show(cell(fx, pf, 2014, 2024, ITEM, ANCHOR, "2014->2024 fixed set"))

    # ------------------------------------------------------------------ SECONDARY 2: anchor split
    print("\n" + "=" * 108)
    print("SECONDARY 2 (no bar) — the same design against d %s (E47/E57 anchor distinction)" % ACCESS)
    print("=" * 108)
    fx2 = w_all[[(ITEM, y) for y in WAVES] + [(ACCESS, y) for y in WAVES]].dropna().index
    pf2 = w_all.loc[fx2]
    print("  fixed set for this pair: %d economies" % len(fx2))
    for (y0, y1) in WINDOWS:
        show(cell(fx, pf2, y0, y1, ITEM, ACCESS, "%d->%d" % (y0, y1)))
    show(cell(fx, pf2, 2014, 2024, ITEM, ACCESS, "2014->2024"))

    # ------------------------------------------------ SECONDARY 3: agenda item 12.2 denominators
    print("\n" + "=" * 108)
    print("SECONDARY 3 (no bar) — agenda item 12.2: the denominator re-check owed on fin31d, fin34c")
    print("=" * 108)
    d24 = dev[dev["year"] == 2024].set_index("countrynewwb")
    w24 = d24["pop_adult"]
    anch = d24[ANCHOR] * 100
    for item, base in [("fin34c", "fin32"), ("fin31d", None)]:
        x = d24[item] * 100
        m = pd.notna(x) & pd.notna(anch) & pd.notna(w24)
        rw = fx.weighted_corr(x[m], anch[m], w24[m])[0]
        ru = ucorr(x[m], anch[m])
        print("\n  %s  all-adult denominator (as published): r_w %+.3f  r_u %+.3f   n=%d"
              % (item, rw, ru, int(m.sum())))
        if base is None:
            print("       conditional twin: NOT IDENTIFIED — the only candidate base in the repo is the")
            print("       anchor `%s` itself, so the conditional correlation would be circular. Declared" % ANCHOR)
            print("       in the pre-registration; NOT computed. (`fin31d_s` is a different item, notes 10.)")
            continue
        b = d24[base] * 100
        cond = (x / b).where(b > 0) * 100
        m2 = pd.notna(cond) & pd.notna(anch) & pd.notna(w24)
        rw2 = fx.weighted_corr(cond[m2], anch[m2], w24[m2])[0]
        ru2 = ucorr(cond[m2], anch[m2])
        mb = pd.notna(b) & pd.notna(anch) & pd.notna(w24)
        rwb = fx.weighted_corr(b[mb], anch[mb], w24[mb])[0]
        rub = ucorr(b[mb], anch[mb])
        moved = ((rw <= -0.30) != (rw2 <= -0.30)) or ((ru <= -0.30) != (ru2 <= -0.30))
        print("       conditional on `%s`:            r_w %+.3f  r_u %+.3f   n=%d" % (base, rw2, ru2, int(m2.sum())))
        print("       base factor r(%s, %s):        r_w %+.3f  r_u %+.3f" % (base, ANCHOR, rwb, rub))
        print("       => classification %s between denominators"
              % ("MOVES — denominator-driven" if moved else "does NOT move"))


if __name__ == "__main__":
    main()
