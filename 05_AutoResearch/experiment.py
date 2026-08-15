"""E47 (pre-registered 2026-08-15b): `fin34` (wage payment modes) — the cycle's UNTOUCHED-MODULE draw.

`fin34` is 8 columns x four waves x ~77 developing economies with ZERO ledger mentions: after E45
took `fin31`, it is the best-covered untouched country module left. No parent finding — this is a
breadth draw from the B2 note, not a descendant of anything.

PART A — MAPPING PASS (EXPLORATORY, peek rule). Per-wave developing-panel country counts and
population-weighted levels for all eight columns. Labels are INFERRED from levels and coverage and
are documented as inferred, never authoritative — the repo holds no questionnaire. Part A was
computed before the Part B registration was written and is disclosed as such. No keep hangs on it.

PART B — THE REGISTERED ORIENTATION SCREEN. For each of the four unsuffixed items (fin34a-fin34d),
the 2024 cross-sectional level correlation against the digital-payment headline `g20_any` and against
`account_t_d`, on the developing panel. Four-way classification, fixing the bar E45 recorded as
mis-specified (it was written to catch ORTHOGONAL items and could not see a strongly negative one):

    restatement    |r| >= 0.80
    aligned        +0.30 <= r < 0.80
    counter-moving      r <= -0.30
    independent    |r| < 0.30

Classification requires BOTH lenses to agree; where they disagree the item is `mixed-lens` (B9/B11).

REGISTERED CLAIM (the keep/discard object): "at least one fin34 item counter-moves the
digital-payment headline at r_level <= -0.30 on BOTH lenses in the 2024 cross-section."
Coverage floor: >= 30 developing-panel economies in 2024 AND a weighted level >= 1.0pp (an item at
0.1pp of adults is a floor, not a margin).

B6/B9/B10/B12 on every cell: 2,000-draw country bootstrap percentile interval, unweighted twin,
Kish neff beside nominal n with no significance language on nominal n, G6 drop-top-5, and the NAMED
largest single leave-one-economy-out effect.

DECLARED. Cross-sectional 2024 levels; no trend language on Part B. Every fin34 item is a narrow
variant of the wage/payment-mode concept under G3, unregistered in INDICATORS, and declared narrow.
A correlation between an item and the headline is a statement about MEASUREMENT ORIENTATION, not
behaviour.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 47
WAVES = [2014, 2017, 2021, 2024]
FIN34 = ["fin34a", "fin34b", "fin34c", "fin34d",
         "fin34a_s", "fin34b_s", "fin34c_s", "fin34d_s"]
SCREEN = ["fin34a", "fin34b", "fin34c", "fin34d"]
HEADS = ["g20_any", "account_t_d"]

MIN_C = 30           # coverage floor: developing-panel economies in 2024
MIN_LEVEL = 1.0      # coverage floor: weighted 2024 level in pp
RESTATE = 0.80
ALIGN = 0.30


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
    def one(r):
        if not np.isfinite(r):
            return "n/a"
        if abs(r) >= RESTATE:
            return "restatement"
        if r <= -ALIGN:
            return "counter-moving"
        if r >= ALIGN:
            return "aligned"
        return "independent"
    a, b = one(rw), one(ru)
    return a if a == b else f"mixed-lens ({a} / {b})"


def main():
    fx = Findex()
    dev = fx.pan_dev
    d = dev[dev["year"].isin(WAVES)]

    print("=" * 120)
    print("E47 — fin34 (wage payment modes): the cycle's untouched-module draw")
    print("=" * 120)

    # -------------------------------------------------------------- PART A
    print("\n" + "=" * 120)
    print("PART A — MAPPING PASS (EXPLORATORY, peek rule; labels INFERRED from levels and coverage, "
          "NOT authoritative)")
    print("=" * 120)
    print(f"  {'column':14s}" + "".join(f"{y:>20d}" for y in WAVES))
    print(f"  {'':14s}" + "".join(f"{'n / wtd level pp':>20s}" for _ in WAVES))
    levels = {}
    for c in FIN34 + HEADS:
        cells = []
        for y in WAVES:
            dy = d[d["year"] == y]
            n = int(dy[c].notna().sum())
            v = Findex.wmean(dy, c) * 100 if n else np.nan
            levels[(c, y)] = (n, v)
            cells.append(f"{n:>3d} / {v:>8.1f}" if n else f"{'—':>14s}")
        star = "  <-- headline" if c in HEADS else ""
        print(f"  {c:14s}" + "".join(f"{s:>20s}" for s in cells) + star)

    # -------------------------------------------------------------- panel
    tab = {}
    for c in SCREEN + HEADS:
        w = d.pivot_table(index="countrynewwb", columns="year", values=c) * 100
        for y in WAVES:
            tab[(c, y)] = w[y] if y in w.columns else pd.Series(dtype=float)
    T = pd.DataFrame(tab)
    T["pop"] = dev[dev["year"] == 2024].set_index("countrynewwb")["pop_adult"].reindex(T.index)

    # -------------------------------------------------------------- PART B
    print("\n" + "=" * 120)
    print("PART B — REGISTERED ORIENTATION SCREEN (2024 cross-section)")
    print("=" * 120)
    qualifying, skipped = [], []
    for c in SCREEN:
        n, v = levels[(c, 2024)]
        (qualifying if (n >= MIN_C and np.isfinite(v) and v >= MIN_LEVEL) else skipped).append(
            (c, n, v))
    for c, n, v in skipped:
        print(f"  EXCLUDED {c}: n={n}, 2024 weighted level {v:.1f}pp "
              f"(floors: n >= {MIN_C}, level >= {MIN_LEVEL}pp)")
    print(f"  qualifying items: {', '.join(c for c, _, _ in qualifying)}\n")

    hits = []
    for head in HEADS:
        print("-" * 120)
        print(f"  vs {head}")
        print(f"  {'item':10s}{'r_w':>9s}{'[95% CI]':>20s}{'p_boot':>9s}{'G6':>9s}"
              f"{'r_u':>9s}{'n':>5s}{'neff':>7s}  {'classification':<28s}{'largest LOO'}")
        for c, _, _ in qualifying:
            sub = T[[(c, 2024), (head, 2024), "pop"]].dropna()
            sub.columns = ["x", "y", "w"]
            rw, n = corr(sub["x"], sub["y"], sub["w"])
            ru, _ = corr(sub["x"], sub["y"])
            lo, up, pb = boot_ci(sub, lambda s: corr(s["x"], s["y"], s["w"])[0])
            g6 = fx.gate_jackknife(sub["x"], sub["y"], sub["w"])
            loo = sorted(((corr(sub.drop(i)["x"], sub.drop(i)["y"], sub.drop(i)["w"])[0] - rw, i)
                          for i in sub.index), key=lambda t: -abs(t[0]))[0]
            cls = classify(rw, ru)
            print(f"  {c:10s}{rw:>9.3f}{f'[{lo:+.3f}, {up:+.3f}]':>20s}{pb:>9.3f}"
                  f"{g6['r_droptop']:>9.3f}{ru:>9.3f}{n:>5d}{kish(sub['w']):>7.1f}  "
                  f"{cls:<28s}{loo[1]} {loo[0]:+.3f}")
            if head == "g20_any":
                hits.append((c, rw, ru, cls))
        print()

    # -------------------------------------------------------------- verdict
    counter = [h for h in hits if h[1] <= -ALIGN and h[2] <= -ALIGN]
    print("=" * 120)
    print("E47 REGISTERED CLAIM: at least one fin34 item counter-moves g20_any at r_level <= -0.30 "
          "on BOTH lenses (2024)")
    if counter:
        print(f"  -> KEEP. Counter-moving items: "
              f"{', '.join(f'{c} ({rw:+.3f} wtd / {ru:+.3f} unwtd)' for c, rw, ru, _ in counter)}")
    else:
        print("  -> DISCARD. No qualifying item reaches -0.30 on both lenses.")
        best = min(hits, key=lambda h: h[1]) if hits else None
        if best:
            print(f"     most negative item: {best[0]} at {best[1]:+.3f} wtd / {best[2]:+.3f} unwtd "
                  f"({best[3]})")
    print("=" * 120)


if __name__ == "__main__":
    main()
