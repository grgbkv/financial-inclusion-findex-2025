"""U21 (pre-registered): is being OFFLINE a bigger gate on digital-payment use than being
least-educated? — the access-absorption ruler with CONNECTIVITY as a third margin.

Program 5, items 5.3 and 5.4. Parents: U10/U15/U17 (the ruler). Micro stream, 2024 wave.

B2 BREADTH CELL: micro column `internet_use` — 144,090 non-null, binary, and at ZERO ledger
mentions before this experiment. First use of Program 5's individual-level half.

WHY. The ruler has been run on education, age, income, labour force and urbanicity, always
conditional on holding an account, and the recurring result is that ACCESS absorbs almost none of
the gradient. E29 showed that at the COUNTRY level the rails are not proxies for connectivity. The
individual-level question is different: among people who already hold an account, how large is the
connectivity difference in digital-payment use, and does conditioning on it absorb the education
gradient that account holding could not?

DESIGN, per the pre-registration (all rates weighted by `wgt`, via the fixed micro.py):
  1. unconditional `anydigpayment` by `internet_use`
  2. the same gap among accountholders (`account == 1`)
  3. among accountholders: the connectivity gap beside the EDUCATION gap (educ 3 vs educ 1) and the
     INCOME gap (inc_q 5 vs inc_q 1), all on the same sample
  4. ABSORPTION: the education gap among accountholders recomputed among accountholders who use the
     internet; statistic = 1 - (conditional gap / unconditional-on-connectivity gap)
  5. item 5.4: profile of `internet_use == 0` among accountholders by educ, inc_q, age band, sex,
     urbanicity, labour force, with M2 on every cell

REGISTERED CLAIMS AND BARS:
  C1  among accountholders, the offline-vs-online gap in anydigpayment is >= 5pp AND LARGER than
      the education gap on the same sample
  C2  conditioning on internet_use removes >= 30% of the education gap among accountholders
Each stands or falls on its own bar.

GATES. M1 (weights, enforced by the module). M2 (unweighted n >= 100) on every reported cell.
M3 against the country file on `account` and `anydigpayment`, tolerance 1pp.

DECLARED. `internet_use` is self-reported internet USE — a behaviour, not infrastructure access —
and it is plainly co-determined with digital payment use: a person may report using the internet
BECAUSE they pay digitally. One cross-section cannot separate the directions. "Gate" is shorthand
for a conditional difference and carries no causal content. Conditioning on account holding is
post-treatment (the U6/U8/U10/U14-U20 caveat). Single wave: no trend language.
"""
import numpy as np
import pandas as pd

from micro import Micro

MIN_CELL = 100
GAP_BAR = 5.0
ABSORB_BAR = 0.30

M3_ECONOMIES = ["India", "Kazakhstan", "Poland", "Estonia", "Uzbekistan", "Brazil", "Nigeria",
                "Indonesia", "Turkiye", "Mexico"]


def gap(mi: Micro, col, hi_mask, lo_mask, base, label, hi_lab, lo_lab):
    """Weighted rate difference hi - lo on `col` within `base`, with M2 on both cells."""
    v_hi, n_hi = mi.rate(col, where=base & hi_mask)
    v_lo, n_lo = mi.rate(col, where=base & lo_mask)
    g_hi, g_lo = mi.gate_cell_size(n_hi, MIN_CELL), mi.gate_cell_size(n_lo, MIN_CELL)
    ok = g_hi["ok"] and g_lo["ok"]
    print(f"  {label:52s} {hi_lab:>14s} {v_hi:5.1f}  {lo_lab:>14s} {v_lo:5.1f}  "
          f"gap {v_hi - v_lo:+6.1f}pp   n {n_hi:6d}/{n_lo:6d}  M2 {'ok' if ok else 'FAIL'}")
    return {"label": label, "rate_hi": v_hi, "rate_lo": v_lo, "gap": v_hi - v_lo,
            "n_hi": n_hi, "n_lo": n_lo, "m2_ok": ok}


def run(mi: Micro):
    df = mi.df
    print("U21 — connectivity on the access-absorption ruler (2024 micro, weighted)\n")

    print("M3 country-file cross-check:")
    print("  account       ", mi.gate_country_file("account", "account_t_d", M3_ECONOMIES))
    print("  anydigpayment ", mi.gate_country_file("anydigpayment", "g20_any", M3_ECONOMIES))

    online = df["internet_use"] == 1
    offline = df["internet_use"] == 0
    acct = df["account"] == 1
    all_mask = pd.Series(True, index=df.index)

    educ_hi, educ_lo = df["educ"] == 3, df["educ"] == 1
    inc_hi, inc_lo = df["inc_q"] == 5, df["inc_q"] == 1

    print("\n=== STEP 1 — unconditional connectivity gap in digital-payment use ===")
    s1 = gap(mi, "anydigpayment", online, offline, all_mask,
             "anydigpayment | everyone", "online", "offline")

    print("\n=== STEP 2 — the same gap AMONG ACCOUNTHOLDERS ===")
    s2 = gap(mi, "anydigpayment", online, offline, acct,
             "anydigpayment | accountholders", "online", "offline")
    absorbed_by_account = 1 - (s2["gap"] / s1["gap"]) if s1["gap"] else np.nan
    print(f"  -> account holding absorbs {absorbed_by_account:.1%} of the unconditional "
          f"connectivity gap")

    print("\n=== STEP 3 — the registered comparison, all on accountholders ===")
    e_acct = gap(mi, "anydigpayment", educ_hi, educ_lo, acct,
                 "anydigpayment | accountholders, EDUCATION", "tertiary", "primary-")
    i_acct = gap(mi, "anydigpayment", inc_hi, inc_lo, acct,
                 "anydigpayment | accountholders, INCOME", "q5", "q1")

    print("\n=== STEP 4 — does connectivity absorb the EDUCATION gradient? ===")
    e_online = gap(mi, "anydigpayment", educ_hi, educ_lo, acct & online,
                   "anydigpayment | accountholders WHO USE THE INTERNET, EDUC", "tertiary",
                   "primary-")
    e_offline = gap(mi, "anydigpayment", educ_hi, educ_lo, acct & offline,
                    "anydigpayment | accountholders WHO DO NOT, EDUC", "tertiary", "primary-")
    absorb_e = 1 - (e_online["gap"] / e_acct["gap"]) if e_acct["gap"] else np.nan
    i_online = gap(mi, "anydigpayment", inc_hi, inc_lo, acct & online,
                   "anydigpayment | accountholders WHO USE THE INTERNET, INCOME", "q5", "q1")
    absorb_i = 1 - (i_online["gap"] / i_acct["gap"]) if i_acct["gap"] else np.nan
    print(f"  -> connectivity absorbs {absorb_e:.1%} of the education gap, "
          f"{absorb_i:.1%} of the income gap")

    print("\n=== ITEM 5.4 — who is offline AMONG ACCOUNTHOLDERS? (share internet_use == 0) ===")
    # Two derived columns are attached to the loaded frame so that every rate below is still
    # produced by the module's weighted estimator (gate M1). micro.py itself is untouched.
    df["u21_offline"] = (df["internet_use"] == 0).astype(float)
    df["u21_age_band"] = pd.cut(df["age"], [14, 24, 34, 49, 64, 200],
                                labels=["15-24", "25-34", "35-49", "50-64", "65+"])
    rows = []
    slices = [("educ", {1: "primary or less", 2: "secondary", 3: "tertiary"}),
              ("inc_q", {i: f"income q{i}" for i in range(1, 6)}),
              ("female", {1: "men", 2: "women"}),
              ("urbanicity", {1: "rural", 2: "urban"}),
              ("emp_in", {1: "in workforce", 2: "out of workforce"}),
              ("u21_age_band", {k: k for k in ["15-24", "25-34", "35-49", "50-64", "65+"]})]
    for col, labels in slices:
        for code, lab in labels.items():
            v, n = mi.rate("u21_offline", where=acct & (df[col] == code))
            rows.append({"slice": col, "group": lab, "pct_offline": v, "n": n,
                         "m2_ok": n >= MIN_CELL})
    prof = pd.DataFrame(rows)
    for col in prof["slice"].unique():
        p = prof[prof["slice"] == col]
        print(f"  {col:10s} " + "  ".join(
            f"{r['group']}: {r['pct_offline']:.1f}% (n={r['n']}{'' if r['m2_ok'] else ' M2FAIL'})"
            for _, r in p.iterrows()))

    print("\n" + "=" * 100)
    print("=== VERDICT (pre-registered) ===")
    c1a = s2["gap"] >= GAP_BAR
    c1b = s2["gap"] > e_acct["gap"]
    print(f"  C1  connectivity gap among accountholders = {s2['gap']:+.1f}pp "
          f"(bar >= {GAP_BAR:.0f}pp: {c1a}) AND > education gap {e_acct['gap']:+.1f}pp: {c1b}"
          f"  -> {'KEEP' if (c1a and c1b) else 'DISCARD'}")
    c2 = absorb_e >= ABSORB_BAR
    print(f"  C2  connectivity absorbs {absorb_e:.1%} of the education gap "
          f"(bar >= {ABSORB_BAR:.0%})  -> {'KEEP' if c2 else 'DISCARD'}")
    print(f"  [context] account holding absorbed {absorbed_by_account:.1%} of the connectivity gap; "
          f"connectivity absorbs {absorb_i:.1%} of the income gap")
    return {"s1": s1, "s2": s2, "educ_acct": e_acct, "educ_online": e_online,
            "educ_offline": e_offline, "inc_acct": i_acct, "inc_online": i_online,
            "absorb_e": absorb_e, "absorb_i": absorb_i,
            "absorbed_by_account": absorbed_by_account, "profile": prof}


if __name__ == "__main__":
    run(Micro())
