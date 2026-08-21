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

## Amendment (2026-08-15, from the E44/E45 cycle)

**B13 — the log-odds twin requirement extends from gaps to any pp comparison between groups.** The
2026-08-13 amendment required a scale-free twin beside every *gap* claim. E44 registered a **ratio of
percentage-point changes** (the "reach ratio", disadvantaged Δ / advantaged Δ) in good faith as a
scale-relative statistic and it failed for exactly the arithmetic reason gaps fail: while both groups
are below 50%, equal proportional growth produces **fewer pp** for the lower-starting group. On the
log-odds twin all five dimensions cleared the same bar (0.845–1.107) where three of five failed on pp
(0.576–0.721). **Any between-group comparison of percentage-point changes — a gap, a difference, or a
ratio — must report its log-odds twin, and where the two disagree the pp version is the artifact.**
This is the third instance of the same trap (E21, E43's secondary, E44's P2).

**A clarification owed on `neff`, from E45.** A low Kish `neff` says the **weights are concentrated**;
it does not say the **result is fragile**. E45's `fin31a_31b` cell has `neff` = 7.2 — the ledger's
usual figure — and yet its weighted and unweighted correlations are +0.797 and +0.815, drop-top-5 is
+0.821, and the largest single leave-one-out effect is **Brazil at −0.042**. E42's E16 cell has the
same `neff` and moves +0.198 → +0.726 on dropping China. `neff`, the unweighted twin, G6 and the
named leave-one-out are **four different diagnostics**, and write-ups must stop treating a low `neff`
as though it settled the others.

---

# Amendment (2026-08-15c) — the enforcement pass

Eight changes, adopted after a two-week review of the ledger rather than after a single experiment.
They are **additive**: every gate, threshold and pre-registration rule above stands unchanged. Six
are new rules (B14–B19); two are documentation obligations. `make_index.py` enforces B19 and B14 mechanically (`python3 make_index.py --check` exits non-zero). The review's findings that motivate each
are named, because a rule whose reason is not recorded gets dropped by the next cycle that finds it
inconvenient.

## B14 — a single adjacent-wave Δ→Δ may not be an experiment's PRIMARY

**The rule.** The primary of any country-level association experiment must be **either**

- a **long difference** (a span of two or more transitions), reported with rule B16's wave path, **or**
- an **all-windows design** in which the registered claim must hold in **every** tested transition,
  not a majority.

A single adjacent-window Δ→Δ is a **diagnostic**: it may be reported, it may support a primary, and
it may not by itself produce a `keep`. Existing single-window keeps are grandfathered at their current
status and are **not** promotable without satisfying this rule.

**Why.** E39 measured the autocorrelation of country-level change directly: the Spearman correlation
between an economy's change in one window and its change in the next is **≤ +0.07 in all ten pairs
tested and negative in eight** (formal saving −0.413 / −0.350 / +0.070). Country-level wave-to-wave Δ
is dominated by wave-specific variation. The replication record is the same fact seen from the other
side: partials **0 of 3** (E35), E5b reversing **−0.654 / +0.591 / −0.595** between consecutive
windows (E38), lagged designs **0 of 3** (E37), E43's breadth bars **0/5, 0/5, 1/5** (E44), and E48a
splitting 3/3 weighted against 1/3 unweighted. What survived did so *because* it was tested across
windows — the six bivariate rails (E28/E30) and E42's four-transition account~saving result.

## B15 — register the SIGN, not just the magnitude

Every pre-registration that tests a **family** of items, or any single claim with a directional
reading, must state the **predicted sign** as part of the bar. A result of the right magnitude and the
wrong sign is **not** partial confirmation and may not be counted toward a keep; it is reported
separately and labelled as the opposite pattern.

**Why.** E48's secondary registered the direction. Two of the four pairs returned **larger** than the
keep pair (−0.744 and −0.799 against +0.515) while pointing the **other way** — the digital-aligned
wage modes rise where the cash margin falls. Without the sign in the registration the natural
write-up is "three of four pairs cohere at |r| ≥ 0.30", a sentence that folds two contradictory
patterns into one claim.

## B16 — path before span

Any claim resting on a **long difference** must print the **intermediate wave levels** beside it, and
any **non-monotone** path must be stated in the claim text itself.

**Why.** Both counter-moving margins fall and then rebound — `fin31d` **47.1 → 34.1 → 20.5 → 26.6**
and `fin34c` **15.9 → 11.8 → 8.0 → 15.2**. A 2014→2024 difference reports a fall of ~14 and ~1 points
respectively and erases the reversal completely. B14 pushes the loop toward long differences; B16 is
the cost of that move and is not optional.

## B17 — the micro stream carries a quota

At least **one micro-stream (`U`) experiment every three cycles**, tracked the same way rule B2's
breadth cell is. A cycle that skips it must say so and why.

**Why.** **23 of the ledger's keeps are micro** — the most productive stream per experiment — and it
has not run since **U21 (2026-08-09)**. Meanwhile **154 micro columns in 19 families have zero
mentions**, which is the largest *reachable* untouched surface in the repo now that `con` is blocked
for want of a questionnaire. B2 forces breadth on the country side and nothing forces it here, so the
country side is where every cycle goes.

## B18 — the distillation TRIGGER (a rule, not a recommendation)

When `PAPER_DRAFT_v2.md`'s CORRECTIONS OWED block reaches **five or more items**, or when **ten or
more experiments** have run since the last distillation, **the next cycle is a distillation/rewrite
cycle and registers no new experiments.** The trigger is checked at the same point as rule B1's
coverage run, and the check is recorded in the pre-registration.

**Why.** The 2026-08-10 wrap-up recommended exactly this. Five days and eight experiments later the
draft still carried **six** known-wrong statements and the v3 rewrite had not happened. A
recommendation the loop is free to decline is not a mechanism; this one has a threshold and a
consequence.

**B18 amendment, 2026-08-16 — the trigger reads the CURRENT draft, whatever its version number.**
B18 fired on its first cycle in force (seven items against a threshold of five) and the resulting
rewrite produced `PAPER_DRAFT_v3.md`; `PAPER_DRAFT_v2.md` is marked SUPERSEDED and its corrections
block is closed and frozen. **The trigger is evaluated against the highest-numbered
`PAPER_DRAFT_v*.md` in `05_AutoResearch/`, not against the literal filename `PAPER_DRAFT_v2.md`.**
The experiment-count branch resets at each distillation: the counter runs from the last completed
rewrite (now 2026-08-16, experiment count 73).

**One thing the first firing revealed and the rule should carry.** The two branches measure different
debts. The count branch measures *volume* — how much new evidence the draft has not seen. The
corrections branch measures *known falsity* — how many statements the loop already knows are wrong
and has left standing. On 2026-08-16 the second fired at 7 while the first stood at 7 of 10, i.e. the
draft went stale by being **wrong**, not by being **behind**. A cycle that fires on the corrections
branch alone is still a full rewrite cycle; do not discount it because the experiment count is low.

## B19 — every new `findings.tsv` row carries its structured fields

The ledger schema now begins:

`id · stream · commit · status · design · windows · frame · n · neff · r_w · r_u · parent ·
claim · test · effect · gates · note`

The eight inserted fields are **mandatory on every new row**. Where a field does not apply, write
`na`; where it applies but is genuinely unknown, write `?` — **never leave it blank and never guess**.
Historical rows are backfilled mechanically where the value was recoverable from the prose and left
empty where it was not; an empty cell in a pre-2026-08-15 row means *not recovered*, not *zero*.

**Why.** The five free-text columns had grown to a median `note` of ~400 characters and a maximum of
**1,352**, ~99 KB of prose in a file whose purpose is to be queried. E40's ledger-wide audit had to
recompute all thirty-three statistics from raw frames because they could not be parsed out of the
ledger that recorded them.

## Documentation obligation 1 — `LEDGER_INDEX.md` replaces `RESEARCH_LOG.md` as required reading

`RESEARCH_LOG.md` is **449 KB / ~5,900 lines** and is listed in the run instructions as required
reading at the start of every cycle. It is not readable at that size, and cycles have in practice been
reading its tail and inferring the rest. **`LEDGER_INDEX.md` — one line per experiment, regenerated by
`python3 make_index.py` — is now the required read.** The log stays exactly as it is: the append-only
record, consulted by `grep` for a specific experiment, never front to back.

## Documentation obligation 2 — the four-way module screen is the standard first move

The mandatory mapping pass on an untouched module is followed by the **four-way orientation screen**,
not by E45's redundancy/independence pair:

`restatement` |r| ≥ 0.80 · `aligned` +0.30 ≤ r < 0.80 · `counter-moving` r ≤ −0.30 ·
`independent` |r| < 0.30 — **both lenses must agree**, else `mixed-lens` (B9/B11).

**Why.** E45 logged its own independence definition as mis-specified: written to catch *orthogonal*
items, it could not see a strongly *negative* one and discarded `fin31d_s` at −0.730. The four-way
screen was written as the fix and returned a keep on first use (E47, `fin34c` at −0.552 / −0.486).

## The status vocabulary, in one table

Previously defined across five separate amendment blocks (B4, B8, B9, B11, B13). This table is now
authoritative; where it and an earlier block disagree, this table wins.

| status | meaning | promoted by | demoted by |
|---|---|---|---|
| `keep` | threshold and all gates pass; **both lenses agree** | — (see `keep-window` for Δ claims) | failed replication, or a later audit failing a lens |
| `keep-window` | a kept Δ association on **one** transition (or one long-difference cell) | replication on every tested earlier transition, all agreeing in sign (B4 + B8) → `keep-general` | a failed replication → `discard`, or → stays `keep-window` and is recorded as *failed*, never as *not attempted* |
| `keep-general` | replicated across transitions with sign agreement | — | a later window disagreeing in sign |
| `keep-weighted` | keeps under the **population-weighted** lens only; the claim text must say so (B9) | agreement appearing under both lenses | — |
| `keep-unweighted` | keeps under the **unweighted** lens only (B11) | as above | — |
| `keep-general-unweighted` | B11 + B4: replicated across transitions, unweighted lens (B11) | — | — |
| `keep-exploratory` | the answer was peeked before registration (peek rule, 2026-07-11) | never — re-register on fresh data | — |
| `discard` | threshold or a gate fails on both lenses | — | — |
| `discard-weighted` | the two lenses **disagree** and the finding fails as registered; the lens dependence is part of the result (B9) | — | — |
| `inconclusive` | a registered **diagnostic** whose fixed verdict rule returns neither branch | — | — |

**A bare `keep` means both lenses agree.** Any status that keeps under one lens must name the lens in
the claim text, not only in the status field.

---

# Amendment (2026-08-20) — the second B18 firing, and two rules the ten intervening experiments forced

The B18 trigger fired for the second time, this time on the **count** branch: ten experiments (U22,
E49x, E49, E50, E51x, E51, E52, U23, E53, E54) had run since the 2026-08-16 rewrite, against a
corrections count of one. Output: `PAPER_DRAFT_v4.md`; v3 marked SUPERSEDED with its corrections block
closed and frozen at one item, executed. The two rules below are additive; every gate, threshold and
pre-registration rule above stands unchanged.

**A note on the trigger itself, which its first firing could not show.** B18's own amendment observed
that the two branches measure different debts — *volume* (the count branch) and *known falsity* (the
corrections branch) — and instructed the loop not to discount a corrections firing because the count
was low. The symmetric case has now occurred: this firing had corrections at 1 of 5 and the count at
10 of 10, i.e. the draft was stale by being **behind** rather than **wrong**. It was still a full
rewrite cycle, and it retired a claim the draft had made in its newest section. **Do not discount a
count firing because few corrections are owed.** In practice the count branch found more than the
corrections branch did, because a correction is only ever opened by a cycle that happens to trip over
it — E53 opened v3's one item by accident.

## B20 — hold the denominator fixed, and say what it is

**The rule.** Any claim resting on a wave path, a long difference or a Δ must state whether the
economy set is **balanced across the waves being compared**, and must be computed on a balanced set.
A path or Δ computed over "whoever reports the item in each wave" is **not admissible** as a primary,
and a claim already resting on one must be recomputed before it may be repeated. Where an item's
reporting set changes, report the count and population share of the economies that drop, and name the
largest of them.

**Why.** E53 found, by accident and while testing something else, that the four-item 2021→24 cash
rebound this project had spent three cycles calling its clearest unexplained pattern is **largely
item-level attrition**. Six economies report `fin31d` / `fin34c` / `fin42` / `fin43c` in 2021 and not
in 2024 — Algeria, China, Iran, Mauritius, Russia, Ukraine — and **all six are present in the 2024
wave** (`account_t_d` recorded for each), so this is items dropping out of a file, not economies
dropping out of a survey. China alone holds **25.9%** of the 2021 reporting population on these items
at levels of 4.5 / 1.3 / 6.2 / 1.1, and removing it lifts the 2021 trough by +5.7 / +2.3 / +1.6 /
+2.0pp. On the balanced 71-economy set the 2021→24 changes are **−0.28 / +4.77 / +0.11 / −0.42**:
three of the four items do not rebound at all. The pattern reached `PAPER_DRAFT_v3.md` §8 and the
agenda's item 7.8 before anyone checked the denominator.

**The reason this is a rule and not a caveat.** Reporting sets are **correlated across items within a
module**, so a single large drop-out makes several items appear to move together — which is exactly
the evidence a co-occurrence claim rests on. The failure mode is not "a slightly wrong number"; it is
a manufactured pattern. Note also that headline coverage is no defence: the headline set is reported
by 76–77 economies in every wave and is effectively balanced, which is precisely why every prior
cycle's habits were safe and the first narrow-item path claim was not.

**The audit this rule owes** is agenda item 8.1, now the project's highest-priority open item: no
experiment in the ledger has ever checked whether its wave-to-wave comparison held the economy set
fixed. Until that sweep runs, the size of this risk across the ledger is **unknown**, and the
limitation must be stated as unquantified rather than small.

## B21 — ASCENT DEPTH beside G6, wherever the lenses disagree

**The rule.** On any cell where the weighted and unweighted lenses give different verdicts against the
threshold, report **both** stability depths: the **fragility depth** (fewest greedy removals of large
economies driving `r_w` below the bar, economies named — the G6/B12 direction) and the **ascent
depth** (fewest greedy removals driving `r_u` **above** the bar, economies named). Neither number
alone is stability evidence.

**Why.** G6 and B12 look only at the largest economies, by construction, so the ledger has been able
to say "it survives dropping the giants" and has never been able to say anything about the small ones.
E52 computed the mirror for the first time: on the `fin31d`~`fin34c` cell, **removing Bulgaria alone**
lifts the 2021→24 unweighted r above +0.30, and Ukraine plus Bulgaria does it for 2017→21 — the two
windows that produced E50's lens split — against weighted fragility depths of 5 / 2 / 2 / 3 named
economies on the same cells. **Neither lens is the stable one**; the unweighted lens is merely
unstable in economies nobody names. E52's write-up recommended adopting this as a habit before it
became a rule; one cycle later it is a rule, because §10 of the draft could not state its
stability result honestly without it.

**A related result that closes a defence, and belongs beside this rule.** The natural reply to the
B9/B11/E40 de-weighting critique is that the weighted lens is *correctly* detecting an association
that is genuinely stronger among large economies. E52 produced an unregistered pattern consistent
with that (within-tercile `r_u` rising with population size in 4 of 4 cells, mean top-minus-bottom
+0.253); **E54 registered it fresh on the six E28/E30 rails × three windows and it failed wide** —
mean Δr **+0.047** against a +0.15 bar, positive in **9 of 18**, and, decisively, the registered
random-split null shows that splitting economies by population does **no more than splitting them at
random** (band [−0.115, +0.108], `p_perm` 0.209). **The de-weighting critique stands as written and
this defence of the weighted lens is closed.** Do not re-open it without a design that differs from
E54's in a stated way.
