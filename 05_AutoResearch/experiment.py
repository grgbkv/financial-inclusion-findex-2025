"""E33 (pre-registered): do the digitalization rails reach a SECOND welfare margin (`fh`), 2021->24?

Program 4 — the welfare margin reopened (agenda items 4.1, 4.2, 4.4). Parent: **E26**, which found
the three rails miss the welfare margin at the registered bar (wage digitalization r = +0.294 vs a
0.30 threshold) on a SINGLE self-reported measure, `fin24aSD_ND`. Item 4.2 asks whether that null is
a measure artifact or a real boundary. First descendant of E26, so rule B3's lineage cap is not
engaged.

B2 BREADTH CELL: the `fh` family (`fh1`, `fh2`, `fh2a`, `fh1_fh2`) — an UNTOUCHED country module,
zero ledger mentions, one of the thirteen untouched families in the coverage audit. 2021 AND 2024
coverage on ~74/71 developing economies, so it carries a usable delta.

G3 DECLARATION. The harness INDICATORS registry does not cover `fh`, so `gate_variant` returns
UNREGISTERED by construction — disclosed, not evaded. Declared instead: `fh1` and `fh2` are the
PRIMARY items, `fh1_fh2` the declared composite, `fh2a` EXCLUDED (2024 only, no delta).

POLARITY CLAUSE. The country file is unlabelled, so whether a higher `fh1`/`fh2` means better or
worse financial health is NOT known at registration time. The pre-registered quantity is therefore
the MAGNITUDE and SIGN-CONSISTENCY of the co-movement, not its welfare direction: the sign must be
consistent across all three rails for a given item, and consistent across `fh1` and `fh2`. The
welfare READING of that sign is declared in advance to be an interpretive step that is NOT
pre-registered; it is labelled as such in the verdict and anchored by reporting the pop-weighted
2021 and 2024 levels of each item beside the correlations.

KEEP THRESHOLD. At least one of fh1/fh2/fh1_fh2 reaches |r| >= 0.30 against at least TWO of the
three rails, with the same sign on all three rails and the same sign for fh1 and fh2; AND G4 passes;
AND G6 is sign-stable on every counting cell; AND the E4 judgment rule holds on those cells
(|r_droptop| >= 0.5 |r_full|).

B6: country bootstrap 2,000 draws, percentile 95% interval on every primary correlation; Kish neff
beside the nominal n everywhere.

B4: any keep here is 2021->2024 only and is STRUCTURALLY UNPROMOTABLE (`fh` has no pre-2021 wave),
exactly as E29 is. Logged `keep-window` and declared so now.

DECLARED. Descriptive co-movement of contemporaneous changes. Identifies nothing. The registered
comparison is E26's +0.294 on `fin24aSD_ND`.
"""
import numpy as np
import pandas as pd

from harness import Findex

BOOT = 2000
SEED = 33
BAR = 0.30
WINDOW = (2021, 2024)

FH_PRIMARY = ["fh1", "fh2", "fh1_fh2"]      # fh2a excluded: 2024 only, no delta
RAILS = {                                    # E26's three rails, same columns
    "wage (fin32_acc)":        "fin32_acc",
    "digital pay (g20_any)":   "g20_any",
    "mobile money (mobileacc)": "mobileaccount_t_d",
}
SECONDARY = {
    "A 4.4 saving surge (fin17a_17a1_d)": "fin17a_17a1_d",
    "B 4.2 resilience (fin24aSD_ND)":     "fin24aSD_ND",
}


def _kish(w):
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def delta_frame(fx: Findex, xcol, ycol):
    y0, y1 = WINDOW
    wx = fx.country_panel(fx.pan_dev, xcol, [y0, y1])
    wy = fx.country_panel(fx.pan_dev, ycol, [y0, y1])
    return pd.DataFrame({"dx": wx[y1] - wx[y0],
                         "dy": wy[y1] - wy[y0],
                         "pop": wx["pop"]}).dropna()


def _boot_ci(fx: Findex, df, draws=BOOT, seed=SEED):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(df))
    out = []
    for _ in range(draws):
        d = df.iloc[rng.choice(idx, size=len(idx), replace=True)]
        r, _n = fx.weighted_corr(d["dx"], d["dy"], d["pop"])
        if pd.notna(r):
            out.append(r)
    if len(out) < draws * 0.9:
        return None, None
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def _terciles(df):
    """Mean dy (pop-weighted) within terciles of dx — ledger convention."""
    if len(df) < 9:
        return None
    t = pd.qcut(df["dx"], 3, labels=["low", "mid", "high"])
    return [float(np.average(g["dy"], weights=g["pop"])) for _, g in df.groupby(t, observed=True)]


def cell(fx: Findex, fh, rail_name, rail_col, show_terciles=True):
    df = delta_frame(fx, rail_col, fh)
    if len(df) < 10:
        print(f"    {rail_name:28s} insufficient coverage (n={len(df)})")
        return None
    r, n = fx.weighted_corr(df["dx"], df["dy"], df["pop"])
    g6 = fx.gate_jackknife(df["dx"], df["dy"], df["pop"])
    lo, hi = _boot_ci(fx, df)
    rd = g6.get("r_droptop")
    ret = abs(rd) / abs(r) if (rd is not None and abs(r) > 1e-9) else np.nan
    ci = f"[{lo:+.3f},{hi:+.3f}]" if lo is not None else "n/a"
    ter = _terciles(df) if show_terciles else None
    ters = ("  terciles " + "/".join(f"{v:+.1f}" for v in ter)) if ter else ""
    print(f"    {rail_name:28s} r={r:+.3f}  n={n:3d}  neff={_kish(df['pop']):4.1f}  "
          f"CI95 {ci:>18s}  G6 {'ok ' if g6['ok'] else 'FAIL'} r_drop={rd:+.3f} "
          f"ret={ret:.2f}{ters}")
    return {"fh": fh, "rail": rail_name, "r": r, "n": n, "neff": _kish(df["pop"]),
            "ci": (lo, hi), "g6_ok": bool(g6["ok"]), "r_droptop": rd, "ret": ret}


def run(fx: Findex):
    y0, y1 = WINDOW
    print("=" * 104)
    print("E33 — do the digitalization rails reach the `fh` financial-health margin? "
          f"({y0}->{y1}, pan_dev)")
    print("=" * 104)

    # ---- G3 disclosure + polarity anchor (levels; the welfare reading is NOT pre-registered) --
    print("\nG3 (declared): harness INDICATORS does not cover the `fh` family — "
          f"gate_variant('resilience','fh1') -> {fx.gate_variant('resilience', 'fh1')['role']}")
    print("\nPOLARITY ANCHOR — pop-weighted developing-panel LEVELS (pp), interpretive only:")
    for col in FH_PRIMARY + ["fh2a"]:
        s = fx.series(fx.pan_dev, col, years=[2021, 2024])
        cov = {y: fx.gate_coverage(fx.pan_dev, col, y) for y in (2021, 2024)}
        lv = "  ".join(f"{y}={s[y]:5.1f}" for y in s.index)
        print(f"  {col:9s} {lv:24s}  "
              f"n_countries 2021={cov[2021]['n_countries']:3d} 2024={cov[2024]['n_countries']:3d}  "
              f"pop share 2024={cov[2024]['pop_share']:.2f}"
              + ("   [EXCLUDED from the primary: single wave]" if col == "fh2a" else ""))

    # ---- PRIMARY (4.1) -----------------------------------------------------------------------
    print("\n" + "-" * 104)
    print("PRIMARY (4.1) — d(fh) ~ d(rail), E26's construction with the destination swapped")
    print("-" * 104)
    results = []
    for fh in FH_PRIMARY:
        print(f"  {fh}:")
        for rn, rc in RAILS.items():
            out = cell(fx, fh, rn, rc)
            if out:
                results.append(out)

    res = pd.DataFrame(results)

    # ---- SECONDARY ---------------------------------------------------------------------------
    print("\n" + "-" * 104)
    print("SECONDARY — A (4.4) does fh track the saving surge?  B (4.2) do the two welfare "
          "measures agree?")
    print("-" * 104)
    sec = []
    for fh in FH_PRIMARY:
        print(f"  {fh}:")
        for sn, sc in SECONDARY.items():
            out = cell(fx, fh, sn, sc, show_terciles=False)
            if out:
                sec.append(out)
    sec = pd.DataFrame(sec)

    # ---- pre-registered threshold ------------------------------------------------------------
    print("\n" + "=" * 104)
    print("PRE-REGISTERED THRESHOLD")
    print("=" * 104)
    kept_any = False
    for fh in FH_PRIMARY:
        sub = res[res["fh"] == fh]
        if sub.empty:
            continue
        n_bar = int((sub["r"].abs() >= BAR).sum())
        signs = set(np.sign(sub["r"]))
        sign_consistent = len(signs) == 1
        counting = sub[sub["r"].abs() >= BAR]
        g6_ok = bool(counting["g6_ok"].all()) if len(counting) else False
        e4_ok = bool((counting["ret"] >= 0.5).all()) if len(counting) else False
        print(f"  {fh:9s} |r|>=0.30 on {n_bar}/3 rails (bar 2)  "
              f"sign-consistent across rails: {sign_consistent}  "
              f"G6 on counting cells: {g6_ok}  E4 retention>=0.5: {e4_ok}")
        if n_bar >= 2 and sign_consistent and g6_ok and e4_ok:
            kept_any = True

    # cross-item sign consistency between fh1 and fh2 (required by the pre-registration)
    s1 = res[res["fh"] == "fh1"]["r"]
    s2 = res[res["fh"] == "fh2"]["r"]
    cross_ok = (len(s1) and len(s2)
                and len(set(np.sign(s1)) | set(np.sign(s2))) == 1)
    print(f"\n  Cross-item sign consistency (fh1 and fh2 same sign on all rails): {bool(cross_ok)}")
    verdict = "KEEP (keep-window, structurally unpromotable)" if (kept_any and cross_ok) \
        else "DISCARD"
    print(f"\n  VERDICT: {verdict}")

    print(f"\n  Registered comparison — E26 on `fin24aSD_ND`: wage +0.294, g20 +0.000, mm +0.208")
    best = res.loc[res["r"].abs().idxmax()] if len(res) else None
    if best is not None:
        print(f"  Strongest primary cell here: {best['fh']} ~ {best['rail']} "
              f"r={best['r']:+.3f} (n={best['n']}, neff={best['neff']:.1f})")
    print(f"  Kish neff across primary cells: {res['neff'].min():.1f}-{res['neff'].max():.1f} "
          f"on nominal n {int(res['n'].min())}-{int(res['n'].max())}")
    return res, sec


if __name__ == "__main__":
    fx = Findex()
    run(fx)
