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
