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

## Addendum (2026-08-09, from the E36/U21/P28 cycle)

- **Program 3 — item 3.7 is answered, negatively, and the lineage cap now binds.** The
  resource/ascription dividing line does **not** hold as a two-class rule: employment's *usage* gap
  narrowed in 57.4% of economies (the registered divergence bar was < 50%), and the `gender` frame
  is a coin flip on both margins (54.5% access, 53.2% usage, both p > 0.5). What survives is an
  **ordering, not a split**: access-minus-usage asymmetry runs income +23.3pp > education +18.0 >
  laborforce +7.1 > gender +1.3 > age −0.9. **New item 3.8:** if this ordering is to become a claim,
  it needs a pre-registered *monotonicity* statistic (e.g. rank correlation of the asymmetry against
  an independent measure of how resource-linked each axis is), not five separate share tests — and
  it must take a parent other than E31, since **E31 → E34 → E36 exhausts rule B3's cap**.
  Second finding, on a frame at zero prior mentions: **`gender` is the purest big-country artifact
  in the ledger** — weighted mean Δ log-odds access −0.266 against an unweighted −0.002, with G6
  flipping the sign to +0.057. The pop-weighted gender access gap fell 10.2 → 4.6pp over 13 years;
  in the typical economy it barely moved.
- **Program 5 — the micro half is open and item 5.3 is answered.** Among accountholders the
  connectivity gap in digital-payment use is **+13.6pp**, *smaller* than the education gap
  (**+16.8pp**) on the same sample, and conditioning on `internet_use` absorbs only **22.8%** of the
  education gradient. The result that reframes the ruler: **account holding absorbs 55.5% of the
  unconditional connectivity gap** (+30.5 → +13.6pp), where it absorbs almost none of the education,
  income or age gradients. Connectivity is mostly an *access* story; the resource axes are not.
  **5.4 is answered descriptively** (offline share among accountholders: 43.6% primary-or-less vs
  2.3% tertiary; 34.6% at 65+; 22.7% rural vs 11.8% urban; sex nearly flat). **New item 5.5:** the
  within-country version of 5.3 (per-economy connectivity gaps, M2 per economy, the U19/U20 design)
  — the pooled figure could still be a composition artifact and every other ruler axis has had that
  test.
- **The prediction stream is CLOSED.** P28 (basin-level drift, the last untested knob on the base
  predictor and the mechanism P27's rule demanded) cleared both of P26's screening conditions on
  account — single-peaked <=2021 CV curve, interior minimum, +0.107pp margin — and then **worsened
  the holdout 5.014 → 5.124**. Sixth CV→holdout non-transfer, first to pass the shape screen: at
  `neff` ≈ 7 the *shape* of a CV curve is no more informative about the holdout than its argmin was.
  Champion final: **account 5.014 / resilience 6.625 / saving 6.831**, skill over persistence
  10.1% / 0.8% / 30.1%. Do not register another predictor experiment; if the stream is ever
  reopened it should be by a change to the *task* (a new target, or an earlier holdout wave), not by
  another mechanism on this one.
- **Program 7 is BLOCKED, not deferred.** The microdata zip ships no codebook and the `con*` items
  are bare numeric codes, so the mandatory mapping pass cannot be done from the repo (see
  `HARNESS_V2_NOTES.md` item 5). Until the questionnaire is obtained, the largest untouched block is
  unreachable — plan cycles as if it did not exist.
- **B2 note for the next cycle.** `gender` and `laborforce` are now used; `internet_use` is now used.
  The thinnest remaining *frame* is `urbanicity` (single-wave, so gap trajectories are impossible).
  Untouched country modules unchanged: `fin25` (emergency-fund sources, agenda 4.3, the best
  remaining new-ground target), `fin31`, `fin34`, `fin43`, `fin13`, `fin14`, `dig_acc`,
  `merchant_pay`, `borrow_any_t_d`. The untouched micro surface outside `con` is `fin22`, `fin24`,
  `fin31`, `fin34`, `fin39`, `fin43` and the payment-channel singletons.

## Addendum (2026-08-10, from the E37/E38/E39 cycle)

- **Program 6 is CLOSED, negatively, by the experiment that opened it.** E37 ran items 6.1–6.3 as
  the loop's first lagged design and no rung survives: **R1 +0.066** (interval through zero, G6
  flips the sign), **R2 +0.447** but with jackknife retention **0.28** and a **−0.434** reversal in
  2014→2017, **R3 −0.126** pooled while the three windows read **+0.295 / +0.280 / −0.742**. **Item
  6.4 (the diagonal-dominance matrix) is withdrawn, not deferred** — a 4×4 matrix of a design whose
  best cell is a five-country artifact, evaluated at `neff` ≈ 7, is a false-discovery machine. Item
  **6.5 is answered by E38** (below). Program 6 has no live items.
- **Two rules for every future pooled-transition design, both learned the hard way in E37.**
  (i) Report the **country-level** Kish `neff`, not the stacked one: three rows per economy tripled
  the row-level figure to 22.2 while the honest figure stayed at **7.5**, and the bootstrap must
  resample **countries carrying all their rows**. (ii) **Always print the per-window terms.** R3's
  pooled −0.126 was the average of a stable positive relationship and a violent negative one; the
  pooled number described neither.
- **Program 1 — the replication debt is now effectively exhausted, and mostly negatively.** E38 ran
  E5b on both earlier transitions: the partial is **−0.654 / +0.591 / −0.595**, i.e. it reverses
  between consecutive windows and reverses back, with G6 retentions of 0.41 / 0.05 / 0.05 and every
  bootstrap interval straddling zero. **E5b fails promotion and is recommended for demotion to
  `discard`.** Remaining `keep-window` and unreplicated: **E7** (already recommended for demotion by
  E32) and **E22**. With E23/E24/E25 failed (E35) and E5b failed here, the honest summary is that
  **only the six E28/E30 rail promotions ever replicated**. **New rule proposed for the next
  protocol amendment: a promotion requires EVERY tested earlier window to agree in sign, not one of
  them** — E38's promotion rule passed mechanically on a claim that reverses, and only the standing
  E4 magnitude rule stopped it.
- **A distillation is now overdue and has a concrete backlog.** Two demotions are pending and
  un-executed (**E7**, **E5b**); items 2.2/2.3 are paid for the Δ→Δ and partial families but open
  for the level→change and gap families; and E39 changes the framing the paper draft is built on.
  **The next cycle should be a distillation pass, not three new experiments.**
- **Program 1 item 1.5 is answered, and it is the cycle's keep.** E39: 2021→24 is a real
  within-country saving episode (**42.1%** of economies ≥ +10pp against a 20.8% previous best,
  largest unweighted median of the four windows, G5 ok at 1.7pp) — it survives the weighting
  critique that sank E31/E36. **But each margin peaks in a different window: account ownership
  2011→14, digital payments 2014→17 (2021→24 is digital payments' WEAKEST window, 21.1%), saving and
  borrowing 2021→24 (borrowing highest of all, 52.6%).** **New item 1.6:** rewrite the paper draft's
  Section 4 around a **balance-sheet** window rather than a digital-inclusion one, and check the
  rails claims (E1/E10/E12) against the fact that the rails themselves were **decelerating** in the
  window where they correlate best with saving.
- **Movers do not repeat, and this is now measured.** Consecutive-window Spearman of per-country
  changes is **≤ +0.07 in all ten pairs and negative in eight** (formal saving −0.413 / −0.350 /
  +0.070). Together with E37's null this is one fact: nothing observable at t predicts the size of
  the next move. It is the best available post-hoc account of why the prediction stream closed where
  it did, and it should be cited whenever anyone proposes reopening it.
- **B2 note for the next cycle.** `borrow_any_t_d` is now used and **2011→2014 is no longer thin**
  (E39). Untouched country modules: `fin25` (agenda 4.3, still the best remaining new-ground
  target), `fin31`, `fin34`, `fin43`, `fin13`, `fin14`, `dig_acc`, `merchant_pay`, plus the blocked
  `con`. **A micro design was pre-checked and abandoned before registration:** mobile-only vs
  bank-only accountholders on the untouched `merchantpay_dig` column qualifies only **5 of 77**
  economies at M2's n ≥ 100 per cell, so that column is pooled-only and badly composition-confounded
  — do not re-propose it as a within-country design.

## Addendum (2026-08-11, from the E40/E41 distillation cycle)

- **Rule B7 is PAID and Program 2 is effectively closed.** E40 ran a **ledger-wide** BH over
  **thirty-three** association tests in six blocks (Δ→Δ, partials, level→change, gap designs, the
  2024 cross-section, and the earlier-window replications), all recomputed from raw frames —
  **33/33 reproduced the r on record within 0.02**. Items 2.2 and 2.3 are now paid for **every**
  association family, not just Δ→Δ and partials. Results: **18/20 kept rows survive BH on `p_boot`**,
  and **the only two failures are E7 and E5b — exactly the two demotions that were already pending**.
  **1/33 survives at `neff`** (E22a, SSA, `neff` = 9.5, the highest in the family precisely because
  it excludes the giants) against **26/33 on nominal n**. Median `neff` **7.2** vs median nominal n
  **71**. Median de-weighting shift ledger-wide is **−0.051** — E32's "relocates rather than
  inflates" survives, now measured on six designs instead of one.
- **Item 2.5 is the live inference item and it has been upgraded from clean-up to structural.**
  E40's claim C **failed**: two ledger discards cross 0.30 on de-weighting (**E16** +0.198/+0.555,
  **E26** +0.294/+0.364), and **E41 produced a third the same day in a live test** — +0.039 weighted
  against **+0.418 unweighted**, with drop-top-5 at **+0.421**. The weighting is deciding
  keep/discard in both directions at roughly one case per handful of tests. **New rule B9** now
  requires the unweighted twin on every association keep and a `keep-weighted` status when the two
  lenses disagree. **New item 2.6:** re-examine E16 and E26 under B9 as candidate `keep-weighted`
  rows — E26 in particular, because the paper's Section 6 boundary rests on it.
- **Two demotions executed, one flag raised.** E7 and E5b are now `discard` in `findings.tsv`
  (recommended by E32 and E38, confirmed independently by E40). **E13 is flagged**: it fails the
  unweighted lens in **both** windows (+0.188 and, in its E30b replication, +0.248), so its
  `keep-general` promotion rests on the population weighting twice over. Flagged, not demoted.
- **Program 1 status — final.** The replication debt is closed. Only **E22** remains `keep-window`
  and unreplicated (E22 is a 2021→24 regional split of E1, whose parent *is* replicated). The
  honest ledger summary: **six bivariate co-movements replicated (E1/E10/E11/E12/E13/E14), one of
  them flagged; every partial and every level→change design that was tested on an earlier window
  failed.**
- **E39's balance-sheet reframing passed an out-of-sample check.** E41 inserted a margin chosen
  *after* the reframing was written — `merchant_pay`, an untouched module — into E39's table and it
  sorted with the digital rails (**26.3%** of economies gaining ≥ 10pp) rather than the balance
  sheet (saving 42.1%, borrowing 52.6%). **Item 1.6 is executed**: `PAPER_DRAFT_v2.md` now carries a
  seven-point CORRECTIONS OWED block and `EXTENSIONS_DRAFT.md` a status block; the v3 rewrite itself
  is the natural next non-experiment cycle.
- **B2 note for the next cycle.** `merchant_pay` is now used. Untouched country modules: **`fin25`**
  (emergency-fund detail — note that only `fin25e2`/`fin25e2b` have 2021 *and* 2024; the other
  twelve columns are 2024-only, so the agenda's "2021+2024" description of this family was too
  generous), `fin31` (digital-payment detail, **four waves × 77 economies — the best-covered
  untouched block left**), `fin34` (wage payment modes, four waves), `fin43` (agricultural payments,
  four waves), `fin13`/`fin14` (2024, only 27 economies), `dig_acc` (2024-only), plus the blocked
  `con`. **Caution carried from Program 7:** `fin31`/`fin34`/`fin43` are letter-suffixed items with
  no questionnaire in the repo, so any experiment on them needs the mandatory mapping pass logged as
  exploratory first — they are not as free as their wave coverage makes them look. The thinnest
  remaining *frame* is `urbanicity` (single wave).

## Addendum (2026-08-13, from the E42/E43 cycle)

- **Program 2 is CLOSED, and item 2.6 resolved in an unexpected direction.** E42 executed the B9
  re-status (**E16 and E26 → `discard-weighted`**) and then found that the substantive question
  behind it has a clean answer: the account-growth ~ formal-saving co-movement holds at
  **+0.470 / +0.361 / +0.394 / +0.555 unweighted across all four transitions**, every bootstrap
  interval excluding zero, and at **+0.431 / +0.736 / +0.641 / +0.198 weighted** — clearing 0.30 in
  three of four windows there too. **E16 was never a weak association; it was a strong one measured
  in the single window where the weighting cancels it, and P3 shows the cancellation is China
  alone** (drop China: +0.198 → +0.726; drop India: +0.273). New statuses **B11**
  (`keep-unweighted` / `keep-general-unweighted`) and **B12** (name the economy, never "five
  economies") are in `program_findex.md`. Item 2.5 is subsumed: the answer to "how much of each
  result is the weighting" is *cell-specific and sometimes one country*, which is why B12 now
  requires the leave-one-out by name.
- **The single most consequential line for the paper draft.** E40's "BH rejects 1 of 33 at
  `neff` ≈ 7" is a critique of the **population-weighted** ledger only — an unweighted correlation
  over 77 economies has `neff` = n. The corrections block in `PAPER_DRAFT_v2.md` currently states the
  `neff` problem without this qualification and should be amended in the v3 rewrite: the honest
  framing is that the repo has been reporting the typical-*person* statistic as though it answered the
  typical-*economy* question, not that its associations are undersupported across the board.
  Regional clustering remains unmodelled under either lens and is a genuine unaddressed limitation.
- **Program 3 — item 3.6 is answered and it is a `keep-window`.** E43: the 2021–24 saving surge
  reached **every** disadvantaged half (weighted Δ +7.4 to +16.0pp; 29–56% of economies delivering
  ≥+10pp to the disadvantaged group against E39's 42.1% all-adults reference), with **the young the
  only slice to out-gain its counterpart** (+16.0 vs +14.2). **New item 3.9, and it is now this
  program's highest-value one:** replicate the primary on 2017→2021 — the slice frame supports it and
  it is the only route to `keep-general` under B4.
- **A gap-design trap sprung for the second time.** E43's registered pp-gap secondary showed the
  income, education and labour-force gaps widening in roughly three economies of four, surviving G6
  *and* de-weighting; its scale-free log-odds twin showed **no systematic widening**, with income at a
  52.7% coin flip and unweighted/G6 changes turning negative. This is E21's discard reproduced on five
  axes at once. `program_findex.md` now requires the log-odds twin on every gap claim. **Anyone
  tempted to write "the surge was regressive" should read E43's diagnostic table first.**
- **B2 note for the next cycle.** The `education`, `age_cat`, `laborforce` and `gender` slice frames
  are now properly used (five dimensions in one experiment) and **2011→2014 and 2014→2017 gained a
  four-window design**. `urbanicity` remains the only untouched frame and is single-wave, so it admits
  cross-sections only. Untouched country modules are unchanged and still led by **`fin31`** (digital
  payment detail, four waves × 77 — the best-covered untouched block), then `fin25`, `fin34`, `fin43`,
  `fin13`, `fin14`, `dig_acc`, plus the blocked `con`. **All of them are letter-suffixed items with no
  questionnaire in the repo**, so each needs the mandatory exploratory mapping pass first, and
  `dig_acc` was pre-checked this cycle: it correlates **+0.963** with `g20_any` in the 2024
  cross-section, so it is close to a restatement of the digital-payment headline and is a poor
  new-ground target despite being untouched.

## Addendum (2026-08-15, from the E44/E45 cycle)

- **Program 3 — item 3.9 is answered, negatively, and E43's promotion route is closed.** E44 ran
  E43's bars verbatim on all three earlier transitions: **0/5, 0/5 and 1/5 dimensions** clear them
  against 5/5 in 2021→24, so **E43 stays `keep-window` and is now on record as having *failed* its
  promotion test**. The failure is a **magnitude** failure, declared in advance: bar (a) is nearly met
  in the earlier windows (+4.49 to +6.41pp across slices) while bar (b) — 25% of economies delivering
  ≥+10pp to the disadvantaged half — is missed everywhere (0.0–36.8% against 29.1–56.4%). E39 had
  already established 2021→24 as the largest within-country saving episode of the four; **there was no
  earlier episode of that size for the breadth question to be asked of.** No further replication of
  E43 should be registered — the answer will not change by re-asking it.
- **A frame fact for anyone planning `pan_grp` work on earlier waves:** the slice frame covers only
  **27 / 34 / 38** economies in 2011→14 / 2014→17 / 2017→21 against 55 in 2021→24, at country-level
  Kish `neff` of **4.2 / 4.6 / 4.8**. The earlier windows are thin in this frame in a way the `all`
  frame is not, and any design there should be powered accordingly.
- **New item 1.7, from E44's earlier-window table:** formal saving **declines in every slice** in
  2014→2017 (weighted Δ −3.65 to +2.35pp, unweighted medians negative in four of five). That is the
  slice-level counterpart of the `save_any_t_d` 53.1 → 43.6 drop that item 1.4 flags as possibly
  definitional. **Settling whether the 2014→17 drop is real or a definitional break is now blocking
  two items** (1.4 and any decade-scale claim on this margin) and should be the next Program-1 slot.
- **Program 7-adjacent — `fin31` is screened and the module is HALF-open (E45).** It is neither a
  `dig_acc`-style restatement (median |r_level| **0.745 wtd / 0.680 unwtd** against a 0.80 bar) nor
  cleanly independent (no item clears the independence definition). **New item 7.6, and it is the best
  new-ground target this cycle produced:** `fin31d` / `fin31d_s` are the **only country-file columns
  that move against the digital-payment headline** (−0.401 and −0.730 in 2024 levels, on both lenses,
  through G6), and `fin31d` **falls 47.1 → 26.6pp** across the decade while `g20_any` rises 34.3 →
  60.9. Structurally this reads as a **cash / non-digital residual margin** and it is the loop's first
  candidate for measuring the *retreat of cash* rather than the advance of digital payment — with the
  standing caveat that all `fin31` item meanings are inferred from levels and coverage
  (`HARNESS_V2_NOTES.md` item 6), never from a questionnaire. Four waves × 77 economies, so it
  supports Δ designs and earlier-window replication, unlike most untouched blocks.
- **A `neff` clarification that changes how results should be read, now rule-level.** E45's
  `fin31a_31b` cell has the ledger's usual `neff` = 7.2 and is simultaneously the most robust cell in
  it: weighted +0.797 vs unweighted +0.815, drop-top-5 +0.821, largest leave-one-out **Brazil at
  −0.042**. A low `neff` says the *weights* are concentrated, not that the *result* is fragile —
  contrast E42's China cell at the same `neff`. Four diagnostics, four questions.
- **B2 note for the next cycle.** `fin31` is now used (its `_s` family supports 2021→24 only; the
  unsuffixed items support all four transitions). Untouched country modules remaining: **`fin34`**
  (wage payment modes, four waves — now the best-covered untouched block), `fin43` (agricultural
  payments, four waves), `fin25` (mostly 2024-only), `fin13`/`fin14` (2024, 27 economies), `dig_acc`
  (2024-only and a near-restatement of the headline), plus the blocked `con`. The `pan_grp` slice
  frames are now used on **all four** transitions. `urbanicity` remains the only untouched frame and
  is single-wave.

## Addendum (2026-08-15b, from the E46/E47/E48 cycle)

- **Program 1 — item 1.4 is ANSWERED and item 1.7 is unblocked.** E46 ran five pre-registered
  diagnostics on the 2014→2017 `save_any_t_d` drop (53.1 → 43.6) with the verdict rule fixed in
  advance. The rule returns **inconclusive** (1 of 3 pass), but **two of the three failures are
  failures of the definitional hypothesis**: high-income economies **rose** in the same window
  (+1.65pp weighted, only 45.0% falling, against a 70% bar) under the *same* questionnaire, and the
  developing series returns to **53.0 in 2024 — 0.1pp from its 2014 value** after passing through
  43.6 and 42.4. An instrument does not un-break itself. **Treat the decade series on this margin as
  continuous; stop hedging decade-scale saving claims on a suspected definitional break.** What
  diagnostic (c) adds and no future write-up should drop: **90.2% of the drop sits in the non-formal
  residual** (Δformal −0.91pp against Δresidual −8.36pp; per economy, total falls in 62.3% but formal
  in 49.4%). Whatever happened in 2014→17 happened to saving *outside* financial institutions. The
  design cannot separate a real informal-saving contraction from a change in how non-formal channels
  were enumerated, and it should not pretend to. **Program 1 now has no live items.**
- **A frame fact worth carrying:** the **high-income panel** (`pan_all` minus `pan_dev`, 40 economies,
  `neff` 9.2 — the highest in the ledger, precisely because it excludes the giants) is now used and is
  a cheap, powerful **placebo frame** for any "did the instrument change?" question. Caveat: it holds
  only **5** economies reporting `save_any_t_d` in 2024, so it supports early-wave contrasts, not 2024
  ones.
- **Programs 7-adjacent — a second counter-moving margin, and the module screen that found it.** E47
  drew **`fin34`** (wage payment modes, 8 cols × four waves, **zero prior mentions**) and its
  registered screen **keeps**: **`fin34c` correlates −0.552 wtd / −0.486 unwtd with `g20_any`** in the
  2024 cross-section, through G6 (−0.553), largest leave-one-out **Brazil +0.096**. The screen used a
  **four-way classification** (restatement / aligned / **counter-moving** / independent, both lenses
  agreeing or else `mixed-lens`) that directly fixes the bar E45 logged as mis-specified against
  itself — **and it earned its keep on first use**: E45's independence definition would have missed
  `fin34c` exactly as it missed `fin31d_s`. **This screen is now the recommended first move on any
  untouched module**, replacing the redundancy/independence pair.
- **The orientation EMERGES, which is the part worth following.** `fin34c` vs `g20_any` by wave:
  **+0.028/−0.122 (2014) → −0.419/−0.323 (2017) → −0.690/−0.367 (2021) → −0.552/−0.486 (2024)**. It
  starts orthogonal and turns counter-moving as digital payment spreads. Both candidate cash margins
  also share an odd trajectory: a decade-long fall then a **rebound in the last window** (`fin34c`
  15.9 → 8.0 → 15.2; `fin31d` 47.1 → 20.5 → 26.6). **New item 7.8: what is the 2021→24 rebound?** It
  is common to two items in two modules and is unexplained.
- **Item 7.6 is answered in two halves, and the split is the finding.** E48's **primary is
  `discard-weighted`**: r(Δ`fin31d`, Δ`g20_any`) clears −0.30 on both lenses in **1 of 3** registered
  cells — the weighted lens would have kept 3/3 (−0.400 / −0.759 / −0.336), the unweighted 1/3
  (−0.159 / −0.352 / −0.266). **E45's counter-moving level correlation is a cross-sectional
  composition fact — cash-heavy economies are digital-poor economies — not a within-country dynamic
  one.** The **secondary keeps** (`keep-window`): the two counter-moving margins **retreat together**,
  r(Δ`fin31d`, Δ`fin34c`) = **+0.515 / +0.389** over 2014→2024, surviving BH at q = 0.10 over four
  registered pairs, with a partial controlling for Δ`g20_any` that **strengthens to +0.597 / +0.383**.
  The two digital-aligned modes run the other way (`fin34a` −0.744, `fin34b` −0.799), so all four
  items sort onto opposite sides of one axis. **New item 7.7, the promotion route for E48b:**
  replicate the `fin31d`~`fin34c` pair **per window** (2014→17, 2017→21, 2021→24) — it is currently a
  single long-difference cell.
- **A registered *direction* did real work, and this is a design lesson.** E48's secondary named the
  predicted sign in advance. `fin34a` and `fin34b` came back **larger** than the keep pair (−0.744,
  −0.799) and were **not eligible**, because they point the opposite way. Without the direction in the
  registration, the obvious write-up would have been "three of four pairs cohere at |r| ≥ 0.30" — a
  sentence that describes two contradictory patterns as one. **Every future multi-item family test
  should register the sign, not just the magnitude.**
- **B2 note for the next cycle.** `fin34` is now used, and the **high-income panel frame** is now
  used. Untouched country modules remaining: **`fin43`** (agricultural payments, four waves × 71 — now
  the best-covered untouched block and the natural next four-way screen), `fin25` (mostly 2024-only),
  `fin13`/`fin14` (2024, 27 economies), `dig_acc` (2024-only, a near-restatement), plus the blocked
  `con`. The largest untouched surface in the repo is still the **micro** side: `con` (52 cols),
  `fin48`/`fin49` (12), and `fin22`/`fin24`/`fin31`/`fin34`/`fin39`/`fin43` — **154 micro columns in
  19 families, zero mentions**, and the micro stream has not run since U21. `urbanicity` remains the
  only untouched frame and is single-wave.

---

# Cycle shape — REWRITTEN 2026-08-15c (the old one aimed a third of every run at closed programs)

**The old shape is dead and must not be used.** It read *"one Program-1 replication + one new-ground
experiment + one prediction experiment, with Programs 1 and 2 interleaved every third cycle."*
**Program 1 closed on 2026-08-15** (E46 answered its last live item, 1.4/1.7). **Program 2 closed on
2026-08-13** (E42). **The prediction stream closed at P28 on 2026-08-09.** Two of the three slots
named point at nothing.

## The current shape

| slot | what goes in it | the rule behind it |
|---|---|---|
| 1 | **an untouched-module pass**: mandatory mapping (exploratory) + the four-way orientation screen | B2 + Documentation obligation 2 |
| 2 | **a micro-stream (`U`) experiment**, at least every third cycle | **B17** |
| 3 | **a replication, promotion test, or inference pass on a standing keep** — under B14 this is now a long difference or an all-windows design, never a fresh single adjacent window | **B14**, B4/B8 |

**Before slot 1 is chosen:** run `python3 coverage.py` (B1), regenerate and read
`LEDGER_INDEX.md` (`python3 make_index.py`), and **check the B18 distillation trigger**. If the
trigger has fired, the whole cycle is a rewrite cycle and none of the three slots is used.

## Live programs, as of 2026-08-15c

- **Programs 1, 2 and 6 are CLOSED.** Do not register against them.
- **Program 3** (`pan_grp` inequality panel): items 3.1, 3.2, 3.5, 3.8 live; 3.6/3.9 closed by E44.
- **Program 4** (welfare margin): item **4.3** (`fin25` emergency-fund sources) live; **4.5** (obtain
  the `fh1`/`fh2` labels) blocked on the questionnaire.
- **Program 5** (connectivity): item **5.5** live (the within-country version of 5.3).
- **Program 7** (consumer protection): **BLOCKED** on the questionnaire. Its adjacent items **7.7**
  and **7.8**, below, are not.
- **New item 7.7** — the promotion route for E48b: replicate the `fin31d`~`fin34c` pair **per window**
  (2014→17, 2017→21, 2021→24). Currently a single long-difference cell.
- **New item 7.8** — **what is the 2021→24 rebound?** Both counter-moving margins fall for a decade
  and then turn: `fin31d` 47.1 → 34.1 → 20.5 → **26.6**, `fin34c` 15.9 → 11.8 → 8.0 → **15.2**. Common
  to two items in two modules, and unexplained.
- **New item 3.10** — the best remaining untouched *country* module is **`fin43`** (agricultural
  payments, four waves × 71). It is the natural next slot-1 four-way screen.

## The prediction stream — the ONE condition that reopens it

P28's closing rule says the stream may reopen only by a change to the **task**, never by another
mechanism on this one. The strongest available task change, and the only one currently recommended:

> **An earlier holdout wave.** Train on history ≤ 2017 and predict 2021, scoring with the same
> evaluator. The champion has been evaluated on **exactly one** holdout, so its MAEs — account
> **5.014**, resilience **6.625**, saving **6.831** — have no error bar, and nobody knows whether
> 5.014 is a property of the method or of the 2024 wave. This is estimable entirely from data the
> current rules already allow, and it is a *validation* of the closed champion rather than a new
> attempt to beat it.

Everything else stays closed. In particular, **do not** register another shrinkage-operator variant:
adaptive `k` (P24/P25), basin center (P22/P23), the global constant (P9), resolution (P26), stage
count (P19–P21) and basin drift (P28) are all tested and rejected, and there have been **six
CV→holdout non-transfers**, one of them after passing P26's shape screen.

---

## Addendum (2026-08-16, the B18 distillation cycle — no experiments)

**The cycle registered nothing.** Rule B18 fired on its first cycle in force: `PAPER_DRAFT_v2.md`
carried **seven** CORRECTIONS OWED against a threshold of five. The count branch had *not* fired
(seven experiments since the 2026-08-11 distillation, against a threshold of ten), so the draft was
stale by being **wrong**, not by being **behind**. Output: **`PAPER_DRAFT_v3.md`**, which executes all
seven corrections and folds in E42–E48; v2 marked SUPERSEDED with its corrections block frozen;
`EXTENSIONS_DRAFT.md` marked absorbed into v3; B18 amended to read the highest-numbered draft file.

- **The micro quota (B17) is UNPAID and is carried.** The micro stream has not run since **U21
  (2026-08-09)**, which is now two cycles. **The next cycle must open with a `U` experiment** — this
  is the single most binding constraint on the next run, ahead of the B2 breadth cell. The reason has
  not changed and has strengthened: the micro stream holds **14 of the ledger's 36 keeps** on 23
  experiments (a 61% keep rate against 44% country-side), and **154 micro columns in 19 families have
  zero mentions**.
- **A design-family fact the rewrite surfaced, and it belongs in the agenda rather than only in the
  paper.** Grouping the ledger by *design* rather than by topic gives base rates that no single
  experiment shows: **`level-to-change` is 0 keeps in 7 attempts**, while `micro-cross-section` is
  14/23 and `delta-delta-multi` (the all-windows design B14 now requires) is 3/4. Read the 0/7 as a
  property of the *instrument on this panel*, not of the seven hypotheses — it is the same fact as
  E39's repeat-mover null (consecutive-window Spearman ≤ +0.07 in all ten pairs, negative in eight)
  seen from the design side. **Do not register another level-to-change design without first stating
  what makes it different from the seven that failed.**
- **The distillation confirmed the agenda's live-item list is accurate.** No status changes were
  owed: the E7/E5b demotions were executed 2026-08-11, the failed promotions (E23/E24/E25, E43, E5b)
  are recorded as *failed* rather than *not attempted*, and E13's weighting flag stands. The ledger
  was in sync with itself; only the draft was behind it.
- **Live items, unchanged by this cycle:** 3.1, 3.2, 3.5, 3.8 (`pan_grp`); 4.3 (`fin25`); 5.5
  (within-country connectivity gaps — **the natural B17 micro draw for the next cycle**); 7.7
  (per-window replication of the `fin31d`~`fin34c` co-retreat); 7.8 (the unexplained 2021→24 rebound);
  3.10 (`fin43` as the next untouched-module screen). Programs 1, 2 and 6 stay closed; Program 7 stays
  blocked on the questionnaire; the prediction stream stays closed with one reopening condition (an
  earlier holdout wave).
- **A non-analytical item promoted to the top of v3's agenda, because three separate lines of work are
  blocked on it:** obtain the Findex questionnaire. It blocks the `fh1`/`fh2` polarity (Program 4),
  the `fin31`/`fin34` cash-margin labels (items 7.6–7.8, currently structural inference only), and the
  entire `con` module (Program 7, 133 country columns and 52 micro columns).
- **B2 note for the next cycle.** No new coverage was consumed — the cycle computed no outcome.
  Country modules untouched: `con` (blocked), **`fin` (93 cols — see the correction below)**,
  `fin13`, `fin25`, `fin14`, `fin43`, `inactive_t_d_s`. `urbanicity` remains the only unused frame and
  is single-wave. Transition mention counts remain lopsided at 19 / 64 / 127 / **286** across
  2011→14 / 14→17 / 17→21 / 21→24.

- **CORRECTION, same day — every B2 note since 2026-08-05 has named the wrong "best remaining
  untouched block", and this one did too until it was checked.** The notes have rotated through
  `fin25` → `fin31` → `fin34` → `fin43`, each crowned "the best-covered untouched block left", while
  the **93-column `fin` catch-all sat unopened** because the module summary lists it as one anonymous
  family and no cycle ran `coverage.py --module fin`. Opened on 2026-08-16, it contains **24 columns
  with at least three waves at ≥70 developing economies**, of which **`fin10` and `fin2_t_d` have all
  five waves × 77 economies** — better wave coverage than any indicator the ledger has ever used
  outside the headline set, and far better than `fin43` (6 cols, four waves × 71). Also present with
  usable Δ coverage: `fin30` and `fin37` (four waves × 77), the `fin37_39*` family (five columns, four
  waves), the `fin37_38*` and `fin38*` families (three waves × 77), and `fin26a` (three waves).
  **`fin10` / `fin2_t_d` are now the recommended slot-1 draw, ahead of item 3.10's `fin43`**, subject
  to the standing rule that an untouched module gets the mandatory exploratory mapping pass and the
  four-way orientation screen first — and to the standing caveat that item *meaning* is inferred from
  levels and coverage, never from a questionnaire.
  **The process lesson is the reusable part:** a module-level coverage summary hides a catch-all, and
  five consecutive cycles inherited the previous cycle's B2 note instead of re-deriving it — the same
  seeded-from-the-last-cycle failure the 2026-08-01 audit created rule B1 to stop, reappearing one
  level up in the *instrument's own summary line*. **Every cycle must run `coverage.py --module` on
  the largest untouched family before naming a target, not read the family count and move on.**

## Addendum (2026-08-17, from the U22/E49/E50 cycle)

- **Program 5 — item 5.5 is ANSWERED and the program's micro half is now closed.** U22 keeps: the
  connectivity gap in digital-payment use among accountholders has a **median of +10.62pp within
  economies, positive in 55 of 56 (98.2%)**, with a composition wedge of **+4.58pp (30.1% of the
  pooled gap)** — the largest wedge of the three ruler axes given this test (U19 22%, U20 28%) and
  still a minority of the pooled figure. U21's pooled 55.5% absorption of the connectivity gap by
  account holding becomes a **median 65.0% within economies**, so the pooled number understated the
  typical economy. **A frame fact for anyone planning micro within-country work:** M2 on *both* cells
  of a connectivity split qualifies only **56 of 140 economies holding 40.8% of accountholding
  respondents**, because the offline accountholder cell is thin wherever internet use is high. The
  qualifying set is tilted toward lower-connectivity economies and any median computed on it is a
  statement about them. The saturated cases (Kenya +0.3, Malawi +0.1, both 97–99% on both sides)
  show the gradient closing where digital payment is universal.
- **The `fin` catch-all is OPENED and it is not a source of counter-moving margins.** E49 screened
  all **24 eligible columns** (≥3 waves × ≥70 developing economies, out of 93) and returned
  **0 counter-moving, 12 aligned, 7 independent, 4 mixed-lens, 1 restatement**. `fin26a` at
  **+0.933 / +0.852** is a re-description of the digital headline and must not be used as an
  independent margin — a second `dig_acc`. `fin2_t_d` and `fin10`, the two five-wave columns the
  2026-08-16 correction recommended as the best untouched draw, are both `mixed-lens`
  restatement/aligned and both moved by **China alone**. **The consequence: `fin31d` and `fin34c`
  remain the ONLY counter-moving country-file margins in the ledger, now out of three modules
  screened identically.**
- **Three structural facts recorded in `HARNESS_V2_NOTES.md` item 9, and one is a standing rule.**
  (i) The `fin37`/`fin38`/`fin39` items **compose** — `fin37_38`, `fin37_39x`, `fin38_39x` and
  `fin37_38_39x` are intersections or unions of the base items. **Any future experiment on this
  family must pick ONE level of the composition and say which**; correlating a parent with its own
  component is exactly the redundancy trap E45 was written to catch, and this family makes it easy to
  fall into. (ii) The `a`/`b`/`c`/`d` suffixes behave consistently across all three composites (a, b
  rise and are aligned; c, d fall and are independent-to-slightly-negative), the strongest available
  structural evidence that the letters are the same four categories throughout. (iii) **`fin30` falls
  57.0 → 45.3 across the decade and is NOT counter-moving** (+0.254/+0.306) — the loop's first clean
  case separating a *declining* margin from a *counter-moving* one, and a caution against reading
  the two as the same thing.
- **Item 7.7 is ANSWERED and E48b's promotion route is closed.** E50's all-windows test gives
  weighted **+0.795 / +0.650 / +0.615** (3/3) against unweighted **+0.431 / +0.243 / +0.263** (1/3),
  so the promotion is `discard-weighted` and **E48b stays `keep-window`, recorded as FAILED**. Two
  registered observations survive the failure. It is **not a reversal** — all six lens-windows are
  positive, a magnitude failure of the 0.30 bar rather than an E5b-style sign flip. And it
  **reproduces E48's primary lens split exactly (weighted 3/3, unweighted 1/3) on a different pair of
  margins in the same two modules**, with China and India carrying it. **New item 7.9:** the cash
  margins' cell is now the ledger's clearest standing case of a *stable* weighted/unweighted
  disagreement — the same split from two designs — and it deserves a B12 leave-one-out sweep rather
  than another correlation. Do not re-register the promotion; the answer will not change.
- **Item 7.8 (the 2021→24 rebound) is UNANSWERED and gained a third instance.** `fin42` in the `fin`
  catch-all falls **24.6 → 14.7 → 10.8** and rebounds to **13.4**, the same shape as `fin31d`
  (47.1 → 20.5 → 26.6) and `fin34c` (15.9 → 8.0 → 15.2). Three items in three modules now share it.
  This is the best-supported unexplained pattern in the repo and should be the next cycle's slot-3
  or slot-1 draw.
- **B2 note for the next cycle — re-derived, not inherited.** `fin` is now used. Country modules
  still untouched: **`fin43`** (agricultural payments, 6 cols × four waves × 71 — now genuinely the
  best-covered untouched country block, and this note was checked with `coverage.py --module`
  rather than read off the family count), `fin25` (mostly 2024-only), `fin13`/`fin14` (2024,
  27 economies), plus the blocked `con`. **The largest untouched surface in the repo remains the
  micro side**: `con` (52 cols), `fin48`/`fin49` (12), and `fin22`/`fin24`/`fin31`/`fin34`/`fin39`/
  `fin43` — ~150 micro columns in 18 families, zero mentions. `urbanicity` remains the only unused
  frame and is single-wave. **B17 is PAID this cycle (U22) and next falls due in three cycles.**

## Addendum (2026-08-18, from the E51/E52 cycle)

- **`fin43` is OPENED and the counter-moving margin count stays at two.** E51's four-way screen on
  the agricultural-payments module returns **0 of 4 counter-moving** against the digital headline:
  `fin43a` +0.370/+0.492 and `fin43b` +0.431/+0.391 are `aligned`, `fin43c` −0.146/−0.234 and
  `fin43d` −0.023/−0.135 are `independent`. **Four modules have now been screened with the same
  instrument (`fin31`, `fin34`, `fin`, `fin43`) and `fin31d` and `fin34c` are still the only
  counter-moving country-file margins in the ledger.** `fin43` was the best remaining prior for a
  third — payments in the part of the economy where cash persists longest — so the two-margin count
  is now hard to read as a sampling accident.
- **NEW ITEM 7.10 — the anchor split on `fin43c`, the loop's best-specified unregistered lead.**
  `fin43c` is *independent* of `g20_any` (−0.146/−0.234) and **counter-moving with `account_t_d` on
  both lenses** (−0.389 / −0.322, G6 −0.273, CI [−0.653, +0.035]). That is the **mirror image of
  `fin34c`**, which counter-moves with digital payment and not with access. E51's secondary carried
  no registered bar and the interval includes zero, so this is a **lead, not a finding**. The
  registered version is a primary against `account_t_d` with a Δ design or a long difference — note
  `fin43c` carries four waves — and it should say in advance which anchor a "cash margin" is supposed
  to run against, because the two known cases disagree.
- **`_s` columns are CONDITIONAL versions and must never share a correlation with their base item.**
  `fin43c` 8.8% of adults vs `fin43c_s` 77.8% on 30 economies; `fin43b` 2.2% vs `fin43b_s` 46.8% on 3.
  Recorded as `HARNESS_V2_NOTES.md` item 10. All `_s` columns in the country file are unusable on
  coverage grounds anyway (2–52 economies).
- **Item 7.9 is ANSWERED and the answer is "neither mechanism", which is itself the result.** E52's
  weight-structure sweep on the `fin31d`~`fin34c` cell returns **INCONCLUSIVE** under its registered
  rule. **Leverage is rejected 0/4**: winsorizing the weights at the 90th percentile lifts `neff`
  from 7.2 to ~32 and leaves r_w at **+0.591 / +0.466 / +0.418 / +0.476**; even a median cap
  (`neff` ≈ 60) gives +0.468 / +0.294 / +0.292 / +0.403. **The binary heterogeneity pattern fires
  only 2/4**, and it fails because the *bottom* population tercile also clears +0.30 in two cells,
  not because the top fails — the top tercile clears the bar in **4 of 4**.
- **NEW ITEM 2.1b (inference layer) — the graded size gradient, and it must be registered fresh.**
  E52's within-tercile unweighted r rises with population size in **4 of 4 cells** (mean
  top-minus-bottom **+0.253**, monotone across all three terciles in 3 of 4). This is the natural
  registered form of the heterogeneity hypothesis and **E52 cannot claim it, having looked first**.
  A clean registration would test the gradient on a *different* cell — the six bivariate rails
  (E28/E30) are the obvious candidates and would say whether population-graded association strength
  is a property of this cash cell or of the ledger.
- **NEW ITEM 2.2b — ASCENT DEPTH belongs beside G6 in every write-up.** E52's mirror statistic to
  fragility depth shows the **unweighted** verdict on this cell is decided by one or two *small*
  economies: **removing Bulgaria alone lifts the 2021→24 unweighted r above +0.30**, and Ukraine plus
  Bulgaria does it for 2017→21 — exactly the two windows that produced E50's lens split. Fragility
  depth on the weighted side is 5 / 2 / 2 / 3 named economies. **G6 and B12 look only at the largest
  economies by construction, so the ledger has been reporting one-sided stability evidence.** The
  cheap fix is to report both depths on any cell where the lenses disagree; the loop should adopt it
  as a reporting habit before it becomes a rule.
- **Item 7.8 (the 2021→24 rebound) gains a FOURTH instance and is now the repo's clearest unexplained
  pattern.** `fin43c` runs 21.5 → 10.7 → 6.6 → **8.8**, joining `fin31d` (47.1 → 20.5 → 26.6),
  `fin34c` (15.9 → 8.0 → 15.2) and `fin42` (24.6 → 10.8 → 13.4). Four items, four modules, all
  cash-side, all rebounding in the same window. It still needs a **B14-compliant primary that is not
  another adjacent-window Δ→Δ**; the most promising shape is a *distribution* design in E39's mould
  (is the rebound within-country or compositional?) crossed with cross-item co-occurrence, since
  single-item mean reversion explains a V-shape but not four V-shapes in the same window.
- **B2 note for the next cycle — re-derived.** The country file is now **69/429 columns (16%)**
  touched (`coverage.py` counts all six `fin43` columns, the two unusable `_s` ones included). **Every untouched country family that clears the eligibility floor is gone**: what remains
  is `con` (133 cols, 2024-only, blocked for want of a questionnaire), `fin25` (14, mostly 2024-only),
  `fin13`/`fin14` (38 cols, 2024, 27 economies). **The B2 breadth cell therefore has to move to the
  micro side or to the frames**: 112 untouched micro columns in 17 families, and `urbanicity` remains
  the only untouched country frame (single-wave). **B17 falls due in two cycles and the next cycle
  should pay it early**, since micro is now also where B2 has to point.

## Addendum (2026-08-19, from the U23/E53/E54 cycle)

- **ITEM 7.8 IS OVERTURNED AND MUST BE REWRITTEN — the aggregate four-item cash rebound is largely
  ITEM-LEVEL ATTRITION.** E53's registered Secondary A/B, plus one labelled diagnostic, show that the
  paths this agenda has been quoting are computed over whoever reports the item in each wave. **Six
  economies report `fin31d`/`fin34c`/`fin42`/`fin43c` in 2021 and not in 2024 — Algeria, China, Iran,
  Mauritius, Russia, Ukraine — and all six ARE in the 2024 wave** (`account_t_d` present for each).
  On the balanced 71-economy set the 2021→24 changes are **−0.28 / +4.77 / +0.11 / −0.42**: three of
  the four items do not rebound at all, and **unweighted all four are flat or still falling**. The
  share of economies whose 2021→24 change is positive is **39.4 / 42.3 / 46.5 / 47.9%** — under half
  on every item, median change negative on all four. **China alone holds 25.9% of the 2021 reporting
  population on these items at levels 4.5 / 1.3 / 6.2 / 1.1; dropping China lifts the 2021 trough by
  +5.7 / +2.3 / +1.6 / +2.0pp.** The rebound is China leaving the denominator. `PAPER_DRAFT_v3.md`
  now carries this as its first CORRECTIONS OWED item (count 1 of 5).
- **What replaces item 7.8: a MINORITY within-country V-cluster, and it is real.** 10 of 71 economies
  carry the fall-then-rebound on **≥3 of the 4** items — **2.11×** an independence permutation null,
  above its p97.5, `p_perm` 0.003, bootstrap CI [7.0%, 22.5%]. Named: **Bulgaria, Congo Rep.,
  Dominican Republic, India, Madagascar, Philippines, Sri Lanka, Thailand, Uganda, Viet Nam.** The
  keep is **margin-dependent** (the two-part bar fires at the registered 1pp margin, not at 0 or 2pp,
  though direction and `p_perm` hold at all three). The population-weighted twin is 44.2% vs a 6.8%
  null — that number is India.
- **NEW ITEM 8.1 (audit, high priority) — how much of the ledger rests on item-level attrition
  between 2021 and 2024?** E53 found a six-economy, China-led attrition pattern on four cash-side
  items by accident. **No experiment in the ledger has ever checked whether its wave-to-wave
  comparison holds the economy set fixed.** The registered form is a ledger-wide sweep: for every
  column used in a Δ or path claim, the count and population share of economies reporting at t and
  not at t+1, and the aggregate difference between the unbalanced and balanced series. This is
  cheap, mechanical, and it is the natural successor to E40's BH/de-weighting audit.
- **ITEM 2.1b IS ANSWERED: NO.** E54 registered E52's size gradient fresh on the six E28/E30 rails ×
  three windows and it fails wide — mean Δr **+0.047** against a +0.15 bar, positive in **9 of 18**,
  monotone in 3 of 18, bootstrap CI [−0.074, +0.162]. The registered random-split null is decisive:
  splitting economies by population does **no more** than splitting them at random (null band
  [−0.115, +0.108], `p_perm` 0.209). **The ledger's weighted/unweighted disagreements therefore
  cannot be reread as the weighted lens correctly detecting a stronger association among large
  economies; the B9/B11/E40 de-weighting critique stands as written.**
- **NEW ITEM 2.1c (a lead, explicitly unregistered).** E54's window means are 2014→17 **−0.113**
  (2/6 rails positive), 2017→21 **+0.014** (2/6), 2021→24 **+0.240** (**5 of 6**). The size gradient
  is visible only in the most recent window — the window E52's cash cell spans. It has no
  multiplicity control and is a subset of a failed primary. A fresh registration must name the
  window in advance and should say why 2021→24 would differ.
- **PROGRAM 7's MICRO HALF IS OPEN and the country half is confirmed permanently blocked.** U23
  opened three untouched micro columns — `receive_pensions`, `receive_agriculture`, `pay_utilities` —
  and keeps: the last-mile education gradient in digital payment *mode* holds in **all three**
  (**+6.51 / +14.16 / +26.07pp**, all intervals excluding zero), so it is a property of the adult and
  not of one payer. The `con` module was re-checked this cycle and stays blocked: no questionnaire
  ships with either file and the column names are opaque, so **no `con` claim can be worded**, at
  either level. `domestic_remittances` is blocked on the same grounds — its four codes do not match
  the payment-stream family (code 4 has account 0.942 but anydigpayment 0.481).
- **NEW ITEM 7.11 — the payer-set / self-directed split in access absorption, the cycle's most
  suggestive unregistered pattern.** Account holding absorbs **69.0%** of the education gradient in
  the **pension** stream (an institution pays), **49.4%** in agriculture, and only **30.3%** in
  utilities and **30.9%** in wages. The ruler's standing ~64% figure (U10/U19) is reproduced almost
  exactly by the one stream where the payer is a public institution and missed by half where it is
  not. The registered secondary that produced it cleared its bar by **0.6pp** and is a coin flip; the
  *pattern across streams* is what deserves a fresh registration, with the ordering named in advance.
- **A FRAME FACT for micro within-country work, alongside U22's.** The within-economy composition
  check is **unrunnable** for pensions and agriculture: **zero** economies reach 100 unweighted
  respondents in both education cells. Those two streams are pooled-only and unverified on
  composition. `pay_utilities` qualifies 8 economies (14.4% of participants) with a composition wedge
  of **+3.91pp (11%)** — the smallest of any axis measured this way (U19 22%, U20 28%, U22 30%).
- **B2 note for the next cycle — re-derived.** Country file **69/429 (16%)**, unchanged: E53 and E54
  reused touched columns and bought their breadth in *design*. Micro **48/192 (25%)** after U23. The
  reachable untouched micro surface is now `fin22` (9, borrowing sources), `fin24`/`fin25e` (11,
  emergency funds — the country-side twin is also untouched), `fin13`/`fin14` (13, 36 economies),
  `fin39` (4, utility-payment detail), `fin48`/`fin49` (12, digital-risk exposure, 8,037 respondents
  in 82 economies — a split-sample module, check the weights before registering), plus `fin32`/
  `fin33`/`dig_account`. `urbanicity` remains the only untouched country frame and is single-wave.
  **B17 is PAID this cycle (U23) and next falls due in three cycles.**

## Addendum (2026-08-20, the second B18 distillation cycle — no experiments)

**The cycle registered nothing.** Rule B18 fired on the **count** branch: ten experiments (U22, E49x,
E49, E50, E51x, E51, E52, U23, E53, E54) since the 2026-08-16 rewrite, against a corrections count of
**1 of 5**. This is the mirror of the first firing (corrections 7, count 7 of 10): v3 was stale by
being **behind**, not by being **wrong**. It was still a full rewrite, and it retired a claim v3 made
in its newest section. Output: **`PAPER_DRAFT_v4.md`**; v3 SUPERSEDED with its corrections block
closed and frozen at one item, executed; two new rules **B20** and **B21** in `program_findex.md`.

- **What the rewrite changed, and it is one section.** §8 (the cash side) is rebuilt in full from four
  experiments. v3's "both margins fall for a decade and then rebound" is **deleted**; the section now
  carries the four-module screen base rate (2 counter-moving margins from `fin31`, `fin34`, `fin`,
  `fin43`), E48b's **failed** per-window promotion (weighted 3/3, unweighted 1/3, reproducing E48a's
  split exactly), E52's audit rejecting both leverage and binary heterogeneity, and E53's attrition
  correction with the surviving minority V-cluster. §9 gains U22's connectivity axis and U23's
  four-stream last-mile gradient; §10 gains E54's rejection of the population-gradient defence and
  E52's ascent-depth symmetry; §13's items 2, 3 and 6 are **closed** by that evidence.
- **NEW RULE B20 — hold the denominator fixed.** Any path, long difference or Δ must be computed on a
  **balanced** economy set and must say so; an unbalanced one is not admissible as a primary. Reason:
  reporting sets are correlated across items within a module, so one large drop-out manufactures
  apparent co-movement — which is the evidence a co-occurrence claim rests on. Headline coverage
  (76–77 economies every wave) is why every prior cycle's habits were safe and the first narrow-item
  path claim was not.
- **NEW RULE B21 — ascent depth beside G6.** Wherever the lenses disagree, report both the fragility
  depth (large economies, the G6/B12 direction) and the ascent depth (small economies, the mirror).
  E52 recommended this as a habit one cycle ago; it is a rule now because §10 could not state its
  stability result honestly without it. **Neither lens is the stable one.**
- **ITEM 2.1b's answer is now load-bearing and the defence it closes should not be reopened.** E54's
  random-split null (`p_perm` 0.209) is recorded in B21's block: the weighted lens is not correctly
  detecting stronger association among large economies. Item **2.1c** (the 2021→24-only window mean of
  +0.240, 5 of 6 rails) survives as a lead with the window to be named in advance.
- **ITEM 8.1 IS THE PROJECT'S HIGHEST-PRIORITY OPEN ITEM**, promoted from "new, high priority" to the
  top of v4's extension agenda and named in v4 §12 as the largest known **unquantified** risk. Until
  the ledger-wide reporting-set sweep runs, nobody knows how many other Δ or path claims share E53's
  failure. Its registered form is unchanged: per column used in a Δ or path claim, the count and
  population share of economies reporting at *t* and not *t+1*, and the unbalanced-minus-balanced
  difference. It is cheap and mechanical and should be **the next cycle's slot-3 draw**.
- **Live items after this cycle.** Program 3: 3.1, 3.2, 3.5, 3.8 (`pan_grp`). Program 4: 4.3 (`fin25`
  emergency-fund sources); 4.5 blocked. Program 5: closed on the micro half (U22), country half
  unchanged. Program 7: country half **permanently blocked** (`con` re-checked 2026-08-19); micro half
  **open**. Items **7.10** (the `fin43c` anchor split — v4 §8.5 states the anchor question the
  registration must answer), **7.11** (the payer-set ordering in access absorption, 69% institutional
  vs ~30% self-directed, from a secondary that cleared by 0.6pp), **2.1c**, **8.1**, **3.10** closed by
  E51. Items **7.7** (closed, failed) and **7.8** (**RETIRED** — the premise was wrong; what replaces
  it is E53's minority V-cluster, which has no promotion route) are struck.
- **B2 note for the next cycle — re-derived, not inherited.** No coverage consumed (no outcome
  computed): country file **70/429 (16%)**, micro **51/192 (27%)**. Untouched country families:
  `con` (133, blocked), `fin13` (30, 2024 × 27 economies), `fin25` (14, mostly 2024-only), `fin14`
  (8, 2024 × 27) — **185 columns of which 133 are blocked and the rest fail the wave-coverage floor**,
  so the country side has **no eligible untouched module left** and B2's cell must come from the micro
  file or the frames. Untouched micro: **102 columns in 10 families** — `con` (52, blocked),
  `fin22` (9, borrowing sources), `fin13` (8), `fin24` (7, emergency funds), `fin48`/`fin49` (12,
  digital-risk exposure — a split-sample module, check the weights first), `fin14` (5), `fin25` (4),
  `fin39` (4, utility-payment detail), `dig_account` (1). `urbanicity` remains the only untouched
  country frame and is single-wave. **B17 was paid 2026-08-19 (U23) and next falls due in two
  cycles**; this skip carries no micro debt, unlike the 2026-08-16 firing.

## Addendum (2026-08-21, from the U24x/U24/E55 cycle)

- **ITEM 8.1 IS ANSWERED, and the answer is "one window, not the whole ledger".** E55's registered
  localization claim is **REJECTED at Branch 3** on its own bars — (b) 19 of 137 cells at ≥2pp =
  **13.9%** against a <10% bar, and (c) **8 keep-backing cells** against a bar of zero — but the
  shape of the failure is the usable result. Cells above 2pp by transition: 2011→14 **0/6**, 2014→17
  **2/33**, 2017→21 **1/43**, 2021→24 **16/55 (29.1%)**. Median |discrepancy| is **exactly 0.000pp**
  in the three earlier windows and 0.534pp in 2021→24; **78 of 137 cells (56.9%) are perfectly
  balanced**. The registered mechanism check fires at **38 of 40 (95.0%)**: the discrepancy's sign
  follows `sign(retained − dropped)` at *t*, so the bias is predictable from the drop, not random.
- **TWO NEW CORRECTIONS OWED in `PAPER_DRAFT_v4.md` (its corrections branch now reads 2 of 5).**
  `fin32_acc` — **E10's wage rail, a `keep-general`** — reads **−3.21pp** unbalanced and **+4.40pp**
  balanced over 2021→24 (discrepancy −7.61, the largest non-`_s` figure in the audit). The entire
  `fh` family — **E33's second welfare margin** — flips the same way (`fh1` −1.40 → +1.81, `fh2`
  −0.67 → +2.72, `fh1_fh2` −0.85 → +2.70). **E53 had touched neither.** The associations themselves
  are Δ→Δ and balanced by construction; what is wrong is any statement about the **aggregate
  direction** of these margins in 2021→24.
- **NEW ITEM 8.2 — the 2021→24 six-economy item block, now the best-specified open question on the
  country side.** Five or six economies holding **31.7–32.3%** of the *t* reporting population drop
  out of the narrow-item block between 2021 and 2024 while remaining in the wave, China alone at
  **26.4–27.2%**. E53 named them on four cash items; E55 shows the same block hitting `fin32_acc`,
  `fin31a`, `fin34a`, `fin30`, `fin32`, `fin31a_31b` and the three `fh` columns. The registered
  question is whether the affected columns share a **questionnaire module** or a **country-file
  release rule**, since a single cause would let every affected claim be corrected at once rather
  than one at a time.
- **NEW ITEM 8.3 — SAMPLE exposure is a second, separate risk and it is now measured.** E55's
  labelled diagnostic: E12 and E11 hold 76–77 economies and 97–100% of panel adult population in
  every window, but the three **mobile-money rails (E1, E13, E14) run on 54–59 economies and 67–71%
  of the population throughout** — a coverage property of `mobileaccount_t_d`, not attrition — and
  **E10's wage rail falls from 77 economies / 100% to 71 / 69% in exactly the 2021→24 window its keep
  is measured in**. Nothing in the ledger reports the population share behind an association. The
  registered form is a standing reporting requirement, not an experiment.
- **THE MICRO EMERGENCY-FUND MODULE IS OPEN and fully identified (U24x).** The 11 columns carry
  numeric codes; they were identified by matching per-economy weighted shares against the labelled
  country file, at **median |dev| 0.000pp and max 0.000pp on 98 economies**. `fin24` is the **main
  source** of emergency funds (savings / family-friends / working / borrowing / selling assets /
  other / not possible), `fin24a` the **difficulty** follow-up, and `fin24a ∈ {2,3}` over the `fin24`
  denominator **is** the harness's `resilience` headline `fin24aSD_ND`, exactly. **This method
  generalizes**: any numerically-coded micro module with a labelled country-file twin can be opened
  the same way, which is the first crack in the wall that blocks `con`. `con` itself stays blocked —
  its country twin is unlabelled too — but the technique should be tried on `fin13`/`fin14`/`fin22`
  before those are written off.
- **U24 KEEPS and Program 4's welfare margin now has an individual-level result.** Account holding
  absorbs **56.9%** of the education gradient in digital-payment use and **8.6%** of the gradient in
  emergency-fund resilience, on the same 98-economy sample; bootstrap intervals **[+38.4%, +72.8%]**
  and **[−3.1%, +21.1%]** do not overlap, and the resilience interval contains zero. Within-country,
  the account-conditional gap is positive in **64 of 64** qualifying economies (median +20.61pp).
  The ledger's access-absorption ruler is a **usage** instrument and does not reach welfare — which
  is the country stream's E2/E15/E26 resilience null seen from the individual side.
- **NEW ITEM 4.6 — the SOURCE composition of emergency funds, the cycle's clearest unregistered
  lead.** U24x's mapping (an exploratory pass, so nothing here is claimable) shows the pooled main
  source is **family/friends 37.5%**, working 16.8%, **savings only 16.3%**, selling assets 10.9%,
  borrowing 7.4%. The registered question is whether the *source* is education- or income-graded in
  the direction the balance-sheet story predicts — savings-side up the gradient, family/friends down
  — with the **sign named per source in advance** (B15), and whether account holding absorbs the
  savings-source gradient the way it absorbs usage. `fin24b` (the second source) supports the same
  design and reproduces `fin24ba`–`bd` exactly.
- **B2 note for the next cycle — re-derived, not inherited.** Country file **70/429 (16%)**: E55
  reused touched columns by construction (its audit set *is* the touched set) and bought its breadth
  in design. Micro **62/192 (32%)** after U24x's eleven. Reachable untouched micro: `con` (52,
  blocked), `fin22` (9, borrowing sources), `fin13` (8), `fin48`/`fin49` (12, digital-risk exposure —
  split-sample, check the weights, and try U24x's country-twin matching method first), `fin14` (5),
  `fin39` (4), `dig_account` (1). `urbanicity` remains the only untouched country frame and is
  single-wave. **B17 was paid this cycle (U24) and next falls due in three cycles.**
- **B18 state after this cycle.** Corrections branch **2 of 5** (both opened by E55); count branch
  **3 of 10** (U24x, U24, E55 since the 2026-08-20 rewrite). Neither fires next cycle unless the
  next cycle opens three more corrections.

## Addendum (2026-08-22, from the U25x/U25/E56 cycle)

- **THE MOBILE-MONEY USAGE MODULE IS OPEN, and it is two blocks (U25x).** 19 code-cells identified
  against labelled country twins, **18 at median |dev| of exactly 0.000pp** on 36 economies, using
  U24x's method — which has now opened a second module and should be treated as the standard opener.
  The structural find is that **`fin13` is asked only of mobile-money HOLDERS and `fin14` only of
  NON-holders**, disjoint subsamples with **zero overlap**, a fact the country file's column names do
  not carry. `fin13a`/`b`/`c` are four-level frequency partitions; `fin13d` and `fin14e` have no
  country twin and remain unidentified. Any future use of either block is conditional and must say so.
- **NEW ITEM 9.1 — the DENOMINATOR trap, the cycle's most transferable result (U25).** Aggregating a
  conditionally-asked micro block to the population denominator its country twin uses gives
  *penetration × conditional rate*, so a screen run on it measures **penetration**. U25's two
  counter-moving items (**−0.611/−0.760** and **−0.685/−0.744**, both G6-stable with bootstrap
  intervals excluding zero) collapse to **−0.073/−0.322** and **−0.245/−0.247** on their own
  denominator, while the complement factor alone reproduces the anchor at **−0.903/−0.938**. Nine of
  19 items restate `mobileaccount_t_d` at |r| ≥ 0.80 on the same denominator. **Registered form: a
  standing addition to the four-way screen** — run it on the block's own denominator and report the
  complement factor's own correlation beside any negative classification.
- **NEW ITEM 9.2 — the existential bar needs a family-wise correction, and it bites.** The four-way
  screen's keep condition is *at least one item in the module*, which is a multiplicity design. U25's
  sole conditional-denominator survivor (`fin14d`, −0.556/−0.396, G6 −0.515, CI [−0.759, −0.150])
  **fails BH at q = 0.10 over its own 19-test family — BH rejects 0 of 19**. The five modules screened
  to date (`fin31`, `fin34`, `fin`, `fin43`, `fin13`/`fin14`) have never carried one. **Registered
  form: BH over the module's own family is part of the screen, declared in the pre-registration.**
- **ITEM 8.2 ANSWERED in substance, registered bar FAILED (E56).** The 2021→24 dropout is **one
  six-economy release block** — Algeria, China, Iran, Mauritius, Russia, Ukraine, **31.4%** of
  developing-panel adult population, **all six present in the 2024 wave** — spanning **ten column
  families across the payments section**, not one questionnaire module. 55 of 78 non-trivially-
  dropping columns (**70.5%**) share it exactly against an 80% bar → **discard**. Among the **63
  usable** columns there are only **three distinct dropper sets** and the figure is **87.3%**.
- **NEW ITEM 8.4 — `_s` columns in audit denominators, opened by E56's own failure.** E56's verdict
  turns entirely on whether 13 documented-unusable `_s` columns belong in the denominator.
  `HARNESS_V2_NOTES` item 10 already records them as unusable and no claim rests on one, but E56 did
  not declare their exclusion in advance and therefore could not take its verdict from the cut. E55
  ran the same cut and its verdict did not turn on it. **Registered form: a standing declared rule
  excluding `_s` from audit denominators**, so the choice is never available to a cycle that has
  already seen the number.
- **BOTH E55 CORRECTIONS NOW HAVE REPLACEMENT NUMBERS (E56 secondary, rule B16).** `fin32_acc`
  **8.04 → 10.35 → 12.03 → 16.43**, monotone, largest step **+4.40** in the very window the unbalanced
  series calls a −3.21pp retreat; `fh1` **+1.81**, `fh2` **+2.72**, `fh1_fh2` **+2.70**. All four
  last-window deltas sign-flip. `PAPER_DRAFT_v4.md` is annotated; **execution is owed at the next
  distillation and the corrections branch stays at 2 of 5**.
- **B2 note for the next cycle.** Country file unchanged in columns touched by claims (E56 audits the
  touched set); micro **81/192 (42%)** after U25x's 19. Reachable untouched micro: `con` (52,
  blocked), `fin22` (9), `fin48`/`fin49` (12, digital-risk — try U24x's matching method), `fin39` (4),
  `dig_account` (1), plus `fin13d`/`fin14e` which have no country twin. `urbanicity` remains the only
  untouched country frame. **B17 paid again this cycle** (U25x/U25).
- **B3 IS AT ITS CAP.** E53 → E55 → E56 is three consecutive experiments in one lineage. **The next
  cycle may not extend it** — no further descendant of E53's reporting-set line.
- **B18 state after this cycle.** Corrections branch **2 of 5** (annotated, not executed); count
  branch **6 of 10** (U24x, U24, E55, U25x, U25, E56 since the 2026-08-20 rewrite). Neither fires
  next cycle; the count branch fires the cycle after next if that cycle runs three or more.
- **DEFERRED BY BUDGET, carried forward as the strongest open micro lead: item 4.6**, the
  education/income gradient in the *source* of emergency funds (`fin24`/`fin24b`), signs named per
  source in advance.

## Addendum (2026-08-23, from the U26x/U26/U27 cycle)

- **THE REACHABLE UNTOUCHED MICRO SURFACE IS EXHAUSTED (U26x).** `fin39` (4 columns) and
  `fin48`/`fin49` (12) are open; what remains untouched is `con` (52, still blocked) and `fin22`
  (thin, 1 of 9 used). **Neither of this cycle's modules has any country-file twin**, so the
  share-matching method that opened `fin24` and `fin13`/`fin14` at median |dev| 0.000pp **could not
  run**, and both maps are structural and **not M3-validated** — a materially weaker footing that
  must travel with any future use. Structural maps are in `HARNESS_V2_NOTES` item 12.
- **NEW ITEM 10.1 — `fin48`/`fin49` is the first module the loop must declare UNUSABLE at the
  country level, and the reason generalizes.** One 12-item battery, one identical 8,037-respondent
  sample, **median 50 respondents per economy and only 23 of 82 economies at n ≥ 100**. The
  registered eligibility rule (≥ 30 economies at n ≥ 100, fixed before the run) excluded it
  mechanically. **Registered form: make that eligibility rule a standing part of the four-way
  screen**, declared in advance, so a thin block is never screened and then explained away. The
  block remains available for **pooled individual-level** description, on a sample that must be
  described as **61.1% unbanked against 26.2% in the file** — never as representative.
- **ITEM 9.1 NEEDS REWORDING, and U26 is why.** U25 found a denominator that *manufactured*
  counter-movement; U26 finds one that *suppresses* a positive association (`fin39a` +0.284/+0.482
  on its own denominator, **+0.484/+0.600** on the population denominator, `mixed-lens` → `aligned`,
  complement factor **−0.273/−0.437**), while `fin39b` is nearly denominator-invariant. **The shift
  is item-specific in size and in direction.** The standing addition to the screen should read
  *report both denominators and the complement factor*, not *the own denominator is the primary*.
- **ITEM 4.6 IS ANSWERED and the registered claim is REJECTED (U27) — but the shape of the failure
  is the usable result.** The savings source of emergency funds is education-graded at **+8.17pp**
  [+6.36, +10.16] and the substitution runs against the **distress** cells — selling assets
  **−5.74**, "not possible" **−4.68** — **not** against family and friends, which is **flat**
  (38.7% vs 39.0%, gap **−0.35pp**, CI straddling zero). All four registered signs are correct; bar
  (ii) fails and under B15 correct signs do not rescue a magnitude bar. On the **income** axis the
  same four signs hold and family/friends reaches **−4.10** — the informal-transfer substitution is
  an income phenomenon and not an education one, which is the sharpest new fact in the cycle.
- **THE ACCESS-ABSORPTION RULER NOW HAS THREE MARGINS AND A CLEAN SPLIT.** On the identical
  98-economy sample: usage (`anydigpayment`) **56.9%**, welfare (`fin24aSD_ND`) **8.6%**,
  savings-*source* composition **5.1%** with CI **[−12.3%, +29.4%]** containing zero. Two welfare-side
  margins now sit an order of magnitude below the usage margin. **NEW ITEM 4.7: the ruler is worth a
  registered fourth and fifth margin** — the natural candidates are the `fin24a` difficulty scale's
  *very difficult* cell and a borrowing-side margin — before any distillation writes the two-sided
  reading into a draft.
- **A composition-wedge benchmark worth carrying.** U27's pooled savings gap is **+7.93pp** over the
  same 88 economies whose median is **+7.84pp** — a wedge of **+0.09pp**, against U23's +3.91pp
  (11%). This is the cleanest within-country/between-country agreement the ledger has produced and
  it is the number future pooled micro claims should be compared to.
- **B2 note for the next cycle.** Micro **94/192 (49%)** after U26x's sixteen; country file
  unchanged at **98/429 (23%)**. Untouched and reachable: `fin22` (9, thin — and it HAS a labelled
  country twin, so U24x's method works there), `dig_account` (1), `fin13d`/`fin14e` (no twin).
  `con` stays blocked at both levels. **`urbanicity` is the only untouched country frame** and is
  single-wave — with the micro surface exhausted, it is the next breadth cell by default.
  **B17 paid a third consecutive cycle** (U27).
- **B3.** U26x/U26 parent **none**; U27 parent **U24**, chain length 1. The E53 → E55 → E56 chain was
  **not** extended, as its cap required.
- **B18 state after this cycle. Corrections branch 2 of 5** (still annotated, not executed).
  **Count branch 9 of 10** (U24x, U24, E55, U25x, U25, E56, U26x, U26, U27 since the 2026-08-20
  rewrite). **The next cycle fires on the count branch the moment it registers anything**, so it
  should be planned as a distillation/rewrite cycle producing `PAPER_DRAFT_v5.md` and executing
  E55's two outstanding corrections with E56's replacement numbers.
- **DEFERRED BY BUDGET, carried forward:** the **all-windows promotion test of E22** (`keep-window`,
  the mobile-money~saving-surge co-movement outside Sub-Saharan Africa), which has no descendants and
  has never been tested outside 2021→24. Under B14 it must be an all-windows design over 2014→17 /
  2017→21 / 2021→24 with sign agreement required in every window (B8).

## Addendum (2026-08-24, from the E57x/E57/E58 cycle)

- **THE `fin22` BORROWING-SOURCES MODULE IS OPEN and it produced the cycle's keep (E57x/E57).** Six
  of eleven columns are screenable under the standing eligibility rule; `fin22f` (1 wave) and
  `fin22h` (2) fail it, and `fin22a_22a1_22g_d` (declared composite / registered headline) and
  `fin22h_s` (`_s`, 8–10 economies) were excluded **before** the run. Item meanings are **not**
  established — no questionnaire — but the harness's own headline definition fixes `fin22a` and
  `fin22g` as the **formal** sources, which is enough to place `fin22d` as non-formal.
- **NEW ITEM 11.1 — the counter-moving count is THREE and the standing description is retired.**
  `fin22d` at **−0.557 / −0.400** joins `fin31d` and `fin34c`. Both of those are payment-mode items
  and this one is **liability-side**, so "the counter-moving margins are payment modes" is no longer
  the right sentence and must be removed wherever the drafts say it. It is also the **first**
  counter-moving item in six screened modules to survive **BH over its own family** (agenda 9.2),
  which is the bar that retired U25's `fin14d`.
- **NEW ITEM 11.2 — `fin22d` is the best-conditioned cell the screen has produced, and it is worth a
  Δ design.** Fragility depth **14** (against `fin22b`'s 1 and E52's 2–5 on the `fin31d`/`fin34c`
  cells), ascent depth **0**, denominator-invariant (**−0.582 / −0.534** conditional), base factor
  only **−0.261 / −0.026**, and **M3-exact** against the micro file (median and max |dev| 0.000pp on
  98 economies). E57 is a **cross-sectional composition** claim by construction and E48 is the
  standing proof that cross-section and Δ come apart. The registered next move is an **all-windows
  Δ→Δ** (B14) of `d fin22d` against `d g20_any` over 2014→17 / 2017→21 / 2021→24, with **B20's
  balanced denominator declared in advance** — `fin22` is in E56's payments block risk zone and the
  2024 reporting set is 76 against 77 earlier.
- **NEW ITEM 11.3 — E22 is DISCARDED as a promotion and its intensity sentence is retired (E58).**
  E22 stays `keep-window`. Four of six cells pass on both lenses; **both failures are 2014→2017**,
  and the regional split shows the pooled null in that window is **not** two regional stories
  cancelling. Separately, E22's declared "mobile money is the more dominant rail inside SSA" reverses
  in 2017→2021 (**SSA +0.405 vs rest +0.675**), so it is a **window** property. `PAPER_DRAFT_v4.md`
  repeats the intensity reading and the **next distillation must fix it**.
- **NEW ITEM 11.4 — the E4 magnitude rule needs one clause.** It is a ratio `|r_droptop| / |r_full|`
  and explodes near zero: E58's `rest` 2014→17 cell "passes" E4 at **11.17** on an `r_full` of
  **+0.054**. Harmless there because the 0.30 bar rejects first, but the rule reads like a stability
  test and is only meaningful **conditional on the association clearing its threshold**. Registered
  form: add that clause at the next amendment pass.
- **A `neff` fact worth carrying (E58).** The SSA subsample has `neff` **9.4–9.5 on 25–26 economies**
  while rest-of-developing has **4.8–5.0 on 28–33** — the smaller subsample has the **larger**
  effective n. Regional splits are therefore not uniformly worse-conditioned than the pooled frame,
  and the pooled `pan_dev` figure of ~7 is an average over two very different weight structures.
- **B2 note for the next cycle.** Country file **107 of 429 (25%)** after E57x's nine; micro
  unchanged at 94/192 (49%). Untouched and reachable: micro `fin22` (8 of 9 — and E57's M3 result
  means U24x's method already works there), `dig_account` (1), `fin13d`/`fin14e` (no twin). `con`
  stays blocked at both levels. **`urbanicity` is still the only untouched country frame.**
- **B17.** Not due (paid in each of the three preceding cycles) and **not paid** this cycle; the
  reachable untouched micro surface is exhausted and both strong leads were country-level. **Owed by
  the first cycle after the rewrite.**
- **B18 state after this cycle. Corrections branch 2 of 5** (still annotated, not executed).
  **Count branch 12 of 10 — OVER THRESHOLD.** The next cycle **must** be a distillation/rewrite
  cycle producing `PAPER_DRAFT_v5.md`: it executes E55's two corrections with E56's replacement
  numbers, retires the payment-mode description (11.1) and E22's intensity sentence (11.3), and
  folds in U24, U27, E53–E58.
