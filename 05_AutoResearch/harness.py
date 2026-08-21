"""Fixed harness for the Findex autoresearch loop. NOT modified during experiments.

Provides: canonical frames (balanced panel, official aggregates, group slices),
weighted statistics, the rigor gates from the working paper (the four aggregation
pitfalls, automated), and the fixed prediction-stream evaluator.

Every experiment consumes data ONLY through this module. That is the point:
the gates cannot be skipped by construction.
"""
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "01_Data", "GlobalFindexDatabase2025.csv")

YEARS = [2011, 2014, 2017, 2021, 2024]

# Indicator families: concept -> variants. Experiments must reference concepts
# through this registry; using a narrow variant where a headline exists must be
# declared (gate G3).
INDICATORS = {
    "account": {"headline": "account_t_d"},
    "mobile_money": {"headline": "mobileaccount_t_d"},
    "fi_account": {"headline": "fiaccount_t_d"},
    "digital_payment": {"headline": "g20_any"},
    "saved_formally": {"headline": "fin17a_17a1_d", "narrow": "fin17a"},
    "borrowed_formally": {"headline": "fin22a_22a1_22g_d", "narrow": "fin22a"},
    "inactive": {"headline": "inactive_t_d"},
    "resilience": {"headline": "fin24aSD_ND"},
}

OFFICIAL_ENTITIES = {
    "world": "world",
    "developing": "Developing economies",
}


class Findex:
    """Canonical data access. One instance per process."""

    def __init__(self):
        df = pd.read_csv(DATA, low_memory=False)
        df["year"] = df["year"].replace(2022, 2021)  # wave merge, before anything else
        self.raw = df
        self.countries = df[df["regionwb24_hi"].notna()].copy()
        self.official = df[df["regionwb24_hi"].isna()].copy()

        c_all = self.countries[self.countries["group"] == "all"]
        waves = c_all.groupby("countrynewwb")["year"].nunique()
        self.panel_names = set(waves[waves == 5].index)

        self.pan_all = c_all[c_all["countrynewwb"].isin(self.panel_names)].copy()
        self.pan_dev = self.pan_all[self.pan_all["incomegroupwb24"] != "High income"].copy()
        self.pan_grp = self.countries[
            self.countries["countrynewwb"].isin(self.panel_names)].copy()
        # Unbalanced full sample: allowed ONLY as explicitly-labeled robustness (G2)
        self.full_all_UNBALANCED = c_all.copy()

    # ------------------------------------------------------------ statistics
    @staticmethod
    def wmean(d, col, w="pop_adult"):
        s = d.dropna(subset=[col, w])
        return np.nan if s.empty else float(np.average(s[col], weights=s[w]))

    def series(self, frame, col, years=YEARS):
        return pd.Series(
            {y: self.wmean(frame[frame["year"] == y], col) for y in years}).dropna() * 100

    def official_series(self, entity_key, col, years=YEARS):
        entity = OFFICIAL_ENTITIES[entity_key]
        d = self.official[(self.official["countrynewwb"] == entity)
                          & (self.official["group"] == "all")]
        out = {}
        for y in years:
            v = d.loc[d["year"] == y, col]
            if len(v) and pd.notna(v.iloc[0]):
                out[y] = float(v.iloc[0]) * 100
        return pd.Series(out)

    def country_panel(self, frame, col, years):
        """Wide per-country table of col for the given years (values in pp),
        plus 2024 adult population as weight."""
        sub = frame[frame["year"].isin(years)]
        wide = sub.pivot_table(index="countrynewwb", columns="year", values=col) * 100
        pop = frame[frame["year"] == 2024].set_index("countrynewwb")["pop_adult"]
        wide["pop"] = pop
        return wide

    @staticmethod
    def weighted_corr(x, y, w):
        m = pd.notna(x) & pd.notna(y) & pd.notna(w)
        x, y, w = x[m], y[m], w[m]
        if len(x) < 10:
            return np.nan, int(len(x))
        mx, my = np.average(x, weights=w), np.average(y, weights=w)
        cov = np.average((x - mx) * (y - my), weights=w)
        sx = np.sqrt(np.average((x - mx) ** 2, weights=w))
        sy = np.sqrt(np.average((y - my) ** 2, weights=w))
        return float(cov / (sx * sy)), int(len(x))

    # ------------------------------------------------------------ rigor gates
    def gate_coverage(self, frame, col, year, min_countries=30, min_pop_share=0.5):
        """G4: enough countries and population behind an aggregate claim."""
        d = frame[frame["year"] == year].dropna(subset=[col, "pop_adult"])
        n = d["countrynewwb"].nunique()
        base = frame[frame["year"] == year]["pop_adult"].sum()
        share = d["pop_adult"].sum() / base if base else 0.0
        ok = n >= min_countries and share >= min_pop_share
        return {"gate": "G4_coverage", "ok": bool(ok), "n_countries": int(n),
                "pop_share": round(float(share), 3)}

    def gate_official(self, computed_series_pp, entity_key, col, tol_pp=2.5):
        """G5: computed aggregate must track the official one where it exists."""
        off = self.official_series(entity_key, col)
        common = [y for y in computed_series_pp.index if y in off.index]
        if not common:
            return {"gate": "G5_official", "ok": True, "note": "no official series"}
        dev = max(abs(computed_series_pp[y] - off[y]) for y in common)
        return {"gate": "G5_official", "ok": bool(dev <= tol_pp),
                "max_dev_pp": round(float(dev), 2)}

    def gate_jackknife(self, x, y, w, drop_top=5):
        """G6: association keeps its sign when the largest-population countries
        are removed (guards against one-country stories, e.g. India/China)."""
        r_full, n = self.weighted_corr(x, y, w)
        if pd.isna(r_full):
            return {"gate": "G6_jackknife", "ok": False, "note": "insufficient n"}
        keep = w.sort_values(ascending=False).index[drop_top:]
        r_jack, _ = self.weighted_corr(x.reindex(keep), y.reindex(keep), w.reindex(keep))
        ok = pd.notna(r_jack) and np.sign(r_jack) == np.sign(r_full)
        return {"gate": "G6_jackknife", "ok": bool(ok),
                "r_full": round(r_full, 3), "r_droptop": round(float(r_jack), 3) if pd.notna(r_jack) else None,
                "n": n}

    @staticmethod
    def gate_variant(concept, used_col):
        """G3: declare which variant of an indicator family is in use."""
        fam = INDICATORS.get(concept, {})
        role = next((k for k, v in fam.items() if v == used_col), None)
        return {"gate": "G3_variant", "ok": role is not None,
                "concept": concept, "role": role or "UNREGISTERED"}

    # ------------------------------------------------------------ prediction stream
    PRED_TARGETS = ["account_t_d", "fin24aSD_ND", "fin17a_17a1_d"]

    def prediction_task(self):
        """Fixed task: given panel history <=2021, predict 2024 per country.
        Returns (train_frame, test_truth) — test truth is used ONLY by evaluate()."""
        train = self.pan_all[self.pan_all["year"] <= 2021].copy()
        truth = {}
        for t in self.PRED_TARGETS:
            truth[t] = self.pan_all[self.pan_all["year"] == 2024].set_index(
                "countrynewwb")[t] * 100
        return train, truth

    def evaluate_predictions(self, preds):
        """preds: {target: pd.Series indexed by countrynewwb, values in pp}.
        Returns per-target MAE (pp) over panel countries with truth available."""
        _, truth = self.prediction_task()
        out = {}
        for t, p in preds.items():
            tr = truth[t].dropna()
            common = tr.index.intersection(p.dropna().index)
            if len(common) < 50:
                out[t] = {"mae": None, "n": int(len(common)), "note": "insufficient coverage"}
                continue
            mae = float((p.reindex(common) - tr.reindex(common)).abs().mean())
            out[t] = {"mae": round(mae, 3), "n": int(len(common))}
        return out


def self_check():
    """Harness must reproduce the working paper's published numbers exactly."""
    fx = Findex()
    acc = fx.series(fx.pan_all, "account_t_d")
    assert round(acc[2011], 1) == 51.4 and round(acc[2024], 1) == 78.9, acc
    res = fx.series(fx.pan_dev, "fin24aSD_ND", [2021, 2024])
    assert round(res[2021], 1) == 54.7 and round(res[2024], 1) == 54.5, res
    sav = fx.series(fx.pan_dev, "fin17a_17a1_d", [2021, 2024])
    assert round(sav[2024], 1) == 38.0, sav
    off = fx.gate_official(acc, "world", "account_t_d")
    assert off["ok"] and off["max_dev_pp"] <= 1.5, off
    assert len(fx.panel_names) == 117
    print("harness self-check: OK (paper numbers reproduced, 117-country panel)")


if __name__ == "__main__":
    self_check()
