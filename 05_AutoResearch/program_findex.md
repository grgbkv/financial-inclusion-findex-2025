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

## Amendments (2026-07-11, after the first scheduled run)

1. **The peek rule.** Any exploratory look at an outcome ("calibration check") must be logged
   as an *exploratory* entry BEFORE the formal pre-registration, and a hypothesis whose answer
   was peeked on the same data cannot be logged as `keep` under pre-registration — mark such
   findings `keep-exploratory`. Pre-registration only binds when the answer was genuinely
   unknown at registration time. (Trigger: experiment M1 disclosed a prior calibration peek —
   honest, but the verdict class must reflect it.)
2. **Experiment IDs.** Micro-stream experiments use `U<n>` IDs (U for "unit-level") to avoid
   colliding with the micro gate names M1-M3. Existing rows M1/M2 in findings.tsv are
   grandfathered; read them as U1/U2.

## Amendments (2026-08-01, after the coverage audit)

A coverage audit at experiment 50 found the loop had used **~5% of the country file's 429 indicator
columns**, **11% of the micro file's 192**, **one of four wave transitions**, and **one of seven
country frames**. Fourteen country modules (310 columns) had never been touched, including the
entire consumer-protection/fraud module and the financial-health items. The cause is structural, not
accidental: each cycle's backlog was seeded from the previous cycle's kept finding, which is
hill-climbing, and hill-climbing sinks one deep shaft. The rules below make breadth a constraint
rather than an aspiration. They are additive — every gate, threshold and pre-registration rule above
stands unchanged.

### Breadth discipline

**B1 — Coverage first.** Run `python3 coverage.py` at the start of every cycle, before choosing
hypotheses. It reports, without computing any outcome (so it is never a peek): columns and modules
touched by the ledger, wave transitions used, and frame usage. The cycle's pre-registration must
name the coverage cells its experiments land on.

**B2 — Frame rotation.** At least **one experiment per cycle** must land on an **untouched or thin**
cell: a module the ledger has never used, a wave transition other than 2021→2024, or a country frame
other than `pan_dev` with `group == "all"`. A cycle of three experiments all inside the current
shaft is a protocol violation, however good the hypotheses are.

**B3 — Lineage cap.** No more than **three consecutive experiments** may descend from the same
parent finding. The fourth must jump. Record the parent in the pre-registration so the chain is
auditable; the E23 → E24 → E25 → E26 sequence is exactly the pattern this cap exists to break.

**B4 — Replication window.** A kept 2021→2024 association is a **window claim**, not a general one,
until it has been replicated on at least one earlier transition. Such findings are logged with
status `keep-window`; they are promoted to `keep-general` only after replication, and only a
`keep-general` may enter `EXTENSIONS_DRAFT.md` or the paper draft as a regularity. Existing keeps are
grandfathered as `keep-window` and are listed for replication in `RESEARCH_AGENDA.md` Program 1.

**B5 — Lagged designs are in scope.** Every country-level experiment to date correlates
contemporaneous changes, which is why every claim carries "identifies nothing". Designs that relate a
**level or change at t** to a **subsequent change at t+1** are explicitly allowed and encouraged.
They remain descriptive — a temporal-ordering statement, never a causal one — and must be worded as
such, but they are a strictly stronger form of evidence than same-window co-movement and the
five-wave panel supports them.

**B6 — Inference on new keeps.** From this amendment, any **new** association keep must report,
computed inside the experiment file (the harness stays fixed): (i) a **bootstrap interval** for the
statistic — resample countries with replacement, ≥1,000 draws, percentile interval; and (ii) the
**Kish effective sample size** of the population weights, `neff = (Σw)² / Σw²`, alongside the nominal
n. A population-weighted correlation on 76 countries whose weight is concentrated in five economies
does not have 76 degrees of freedom, and the ledger should stop implying it does. G6 stays — it
answers a different question (one-country stories) than an interval does.

**B7 — Multiple testing.** The ledger's keep count is now large enough that a false-discovery
accounting is owed. Report a Benjamini–Hochberg-adjusted view over the association ledger before the
next distillation into the paper draft (carried from the harness v2 note #2, now due).

### Frames declared in scope

Previously used: `pan_all`, `pan_dev`, both with `group == "all"`. Now also in scope, through the
existing `Findex.pan_grp` frame:

- `group == "gender"` (men / women), `"income"` (poorest 40% / richest 60%), `"education"`
  (primary or less / secondary or more), `"age_cat"` (15-24 / 25+), `"laborforce"` (in / out),
  `"urbanicity"` (rural / urban) — 117 panel economies, five waves for all but urbanicity.

That is a 13-year within-country inequality panel across six dimensions. Two experiments (E20, E21)
had used it as of this amendment.

## Amendments (2026-08-11, the distillation pass)

Two demotions that had been standing as recommendations were executed, and three rules are added.
All existing gates, thresholds and pre-registration rules stand unchanged.

**Executed status changes.**

- **E7** `keep-window` → **`discard`**. Recommended by E32 (BH `p_boot` 0.068; unweighted +0.541 →
  +0.283; E4 retention 0.44), confirmed by E40's ledger-wide audit.
- **E5b** `keep-window` → **`discard`**. Recommended by E38 (the partial reads −0.654 / +0.591 /
  −0.595 across consecutive windows), confirmed by E40 (`p_boot` 0.331, retention 0.19, and an
  unweighted partial of **+0.106** against a weighted −0.595 — a sign flip on de-weighting).
- **E13** stays `keep-general` but is **flagged**: E40 found it fails the unweighted lens in *both*
  windows (+0.188 here, +0.248 in its E30b replication), so its promotion rests on the population
  weighting twice over.

**B8 — Sign agreement on promotion.** A `keep-window` finding is promoted to `keep-general` only if
**every** tested earlier window agrees in sign and clears the original threshold. One agreeing
window is not enough. *(Proposed by E38, where a promotion rule reading "at least one earlier
window" mechanically passed a partial that reversed between consecutive windows and reversed back;
only the standing E4 magnitude rule stopped it.)*

**B9 — The unweighted twin is mandatory, and disagreement is a status.** Every association keep must
report the unweighted correlation beside the population-weighted one. Where the two lenses give
different verdicts against the 0.30 threshold, the finding is logged **`keep-weighted`** (or
`discard-weighted`) rather than `keep`/`discard`, and the weighting dependence is stated in the
claim itself. *(E40 found the weighting crossing the threshold in both directions — E16
+0.198/+0.555 and E26 +0.294/+0.364 — and E41, run the same day, produced a live case at
+0.039/+0.418 with drop-top-5 at +0.421. At `neff` ≈ 7 the 0.30 bar is a bar on a statistic that
five economies decide.)*

**B10 — `neff` beside every n, and no significance language on nominal n.** Every reported
association carries its Kish `neff` next to the nominal n, and no write-up may attach significance
language to nominal n. Across E40's thirty-three tests spanning every design in the ledger, BH at
q = 0.10 rejects **26 of 33 on nominal n and 1 of 33 on `p_neff`**; median `neff` is **7.2** against
a median nominal n of **71**. *(Carried from E32 and now established ledger-wide.)*

## Amendments (2026-08-13, from the E42/E43 cycle)

**B11 — `keep-unweighted` / `keep-general-unweighted`, the symmetric partner of B9.** B9 created
`keep-weighted` for a finding that keeps under the population-weighted lens and not the unweighted
one. The mirror case is now live: E42 found an association clearing 0.30 in **all four** transitions
unweighted and in three of four weighted. Such a finding is logged **`keep-unweighted`**, or
**`keep-general-unweighted`** where B4's replication requirement is also met, and the lens is named
in the claim text. A status must always name the lens the keep holds under; a bare `keep` now means
both lenses agree.

**B12 — name the economies, do not say "five economies".** The ledger's standing phrase "five
economies decide it" is a *hypothesis about a cell*, not a property of the frame. E42's P3 ran a
leave-one-economy-out on the E16 cell and found **China alone** moves `r_w` from +0.198 to +0.726,
while India — with almost the same population weight — moves it by +0.074. Every future G6 report on
a weighted association must accompany the drop-top-5 figure with the **single largest leave-one-out
effect and the economy's name**. It costs one loop and it replaces a guess with a fact.

**The `neff` critique does not transfer to the unweighted lens, and write-ups must stop implying it
does.** E40's headline result — BH rejects 1 of 33 at `neff` ≈ 7 — is a statement about the
**population-weighted** ledger. An unweighted correlation over 77 economies has `neff` = n = 77,
because there are no weights to concentrate. Two caveats survive and must be carried with the point:
economies are not independent draws (regional clustering is unmodelled anywhere in this repo), and
the unweighted statistic answers a **different question** — it describes the typical *economy*, the
weighted one the typical *person*. Neither is the correct lens. The ledger has been reporting one of
them as if it answered both, and B9/B11 exist to stop that.

**A standing requirement for every pp-gap design.** E43's registered pp-gap secondary showed the
income, education and labour-force gaps widening in ~3 economies out of 4, surviving both G6 and
de-weighting — and its **scale-free log-odds twin showed no systematic widening at all**, with income
turning negative on two of three lenses. This is E21's discard reproduced on five axes. **Any gap
claim must report the log-odds twin beside the pp version, and where they disagree the pp version is
the artifact** — levels rose from a low base everywhere in this window, and a pp gap widens
arithmetically under those conditions.
