"""E54 (pre-registered 2026-08-19): does association strength rise with ECONOMY SIZE?

Agenda item 2.1b, registered fresh. Parent: E52 (which observed the gradient on the fin31d~fin34c
cash cell AFTER looking and could not claim it). Frame pan_dev. Rule B14: no new Delta->Delta
primary -- the 18 cells are existing all-windows cells of standing keeps and the primary statistic
is a BETWEEN-TERCILE DIFFERENCE OF CORRELATIONS evaluated across all three windows jointly.

Six rails x three windows = 18 cells. In each, split economies into terciles of 2024 adult
population and take the UNWEIGHTED Pearson r inside each tercile.
  Delta_r = r(top tercile) - r(bottom tercile)
REGISTERED SIGN (B15): POSITIVE. KEEP if mean Delta_r >= +0.15 AND Delta_r > 0 in >= 12 of 18.
SECONDARY 1: 1,000 RANDOM splits ignoring population -- the null for "any split does this".
SECONDARY 2: monotone count r(top) > r(mid) > r(bottom), and the full per-cell table.
INFERENCE (B6): economy bootstrap within terciles, 1,000 draws, on the mean Delta_r; Kish neff.
GATES: G3 headline variants declared; G4 per window; G5 na; G6 na (no single association claimed --
the random-split null is the registered substitute). Any tercile below 15 economies drops its cell.
"""
import numpy as np
import pandas as pd

from harness import Findex

RAILS = [
    ("E1  mobile money ~ formal saving", "mobileaccount_t_d", "fin17a_17a1_d"),
    ("E10 wage digitalization ~ saving", "fin32_acc", "fin17a_17a1_d"),
    ("E12 digital payment ~ saving", "g20_any", "fin17a_17a1_d"),
    ("E11 formal borrowing ~ saving", "fin22a_22a1_22g_d", "fin17a_17a1_d"),
    ("E13 FI account ~ mobile money", "fiaccount_t_d", "mobileaccount_t_d"),
    ("E14 mobile money ~ digital payment", "mobileaccount_t_d", "g20_any"),
]
WINDOWS = [(2014, 2017), (2017, 2021), (2021, 2024)]
MIN_TERCILE = 15
MEAN_BAR = 0.15
COUNT_BAR = 12
DRAWS = 1000
SEED = 20260819


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def cell_frame(f, xcol, ycol, y0, y1):
    """Complete-case deltas for one rail x window, with the 2024 population weight."""
    wx = f.country_panel(f.pan_dev, xcol, [y0, y1])
    wy = f.country_panel(f.pan_dev, ycol, [y0, y1])
    d = pd.DataFrame({"dx": wx[y1] - wx[y0], "dy": wy[y1] - wy[y0], "pop": wx["pop"]}).dropna()
    return d


def tercile_rs(d, order):
    """Unweighted r inside each third of `order` (a ranking of d's index, low -> high)."""
    n = len(order)
    cuts = [order[: n // 3], order[n // 3: 2 * n // 3], order[2 * n // 3:]]
    out = []
    for c in cuts:
        s = d.loc[c]
        out.append(float(np.corrcoef(s["dx"], s["dy"])[0, 1]) if len(s) >= 3 else np.nan)
    return out, [len(c) for c in cuts]


def main():
    f = Findex()
    print("=" * 96)
    print("E54 — is association strength POPULATION-GRADED? (agenda item 2.1b, registered fresh)")
    print("=" * 96)
    print("G3: all six rails at their registered E28/E30 headline variants. Terciles are of 2024 "
          "adult population;\n    the within-tercile correlation is UNWEIGHTED by construction.")

    rows, dropped = [], []
    for name, xc, yc in RAILS:
        for (y0, y1) in WINDOWS:
            d = cell_frame(f, xc, yc, y0, y1)
            order = list(d["pop"].sort_values().index)
            rs, sizes = tercile_rs(d, order)
            if min(sizes) < MIN_TERCILE or any(pd.isna(r) for r in rs):
                dropped.append(f"{name} {y0}->{y1} (tercile sizes {sizes})")
                continue
            rows.append({"rail": name, "window": f"{y0}->{y1}", "n": len(d),
                         "neff": round(kish(d["pop"]), 1),
                         "r_bot": round(rs[0], 3), "r_mid": round(rs[1], 3),
                         "r_top": round(rs[2], 3),
                         "delta_r": round(rs[2] - rs[0], 3),
                         "monotone": bool(rs[2] > rs[1] > rs[0])})
    tab = pd.DataFrame(rows)
    print(f"\nG4: {len(tab)} of 18 cells usable; dropped {len(dropped)}"
          + ("" if not dropped else ":\n   " + "\n   ".join(dropped)))
    print("\n" + "=" * 96)
    print("SECONDARY 2 — the per-cell table (r within population terciles, unweighted)")
    print("=" * 96)
    print(tab.to_string(index=False))

    mean_d = float(tab["delta_r"].mean())
    pos = int((tab["delta_r"] > 0).sum())
    mono = int(tab["monotone"].sum())
    print(f"\n  mean Delta_r = {mean_d:+.3f} over {len(tab)} cells | positive in {pos}/{len(tab)} "
          f"| monotone top>mid>bot in {mono}/{len(tab)}")
    print(f"  median Delta_r = {tab['delta_r'].median():+.3f} | "
          f"range {tab['delta_r'].min():+.3f} to {tab['delta_r'].max():+.3f}")
    print(f"  Kish neff per window: " +
          ", ".join(f"{w}: {tab[tab['window'] == w]['neff'].median():.1f}"
                    for w in tab["window"].unique()))

    # ------------------------------------------------ SECONDARY 1: random-split null
    rng = np.random.default_rng(SEED)
    cells = []
    for name, xc, yc in RAILS:
        for (y0, y1) in WINDOWS:
            d = cell_frame(f, xc, yc, y0, y1)
            if len(d) < 3 * MIN_TERCILE:
                continue
            cells.append(d)
    null = []
    for _ in range(DRAWS):
        vals = []
        for d in cells:
            order = list(rng.permutation(d.index))
            rs, _ = tercile_rs(d, order)
            if not any(pd.isna(r) for r in rs):
                vals.append(rs[2] - rs[0])
        null.append(np.mean(vals))
    null = np.array(null)
    p_perm = float((null >= mean_d).mean())
    print("\n" + "=" * 96)
    print("SECONDARY 1 — random-split null (1,000 splits ignoring population)")
    print("=" * 96)
    print(f"  null mean {null.mean():+.3f} | [p2.5 {np.percentile(null, 2.5):+.3f}, "
          f"p97.5 {np.percentile(null, 97.5):+.3f}] | observed {mean_d:+.3f} | "
          f"p_perm(null >= observed) {p_perm:.3f}")
    print(f"  -> the population split is {'OUTSIDE' if mean_d > np.percentile(null, 97.5) else 'INSIDE'}"
          f" the random-split distribution")

    # ------------------------------------------------ B6: bootstrap within terciles
    boot = []
    for _ in range(DRAWS):
        vals = []
        for d in cells:
            order = list(d["pop"].sort_values().index)
            n = len(order)
            cuts = [order[: n // 3], order[n // 3: 2 * n // 3], order[2 * n // 3:]]
            rs = []
            for c in cuts:
                pick = rng.choice(c, size=len(c), replace=True)
                s = d.loc[pick]
                rs.append(float(np.corrcoef(s["dx"], s["dy"])[0, 1])
                          if s["dx"].std() > 0 and s["dy"].std() > 0 else np.nan)
            if not any(pd.isna(r) for r in rs):
                vals.append(rs[2] - rs[0])
        boot.append(np.mean(vals))
    boot = np.array(boot)
    print("\n" + "=" * 96)
    print("B6 INFERENCE — economy bootstrap within terciles (1,000 draws)")
    print("=" * 96)
    print(f"  mean Delta_r {mean_d:+.3f}  95% CI [{np.percentile(boot, 2.5):+.3f}, "
          f"{np.percentile(boot, 97.5):+.3f}]  |  "
          f"{'excludes zero' if np.percentile(boot, 2.5) > 0 else 'INCLUDES ZERO'}")

    print("\n" + "=" * 96)
    print("VERDICT against the registered bars")
    print("=" * 96)
    b1 = mean_d >= MEAN_BAR
    b2 = pos >= COUNT_BAR
    print(f"  mean Delta_r {mean_d:+.3f} >= +{MEAN_BAR}: {'PASS' if b1 else 'FAIL'}")
    print(f"  positive in {pos}/{len(tab)} >= {COUNT_BAR}: {'PASS' if b2 else 'FAIL'}")
    print(f"  registered sign POSITIVE, observed {'POSITIVE' if mean_d > 0 else 'NEGATIVE'}")
    print(f"  -> {'KEEP' if (b1 and b2) else 'DISCARD as registered'}")


if __name__ == "__main__":
    main()
