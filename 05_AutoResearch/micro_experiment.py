"""U26x (exploratory) + U26 (registered 2026-08-23) — the LAST TWO UNTOUCHED micro families:
`fin39` (4 columns, coverage.py label "utility payments") and `fin48`/`fin49` (12 columns,
coverage.py label "digital-risk exposure"). Neither has a country-file twin, so U24x's/U25x's
share-matching identification CANNOT run and identification is STRUCTURAL ONLY (denominator,
response scale, filter profile, M2 economy count). The coverage.py labels are a hand-written
dictionary, not questionnaire text; no behavioural meaning is attached to any item.

U26, REGISTERED. Four-way orientation screen (Documentation obligation 2) of every usable item,
aggregated as the per-economy weighted share of code 1 over THE COLUMN'S OWN non-missing
denominator (agenda item 9.1), M2-filtered at unweighted n >= 100, against `g20_any` in the 2024
cross-section:
    restatement |r| >= 0.80 | aligned +0.30..0.80 | counter-moving -0.80..-0.30 | independent < 0.30
both lenses must agree, else `mixed-lens`. KEEP requires >= 1 counter-moving item on BOTH lenses,
G6 sign-stable, bootstrap (2,000 economy draws) excluding zero, AND rejected by BH at q = 0.10 over
the module's own family (agenda item 9.2, declared IN ADVANCE this time). Registered sign: NEGATIVE.
Screen runs on whichever block clears >= 30 economies at n >= 100; if neither clears, DISCARD on
coverage. Secondary anchor (no bar): `account_t_d`.
"""
import numpy as np
import pandas as pd

from micro import Micro, COUNTRY_CSV

BLOCKS = {
    "fin39": ["fin39a", "fin39b", "fin39c", "fin39d"],
    "fin48_fin49": ["fin48a", "fin48b", "fin48c", "fin48d", "fin48e", "fin48f",
                    "fin49a", "fin49b", "fin49c", "fin49d", "fin49e", "fin49f"],
}
FLAGS = ["account", "account_fin", "account_mob", "anydigpayment", "internet_use",
         "merchantpay_dig", "pay_utilities", "saved", "borrowed", "receive_wages"]
NAME_FIX = {"Czech Republic": "Czechia", "Slovak Republic": "Slovakia"}
M2_MIN = 100
MIN_ECON = 30
RNG = np.random.default_rng(20260823)


def country_2024():
    c = pd.read_csv(COUNTRY_CSV, low_memory=False)
    c = c[(c["year"] == 2024) & (c["group"] == "all") & c["regionwb24_hi"].notna()]
    return c.set_index("countrynewwb")


# ------------------------------------------------------------------ U26x mapping pass
def mapping_pass(mi, c):
    df = mi.df
    print("=" * 100)
    print("U26x — EXPLORATORY structural mapping pass: the last two untouched micro families")
    print("=" * 100)
    print("No country-file twin exists for fin39/fin48/fin49 (verified: 0 matching columns in "
          "GlobalFindexDatabase2025.csv),\nso U24x/U25x share-matching cannot run. Identification "
          "below is STRUCTURAL ONLY and is not M3-validated.\n")

    m2_counts = {}
    for block, cols in BLOCKS.items():
        anchor_col = cols[0]
        asked = df[df[anchor_col].notna()]
        econs = sorted(asked["economy"].unique())
        in_econ = df[df["economy"].isin(econs)]
        print("-" * 100)
        print("BLOCK %s — %d columns" % (block, len(cols)))
        print("  asked: %d respondents (%.1f%% of file) in %d economies; those economies hold "
              "%d respondents" % (len(asked), 100 * len(asked) / len(df), len(econs), len(in_econ)))
        share_asked = in_econ.groupby("economy")[anchor_col].apply(lambda s: 100 * s.notna().mean())
        print("  share of each block economy's respondents asked: min %.1f%% median %.1f%% "
              "max %.1f%%" % (share_asked.min(), share_asked.median(), share_asked.max()))
        print("  => %s" % ("ECONOMY-LEVEL subsample (economies complete)" if share_asked.min() > 99
                           else "WITHIN-ECONOMY conditional/split subsample — every statistic on "
                                "this block is CONDITIONAL"))

        print("\n  %-9s %9s %8s %8s %10s  %s" % ("col", "n", "n_econ", "n>=100", "code1_pct",
                                                 "code distribution (unweighted)"))
        for col in cols:
            s = df[col].dropna()
            ne = int(df.loc[df[col].notna(), "economy"].nunique())
            per = df[df[col].notna()].groupby("economy").size()
            n100 = int((per >= M2_MIN).sum())
            vc = s.value_counts().sort_index()
            dist = "  ".join("%d:%d" % (int(k), v) for k, v in vc.items())
            sub = df[df[col].notna()].dropna(subset=["wgt"])
            p1 = 100 * np.average(sub[col].eq(1).astype(float), weights=sub["wgt"])
            print("  %-9s %9d %8d %8d %9.1f%%  %s" % (col, len(s), ne, n100, p1, dist))
            m2_counts.setdefault(block, {})[col] = n100
        print("  per-economy asked-n: median %.0f min %d max %d"
              % (per.median(), per.min(), per.max()))

        print("\n  FILTER PROFILE — pooled unweighted mean of labelled binaries, "
              "inside the asked sample vs whole file:")
        for f in FLAGS:
            if f not in df.columns:
                continue
            a = pd.to_numeric(asked[f], errors="coerce")
            b = pd.to_numeric(df[f], errors="coerce")
            if a.notna().sum() == 0:
                continue
            print("    %-16s asked %.3f (n=%d)   file %.3f   diff %+.3f"
                  % (f, a.mean(), a.notna().sum(), b.mean(), a.mean() - b.mean()))

        print("\n  PARTITION CHECK (weighted composition over each column's own denominator):")
        for col in cols:
            s = df[df[col].notna()].dropna(subset=["wgt"])
            sh = s.groupby(col)["wgt"].sum() / s["wgt"].sum() * 100
            print("    %-9s " % col + "  ".join("%d:%5.1f%%" % (k, v) for k, v in sh.items()))

        print("\n  NESTING (is a column a follow-up of another in the same block?):")
        base = df[cols[0]].notna()
        for col in cols[1:]:
            m = df[col].notna()
            print("    %-9s n=%6d | subset of %s: %s | overlap %d"
                  % (col, int(m.sum()), cols[0], "yes" if (m & ~base).sum() == 0 else "no",
                     int((m & base).sum())))
        print()

    print("=" * 100)
    print("REGISTERED SCREEN-ELIGIBILITY RULE (fixed before the run): a block carries the screen "
          "only if\n>= %d economies clear unweighted n >= %d." % (MIN_ECON, M2_MIN))
    eligible = []
    for block, cols in BLOCKS.items():
        best = max(m2_counts[block].values())
        ok = best >= MIN_ECON
        print("  %-12s max economies at n>=%d across its columns: %3d  ->  %s"
              % (block, M2_MIN, best, "ELIGIBLE" if ok else "NOT ELIGIBLE"))
        if ok:
            eligible.append(block)
    print("=" * 100)
    return eligible, m2_counts


# ------------------------------------------------------------------ U26 screen machinery
def wcorr(x, y, w):
    m = pd.notna(x) & pd.notna(y) & pd.notna(w)
    x, y, w = x[m], y[m], w[m]
    if len(x) < 10:
        return np.nan, len(x)
    mx, my = np.average(x, weights=w), np.average(y, weights=w)
    cov = np.average((x - mx) * (y - my), weights=w)
    sx = np.sqrt(np.average((x - mx) ** 2, weights=w))
    sy = np.sqrt(np.average((y - my) ** 2, weights=w))
    return float(cov / (sx * sy)), len(x)


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
    return a if a == b else "mixed-lens"


def boot_ci(x, y, w, draws=2000):
    idx = np.array(x.index)
    out = []
    for _ in range(draws):
        take = idx[RNG.choice(len(idx), len(idx), replace=True)]
        r, _n = wcorr(pd.Series(x.loc[take].values), pd.Series(y.loc[take].values),
                      pd.Series(w.loc[take].values))
        if pd.notna(r):
            out.append(r)
    out = np.array(out)
    lo, hi = np.percentile(out, [2.5, 97.5])
    p = 2 * min((out <= 0).mean(), (out >= 0).mean())
    return float(lo), float(hi), float(p)


def screen(items, anchor_s, pop, label, do_boot=True):
    print("\n" + "=" * 100)
    print("U26 — four-way orientation screen vs `%s`" % label)
    print("=" * 100)
    print("%-14s %7s %7s %15s %5s %7s  %s"
          % ("item", "r_w", "r_u", "class", "n", "neff", "G6 drop5 / largest LOO (named)"))
    rows = []
    for name, ser in items.items():
        common = ser.dropna().index.intersection(anchor_s.dropna().index).intersection(pop.index)
        if len(common) < 10:
            continue
        x, y, w = ser.loc[common], anchor_s.loc[common], pop.loc[common]
        rw, n = wcorr(x, y, w)
        ru, _ = wcorr(x, y, pd.Series(1.0, index=common))
        if pd.isna(rw):
            continue
        neff = (w.sum() ** 2) / (w ** 2).sum()
        keep = w.sort_values(ascending=False).index[5:]
        r_drop, _ = wcorr(x.loc[keep], y.loc[keep], w.loc[keep])
        loo = {}
        for e in common:
            k = common.drop(e)
            r_i, _ = wcorr(x.loc[k], y.loc[k], w.loc[k])
            loo[e] = r_i - rw
        big = max(loo, key=lambda e: abs(loo[e]))
        cls = classify(rw, ru)
        ci = boot_ci(x, y, w) if do_boot else None
        rows.append({"item": name, "r_w": rw, "r_u": ru, "cls": cls, "n": n, "neff": neff,
                     "r_drop": r_drop, "loo_econ": big, "loo_d": loo[big], "ci": ci})
        print("%-14s %+7.3f %+7.3f %15s %5d %7.1f  drop5 %+.3f / %s %+.3f"
              % (name, rw, ru, cls, n, neff, r_drop, big[:16], loo[big]))
        if ci:
            print("%-14s   bootstrap 2,000 economy draws: [%+.3f, %+.3f]  p_boot=%.4f"
                  % ("", ci[0], ci[1], ci[2]))
    return rows


def bh(rows, q=0.10):
    ps = sorted([(r["ci"][2], r["item"]) for r in rows if r["ci"]])
    m = len(ps)
    print("\nBH FAMILY-WISE CORRECTION over the module's own family of %d tests (q = %.2f) "
          "— registered IN ADVANCE (agenda item 9.2):" % (m, q))
    kmax = 0
    for i, (p, name) in enumerate(ps, 1):
        crit = q * i / m
        if p <= crit:
            kmax = i
        print("  %-14s p_boot=%.4f  BH crit=%.4f  %s" % (name, p, crit, "reject" if p <= crit else ""))
    rejected = {n for _p, n in ps[:kmax]}
    print("  BH rejects %d of %d." % (kmax, m))
    return rejected


def main():
    mi = Micro()
    c = country_2024()
    eligible, m2_counts = mapping_pass(mi, c)

    df = mi.df
    pop = c["pop_adult"].dropna()

    if not eligible:
        print("\nNO BLOCK CLEARS THE REGISTERED ELIGIBILITY RULE -> U26 is a DISCARD on coverage.")
        return

    def share_own(col):
        """per-economy weighted share of code 1 over the column's OWN non-missing denominator,
        M2-filtered at unweighted n >= 100 (agenda item 9.1: the own denominator is primary)."""
        s = df[df[col].notna()].dropna(subset=["wgt"])
        g = s.assign(_h=s[col].eq(1).astype(float) * s["wgt"]).groupby(
            "economy")[["_h", "wgt"]].sum()
        n = s.groupby("economy").size()
        ser = (g["_h"] / g["wgt"] * 100)[n >= M2_MIN]
        ser.index = [NAME_FIX.get(e, e) for e in ser.index]
        return ser

    def share_pop(col, econs):
        """the same item on the POPULATION denominator (all respondents in the block economies)
        — reported as the U25 contrast, never as the primary."""
        s = df[df["economy"].isin(econs)].dropna(subset=["wgt"])
        g = s.assign(_h=df[col].eq(1).reindex(s.index).fillna(False).astype(float)
                     * s["wgt"]).groupby("economy")[["_h", "wgt"]].sum()
        ser = (g["_h"] / g["wgt"] * 100)
        ser.index = [NAME_FIX.get(e, e) for e in ser.index]
        return ser

    for block in eligible:
        cols = [x for x in BLOCKS[block] if m2_counts[block][x] >= MIN_ECON]
        econs = sorted(df.loc[df[BLOCKS[block][0]].notna(), "economy"].unique())
        print("\n\n" + "#" * 100)
        print("# U26 REGISTERED SCREEN — block %s, screenable columns %s" % (block, cols))
        print("#" * 100)
        items = {col: share_own(col) for col in cols}

        for anchor in ("g20_any", "account_t_d"):
            a = (c[anchor] * 100).dropna()
            rows = screen(items, a, pop, anchor + "  [OWN-BLOCK denominator, M2-filtered]")
            if anchor != "g20_any":
                continue
            rejected = bh(rows)
            cm = [r for r in rows if r["cls"] == "counter-moving"]
            print("\nREGISTERED KEEP CONDITION (>=1 counter-moving on BOTH lenses, G6 sign-stable,"
                  "\nbootstrap excluding zero, AND rejected by BH at q=0.10 over the module family):")
            if not cm:
                print("  0 counter-moving items -> DISCARD as registered.")
            for r in cm:
                sign_ok = np.sign(r["r_drop"]) == np.sign(r["r_w"])
                ci_ok = r["ci"] and r["ci"][0] < 0 and r["ci"][1] < 0
                bh_ok = r["item"] in rejected
                print("  %-14s G6 sign %s | CI excludes 0 %s | BH reject %s -> %s"
                      % (r["item"], "OK" if sign_ok else "FAIL", "OK" if ci_ok else "FAIL",
                         "OK" if bh_ok else "FAIL",
                         "KEEP" if (sign_ok and ci_ok and bh_ok) else "FAIL"))
            print("\nclassification counts vs g20_any: %s"
                  % dict(pd.Series([r["cls"] for r in rows]).value_counts()))

            # G4 on the declared frame
            idx = [e for e in items[cols[0]].index if e in pop.index]
            print("G4 (declared frame = the economies that field the module, M2-filtered): "
                  "%d economies, %.1f%% of country-file 2024 adult population"
                  % (len(idx), 100 * pop.reindex(idx).sum() / pop.sum()))
            inc = c.reindex(idx)
            print("income mix: %s" % dict(inc["incomegroupwb24"].value_counts()))

            # --- agenda item 9.1: the denominator diagnostic, beside any negative class
            print("\nDENOMINATOR DIAGNOSTIC (agenda item 9.1) — the same items on the POPULATION "
                  "denominator,\nplus the complement factor's own correlation with the anchor:")
            items_pop = {col: share_pop(col, econs) for col in cols}
            rows_pop = screen(items_pop, a, pop,
                              "g20_any  [POPULATION denominator — contrast only]", do_boot=False)
            pmap = {r["item"]: r for r in rows_pop}
            for r in rows:
                q = pmap.get(r["item"])
                if q:
                    print("  %-14s own-denom r_w %+.3f r_u %+.3f (%-14s) | pop-denom r_w %+.3f "
                          "r_u %+.3f (%s)" % (r["item"], r["r_w"], r["r_u"], r["cls"],
                                              q["r_w"], q["r_u"], q["cls"]))
            base = BLOCKS[block][0]
            pen = df[df["economy"].isin(econs)].dropna(subset=["wgt"])
            gp = pen.assign(_h=df[base].notna().reindex(pen.index).fillna(False).astype(float)
                            * pen["wgt"]).groupby("economy")[["_h", "wgt"]].sum()
            penetration = (gp["_h"] / gp["wgt"] * 100)
            penetration.index = [NAME_FIX.get(e, e) for e in penetration.index]
            comp = (100 - penetration).reindex(idx).dropna()
            k = comp.index.intersection(a.index).intersection(pop.index)
            rwc, _ = wcorr(comp.loc[k], a.loc[k], pop.loc[k])
            ruc, _ = wcorr(comp.loc[k], a.loc[k], pd.Series(1.0, index=k))
            print("  COMPLEMENT FACTOR r(100 - block-asked share, g20_any) over %d economies: "
                  "weighted %+.3f, unweighted %+.3f -> class %s"
                  % (len(k), rwc, ruc, classify(rwc, ruc)))


if __name__ == "__main__":
    main()
