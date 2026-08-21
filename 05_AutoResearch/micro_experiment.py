"""U24x (exploratory) + U24 (registered 2026-08-21) — the untouched micro EMERGENCY-FUND module.

U24x, MAPPING PASS (exploratory under the peek rule). The 11 columns carry NUMERIC codes, not text
labels, so the module was identified mechanically: for every column x every code, the per-economy
weighted share was matched against every labelled country-file `fin24*`/`fin25*` column. Result
(median |dev| = 0.000pp, max 0.000pp over 98 economies unless noted):

  fin24  = MAIN SOURCE of emergency funds. 1 savings (=fin24sav), 2 family/friends (=fin24fam),
           3 money from working (=fin24work), 4 borrowing (=fin24bor), 5 selling assets
           (=fin24sell), 6 other (=fin24other), 7 not possible (~fin24aN, med dev 2.40), 8/9 DK/RF.
  fin24a = DIFFICULTY, asked only of codes 1-6. 1 very difficult (=fin24aVD), 2 somewhat difficult
           (=fin24aSD), 3 not difficult (=fin24aND), 4/5 DK/RF.
  fin24b codes 1/2/3/4 = fin24ba/bb/bc/bd exactly;  fin24c code 1 = fin24c exactly.
  Module coverage: 98 economies, 102,954 respondents (71.5% of the file). This is an ECONOMY-level
  subsample, not a within-economy split sample, so `wgt` is the correct weight inside the 98.

  M3, EXACT: `fin24a in {2,3}` over the `fin24` denominator reproduces the country file's
  `fin24aSD_ND` -- the harness's declared `resilience` headline -- with max |dev| = 0.000pp on all
  98 economies. That is the outcome U24 uses, so G3 is the declared headline variant.

U24, REGISTERED. Does the access-absorption ruler (account holding absorbs ~64% of the education
gradient in digital-payment use) transfer to a WELFARE margin? Registered sign: POSITIVE gradient.
Keep bar: (1) unconditional gap >= +5pp, (2) absorption < 40%, (3) conditional gap >= +5pp.
Registered split: educ >= 2 (secondary or more) vs educ == 1 (primary or less).
Declared secondary for comparability with U10/U19: educ == 3 vs educ == 1, the ledger's usual split.
Declared benchmark: the identical statistic on `anydigpayment` computed on the SAME 98-economy
sample, so the contrast is not against a figure from a different frame.
"""
import itertools

import numpy as np
import pandas as pd

from micro import Micro, COUNTRY_CSV

SRC = {1: "savings", 2: "family/friends", 3: "money from working", 4: "borrowing",
       5: "selling assets", 6: "other", 7: "not possible", 8: "DK", 9: "RF"}
COLS = ["fin24", "fin24a", "fin24b", "fin24c", "fin24d1", "fin24d2", "fin24d3",
        "fin25e1", "fin25e2", "fin25e3", "fin25e4"]


# --------------------------------------------------------------------------- U24x mapping
def mapping_pass(mi):
    df, out = mi.df, []
    c = pd.read_csv(COUNTRY_CSV, low_memory=False)
    c = c[(c["year"] == 2024) & (c["group"] == "all")].set_index("countrynewwb")
    nm = {"Czech Republic": "Czechia", "Slovak Republic": "Slovakia"}
    cc = [x for x in c.columns if (x.startswith("fin24") or x.startswith("fin25"))
          and not x.endswith("_s")]

    def econ_share(mask, denom):
        s = df[denom].dropna(subset=["wgt"])
        h = mask.reindex(s.index).fillna(False).astype(float)
        g = s.assign(_h=h * s["wgt"]).groupby("economy")[["_h", "wgt"]].sum()
        return g["_h"] / g["wgt"] * 100

    def dev_vs(mask, denom, ccol):
        r, t = econ_share(mask, denom), c[ccol] * 100
        idx = [e for e in r.index if nm.get(e, e) in t.index and pd.notna(t.get(nm.get(e, e)))]
        d = np.abs(np.array([r[e] - t[nm.get(e, e)] for e in idx]))
        return float(np.median(d)), float(d.max()), len(idx)

    print("=" * 92)
    print("U24x — EXPLORATORY mapping pass, micro emergency-fund module (11 untouched columns)")
    print("=" * 92)
    print("%-10s %10s %10s %8s %11s" % ("col", "n_nonmiss", "share_file", "n_econ", "n_econ>=100"))
    for col in COLS:
        n = int(df[col].notna().sum())
        ne = int(df.loc[df[col].notna(), "economy"].nunique())
        n100 = int(df[df[col].notna()].groupby("economy").size().ge(100).sum())
        print("%-10s %10d %9.1f%% %8d %11d" % (col, n, 100 * n / len(df), ne, n100))

    base = df["fin24"].notna()
    print("\nbest single-code match per code of `fin24` and `fin24a` (all country fin24*/fin25*):")
    for mcol in ["fin24", "fin24a"]:
        for code in sorted(df[mcol].dropna().unique()):
            best = []
            for ccol in cc:
                try:
                    med, mx, n = dev_vs(df[mcol].eq(code), base, ccol)
                except Exception:
                    continue
                if n >= 20:
                    best.append((med, mx, ccol, n))
            best.sort()
            if best:
                print("  %-7s code %-4.0f -> %-16s med|dev|=%6.3f max=%6.2f (n=%d)"
                      % (mcol, code, best[0][2], best[0][0], best[0][1], best[0][3]))
    med, mx, n = dev_vs(df["fin24a"].isin([2, 3]), base, "fin24aSD_ND")
    print("\nM3 on the OUTCOME U24 uses: fin24a in {2,3} over the fin24 denominator vs "
          "country `fin24aSD_ND`: med|dev|=%.4f max=%.4f on %d economies" % (med, mx, n))
    out.append(("M3", med, mx, n))
    print("\nweighted composition of `fin24` (main source of emergency funds), pooled over the 98:")
    s = df[base].dropna(subset=["wgt"])
    sh = s.groupby("fin24")["wgt"].sum() / s["wgt"].sum() * 100
    for k, v in sh.items():
        print("   %-1.0f %-20s %6.2f%%" % (k, SRC.get(int(k), "?"), v))
    return out


# --------------------------------------------------------------------------- U24 machinery
def wrate(d, col):
    s = d.dropna(subset=[col, "wgt"])
    if s.empty:
        return np.nan, 0
    return float(np.average(s[col], weights=s["wgt"])) * 100, int(len(s))


def gap(d, col, hi_mask, lo_mask):
    """rate(advantaged) - rate(disadvantaged), in pp, with both unweighted cell n."""
    rh, nh = wrate(d[hi_mask.reindex(d.index).fillna(False)], col)
    rl, nl = wrate(d[lo_mask.reindex(d.index).fillna(False)], col)
    return rh - rl, rh, rl, nh, nl


def block(d, col, hi, lo, label):
    g_all = gap(d, col, hi, lo)
    acc = d[d["account"] == 1]
    g_acc = gap(acc, col, hi, lo)
    absorb = np.nan if abs(g_all[0]) < 1e-9 else 1 - g_acc[0] / g_all[0]
    print("  %-34s uncond %+6.2fpp (%5.1f vs %5.1f, n %6d/%6d) | "
          "acct-cond %+6.2fpp (%5.1f vs %5.1f, n %6d/%6d) | absorption %6.1f%%"
          % (label, g_all[0], g_all[1], g_all[2], g_all[3], g_all[4],
             g_acc[0], g_acc[1], g_acc[2], g_acc[3], g_acc[4], 100 * absorb))
    return {"uncond": g_all[0], "cond": g_acc[0], "absorb": absorb,
            "n_hi": g_all[3], "n_lo": g_all[4], "n_hi_c": g_acc[3], "n_lo_c": g_acc[4]}


def kish(w):
    w = np.asarray(w, float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def boot(d, col, hi, lo, draws=2000, seed=20260821):
    rng = np.random.default_rng(seed)
    econs = d["economy"].unique()
    by = {e: d[d["economy"] == e] for e in econs}
    U, C, A = [], [], []
    for _ in range(draws):
        pick = rng.choice(econs, size=len(econs), replace=True)
        s = pd.concat([by[e] for e in pick])
        gu = gap(s, col, hi, lo)[0]
        gc = gap(s[s["account"] == 1], col, hi, lo)[0]
        U.append(gu); C.append(gc)
        A.append(np.nan if abs(gu) < 1e-9 else 1 - gc / gu)
    q = lambda v: (float(np.nanpercentile(v, 2.5)), float(np.nanpercentile(v, 97.5)))
    return q(U), q(C), q(A)


def within_economy(d, col, hi, lo, min_n=100):
    rows = []
    for e, sub in d[d["account"] == 1].groupby("economy"):
        h = sub[hi.reindex(sub.index).fillna(False)]
        l = sub[lo.reindex(sub.index).fillna(False)]
        nh = int(h[col].notna().sum()); nl = int(l[col].notna().sum())
        if nh < min_n or nl < min_n:
            continue
        rh, _ = wrate(h, col); rl, _ = wrate(l, col)
        rows.append({"economy": e, "gap": rh - rl, "n_hi": nh, "n_lo": nl,
                     "participants": nh + nl})
    return pd.DataFrame(rows)


def main():
    mi = Micro()
    mapping_pass(mi)

    df = mi.df.copy()
    base = df["fin24"].notna()
    df["resilient"] = np.where(base, df["fin24a"].isin([2, 3]).astype(float), np.nan)
    d = df[base & df["educ"].notna() & df["account"].notna()].copy()

    hi_reg = d["educ"] >= 2            # registered: secondary or more
    lo_reg = d["educ"] == 1            # registered: primary or less
    hi_led = d["educ"] == 3            # ledger-standard comparability twin
    lo_led = d["educ"] == 1

    print("\n" + "=" * 92)
    print("U24 — the access-absorption ruler on a WELFARE margin (fin24aSD_ND equivalent)")
    print("sample: %d respondents, %d economies (the 98-economy module set)"
          % (len(d), d["economy"].nunique()))
    print("Kish neff of the weights: %.1f (nominal n %d)" % (kish(d["wgt"]), len(d)))
    print("=" * 92)

    print("\nPRIMARY — registered split (educ>=2 vs educ==1):")
    P = block(d, "resilient", hi_reg, lo_reg, "resilience (fin24aSD_ND)")
    print("\nDECLARED BENCHMARK — same statistic, same 98-economy sample, usage margin:")
    B = block(d, "anydigpayment", hi_reg, lo_reg, "digital payment (anydigpayment)")
    print("\nDECLARED SECONDARY — ledger-standard split (educ==3 vs educ==1):")
    P3 = block(d, "resilient", hi_led, lo_led, "resilience (fin24aSD_ND)")
    B3 = block(d, "anydigpayment", hi_led, lo_led, "digital payment (anydigpayment)")

    print("\nB6 country-clustered bootstrap, 2,000 draws, percentile intervals (registered split):")
    cu, cc_, ca = boot(d, "resilient", hi_reg, lo_reg)
    print("  resilience  uncond [%+.2f, %+.2f]  cond [%+.2f, %+.2f]  absorption [%.1f%%, %.1f%%]"
          % (cu[0], cu[1], cc_[0], cc_[1], 100 * ca[0], 100 * ca[1]))
    bu, bc, ba = boot(d, "anydigpayment", hi_reg, lo_reg)
    print("  digital pay uncond [%+.2f, %+.2f]  cond [%+.2f, %+.2f]  absorption [%.1f%%, %.1f%%]"
          % (bu[0], bu[1], bc[0], bc[1], 100 * ba[0], 100 * ba[1]))

    print("\nREGISTERED SECONDARY — within-economy sign of the account-conditional gap "
          "(M2 >=100 in both cells):")
    for tag, h, l in [("registered split", hi_reg, lo_reg), ("ledger split", hi_led, lo_led)]:
        w = within_economy(d, "resilient", h, l)
        wd = within_economy(d, "anydigpayment", h, l)
        if len(w):
            pos = float((w["gap"] > 0).mean())
            share = w["participants"].sum() / len(d[d["account"] == 1])
            print("  %-17s resilience: %d economies qualify (%.1f%% of acct respondents), "
                  "median gap %+.2fpp, positive in %d/%d (%.1f%%)"
                  % (tag, len(w), 100 * share, w["gap"].median(),
                     int((w["gap"] > 0).sum()), len(w), 100 * pos))
        if len(wd):
            print("  %-17s digitalpay: %d economies qualify, median gap %+.2fpp, "
                  "positive in %d/%d (%.1f%%)"
                  % (tag, len(wd), wd["gap"].median(), int((wd["gap"] > 0).sum()), len(wd)))

    print("\nVERDICT AGAINST THE REGISTERED BAR (educ>=2 vs educ==1):")
    b1 = P["uncond"] >= 5.0
    b2 = P["absorb"] < 0.40
    b3 = P["cond"] >= 5.0
    print("  (1) uncond gap >= +5pp and POSITIVE: %+.2f  -> %s" % (P["uncond"], "PASS" if b1 else "FAIL"))
    print("  (2) absorption < 40%%:                %.1f%%  -> %s" % (100 * P["absorb"], "PASS" if b2 else "FAIL"))
    print("  (3) cond gap  >= +5pp and POSITIVE:  %+.2f  -> %s" % (P["cond"], "PASS" if b3 else "FAIL"))
    print("  ==> %s" % ("KEEP" if (b1 and b2 and b3) else "DISCARD"))
    print("\n  benchmark on the same sample: usage-margin absorption %.1f%% vs "
          "welfare-margin absorption %.1f%%" % (100 * B["absorb"], 100 * P["absorb"]))
    print("  ledger-split twin: welfare %.1f%% vs usage %.1f%% absorption"
          % (100 * P3["absorb"], 100 * B3["absorb"]))


if __name__ == "__main__":
    main()
