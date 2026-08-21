"""Fixed micro-level layer for the Findex autoresearch loop. NOT modified during runs.

Individual-level Global Findex 2025 (WLD_2024_FINDEX_v02_M, labelled CSV): 144,090
respondents, 140 economies, 2024 wave, survey weights in `wgt`.

License (WB Microdata Library): research use only, NO redistribution — the microdata/
folder is gitignored; aggregates and findings derived from it may be published, raw
rows never.

Micro rigor gates:
  M1 — weights are mandatory: this module only exposes weighted statistics.
  M2 — minimum unweighted cell size for any subgroup estimate (default 100).
  M3 — country-file cross-check: weighted micro aggregates must reproduce the
       country-level database where an equivalent indicator exists.
"""
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
MICRO_CSV = os.path.join(HERE, "microdata",
                         "findex_microdata_2025_labelled_update112425.csv")
COUNTRY_CSV = os.path.join(HERE, "..", "01_Data", "GlobalFindexDatabase2025.csv")

# labelled-CSV headline outcomes already coded 0/1 in v02
BINARY_OUTCOMES = ["account", "account_fin", "account_mob", "saved", "borrowed",
                   "anydigpayment", "receive_wages", "receive_transfers",
                   "merchantpay_dig", "pay_utilities"]

DEMOGRAPHICS = ["female", "age", "educ", "inc_q", "emp_in", "urbanicity"]


class Micro:
    def __init__(self):
        self.df = pd.read_csv(MICRO_CSV, low_memory=False)
        for col in BINARY_OUTCOMES:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors="coerce")

    # ------------------------------------------------------------- statistics
    @staticmethod
    def _wavg(sub, col):
        s = sub.dropna(subset=[col, "wgt"])
        if s.empty:
            return np.nan, 0
        return float(np.average(s[col], weights=s["wgt"])), int(len(s))

    def rate(self, col, economy=None, where=None):
        """Weighted rate (pp) of a binary column, with unweighted n. `where` is a
        boolean mask aligned to self.df."""
        sub = self.df
        if economy is not None:
            sub = sub[sub["economy"] == economy]
        if where is not None:
            sub = sub[where.reindex(sub.index).fillna(False)]
        v, n = self._wavg(sub, col)
        return (v * 100 if pd.notna(v) else np.nan), n

    def rate_by(self, col, by, economies=None):
        """Weighted rate (pp) of `col` split by category column `by`, pooled or
        restricted to a list of economies. Returns DataFrame [group, rate_pp, n]."""
        sub = self.df if economies is None else self.df[self.df["economy"].isin(economies)]
        rows = []
        for g, grp in sub.groupby(by, dropna=True):
            v, n = self._wavg(grp, col)
            rows.append({by: g, "rate_pp": round(v * 100, 2) if pd.notna(v) else np.nan,
                         "n_unweighted": n})
        return pd.DataFrame(rows)

    # ------------------------------------------------------------- gates
    @staticmethod
    def gate_cell_size(n, min_n=100):
        """M2: refuse subgroup claims built on thin cells."""
        return {"gate": "M2_cell_size", "ok": bool(n >= min_n), "n_unweighted": int(n)}

    def gate_country_file(self, micro_col, country_col, economies, tol_pp=1.0):
        """M3: weighted micro aggregate must reproduce the country-level database."""
        c = pd.read_csv(COUNTRY_CSV, low_memory=False)
        c = c[(c["year"] == 2024) & (c["group"] == "all")].set_index(
            "countrynewwb")[country_col] * 100
        name_map = {"Czech Republic": "Czechia", "Slovak Republic": "Slovakia"}
        devs = []
        for e in economies:
            mv, n = self.rate(micro_col, economy=e)
            cv = c.get(name_map.get(e, e), np.nan)
            if pd.notna(mv) and pd.notna(cv):
                devs.append(abs(mv - cv))
        if not devs:
            return {"gate": "M3_country_file", "ok": False, "note": "no comparable economies"}
        return {"gate": "M3_country_file", "ok": bool(max(devs) <= tol_pp),
                "max_dev_pp": round(max(devs), 2), "n_economies": len(devs)}


def self_check():
    mi = Micro()
    assert len(mi.df) == 144090, len(mi.df)
    g = mi.gate_country_file("account", "account_t_d",
                             ["India", "Kazakhstan", "Poland", "Estonia", "Uzbekistan",
                              "Czech Republic"])
    assert g["ok"] and g["max_dev_pp"] <= 0.1, g
    r, n = mi.rate("account", economy="Uzbekistan")
    assert n > 900 and abs(r - 59.7) < 0.5, (r, n)
    print("micro self-check: OK — 144,090 rows; micro aggregates reproduce the "
          "country file (max dev %.2fpp over %d economies)" % (g["max_dev_pp"], g["n_economies"]))


if __name__ == "__main__":
    self_check()
