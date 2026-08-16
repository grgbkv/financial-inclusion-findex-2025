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
  Country modules untouched: `con` (blocked), `fin` (93 cols), `fin13`, `fin25`, `fin14`, `fin43`,
  `inactive_t_d_s`. `urbanicity` remains the only unused frame and is single-wave. Transition mention
  counts remain lopsided at 19 / 64 / 127 / **286** across 2011→14 / 14→17 / 17→21 / 21→24.
