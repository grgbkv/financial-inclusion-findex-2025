"""U25x (exploratory) + U25 (registered 2026-08-22) — the untouched `fin13`/`fin14` MOBILE-MONEY
USAGE module: mapping pass plus the four-way orientation screen.

U25x, MAPPING PASS (exploratory under the peek rule). The 13 micro columns carry NUMERIC codes,
not text labels, so U24x's identification method is applied unchanged: for every column x every
code, the per-economy weighted share is matched against every labelled country-file `fin13*`/
`fin14*` column (38 of them, 2024, group == "all"). A code is declared IDENTIFIED at median
|dev| <= 0.10pp across common economies. Item meanings are inferred from country column NAMES and
from the share match only -- there is no questionnaire in the repo (HARNESS_V2_NOTES items 5-6).

U25, REGISTERED. Four-way orientation screen (Documentation obligation 2) of every identified item
against `g20_any` in the 2024 cross-section over the module's own economy set:
    restatement |r| >= 0.80 | aligned +0.30..0.80 | counter-moving -0.80..-0.30 | independent < 0.30
both lenses must agree, else `mixed-lens`. KEEP requires >= 1 counter-moving item on BOTH lenses,
G6 sign-stable, bootstrap (2,000 economy draws) excluding zero. Registered sign: NEGATIVE.
Secondary anchor (no bar): `mobileaccount_t_d`.
"""
import numpy as np
import pandas as pd

from micro import Micro, COUNTRY_CSV

MCOLS = ["fin13_1", "fin13a", "fin13b", "fin13c", "fin13d", "fin13e", "fin13f", "fin13f_1",
         "fin14a", "fin14b", "fin14c", "fin14d", "fin14e"]
NAME_FIX = {"Czech Republic": "Czechia", "Slovak Republic": "Slovakia"}
RNG = np.random.default_rng(20260822)


def country_2024():
    c = pd.read_csv(COUNTRY_CSV, low_memory=False)
    c = c[(c["year"] == 2024) & (c["group"] == "all") & c["regionwb24_hi"].notna()]
    return c.set_index("countrynewwb")


# ------------------------------------------------------------------ U25x mapping pass
def mapping_pass(mi, c):
    df = mi.df
    ccols = [x for x in c.columns if x.startswith(("fin13", "fin14")) and not x.endswith("_s")]

    def econ_share(mask, denom_mask):
        s = df[denom_mask].dropna(subset=["wgt"])
        h = mask.reindex(s.index).fillna(False).astype(float)
        g = s.assign(_h=h * s["wgt"]).groupby("economy")[["_h", "wgt"]].sum()
        return g["_h"] / g["wgt"] * 100

    def dev_vs(mask, denom_mask, ccol):
        r, t = econ_share(mask, denom_mask), c[ccol] * 100
        idx = [e for e in r.index if NAME_FIX.get(e, e) in t.index
               and pd.notna(t.get(NAME_FIX.get(e, e)))]
        if len(idx) < 15:
            return np.nan, np.nan, len(idx)
        d = np.abs(np.array([r[e] - t[NAME_FIX.get(e, e)] for e in idx]))
        return float(np.median(d)), float(d.max()), len(idx)

    print("=" * 96)
    print("U25x — EXPLORATORY mapping pass, micro MOBILE-MONEY USAGE module (13 untouched columns)")
    print("=" * 96)
    print("%-10s %10s %9s %8s %12s" % ("col", "n_nonmiss", "share", "n_econ", "n_econ>=100"))
    for col in MCOLS:
        n = int(df[col].notna().sum())
        ne = int(df.loc[df[col].notna(), "economy"].nunique())
        n100 = int(df[df[col].notna()].groupby("economy").size().ge(100).sum())
        print("%-10s %10d %8.1f%% %8d %12d" % (col, n, 100 * n / len(df), ne, n100))

    # --- denominator structure: economy-level subsample or within-economy conditional?
    econs = sorted(df.loc[df["fin13a"].notna(), "economy"].unique())
    sub = df[df["economy"].isin(econs)]
    cov = sub.groupby("economy").apply(
        lambda g: pd.Series({"n_econ_total": len(g),
                             "n_fin13a": int(g["fin13a"].notna().sum()),
                             "share_asked": 100 * g["fin13a"].notna().mean(),
                             "mm_acct_rate": 100 * g["account_mob"].mean(skipna=True)}),
        include_groups=False)
    print("\nDENOMINATOR STRUCTURE — %d module economies, %d respondents in those economies, "
          "%d asked fin13a" % (len(econs), len(sub), int(sub["fin13a"].notna().sum())))
    print("  share of each module economy's respondents asked fin13a: min %.1f%% median %.1f%% "
          "max %.1f%%" % (cov["share_asked"].min(), cov["share_asked"].median(),
                          cov["share_asked"].max()))
    print("  => WITHIN-ECONOMY CONDITIONAL subsample" if cov["share_asked"].max() < 99
          else "  => ECONOMY-LEVEL subsample")
    amob = sub.loc[sub["fin13a"].notna(), "account_mob"]
    print("  account_mob inside the module sample: mean %.3f, n_nonnull %d  (variance usable: %s)"
          % (amob.mean(), amob.notna().sum(), "yes" if 0.05 < amob.mean() < 0.95 else "NO"))
    print("  fin13_1 sample vs fin13a sample: %d vs %d respondents"
          % (int(df['fin13_1'].notna().sum()), int(df['fin13a'].notna().sum())))
    a13, a14 = df["fin13a"].notna(), df["fin14a"].notna()
    print("  BLOCK STRUCTURE: fin13a n=%d (account_mob mean %.3f) | fin14a n=%d "
          "(account_mob mean %.3f) | overlap %d respondents"
          % (int(a13.sum()), df.loc[a13, "account_mob"].mean(),
             int(a14.sum()), df.loc[a14, "account_mob"].mean(), int((a13 & a14).sum())))
    print("  => the two blocks are DISJOINT COMPLEMENTARY subsamples: fin13 is asked of "
          "mobile-money HOLDERS, fin14 of NON-holders (any-account rate %.3f among them)."
          % df.loc[a14, "account"].mean())

    # --- code identification
    # DISCLOSED POST-RUN PATCH (exploratory pass only): the own-column denominator identified
    # ZERO code-cells, because the module is asked only of mobile-money accountholders while the
    # country twin is a share of ALL adults. The pass therefore tries BOTH denominators. The
    # registered U25 screen (anchor, bars, keep condition) is untouched.
    in_mod = df["economy"].isin(econs)
    print("\nBEST single-code match per code, TWO denominators:"
          "  [own] = the column's own nonmissing set;  [pop] = all respondents in the 36 economies")
    ident = {}
    for mcol in MCOLS:
      for dlabel, denom in (("own", df[mcol].notna()), ("pop", in_mod)):
        for code in sorted(df[mcol].dropna().unique()):
            if (df[mcol] == code).sum() < 50:
                continue
            best = []
            for ccol in ccols:
                med, mx, n = dev_vs(df[mcol].eq(code), denom, ccol)
                if pd.notna(med):
                    best.append((med, mx, ccol, n))
            best.sort()
            if best:
                med, mx, ccol, n = best[0]
                flag = "IDENT" if med <= 0.10 else ("close" if med <= 1.0 else "")
                if med <= 1.0:
                    print("  [%s] %-9s code %-3.0f -> %-14s med|dev|=%7.3f max=%7.3f (n=%d) %s"
                          % (dlabel, mcol, code, ccol, med, mx, n, flag))
                if med <= 0.10:
                    ident[(mcol, int(code))] = (ccol, med, mx, n, dlabel)
    print("\nIDENTIFIED (median |dev| <= 0.10pp): %d code-cells" % len(ident))

    # --- composition check: do the codes of each question partition?
    print("\nPARTITION CHECK (weighted composition of each column over its own denominator):")
    for mcol in MCOLS:
        s = df[df[mcol].notna()].dropna(subset=["wgt"])
        sh = s.groupby(mcol)["wgt"].sum() / s["wgt"].sum() * 100
        print("  %-9s " % mcol + "  ".join("%d:%5.1f%%" % (k, v) for k, v in sh.items()))
    return ident, econs


# ------------------------------------------------------------------ U25 screen machinery
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
        s = RNG.choice(len(idx), len(idx), replace=True)
        take = idx[s]
        r, _n = wcorr(pd.Series(x.loc[take].values), pd.Series(y.loc[take].values),
                      pd.Series(w.loc[take].values))
        if pd.notna(r):
            out.append(r)
    out = np.array(out)
    lo, hi = np.percentile(out, [2.5, 97.5])
    p = 2 * min((out <= 0).mean(), (out >= 0).mean())
    return float(lo), float(hi), float(p)


def screen(items, anchor_s, pop, label, do_boot):
    print("\n" + "=" * 96)
    print("U25 — four-way orientation screen vs `%s`" % label)
    print("=" * 96)
    print("%-26s %7s %7s %16s %6s %8s %-22s" %
          ("item", "r_w", "r_u", "class", "n", "neff", "G6 / largest LOO"))
    rows = []
    for name, ser in items.items():
        common = ser.dropna().index.intersection(anchor_s.dropna().index).intersection(pop.index)
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
        ci = boot_ci(x, y, w) if (do_boot and cls in ("counter-moving", "aligned",
                                                     "restatement")) else None
        rows.append({"item": name, "r_w": rw, "r_u": ru, "cls": cls, "n": n, "neff": neff,
                     "r_drop": r_drop, "loo_econ": big, "loo_d": loo[big], "ci": ci,
                     "x": x, "y": y, "w": w})
        print("%-26s %+7.3f %+7.3f %16s %6d %8.1f  drop5 %+.3f / %s %+.3f"
              % (name, rw, ru, cls, n, neff, r_drop, big[:14], loo[big]))
        if ci:
            print("%-26s   bootstrap 2,000 economy draws: [%+.3f, %+.3f]  p_boot=%.3f"
                  % ("", ci[0], ci[1], ci[2]))
    return rows


def main():
    mi = Micro()
    c = country_2024()
    ident, econs = mapping_pass(mi, c)

    df = mi.df
    # per-economy weighted share of each identified code, over that column's own denominator
    def share(mcol, code, denom):
        s = df[denom].dropna(subset=["wgt"])
        h = df[mcol].eq(code).reindex(s.index).fillna(False).astype(float)
        g = s.assign(_h=h * s["wgt"]).groupby("economy")[["_h", "wgt"]].sum()
        ser = (g["_h"] / g["wgt"] * 100)
        ser.index = [NAME_FIX.get(e, e) for e in ser.index]
        return ser

    items, items_cond = {}, {}
    for (mcol, code), (ccol, med, mx, n, dlabel) in sorted(ident.items()):
        key = "%s=%d [%s]" % (mcol, code, ccol)
        items[key] = share(mcol, code, df["economy"].isin(econs))
        items_cond[key] = share(mcol, code, df[mcol].notna())
    print("\nscreenable items: %d (each in TWO denominators: population and own-block)" % len(items))

    pop = c["pop_adult"].dropna()
    for anchor, do_boot in (("g20_any", True), ("mobileaccount_t_d", False)):
        a = (c[anchor] * 100).dropna()
        rows = screen(items, a, pop, anchor + "  [POPULATION denominator]", do_boot)
        if anchor == "g20_any":
            cm = [r for r in rows if r["cls"] == "counter-moving"]
            print("\nREGISTERED KEEP CONDITION (>=1 counter-moving on BOTH lenses, G6 sign-stable,"
                  " bootstrap excluding zero):")
            if not cm:
                print("  0 counter-moving items -> DISCARD as registered.")
            for r in cm:
                sign_ok = np.sign(r["r_drop"]) == np.sign(r["r_w"])
                ci_ok = r["ci"] and (r["ci"][0] < 0 and r["ci"][1] < 0)
                print("  %-26s G6 sign %s | CI excludes 0 %s -> %s"
                      % (r["item"], "OK" if sign_ok else "FAIL", "OK" if ci_ok else "FAIL",
                         "KEEP" if (sign_ok and ci_ok) else "FAIL"))
            tab = pd.Series([r["cls"] for r in rows]).value_counts()
            print("\nclassification counts vs g20_any: %s" % dict(tab))
            # G4 coverage of the module frame
            share = pop.reindex([e for e in items[list(items)[0]].index
                                 if e in pop.index]).sum() / pop.sum()
            print("G4 (declared frame = the module's own economy set): %d economies, "
                  "%.1f%% of country-file 2024 adult population" % (len(econs), 100 * share))
            inc = c.reindex([e for e in items[list(items)[0]].index if e in c.index])
            print("income mix of the module set: %s" % dict(inc["incomegroupwb24"].value_counts()))

            # ---- REGISTERED CONDITIONAL READING (pre-registration, U25x denominator clause):
            # "if the module is a within-economy conditional subsample, every statistic is a
            # conditional one and the claim text must say so." Same screen, own-block denominator.
            rows_c = screen(items_cond, a, pop, "g20_any  [OWN-BLOCK conditional denominator]",
                            True)
            cmap = {r["item"]: r for r in rows_c}
            print("\nBOTH-DENOMINATOR COMPARISON on the population-denominator counter-movers:")
            for r in rows:
                if r["cls"] == "counter-moving":
                    q = cmap.get(r["item"])
                    print("  %-26s pop: r_w %+.3f r_u %+.3f (%s)  |  conditional: r_w %+.3f "
                          "r_u %+.3f (%s)" % (r["item"], r["r_w"], r["r_u"], r["cls"],
                                              q["r_w"], q["r_u"], q["cls"]))
            print("\nCOMPLEMENT-DENOMINATOR DECOMPOSITION (is the counter-movement the item or "
                  "the 1 - mobile-money-rate factor?):")
            mm = (c["mobileaccount_t_d"] * 100).dropna()
            common = mm.index.intersection(a.index).intersection(pop.index).intersection(
                items[list(items)[0]].dropna().index)
            comp = 100 - mm.loc[common]
            rw, _ = wcorr(comp, a.loc[common], pop.loc[common])
            ru, _ = wcorr(comp, a.loc[common], pd.Series(1.0, index=common))
            print("  r(100 - mobileaccount_t_d, g20_any) over the %d module economies: "
                  "weighted %+.3f, unweighted %+.3f -> class %s"
                  % (len(common), rw, ru, classify(rw, ru)))

            # ---- DISCLOSED FAMILY-WISE CORRECTION (rule B7), decided BEFORE it was computed:
            # the registered bars decide the verdict; an item that meets them but fails BH at
            # q = 0.10 over its own 19-test family is RETIRED, not kept.
            print("\nBH FAMILY-WISE CORRECTION over the %d conditional-denominator tests vs "
                  "g20_any (q = 0.10):" % len(items_cond))
            ps = []
            for name, ser in items_cond.items():
                k = ser.dropna().index.intersection(a.dropna().index).intersection(pop.index)
                lo, hi, pb = boot_ci(ser.loc[k], a.loc[k], pop.loc[k])
                ps.append((pb, name))
            ps.sort()
            m = len(ps)
            for i, (pb, name) in enumerate(ps, 1):
                crit = 0.10 * i / m
                print("  %-26s p_boot=%.4f  BH crit=%.4f  %s"
                      % (name, pb, crit, "reject" if pb <= crit else ""))
            kmax = max([i for i, (pb, _n) in enumerate(ps, 1) if pb <= 0.10 * i / m] or [0])
            passing = {n for _i, (pb, n) in enumerate(ps[:kmax], 1)}
            print("  BH rejects %d of %d; fin14d in the rejected set: %s"
                  % (kmax, m, "YES" if any("fin14d" in n for n in passing) else "NO"))


if __name__ == "__main__":
    main()
