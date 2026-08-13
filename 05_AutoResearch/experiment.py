"""E42 (pre-registered 2026-08-13): is the UNWEIGHTED ledger a different ledger?

Program 2, item 2.6. Parent: **E40** (the ledger-wide BH + de-weighting audit) — first descendant,
inside rule B3's cap.

WHY. E40's claim C failed and E41 produced a third live instance the same day: the population
weighting sets the keep/discard boundary in BOTH directions (E16 +0.198w/+0.555u, E26 +0.294w/+0.364u,
E41 +0.039w/+0.418u). Rule B9 now requires a `keep-weighted`/`discard-weighted` status when the two
lenses disagree. A re-status alone is bookkeeping; the question worth registering is whether the
UNWEIGHTED result is a regularity or a one-window accident — rule B8 applied to the unweighted lens.

COVERAGE FACT CHECKED BEFORE REGISTRATION (no outcome computed): `fin24aSD_ND` exists for 2021 and
2024 only, so E26 can NEVER be replicated on an earlier window (unpromotable, like E29).
`account_t_d` and `fin17a_17a1_d` have all five waves, so E16 can be tested on three earlier
transitions. The generality test therefore binds on E16 only. Declared up front.

P1 — RE-STATUS UNDER B9 (mechanical, executed either way). Recompute E16 and E26 in 2021->24 under
both lenses from raw frames. PASS if both reproduce E40's figures within 0.02; on passing, both rows
move `discard` -> `discard-weighted`.

P2 — THE REGISTERED CLAIM (B8 on the unweighted lens). Unweighted r(d account_t_d, d fin17a_17a1_d)
on the developing panel in 2011->14, 2014->17 and 2017->21. KEEP: r_u >= +0.30 AND positive in ALL
THREE earlier windows. Any window below the bar or of the opposite sign is a DISCARD. 2014->2017 is
a known low-power window (five of six unstable cells across E28/E30) but still counts — B8 admits no
exemptions chosen after the fact.

P3 — IS THE DIVERGENCE ONE ECONOMY? Leave-one-economy-out on the 2021->24 weighted E16 cell.
BAR: max |d r_w| >= 0.20 => single-economy artifact (name it); every drop < 0.20 => distributed
weighting effect, and the ledger's "five economies decide it" language needs softening.

B6 on every cell: 2,000-draw country bootstrap percentile interval, Kish neff, both lenses.

DECLARED. P1 creates no new association. P2's claim, if it passes, is a descriptive co-movement of
contemporaneous changes — it identifies nothing and is not causal. An unweighted correlation
describes the typical ECONOMY, not the typical PERSON; that difference is the finding's content.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 42
P2_BAR = 0.30
P3_BAR = 0.20

ACC = "account_t_d"
SAV = "fin17a_17a1_d"
WAGE = "fin32_acc"
RES = "fin24aSD_ND"

WINDOWS = [(2011, 2014), (2014, 2017), (2017, 2021), (2021, 2024)]
EARLIER = [(2011, 2014), (2014, 2017), (2017, 2021)]

# E40's figures on record, for the P1 reproduction check
ON_RECORD = {"E16": (0.198, 0.555), "E26": (0.294, 0.364)}


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _ucorr(x, y):
    m = pd.notna(x) & pd.notna(y)
    return float(np.corrcoef(x[m], y[m])[0, 1]) if m.sum() >= 10 else np.nan


def delta(fx, col, window):
    t0, t1 = window
    w = fx.country_panel(fx.pan_dev, col, [t0, t1])
    if t0 not in w.columns or t1 not in w.columns:
        return pd.DataFrame(columns=["d", "pop"])
    return pd.DataFrame({"d": w[t1] - w[t0], "pop": w["pop"]}).dropna()


def cell(fx, xcol, ycol, window):
    """Aligned per-country delta pair for one window, indexed by economy name."""
    dx, dy = delta(fx, xcol, window), delta(fx, ycol, window)
    return pd.DataFrame({"dx": dx["d"], "dy": dy["d"], "pop": dx["pop"]}).dropna()


def boot(fx, df, weighted, draws=BOOT, seed=SEED):
    """Country bootstrap percentile interval + two-sided p for the null r = 0."""
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        d = df.iloc[rng.choice(idx, size=len(idx), replace=True)]
        r = fx.weighted_corr(d["dx"], d["dy"], d["pop"])[0] if weighted \
            else _ucorr(d["dx"].values, d["dy"].values)
        if pd.notna(r):
            out.append(r)
    a = np.asarray(out)
    tail = min((a <= 0).mean(), (a >= 0).mean())
    return (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)),
            float(max(2.0 * tail, 1.0 / draws)))


def report(fx, df, label, weighted_primary=True):
    rw, n = fx.weighted_corr(df["dx"], df["dy"], df["pop"])
    ru = _ucorr(df["dx"].values, df["dy"].values)
    lo, hi, p = boot(fx, df, weighted=weighted_primary)
    g6 = fx.gate_jackknife(df["dx"], df["dy"], df["pop"])
    rd = g6.get("r_droptop")
    prim = rw if weighted_primary else ru
    ret = abs(rd) / abs(prim) if (rd is not None and pd.notna(rd) and abs(prim) > 1e-9) else np.nan
    lens = "w" if weighted_primary else "u"
    print(f"  {label:30s} r_w={rw:+.3f}  r_u={ru:+.3f}  n={n:3d}  neff={_kish(df['pop']):5.1f}  "
          f"CI_{lens}[{lo:+.3f},{hi:+.3f}]  p_boot={p:.4f}  G6={rd:+.3f} (ret {ret:.2f})")
    return {"r_w": rw, "r_u": ru, "n": n, "neff": _kish(df["pop"]), "lo": lo, "hi": hi,
            "p": p, "g6": rd, "ret": ret}


def run(fx: Findex):
    print("=" * 112)
    print("E42 — is the UNWEIGHTED ledger a different ledger? (Program 2 item 2.6; parent E40)")
    print("=" * 112)

    # ------------------------------------------------------------------ P1
    print("\nP1 — B9 RE-STATUS: reproduce E16 and E26 in 2021->24 under both lenses")
    print("     (bar: within 0.02 of E40's figures on record)\n")
    p1 = {}
    for name, (xc, yc) in [("E16", (ACC, SAV)), ("E26", (WAGE, RES))]:
        d = cell(fx, xc, yc, (2021, 2024))
        res = report(fx, d, f"{name} 2021->24")
        rec_w, rec_u = ON_RECORD[name]
        ok = abs(res["r_w"] - rec_w) <= 0.02 and abs(res["r_u"] - rec_u) <= 0.02
        disagree = (abs(res["r_w"]) < P2_BAR) != (abs(res["r_u"]) < P2_BAR)
        print(f"     on record r_w={rec_w:+.3f} r_u={rec_u:+.3f} -> reproduced: {ok}; "
              f"lenses disagree at 0.30: {disagree}")
        p1[name] = {"ok": ok, "disagree": disagree, **res}
    p1_pass = all(v["ok"] for v in p1.values())
    print(f"\n  P1 VERDICT: {'PASS' if p1_pass else 'FAIL'} — both reproduce within 0.02: {p1_pass}")

    # ------------------------------------------------------------------ P2
    print("\n" + "-" * 112)
    print("P2 — B8 ON THE UNWEIGHTED LENS: r_u(d account, d formal saving) in every earlier window")
    print("     (bar: r_u >= +0.30, positive sign, in ALL THREE)\n")
    p2 = {}
    for w in WINDOWS:
        d = cell(fx, ACC, SAV, w)
        p2[w] = report(fx, d, f"{w[0]}->{w[1]}", weighted_primary=False)
    passes = {w: (p2[w]["r_u"] >= P2_BAR) for w in EARLIER}
    print("\n     earlier-window bar (r_u >= +0.30, positive):")
    for w in EARLIER:
        print(f"       {w[0]}->{w[1]}  r_u={p2[w]['r_u']:+.3f}  "
              f"{'PASS' if passes[w] else 'FAIL'}")
    p2_pass = all(passes.values())
    print(f"\n  P2 VERDICT: {'KEEP' if p2_pass else 'DISCARD'} — "
          f"{sum(passes.values())}/3 earlier windows clear the bar")

    # de-weighting shift per window, reported as context
    print("\n     de-weighting shift (r_u - r_w) by window:")
    for w in WINDOWS:
        print(f"       {w[0]}->{w[1]}  r_w={p2[w]['r_w']:+.3f}  r_u={p2[w]['r_u']:+.3f}  "
              f"shift={p2[w]['r_u'] - p2[w]['r_w']:+.3f}")

    # ------------------------------------------------------------------ P3
    print("\n" + "-" * 112)
    print("P3 — LEAVE-ONE-ECONOMY-OUT on the 2021->24 weighted E16 cell")
    print(f"     (bar: max |d r_w| >= {P3_BAR} => single-economy artifact)\n")
    d = cell(fx, ACC, SAV, (2021, 2024))
    r_full = fx.weighted_corr(d["dx"], d["dy"], d["pop"])[0]
    loo = {}
    for e in d.index:
        s = d.drop(index=e)
        loo[e] = fx.weighted_corr(s["dx"], s["dy"], s["pop"])[0] - r_full
    loo = pd.Series(loo).sort_values(key=abs, ascending=False)
    print(f"     full-sample r_w = {r_full:+.3f} (r_u = {p2[(2021, 2024)]['r_u']:+.3f}, "
          f"gap = {p2[(2021, 2024)]['r_u'] - r_full:+.3f})")
    print("     largest single-economy effects on r_w:")
    for e, v in loo.head(8).items():
        pop_share = d.loc[e, "pop"] / d["pop"].sum() * 100
        print(f"       drop {e:22s} d r_w = {v:+.3f}   -> r_w = {r_full + v:+.3f}   "
              f"(pop share {pop_share:4.1f}%)")
    p3_single = abs(loo.iloc[0]) >= P3_BAR
    print(f"\n  P3 VERDICT: max |d r_w| = {abs(loo.iloc[0]):.3f} ({loo.index[0]}) -> "
          f"{'SINGLE-ECONOMY ARTIFACT' if p3_single else 'DISTRIBUTED WEIGHTING EFFECT'}")

    # how many economies must be dropped before r_w reaches the unweighted value?
    order = d.assign(share=d["pop"] / d["pop"].sum()).sort_values("share", ascending=False)
    target = p2[(2021, 2024)]["r_u"]
    print("\n     cumulative drop of the largest economies (E16 2021->24):")
    for k in range(0, 7):
        s = d.drop(index=order.index[:k]) if k else d
        rk = fx.weighted_corr(s["dx"], s["dy"], s["pop"])[0]
        print(f"       drop top {k}: r_w = {rk:+.3f}   n = {len(s)}   "
              f"neff = {_kish(s['pop']):5.1f}" + ("   <- unweighted target %+.3f" % target
                                                  if k == 0 else ""))

    print("\n" + "=" * 112)
    print(f"SUMMARY  P1 {'PASS' if p1_pass else 'FAIL'} (re-status E16/E26 -> discard-weighted)  |  "
          f"P2 {'KEEP' if p2_pass else 'DISCARD'}  |  "
          f"P3 {'single-economy' if p3_single else 'distributed'}")
    print("=" * 112)


if __name__ == "__main__":
    run(Findex())
