"""E41 (pre-registered): does the untouched merchant-payment margin behave like a RAIL or like the
BALANCE SHEET in 2021->2024?

B2 BREADTH CELL for this cycle: the country module `merchant_pay` — one column, reported in 2021
and 2024 only (77 / 76 developing panel economies), **zero ledger mentions**.

Parent: **E39** (the balance-sheet reframing), NOT the rails chain — E23 -> E24 -> E25 -> E35 is
already at rule B3's lineage cap.

WHY. E39 found that each margin's biggest window is a different one: account ownership 2011->14,
digital payments 2014->17, saving and borrowing 2021->24. So 2021-24 is a BALANCE-SHEET window, and
2021->24 is digital payments' WEAKEST window (21.1% of economies gained >= 10pp, against 42.1% for
saving and 52.6% for borrowing). That framing makes a sharp prediction on a margin the ledger has
never touched: `merchant_pay` is the most use-side digital margin in the country file — a payment
made to a merchant rather than a transfer or a wage — and it exists for exactly the two waves the
episode spans.

G3 DECLARATION, made honestly. `merchant_pay` is the sole column in its module and has no
headline/narrow variant, so no variant choice is being made. But the repo contains NO questionnaire
(HARNESS_V2_NOTES.md item 5), so the exact item wording — in particular whether the margin is
digital-only — is not documented. Every claim is worded about "the merchant-payment margin AS CODED
in the country file", and the item's descriptive statistics (level per wave, dispersion) are printed
so a reader can judge the coding.

TWO PRE-REGISTERED TESTS.
  P1 (E39's prediction, distributional): share of developing panel economies with
     d merchant_pay >= +10pp. BAR: < 42.1% (formal saving's share in the same window).
  P2 (the rails test, association): pop-weighted r(d merchant_pay, d fin17a_17a1_d) on the common
     sample. KEEP THRESHOLD |r| >= 0.30 + G6 sign-stability with E4 retention >= 0.5 + the B6
     inference layer (2,000-draw country bootstrap percentile interval, Kish neff, unweighted twin).
  Context, reported but NOT registered as tests: r vs d g20_any and r vs d borrow_any_t_d.

REGISTERED JOINT READING. P1 passing and P2 failing is the E39-consistent outcome. P1 failing is
evidence against E39's framing and is recorded as such. P2 passing on its own is a `keep-window`
only: `merchant_pay` has two waves, so under B4 it can NEVER be promoted to keep-general, exactly
like E29. Registered up front so a positive result is not over-read.

DECLARED. Contemporaneous co-movement over one window. Identifies nothing, is not causal, and with
two waves cannot be a general regularity under B4 whatever it returns.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 41
BIG_MOVE = 10.0
P1_BAR = 42.1          # formal saving's share of economies >= +10pp in 2021->24 (E39)
P2_BAR = 0.30
WINDOW = (2021, 2024)

MP = "merchant_pay"
SAV = "fin17a_17a1_d"
G20 = "g20_any"
BOR = "borrow_any_t_d"
ACC = "account_t_d"


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _ucorr(x, y):
    m = pd.notna(x) & pd.notna(y)
    return float(np.corrcoef(x[m], y[m])[0, 1]) if m.sum() >= 10 else np.nan


def delta(fx, col):
    t0, t1 = WINDOW
    w = fx.country_panel(fx.pan_dev, col, [t0, t1])
    if t0 not in w.columns or t1 not in w.columns:
        return pd.DataFrame(columns=["l0", "l1", "d", "pop"])
    return pd.DataFrame({"l0": w[t0], "l1": w[t1], "d": w[t1] - w[t0], "pop": w["pop"]}).dropna()


def boot_r(fx, df, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx, out = np.arange(len(df)), []
    for _ in range(draws):
        d = df.iloc[rng.choice(idx, size=len(idx), replace=True)]
        r, _n = fx.weighted_corr(d["dx"], d["dy"], d["pop"])
        if pd.notna(r):
            out.append(r)
    a = np.asarray(out)
    tail = min((a <= 0).mean(), (a >= 0).mean())
    return (float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5)),
            float(max(2.0 * tail, 1.0 / draws)))


def pair(fx, dmp, other_col):
    d2 = delta(fx, other_col)
    return pd.DataFrame({"dx": dmp["d"], "dy": d2["d"], "pop": dmp["pop"]}).dropna(
        ).reset_index(drop=True)


def assoc(fx, df, label):
    r, n = fx.weighted_corr(df["dx"], df["dy"], df["pop"])
    ru = _ucorr(df["dx"], df["dy"])
    lo, hi, p = boot_r(fx, df)
    g6 = fx.gate_jackknife(df["dx"], df["dy"], df["pop"])
    rd = g6.get("r_droptop")
    ret = abs(rd) / abs(r) if (rd is not None and pd.notna(rd) and abs(r) > 1e-9) else np.nan
    print(f"  {label:44s} r_w={r:+.3f}  r_u={ru:+.3f}  n={n:3d}  neff={_kish(df['pop']):4.1f}  "
          f"CI[{lo:+.3f},{hi:+.3f}]  p_boot={p:.4f}  G6={rd:+.3f} (ret {ret:.2f})")
    return {"r": r, "ru": ru, "n": n, "neff": _kish(df["pop"]), "lo": lo, "hi": hi,
            "p": p, "r_droptop": rd, "ret": ret, "g6_ok": g6["ok"]}


def run(fx: Findex):
    print("=" * 108)
    print("E41 — the untouched `merchant_pay` margin: rail or balance sheet? (2021->2024, pan_dev)")
    print("=" * 108)

    mp = delta(fx, MP)
    t0, t1 = WINDOW

    # ---- G3/G4: what this column actually looks like, printed before any test is read ---------
    print(f"\nTHE COLUMN (G3 — sole member of its module, no variant; wording undocumented)")
    print(f"  n economies with both waves: {len(mp)}")
    print(f"  {t0} level: pop-weighted {np.average(mp['l0'], weights=mp['pop']):5.1f}pp   "
          f"unweighted mean {mp['l0'].mean():5.1f}pp   median {mp['l0'].median():5.1f}pp   "
          f"range {mp['l0'].min():.1f}-{mp['l0'].max():.1f}")
    print(f"  {t1} level: pop-weighted {np.average(mp['l1'], weights=mp['pop']):5.1f}pp   "
          f"unweighted mean {mp['l1'].mean():5.1f}pp   median {mp['l1'].median():5.1f}pp   "
          f"range {mp['l1'].min():.1f}-{mp['l1'].max():.1f}")
    cov = fx.gate_coverage(fx.pan_dev, MP, 2024)
    print(f"  G4: {cov['n_countries']} economies, population share {cov['pop_share']:.3f} "
          f"-> {'ok' if cov['ok'] else 'FAIL'}")

    # ---- P1: the distributional test --------------------------------------------------------
    share = float((mp["d"] >= BIG_MOVE).mean()) * 100
    se = np.sqrt((share / 100) * (1 - share / 100) / len(mp)) * 100
    print("\n" + "-" * 108)
    print("P1 — share of developing panel economies gaining >= +10pp, 2021->2024 "
          "(E39's table, with merchant_pay inserted)")
    print("-" * 108)
    print(f"  {'margin':22s} {'share >=+10pp':>14s} {'median d':>10s} {'mean d (unw)':>13s} "
          f"{'mean d (wtd)':>13s} {'n':>4s}")
    ref = {}
    for name, col in [("merchant payments", MP), ("formal saving", SAV), ("any borrowing", BOR),
                      ("digital payments", G20), ("account ownership", ACC)]:
        d = delta(fx, col)
        s = float((d["d"] >= BIG_MOVE).mean()) * 100
        ref[name] = s
        print(f"  {name:22s} {s:13.1f}% {d['d'].median():10.2f} {d['d'].mean():13.2f} "
              f"{np.average(d['d'], weights=d['pop']):13.2f} {len(d):4d}")
    p1_pass = share < P1_BAR
    print(f"\n  P1: merchant payments {share:.1f}% (+-{1.96*se:.1f} binomial 95%) vs bar "
          f"< {P1_BAR}%  ->  {'PASS' if p1_pass else 'FAIL'}")

    # ---- P2: the registered association -----------------------------------------------------
    print("\n" + "-" * 108)
    print("P2 — registered association, plus the two context cells (B6 inference on all three)")
    print("-" * 108)
    p2 = assoc(fx, pair(fx, mp, SAV), "REGISTERED  d merchant_pay ~ d formal saving")
    ctx_g20 = assoc(fx, pair(fx, mp, G20), "context     d merchant_pay ~ d digital payments")
    ctx_bor = assoc(fx, pair(fx, mp, BOR), "context     d merchant_pay ~ d any borrowing")

    p2_pass = (abs(p2["r"]) >= P2_BAR) and p2["g6_ok"] and (p2["ret"] >= 0.5)
    print(f"\n  P2: |r| = {abs(p2['r']):.3f} vs bar {P2_BAR}; G6 sign-stable "
          f"{p2['g6_ok']}; E4 retention {p2['ret']:.2f} vs 0.5  ->  "
          f"{'PASS' if p2_pass else 'FAIL'}")

    print("\n" + "=" * 108)
    print("VERDICT INPUTS")
    print("=" * 108)
    print(f"  P1 (E39's balance-sheet prediction)  {'PASS' if p1_pass else 'FAIL'}")
    print(f"  P2 (merchant payments as a rail)     {'PASS' if p2_pass else 'FAIL'}")
    print("  Registered joint reading: P1 pass + P2 fail = the E39-consistent outcome "
          "(a rail that was not moving).")
    print("  B4: two waves only — merchant_pay can never reach keep-general, whatever P2 returns.")
    return {"share": share, "p1": p1_pass, "p2": p2_pass, "assoc": p2,
            "ctx_g20": ctx_g20, "ctx_bor": ctx_bor}


if __name__ == "__main__":
    run(Findex())
