"""E56 (registered 2026-08-22) — agenda item 8.2: is the 2021->2024 item-level dropout ONE block or
per-item attrition, and what do the balanced paths of the two exposed keeps say?

Parent E55 (chain E53 -> E55 -> E56, at the B3 cap). Audit / measurement pass, not an association
experiment, so B14 does not bind.

PRIMARY (registered): for every country column with >=30 developing-panel economies reporting in
2021, D(col) = economies reporting in 2021 and NOT in 2024. Restrict to |D| >= 3. D* = the modal
dropper set. BAR: >= 80% of non-trivially-dropping columns have Jaccard(D, D*) >= 0.90 -> the
dropout is a single block; below the bar -> per-item attrition. Registered sign/direction: the sets
COINCIDE.
SECONDARY 1 (no bar): module membership of the columns whose D matches D*.
SECONDARY 2 (rule B16): the fully balanced wave path of fin32_acc (E10, keep-general) and fh1 / fh2 /
fh1_fh2 (E33, keep-window) -- the two corrections E55 opened in PAPER_DRAFT_v4.md.
"""
import re
from collections import Counter

import numpy as np
import pandas as pd

from harness import Findex, YEARS

MIN_2021 = 30
MIN_DROP = 3
JACCARD_BAR = 0.90
SHARE_BAR = 0.80


def reporters(dev, col, year):
    d = dev[(dev["year"] == year) & dev[col].notna()]
    return frozenset(d["countrynewwb"].unique())


def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 1.0


def module_of(col):
    m = re.match(r"([a-z_]+[0-9]*)", col)
    return m.group(1) if m else col


def main():
    fx = Findex()
    dev = fx.pan_dev
    pop24 = dev[dev["year"] == 2024].set_index("countrynewwb")["pop_adult"]
    skip = {"year", "pop_adult", "countrynewwb", "codewb", "regionwb24_hi", "group",
            "incomegroupwb24", "adultpopulation", "pop_adult_18"}
    cols = [c for c in dev.columns
            if c not in skip and pd.api.types.is_numeric_dtype(dev[c])]

    print("=" * 96)
    print("E56 — agenda item 8.2: ONE dropout block or per-item attrition? (developing panel)")
    print("=" * 96)

    recs = []
    for c in cols:
        r21, r24 = reporters(dev, c, 2021), reporters(dev, c, 2024)
        if len(r21) < MIN_2021:
            continue
        D = r21 - r24
        recs.append({"col": c, "n21": len(r21), "n24": len(r24), "nD": len(D), "D": D,
                     "dead": len(r24) == 0})
    print("eligible columns (>=%d developing-panel economies in 2021): %d" % (MIN_2021, len(recs)))

    nz = [r for r in recs if r["nD"] >= MIN_DROP]
    dead = [r for r in nz if r["dead"]]
    print("columns with a non-trivial drop (|D| >= %d): %d   (of which DISCONTINUED, "
          "zero 2024 reporters: %d)" % (MIN_DROP, len(nz), len(dead)))
    print("columns with |D| in {1,2}: %d ; perfectly stable (|D| = 0): %d"
          % (sum(1 for r in recs if 1 <= r["nD"] <= 2), sum(1 for r in recs if r["nD"] == 0)))

    def primary(rows, label):
        if not rows:
            print("\n[%s] no columns" % label)
            return None, 0.0
        counts = Counter(r["D"] for r in rows)
        Dstar, k = counts.most_common(1)[0]
        near = [r for r in rows if jaccard(r["D"], Dstar) >= JACCARD_BAR]
        share = len(near) / len(rows)
        print("\n[%s] %d columns; modal dropper set D* has |D*| = %d and is EXACTLY shared by "
              "%d columns (%.1f%%)" % (label, len(rows), len(Dstar), k, 100 * k / len(rows)))
        print("  D* = %s" % ", ".join(sorted(Dstar)))
        print("  columns with Jaccard(D, D*) >= %.2f: %d of %d = %.1f%%  (bar %.0f%%)  -> %s"
              % (JACCARD_BAR, len(near), len(rows), 100 * share, 100 * SHARE_BAR,
                 "PASS" if share >= SHARE_BAR else "FAIL"))
        js = sorted(jaccard(r["D"], Dstar) for r in rows)
        print("  Jaccard(D, D*) distribution: min %.2f p25 %.2f median %.2f p75 %.2f max %.2f"
              % (js[0], np.percentile(js, 25), np.median(js), np.percentile(js, 75), js[-1]))
        print("  distinct dropper sets among these columns: %d" % len(counts))
        for D, n in counts.most_common(6):
            print("    n=%-3d |D|=%-3d %s" % (n, len(D), ", ".join(sorted(D))[:70]))
        return Dstar, share

    Dstar, share = primary(nz, "REGISTERED PRIMARY — all non-trivially-dropping columns")
    primary([r for r in nz if not r["dead"]],
            "declared robustness — excluding discontinued columns")

    # --- D* provenance: are its economies still in the 2024 wave?
    print("\nD* ECONOMIES IN THE 2024 WAVE (E53's test: items dropping out, not economies):")
    for e in sorted(Dstar):
        row = dev[(dev["year"] == 2024) & (dev["countrynewwb"] == e)]
        acc = row["account_t_d"].notna().any() if len(row) else False
        p = pop24.get(e, np.nan)
        print("  %-14s in 2024 wave: %-5s account_t_d recorded: %-5s  2024 adult pop %.1fm"
              % (e, bool(len(row)), bool(acc), p / 1e6 if pd.notna(p) else float("nan")))
    tot = pop24.sum()
    print("  D* holds %.1f%% of 2024 developing-panel adult population"
          % (100 * pop24.reindex(sorted(Dstar)).sum() / tot))

    # --- SECONDARY 1: module membership of the block
    exact = [r["col"] for r in nz if r["D"] == Dstar]
    mods = Counter(module_of(c) for c in exact)
    print("\nSECONDARY 1 — module membership of the %d columns sharing D* EXACTLY:" % len(exact))
    for m, n in mods.most_common():
        print("  %-12s %3d   %s" % (m, n, ", ".join(sorted(c for c in exact
                                                           if module_of(c) == m))[:70]))
    allmods = Counter(module_of(r["col"]) for r in recs)
    print("  coverage of each affected module: " + "; ".join(
        "%s %d/%d" % (m, n, allmods[m]) for m, n in mods.most_common(8)))

    # --- SECONDARY 2 (B16): balanced wave paths for the two corrections E55 opened
    print("\n" + "=" * 96)
    print("SECONDARY 2 (rule B16) — balanced wave paths for the columns E55 exposed")
    print("=" * 96)
    for col, yrs in (("fin32_acc", [2014, 2017, 2021, 2024]),
                     ("fh1", [2021, 2024]), ("fh2", [2021, 2024]),
                     ("fh1_fh2", [2021, 2024])):
        sets = [reporters(dev, col, y) for y in yrs]
        bal = frozenset.intersection(*sets)
        print("\n%s — reporters by wave: %s ; BALANCED set %d economies, %.1f%% of 2024 "
              "developing-panel adult population"
              % (col, dict(zip(yrs, [len(s) for s in sets])), len(bal),
                 100 * pop24.reindex(sorted(bal)).sum() / tot))
        unb, ba = [], []
        for y in yrs:
            d = dev[dev["year"] == y]
            unb.append(fx.wmean(d, col) * 100)
            ba.append(fx.wmean(d[d["countrynewwb"].isin(bal)], col) * 100)
        print("  unbalanced (each wave over its own reporters): "
              + "  ".join("%d %6.2f" % (y, v) for y, v in zip(yrs, unb)))
        print("  BALANCED   (one fixed denominator):            "
              + "  ".join("%d %6.2f" % (y, v) for y, v in zip(yrs, ba)))
        d_unb, d_bal = unb[-1] - unb[-2], ba[-1] - ba[-2]
        print("  last-window delta: unbalanced %+.2fpp, balanced %+.2fpp, discrepancy %+.2fpp%s"
              % (d_unb, d_bal, d_unb - d_bal,
                 "   [SIGN FLIP]" if np.sign(d_unb) != np.sign(d_bal) else ""))
        if len(ba) > 2:
            diffs = np.diff(ba)
            mono = np.all(diffs >= 0) or np.all(diffs <= 0)
            print("  balanced path is %s: steps %s"
                  % ("MONOTONE" if mono else "NON-MONOTONE",
                     " ".join("%+.2f" % d for d in diffs)))
        # G4 on the balanced set
        g4 = fx.gate_coverage(dev[dev["countrynewwb"].isin(bal)], col, yrs[-1])
        print("  G4 on the balanced set: %s" % g4)

    print("\n" + "=" * 96)
    print("VERDICT: registered bar %.0f%% of non-trivially-dropping columns at Jaccard >= %.2f; "
          "observed %.1f%% -> %s" % (100 * SHARE_BAR, JACCARD_BAR, 100 * share,
                                     "KEEP" if share >= SHARE_BAR else "DISCARD"))
    print("=" * 96)


if __name__ == "__main__":
    main()
