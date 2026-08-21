"""E55 (pre-registered 2026-08-21): the LEDGER-WIDE REPORTING-SET AUDIT — agenda item 8.1.

Parent: E53. Design: audit. Frame: pan_dev. Windows: all four transitions.

WHY. Rule B20 (2026-08-20) requires a balanced economy set on any path, long difference or Delta.
E53 found the four-item cash "rebound" was largely six economies -- China the largest -- dropping
out of the ITEMS while staying in the WAVE. No experiment in the ledger had ever checked whether
its own wave-to-wave comparison held the economy set fixed, so PAPER_DRAFT_v4 §12 states the risk
as UNQUANTIFIED. This quantifies it.

AUDIT SET (mechanical, not chosen): every country-file column the ledger has touched, detected with
coverage.py's word-boundary regex over findings.tsv + RESEARCH_LOG.md + results_prediction.tsv,
restricted to columns reporting >= 30 developing-panel economies in at least two waves.

PER COLUMN x TRANSITION: n at t, n at t+1, n balanced, n dropped, n added; population share of the
droppers inside the t reporting set; the NAME of the largest dropper; Delta_unbalanced (wmean over
each wave's own reporters), Delta_balanced (intersection only), and discrepancy = unbal - bal.

REGISTERED CLAIM: E53's attrition failure is LOCALIZED to narrow items and does not characterize
the ledger.
REGISTERED SIGN (B15): among cells with a non-trivial drop (>= 3 economies or >= 5% of the t
population), the discrepancy's sign follows sign(retained mean - dropped mean) at t in a MAJORITY.
KEEP BAR, three branches fixed in advance:
  (a) median |discrepancy| over all cells < 0.50pp, AND
  (b) share of cells with |discrepancy| >= 2.0pp below 10%, AND
  (c) among cells backing a KEPT ledger finding, none has |discrepancy| >= 2.0pp.
  Branch 1 (a,b,c hold)      -> keep.
  Branch 2 (a,b hold, c fails) -> keep with corrections owed; the exposed keeps are named.
  Branch 3 (a or b fails)     -> discard; every column above the 2pp bar is named.
DIAGNOSTIC (labelled, NOT part of the bar): association designs are balanced automatically by the
pairwise-complete construction but lose SAMPLE; per ledger association cell, report the n of the
pairwise-complete set against the headline 76-77 and the population share it holds.
GATES: G3 the ledger's own declared variants, carried unchanged; G4 every cell carries n and
population share by construction; G5 na; G6 na (no association is claimed).
"""
import os
import re

import numpy as np
import pandas as pd

from harness import Findex, YEARS

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER_FILES = ["findings.tsv", "RESEARCH_LOG.md", "results_prediction.tsv"]
TRANSITIONS = [(a, b) for a, b in zip(YEARS, YEARS[1:])]
MIN_ECON = 30
MEDIAN_BAR = 0.50
BIG_BAR = 2.0
BIG_SHARE_BAR = 0.10

# Columns backing a KEPT ledger finding (branch (c)). Read off LEDGER_INDEX.md's keeps table.
KEEP_COLS = {
    "account_t_d", "fiaccount_t_d", "mobileaccount_t_d", "g20_any", "fin17a_17a1_d",
    "fin22a_22a1_22g_d", "fin32_acc", "save_any_t_d", "fin31d", "fin34c", "fin42", "fin43c",
    "merchant_pay", "fh1", "fh2", "fh1_fh2", "internet", "dig_acc",
}


def ledger_text():
    parts = []
    for f in LEDGER_FILES:
        p = os.path.join(HERE, f)
        if os.path.exists(p):
            parts.append(open(p, encoding="utf-8", errors="ignore").read())
    return "\n".join(parts)


def used_columns(text, columns):
    used = []
    for c in columns:
        if re.search(r"(?<![A-Za-z0-9_])" + re.escape(c) + r"(?![A-Za-z0-9_])", text):
            used.append(c)
    return used


def wmean(d, col):
    s = d.dropna(subset=[col, "pop_adult"])
    return np.nan if s.empty else float(np.average(s[col], weights=s["pop_adult"])) * 100


def main():
    fx = Findex()
    frame = fx.pan_dev
    meta = {"year", "countrynewwb", "countrycode", "regionwb24_hi", "incomegroupwb24",
            "adultpopulation", "pop_adult", "group", "codewb", "region", "income"}
    numeric = [c for c in frame.columns
               if c not in meta and pd.api.types.is_numeric_dtype(frame[c])]
    text = ledger_text()
    touched = used_columns(text, numeric)

    # eligibility: >= MIN_ECON developing-panel economies in at least two waves
    elig = []
    for c in touched:
        waves = [len(frame[(frame["year"] == y)].dropna(subset=[c, "pop_adult"]))
                 for y in YEARS]
        if sum(w >= MIN_ECON for w in waves) >= 2:
            elig.append(c)
    elig.sort()

    print("=" * 108)
    print("E55 — LEDGER-WIDE REPORTING-SET AUDIT (agenda item 8.1, rule B20)")
    print("country-file numeric columns: %d | ledger-touched: %d | eligible (>=%d economies in "
          ">=2 waves): %d" % (len(numeric), len(touched), MIN_ECON, len(elig)))
    print("frame: pan_dev | transitions: %s" % ", ".join("%d-%d" % t for t in TRANSITIONS))
    print("=" * 108)

    rows = []
    for c in elig:
        for (a, b) in TRANSITIONS:
            da = frame[frame["year"] == a].dropna(subset=[c, "pop_adult"])
            db = frame[frame["year"] == b].dropna(subset=[c, "pop_adult"])
            if len(da) < MIN_ECON or len(db) < MIN_ECON:
                continue
            sa = set(da["countrynewwb"]); sb = set(db["countrynewwb"])
            both = sa & sb
            dropped = sa - sb
            added = sb - sa
            if len(both) < MIN_ECON:
                continue
            pop_a = da["pop_adult"].sum()
            drop_pop = da[da["countrynewwb"].isin(dropped)]["pop_adult"].sum()
            add_pop = db[db["countrynewwb"].isin(added)]["pop_adult"].sum()
            biggest = "-"
            if dropped:
                dd = da[da["countrynewwb"].isin(dropped)].sort_values("pop_adult",
                                                                     ascending=False)
                biggest = "%s (%.1f%%)" % (dd.iloc[0]["countrynewwb"],
                                           100 * dd.iloc[0]["pop_adult"] / pop_a)
            d_unbal = wmean(db, c) - wmean(da, c)
            d_bal = (wmean(db[db["countrynewwb"].isin(both)], c)
                     - wmean(da[da["countrynewwb"].isin(both)], c))
            retained_a = wmean(da[da["countrynewwb"].isin(both)], c)
            dropped_a = wmean(da[da["countrynewwb"].isin(dropped)], c) if dropped else np.nan
            rows.append({
                "col": c, "win": "%d-%d" % (a, b), "n_a": len(da), "n_b": len(db),
                "n_bal": len(both), "n_drop": len(dropped), "n_add": len(added),
                "drop_pop_share": 100 * drop_pop / pop_a if pop_a else np.nan,
                "add_pop_share": 100 * add_pop / db["pop_adult"].sum() if len(db) else np.nan,
                "biggest_drop": biggest, "d_unbal": d_unbal, "d_bal": d_bal,
                "disc": d_unbal - d_bal, "retained_a": retained_a, "dropped_a": dropped_a,
                "keep_col": c in KEEP_COLS})
    R = pd.DataFrame(rows)

    print("\n%d column x transition cells audited over %d columns.\n"
          % (len(R), R["col"].nunique()))
    med = float(R["disc"].abs().median())
    big = R[R["disc"].abs() >= BIG_BAR]
    share_big = len(big) / len(R)
    print("PRIMARY BARS")
    a_ok = med < MEDIAN_BAR
    b_ok = share_big < BIG_SHARE_BAR
    print("  (a) median |discrepancy| = %.4fpp  (bar < %.2f)  -> %s"
          % (med, MEDIAN_BAR, "PASS" if a_ok else "FAIL"))
    print("  (b) cells with |disc| >= %.1fpp: %d of %d = %.1f%%  (bar < %.0f%%)  -> %s"
          % (BIG_BAR, len(big), len(R), 100 * share_big, 100 * BIG_SHARE_BAR,
             "PASS" if b_ok else "FAIL"))
    keep_big = big[big["keep_col"]]
    c_ok = len(keep_big) == 0
    print("  (c) keep-backing cells with |disc| >= %.1fpp: %d  -> %s"
          % (BIG_BAR, len(keep_big), "PASS" if c_ok else "FAIL"))
    branch = 1 if (a_ok and b_ok and c_ok) else (2 if (a_ok and b_ok) else 3)
    print("  ==> BRANCH %d: %s" % (branch, {1: "KEEP", 2: "KEEP WITH CORRECTIONS OWED",
                                            3: "DISCARD"}[branch]))

    print("\nDISTRIBUTION OF |discrepancy| (pp)")
    q = R["disc"].abs().quantile([0.5, 0.75, 0.9, 0.95, 0.99, 1.0])
    print("  " + "  ".join("p%02d=%.3f" % (int(k * 100), v) for k, v in q.items()))
    print("  cells with a perfectly balanced set (n_drop=0 and n_add=0): %d of %d (%.1f%%)"
          % (int(((R["n_drop"] == 0) & (R["n_add"] == 0)).sum()), len(R),
             100 * ((R["n_drop"] == 0) & (R["n_add"] == 0)).mean()))
    print("  cells with any dropper: %d (%.1f%%) | any adder: %d (%.1f%%)"
          % (int((R["n_drop"] > 0).sum()), 100 * (R["n_drop"] > 0).mean(),
             int((R["n_add"] > 0).sum()), 100 * (R["n_add"] > 0).mean()))

    print("\nWORST 20 CELLS BY |discrepancy|")
    print("  %-22s %-10s %4s %4s %5s %4s %7s  %-26s %8s %8s %8s %s"
          % ("col", "window", "n_a", "n_b", "n_bal", "drp", "drp_pop", "largest dropper",
             "d_unbal", "d_bal", "disc", "keep?"))
    for _, r in R.reindex(R["disc"].abs().sort_values(ascending=False).index).head(20).iterrows():
        print("  %-22s %-10s %4d %4d %5d %4d %6.1f%%  %-26s %+8.2f %+8.2f %+8.2f %s"
              % (r["col"], r["win"], r["n_a"], r["n_b"], r["n_bal"], r["n_drop"],
                 r["drop_pop_share"], r["biggest_drop"][:26], r["d_unbal"], r["d_bal"],
                 r["disc"], "YES" if r["keep_col"] else ""))

    print("\nKEEP-BACKING COLUMNS, every cell (branch (c) evidence)")
    K = R[R["keep_col"]].copy()
    print("  %d cells over %d columns | median |disc| = %.4fpp | max |disc| = %.3fpp"
          % (len(K), K["col"].nunique(), K["disc"].abs().median(), K["disc"].abs().max()))
    worst = K.reindex(K["disc"].abs().sort_values(ascending=False).index).head(12)
    for _, r in worst.iterrows():
        print("   %-22s %-10s n %3d->%3d bal %3d drop %2d (%5.1f%% pop, %s)  unbal %+7.2f "
              "bal %+7.2f disc %+6.2f" % (r["col"], r["win"], r["n_a"], r["n_b"], r["n_bal"],
                                          r["n_drop"], r["drop_pop_share"],
                                          r["biggest_drop"][:22], r["d_unbal"], r["d_bal"],
                                          r["disc"]))

    print("\nREGISTERED SIGN CHECK (B15) — non-trivial drops only "
          "(>=3 economies or >=5%% of the t population)")
    NT = R[((R["n_drop"] >= 3) | (R["drop_pop_share"] >= 5.0)) & R["dropped_a"].notna()].copy()
    NT["pred"] = np.sign(NT["retained_a"] - NT["dropped_a"])
    NT["obs"] = np.sign(NT["disc"])
    agree = NT[NT["pred"] != 0]
    hit = float((agree["pred"] == agree["obs"]).mean()) if len(agree) else np.nan
    print("  %d non-trivial-drop cells | sign(disc) matches sign(retained - dropped) at t in "
          "%d of %d = %.1f%%  -> %s" % (len(NT), int((agree["pred"] == agree["obs"]).sum()),
                                        len(agree), 100 * hit,
                                        "MAJORITY, as registered" if hit > 0.5 else "NOT a majority"))
    print("  mean |disc| on non-trivial-drop cells %.3fpp vs %.3fpp elsewhere"
          % (NT["disc"].abs().mean(), R[~R.index.isin(NT.index)]["disc"].abs().mean()))

    print("\nDIAGNOSTIC (labelled, no verdict) — SAMPLE exposure of association designs")
    RAILS = [("E1  mobilemoney~saving", "mobileaccount_t_d", "fin17a_17a1_d"),
             ("E10 wagedigi~saving", "fin32_acc", "fin17a_17a1_d"),
             ("E12 digipay~saving", "g20_any", "fin17a_17a1_d"),
             ("E11 borrowing~saving", "fin22a_22a1_22g_d", "fin17a_17a1_d"),
             ("E13 FIacct~mobilemoney", "fiaccount_t_d", "mobileaccount_t_d"),
             ("E14 mobilemoney~digipay", "mobileaccount_t_d", "g20_any"),
             ("E48b fin31d~fin34c", "fin31d", "fin34c")]
    for label, x, y in RAILS:
        if x not in frame.columns or y not in frame.columns:
            continue
        line = []
        for (a, b) in TRANSITIONS:
            w = fx.country_panel(frame, x, [a, b]).join(
                fx.country_panel(frame, y, [a, b]), lsuffix="_x", rsuffix="_y")
            need = ["%d_x" % a, "%d_x" % b, "%d_y" % a, "%d_y" % b]
            if any(k not in w.columns for k in need):
                line.append("%d-%d n/a" % (a, b))
                continue
            dx = w["%d_x" % b] - w["%d_x" % a]
            dy = w["%d_y" % b] - w["%d_y" % a]
            m = dx.notna() & dy.notna() & w["pop_x"].notna()
            n = int(m.sum())
            # denominator held fixed at the 2024 adult population of the whole dev panel,
            # so the shares are comparable across windows (rule B20's own logic)
            base_pop = frame[frame["year"] == 2024]["pop_adult"].sum()
            share = (w.loc[m, "pop_x"].sum() / base_pop) if n else np.nan
            line.append("%d-%d n=%d (%.0f%% pop)" % (a, b, n, 100 * share))
        print("  %-24s %s  [headline set: %d economies]"
              % (label, " | ".join(line),
                 frame[frame["year"] == 2024].dropna(subset=["account_t_d"])
                 ["countrynewwb"].nunique()))

    R.to_csv(os.path.join(HERE, "e55_reporting_set_audit.csv"), index=False)
    print("\nfull per-cell table written to e55_reporting_set_audit.csv (%d rows)" % len(R))


if __name__ == "__main__":
    main()
