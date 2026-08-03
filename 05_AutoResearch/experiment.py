"""E31 (pre-registered): over 13 years, do ACCESS gaps close while USAGE gaps stay open?

Program 3 — the 13-year inequality panel, and this cycle's B2 breadth experiment. `pan_grp` is the
largest untouched FRAME in the repo: six demographic slices x five waves x 117 economies, and
`education`, `age_cat` and `laborforce` have ZERO ledger mentions. The paper's "access converges,
use diverges" motif was tested once (E17, on country levels) and discarded; it has never been tested
where it is most natural — WITHIN countries, across demographic groups, over the whole panel.
Parents: E17 / E20 / E21 (the gap-and-convergence family, last touched at E21).

CONSTRUCTION. Developing panel economies only. Five dimensions with multi-wave coverage;
`urbanicity` is 2024-only and is EXCLUDED from the primary, reported as a single-wave line.
Advantaged group declared a priori (pre-registered before any answer):
    gender -> men | income -> richest 60% | education -> secondary edu or more
    age_cat -> age 25+ | laborforce -> in laborforce
Per country per wave: gap = advantaged - disadvantaged (pp). Aggregate = population-weighted mean
gap across economies, weight = 2024 adult population (ledger convention).
    ACCESS margin = account_t_d, window 2011 -> 2024
    USAGE  margin = g20_any,     window 2014 -> 2024  (column absent in 2011; declared)

PRIMARY TEST AND THRESHOLD.
  Claim A (access gaps closed):     >= 3 of 5 dimensions with d_gap_access <= -5pp
  Claim B (usage gaps did not):     >= 3 of 5 dimensions with d_gap_usage  >  -5pp
  JOINT claim kept iff A and B both hold AND >= 3 of 5 dimensions show the divergent pattern
  INDIVIDUALLY (d_gap_access <= -5pp and d_gap_usage > -5pp in the same dimension).

SCALE-FREE REQUIREMENT (mandatory — the agenda's ceiling-artifact note). The pp gap must compress
mechanically as the advantaged group approaches 100%, so the log-odds gap
L = logit(adv) - logit(disadv) is computed for every cell and its delta reported beside the pp
delta. A dimension may only COUNT toward the joint claim if dL and d_gap AGREE IN SIGN; where they
disagree the pp narrowing is declared a ceiling artifact and the dimension counts as a non-closer.

GATES. G3 (account_t_d, g20_any headlines declared), G4 per wave and dimension, G6 (drop top-5
population, sign stability of each d_gap). B6: country bootstrap 2,000 draws, percentile 95%
interval on every d_gap, Kish neff per dimension.

DECLARED. Descriptive within-country gap arithmetic across waves — an ordering of gaps in time,
never a claim about what moved them. The bootstrap is over COUNTRIES only; the within-country
subgroup sampling error is not in this file and is not captured.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 31

ACCESS, USAGE = "account_t_d", "g20_any"
ACCESS_WINDOW, USAGE_WINDOW = (2011, 2024), (2014, 2024)

# dimension -> (advantaged group2 label, disadvantaged group2 label) — declared a priori
DIMENSIONS = {
    "gender": ("men", "women"),
    "income": ("richest 60%", "poorest 40%"),
    "education": ("secondary edu or more", "prim edu or less"),
    "age_cat": ("age 25+", "ages 15-24"),
    "laborforce": ("in laborforce", "out of laborforce"),
}
SINGLE_WAVE = {"urbanicity": ("urban", "rural")}  # 2024 only — descriptive line, not in the primary

PP_BAR = -5.0  # pre-registered group-difference threshold


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _logit(p_pp):
    """logit of a percentage, clipped away from the boundaries (0.5pp) for numerical safety."""
    p = np.clip(np.asarray(p_pp, float) / 100.0, 0.005, 0.995)
    return np.log(p / (1 - p))


def gap_frame(fx: Findex, dim, col, years):
    """Per-country gap (pp) and log-odds gap for `col` in each wave of `years`.
    Returns a country-indexed frame with gap_<y>, L_<y> for each year, plus the 2024 pop weight."""
    adv_lab, dis_lab = (DIMENSIONS | SINGLE_WAVE)[dim]
    g = fx.pan_grp
    g = g[(g["group"] == dim) & (g["incomegroupwb24"] != "High income")]
    out = {}
    for y in years:
        w_ = g[g["year"] == y]
        adv = w_[w_["group2"] == adv_lab].set_index("countrynewwb")[col] * 100
        dis = w_[w_["group2"] == dis_lab].set_index("countrynewwb")[col] * 100
        common = adv.dropna().index.intersection(dis.dropna().index)
        out[f"gap_{y}"] = (adv - dis).reindex(common)
        out[f"L_{y}"] = pd.Series(_logit(adv.reindex(common)) - _logit(dis.reindex(common)),
                                  index=common)
    df = pd.DataFrame(out)
    pop = g[g["year"] == 2024].drop_duplicates("countrynewwb").set_index(
        "countrynewwb")["pop_adult"]
    df["pop"] = pop
    return df.dropna()


def _wmean(v, w):
    return float(np.average(np.asarray(v, float), weights=np.asarray(w, float)))


def _boot_ci(fn, frame, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(frame))
    out = []
    for _ in range(draws):
        v = fn(frame.iloc[rng.choice(idx, size=len(idx), replace=True)])
        if v is not None and pd.notna(v):
            out.append(v)
    if len(out) < draws * 0.9:
        return None, None
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def margin(fx: Findex, name, col, window):
    y0, y1 = window
    print("\n" + "=" * 100)
    print(f"{name} MARGIN — `{col}`, gap = advantaged - disadvantaged, {y0} -> {y1} (dev panel)")
    print("=" * 100)
    res = {}
    for dim in DIMENSIONS:
        df = gap_frame(fx, dim, col, [y0, y1])
        if len(df) < 10:
            print(f"  {dim:12s} insufficient coverage (n={len(df)})")
            continue
        w = df["pop"]
        g0, g1 = _wmean(df[f"gap_{y0}"], w), _wmean(df[f"gap_{y1}"], w)
        l0, l1 = _wmean(df[f"L_{y0}"], w), _wmean(df[f"L_{y1}"], w)
        dgap, dL = g1 - g0, l1 - l0

        lo, hi = _boot_ci(
            lambda s: _wmean(s[f"gap_{y1}"], s["pop"]) - _wmean(s[f"gap_{y0}"], s["pop"]),
            df, seed=SEED + hash(dim) % 1000)
        # G6: drop the five largest-population economies, does d_gap keep its sign?
        keep = w.sort_values(ascending=False).index[5:]
        d_jack = (_wmean(df.loc[keep, f"gap_{y1}"], w[keep])
                  - _wmean(df.loc[keep, f"gap_{y0}"], w[keep]))
        g6_ok = np.sign(d_jack) == np.sign(dgap)
        agree = np.sign(dL) == np.sign(dgap)
        share_narrow = float((df[f"gap_{y1}"] < df[f"gap_{y0}"]).mean())

        print(f"\n  {dim:12s} gap {g0:5.1f}pp ({y0})  ->  {g1:5.1f}pp ({y1})    "
              f"Δgap = {dgap:+5.1f}pp   95% CI [{lo:+.1f}, {hi:+.1f}]")
        print(f"               log-odds gap {l0:+.3f} -> {l1:+.3f}   ΔL = {dL:+.3f}   "
              f"sign agrees with Δgap: {agree}")
        print(f"               n={len(df)}  Kish neff={_kish(w):.1f}   "
              f"G6 drop-top-5 Δgap = {d_jack:+.1f}pp (sign-stable {g6_ok})   "
              f"{share_narrow:.0%} of economies narrowed")
        print(f"               G4 {fx.gate_coverage(fx.pan_dev, col, y1)}")
        res[dim] = {"g0": g0, "g1": g1, "dgap": dgap, "dL": dL, "agree": bool(agree),
                    "g6_ok": bool(g6_ok), "n": len(df), "neff": _kish(w), "ci": (lo, hi)}
    return res


if __name__ == "__main__":
    fx = Findex()
    print("E31 — the 13-year inequality panel: access vs usage gaps within countries")
    print("Frame: pan_grp, developing economies. UNTOUCHED frames used: education, age_cat,")
    print("laborforce (0 ledger mentions each); gender and income also included.\n")
    print("G3:", fx.gate_variant("account", ACCESS), fx.gate_variant("digital_payment", USAGE))
    print("G5: n/a — no official series for a within-country demographic gap")
    print("Advantaged group declared a priori:",
          {k: v[0] for k, v in DIMENSIONS.items()})

    acc = margin(fx, "ACCESS", ACCESS, ACCESS_WINDOW)
    use = margin(fx, "USAGE", USAGE, USAGE_WINDOW)

    print("\n" + "=" * 100)
    print("PRIMARY — pre-registered joint claim: access gaps close while usage gaps do not")
    print("=" * 100)
    print(f"  {'dimension':12s} {'Δgap access':>13s} {'ΔL access':>11s} {'Δgap usage':>12s}"
          f" {'ΔL usage':>10s}   {'closer?':>8s} {'divergent?':>11s}")
    A = B = J = 0
    for dim in DIMENSIONS:
        a, u = acc.get(dim), use.get(dim)
        if not a or not u:
            print(f"  {dim:12s} — insufficient coverage")
            continue
        # a dimension counts as an access-closer only if pp and log-odds AGREE (ceiling guard)
        closed = (a["dgap"] <= PP_BAR) and a["agree"]
        not_closed_use = u["dgap"] > PP_BAR
        divergent = closed and not_closed_use
        A += closed
        B += not_closed_use
        J += divergent
        print(f"  {dim:12s} {a['dgap']:+12.1f}pp {a['dL']:+11.3f} {u['dgap']:+11.1f}pp"
              f" {u['dL']:+10.3f}   {str(closed):>8s} {str(divergent):>11s}")
    claim_a, claim_b, joint = A >= 3, B >= 3, (A >= 3 and B >= 3 and J >= 3)
    print(f"\n  Claim A (access gaps closed, >=3 of 5 with Δgap <= -5pp AND log-odds agreement): "
          f"{A}/5 -> {claim_a}")
    print(f"  Claim B (usage gaps did NOT close, >=3 of 5 with Δgap > -5pp):                    "
          f"{B}/5 -> {claim_b}")
    print(f"  JOINT claim (A and B and >=3 of 5 divergent INDIVIDUALLY):                        "
          f"{J}/5 -> {joint}")
    print(f"\n  >>> REGISTERED VERDICT: joint claim {'KEPT' if joint else 'DISCARDED'}")

    print("\n" + "=" * 100)
    print("DESCRIPTIVE — urbanicity, 2024 only (single wave, excluded from the primary by design)")
    print("=" * 100)
    for col, lab in [(ACCESS, "account"), (USAGE, "digital payment")]:
        df = gap_frame(fx, "urbanicity", col, [2024])
        if len(df) >= 10:
            print(f"  urban - rural {lab:16s} gap 2024 = "
                  f"{_wmean(df['gap_2024'], df['pop']):+5.1f}pp   (n={len(df)}, "
                  f"Kish neff={_kish(df['pop']):.1f}, log-odds {_wmean(df['L_2024'], df['pop']):+.3f})")
