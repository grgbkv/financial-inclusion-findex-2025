"""M1 + M2 (both pre-registered; independent tests). First use of the micro stream.

M1: "not enough money" barrier (fin11a) among unbanked adults, by income quintile.
M2: mobile-only vs bank-only accountholders, demographic profile (age, education).
"""
from micro import Micro


def run(mi: Micro):
    df = mi.df

    # ---------------- M1
    unb = df[df["account"] == 0].copy()
    unb["fin11a_y"] = (unb["fin11a"] == 1).astype(float)
    unb.loc[unb["fin11a"].isna(), "fin11a_y"] = float("nan")

    rows = []
    for q in sorted(unb["inc_q"].dropna().unique()):
        sub = unb[unb["inc_q"] == q]
        v, n = mi._wavg(sub, "fin11a_y")
        rows.append((q, v * 100 if v == v else float("nan"), n))
        print(f"M1  inc_q={q:.0f}  fin11a rate={v*100:.1f}pp  n={n}")
        print("M1 ", mi.gate_cell_size(n))

    q1_rate = next(r[1] for r in rows if r[0] == 1.0)
    q5_rate = next(r[1] for r in rows if r[0] == 5.0)
    print(f"M1  group diff (q1 - q5) = {q1_rate - q5_rate:.1f}pp")

    # ---------------- M2
    mobile_only = df[(df["account_mob"] == 1) & (df["account_fin"] == 0)].copy()
    bank_only = df[(df["account_fin"] == 1) & (df["account_mob"] == 0)].copy()
    for sub in (mobile_only, bank_only):
        sub["young"] = (sub["age"] <= 35).astype(float)
        sub["primary_only"] = (sub["educ"] == 1).astype(float)

    results = {}
    for label, sub in [("mobile_only", mobile_only), ("bank_only", bank_only)]:
        y, n_y = mi._wavg(sub, "young")
        p, n_p = mi._wavg(sub, "primary_only")
        results[label] = (y * 100, p * 100)
        print(f"M2  {label}  young<=35={y*100:.1f}pp (n={n_y})  primary_only={p*100:.1f}pp (n={n_p})")
        print("M2 ", mi.gate_cell_size(n_y))
        print("M2 ", mi.gate_cell_size(n_p))

    d_young = results["mobile_only"][0] - results["bank_only"][0]
    d_primary = results["mobile_only"][1] - results["bank_only"][1]
    print(f"M2  group diff young<=35 (mobile_only - bank_only) = {d_young:.1f}pp")
    print(f"M2  group diff primary_only (mobile_only - bank_only) = {d_primary:.1f}pp")


if __name__ == "__main__":
    run(Micro())
