"""E53 (pre-registered 2026-08-19): is the 2021->24 cash rebound a COMMON EPISODE inside the same
economies, or four independent item-level reversions?

Agenda item 7.8. Parent: none (nearest design ancestor E39). Frame pan_dev. Rule B14: distribution
design over the full four-wave path; the primary is a co-occurrence count, not a Delta->Delta.

Four cash-side items in four different modules all fall 2014->2021 and rebound 2021->2024:
  fin31d (digital-payment detail), fin34c (wage payment modes), fin42 (fin catch-all),
  fin43c (agricultural payments).

PRIMARY. On economies with all four items x all four waves: V(economy, item) = 1 if
level_2021 < level_2014 - MARGIN and level_2024 > level_2021 + MARGIN. S3 = share of economies with
>= 3 of 4 V-items. Null = 1,000 permutations shuffling each item's V-indicator independently across
economies (marginals preserved, co-occurrence destroyed).
REGISTERED SIGN (B15): POSITIVE excess. KEEP if S3_obs >= 1.5 x null mean AND above the null p97.5.

SECONDARY A: every item's four wave levels on this exact set (B16, path before span).
SECONDARY B: per item, share of economies with a positive 2021->24 change, unweighted and
population-weighted, plus the median change (the E39 within-country-vs-composition question).
SECONDARY C: population-weighted twin of the primary.
ROBUSTNESS: margins 0 / 1 / 2pp, and the mirror tail (share with ZERO V-items) against the null.
INFERENCE (B6): economy bootstrap 1,000 draws on S3; Kish neff of the 2024 population weights.

GATES: G3 base (non-_s) columns only; G4 coverage; G5 n/a; G6 n/a (no correlation) -- the mirror
tail and the weighted twin are the registered substitutes.
"""
import numpy as np
import pandas as pd

from harness import Findex

ITEMS = ["fin31d", "fin34c", "fin42", "fin43c"]
WAVES = [2014, 2017, 2021, 2024]
MARGINS = [0.0, 1.0, 2.0]
PRIMARY_MARGIN = 1.0
DRAWS = 1000
RATIO_BAR = 1.5
SEED = 20260819


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def build(f):
    """Wide panel: index = economy, columns = (item, wave), plus pop. Complete cases only."""
    frames = {}
    for it in ITEMS:
        w = f.country_panel(f.pan_dev, it, WAVES)
        frames[it] = w
    idx = None
    for it in ITEMS:
        ok = frames[it].index[frames[it][WAVES].notna().all(axis=1)]
        idx = set(ok) if idx is None else idx & set(ok)
    idx = sorted(idx)
    out = pd.DataFrame(index=idx)
    for it in ITEMS:
        for y in WAVES:
            out[(it, y)] = frames[it].loc[idx, y]
    out["pop"] = frames[ITEMS[0]].loc[idx, "pop"]
    return out


def v_matrix(panel, margin):
    V = pd.DataFrame(index=panel.index)
    for it in ITEMS:
        fell = panel[(it, 2021)] < panel[(it, 2014)] - margin
        rose = panel[(it, 2024)] > panel[(it, 2021)] + margin
        V[it] = (fell & rose).astype(int)
    return V


def permutation_null(V, weights=None, draws=DRAWS, seed=SEED):
    """Shuffle each item's V-indicator independently; return the null distributions of
    S3 (>=3 of 4) and S0 (zero of 4)."""
    rng = np.random.default_rng(seed)
    arr = V.to_numpy()
    n = arr.shape[0]
    w = np.ones(n) if weights is None else np.asarray(weights, dtype=float)
    w = w / w.sum()
    s3, s0 = [], []
    for _ in range(draws):
        perm = np.column_stack([rng.permutation(arr[:, j]) for j in range(arr.shape[1])])
        tot = perm.sum(axis=1)
        s3.append(float(w[tot >= 3].sum()))
        s0.append(float(w[tot == 0].sum()))
    return np.array(s3), np.array(s0)


def report_margin(V, panel, margin, label, weights=None):
    tot = V.sum(axis=1)
    w = np.ones(len(V)) if weights is None else np.asarray(weights, dtype=float)
    w = w / w.sum()
    s3_obs = float(w[(tot >= 3).to_numpy()].sum())
    s0_obs = float(w[(tot == 0).to_numpy()].sum())
    s3_null, s0_null = permutation_null(V, weights=weights)
    print(f"\n  --- {label} (margin {margin:.0f}pp) ---")
    print("   V-items per economy: " +
          ", ".join(f"{k}:{int((tot == k).sum())}" for k in range(5)) +
          f"   (item V-rates: " + ", ".join(f"{it} {V[it].mean():.0%}" for it in ITEMS) + ")")
    print(f"   S3 observed {s3_obs:.4f} | null mean {s3_null.mean():.4f} "
          f"[p2.5 {np.percentile(s3_null, 2.5):.4f}, p97.5 {np.percentile(s3_null, 97.5):.4f}] "
          f"| ratio {s3_obs / s3_null.mean() if s3_null.mean() else np.inf:.2f}x "
          f"| p_perm(>=obs) {(s3_null >= s3_obs).mean():.3f}")
    print(f"   S0 observed {s0_obs:.4f} | null mean {s0_null.mean():.4f} "
          f"[p2.5 {np.percentile(s0_null, 2.5):.4f}, p97.5 {np.percentile(s0_null, 97.5):.4f}] "
          f"| ratio {s0_obs / s0_null.mean() if s0_null.mean() else np.inf:.2f}x")
    ratio = s3_obs / s3_null.mean() if s3_null.mean() else np.inf
    passed = (ratio >= RATIO_BAR) and (s3_obs > np.percentile(s3_null, 97.5))
    print(f"   registered bars: ratio >= {RATIO_BAR} AND above null p97.5  ->  "
          f"{'PASS' if passed else 'FAIL'}")
    return {"s3": s3_obs, "null_mean": float(s3_null.mean()),
            "p975": float(np.percentile(s3_null, 97.5)), "ratio": ratio,
            "p_perm": float((s3_null >= s3_obs).mean()), "pass": passed, "tot": tot}


def main():
    f = Findex()
    panel = build(f)
    pop = panel["pop"]
    print("=" * 92)
    print("E53 — is the 2021->24 cash rebound a COMMON within-economy episode? (agenda item 7.8)")
    print("=" * 92)
    print(f"\nG4 coverage: {len(panel)} developing-panel economies with all 4 items x all 4 waves; "
          f"share of pan_dev 2024 adult population "
          f"{pop.sum() / f.pan_dev[f.pan_dev['year'] == 2024]['pop_adult'].sum():.1%}")
    print(f"B10: nominal n = {len(panel)}, Kish neff of the 2024 population weights "
          f"= {kish(pop):.1f}")
    print("G3: base (non-_s) columns only — the _s twins are conditional versions "
          "(HARNESS_V2_NOTES item 10) and are excluded.")

    print("\n" + "=" * 92)
    print("SECONDARY A — the PATH on this exact set (B16: path before span)")
    print("=" * 92)
    rows = []
    for it in ITEMS:
        wt = [float(np.average(panel[(it, y)], weights=pop)) for y in WAVES]
        uw = [float(panel[(it, y)].mean()) for y in WAVES]
        rows.append({"item": it,
                     "weighted": " -> ".join(f"{v:.1f}" for v in wt),
                     "unweighted": " -> ".join(f"{v:.1f}" for v in uw),
                     "d2021_24_w": round(wt[3] - wt[2], 2),
                     "d2014_24_w": round(wt[3] - wt[0], 2)})
    print(pd.DataFrame(rows).to_string(index=False))

    print("\n" + "=" * 92)
    print("SECONDARY B — is the rebound WITHIN-COUNTRY or a few large economies? (E39's question)")
    print("=" * 92)
    rows = []
    for it in ITEMS:
        d = panel[(it, 2024)] - panel[(it, 2021)]
        share_u = float((d > 0).mean())
        share_w = float(pop[d > 0].sum() / pop.sum())
        rows.append({"item": it, "median_d_pp": round(float(d.median()), 2),
                     "mean_d_pp": round(float(d.mean()), 2),
                     "share_rising_unw": f"{share_u:.1%}",
                     "share_rising_popw": f"{share_w:.1%}",
                     "n_rising": int((d > 0).sum())})
    print(pd.DataFrame(rows).to_string(index=False))

    print("\n" + "=" * 92)
    print("PRIMARY + ROBUSTNESS — co-occurrence against a permutation null")
    print("=" * 92)
    res = {}
    for m in MARGINS:
        V = v_matrix(panel, m)
        res[m] = report_margin(V, panel, m, "UNWEIGHTED (registered primary)")

    print("\n" + "=" * 92)
    print("SECONDARY C — population-weighted twin of the primary (margin 1pp)")
    print("=" * 92)
    Vp = v_matrix(panel, PRIMARY_MARGIN)
    report_margin(Vp, panel, PRIMARY_MARGIN, "POPULATION-WEIGHTED", weights=pop.to_numpy())

    print("\n" + "=" * 92)
    print("B6 INFERENCE — economy bootstrap on S3 (1,000 draws), primary margin")
    print("=" * 92)
    rng = np.random.default_rng(SEED)
    tot = res[PRIMARY_MARGIN]["tot"].to_numpy()
    boot = np.array([(rng.choice(tot, size=len(tot), replace=True) >= 3).mean()
                     for _ in range(DRAWS)])
    print(f"   S3 = {res[PRIMARY_MARGIN]['s3']:.4f}  95% CI "
          f"[{np.percentile(boot, 2.5):.4f}, {np.percentile(boot, 97.5):.4f}]")

    print("\n   economies carrying >= 3 V-items (margin 1pp): " +
          ", ".join(sorted(res[PRIMARY_MARGIN]["tot"][res[PRIMARY_MARGIN]["tot"] >= 3].index)))

    print("\n" + "=" * 92)
    print("VERDICT")
    print("=" * 92)
    p = res[PRIMARY_MARGIN]
    print(f"   registered primary (margin 1pp): S3 {p['s3']:.4f} vs null {p['null_mean']:.4f} "
          f"= {p['ratio']:.2f}x, p_perm {p['p_perm']:.3f}  ->  "
          f"{'KEEP' if p['pass'] else 'DISCARD as registered'}")
    print("   margin sensitivity: " +
          ", ".join(f"{m:.0f}pp {'PASS' if res[m]['pass'] else 'FAIL'} "
                    f"({res[m]['ratio']:.2f}x)" for m in MARGINS))


if __name__ == "__main__":
    main()
