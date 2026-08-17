"""E49 (pre-registered 2026-08-17): the `fin` catch-all — mandatory mapping pass plus the
four-way orientation screen.

B2 BREADTH CELL. `fin` is a 93-column catch-all family with ZERO ledger mentions — the largest
reachable untouched block in the country file, and the one the 2026-08-16 correction found had been
hidden behind five consecutive B2 notes that crowned smaller families instead. No parent: a new
module.

PART A — MAPPING PASS, logged as EXPLORATORY under the peek rule (2026-07-11). For every `fin`
column with >= 3 waves at >= 70 developing economies, print the population-weighted level by wave and
the country count. Item MEANINGS ARE INFERRED from levels and coverage only; there is no
questionnaire in the repo (HARNESS_V2_NOTES.md items 5-6) and that caveat travels with every claim
made here.

PART B — THE FOUR-WAY ORIENTATION SCREEN (Documentation obligation 2, 2026-08-15c), the registered
primary. Each eligible item against the digital-payment headline `g20_any` in the 2024
developing-panel cross-section (E45/E47's anchor, so the results are comparable), BOTH lenses:

    restatement    |r| >= 0.80
    aligned        +0.30 <= r < 0.80
    counter-moving r <= -0.30
    independent    |r| < 0.30
    both lenses must AGREE, else `mixed-lens` (B9/B11)

REGISTERED KEEP CONDITION: at least one item classifies as `counter-moving` on BOTH lenses, survives
G6 with the sign intact, and has a bootstrap interval (2,000 country draws) excluding zero. A screen
returning only restatement/aligned items is a DISCARD — the module would then be a re-description of
the headline, as `dig_acc` was found to be.

REGISTERED SIGN (B15): the keep direction is NEGATIVE. An item at r >= +0.80 is a restatement and is
the OPPOSITE result, not partial confirmation.

SECONDARY (registered, no bar): the same screen against `account_t_d`, for every eligible item. It
distinguishes "counter-moves with digital payment" from "counter-moves with financial access in
general" — the distinction E47 drew on `fin34c`.

B6/B9/B10/B12 on every cell: weighted and unweighted r, bootstrap percentile interval and p_boot,
Kish neff beside nominal n, G6 drop-top-5, and the LARGEST SINGLE LEAVE-ONE-OUT effect with the
economy NAMED.

DECLARED. A 2024 cross-sectional LEVEL correlation is a COMPOSITION statement about economies, not a
within-country dynamic one — E48's primary is the standing proof that the two come apart. No delta
claim is registered here. G3: every `fin` item is an unregistered narrow variant.
"""
import numpy as np
import pandas as pd

from coverage import _module_of          # read-only instrument; module classification only
from harness import Findex

BOOT = 2000
SEED = 49
YEARS = [2011, 2014, 2017, 2021, 2024]
HEAD = "g20_any"
ACCT = "account_t_d"

MIN_WAVES = 3          # registered eligibility
MIN_COUNTRIES = 70     # registered eligibility
RESTATE = 0.80
BAR = 0.30


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def corr(x, y, w=None):
    m = pd.notna(x) & pd.notna(y)
    if w is not None:
        m &= pd.notna(w)
    x, y = x[m], y[m]
    if len(x) < 10:
        return np.nan, int(len(x))
    ww = np.ones(len(x)) if w is None else np.asarray(w[m], dtype=float)
    mx, my = np.average(x, weights=ww), np.average(y, weights=ww)
    sx = np.sqrt(np.average((x - mx) ** 2, weights=ww))
    sy = np.sqrt(np.average((y - my) ** 2, weights=ww))
    if sx == 0 or sy == 0:
        return np.nan, int(len(x))
    return float(np.average((x - mx) * (y - my), weights=ww) / (sx * sy)), int(len(x))


def boot_ci(df, fn, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        v = fn(df.iloc[rng.choice(idx, size=len(idx), replace=True)])
        if pd.notna(v) and np.isfinite(v):
            out.append(v)
    if len(out) < draws // 4:
        return np.nan, np.nan, np.nan
    a = np.asarray(out)
    return (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)),
            float(2 * min((a <= 0).mean(), (a >= 0).mean())))


def classify(rw, ru):
    """The four-way screen. Both lenses must agree, else mixed-lens."""
    def one(r):
        if pd.isna(r):
            return "na"
        if abs(r) >= RESTATE:
            return "restatement"
        if r >= BAR:
            return "aligned"
        if r <= -BAR:
            return "counter-moving"
        return "independent"
    a, b = one(rw), one(ru)
    return a if a == b else f"mixed-lens ({a}/{b})", a, b


def screen_cell(T, col, anchor, fx, full=True):
    sub = T[[col, anchor, "pop"]].dropna()
    if len(sub) < 10:
        return None
    x, y, w = sub[col], sub[anchor], sub["pop"]
    rw, n = corr(x, y, w)
    ru, _ = corr(x, y)
    cls, cw, cu = classify(rw, ru)
    out = {"col": col, "r_w": rw, "r_u": ru, "n": n, "neff": kish(w), "class": cls,
           "cls_w": cw, "cls_u": cu}
    if full:
        d = pd.DataFrame({"x": x, "y": y, "w": w})
        lo, up, pb = boot_ci(d, lambda s: corr(s["x"], s["y"], s["w"])[0])
        g6 = fx.gate_jackknife(x, y, w)
        loo = sorted(((corr(d.drop(i)["x"], d.drop(i)["y"], d.drop(i)["w"])[0] - rw, i)
                      for i in d.index), key=lambda t: -abs(t[0]))[0]
        out.update({"ci": (lo, up), "p_boot": pb, "g6": g6["r_droptop"], "loo": loo})
    return out


def show(rows, title):
    print(f"\n{title}")
    print(f"  {'item':22s}{'r_w':>8s}{'[95% CI]':>20s}{'p_boot':>8s}{'G6':>8s}{'r_u':>8s}"
          f"{'n':>5s}{'neff':>7s}  {'largest LOO':>26s}  class")
    for r in rows:
        ci = f"[{r['ci'][0]:+.3f}, {r['ci'][1]:+.3f}]"
        loo = f"{r['loo'][1]} {r['loo'][0]:+.3f}"
        print(f"  {r['col']:22s}{r['r_w']:>8.3f}{ci:>20s}{r['p_boot']:>8.3f}"
              f"{r['g6']:>8.3f}{r['r_u']:>8.3f}{r['n']:>5d}{r['neff']:>7.1f}  {loo:>26s}  "
              f"{r['class']}")


def main():
    fx = Findex()
    dev = fx.pan_dev
    skip = {"year", "pop_adult", "group", "group2", "countrynewwb", "codewb",
            "regionwb24_hi", "incomegroupwb24"}
    fin_cols = sorted(c for c in fx.raw.columns
                      if c not in skip and _module_of(c) == "fin")

    print("=" * 132)
    print("E49 — the untouched `fin` catch-all: mapping pass (EXPLORATORY) + four-way "
          "orientation screen (REGISTERED)")
    print(f"      {len(fin_cols)} columns in the family, zero prior ledger mentions")
    print("=" * 132)

    # ------------------------------------------------------- PART A: mapping (EXPLORATORY)
    print("\n" + "-" * 132)
    print("PART A — MAPPING PASS (EXPLORATORY, peek rule). Weighted level by wave, developing "
          "panel; countries reporting in brackets.")
    print("Item meanings are INFERRED from levels and coverage. There is no questionnaire in "
          "the repo.")
    print("-" * 132)
    rows = []
    for c in fin_cols:
        lv, nc = {}, {}
        for y in YEARS:
            d = dev[(dev["year"] == y)].dropna(subset=[c, "pop_adult"])
            nc[y] = int(d["countrynewwb"].nunique())
            lv[y] = (float(np.average(d[c], weights=d["pop_adult"])) * 100
                     if len(d) else np.nan)
        good = sum(1 for y in YEARS if nc[y] >= MIN_COUNTRIES)
        rows.append({"col": c, "waves_ok": good, **{f"lv{y}": lv[y] for y in YEARS},
                     **{f"n{y}": nc[y] for y in YEARS}})
    M = pd.DataFrame(rows)
    elig = M[M["waves_ok"] >= MIN_WAVES].sort_values("waves_ok", ascending=False)
    print(f"  {'item':22s}{'waves':>6s}   " +
          "".join(f"{y:>16d}" for y in YEARS))
    for _, r in elig.iterrows():
        cells = "".join(
            ("      --      " if pd.isna(r[f'lv{y}']) or r[f'n{y}'] < MIN_COUNTRIES
             else f"{r[f'lv{y}']:8.1f} [{int(r[f'n{y}']):2d}]").rjust(16) for y in YEARS)
        print(f"  {r['col']:22s}{int(r['waves_ok']):>6d}   {cells}")
    print(f"\n  ELIGIBLE (>= {MIN_WAVES} waves at >= {MIN_COUNTRIES} developing economies): "
          f"{len(elig)} of {len(fin_cols)} columns")
    ineligible = M[M["waves_ok"] < MIN_WAVES]
    print(f"  ineligible (thin or single-wave): {len(ineligible)} columns — "
          f"{', '.join(ineligible['col'].head(20))}{' ...' if len(ineligible) > 20 else ''}")

    # ------------------------------------------------------- PART B: the registered screen
    y24 = dev[dev["year"] == 2024]
    tab = y24.set_index("countrynewwb")
    T = pd.DataFrame({c: tab[c] * 100 for c in list(elig["col"]) + [HEAD, ACCT]})
    T["pop"] = tab["pop_adult"]

    print("\n" + "-" * 132)
    print("PART B — FOUR-WAY ORIENTATION SCREEN (REGISTERED PRIMARY) vs the digital-payment "
          "headline `g20_any`, 2024 levels")
    print(f"  restatement |r|>={RESTATE} · aligned +{BAR}<=r<{RESTATE} · counter-moving "
          f"r<=-{BAR} · independent |r|<{BAR} · both lenses must agree")
    print("-" * 132)
    g4 = fx.gate_coverage(dev, HEAD, 2024)
    print(f"  G4 on the anchor: {g4}")

    cells = []
    for c in elig["col"]:
        r = screen_cell(T, c, HEAD, fx, full=True)
        if r:
            cells.append(r)
    cells.sort(key=lambda r: r["r_w"])
    show(cells, "vs g20_any (2024 developing-panel levels):")

    counts = pd.Series([r["class"].split(" ")[0] for r in cells]).value_counts()
    print("\n  classification counts: " +
          ", ".join(f"{k} {v}" for k, v in counts.items()))

    # registered keep condition
    cm = [r for r in cells if r["class"] == "counter-moving"]
    cm_ok = [r for r in cm
             if pd.notna(r["g6"]) and r["g6"] <= 0 and r["ci"][1] < 0]
    print(f"\n  counter-moving on BOTH lenses: "
          f"{', '.join(r['col'] for r in cm) if cm else 'NONE'}")
    print(f"  ... of which survive G6 with the sign intact AND a CI excluding zero: "
          f"{', '.join(r['col'] for r in cm_ok) if cm_ok else 'NONE'}")
    keep = bool(cm_ok)

    # ------------------------------------------------------- SECONDARY vs account_t_d
    print("\n" + "-" * 132)
    print("SECONDARY (registered, no bar) — the same screen vs `account_t_d`: counter-moving "
          "with DIGITAL PAYMENT or with ACCESS in general?")
    print("-" * 132)
    a_cells = []
    for c in elig["col"]:
        r = screen_cell(T, c, ACCT, fx, full=True)
        if r:
            a_cells.append(r)
    order = {r["col"]: i for i, r in enumerate(cells)}
    a_cells.sort(key=lambda r: order.get(r["col"], 999))
    show(a_cells, "vs account_t_d (2024 developing-panel levels):")
    a_by = {r["col"]: r for r in a_cells}
    print("\n  side by side for every counter-moving item:")
    for r in cm:
        a = a_by.get(r["col"])
        print(f"    {r['col']:22s} vs g20_any {r['r_w']:+.3f}/{r['r_u']:+.3f} ({r['class']})"
              f"   |   vs account_t_d {a['r_w']:+.3f}/{a['r_u']:+.3f} ({a['class']})")

    # ------------------------------------------------------- VERDICT
    print("\n" + "=" * 132)
    print("E49 VERDICT (pre-registered)")
    print(f"  registered keep condition: >= 1 item `counter-moving` on both lenses, through G6, "
          f"CI excluding zero -> {'MET' if keep else 'NOT MET'}")
    print(f"  B15 registered sign: NEGATIVE. Items at r >= +{RESTATE} are restatements and are the "
          f"opposite result, not partial confirmation "
          f"({sum(1 for r in cells if r['class'] == 'restatement')} such items).")
    print(f"  -> E49 {'KEEP' if keep else 'DISCARD'}")
    if not keep:
        print("     Registered null reading: the `fin` catch-all would then contain no margin that")
        print("     runs against the digital-payment headline in the 2024 cross-section, and the")
        print("     two counter-moving margins found so far (fin31d, fin34c) stay the only ones.")
    print("=" * 132)
    print("\nEXPLORATORY MAPPING is written to HARNESS_V2_NOTES.md. Every meaning below is "
          "INFERRED from levels\nand coverage; none is read from a questionnaire (the repo has "
          "none). Part A is logged as exploratory.")


if __name__ == "__main__":
    main()
