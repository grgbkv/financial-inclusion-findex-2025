"""P27 (pre-registered): error anatomy of the P18 champion, with a registered stopping rule.

Parent: P26. NOT a mechanism — a diagnostic. `predictor.py` is NOT modified by this file; it is
imported and run unchanged, so all three MAEs stay byte-identical to the champion.

PEEK DISCLOSURE, per the pre-registration and the amended peek rule: this reads 2024 residuals and
is therefore NOT blind to the holdout. It is logged as exploratory/diagnostic. No MAE may improve as
a result of it, and any future feature or basin choice traceable to what is learned here must be
declared peek-informed in its own pre-registration. Nothing here can produce a keep.

THE FIVE REGISTERED PANELS
  (a) BIAS vs SCATTER  — mean SIGNED error beside the MAE per target.
  (b) STRUCTURE        — MAE and mean signed error by region and by income group.
  (c) CONCENTRATION    — share of total absolute error from the ten worst countries, and who they are.
  (d) BENCHMARK LADDER — champion vs persistence vs panel-mean vs the movement scale
                         (median |delta 2021->2024| of the target).
  (e) COMMON FACTOR    — correlation of signed residuals ACROSS the three targets, country by country.

REGISTERED DECISION RULE
  If |mean signed error| >= 0.25 x MAE on ANY target, a systematic and in-principle correctable
  component remains and the stream registers ONE MORE MECHANISM next cycle.
  If all three targets are near-zero-mean AND cross-target residual correlation is < 0.30, the
  champion is declared FINAL and the stream closes.
"""
import numpy as np
import pandas as pd

from harness import Findex
import predictor as P

BIAS_RATIO_BAR = 0.25
CROSS_CORR_BAR = 0.30
TOPK = 10


def champion_predictions(fx: Findex):
    """Run predictor.py's own selection logic verbatim — the P18 champion, unmodified."""
    use_two = {"fin17a_17a1_d": True, "fin24aSD_ND": False,
               "account_t_d": P._select_two_stage(fx, "account_t_d")}
    use_three = {"fin17a_17a1_d": P._select_third_stage(fx, "fin17a_17a1_d"),
                 "account_t_d": P._select_third_stage(fx, "account_t_d")}
    use_four = {"fin17a_17a1_d": P._select_fourth_stage(fx, "fin17a_17a1_d")}
    return P.predict(fx, use_two, use_three, use_four)


def residual_frame(fx: Findex, preds):
    """Signed residual (pred - truth, pp) per country per target, plus frame metadata."""
    _, truth = fx.prediction_task()
    meta = (fx.pan_all[fx.pan_all["year"] == 2024]
            .set_index("countrynewwb")[["regionwb24_hi", "incomegroupwb24", "pop_adult"]])
    out = {}
    for t in fx.PRED_TARGETS:
        tr = truth[t].dropna()
        p = preds[t].dropna()
        common = tr.index.intersection(p.index)
        out[t] = pd.DataFrame({
            "pred": p.reindex(common), "truth": tr.reindex(common),
            "resid": p.reindex(common) - tr.reindex(common),
        }).join(meta, how="left")
    return out


def panel_a(res):
    print("\n(a) BIAS vs SCATTER — is the champion off-centre or just noisy?\n")
    print(f"  {'target':20s} {'n':>4s} {'MAE':>7s} {'mean signed':>12s} {'ratio':>7s} "
          f"{'SD resid':>9s}  verdict")
    rows = []
    for t, d in res.items():
        mae = d["resid"].abs().mean()
        ms = d["resid"].mean()
        ratio = abs(ms) / mae
        rows.append({"target": t, "mae": mae, "mean_signed": ms, "ratio": ratio})
        flag = "BIASED" if ratio >= BIAS_RATIO_BAR else "centred"
        print(f"  {t:20s} {len(d):4d} {mae:7.3f} {ms:+12.3f} {ratio:7.3f} "
              f"{d['resid'].std():9.3f}  {flag}")
    return pd.DataFrame(rows)


def panel_b(res):
    print("\n(b) STRUCTURE — does one basin carry the residual?\n")
    for t, d in res.items():
        print(f"  {t}")
        for key, label in [("regionwb24_hi", "region"), ("incomegroupwb24", "income group")]:
            g = d.groupby(key, observed=True)["resid"].agg(
                n="size", mae=lambda s: s.abs().mean(), mean_signed="mean")
            g = g[g["n"] >= 4].sort_values("mae", ascending=False)
            print(f"    by {label}:")
            for k, r in g.iterrows():
                print(f"      {str(k)[:34]:34s} n={int(r['n']):3d}  MAE={r['mae']:6.3f}  "
                      f"mean signed={r['mean_signed']:+7.3f}")
        print()


def panel_c(res):
    print("(c) CONCENTRATION — how much of the error lives in the tail?\n")
    for t, d in res.items():
        a = d["resid"].abs().sort_values(ascending=False)
        share = a.head(TOPK).sum() / a.sum()
        even = TOPK / len(a)
        worst = ", ".join(f"{c} ({d.loc[c, 'resid']:+.1f})" for c in a.head(6).index)
        print(f"  {t:20s} top-{TOPK} carry {share:6.1%} of total |error|  "
              f"(even split would be {even:.1%}, concentration ratio {share / even:.2f}x)")
        print(f"                       worst six: {worst}")
    print()


def panel_d(fx: Findex, res, preds):
    """Champion vs persistence vs panel-mean vs the movement scale."""
    print("(d) BENCHMARK LADDER — how much of what there was to predict was predicted?\n")
    train, truth = fx.prediction_task()
    print(f"  {'target':20s} {'champion':>9s} {'persist':>9s} {'panelmean':>10s} "
          f"{'movement':>9s} {'skill vs persist':>17s}")
    for t in fx.PRED_TARGETS:
        wide = train.pivot_table(index="countrynewwb", columns="year", values=t) * 100
        last = wide.get(2021)
        tr = truth[t].dropna()
        common = tr.index.intersection(last.dropna().index).intersection(preds[t].dropna().index)
        y = tr.reindex(common)
        champ = (preds[t].reindex(common) - y).abs().mean()
        pers = (last.reindex(common) - y).abs().mean()
        pmean = (y.mean() - y).abs().mean()
        move = (last.reindex(common) - y).abs().median()   # median |actual change|
        skill = 1 - champ / pers
        print(f"  {t:20s} {champ:9.3f} {pers:9.3f} {pmean:10.3f} {move:9.3f} {skill:16.1%}")
    print("\n  'movement' = median |actual 2021->2024 change| on the evaluation sample; a champion")
    print("  MAE below it means the typical country's move is larger than the typical miss.\n")


def panel_e(res):
    print("(e) COMMON FACTOR — does the model miss the same countries on every margin?\n")
    wide = pd.DataFrame({t: d["resid"] for t, d in res.items()})
    c = wide.corr(min_periods=30)
    print(c.round(3).to_string())
    pairs = [(a, b, c.loc[a, b]) for i, a in enumerate(c.columns) for b in c.columns[i + 1:]]
    mx = max(abs(v) for _, _, v in pairs)
    print(f"\n  pairwise n (countries with both residuals): "
          f"{', '.join(f'{a[:12]}~{b[:12]}: {int(wide[[a, b]].dropna().shape[0])}' for a, b, _ in pairs)}")
    print(f"  largest |cross-target residual correlation| = {mx:.3f}  (bar {CROSS_CORR_BAR})")
    return mx


def main():
    fx = Findex()
    preds = champion_predictions(fx)
    ev = fx.evaluate_predictions(preds)
    print("P27 — error anatomy of the P18 champion (predictor.py imported UNCHANGED)\n")
    print("  champion MAEs from the harness evaluator:",
          {t: r["mae"] for t, r in ev.items()})

    res = residual_frame(fx, preds)
    bias = panel_a(res)
    panel_b(res)
    panel_c(res)
    panel_d(fx, res, preds)
    mx = panel_e(res)

    print("\n" + "=" * 92)
    print("REGISTERED DECISION RULE")
    biased = bias[bias["ratio"] >= BIAS_RATIO_BAR]
    if len(biased):
        print(f"  |mean signed error| >= {BIAS_RATIO_BAR} x MAE on "
              f"{', '.join(biased['target'])} -> a systematic, in-principle correctable component")
        print("  REMAINS. The stream REGISTERS ONE MORE MECHANISM next cycle.")
    elif mx < CROSS_CORR_BAR:
        print("  All three targets are centred AND cross-target residual correlation "
              f"{mx:.3f} < {CROSS_CORR_BAR}.")
        print("  The champion is declared FINAL and the prediction stream CLOSES.")
    else:
        print(f"  All three targets are centred, but cross-target residual correlation {mx:.3f} "
              f">= {CROSS_CORR_BAR}:")
        print("  a common country-level shock the model misses on several margins at once.")
        print("  The stream REGISTERS ONE MORE MECHANISM (a joint/common-factor term) next cycle.")


if __name__ == "__main__":
    main()
