"""E39 (pre-registered): is 2021->2024 actually a unique episode, or only a weighted-mean one?

Program 1, item 1.5. Parent: E27 / the paper draft's Section 4 framing. NOT the rails chain.

B2 BREADTH CELL: all four transitions including **2011->2014**, the thinnest in the audit
(6 ledger mentions), and `borrow_any_t_d` (untouched module) as a context margin.

WHY THIS IS OWED. The entire ledger is built on a 2021->2024 "saving surge", and rule B4 exists
precisely because that window may be special. But nobody has checked whether the surge is unique
WITHIN COUNTRIES or only in the population-weighted aggregate. E31 and E36 both showed those two
can point in opposite directions — a weighted mean can move a long way while a minority of
economies moves with it.

DESIGN, per the pre-registration. For each margin and each available transition, the distribution
of per-country change on `pan_dev`: unweighted median, unweighted mean, IQR, the SHARE of economies
with change >= +10pp, and the population-weighted mean for contrast.

  PRIMARY margin  fin17a_17a1_d (formal saving)
  CONTEXT margins account_t_d, g20_any, borrow_any_t_d

PRIMARY PRE-REGISTERED STATISTIC (formal saving). 2021->2024 is declared unique iff BOTH:
  (a) its unweighted share of economies with change >= +10pp is >= 1.5x the largest such share in
      any earlier transition, AND
  (b) its unweighted median change is the largest of the four.

REGISTERED ALTERNATIVE OUTCOME. If 2021->2024 is NOT top on both, the "episode" framing is an
aggregate artifact and Section 4 of the paper draft needs rewording — that outcome is the more
valuable of the two and is logged as a keep in the negative direction.

Gates: G4 · G5 against the official developing aggregate for fin17a_17a1_d where it exists · G6 is
not applicable to an unweighted share and is reported as the weighted-vs-unweighted contrast
instead. No bootstrap: the primary statistic is a share, not an association, and B6 binds on
association keeps (the share's binomial interval is reported as a descriptive courtesy).

DECLARED. Descriptive distributional comparison across waves. Wave spacing is uneven (3/3/4/3
years) and the 2021 wave is a pandemic-period measurement; both are stated, neither is adjusted for.
"""
import numpy as np
import pandas as pd

from harness import Findex

BIG_MOVE = 10.0          # pp
UNIQUE_FACTOR = 1.5
SEED = 39
TRANSITIONS = [(2011, 2014), (2014, 2017), (2017, 2021), (2021, 2024)]

PRIMARY = ("fin17a_17a1_d", "formal saving")
CONTEXT = [("account_t_d", "account ownership"),
           ("g20_any", "digital payments"),
           ("borrow_any_t_d", "any borrowing")]


def deltas(fx: Findex, col, t0, t1):
    w = fx.country_panel(fx.pan_dev, col, [t0, t1])
    if t0 not in w.columns or t1 not in w.columns:
        return pd.DataFrame(columns=["d", "pop"])   # g20_any and borrow_any_t_d start in 2014
    return pd.DataFrame({"d": w[t1] - w[t0], "pop": w["pop"]}).dropna()


def describe(d):
    if len(d) < 30:
        return None
    share = float((d["d"] >= BIG_MOVE).mean())
    se = np.sqrt(share * (1 - share) / len(d))
    return {
        "n": len(d),
        "median": float(d["d"].median()),
        "mean_unw": float(d["d"].mean()),
        "mean_wtd": float(np.average(d["d"], weights=d["pop"])),
        "iqr": float(d["d"].quantile(0.75) - d["d"].quantile(0.25)),
        "share_big": share,
        "share_lo": max(0.0, share - 1.96 * se),
        "share_hi": min(1.0, share + 1.96 * se),
    }


def margin_table(fx: Findex, col):
    rows = []
    for t0, t1 in TRANSITIONS:
        d = deltas(fx, col, t0, t1)
        r = describe(d)
        if r:
            r["span"] = f"{t0}->{t1}"
            rows.append(r)
    return pd.DataFrame(rows).set_index("span") if rows else pd.DataFrame()


def show(name, col, tbl):
    print("-" * 96)
    print(f"{name}  ({col})")
    if tbl.empty:
        print("  no transition reaches 30 economies")
        return
    print(f"  {'span':12s} {'n':>4s} {'median':>8s} {'mean_unw':>9s} {'mean_WTD':>9s} {'IQR':>7s} "
          f"{'share>=+10pp':>13s}  {'95% CI':>16s}")
    for span, r in tbl.iterrows():
        print(f"  {span:12s} {int(r['n']):4d} {r['median']:+8.2f} {r['mean_unw']:+9.2f} "
              f"{r['mean_wtd']:+9.2f} {r['iqr']:7.2f} {r['share_big']*100:12.1f}%  "
              f"[{r['share_lo']*100:5.1f}%,{r['share_hi']*100:5.1f}%]")


def repeat_movers(fx: Findex, col):
    """Descriptive: does a big mover in one window move again in the next? Spearman on consecutive
    per-country deltas."""
    out = []
    for i in range(len(TRANSITIONS) - 1):
        a0, a1 = TRANSITIONS[i]
        b0, b1 = TRANSITIONS[i + 1]
        da, db = deltas(fx, col, a0, a1)["d"], deltas(fx, col, b0, b1)["d"]
        j = pd.concat([da.rename("a"), db.rename("b")], axis=1).dropna()
        if len(j) >= 30:
            out.append((f"{a0}->{a1} vs {b0}->{b1}", len(j),
                        float(j["a"].corr(j["b"], method="spearman"))))
    return out


def run(fx: Findex):
    print("=" * 96)
    print("E39 — IS 2021->2024 A UNIQUE EPISODE? Distribution of per-country change, four windows")
    print("=" * 96)
    print(f"pan_dev | unique iff share(>= +{BIG_MOVE:.0f}pp) >= {UNIQUE_FACTOR}x the best earlier "
          f"window AND the median is the largest of the four\n")

    col, name = PRIMARY
    prim = margin_table(fx, col)
    show(f"PRIMARY — {name}", col, prim)

    last = f"{TRANSITIONS[-1][0]}->{TRANSITIONS[-1][1]}"
    earlier = prim.drop(index=last)
    cond_a = prim.loc[last, "share_big"] >= UNIQUE_FACTOR * earlier["share_big"].max()
    cond_b = prim.loc[last, "median"] >= prim["median"].max() - 1e-12
    print(f"\n  (a) share test: {prim.loc[last,'share_big']*100:.1f}% vs "
          f"{UNIQUE_FACTOR}x{earlier['share_big'].max()*100:.1f}% = "
          f"{UNIQUE_FACTOR*earlier['share_big'].max()*100:.1f}%  -> {bool(cond_a)}")
    print(f"  (b) median test: {prim.loc[last,'median']:+.2f}pp is the largest of the four "
          f"-> {bool(cond_b)}")
    print(f"  UNIQUE-EPISODE CLAIM: {'CONFIRMED' if (cond_a and cond_b) else 'REJECTED'}")

    print("\nCONTEXT MARGINS — which window was each margin's own big one?")
    for c, nm in CONTEXT:
        t = margin_table(fx, c)
        show(nm, c, t)
        if not t.empty:
            print(f"    -> top window by share>=+10pp: {t['share_big'].idxmax()} "
                  f"({t['share_big'].max()*100:.1f}%) | by median: {t['median'].idxmax()} "
                  f"({t['median'].max():+.2f}pp)")

    print("-" * 96)
    print("REPEAT MOVERS (Spearman of consecutive per-country changes; descriptive)")
    for c, nm in [PRIMARY] + CONTEXT:
        for lbl, n, rho in repeat_movers(fx, c):
            print(f"  {nm:20s} {lbl:26s} n={n:3d}  rho={rho:+.3f}")

    print("-" * 96)
    print("GATES")
    for y in (2021, 2024):
        g4 = fx.gate_coverage(fx.pan_dev, col, y)
        print(f"  G4 {col} {y}: ok={g4['ok']} n={g4['n_countries']} pop_share={g4['pop_share']}")
    g5 = fx.gate_official(fx.series(fx.pan_dev, col), "developing", col)
    print(f"  G5 {col} vs official developing aggregate: {g5}")
    print("  G6 n/a for an unweighted share — the weighted-vs-unweighted mean columns above are "
          "the equivalent contrast")
    print("=" * 96)
    return prim


if __name__ == "__main__":
    run(Findex())
