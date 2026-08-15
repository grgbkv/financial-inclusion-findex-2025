"""E46 (pre-registered 2026-08-15b): is the 2014->2017 fall in `save_any_t_d` (53.1 -> 43.6) a
DEFINITIONAL BREAK in the instrument or a real behavioural decline?

Agenda items 1.4 and 1.7. Parent: E39 / E44 item 1.7 (formal saving declines in EVERY demographic
slice in 2014->17, the slice-level counterpart of this drop). Two agenda items and any decade-scale
claim on the saving margin are blocked on this question.

This is a MEASUREMENT question, not an association: no 0.30 threshold applies. The pre-registered
object is a verdict rule over five diagnostics, fixed before any of them was computed.

  (a) UNIVERSALITY   share of dev-panel economies with delta save_any < 0 in 2014->17 vs the other
                     windows. BAR: >= 80% falling AND >= 20pp above the highest other window.
  (b) HIGH-INCOME    the same share on the HIGH-INCOME panel frame (pan_all minus pan_dev, ~40
      CONTAMINATION  economies) — a frame with zero ledger mentions. BAR: >= 70% also falling.
  (c) COMPONENT      decompose delta save_any into delta formal (fin17a_17a1_d) and the RESIDUAL
      DECOUPLING     (total minus formal). BAR: >= 70% of the pp drop sits in the residual.
  (d) PERSISTENCE    2017 / 2021 / 2024 levels. BAR: never returns within 5pp of 2014. Reported for
                     every verdict; does NOT enter the rule (a real decline can persist too).
  (e) G5 OFFICIAL    the official Developing-economies aggregate must show the same drop within
                     2.5pp. A computation check: if it FAILS the experiment is VOID.

  VERDICT RULE (fixed in advance):
    definitional-break consistent  if (a) AND (b) AND (c) pass, and (e) holds
    real decline                   if (a) passes but BOTH (b) and (c) fail
    inconclusive                   otherwise

B6/B9/B10: 2,000-draw country bootstrap on each share; Kish neff beside every nominal n and no
significance language on nominal n; unweighted median delta beside the population-weighted mean.

E35 RULE: the file recomputes the ledger's published 2014/2017 levels (53.1 / 43.6) BEFORE any
diagnostic is read, and aborts on a mismatch > 0.2pp.

DECLARED. `save_any_t_d` and `fin17a_17a1_d` are headline variants under G3. Descriptive measurement
diagnostics only, nothing causal. "Definitional break" is a claim about the INSTRUMENT, offered as
the reading most consistent with the signatures — the repo holds no questionnaire
(HARNESS_V2_NOTES.md items 5 and 6), so it can never be a documented fact here.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 46
WAVES = [2014, 2017, 2021, 2024]
TOTAL = "save_any_t_d"
FORMAL = "fin17a_17a1_d"

BAR_A_SHARE = 0.80      # (a) share of dev economies falling in 2014->17
BAR_A_MARGIN = 20.0     # (a) pp above the highest other window
BAR_B_SHARE = 0.70      # (b) share of high-income economies falling
BAR_C_RESID = 0.70      # (c) fraction of the drop sitting in the residual
BAR_D_RETURN = 5.0      # (d) pp of 2014 the series must never return within

LEDGER_2014, LEDGER_2017 = 53.1, 43.6


def kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def boot_share(vals, draws=BOOT, seed=SEED):
    """Percentile interval for the share of economies below zero, resampling economies."""
    a = np.asarray(vals, dtype=float)
    a = a[np.isfinite(a)]
    if len(a) < 10:
        return np.nan, np.nan
    rng = np.random.default_rng(seed)
    sh = [(a[rng.integers(0, len(a), len(a))] < 0).mean() for _ in range(draws)]
    return float(np.percentile(sh, 2.5)), float(np.percentile(sh, 97.5))


def panel(frame, col):
    w = frame[frame["year"].isin(WAVES)].pivot_table(
        index="countrynewwb", columns="year", values=col) * 100
    pop = frame[frame["year"] == 2024].set_index("countrynewwb")["pop_adult"]
    w["pop"] = pop.reindex(w.index)
    return w


def wmean(s, w):
    m = pd.notna(s) & pd.notna(w)
    return float(np.average(s[m], weights=w[m])) if m.sum() else np.nan


def main():
    fx = Findex()
    dev = fx.pan_dev
    hi = fx.pan_all[fx.pan_all["incomegroupwb24"] == "High income"].copy()

    print("=" * 108)
    print("E46 — the 2014->2017 saving drop: definitional break or real decline?")
    print("=" * 108)

    # ---------------------------------------------------------------- E35 rule
    tot_dev = fx.series(dev, TOTAL, WAVES)
    d14, d17 = tot_dev[2014], tot_dev[2017]
    print(f"\nE35 RULE — reproduce the ledger before reading anything: "
          f"2014 {d14:.1f} (ledger {LEDGER_2014}) | 2017 {d17:.1f} (ledger {LEDGER_2017})")
    for got, want, lab in ((d14, LEDGER_2014, "2014"), (d17, LEDGER_2017, "2017")):
        assert abs(got - want) <= 0.2, f"ABORT: {lab} is {got:.2f}, ledger says {want}"
    print("  reproduced within 0.2pp — proceeding.")

    # ------------------------------------------------------- (e) G5, run first
    print("\n" + "-" * 108)
    print("(e) G5 OFFICIAL CROSS-CHECK — a computation check; failure VOIDS the experiment")
    print("-" * 108)
    g5 = fx.gate_official(tot_dev, "developing", TOTAL)
    off = fx.official_series("developing", TOTAL, WAVES)
    print(f"  computed (dev panel): " + "  ".join(f"{y}={tot_dev[y]:.1f}" for y in tot_dev.index))
    print(f"  official  (Developing economies): " +
          "  ".join(f"{y}={off[y]:.1f}" for y in off.index))
    print(f"  {g5}")
    if not g5["ok"]:
        print("\n  *** VOID: computed aggregate does not track the official one. ***")
        return

    # ------------------------------------------------------------ (d) levels
    print("\n" + "-" * 108)
    print("(d) PERSISTENCE — dev-panel population-weighted levels, all four waves")
    print("-" * 108)
    fml_dev = fx.series(dev, FORMAL, WAVES)
    tot_hi = fx.series(hi, TOTAL, WAVES)
    print(f"  {'series':34s}" + "".join(f"{y:>10d}" for y in WAVES))
    for lab, s in (("save_any_t_d (developing)", tot_dev),
                   ("fin17a_17a1_d formal (developing)", fml_dev),
                   ("save_any_t_d (HIGH INCOME)", tot_hi)):
        print(f"  {lab:34s}" + "".join(
            f"{s[y]:>10.1f}" if y in s.index else f"{'—':>10s}" for y in WAVES))
    later = [tot_dev[y] for y in (2017, 2021, 2024) if y in tot_dev.index]
    closest = min(abs(v - d14) for v in later)
    d_pass = closest > BAR_D_RETURN
    print(f"\n  closest later wave to the 2014 level: {closest:.1f}pp away "
          f"(bar: never within {BAR_D_RETURN}pp) -> "
          f"{'PASS (level shift persists)' if d_pass else 'FAIL (series recovers)'}")

    # -------------------------------------------------- (a) and (b) shares
    ptot_dev, ptot_hi = panel(dev, TOTAL), panel(hi, TOTAL)
    windows = [(2014, 2017), (2017, 2021), (2021, 2024)]

    def share_table(p, label):
        rows = []
        for a, b in windows:
            if a not in p.columns or b not in p.columns:
                continue
            d = (p[b] - p[a]).dropna()
            w = p["pop"].reindex(d.index)
            lo, up = boot_share(d.values)
            rows.append({
                "window": f"{a}->{b}", "n": len(d), "neff": kish(w.dropna()),
                "share_neg": float((d < 0).mean()), "ci": (lo, up),
                "wmean": wmean(d, w), "umedian": float(d.median()),
            })
        print(f"\n  {label}")
        print(f"    {'window':12s}{'n':>5s}{'neff':>7s}{'% falling':>11s}"
              f"{'[95% CI]':>20s}{'wtd mean d':>12s}{'unwtd med d':>13s}")
        for r in rows:
            ci = f"[{r['ci'][0]*100:.1f}, {r['ci'][1]*100:.1f}]"
            print(f"    {r['window']:12s}{r['n']:>5d}{r['neff']:>7.1f}"
                  f"{r['share_neg']*100:>10.1f}%{ci:>20s}"
                  f"{r['wmean']:>12.2f}{r['umedian']:>13.2f}")
        return {r["window"]: r for r in rows}

    print("\n" + "-" * 108)
    print("(a) UNIVERSALITY / (b) HIGH-INCOME CONTAMINATION — share of economies with a FALLING "
          "total-saving rate")
    print("-" * 108)
    sd = share_table(ptot_dev, "developing panel (77 economies)")
    sh = share_table(ptot_hi, "HIGH-INCOME panel (frame with zero prior ledger mentions)")

    a_share = sd["2014->2017"]["share_neg"]
    other_max = max(sd[k]["share_neg"] for k in sd if k != "2014->2017")
    a_pass = a_share >= BAR_A_SHARE and (a_share - other_max) * 100 >= BAR_A_MARGIN
    print(f"\n  (a) 2014->17 {a_share*100:.1f}% vs best other window {other_max*100:.1f}% "
          f"(margin {(a_share-other_max)*100:.1f}pp; bars {BAR_A_SHARE*100:.0f}% and "
          f"{BAR_A_MARGIN:.0f}pp) -> {'PASS' if a_pass else 'FAIL'}")

    b_share = sh["2014->2017"]["share_neg"]
    b_pass = b_share >= BAR_B_SHARE
    print(f"  (b) high income 2014->17 {b_share*100:.1f}% falling "
          f"(bar {BAR_B_SHARE*100:.0f}%) -> {'PASS' if b_pass else 'FAIL'}")

    # ------------------------------------------------ (c) component decoupling
    print("\n" + "-" * 108)
    print("(c) COMPONENT DECOUPLING — where does the drop sit: formal saving, or the "
          "non-formal residual?")
    print("-" * 108)
    pf = panel(dev, FORMAL)
    common = ptot_dev.index.intersection(pf.index)
    tt, ff = ptot_dev.loc[common], pf.loc[common]
    print(f"  {'window':12s}{'d total':>10s}{'d formal':>11s}{'d residual':>12s}"
          f"{'resid share':>13s}{'n':>6s}{'neff':>7s}")
    c_pass = None
    for a, b in windows:
        m = pd.notna(tt[a]) & pd.notna(tt[b]) & pd.notna(ff[a]) & pd.notna(ff[b])
        w = tt.loc[m, "pop"]
        dt = wmean(tt.loc[m, b] - tt.loc[m, a], w)
        df_ = wmean(ff.loc[m, b] - ff.loc[m, a], w)
        dr = dt - df_
        rs = dr / dt if dt != 0 else np.nan
        print(f"  {a}->{b:<7d}{dt:>10.2f}{df_:>11.2f}{dr:>12.2f}{rs*100:>12.1f}%"
              f"{int(m.sum()):>6d}{kish(w.dropna()):>7.1f}")
        if (a, b) == (2014, 2017):
            c_pass = bool(dt < 0 and rs >= BAR_C_RESID)
            c_resid_share = rs
    print(f"\n  (c) residual carries {c_resid_share*100:.1f}% of the 2014->17 drop "
          f"(bar {BAR_C_RESID*100:.0f}%) -> {'PASS' if c_pass else 'FAIL'}")

    # per-economy version of (c): does formal saving fall in the same economies?
    m = pd.notna(tt[2014]) & pd.notna(tt[2017]) & pd.notna(ff[2014]) & pd.notna(ff[2017])
    dtot = (tt.loc[m, 2017] - tt.loc[m, 2014])
    dfml = (ff.loc[m, 2017] - ff.loc[m, 2014])
    dres = dtot - dfml
    print(f"  per-economy 2014->17: total falls in {(dtot<0).mean()*100:.1f}% of economies, "
          f"formal in {(dfml<0).mean()*100:.1f}%, residual in {(dres<0).mean()*100:.1f}% "
          f"(n={int(m.sum())})")

    # ---------------------------------------------------------------- verdict
    print("\n" + "=" * 108)
    if a_pass and b_pass and c_pass:
        verdict = "DEFINITIONAL-BREAK CONSISTENT"
    elif a_pass and not b_pass and not c_pass:
        verdict = "REAL DECLINE"
    else:
        verdict = "INCONCLUSIVE"
    print(f"E46 VERDICT: {verdict}")
    print(f"  (a) universality        {'PASS' if a_pass else 'FAIL'}")
    print(f"  (b) high-income contam. {'PASS' if b_pass else 'FAIL'}")
    print(f"  (c) component decoupling{'PASS' if c_pass else 'FAIL'}")
    print(f"  (d) persistence         {'PASS' if d_pass else 'FAIL'}   (reported, not in the rule)")
    print(f"  (e) G5 official         PASS")
    print("=" * 108)


if __name__ == "__main__":
    main()
