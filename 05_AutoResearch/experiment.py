"""E38 (pre-registered): does the E5b "accounts-first" pattern replicate on earlier transitions?

Program 1 (the replication debt), agenda item 6.5. Parent: E5b (`keep-window`) — one of the three
remaining unreplicated keeps, with E7 and E22.

WHAT E5b CLAIMED. Usage intensity at t = g20_any(t) / account_t_d(t) — what share of an economy's
accountholders actually pay digitally. E5b partialled that ratio against subsequent account growth,
holding the account LEVEL at t fixed (pop-weighted LS residualization), and found
**r_partial = -0.595 (n=77) on 2021->2024** against a convergence benchmark of -0.301: at the same
account level, economies whose existing accounts were LESS used grew accounts FASTER. Hence
"accounts first" — breadth runs ahead of depth.

TEST, per the pre-registration: the identical construction on **2014->2017** and **2017->2021**,
with **2021->2024 recomputed inside this file** (the rule adopted from E35, where recomputing the
original window is what caught a weight-join defect before any verdict was read).

PROMOTION THRESHOLD. E5b promotes keep-window -> keep-general only if at least one earlier
transition gives r_partial <= -0.30 with the same sign AND the drop-top-5 jackknife keeps that sign.
Otherwise E5b stays keep-window and is recorded as having FAILED its promotion test.

REGISTERED SECONDARY VERDICT, declared up front because it is uncomfortable. E5b's ORIGINAL window
already fails the E4 magnitude rule as now written (jackknife retention 0.19: -0.595 -> -0.114) and
that rule post-dates the finding. If the earlier windows also collapse under the jackknife,
**recommend demoting E5b to `discard`**, as E32 recommended for E7.

Gates: G4 · G6 drop-top-5 · B6 country bootstrap (2,000 draws, percentile interval) + Kish neff,
per window. Registered note on power: 2014->2017 has failed to produce a stable sign in five of six
cells across E28 and E30, so a null there is weak evidence of absence; 2017->2021 decides it.

DECLARED. Descriptive temporal ordering; a ratio measured before a change is not identification.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 38
PROMOTE_BAR = -0.30
TRANSITIONS = [(2014, 2017), (2017, 2021), (2021, 2024)]
ORIGINAL = (2021, 2024)
E5B_ORIGINAL_PARTIAL = -0.595   # value on record in findings.tsv, for the reproduction check


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def _wcorr(x, y, w):
    x, y, w = (np.asarray(v, float) for v in (x, y, w))
    m = ~(np.isnan(x) | np.isnan(y) | np.isnan(w))
    x, y, w = x[m], y[m], w[m]
    if len(x) < 10:
        return np.nan, len(x)
    mx, my = np.average(x, weights=w), np.average(y, weights=w)
    sx = np.sqrt(np.average((x - mx) ** 2, weights=w))
    sy = np.sqrt(np.average((y - my) ** 2, weights=w))
    if sx == 0 or sy == 0:
        return np.nan, len(x)
    return float(np.average((x - mx) * (y - my), weights=w) / (sx * sy)), len(x)


def _wresid(y, z, w):
    """Pop-weighted LS residual of y on z with intercept (the E5b construction)."""
    y, z, w = (np.asarray(v, float) for v in (y, z, w))
    mz, my = np.average(z, weights=w), np.average(y, weights=w)
    var = np.average((z - mz) ** 2, weights=w)
    b = 0.0 if var == 0 else np.average((z - mz) * (y - my), weights=w) / var
    return y - (my + b * (z - mz))


def build(fx: Findex, t0, t1):
    """One transition: usage-intensity ratio at t0, account level at t0, account change t0->t1."""
    acc = fx.country_panel(fx.pan_dev, "account_t_d", [t0, t1])
    g20 = fx.country_panel(fx.pan_dev, "g20_any", [t0])
    df = pd.DataFrame({
        "acc_t0": acc[t0],
        "d_acc": acc[t1] - acc[t0],
        "g20_t0": g20[t0],
        "pop": acc["pop"],
    }).dropna()
    df = df[df["acc_t0"] > 0]
    df["ratio"] = df["g20_t0"] / df["acc_t0"]      # usage intensity: users per accountholder
    return df.reset_index().rename(columns={"countrynewwb": "country"})


def stats(df):
    df = df.reset_index(drop=True)
    w = df["pop"]
    raw, n = _wcorr(df["ratio"], df["d_acc"], w)
    bench, _ = _wcorr(df["acc_t0"], df["d_acc"], w)     # the convergence benchmark (E17: -0.301)
    rx = _wresid(df["ratio"], df["acc_t0"], w)
    ry = _wresid(df["d_acc"], df["acc_t0"], w)
    part, _ = _wcorr(rx, ry, w)
    return {"r": raw, "partial": part, "bench": bench, "n": n, "neff": _kish(w)}


def drop_top(df, k=5):
    top = df.nlargest(k, "pop")["country"]
    return df[~df["country"].isin(top)]


def bootstrap(df, rng, draws=BOOT):
    out_r, out_p = [], []
    idx = np.arange(len(df))
    for _ in range(draws):
        s = df.iloc[rng.choice(idx, size=len(idx), replace=True)]
        st = stats(s)
        if pd.notna(st["partial"]):
            out_r.append(st["r"])
            out_p.append(st["partial"])
    return np.array(out_r), np.array(out_p)


def run(fx: Findex):
    rng = np.random.default_rng(SEED)
    print("=" * 92)
    print("E38 — E5b REPLICATION: usage intensity at t -> subsequent account growth, at the same")
    print("      account level. Promotion needs an earlier window with r_partial <= -0.30, sign-stable.")
    print("=" * 92)

    rows = []
    for t0, t1 in TRANSITIONS:
        df = build(fx, t0, t1)
        st = stats(df)
        st_dt = stats(drop_top(df))
        br, bp = bootstrap(df, rng)
        lo, hi = np.percentile(bp, [2.5, 97.5])
        p_boot = 2 * min((bp <= 0).mean(), (bp >= 0).mean())
        ret = abs(st_dt["partial"]) / abs(st["partial"]) if st["partial"] else np.nan
        tag = "  [ORIGINAL WINDOW]" if (t0, t1) == ORIGINAL else ""
        print("-" * 92)
        print(f"{t0}->{t1}{tag}   n={st['n']}   Kish neff={st['neff']:.1f}")
        print(f"  raw r(ratio, d_account)          = {st['r']:+.3f}")
        print(f"  PRIMARY partial | account level  = {st['partial']:+.3f}   "
              f"95% CI [{lo:+.3f}, {hi:+.3f}]   p_boot={p_boot:.3f}")
        print(f"  convergence benchmark r(acc,d)   = {st['bench']:+.3f}")
        print(f"  G6 drop-top-5: partial = {st_dt['partial']:+.3f}  (retention {ret:.2f}, "
              f"n={st_dt['n']}, neff={st_dt['neff']:.1f})")
        print(f"  mean usage intensity at t0 = {np.average(df['ratio'], weights=df['pop']):.3f} "
              f"| pop-weighted mean d_account = {np.average(df['d_acc'], weights=df['pop']):+.2f}pp")
        rows.append({"span": f"{t0}->{t1}", "n": st["n"], "neff": round(st["neff"], 1),
                     "r_raw": st["r"], "partial": st["partial"], "ci_lo": lo, "ci_hi": hi,
                     "p_boot": p_boot, "bench": st["bench"],
                     "partial_droptop": st_dt["partial"], "retention": ret})

    tbl = pd.DataFrame(rows)
    print("=" * 92)
    print(tbl.to_string(index=False))

    # reproduction check on the original window (the E35 convention)
    orig = tbl[tbl["span"] == f"{ORIGINAL[0]}->{ORIGINAL[1]}"].iloc[0]
    dev = abs(orig["partial"] - E5B_ORIGINAL_PARTIAL)
    print(f"\nREPRODUCTION CHECK: this file gives {orig['partial']:+.3f} on {orig['span']} against "
          f"{E5B_ORIGINAL_PARTIAL:+.3f} on record — deviation {dev:.3f} "
          f"({'reproduces' if dev <= 0.02 else 'DOES NOT REPRODUCE'})")

    earlier = tbl[tbl["span"] != f"{ORIGINAL[0]}->{ORIGINAL[1]}"]
    promote = bool(((earlier["partial"] <= PROMOTE_BAR)
                    & (np.sign(earlier["partial_droptop"]) == np.sign(earlier["partial"]))).any())
    print(f"\nPROMOTION (needs an earlier window with partial <= {PROMOTE_BAR:+.2f} AND "
          f"sign-stable under G6): {'YES -> keep-general' if promote else 'NO -> stays keep-window, FAILED'}")
    collapse = bool((earlier["retention"].fillna(0) < 0.5).all()
                    and orig["retention"] < 0.5)
    print(f"REGISTERED SECONDARY VERDICT (all windows collapse under the jackknife -> recommend "
          f"demoting E5b to discard): {collapse}")
    print("=" * 92)
    return tbl


if __name__ == "__main__":
    run(Findex())
