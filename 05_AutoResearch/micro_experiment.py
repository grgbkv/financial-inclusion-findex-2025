"""U24x (EXPLORATORY, registered 2026-08-21): mandatory mapping pass on the untouched micro
EMERGENCY-FUND module — `fin24`, `fin24a`, `fin24b`, `fin24c`, `fin24d1`, `fin24d2`, `fin24d3`,
`fin25e1`, `fin25e2`, `fin25e3`, `fin25e4`. Eleven columns, zero ledger mentions.

Logged as EXPLORATORY under the peek rule (2026-07-11). No hypothesis, no threshold, no keep.
This is rule B2's breadth cell for the cycle and the structural half of slot 1.

WHAT IT COMPUTES: labelled value sets with weighted shares, unweighted non-missing n, economies
with >= 100 unweighted non-missing respondents, the split-sample check (is `wgt` the right weight
for this module?), and ONE binary recode of the headline possibility item with its M3 cross-check
against the country file's `fin24aSD_ND`.

WHAT IT MUST NOT COMPUTE, so U24 stays genuinely pre-registered: nothing split by `educ`, `inc_q`,
`age`, `female`, `emp_in`, `urbanicity` or `account`; no gradient, no absorption statistic.
"""
import numpy as np
import pandas as pd

from micro import Micro

COLS = ["fin24", "fin24a", "fin24b", "fin24c", "fin24d1", "fin24d2", "fin24d3",
        "fin25e1", "fin25e2", "fin25e3", "fin25e4"]


def value_block(df, col):
    s = df.dropna(subset=[col, "wgt"])
    if s.empty:
        return None, 0, 0
    tot = s["wgt"].sum()
    shares = (s.groupby(col)["wgt"].sum() / tot * 100).sort_values(ascending=False)
    counts = s.groupby(col).size()
    out = pd.DataFrame({"weighted_share_pp": shares.round(2),
                        "n_unweighted": counts.reindex(shares.index)})
    n_econ = int(s.groupby("economy").size().ge(100).sum())
    return out, int(len(s)), n_econ


def main():
    mi = Micro()
    df = mi.df
    print("=" * 92)
    print("U24x — EXPLORATORY mapping pass, micro emergency-fund module (11 untouched columns)")
    print("file: %d respondents, %d economies, 2024 wave" % (len(df), df["economy"].nunique()))
    print("=" * 92)

    print("\n--- SPLIT-SAMPLE CHECK (is `wgt` the right weight for this module?) ---")
    print("%-10s %10s %10s %8s %10s" % ("col", "n_nonmiss", "share_file", "n_econ", "n_econ>=100"))
    for c in COLS:
        n = int(df[c].notna().sum()) if c in df.columns else -1
        ne = int(df.loc[df[c].notna(), "economy"].nunique()) if c in df.columns else -1
        ne100 = int(df[df[c].notna()].groupby("economy").size().ge(100).sum()) if c in df.columns else -1
        print("%-10s %10d %9.1f%% %8d %10d" % (c, n, 100 * n / len(df), ne, ne100))

    print("\n--- VALUE SETS (labelled), weighted shares ---")
    for c in COLS:
        if c not in df.columns:
            print("\n[%s] ABSENT" % c)
            continue
        blk, n, ne = value_block(df, c)
        print("\n[%s]  n_nonmiss=%d  economies with n>=100: %d" % (c, n, ne))
        if blk is None:
            print("  (empty)")
        else:
            for v, row in blk.iterrows():
                print("   %-58s %7.2f%%  n=%d" % (str(v)[:58], row["weighted_share_pp"],
                                                  row["n_unweighted"]))

    print("\n--- CANDIDATE BINARY RECODE OF THE HEADLINE POSSIBILITY ITEM + M3 ---")
    if "fin24" in df.columns:
        vals = sorted([v for v in df["fin24"].dropna().unique()], key=str)
        print("fin24 raw values: %s" % vals)
        # country file `fin24aSD_ND`: 'very possible' or 'somewhat possible'
        pos = [v for v in vals if isinstance(v, str)
               and ("very possible" in v.lower() or "somewhat possible" in v.lower())]
        print("recode -> 1 for: %s" % pos)
        if pos:
            df["_resilient"] = np.where(df["fin24"].isin(pos), 1.0,
                                        np.where(df["fin24"].notna(), 0.0, np.nan))
            # exclude DK/RF from the denominator only if a DK/RF label exists
            dkrf = [v for v in vals if isinstance(v, str)
                    and ("don't know" in v.lower() or "refuse" in v.lower()
                         or v.strip().lower() in ("dk", "rf", "(dk)", "(rf)"))]
            print("DK/RF labels detected (kept in denominator for the M3 check): %s" % dkrf)
            r, n = mi.rate("_resilient")
            print("pooled weighted rate = %.2fpp on n=%d" % (r, n))
            mi.df = df
            econ = sorted(df.loc[df["_resilient"].notna(), "economy"].unique())[:400]
            g = mi.gate_country_file("_resilient", "fin24aSD_ND", econ, tol_pp=1.0)
            print("M3: %s" % g)
            # per-economy deviation detail so the recode can be judged, not just gated
            c = pd.read_csv(mi.__class__.__module__ and
                            __import__("micro").COUNTRY_CSV, low_memory=False)
            c = c[(c["year"] == 2024) & (c["group"] == "all")].set_index(
                "countrynewwb")["fin24aSD_ND"] * 100
            nm = {"Czech Republic": "Czechia", "Slovak Republic": "Slovakia"}
            devs = []
            for e in econ:
                mv, nn = mi.rate("_resilient", economy=e)
                cv = c.get(nm.get(e, e), np.nan)
                if pd.notna(mv) and pd.notna(cv):
                    devs.append((abs(mv - cv), e, mv, cv))
            devs.sort(reverse=True)
            print("economies compared: %d | median |dev| = %.3fpp | worst five:"
                  % (len(devs), float(np.median([d[0] for d in devs]))))
            for d in devs[:5]:
                print("   %-28s micro %6.2f  country %6.2f  dev %5.2f" % (d[1], d[2], d[3], d[0]))

    print("\n--- ACCOUNT-CONDITIONAL COVERAGE (structural only: cell counts, no rates) ---")
    if "_resilient" in df.columns:
        sub = df[df["_resilient"].notna() & df["account"].notna() & df["educ"].notna()]
        print("respondents with resilience + account + educ all present: %d" % len(sub))
        both = sub[sub["account"] == 1].groupby(["economy", "educ"]).size().unstack(fill_value=0)
        if both.shape[1] >= 2:
            lo, hi = both.columns.min(), both.columns.max()
            qual = both[(both[lo] >= 100) & (both[hi] >= 100)]
            print("educ codes present: %s" % list(both.columns))
            print("economies with n>=100 in BOTH extreme educ cells within account==1: %d of %d"
                  % (len(qual), len(both)))
    print("\nEXPLORATORY — no verdict, no keep. U24 is registered separately.")


if __name__ == "__main__":
    main()
