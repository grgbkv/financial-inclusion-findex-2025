"""U28x (registered 2026-08-26) — EXPLORATORY mapping pass on the untouched micro `fin22` block.

Logged as `exploratory` under the peek rule, BEFORE U28 is registered. No hypothesis, no bar, no
keep. Parent: none (module-opening pass). B2's breadth cell for this cycle: eight of nine micro
`fin22` columns have zero ledger mentions and this is the last reachable untouched micro family
(U26x declared the rest exhausted).

WHAT IT REPORTS, and nothing else:
  (1) every `fin22*` column in the 2024 individual file: value coding, respondents asked, economies;
  (2) the DENOMINATOR each item sits on -- all module adults vs a conditional subsample -- which is
      the whole point of the pass, because U25's trap was a conditional item read as an all-adult
      one. E57 established fin22b/fin22d/fin22e are M3-exact against the country file while
      fin22c/fin22g are conditionally asked; this extends that to the block;
  (3) M3: |micro share - country-file twin| over the module economies, median and max;
  (4) the unweighted cell sizes of the education and income splits U28 will use, so M2 is checked
      BEFORE the claim is written.

It computes NO gradient and NO group difference. Cell SIZES are counts of respondents, not rates.
"""
import numpy as np
import pandas as pd

from micro import Micro


def main():
    mi = Micro()
    df = mi.df
    cols = sorted([c for c in df.columns if c.startswith("fin22")])
    print("=" * 104)
    print("U28x — EXPLORATORY mapping pass on the micro `fin22` borrowing-source block (2024)")
    print("=" * 104)
    print("columns present: %s\n" % ", ".join(cols))

    n_all = len(df)
    print("%-12s %9s %9s %6s  %-28s %s" % ("column", "n_asked", "n_nonmiss", "econ", "value codes (count)", "denominator"))
    print("-" * 104)
    info = {}
    for c in cols:
        s = df[c]
        asked = s.notna()
        vals = s[asked].value_counts().sort_index()
        econ = df.loc[asked, "economy"].nunique()
        coding = ", ".join("%s:%d" % (str(k)[:14], v) for k, v in list(vals.items())[:4])
        info[c] = {"asked": int(asked.sum()), "econ": int(econ), "vals": vals}
        print("%-12s %9d %9d %6d  %-28s" % (c, int(asked.sum()), int(asked.sum()), econ, coding))
    print("\n  file total = %d respondents, %d economies" % (n_all, df["economy"].nunique()))

    # ---- denominator structure: which items are asked of the SAME set of respondents
    print("\n" + "=" * 104)
    print("DENOMINATOR STRUCTURE — respondent sets, and whether each item shares the module base")
    print("=" * 104)
    base = max(info, key=lambda c: info[c]["asked"])
    base_mask = df[base].notna()
    print("largest respondent set: `%s` with %d respondents over %d economies -- taken as the MODULE BASE"
          % (base, info[base]["asked"], info[base]["econ"]))
    for c in cols:
        m = df[c].notna()
        inter = int((m & base_mask).sum())
        print("  %-12s asked of %6d  (%5.1f%% of the module base; %d of them inside it)   %s"
              % (c, info[c]["asked"], 100 * info[c]["asked"] / max(info[base]["asked"], 1), inter,
                 "ALL-MODULE denominator" if info[c]["asked"] >= 0.97 * info[base]["asked"]
                 else "CONDITIONAL subsample"))

    # ---- M3 against the country file, per column where a twin exists
    print("\n" + "=" * 104)
    print("M3 — micro share vs the country-file twin, over the module economies")
    print("=" * 104)
    country = pd.read_csv(Micro.__module__ and __import__("micro").COUNTRY_CSV, low_memory=False)
    country = country[(country["year"] == 2024) & (country["group"] == "all")]
    cser = country.set_index("countrynewwb")
    name_map = {"Czech Republic": "Czechia", "Slovak Republic": "Slovakia"}
    for c in cols:
        if c not in cser.columns:
            print("  %-12s no country-file twin" % c)
            continue
        econs = sorted(df.loc[df[c].notna(), "economy"].unique())
        devs = []
        for e in econs:
            sub = df[(df["economy"] == e) & df[c].notna()]
            if sub.empty or sub["wgt"].sum() == 0:
                continue
            mv = 100 * np.average(sub[c].eq(1).astype(float), weights=sub["wgt"])
            cv = cser[c].get(name_map.get(e, e), np.nan)
            if pd.notna(cv):
                devs.append(abs(mv - float(cv) * 100))
        if devs:
            print("  %-12s n_econ %3d   median |dev| %.3fpp   max |dev| %.3fpp   %s"
                  % (c, len(devs), float(np.median(devs)), float(max(devs)),
                     "M3-EXACT" if max(devs) <= 1.0 else "DIVERGES — different denominator"))
        else:
            print("  %-12s no comparable economies" % c)

    # ---- M2 cell sizes for the splits U28 will use (counts only, no rates)
    print("\n" + "=" * 104)
    print("M2 CELL SIZES for the splits U28 will use (unweighted respondent counts, NO rates)")
    print("=" * 104)
    bm = df[base].notna()
    for label, mask in [("module base", bm), ("module base & account==1", bm & df["account"].eq(1))]:
        sub = df[mask]
        e_lo = int((sub["educ"] == 1).sum())
        e_hi = int(sub["educ"].isin([2, 3]).sum())
        i_lo = int(sub["inc_q"].isin([1, 2]).sum())
        i_hi = int(sub["inc_q"].isin([3, 4, 5]).sum())
        print("  %-26s n=%6d   educ prim-or-less %6d / secondary+ %6d   poorest40 %6d / richest60 %6d"
              % (label, len(sub), e_lo, e_hi, i_lo, i_hi))
    qual = 0
    for e, g in df[bm].groupby("economy"):
        if (g["educ"] == 1).sum() >= 100 and g["educ"].isin([2, 3]).sum() >= 100:
            qual += 1
    print("  economies with >=100 unweighted in BOTH education cells on the module base: %d of %d"
          % (qual, df.loc[bm, "economy"].nunique()))
    print("\n  educ coding: %s" % dict(df.loc[bm, "educ"].value_counts().sort_index()))
    print("  account coding on the module base: %s" % dict(df.loc[bm, "account"].value_counts(dropna=False).sort_index()))


if __name__ == "__main__":
    main()
