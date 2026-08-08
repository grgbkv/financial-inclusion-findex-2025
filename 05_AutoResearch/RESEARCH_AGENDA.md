# Research agenda — seven programs (opened 2026-08-01)

Replaces the ad-hoc idea backlog. Each cycle picks from here, subject to the breadth rules B1–B7 in
`program_findex.md`; at least one experiment per cycle must land on an untouched coverage cell
(`python3 coverage.py`). Entries are sketches, not pre-registrations — the pre-registration is still
written into `RESEARCH_LOG.md` before the answer is computed, with the exact test and threshold.

Programs are ordered by priority. Programs 1 and 2 are debts against results already claimed;
3–7 open new ground. Column names below are verified present in the data with the wave/country
coverage shown; frames are the fixed `harness.Findex` / `micro.Micro` frames.

---

## Program 1 — Earlier wave transitions (the replication debt)

**Why.** Every country-level keep except two is 2021→2024, so under rule B4 the entire E-series is
`keep-window`. Three transitions are unused: 2011→14, 2014→17, 2017→21. The paper draft already
shows this is not a formality — over 2014→2024 total saving is flat (53.1 → 53.0) while formal
saving rises ~16pp, which is the *relabelling* signature that E27 rejected inside 2021–24.

| # | question | design |
|---|---|---|
| 1.1 | Does the mobile-money ~ formal-saving co-movement (E1, r=0.72) exist in 2014→17 and 2017→21? | E1's exact construction, three windows, same gates; report all three side by side |
| 1.2 | Same for the wage rail (E10, 0.79) and digital payments (E12, 0.37) | E10/E12 constructions across windows |
| 1.3 | Is "access converges, use diverges" (E17) a decade regularity or a 2021–24 feature? | level-at-t vs subsequent change, all four transitions, account and saving |
| 1.4 | Does the E27 accounting flip on the decade? Formal vs total vs other-method saving | E27's construction on 2014→2021 and 2014→2024; resolve whether the 2014→17 drop in `save_any_t_d` (53.1→43.6) is real or a definitional break |
| 1.5 | Is the 2021–24 saving surge unique in magnitude *within countries*, or only in aggregate? | distribution of country-level Δ by transition; share of countries above +10pp |

**Promotion rule:** each replicated keep moves from `keep-window` to `keep-general` (or is
demoted). This program is the precondition for the paper's Section 4 surviving review.

## Program 2 — Inference layer (the statistics debt)

**Why.** The ledger has no standard errors, no intervals and no multiple-testing correction across
50 tests, and population weighting concentrates most of the weight in five economies.

| # | question | design |
|---|---|---|
| 2.1 | How wide are the intervals on the headline associations? | country bootstrap (≥1,000 draws, percentile interval) for E1/E10/E12/E23/E24/E27; report Kish `neff` |
| 2.2 | How many keeps survive false-discovery control? | BH-adjusted view over the association ledger (rule B7) |
| 2.3 | How much of each result is the population weighting? | unweighted replication of every kept association, reported beside the weighted one |
| 2.4 | Are micro standard errors defensible? | check whether PSU/strata are available in the micro file; if so, design-based SEs, else document the limitation explicitly |

## Program 3 — The 13-year inequality panel (`pan_grp`)

**Why.** Six demographic slices × five waves × 117 economies, used by two experiments. This is the
largest untouched *frame* in the repo, and it converts the micro stream's 2024 snapshot into a
dynamic question. Slices: `gender`, `income`, `education`, `age_cat`, `laborforce`, `urbanicity`.

| # | question | design |
|---|---|---|
| 3.1 | Do inclusion gaps follow an inverted-U against the access level — widening while adoption is early and elite-led, narrowing at saturation? | per-country gap (advantaged − disadvantaged) in `account_t_d` vs the country's own access level, pooled across waves; test for a hump (quadratic / tercile pattern) per dimension |
| 3.2 | Which dimension's gap closed fastest over 2011→2024? | gap trajectories per slice, population-weighted, with G6 |
| 3.3 | Is the education gap in *usage* (`g20_any`) closing while the *access* gap closes, or diverging? | two-margin gap trajectories, education slice |
| 3.4 | Age: the micro stream found access absorbs only 10% of the age gap (U15). Does the age gap in access itself move at all over 13 years? | `age_cat` slice, `account_t_d` and `g20_any`, four transitions |
| 3.5 | Labour force: is the out-of-workforce gap (U13, +15.0pp in 2024) a stable structural feature or a widening one? | `laborforce` slice, all waves |
| 3.6 | Does the 2021–24 saving surge show up in *every* slice, or only the advantaged half? | `fin17a_17a1_d` by slice, 2021→2024, all six dimensions |

**Note.** The gap-vs-level design in 3.1 has a mechanical ceiling artifact (gaps must compress as the
advantaged group approaches 100%); pre-registrations must declare a scale-free variant (log-odds
gap, as E21 used) as the primary, with the pp gap as secondary.

## Program 4 — Reopening the welfare margin

**Why.** Section 6 of the paper draft rests on a single self-reported measure (`fin24aSD_ND`), and
three tests (E2, E15, E26) agree it does not move with digitalization. The financial-health items
`fh1`, `fh2`, `fh1_fh2` are available for **2021 and 2024** on ~74/71 developing economies — a second
and third welfare margin with a usable Δ — and `fh2a` for 2024. None has been touched.

| # | question | design |
|---|---|---|
| 4.1 | Do the three digitalization rails co-move with Δ financial health 2021→2024? | E26's construction with `fh1`/`fh2` as the destination; the registered comparison is against E26's +0.294 |
| 4.2 | Is the resilience null a measure artifact or a real boundary? | agreement between `fin24aSD_ND` and `fh1/fh2` changes; if they disagree, the boundary claim is measure-specific |
| 4.3 | Emergency-fund *sources* beyond savings and borrowing (`fin25*`, 14 columns, 2021+2024) | which sources gained where saving surged, extending E7/E18 |
| 4.4 | Does financial health track the saving surge itself? | Δ`fh1_fh2` ~ Δ`fin17a_17a1_d`, dev panel |

## Program 5 — Connectivity as prerequisite

**Why.** The rails story has no answer to "are these three margins just measuring internet
penetration?". `internet` (country, 2024, 77 dev economies) and `internet_use` (micro) are untouched.

| # | question | design |
|---|---|---|
| 5.1 | Is there a connectivity threshold below which digital rails do not function? | account/digital-payment/mobile-money levels vs `internet` in 2024; test for nonlinearity (tercile means, spline or piecewise), not just correlation |
| 5.2 | Do the rails survive conditioning on connectivity? | E23/E24 partials with `internet` (2024 level) added as a control — declared as a *level* control on a Δ design, with that mismatch stated |
| 5.3 | Micro: is `internet_use` the binding constraint on digital-payment use among accountholders? | the access-absorption ruler with connectivity as a third margin: unconditional → account-conditional → account-and-connectivity-conditional |
| 5.4 | Who is offline among accountholders? | demographic profile of `internet_use == 0` within `account == 1`, M2 per cell |

## Program 6 — Sequencing: does financial deepening follow a ladder?

**Why.** Rule B5 opened lagged designs. The hypothesis is that margins move in order — account →
digital payment → saving → credit → resilience — which is testable across five waves and is a
genuine theory rather than a correlation hunt.

| # | question | design |
|---|---|---|
| 6.1 | Does the *level* of account ownership at t predict subsequent growth in digital payments? | level-at-t vs Δ(t→t+1), pooled over transitions, dev panel; convergence benchmark reported alongside (a level always predicts its own subsequent change) |
| 6.2 | Digital-payment level → subsequent saving growth? | same design, one rung up the ladder |
| 6.3 | Saving level → subsequent borrowing growth? | same design |
| 6.4 | Is the ladder order *ordered* — does each rung predict the next better than it predicts rungs two away? | matrix of level-at-t vs Δ-next for all margin pairs; the pre-registered statistic is whether the diagonal dominates |
| 6.5 | Does the E5b "accounts-first" pattern (usage intensity at t → slower subsequent account growth) replicate on earlier transitions? | E5b construction, all four transitions — also settles a weak keep flagged in the paper |

## Program 7 — The consumer-protection and digital-risk module

**Why.** 133 country columns (`con1`–`con32`, 2024, 75–140 economies) and 52 micro columns, plus
`fin48*`/`fin49*` digital-risk items — the single largest untouched block in the repo, and the
natural place to look for the downside of the episode the paper documents. Cross-sectional only
(2024), so all claims are descriptive snapshots with no trend language.

| # | question | design |
|---|---|---|
| 7.1 | Does reported fraud/scam exposure scale with digital-payment penetration across countries? | country level, `con*` fraud items vs `g20_any` 2024 level; declare the exact item(s) under G3 |
| 7.2 | Who is exposed? Is fraud exposure graded like usage, or inverted? | micro, fraud items by educ / inc_q / age / gender among digital-payment users; the access-absorption ruler applied to the risk side |
| 7.3 | Does trust in providers track usage, or lag it? | `con*` trust items vs usage levels, country and micro |
| 7.4 | Are the least-educated over-represented among those who report losing money? | micro, M2 per cell, conditional on digital use |
| 7.5 | Does the fraud gradient run the *opposite* way to the usage gradient? | the sharp version of 7.2: if usage is elite-skewed but *losses* are poor-skewed, that is a first-order policy finding |

**First move in this program must be a mapping experiment**: `python3 coverage.py --module con`
prints the family with per-wave coverage, but the items are unlabelled in the country file. Identify
the items by their 2024 cross-sections and document the mapping in `HARNESS_V2_NOTES.md` before any
hypothesis is registered on them — and log that mapping pass as *exploratory* under the peek rule.

---

## Scheduling suggestion

Roughly one cycle per program on rotation, with Programs 1 and 2 interleaved every third cycle until
the replication and inference debts are paid. A cycle of three experiments that satisfies B2 might
look like: one Program 1 replication, one new-ground experiment (3–7), one prediction-stream
experiment — which is also the natural shape for keeping the paper draft honest while it grows.

---

## Addendum (2026-08-02, from the E28/E29/P24 cycle)

- **Program 1 status.** E28 paid the first instalment: E1/E10/E12 are now `keep-general` (replicated
  on 2017→2021). Still `keep-window` and owed a replication: E5b, E7, E11, E13, E14, E22, E23, E24,
  E25, E29. Agenda item 1.3 (E17 "access converges, use diverges") and 1.4 (the E27 accounting on the
  decade) are the next two with the most riding on them.
- **Program 2 status.** B6 machinery now exists inside `experiment.py` (country bootstrap + Kish
  neff) and can be lifted verbatim. The recurring number is **neff ≈ 7** on the developing panel
  whatever the nominal n — items 2.2 (BH correction, rule B7) and 2.3 (unweighted replication of
  every kept association) are now the highest-value inference items, because a 7-effective-observation
  ledger with 50 tests is exactly where FDR bites.
- **Program 5 status.** 5.1 and 5.2 are answered (E29): no connectivity floor in the 2024
  cross-section, and the rails survive conditioning on the internet level. **5.3 and 5.4 (micro
  `internet_use`) are untouched and now the better half of the program** — E29's finding that mobile
  money is nearly orthogonal to country internet penetration (r = +0.097) makes the individual-level
  question sharper, not redundant.
- **New prediction-stream candidate (from P24), registered for a later cycle:** *shrinkage-neutral*
  reliability grading — rescale `k_g = neff_g/(neff_g+m)` so its population-weighted mean equals the
  incumbent 0.1, so the CV tests the **relative** grading across basins without also cutting the
  average shrinkage. P24's grid could not separate the two and rejected on the level, not the shape.

## Addendum (2026-08-03, from the E30/E31/P25 cycle)

- **Program 1 status.** E30 paid the second instalment: **E11, E13 and E14 are now `keep-general`**
  (replicated on 2017→2021; E14 also on 2014→2017). The ledger has **six** general claims
  (E1, E10, E11, E12, E13, E14). Still `keep-window` and owed a replication: **E5b, E7, E22, E23,
  E24, E25** (E29 is unpromotable — `internet` is single-wave). Agenda items **1.3** (E17 "access
  converges, use diverges" on country levels) and **1.4** (the E27 accounting on the decade) remain
  the two with the most riding on them. Note for whoever runs 1.4: **2014→2017 has now failed to
  produce a stable sign in five of six cells across E28 and E30** — treat it as a low-power window
  and register the variance check up front rather than reading nulls there as absence.
- **Program 3 status.** E31 opened the `education`, `age_cat` and `laborforce` frames and returned a
  clean discard with a useful mechanism: **population-weighted gap trajectories are dominated by a
  handful of large economies** — on gender and education a *minority* of economies narrowed while the
  weighted mean fell 5.8–9.1pp. Any future `pan_grp` item (3.1, 3.4, 3.5, 3.6) should pre-register
  the **unweighted share of economies moving in the claimed direction** as a primary, not a
  diagnostic, alongside G6. The live sub-question E31 raises and does not answer: **why the usage
  log-odds gap widens for income and education while every access log-odds gap narrows** — 3.3 is
  now the highest-value item in this program.
- **Prediction stream — an axis is closed.** P25 (shrinkage-neutral grading, level confound removed,
  incumbent nested) rejects monotonically, as P24 did unnormalized. Combined with P22/P23 (basin
  center) and P9 (global constant), **every knob on the shrinkage operator except the basins
  themselves has been tested and none beats `k = 0.1` toward a population-weighted mean.** Do not
  register another adaptive-`k` or alternative-center variant. The remaining live direction is the
  one P16–P18 actually exploited: **more and better basins** (cross-indicator, data-driven cuts).
  A fifth-stage basin on a genuinely new axis — e.g. terciles of a *non-financial* covariate such as
  `internet` (2024-only, so unusable in features) or a pre-2021 demographic composition variable —
  is the natural next candidate, subject to the ≤2021 constraint.
- **Inference debt (Program 2) is now the most overdue item.** Kish `neff` has come in at **5.7–7.6
  in every cell of every experiment that has measured it** (E28, E29, E30, E31) across four different
  frame families. Items **2.2** (BH correction over the association ledger, rule B7) and **2.3**
  (unweighted replication of every kept association) should be the next cycle's Program-2 slot —
  with six `keep-general` claims now standing, an FDR accounting is owed before any of them reaches
  the paper draft as a regularity.


## Addendum (2026-08-05, from the E32/E33/P26 cycle)

- **Program 2 status — item 2.2 and 2.3 are PAID for the Δ→Δ family, and the answer is bracing.**
  E32 applied BH (q=0.10) and an unweighted replication to the declared sixteen-test family. Two
  results the rest of the agenda must now absorb: (i) **at Kish `neff` ≈ 7, BH rejects 0 of 16** —
  no association in the ledger's core family is defensible as "significant" once the population
  weighting's true degrees of freedom are used, versus 11 of 16 at nominal n. Every future write-up
  must report `neff` beside n and must not attach significance language to nominal n. (ii) the
  weighting **relocates rather than inflates** (median |r| change on de-weighting **+0.011**), which
  kills the simplest dismissal of the ledger but raises a new item: **`E16` is +0.198 weighted and
  +0.555 unweighted**, i.e. a *discard* that an unweighted ledger would have kept. **New item 2.5:
  re-examine the discards whose unweighted counterpart clears 0.30 (E16 the clearest case) — the
  weighting has been silently setting the keep/discard boundary in both directions.**
- **A demotion is owed. E7 (`keep-window`) fails all three lenses** — BH (p_boot 0.068), the
  unweighted replication (+0.541 → +0.283) and the E4 magnitude rule (retention 0.44, applied here
  for the first time since the rule post-dates E7). **Recommend demoting E7 to `discard` at the next
  distillation**; E13 fails the unweighted lens only and is flagged, not demoted, since its
  2017→2021 replication is independent evidence. Items 2.2/2.3 remain **open for the non-Δ→Δ
  families** (partials E5b/E23/E24, level→change E5/E9/E17, gap designs E20/E21).
- **Program 4 status — reopened and productive. E33 is the answer to 4.1, 4.2 and 4.4 in one pass**,
  and it overturns the framing of the paper's Section 6: the "rails do not reach welfare" boundary is
  a property of **`fin24aSD_ND`**, not of welfare. The `fh` family co-moves with all three rails
  (0.354–0.705) while being **nearly orthogonal to `fin24aSD_ND`** (+0.03 to +0.15). Two live
  follow-ups: **4.5 (new) — obtain the `fh1`/`fh2` questionnaire labels and settle the polarity**;
  until then no welfare *direction* may be asserted, and this is the first item owed to
  `HARNESS_V2_NOTES.md`. **4.3 (`fin25*` emergency-fund sources, 14 columns) is untouched** and is
  now the natural next step in this program. Note `fh2a` is 2024-only (level 9.5) and unusable for Δ.
- **Prediction stream — a second axis closes, and a screening rule falls out.** P26 tested basin
  **resolution** (bin count 2–6, incumbent nested). Account's CV is **single-peaked at B=3** — the
  tercile is tuned, not inherited. Saving's CV preferred B=6 by −0.060 on a **bimodal** curve and the
  holdout worsened +0.193pp: the fifth CV→holdout non-transfer. **New screening rule for this stream:
  read the SHAPE of the CV curve, not just its argmin — a thin margin at a secondary local minimum
  at `neff` ≈ 7 is noise, and should not trigger a holdout evaluation.** With adaptive `k`
  (P24/P25), basin center (P22/P23), the global constant (P9) and now resolution (P26) all closed,
  and stage-count exhausted (P19/P20/P21), **the shrinkage operator has no untested knobs left**.
  The next prediction cycle should register a **different mechanism**, not another parameter — the
  honest options are a change in the base predictor (the trend term, untouched since P2 and never
  basin-varying) or accepting the champion as final and turning the stream to characterising its
  errors.
- **B2 note for the next cycle.** `fh` is now used; still-untouched country modules include **`con`
  (133 cols, Program 7, still the largest block), `fin25`, `fin31`, `fin34`, `fin43`, `fin13`,
  `fin14`, `dig_acc`, `merchant_pay`, `borrow_any_t_d`**. The **`age_cat` frame remains at zero
  mentions**, and **2011→2014 remains the thinnest transition (1 mention)**.

## Addendum (2026-08-08, from the E34/E35/P27 cycle)

- **Program 1 status — the replication debt has hit a wall, and it is an informative one.** E35 tried
  the first replication of any *partial* and **0 of 3 promoted**. E23/E24/E25 stay `keep-window` and
  are now on record as having **failed** their promotion test, which is a stronger negative than "not
  yet attempted". The mechanism matters more than the verdict: **r(Δmobile money, Δdigital payments)
  = +0.871 in 2017→2021 versus +0.600 in 2021→2024**, so the two rails were nearly collinear in the
  earlier window and there was no independent variation left to partial. Read the rail decomposition
  as describing the window in which the rails **decoupled**, not as a general structure. **New rule
  for this program, adopted from the E35 run: every replication file must recompute the original
  window inside itself** — that is what caught a weight-join defect before any verdict was read.
  Still `keep-window` and owed a replication: **E5b, E7, E22** (E23/E24/E25 now failed, E29
  unpromotable).
- **Program 2 status — item 2.2/2.3 now paid for a second family, with a new fact.** BH at q=0.10
  over E35's six primary cells: **4/6 on p_boot, 0/6 at `neff` ≈ 7**. The E32 finding reproduces
  exactly. What is *new*: **partials are far more weighting-dependent than bivariates** — only **2/6**
  cells clear 0.30 unweighted, and E25's earlier-window cell flips sign (+0.459 → −0.055). Residualizing
  with the same weights compounds the weighting rather than neutralising it. Items 2.2/2.3 remain open
  only for the **level→change family (E5/E9/E17)** and the **gap designs (E20/E21/E31/E34)**.
- **Program 3 status — a genuine asymmetry across axes, and the highest-value open item shifts.**
  E34 opened the `age_cat` frame and returned a weak keep: the age access gap narrowed in 63.6% of
  economies over the decade, with G6 *strengthening* the effect — the mirror image of E31, where the
  weighted mean moved far but a minority of economies moved with it. More importantly, the **usage**
  age gap narrowed too (64.5%), where E31 found the income and education **usage** log-odds gaps
  *widening*. So **"access converges, use diverges" is axis-specific**: it holds where disadvantage is
  defined by *resources* and fails where it is defined by *cohort*. **New item 3.7: test the same
  two-margin split on `laborforce` and `urbanicity`** — if employment behaves like income and
  urbanicity like age, the resource/cohort dividing line is the finding. Note E34's decade result is
  an accumulation of two mild middle windows against a **widening 2021→24**; the last window deserves
  its own look before the decade claim is leaned on.
- **Prediction stream — the stream stays open on the rule, but P27 changes what "open" means.** The
  champion is **biased, not just noisy**: signed/MAE = **0.72 on saving, 0.49 on resilience**, both
  under-predicting. Against the **movement scale** (median |actual Δ|: 3.405 / 5.761 / 9.234) only
  **saving** has a MAE below the typical country's actual move; **resilience has 0.8% skill over
  persistence** after twenty-seven experiments. Account~saving signed residuals correlate **+0.624**.
  **The binding constraint on the next registration, stated up front:** the residual bias is a broad
  upward 2021-24 level shift invisible to ≤2021 history — the regime change P3 and P10 already failed
  to learn — and any correction fitted to P27's residuals is **peek-informed and inadmissible**. The
  next prediction pre-registration must name how its mechanism is estimable from ≤2021 data alone. If
  none can be named, **close the stream on the benchmark ladder**; that is now the recommended
  default rather than a fallback.
- **B2 note for the next cycle.** `age_cat` is now used. Untouched country modules unchanged and still
  led by **`con` (133 cols, Program 7)**, then `fin25`, `fin31`, `fin34`, `fin43`, `fin13`, `fin14`,
  `dig_acc`, `merchant_pay`, `borrow_any_t_d`. **2011→2014 is no longer the thinnest transition**
  (E34 used it). The thinnest *frames* are now `gender` and `urbanicity`; the largest untouched
  surface in the whole repo remains the **micro consumer-protection/digital-risk block** (`con` 52
  cols, `fin48`/`fin49` 12 cols, zero mentions).
