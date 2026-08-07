"""E34 (pre-registered): has the within-country AGE gap in account ownership narrowed, 2011->2024?

Program 3, item 3.4. Parent: E31 (first descendant, B3 not engaged).

B2 BREADTH CELL: `group == "age_cat"` — the one country frame at ZERO ledger mentions — plus the
2011->2014 transition, the thinnest in the ledger (2 mentions).

DESIGN, per the pre-registration:
  PRIMARY   unweighted SHARE of developing panel economies whose LOG-ODDS age gap
            (logit(p_25+) - logit(p_15-24)) is smaller in 2024 than in 2011.  Keep if >= 60%.
  SEC 1     pop-weighted mean d(log-odds gap) 2011->2024 with its UNWEIGHTED twin beside it;
            the keep also requires these two to carry the SAME (negative) sign.
  SEC 2     the same share per transition (2011->14, 14->17, 17->21, 21->24).
  SEC 3     the usage margin `g20_any` over 2014->2024, same statistics.
  DESCR     pp gap levels by wave, both margins.

Gates: G3 (headline columns), G4, G6 (drop-top-5 on the weighted mean), G5 n/a.
B6: 2,000-draw country bootstrap on the primary share and the weighted mean; Kish neff throughout.

DECLARED. Descriptive gap trajectories. No causal reading. Multi-wave, so B4 does not bind.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 34
SHARE_BAR = 0.60
CLIP = (0.005, 0.995)
ADV, DIS = "age 25+", "ages 15-24"          # advantaged / disadvantaged, declared
WAVES = [2011, 2014, 2017, 2021, 2024]


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _logit(p):
    p = np.clip(p, *CLIP)
    return np.log(p / (1 - p))


def gap_table(fx: Findex, col):
    """Per-country, per-wave age gap on `col`, developing panel economies.

    Returns two wide frames (log-odds gap, pp gap) indexed by country, columns = waves,
    plus a 2024 adult-population weight column."""
    g = fx.pan_grp[fx.pan_grp["group"] == "age_cat"]
    g = g[g["incomegroupwb24"] != "High income"]
    adv = g[g["group2"] == ADV].pivot_table(index="countrynewwb", columns="year", values=col)
    dis = g[g["group2"] == DIS].pivot_table(index="countrynewwb", columns="year", values=col)
    waves = [y for y in WAVES if y in adv.columns and y in dis.columns]
    lo = pd.DataFrame({y: _logit(adv[y]) - _logit(dis[y]) for y in waves})
    pp = pd.DataFrame({y: (adv[y] - dis[y]) * 100 for y in waves})
    # weight: the "all" slice's 2024 adult population, the harness convention
    pop = fx.pan_dev[fx.pan_dev["year"] == 2024].set_index("countrynewwb")["pop_adult"]
    lo["pop"], pp["pop"] = pop, pop
    return lo, pp


def _wmean(v, w):
    m = pd.notna(v) & pd.notna(w)
    return float(np.average(v[m], weights=w[m]))


def transition(lo, y0, y1, label, boot=True):
    """Share narrowing + weighted/unweighted mean change over one span."""
    d = pd.DataFrame({"d": lo[y1] - lo[y0], "pop": lo["pop"]}).dropna()
    share = float((d["d"] < 0).mean())
    wm, um = _wmean(d["d"], d["pop"]), float(d["d"].mean())
    neff, n = _kish(d["pop"]), len(d)

    ci_share = ci_wm = (np.nan, np.nan)
    if boot:
        rng = np.random.default_rng(SEED)
        idx = np.arange(n)
        bs, bw = [], []
        for _ in range(BOOT):
            s = d.iloc[rng.choice(idx, size=n, replace=True)]
            bs.append(float((s["d"] < 0).mean()))
            bw.append(_wmean(s["d"], s["pop"]))
        ci_share = (float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5)))
        ci_wm = (float(np.percentile(bw, 2.5)), float(np.percentile(bw, 97.5)))

    # G6 in its drop-top-5-population form, applied to the weighted mean
    keep = d["pop"].sort_values(ascending=False).index[5:]
    wm_drop = _wmean(d.loc[keep, "d"], d.loc[keep, "pop"])

    print(f"  {label:12s} n={n:3d} neff={neff:4.1f} | share narrowing={share:5.1%}"
          f" [{ci_share[0]:.1%},{ci_share[1]:.1%}]"
          f" | wmean={wm:+.3f} [{ci_wm[0]:+.3f},{ci_wm[1]:+.3f}]"
          f" | unwtd={um:+.3f} | wmean_droptop5={wm_drop:+.3f}")
    return {"span": label, "n": n, "neff": neff, "share": share, "share_lo": ci_share[0],
            "share_hi": ci_share[1], "wmean": wm, "wmean_lo": ci_wm[0], "wmean_hi": ci_wm[1],
            "unwtd": um, "wmean_droptop5": wm_drop}


def levels(fx: Findex, lo, pp, col, label):
    print(f"  pp gap (25+ minus 15-24), pop-weighted, {label}:")
    for y in [c for c in pp.columns if c != "pop"]:
        d = pd.DataFrame({"v": pp[y], "lov": lo[y], "pop": pp["pop"]}).dropna()
        print(f"     {y}: {_wmean(d['v'], d['pop']):+5.1f}pp   "
              f"log-odds {_wmean(d['lov'], d['pop']):+.3f}   (n={len(d)})")


def run(fx: Findex):
    out = {}
    for col, label, spans, full in [
        ("account_t_d", "ACCESS (account_t_d)",
         [(2011, 2014), (2014, 2017), (2017, 2021), (2021, 2024)], (2011, 2024)),
        ("g20_any", "USAGE (g20_any)",
         [(2014, 2017), (2017, 2021), (2021, 2024)], (2014, 2024)),
    ]:
        print(f"\n=== {label} — age gap, developing panel economies ===")
        lo, pp = gap_table(fx, col)
        print(f"  G3: {fx.gate_variant('account' if col == 'account_t_d' else 'digital_payment', col)}")
        print(f"  G4: {fx.gate_coverage(fx.pan_dev, col, full[1])}")
        levels(fx, lo, pp, col, label)
        print(f"  FULL SPAN {full[0]}->{full[1]} (primary for account):")
        out[(col, "full")] = transition(lo, full[0], full[1], f"{full[0]}->{full[1]}")
        print("  per transition:")
        out[(col, "trans")] = [transition(lo, a, b, f"{a}->{b}") for a, b in spans]
        # pp-gap twin of the full-span primary, secondary/descriptive only
        dpp = pd.DataFrame({"d": pp[full[1]] - pp[full[0]], "pop": pp["pop"]}).dropna()
        print(f"  [secondary, pp scale] share narrowing={float((dpp['d'] < 0).mean()):.1%} "
              f"wmean={_wmean(dpp['d'], dpp['pop']):+.2f}pp unwtd={dpp['d'].mean():+.2f}pp")

    p = out[("account_t_d", "full")]
    print("\n=== VERDICT (pre-registered) ===")
    print(f"  PRIMARY share narrowing 2011->2024 (log-odds) = {p['share']:.1%}  "
          f"bar = {SHARE_BAR:.0%}  -> {'PASS' if p['share'] >= SHARE_BAR else 'FAIL'}")
    same_sign = np.sign(p["wmean"]) == np.sign(p["unwtd"]) and p["wmean"] < 0
    print(f"  SIGN AGREEMENT weighted {p['wmean']:+.3f} vs unweighted {p['unwtd']:+.3f}, "
          f"both negative -> {'PASS' if same_sign else 'FAIL'}")
    print(f"  KEEP = {'YES' if (p['share'] >= SHARE_BAR and same_sign) else 'NO'}")
    u = out[("g20_any", "full")]
    print(f"  [SEC 3 two-margin] usage gap 2014->2024: share narrowing={u['share']:.1%}, "
          f"wmean={u['wmean']:+.3f}, unwtd={u['unwtd']:+.3f}")
    return out


if __name__ == "__main__":
    fx = Findex()
    run(fx)
