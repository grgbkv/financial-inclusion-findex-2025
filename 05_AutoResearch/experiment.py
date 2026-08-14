"""E45 (pre-registered 2026-08-15): is the digital-payment DETAIL module (`fin31`) a restatement of
the headline, or does it carry independent variation?

New ground — the cycle's B2 cell. `fin31` is 9 columns x four waves x ~77 developing economies with
ZERO ledger mentions: the best-covered untouched country module left. Parent: **E41** (the
`merchant_pay` untouched-module insert), first descendant on that line.

WHY. `dig_acc` was pre-checked in the previous cycle and correlates +0.963 with `g20_any` in the 2024
cross-section — an untouched module that is not new ground at all. Before the loop spends a cycle
building a hypothesis on `fin31`, it should establish whether the module is in the same position.
The module has no questionnaire in the repo, so the mandatory mapping pass applies.

PART A — MAPPING PASS, logged as EXPLORATORY under the peek rule. Per-wave developing-panel country
counts and population-weighted levels per column, plus the composites against their parts. Labels are
INFERRED from the numbers, documented as inferred and not authoritative. No keep hangs on Part A.

PART B — THE REGISTERED SCREENING CLAIM (written before any fin31 value was computed):
"the `fin31` module is a restatement of the digital-payment headline and carries no independent
variation." Qualifying items: fin31 columns with >= 30 developing-panel economies in BOTH 2021 and
2024. Per item, two statistics under both lenses (B9):
  r_level = corr(item 2024 level, g20_any 2024 level)
  r_delta = corr(item delta 2021->24, g20_any delta 2021->24)
  KEEP the redundancy claim if median |r_level| across qualifying items >= 0.80 on BOTH lenses AND
    no item qualifies as independent.
  An item is INDEPENDENT if |r_level| < 0.50 AND |r_delta| < 0.30 on BOTH lenses.
  DISCARD otherwise, NAMING the independent items as new-ground targets for a later cycle — which is
    the useful outcome either way.

B6/B9/B10/B12: 2,000-draw country bootstrap on every correlation and on the median; Kish neff beside
every nominal n with no significance language on nominal n; unweighted twin beside every weighted
statistic and the verdict labelled with the lens; G6 drop-top-5 on every correlation; and the largest
leave-one-economy-out effect, with the economy NAMED, for the single most important item.

DECLARED. Cross-sectional levels and one delta window. `g20_any` is the declared headline variant of
the digital-payment concept under G3 and every fin31 item is by construction a narrow variant of the
same concept — that overlap IS the hypothesis, not a confound. Nothing here is causal. A high
correlation between an item and the headline is a statement about measurement redundancy, not about
behaviour.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 45
MIN_C = 30            # qualifying coverage, economies, in BOTH 2021 and 2024
RED_BAR = 0.80        # median |r_level| for the redundancy claim
IND_LEVEL = 0.50      # independence: |r_level| below this ...
IND_DELTA = 0.30      # ... and |r_delta| below this, on BOTH lenses

HEAD = "g20_any"
WAVES = [2014, 2017, 2021, 2024]
WINDOW = (2021, 2024)
FIN31 = ["fin31a_31b", "fin31a", "fin31b", "fin31c", "fin31d",
         "fin31a_31b_s", "fin31a_s", "fin31b_s", "fin31d_s"]


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def corr(x, y, w=None):
    """Weighted (w given) or unweighted correlation over the common non-missing support."""
    m = pd.notna(x) & pd.notna(y)
    if w is not None:
        m &= pd.notna(w)
    x, y = x[m], y[m]
    if len(x) < 10:
        return np.nan, int(len(x))
    ww = np.ones(len(x)) if w is None else np.asarray(w[m], dtype=float)
    mx, my = np.average(x, weights=ww), np.average(y, weights=ww)
    sx = np.sqrt(np.average((x - mx) ** 2, weights=ww))
    sy = np.sqrt(np.average((y - my) ** 2, weights=ww))
    if sx == 0 or sy == 0:
        return np.nan, int(len(x))
    return float(np.average((x - mx) * (y - my), weights=ww) / (sx * sy)), int(len(x))


def boot_ci(df, fn, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        v = fn(df.iloc[rng.choice(idx, size=len(idx), replace=True)])
        if pd.notna(v) and np.isfinite(v):
            out.append(v)
    if len(out) < draws // 4:
        return np.nan, np.nan, np.nan
    a = np.asarray(out)
    p_boot = 2 * min((a <= 0).mean(), (a >= 0).mean())
    return float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)), float(p_boot)


def build(fx):
    """Per-economy table: fin31 levels/deltas, headline levels/deltas, population weight."""
    dev = fx.pan_dev
    cols = FIN31 + [HEAD]
    d = dev[dev["year"].isin(WAVES)]
    tab = {}
    for c in cols:
        w = d.pivot_table(index="countrynewwb", columns="year", values=c) * 100
        for y in WAVES:
            tab[(c, y)] = w[y] if y in w.columns else pd.Series(dtype=float)
    out = pd.DataFrame(tab)
    pop = dev[dev["year"] == 2024].set_index("countrynewwb")["pop_adult"]
    out[("pop", 0)] = pop.reindex(out.index)
    return out


def part_a(fx, tab):
    print("=" * 122)
    print("PART A — MAPPING PASS (EXPLORATORY, peek rule; labels INFERRED, not authoritative; "
          "no keep hangs on this)")
    print("=" * 122)
    print(f"  {'column':14s} " + " ".join(f"{y:>18d}" for y in WAVES))
    print(f"  {'':14s} " + " ".join(f"{'n / wtd level pp':>18s}" for _ in WAVES))
    for c in FIN31 + [HEAD]:
        cells = []
        for y in WAVES:
            s = tab[(c, y)].dropna()
            if s.empty:
                cells.append(f"{'—':>18s}")
                continue
            w = tab[("pop", 0)].reindex(s.index)
            m = pd.notna(w)
            lvl = float(np.average(s[m], weights=w[m])) if m.any() else np.nan
            cells.append(f"{len(s):5d} /{lvl:11.1f}")
        print(f"  {c:14s} " + " ".join(cells))

    print("\n  composite relations, 2024 (developing panel, population-weighted levels):")
    for a, parts in [("fin31a_31b", ["fin31a", "fin31b"]),
                     ("fin31a_31b_s", ["fin31a_s", "fin31b_s"])]:
        s = tab[(a, 2024)].dropna()
        if s.empty:
            continue
        w = tab[("pop", 0)].reindex(s.index)
        lvl = float(np.average(s, weights=w))
        ps = []
        for p in parts:
            q = tab[(p, 2024)].dropna()
            if q.empty:
                continue
            wq = tab[("pop", 0)].reindex(q.index)
            ps.append(f"{p}={float(np.average(q, weights=wq)):.1f}")
        r_a, _ = corr(tab[(a, 2024)], tab[(parts[0], 2024)], tab[("pop", 0)])
        print(f"    {a} = {lvl:.1f}   parts: {', '.join(ps)}   r({a},{parts[0]}) = {r_a:+.3f}")

    print("\n  INFERRED reading (documented in HARNESS_V2_NOTES.md as inferred): the `_s` suffix "
          "carries a\n  systematically different level from its unsuffixed twin and different "
          "coverage — treat suffixed and\n  unsuffixed as DIFFERENT items, never as the same "
          "concept measured twice.")


def part_b(fx, tab):
    print("\n" + "=" * 122)
    print("PART B — THE REGISTERED SCREENING CLAIM: is `fin31` a restatement of the headline?")
    print("=" * 122)
    pop = tab[("pop", 0)]
    head24, headd = tab[(HEAD, 2024)], tab[(HEAD, 2024)] - tab[(HEAD, 2021)]

    rows = []
    for c in FIN31:
        n21 = tab[(c, 2021)].notna().sum()
        n24 = tab[(c, 2024)].notna().sum()
        if n21 < MIN_C or n24 < MIN_C:
            rows.append({"col": c, "qual": False, "n21": int(n21), "n24": int(n24)})
            continue
        lvl, dlt = tab[(c, 2024)], tab[(c, 2024)] - tab[(c, 2021)]
        d_lvl = pd.DataFrame({"x": lvl, "y": head24, "w": pop}).dropna()
        d_dlt = pd.DataFrame({"x": dlt, "y": headd, "w": pop}).dropna()

        rw_l, n_l = corr(d_lvl["x"], d_lvl["y"], d_lvl["w"])
        ru_l, _ = corr(d_lvl["x"], d_lvl["y"])
        rw_d, n_d = corr(d_dlt["x"], d_dlt["y"], d_dlt["w"])
        ru_d, _ = corr(d_dlt["x"], d_dlt["y"])

        lo_l, hi_l, p_l = boot_ci(d_lvl, lambda f: corr(f["x"], f["y"], f["w"])[0])
        lo_d, hi_d, p_d = boot_ci(d_dlt, lambda f: corr(f["x"], f["y"], f["w"])[0])

        big = d_lvl.nlargest(5, "w").index
        g6_l = corr(d_lvl.drop(index=big)["x"], d_lvl.drop(index=big)["y"],
                    d_lvl.drop(index=big)["w"])[0]
        bigd = d_dlt.nlargest(5, "w").index
        g6_d = corr(d_dlt.drop(index=bigd)["x"], d_dlt.drop(index=bigd)["y"],
                    d_dlt.drop(index=bigd)["w"])[0]

        indep = (abs(rw_l) < IND_LEVEL and abs(ru_l) < IND_LEVEL
                 and abs(rw_d) < IND_DELTA and abs(ru_d) < IND_DELTA)
        rows.append({"col": c, "qual": True, "n21": int(n21), "n24": int(n24),
                     "n_l": n_l, "neff_l": _kish(d_lvl["w"]), "n_d": n_d,
                     "neff_d": _kish(d_dlt["w"]),
                     "rw_l": rw_l, "ru_l": ru_l, "ci_l": (lo_l, hi_l), "p_l": p_l, "g6_l": g6_l,
                     "rw_d": rw_d, "ru_d": ru_d, "ci_d": (lo_d, hi_d), "p_d": p_d, "g6_d": g6_d,
                     "indep": indep, "tab_l": d_lvl})

    q = [r for r in rows if r["qual"]]
    skipped = [r for r in rows if not r["qual"]]
    if skipped:
        print("  items failing the coverage floor (>= %d economies in BOTH 2021 and 2024): " % MIN_C
              + ", ".join(f"{r['col']} ({r['n21']}/{r['n24']})" for r in skipped))

    print(f"\n  LEVELS — corr(item 2024, {HEAD} 2024)")
    print(f"  {'item':14s} {'n':>3s} {'neff':>5s} {'r_wtd':>7s} {'[95% CI]':>17s} {'p_boot':>7s} "
          f"{'G6':>7s} {'r_unwtd':>8s}")
    for r in q:
        print(f"  {r['col']:14s} {r['n_l']:3d} {r['neff_l']:5.1f} {r['rw_l']:+7.3f} "
              f"[{r['ci_l'][0]:+6.3f},{r['ci_l'][1]:+6.3f}] {r['p_l']:7.3f} {r['g6_l']:+7.3f} "
              f"{r['ru_l']:+8.3f}")

    print(f"\n  CHANGES — corr(item d2021->24, {HEAD} d2021->24)")
    print(f"  {'item':14s} {'n':>3s} {'neff':>5s} {'r_wtd':>7s} {'[95% CI]':>17s} {'p_boot':>7s} "
          f"{'G6':>7s} {'r_unwtd':>8s}")
    for r in q:
        print(f"  {r['col']:14s} {r['n_d']:3d} {r['neff_d']:5.1f} {r['rw_d']:+7.3f} "
              f"[{r['ci_d'][0]:+6.3f},{r['ci_d'][1]:+6.3f}] {r['p_d']:7.3f} {r['g6_d']:+7.3f} "
              f"{r['ru_d']:+8.3f}")

    med_w = float(np.median([abs(r["rw_l"]) for r in q]))
    med_u = float(np.median([abs(r["ru_l"]) for r in q]))
    indep_items = [r["col"] for r in q if r["indep"]]
    keep = med_w >= RED_BAR and med_u >= RED_BAR and not indep_items

    print(f"\n  median |r_level|: weighted {med_w:.3f}   unweighted {med_u:.3f}   "
          f"(redundancy bar {RED_BAR})")
    print(f"  items meeting the INDEPENDENCE definition (|r_level| < {IND_LEVEL} and "
          f"|r_delta| < {IND_DELTA} on BOTH lenses): "
          f"{', '.join(indep_items) if indep_items else 'none'}")
    print(f"\n  VERDICT: redundancy claim {'KEPT' if keep else 'DISCARDED'} — "
          f"{'the module restates the headline' if keep else 'the module carries independent variation'}")
    if indep_items:
        print(f"  NEW-GROUND TARGETS NAMED: {', '.join(indep_items)}")

    # ---- B12: named leave-one-out on the module's flagship item (widest 2024 coverage)
    flag = max(q, key=lambda r: (r["n_l"], -FIN31.index(r["col"])))
    d = flag["tab_l"]
    full = corr(d["x"], d["y"], d["w"])[0]
    best, who = 0.0, None
    for c in d.index:
        v = corr(d.drop(index=c)["x"], d.drop(index=c)["y"], d.drop(index=c)["w"])[0]
        if pd.notna(v) and abs(v - full) > abs(best):
            best, who = v - full, c
    print(f"\n  B12 — largest single leave-one-economy-out on {flag['col']} (levels, widest "
          f"coverage): r_w {full:+.3f}, drop {who} -> {full + best:+.3f} ({best:+.3f}); "
          f"drop-top-5 {flag['g6_l']:+.3f}; neff {flag['neff_l']:.1f} vs n {flag['n_l']}")
    return keep, indep_items


def run(fx: Findex):
    tab = build(fx)
    print("E45 — the fin31 digital-payment detail module: restatement, or new ground? "
          "(B2 cell, zero prior mentions; parent E41)\n")
    part_a(fx, tab)
    keep, indep = part_b(fx, tab)
    print("\n" + "=" * 122)
    print(f"SUMMARY  registered redundancy claim: {'KEEP' if keep else 'DISCARD'}  |  "
          f"independent items: {', '.join(indep) if indep else 'none'}")
    print("=" * 122)


if __name__ == "__main__":
    run(Findex())
