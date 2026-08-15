"""E48 (pre-registered 2026-08-15b): does the cash margin RETREAT where digital payment ADVANCES?
Agenda item 7.6. Parent: E45 (second descendant on that line; E47 has a different parent).

E45 found `fin31d` (level 47.1 -> 34.1 -> 20.5 -> 26.6) and `fin31d_s` to be the only country-file
columns whose 2024 LEVEL runs against `g20_any`, and read them — inferred, no questionnaire — as a
cash / non-digital residual margin. A level correlation is a cross-sectional composition fact. This
experiment asks the within-country dynamic question the level fact does not answer.

PEEK DISCLOSURE. E45 already computed the 2021->24 delta cell for both items (fin31d -0.113 wtd /
-0.317 unwtd; fin31d_s -0.158 / -0.541). That window is PEEKED and cannot support a keep here; it is
reported as a known reference only. The primary is registered on cells whose answer is unknown.

PRIMARY (registered): r(d fin31d, d g20_any) on the developing panel in 2014->2017, 2017->2021, and
the 2014->2024 LONG DIFFERENCE. Threshold r <= -0.30 in the predicted direction on BOTH lenses
(B9/B11) in AT LEAST TWO of the three registered cells. Under B4/B8: keep-general if the 2021->24
reference also agrees in sign, keep-window if it does not.

SECONDARY (registered) — CROSS-MODULE CASH COHERENCE. If fin31d measures a general cash margin rather
than one module's quirk, it should co-move with a cash margin in a DIFFERENT module. Correlate the
2014->2024 long difference of fin31d against the long difference of EACH of the four fin34 items —
all four, NO selection on E47's outcome — both lenses, with Benjamini-Hochberg at q = 0.10 over the
four tests (rule B7). Registered claim: at least one pair clears |r| >= 0.30 in the direction that has
both margins retreating together, on both lenses, and survives BH.

REGISTERED NULL READING, stated in advance so it cannot be written after the fact: a failure of the
primary does NOT rehabilitate the digital headline. It says E45's counter-moving LEVEL correlation is
a cross-sectional composition fact rather than a within-country dynamic one — exactly the distinction
this ledger has repeatedly failed at (E31, E36).

B6/B9/B10/B12 on every cell. fin31d_s is EXCLUDED from the delta design: E45 recorded it as
supporting 2021->24 only.

DECLARED. Delta->delta co-movement inside the same window identifies nothing; both margins may move
with a third factor. fin31d is a narrow, INDICATORS-unregistered variant under G3 whose meaning is
INFERRED from levels and coverage (HARNESS_V2_NOTES.md item 6), and that caveat travels with any
claim made here.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 48
WAVES = [2014, 2017, 2021, 2024]
CASH = "fin31d"
HEAD = "g20_any"
FIN34 = ["fin34a", "fin34b", "fin34c", "fin34d"]

REG_CELLS = [(2014, 2017), (2017, 2021), (2014, 2024)]   # registered, unpeeked
REF_CELL = (2021, 2024)                                  # peeked (E45) — reference only
BAR = -0.30
NEED = 2            # at least two of the three registered cells
Q = 0.10            # BH level on the secondary


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


def cell(T, xcol, ycol, a, b, fx, label):
    """One delta->delta cell with the full B6/B9/B10/B12 reporting block."""
    sub = T[[f"{xcol}@{a}", f"{xcol}@{b}", f"{ycol}@{a}", f"{ycol}@{b}", "pop"]].dropna()
    if len(sub) < 10:
        return None
    out = pd.DataFrame({"x": sub[f"{xcol}@{b}"] - sub[f"{xcol}@{a}"],
                        "y": sub[f"{ycol}@{b}"] - sub[f"{ycol}@{a}"],
                        "w": sub["pop"]})
    rw, n = corr(out["x"], out["y"], out["w"])
    ru, _ = corr(out["x"], out["y"])
    lo, up, pb = boot_ci(out, lambda s: corr(s["x"], s["y"], s["w"])[0])
    g6 = fx.gate_jackknife(out["x"], out["y"], out["w"])
    loo = sorted(((corr(out.drop(i)["x"], out.drop(i)["y"], out.drop(i)["w"])[0] - rw, i)
                  for i in out.index), key=lambda t: -abs(t[0]))[0]
    return {"label": label, "r_w": rw, "ci": (lo, up), "p_boot": pb,
            "g6": g6["r_droptop"], "r_u": ru, "n": n, "neff": kish(out["w"]),
            "loo": loo, "wmean_x": float(np.average(out["x"], weights=out["w"])),
            "wmean_y": float(np.average(out["y"], weights=out["w"]))}


def show(rows, header):
    print(f"  {'cell':14s}{'r_w':>9s}{'[95% CI]':>20s}{'p_boot':>9s}{'G6':>9s}{'r_u':>9s}"
          f"{'n':>5s}{'neff':>7s}  {'wtd d x / d y':>18s}  largest LOO")
    for r in rows:
        ci = f"[{r['ci'][0]:+.3f}, {r['ci'][1]:+.3f}]"
        dd = f"{r['wmean_x']:+.2f} / {r['wmean_y']:+.2f}"
        print(f"  {r['label']:14s}{r['r_w']:>9.3f}{ci:>20s}{r['p_boot']:>9.3f}"
              f"{r['g6']:>9.3f}{r['r_u']:>9.3f}{r['n']:>5d}{r['neff']:>7.1f}  {dd:>18s}  "
              f"{r['loo'][1]} {r['loo'][0]:+.3f}")


def main():
    fx = Findex()
    dev = fx.pan_dev
    d = dev[dev["year"].isin(WAVES)]

    tab = {}
    for c in [CASH, HEAD] + FIN34:
        w = d.pivot_table(index="countrynewwb", columns="year", values=c) * 100
        for y in WAVES:
            tab[f"{c}@{y}"] = w[y] if y in w.columns else pd.Series(dtype=float)
    T = pd.DataFrame(tab)
    T["pop"] = dev[dev["year"] == 2024].set_index("countrynewwb")["pop_adult"].reindex(T.index)

    print("=" * 128)
    print("E48 — does the cash margin retreat where digital payment advances? (agenda item 7.6)")
    print("=" * 128)

    # E35 rule: reproduce E45's published 2021->24 cell before reading anything registered.
    ref = cell(T, CASH, HEAD, *REF_CELL, fx, "2021->2024 REF")
    print(f"\nE35 RULE — reproduce E45's peeked cell first: r_w {ref['r_w']:+.3f} "
          f"(E45 published -0.113), r_u {ref['r_u']:+.3f} (E45 published -0.317)")
    assert abs(ref["r_w"] - (-0.113)) <= 0.02 and abs(ref["r_u"] - (-0.317)) <= 0.02, "ABORT"
    print("  reproduced within 0.02 — proceeding.")

    # ---------------------------------------------------------------- PRIMARY
    print("\n" + "-" * 128)
    print("PRIMARY (registered): r(d fin31d, d g20_any). Bar: r <= -0.30 on BOTH lenses in "
          ">= 2 of the 3 registered cells")
    print("-" * 128)
    rows = [cell(T, CASH, HEAD, a, b, fx, f"{a}->{b}") for a, b in REG_CELLS]
    rows = [r for r in rows if r]
    show(rows, "")
    print("  " + "-" * 124)
    show([ref], "")
    print("  (the 2021->2024 row is PEEKED — E45 — and is a sign reference only, never a keep)")

    passes = [r for r in rows if r["r_w"] <= BAR and r["r_u"] <= BAR]
    print(f"\n  cells clearing {BAR:+.2f} on BOTH lenses: {len(passes)} of {len(rows)} "
          f"({', '.join(r['label'] for r in passes) if passes else 'none'})")
    prim = len(passes) >= NEED
    if prim:
        status = "keep-general" if np.sign(ref["r_w"]) < 0 else "keep-window"
        print(f"  -> PRIMARY KEEP ({status}; the peeked reference "
              f"{'agrees' if np.sign(ref['r_w']) < 0 else 'disagrees'} in sign)")
    else:
        print("  -> PRIMARY DISCARD")

    # -------------------------------------------------------------- SECONDARY
    print("\n" + "-" * 128)
    print("SECONDARY (registered): cross-module cash coherence — d fin31d (2014->2024) vs "
          "d fin34x (2014->2024), all four, BH q=0.10")
    print("-" * 128)
    srows = []
    for c in FIN34:
        r = cell(T, CASH, c, 2014, 2024, fx, c)
        if r:
            srows.append(r)
    show(srows, "")
    ps = sorted(((r["p_boot"], r) for r in srows))
    m = len(ps)
    print(f"\n  Benjamini-Hochberg, q = {Q}, m = {m} tests (on p_boot, the weighted lens):")
    bh_ok = set()
    for i, (p, r) in enumerate(ps, start=1):
        crit = Q * i / m
        mark = "REJECT" if p <= crit else "  --  "
        if p <= crit:
            bh_ok.add(r["label"])
        print(f"    {i}. {r['label']:10s} p_boot {p:.4f}  vs  {crit:.4f}   {mark}")
    # BH step-up: everything up to the largest rejecting index
    idx = [i for i, (p, r) in enumerate(ps, start=1) if p <= Q * i / m]
    bh_ok = {r["label"] for i, (p, r) in enumerate(ps, start=1) if i <= (max(idx) if idx else 0)}

    coherent = [r for r in srows
                if abs(r["r_w"]) >= 0.30 and abs(r["r_u"]) >= 0.30
                and np.sign(r["r_w"]) == np.sign(r["r_u"]) and r["label"] in bh_ok]
    print(f"\n  pairs clearing |r| >= 0.30 on BOTH lenses with agreeing signs AND surviving BH: "
          f"{', '.join(r['label'] for r in coherent) if coherent else 'NONE'}")
    if coherent:
        print("  (sign reading: fin31d and the fin34 item both fall together => POSITIVE r, "
              "since both deltas are negative where cash retreats)")
    sec = bool(coherent)
    print(f"  -> SECONDARY {'KEEP' if sec else 'DISCARD'}")

    print("\n" + "=" * 128)
    print(f"E48 VERDICT: PRIMARY {'KEEP' if prim else 'DISCARD'} | "
          f"SECONDARY {'KEEP' if sec else 'DISCARD'}")
    if not prim:
        print("  Registered null reading (written before the answer): this does NOT rehabilitate the")
        print("  digital headline. It says E45's counter-moving LEVEL correlation is a cross-sectional")
        print("  composition fact, not a within-country dynamic one.")
    print("=" * 128)


if __name__ == "__main__":
    main()
