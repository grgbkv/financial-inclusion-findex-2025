# Findex autoresearch — program

Autonomous empirical-research loop over the Global Findex 2025 data, adapted from
karpathy/autoresearch. Two streams share one discipline: edit → run → keep-or-discard → log.

## Ground rules

- **`harness.py` is fixed.** All data access goes through it: canonical frames (117-country
  balanced panel, official aggregates, group slices), weighted stats, rigor gates, the
  prediction evaluator. Do not modify during a run.
- **Branch discipline.** Runs happen on `autoresearch/<tag>`, never on main. Stage only
  `05_AutoResearch/` paths, never `git add -A`.
- **Every experiment is committed** before it runs (hypothesis experiments as
  `experiment.py` revisions; prediction experiments as `predictor.py` revisions).

## Stream 1 — hypothesis lab

1. **Pre-register first.** Append to `RESEARCH_LOG.md`: hypothesis, planned test, keep
   threshold — BEFORE looking at the answer. This is the data-dredging control.
2. Implement in `experiment.py`, run, read the result.
3. **Gates (from the working paper's pitfall taxonomy, automated in the harness):**
   G3 declared indicator variant · G4 coverage (n countries + population share) ·
   G5 official-aggregate cross-check where applicable · G6 jackknife sign-stability
   (drop the 5 largest-population countries) for any association claim.
4. Verdict: `keep` only if the pre-registered threshold AND all applicable gates pass.
   Everything — kept and discarded — goes to `findings.tsv`. Discards are data, not failures.
5. Claims are descriptive associations, never causal. Say so in the wording.

Keep thresholds (defaults): weighted |r| ≥ 0.30 for associations; group differences ≥ 5 pp;
level claims within G5 tolerance of official aggregates.

## Stream 2 — prediction lab

Fixed task (in the harness): given panel history ≤ 2021, predict each panel country's 2024
value for `account_t_d`, `fin24aSD_ND`, `fin17a_17a1_d`. Metric: per-target MAE in pp.
Iterate `predictor.py` exactly like autoresearch's `train.py`: commit, run, keep if MAE
improves, revert if not. Log to `results_prediction.tsv`.

## Logging

- `findings.tsv` (tab-separated): id, stream, commit, status, claim, test, effect, gates, note
- `results_prediction.tsv`: commit, target, mae_pp, n, status, description
- `RESEARCH_LOG.md`: pre-registrations and verdicts, chronological.

## Run budget

Supervised session: ~2 hours, then distill kept findings into `EXTENSIONS_DRAFT.md`
(candidate material for a working-paper v2). Within the budget, do not stop to ask
whether to continue; outside it, stop and summarize.

## Stream 3 — micro lab (added 2026-07-11)

Individual-level Global Findex 2025 (144,090 respondents, 140 economies, 2024 wave) via the
fixed `micro.py` module. License: research use only, no redistribution — the microdata/
folder is gitignored; published outputs may contain aggregates and findings, never raw rows.

Rules: all statistics weighted (`wgt`, enforced by the module API); gates M2 (unweighted
cell n ≥ 100 for any subgroup claim) and M3 (micro aggregates must reproduce the country
file within 1pp where an equivalent exists) apply on top of pre-registration. Findings log
to findings.tsv with stream = `micro`. Micro claims are within-2024 cross-sectional
descriptions — no trend language (single wave).
