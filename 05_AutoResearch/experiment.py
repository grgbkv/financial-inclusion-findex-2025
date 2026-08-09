"""E36 (pre-registered): is "access converges, use diverges" a RESOURCE/ASCRIPTION line?

Program 3, item 3.7. Parent: E34 (whose parent is E31) — the THIRD consecutive descendant of
E31's gap-trajectory design, so rule B3's cap is reached with this experiment.

B2 BREADTH CELLS: `group == "laborforce"` (thin, 1 mention) and `group == "gender"` (ZERO ledger
mentions, five waves) — the two untested axes of the 13-year inequality panel.

WHY. E31: the income and education USAGE gaps (`g20_any`) widened in log-odds while their ACCESS
gaps narrowed. E34: the age gap narrowed on BOTH margins. The sharp hypothesis is that the split is
set by what defines the disadvantaged group — RESOURCE axes (income, education, employment) diverge
on usage, ASCRIBED axes (age cohort, sex) do not. `laborforce` and `gender` fall on opposite sides
of that line, so this is an out-of-sample test of the split, not a fourth description.

DESIGN, per the pre-registration:
  gap        = logit(p_advantaged) - logit(p_disadvantaged), p clipped to [0.005, 0.995]
  ACCESS     `account_t_d`, 2011->2024      USAGE  `g20_any`, 2014->2024
  PRIMARY    unweighted SHARE of developing panel economies whose gap is SMALLER at span end
  SECONDARY  pop-weighted mean change, its unweighted twin, drop-top-5 (G6)
  Income, education and age are recomputed INSIDE this file (the E35 convention) so the two new
  axes are read beside their originals.

REGISTERED KEEP RULE (joint claim). Keep only if BOTH:
  P1 laborforce = resource-like: access share >= 60% AND usage share  < 50%
  P2 gender     = ascribed-like: access share >= 60% AND usage share >= 60%
Anything else discards the joint claim; the per-axis pattern is logged either way.

Gates: G3 (headline columns), G4 per margin, G6 on every weighted mean, G5 n/a.
B6: 2,000-draw country bootstrap on share and weighted mean; Kish neff in every cell.
B7: BH at q=0.10 over the declared family of TEN cells (5 axes x 2 margins) on the share's
bootstrap p against 0.5.

DECLARED. Descriptive gap trajectories over 13 years. Group composition changes across waves
(schooling expands, populations age, labour-force participation moves), so a narrowing gap is not
evidence that any individual's position changed. No causal reading.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 36
SHARE_BAR = 0.60
DIVERGE_BAR = 0.50
CLIP = (0.005, 0.995)
Q = 0.10
WAVES = [2011, 2014, 2017, 2021, 2024]

# axis -> (advantaged group2 label, disadvantaged group2 label, declared kind)
AXES = {
    "income":     ("richest 60%", "poorest 40%", "resource"),
    "education":  ("secondary edu or more", "prim edu or less", "resource"),
    "laborforce": ("in laborforce", "out of laborforce", "resource (NEW)"),
    "age_cat":    ("age 25+", "ages 15-24", "ascribed"),
    "gender":     ("men", "women", "ascribed (NEW)"),
}

MARGINS = [("account_t_d", "ACCESS", "account", 2011, 2024),
           ("g20_any", "USAGE", "digital_payment", 2014, 2024)]


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _logit(p):
    return np.log(np.clip(p, *CLIP) / (1 - np.clip(p, *CLIP)))


def _wmean(v, w):
    m = pd.notna(v) & pd.notna(w)
    return float(np.average(v[m], weights=w[m])) if m.any() else np.nan


def gap_table(fx: Findex, axis, col):
    """Per-country, per-wave log-odds gap on `col` for one axis, developing panel economies."""
    adv_lab, dis_lab, _ = AXES[axis]
    g = fx.pan_grp[(fx.pan_grp["group"] == axis)
                   & (fx.pan_grp["incomegroupwb24"] != "High income")]
    adv = g[g["group2"] == adv_lab].pivot_table(index="countrynewwb", columns="year", values=col)
    dis = g[g["group2"] == dis_lab].pivot_table(index="countrynewwb", columns="year", values=col)
    if adv.empty or dis.empty:
        raise ValueError(f"axis {axis}: labels {adv_lab!r}/{dis_lab!r} not found")
    waves = [y for y in WAVES if y in adv.columns and y in dis.columns]
    lo = pd.DataFrame({y: _logit(adv[y]) - _logit(dis[y]) for y in waves})
    pp = pd.DataFrame({y: (adv[y] - dis[y]) * 100 for y in waves})
    pop = fx.pan_dev[fx.pan_dev["year"] == 2024].set_index("countrynewwb")["pop_adult"]
    lo["pop"], pp["pop"] = pop, pop
    return lo, pp


def cell(lo, y0, y1, axis, margin):
    """Share narrowing + weighted/unweighted mean change + bootstrap + G6, one axis x margin."""
    d = pd.DataFrame({"d": lo[y1] - lo[y0], "pop": lo["pop"]}).dropna()
    n = len(d)
    share = float((d["d"] < 0).mean())
    wm, um = _wmean(d["d"], d["pop"]), float(d["d"].mean())
    neff = _kish(d["pop"])

    rng = np.random.default_rng(SEED)
    idx = np.arange(n)
    bs, bw = [], []
    for _ in range(BOOT):
        s = d.iloc[rng.choice(idx, size=n, replace=True)]
        bs.append(float((s["d"] < 0).mean()))
        bw.append(_wmean(s["d"], s["pop"]))
    bs, bw = np.asarray(bs), np.asarray(bw)
    # two-sided bootstrap p for the share against the coin flip
    tail = min((bs <= 0.5).mean(), (bs >= 0.5).mean())
    p_share = float(max(2.0 * tail, 1.0 / BOOT))

    keep = d["pop"].sort_values(ascending=False).index[5:]
    wm_drop = _wmean(d.loc[keep, "d"], d.loc[keep, "pop"])
    share_drop = float((d.loc[keep, "d"] < 0).mean())

    return {"axis": axis, "margin": margin, "span": f"{y0}->{y1}", "n": n, "neff": neff,
            "share": share, "share_lo": float(np.percentile(bs, 2.5)),
            "share_hi": float(np.percentile(bs, 97.5)), "p_share": p_share,
            "wmean": wm, "wmean_lo": float(np.percentile(bw, 2.5)),
            "wmean_hi": float(np.percentile(bw, 97.5)), "unwtd": um,
            "wmean_droptop5": wm_drop, "share_droptop5": share_drop}


def benjamini_hochberg(pvals, q=Q):
    p = np.asarray(pvals, dtype=float)
    ok = ~np.isnan(p)
    m = int(ok.sum())
    out = np.zeros(len(p), dtype=bool)
    if m == 0:
        return out
    order = np.argsort(np.where(ok, p, np.inf))[:m]
    thresh = q * np.arange(1, m + 1) / m
    passed = p[order] <= thresh
    if passed.any():
        out[order[:int(np.max(np.where(passed)[0])) + 1]] = True
    return out


def run(fx: Findex):
    print("E36 — resource vs ascribed axes on two margins (dev panel, pan_grp)\n")
    rows, levels = [], []
    for col, margin, concept, y0, y1 in MARGINS:
        print(f"=== {margin} margin: {col}, {y0}->{y1} ===")
        print("  G3:", fx.gate_variant(concept, col), "| G4:", fx.gate_coverage(fx.pan_dev, col, y1))
        for axis in AXES:
            lo, pp = gap_table(fx, axis, col)
            if y0 not in lo.columns or y1 not in lo.columns:
                print(f"  {axis}: span unavailable ({list(lo.columns)})")
                continue
            r = cell(lo, y0, y1, axis, margin)
            rows.append(r)
            print(f"  {axis:11s} [{AXES[axis][2]:14s}] n={r['n']:3d} neff={r['neff']:4.1f} | "
                  f"share narrowing {r['share']:5.1%} [{r['share_lo']:.1%},{r['share_hi']:.1%}] "
                  f"p={r['p_share']:.4f} | wmean {r['wmean']:+.3f} "
                  f"[{r['wmean_lo']:+.3f},{r['wmean_hi']:+.3f}] | unwtd {r['unwtd']:+.3f} | "
                  f"G6 droptop5 wmean {r['wmean_droptop5']:+.3f} share {r['share_droptop5']:.1%}")
            for y in [c for c in pp.columns if c != "pop"]:
                dd = pd.DataFrame({"v": pp[y], "pop": pp["pop"]}).dropna()
                levels.append({"axis": axis, "margin": margin, "year": y,
                               "pp_gap": _wmean(dd["v"], dd["pop"]), "n": len(dd)})
        print()

    res = pd.DataFrame(rows)
    res["bh"] = benjamini_hochberg(res["p_share"].values)

    print("=" * 104)
    print("PP-GAP LEVELS (pop-weighted, advantaged minus disadvantaged)\n")
    lv = pd.DataFrame(levels).pivot_table(index=["margin", "axis"], columns="year",
                                          values="pp_gap")
    print(lv.round(1).to_string())

    print("\n" + "=" * 104)
    print("TEN-CELL FAMILY (BH at q=0.10 on the share's bootstrap p)\n")
    print(f"  {'axis':11s} {'margin':7s} {'n':>4s} {'neff':>5s} {'share':>7s} {'95% CI':>17s} "
          f"{'p':>7s} {'BH':>5s} {'wmean':>7s} {'unwtd':>7s} {'drop5':>7s}")
    for _, r in res.iterrows():
        print(f"  {r['axis']:11s} {r['margin']:7s} {int(r['n']):4d} {r['neff']:5.1f} "
              f"{r['share']:7.1%} [{r['share_lo']:5.1%},{r['share_hi']:5.1%}] {r['p_share']:7.4f} "
              f"{str(bool(r['bh'])):>5s} {r['wmean']:+7.3f} {r['unwtd']:+7.3f} "
              f"{r['wmean_droptop5']:+7.3f}")
    print(f"\n  BH rejects {int(res['bh'].sum())}/{len(res)} cells at q={Q:.2f}; "
          f"uncorrected p<=0.10: {int((res['p_share'] <= Q).sum())}/{len(res)}")

    print("\n" + "=" * 104)
    print("ACCESS-MINUS-USAGE ASYMMETRY (the statistic the hypothesis is about)\n")
    for axis in AXES:
        a = res[(res["axis"] == axis) & (res["margin"] == "ACCESS")]
        u = res[(res["axis"] == axis) & (res["margin"] == "USAGE")]
        if a.empty or u.empty:
            continue
        a, u = a.iloc[0], u.iloc[0]
        print(f"  {axis:11s} [{AXES[axis][2]:14s}] access {a['share']:5.1%} - usage "
              f"{u['share']:5.1%} = {(a['share'] - u['share']) * 100:+5.1f}pp   "
              f"(wmean access {a['wmean']:+.3f}, usage {u['wmean']:+.3f})")

    print("\n=== VERDICT (pre-registered joint claim) ===")
    def get(axis, margin):
        return res[(res["axis"] == axis) & (res["margin"] == margin)].iloc[0]
    la, lu = get("laborforce", "ACCESS"), get("laborforce", "USAGE")
    ga, gu = get("gender", "ACCESS"), get("gender", "USAGE")
    p1 = bool(la["share"] >= SHARE_BAR and lu["share"] < DIVERGE_BAR)
    p2 = bool(ga["share"] >= SHARE_BAR and gu["share"] >= SHARE_BAR)
    print(f"  P1 laborforce resource-like: access {la['share']:.1%} >= {SHARE_BAR:.0%} "
          f"({la['share'] >= SHARE_BAR}) AND usage {lu['share']:.1%} < {DIVERGE_BAR:.0%} "
          f"({lu['share'] < DIVERGE_BAR}) -> {'PASS' if p1 else 'FAIL'}")
    print(f"  P2 gender ascribed-like:     access {ga['share']:.1%} >= {SHARE_BAR:.0%} "
          f"({ga['share'] >= SHARE_BAR}) AND usage {gu['share']:.1%} >= {SHARE_BAR:.0%} "
          f"({gu['share'] >= SHARE_BAR}) -> {'PASS' if p2 else 'FAIL'}")
    print(f"  JOINT KEEP = {'YES' if (p1 and p2) else 'NO'}")
    return res


if __name__ == "__main__":
    run(Findex())
