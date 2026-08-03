"""E30 (pre-registered): do the three NON-saving-destination co-movements replicate earlier?

Program 1, the replication debt. E28 promoted the rails->saving family (E1/E10/E12) by replicating
on 2017->2021. Three further keep-window findings share the same Delta-on-Delta construction but do
NOT have formal saving as the destination, so they are an independent test of whether the ledger's
co-movements are 2021-24 window artifacts:

  E11  d(fin22a_22a1_22g_d) ~ d(fin17a_17a1_d)      formal borrowing ~ formal saving     +0.403
  E13  d(fiaccount_t_d)     ~ d(mobileaccount_t_d)  co-development vs leapfrogging       +0.435
  E14  d(mobileaccount_t_d) ~ d(g20_any)            bundled digital on-ramps             +0.600

TEST. Developing panel, each pair, in 2014->2017 and 2017->2021 (2021->2024 reprinted as the
reference). Population-weighted correlation, weight = 2024 adult population — E1/E10/E12/E28
construction, changing only the window. Delta-tercile means of the destination variable per cell.
Per-window SD of both Deltas (E28's variance-collapse check). Gates G3, G4, G6.
B6 on every cell: country bootstrap 2,000 resamples, percentile 95% interval, Kish neff.

PROMOTION RULE (registered, identical to E28's): keep-window -> keep-general iff in at least one
earlier window r >= +0.30 with the same (positive) sign, G6 sign-stable, and r_droptop >= 0.5 x
r_full (the E4 judgment rule). Failing that in both earlier windows, the finding STAYS keep-window
and is relabelled explicitly window-specific. The bootstrap interval is reported, not a keep
condition.

DECLARED. Contemporaneous Delta-on-Delta co-movement in every window — descriptive, never causal.
Composition differs by pair and window (the mobile-money pairs are thin, ~54-59 economies); each
cell prints its own n, neff and interval. A null in a calm window is not evidence of absence — E28
established 2014->2017 has the least Delta-variance in the series — so the SDs are printed and the
reading is checked rather than assumed.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 30

WINDOWS = [(2014, 2017), (2017, 2021), (2021, 2024)]
REFERENCE_WINDOW = (2021, 2024)

# (label, x column, y column, published 2021->24 r, parent finding)
PAIRS = [
    ("E11 borrow~save", "fin22a_22a1_22g_d", "fin17a_17a1_d", 0.403, "E11"),
    ("E13 fi~mobile", "mobileaccount_t_d", "fiaccount_t_d", 0.435, "E13"),
    ("E14 mobile~g20", "mobileaccount_t_d", "g20_any", 0.600, "E14"),
]

# G3 declarations: every column above is a registry headline except none — all four are headlines.
G3_CONCEPTS = {
    "fin22a_22a1_22g_d": "borrowed_formally",
    "fin17a_17a1_d": "saved_formally",
    "mobileaccount_t_d": "mobile_money",
    "fiaccount_t_d": "fi_account",
    "g20_any": "digital_payment",
}


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _boot_ci(fn, frame, draws=BOOT, seed=SEED):
    """Country bootstrap of a statistic computed from a country-indexed frame (B6)."""
    rng = np.random.default_rng(seed)
    idx = np.arange(len(frame))
    out = []
    for _ in range(draws):
        v = fn(frame.iloc[rng.choice(idx, size=len(idx), replace=True)])
        if v is not None and pd.notna(v):
            out.append(v)
    if len(out) < draws * 0.9:
        return None, None
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def _delta_frame(fx: Findex, xcol, ycol, y0, y1):
    """Per-country Delta of both columns over [y0, y1] plus the 2024 population weight."""
    xw = fx.country_panel(fx.pan_dev, xcol, [y0, y1])
    yw = fx.country_panel(fx.pan_dev, ycol, [y0, y1])
    df = pd.DataFrame({
        "dx": xw[y1] - xw[y0],
        "dy": yw[y1] - yw[y0],
        "pop": xw["pop"],
    }).dropna()
    return df


def run_pair(fx: Findex, label, xcol, ycol, published_r, parent):
    print("\n" + "=" * 96)
    print(f"{label}   d({xcol}) ~ d({ycol})   [parent {parent}, published 2021->24 r = "
          f"{published_r:+.3f}]")
    print("=" * 96)
    cells = {}
    for y0, y1 in WINDOWS:
        df = _delta_frame(fx, xcol, ycol, y0, y1)
        if len(df) < 10:
            print(f"  {y0}->{y1}: insufficient coverage (n={len(df)})")
            cells[(y0, y1)] = None
            continue
        w = df["pop"]
        r, n = fx.weighted_corr(df["dx"], df["dy"], w)
        neff = _kish(w)
        lo, hi = _boot_ci(lambda s: fx.weighted_corr(s["dx"], s["dy"], s["pop"])[0], df,
                          seed=SEED + y0)
        g6 = fx.gate_jackknife(df["dx"], df["dy"], w)
        g4 = fx.gate_coverage(fx.pan_dev, ycol, y1)
        retain = (abs(g6["r_droptop"]) / abs(r)) if (r and g6.get("r_droptop") is not None) else np.nan
        ci = f"[{lo:+.3f}, {hi:+.3f}]" if lo is not None else "n/a"
        tag = "  <- REFERENCE" if (y0, y1) == REFERENCE_WINDOW else ""
        print(f"\n  {y0}->{y1}   r = {r:+.3f}   (n={n}, Kish neff={neff:.1f})   95% CI {ci}{tag}")
        print(f"      G6 sign-stable={g6['ok']}  r_droptop={g6['r_droptop']:+.3f}  "
              f"retention={retain:.2f}   (E4 floor 0.50)")
        print(f"      G4 {g4['n_countries']} economies, pop_share {g4['pop_share']}")
        print(f"      Delta dispersion: SD(dx)={df['dx'].std():5.2f}pp  SD(dy)={df['dy'].std():5.2f}pp")

        ter = pd.qcut(df["dx"], 3, labels=["low", "mid", "high"], duplicates="drop")
        parts = []
        for lab, g in df.groupby(ter, observed=True):
            parts.append(f"{lab} {np.average(g['dy'], weights=g['pop']):+5.1f}pp")
        print(f"      dx-tercile mean dy: {'  '.join(parts)}")

        cells[(y0, y1)] = {"r": r, "n": n, "neff": neff, "ci": (lo, hi),
                           "g6_ok": g6["ok"], "retain": retain}

    # ---- pre-registered promotion rule
    ref = cells[REFERENCE_WINDOW]
    earlier = [(w, c) for w, c in cells.items() if w != REFERENCE_WINDOW and c is not None]
    replicated = [w for w, c in earlier
                  if c["r"] >= 0.30 and np.sign(c["r"]) == np.sign(ref["r"])
                  and c["g6_ok"] and c["retain"] >= 0.50]
    verdict = "PROMOTE keep-window -> keep-general" if replicated else "STAYS keep-window"
    print(f"\n  >>> {parent}: replicating windows = "
          f"{[f'{a}->{b}' for a, b in replicated] or 'none'}   -->  {verdict}")
    return {"parent": parent, "cells": cells, "replicated": replicated,
            "promote": bool(replicated)}


if __name__ == "__main__":
    fx = Findex()
    print("E30 — Program 1 replication debt: E11 / E13 / E14 on 2014->2017 and 2017->2021")
    print("Frame: pan_dev, group == 'all'. Weight: 2024 adult population (ledger convention).\n")
    print("G3 declarations (all five columns are registry headlines):")
    for col, concept in G3_CONCEPTS.items():
        print("   ", fx.gate_variant(concept, col))
    print("G5: n/a — no official series exists for a cross-country correlation")

    results = [run_pair(fx, *p) for p in PAIRS]

    print("\n" + "=" * 96)
    print("SUMMARY — r by window (dev panel, population-weighted)")
    print("=" * 96)
    print(f"  {'finding':18s} {'2014->2017':>18s} {'2017->2021':>18s} {'2021->2024 (ref)':>20s}"
          f"   verdict")
    for res, (label, _, _, _, parent) in zip(results, PAIRS):
        row = []
        for w in WINDOWS:
            c = res["cells"][w]
            row.append(f"{c['r']:+.3f} (n={c['n']})" if c else "n/a")
        print(f"  {parent + ' ' + label.split()[1]:18s} {row[0]:>18s} {row[1]:>18s} {row[2]:>20s}"
              f"   {'PROMOTE' if res['promote'] else 'stays keep-window'}")
    print(f"\nPromotions this experiment: "
          f"{[r['parent'] for r in results if r['promote']] or 'none'}")
