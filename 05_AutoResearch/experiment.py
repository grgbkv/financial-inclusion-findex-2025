"""E37 (pre-registered): does financial deepening follow a SEQUENCING LADDER?

Program 6, items 6.1-6.3. Parent: E17 / E5 (the level->change family). NOT E31 (whose lineage
cap is exhausted) and NOT the rails chain.

B2 BREADTH CELLS, three of them:
  * Program 6 has ZERO prior experiments.
  * `borrow_any_t_d` is an UNTOUCHED country module (rung R3's destination).
  * This is the loop's FIRST lagged design under rule B5: a LEVEL at t against a CHANGE over
    t->t+1, pooled across THREE transitions rather than the usual single 2021->2024 window.

WHY. Every country-level association in the ledger correlates contemporaneous changes, which is
why every claim carries "identifies nothing". The ladder hypothesis is a real theory rather than a
correlation hunt: margins deepen in order — account -> digital payment -> formal saving ->
borrowing — so the LEVEL of a rung at t should predict the SUBSEQUENT GROWTH of the rung above it.

DESIGN, per the pre-registration:
  frame       pan_dev, group == "all" (77 non-high-income panel economies)
  transitions 2014->2017, 2017->2021, 2021->2024
  R1 (6.1)    up = account_t_d      level(t) -> down = d g20_any
  R2 (6.2)    up = g20_any          level(t) -> down = d fin17a_17a1_d
  R3 (6.3)    up = fin17a_17a1_d    level(t) -> down = d borrow_any_t_d   [untouched module]
  PRIMARY     pooled pop-weighted corr over stacked country-transition rows (a country appears
              three times, each row carrying its 2024 adult population as weight)
  PARTIAL     both sides residualized on the DOWNSTREAM margin's own level at t, pop-weighted LS
              (the E5b/E23 construction) — strips the pure convergence channel
  BENCHMARK   r(L_down(t), d_down) — the convergence rate the ladder has to beat (E17: -0.301)

REGISTERED KEEP RULE (joint claim). Keep only if for EVERY rung R1, R2, R3:
  (i)  pooled weighted r >= +0.30, AND
  (ii) the own-level partial keeps its sign and retains >= 0.5 of the raw magnitude (E4 rule).
Registered alternative outcome: negative pooled correlations on all three rungs say the panel is
dominated by convergence and closes items 6.1-6.4 rather than inviting a variant.

Gates: G3 (all four columns are declared headline variants) · G4 per margin/wave · G6 drop-top-5
by population · B6 country bootstrap 2,000 draws resampling COUNTRIES (carrying all three of a
country's transitions together, so pooling does not fake independence) + Kish neff.

DECLARED. Descriptive temporal ordering only. A level measured before a change is not
identification and nothing here is causal. The pooled n counts country-transition rows, not
independent countries — which is precisely what the country-level bootstrap and neff are for.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 37
R_BAR = 0.30
RETENTION_BAR = 0.5
TRANSITIONS = [(2014, 2017), (2017, 2021), (2021, 2024)]

# rung -> (agenda item, upstream col, upstream concept, downstream col, downstream concept)
RUNGS = [
    ("R1", "6.1", "account_t_d",   "account",         "g20_any",        "digital_payment"),
    ("R2", "6.2", "g20_any",       "digital_payment", "fin17a_17a1_d",  "saved_formally"),
    ("R3", "6.3", "fin17a_17a1_d", "saved_formally",  "borrow_any_t_d", None),
]


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _wcorr(x, y, w):
    m = pd.notna(x) & pd.notna(y) & pd.notna(w)
    x, y, w = np.asarray(x[m], float), np.asarray(y[m], float), np.asarray(w[m], float)
    if len(x) < 10:
        return np.nan, len(x)
    mx, my = np.average(x, weights=w), np.average(y, weights=w)
    sx = np.sqrt(np.average((x - mx) ** 2, weights=w))
    sy = np.sqrt(np.average((y - my) ** 2, weights=w))
    if sx == 0 or sy == 0:
        return np.nan, len(x)
    return float(np.average((x - mx) * (y - my), weights=w) / (sx * sy)), len(x)


def _wresid(y, z, w):
    """Pop-weighted LS residual of y on z (with intercept) — the E5b/E23 construction."""
    y, z, w = np.asarray(y, float), np.asarray(z, float), np.asarray(w, float)
    mz, my = np.average(z, weights=w), np.average(y, weights=w)
    var = np.average((z - mz) ** 2, weights=w)
    b = 0.0 if var == 0 else np.average((z - mz) * (y - my), weights=w) / var
    return y - (my + b * (z - mz))


def build(fx: Findex, up_col, down_col):
    """Stacked country-transition rows: upstream level at t, downstream change t->t+1,
    downstream own level at t, weight, country, transition."""
    d = fx.pan_dev
    rows = []
    for t0, t1 in TRANSITIONS:
        up = fx.country_panel(d, up_col, [t0])
        dn = fx.country_panel(d, down_col, [t0, t1])
        j = pd.DataFrame({
            "up_level": up[t0],
            "down_t0": dn[t0],
            "down_d": dn[t1] - dn[t0],
            "pop": dn["pop"],
        }).dropna()
        j["country"] = j.index
        j["span"] = f"{t0}->{t1}"
        rows.append(j.reset_index(drop=True))
    return pd.concat(rows, ignore_index=True)


def stats(df):
    """Raw corr, own-level partial, convergence benchmark, neff — on one stacked table.

    The reset_index is load-bearing: _wresid returns bare arrays, so a sliced (non-zero-based)
    frame would silently misalign them against the weights and return NaN partials.
    """
    df = df.reset_index(drop=True)
    w = df["pop"]
    raw, n = _wcorr(df["up_level"], df["down_d"], w)
    bench, _ = _wcorr(df["down_t0"], df["down_d"], w)
    rx = _wresid(df["up_level"], df["down_t0"], w)
    ry = _wresid(df["down_d"], df["down_t0"], w)
    part, _ = _wcorr(pd.Series(rx), pd.Series(ry), w)
    # Two neffs. The row-level one is inflated by stacking: a country contributing three rows
    # triples the weight sum without adding an economy. The country-level one — each economy's
    # population counted once — is the honest degrees-of-freedom figure.
    cw = df.groupby("country")["pop"].max()
    return {"r": raw, "partial": part, "bench": bench, "n": n,
            "n_countries": df["country"].nunique(),
            "neff": _kish(w), "neff_country": _kish(cw)}


def bootstrap_countries(df, rng, draws=BOOT):
    """B6: resample COUNTRIES with replacement, carrying all of a country's transitions."""
    by = {c: g for c, g in df.groupby("country")}
    names = np.array(list(by))
    out_r, out_p = [], []
    for _ in range(draws):
        pick = rng.choice(names, size=len(names), replace=True)
        s = pd.concat([by[c] for c in pick], ignore_index=True)
        st = stats(s)
        if pd.notna(st["r"]):
            out_r.append(st["r"])
            out_p.append(st["partial"])
    return np.array(out_r), np.array(out_p)


def drop_top(df, k=5):
    """G6: drop the k largest-population economies (by their single 2024 population)."""
    pops = df.groupby("country")["pop"].max().sort_values(ascending=False)
    return df[~df["country"].isin(pops.head(k).index)]


def run(fx: Findex):
    rng = np.random.default_rng(SEED)
    print("=" * 92)
    print("E37 — THE SEQUENCING LADDER: level of a rung at t -> subsequent growth of the rung above")
    print("=" * 92)
    print(f"frame pan_dev group=all | transitions {', '.join(f'{a}->{b}' for a, b in TRANSITIONS)}")
    print(f"keep rule: every rung pooled r >= +{R_BAR:.2f} AND own-level partial keeps sign with "
          f">= {RETENTION_BAR} retention\n")

    summary = []
    for tag, item, up_col, up_con, down_col, down_con in RUNGS:
        df = build(fx, up_col, down_col)
        st = stats(df)
        st_dt = stats(drop_top(df))
        br, bp = bootstrap_countries(df, rng)
        lo, hi = np.percentile(br, [2.5, 97.5])
        plo, phi = np.percentile(bp, [2.5, 97.5])
        p_boot = 2 * min((br <= 0).mean(), (br >= 0).mean())
        retention = abs(st["partial"]) / abs(st["r"]) if st["r"] else np.nan
        sign_ok = np.sign(st["partial"]) == np.sign(st["r"])

        print("-" * 92)
        print(f"{tag} (agenda {item}):  level({up_col}) at t  ->  d({down_col}) over t->t+1")
        print(f"  pooled rows n={st['n']} over {st['n_countries']} economies | Kish neff "
              f"{st['neff']:.1f} row-level, {st['neff_country']:.1f} COUNTRY-level (the honest one)")
        print(f"  PRIMARY pooled weighted r        = {st['r']:+.3f}   95% CI [{lo:+.3f}, {hi:+.3f}]  "
              f"p_boot={p_boot:.3f}")
        print(f"  own-level partial (E5b constr.)  = {st['partial']:+.3f}   95% CI [{plo:+.3f}, {phi:+.3f}]"
              f"   retention={retention:.2f} sign_kept={bool(sign_ok)}")
        print(f"  convergence benchmark r(L_down,d)= {st['bench']:+.3f}  (what the ladder must beat)")
        print(f"  G6 drop-top-5 pop: r = {st_dt['r']:+.3f} (partial {st_dt['partial']:+.3f}, "
              f"n={st_dt['n']}, neff={st_dt['neff']:.1f})")
        for (t0, t1) in TRANSITIONS:
            s = df[df["span"] == f"{t0}->{t1}"]
            ss = stats(s)
            print(f"    {t0}->{t1}: r={ss['r']:+.3f}  partial={ss['partial']:+.3f}  "
                  f"bench={ss['bench']:+.3f}  n={ss['n']:3d}  neff={ss['neff']:4.1f}  "
                  f"mean d_down={np.average(s['down_d'], weights=s['pop']):+5.2f}pp")
        # G4 coverage on both endpoints of the newest transition
        for col, con in ((up_col, up_con), (down_col, down_con)):
            g4 = fx.gate_coverage(fx.pan_dev, col, 2021)
            g3 = fx.gate_variant(con, col) if con else {"gate": "G3_variant", "ok": True,
                                                        "note": "no variant registry entry"}
            print(f"    gate {col:16s} G4 {g4['ok']} (n={g4['n_countries']}, "
                  f"pop {g4['pop_share']}) | G3 {g3['ok']}")

        passes = (pd.notna(st["r"]) and st["r"] >= R_BAR and sign_ok
                  and retention >= RETENTION_BAR)
        print(f"  --> rung {tag} {'PASSES' if passes else 'FAILS'} the registered conditions")
        summary.append({"rung": tag, "r": st["r"], "partial": st["partial"],
                        "bench": st["bench"], "retention": retention, "pass": passes,
                        "neff_country": st["neff_country"], "ci": (lo, hi), "p_boot": p_boot,
                        "r_droptop": st_dt["r"], "n": st["n"]})

    print("=" * 92)
    tbl = pd.DataFrame(summary)
    print(tbl.to_string(index=False))
    kept = bool(tbl["pass"].all())
    print("\nJOINT LADDER CLAIM:", "KEEP" if kept else "DISCARD")
    if not kept:
        neg = (tbl["r"] < 0).all()
        print("  registered alternative outcome (all three rungs negative):", neg)
    print("=" * 92)
    return tbl


if __name__ == "__main__":
    run(Findex())
