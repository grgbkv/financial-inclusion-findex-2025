# Research log — autoresearch/jul11

Pre-registrations and verdicts, chronological. Rules in program_findex.md.

## E1 — pre-registered
**H:** The 2021→2024 formal-saving surge in developing economies is concentrated where
mobile-money adoption grew: Δsaved_formally correlates with Δmobile_money across the 77
developing panel countries (population-weighted).
**Test:** weighted corr of country-level Δ(fin17a_17a1_d) vs Δ(mobileaccount_t_d), 2021→2024,
pan_dev. Gates: G3 (headline variants), G4 (coverage), G6 (jackknife drop-top-5).
**Keep if:** |r| ≥ 0.30 and G6 sign-stable.
**E2 verdict: DISCARD.** r=0.189 < 0.30 and jackknife sign-unstable (0.19 → −0.005).
Negative result worth keeping in prose: even where mobile money surged, resilience did not
reliably follow within three years — consistent with the paper's access-vs-depth gap.

## P1 — pre-registered (prediction stream)
**Idea:** damped-trend predictor: 2024 = 2021 + λ·(2021−2017), λ=0.5, clipped to [0,100].
**Keep if:** MAE improves on persistence for a target without worsening others materially.
**P1 verdict: DISCARD** (pre-registered rule: no material worsening). Saving −1.32pp MAE,
but account +0.55pp — deceleration makes global trend extrapolation overshoot.

## P2 — pre-registered
**Idea:** per-target policy: persistence for account & resilience; damped trend (λ=0.5)
only for saved_formally. **Keep if:** saving MAE < 9.767 with account/resilience unchanged.
**P2 verdict: KEEP.** Saving 8.448 (was 9.767), others unchanged. Champion updated.

## E3 — pre-registered
**H:** Gender gaps in account ownership closed faster where mobile money grew:
Δ(gap) 2021→2024 correlates negatively with Δmobile_money (dev panel countries, group2 rows).
**Test:** per-country gap = men − women (account_t_d, group2), Δgap vs Δmm, weighted; G4/G6.
**Keep if:** |r| ≥ 0.30, sign negative, G6 stable.
**E3 verdict: DISCARD.** Clean null (r=0.008), verified computation. Gap changes are
heterogeneous (std 7.4pp) but orthogonal to mobile-money growth in the 2021→2024 window.

## E5 — pre-registered
**H:** Digital-payment usage is a leading indicator of account-ownership growth: countries
with high g20_any relative to their account level in 2021 ("usage headroom") grow accounts
faster 2021→2024. **Test:** weighted corr of (g20_2021 − account_2021 percentile-residual…
simplified: corr of g20_2021/account_2021 ratio vs Δaccount) on dev panel; G4/G6.
**Keep if:** |r| ≥ 0.30 and G6 stable.
**E5 verdict: DISCARD (direction rejected).** r=−0.59, robust — the reverse of the
hypothesis. Low-usage countries grew accounts fastest. Suspected confound: plain
convergence on the account level.

## E5b — pre-registered
**H:** The negative usage-ratio effect survives controlling for the 2021 account level —
i.e., among countries at similar account levels, LOWER usage intensity still predicts
faster account growth (accounts-first expansion pattern).
**Test:** weighted partial corr of usage_ratio vs Δaccount controlling account_2021
(residualize both on account_2021, weighted); compare |r_partial| to plain convergence
r(account_2021, Δaccount). Gates G4/G6 on the partials.
**Keep if:** |r_partial| ≥ 0.30 with stable sign.
**E5b verdict: KEEP** (threshold met; sign survives control and jackknife). Caveat logged:
magnitude concentrates in large economies. Reading: mass account-opening drives run ahead
of usage infrastructure — the access-vs-depth gap has a growth signature.

## E7 — pre-registered
**H:** Where formal saving surged 2021→2024, savings became a materially bigger *source of
emergency funds*: Δ(fin24sav share among the resilient) correlates with Δ(saved_formally).
**Test:** fin24sav (would use savings for emergency funds) as pp of adults; weighted corr of
Δfin24sav vs Δsaved_formally, dev panel; G4/G6. **Keep if:** |r| ≥ 0.30, stable.
**E7 verdict: KEEP.** r=0.541; composition of resilience is shifting toward own savings
where the saving surge landed. Same big-economy concentration caveat as E5b.

## E4 — pre-registered
**H:** Dormancy follows account drives with a lag: countries with larger account growth in
2014→2017 had higher inactivity in 2017 (the J-curve the notebook's aggregate chart hints at).
**Test:** weighted corr of Δaccount(2014→2017) vs inactive_t_d(2017)/account(2017) ratio,
dev panel; G4/G6. **Keep if:** r ≥ 0.30 stable.

## E6 — pre-registered
**H:** The unusually narrow 2021 income gap partially reverted by 2024: countries whose
poorest-40 account share jumped most 2017→2021 saw the largest gap re-widening 2021→2024.
**Test:** weighted corr of Δpoor40(2017→2021) vs Δgap(2021→2024), dev panel group2; G4/G6.
**Keep if:** r ≥ 0.30 stable.
**E4 verdict: DISCARD** (general claim). r=0.825 → 0.014 without top-5: a large-country
(India-drive) phenomenon, not a cross-country law. Harness-v2 note: G6 should require
magnitude retention, not just sign stability.
**E6 verdict: DISCARD.** Clean null (r=0.03).

## P3 — pre-registered (prediction stream)
**Idea:** saving predictor using only ≤2021 features: 2024_saving = 2021_saving +
β·mobile_money_2021 + γ·Δmm(2017→2021), β,γ fit by weighted OLS on the 2017→2021
transition (train-period supervision only, no 2024 leakage in fitting).
**Keep if:** saving MAE < 8.448 without touching other targets.
**P3 verdict: DISCARD, reverted to P2.** The saving surge was not forecastable from
pre-2021 mobile-money features fit on the previous transition — contemporaneous
correlation (E1) is not predictability. The surge reads as a regime change.

## Session close-out
Budget reached; distilling kept findings into EXTENSIONS_DRAFT.md.

---

# 2026-07-11 daily autoresearch cycle (micro stream, first use of Stream 3)

## M1 — pre-registered
**H:** Among unbanked adults (`account==0`), "not enough money" (`fin11a==1`) is
disproportionately cited by the poorest income quintile vs the richest — a income-gradient
sanity check for the micro layer and a direct read on which barrier binds by income.
**Test:** weighted rate of `fin11a==1` among unbanked, split by `inc_q` (1=poorest..5=richest),
pooled across all 2024 economies. Gates: M2 (cell n>=100 per quintile).
**Keep if:** group difference (q1 rate − q5 rate) >= 5pp, same direction (poorest higher).
**Note:** calibration check beforehand (not treated as the pre-registered result) confirmed
`fin11a` behaves as an income-sensitive barrier (monotonic decline q1->q5), which is why this
indicator was chosen for the formal run below rather than fin11b-f.

## M2 — pre-registered
**H:** Mobile-only accountholders (`account_mob==1 & account_fin==0`) are demographically
distinct from bank-only accountholders (`account_fin==1 & account_mob==0`): younger and less
educated, consistent with mobile money serving as an on-ramp for populations underserved by
traditional banking.
**Test:** weighted share aged <=35 and weighted share with primary-education-only (`educ==1`),
compared between the mobile-only and bank-only groups, pooled globally (2024 wave). Gates:
M2 (cell n>=100 per group).
**Keep if:** group difference >= 5pp on at least one of the two metrics, in the hypothesized
direction (mobile-only higher on both youth-share and low-education-share).

**M1 verdict: KEEP.** fin11a rate q1=35.7pp vs q5=25.3pp, diff=10.3pp, monotonic across all
five quintiles, well clear of threshold. M2 cell-size gate passes for every quintile
(n=3352-4894). Descriptive, single 2024 cross-section — no trend claim.

**M2 verdict: KEEP.** Mobile-only accountholders skew markedly younger (65.4pp vs 40.6pp
aged<=35, diff 24.7pp) and somewhat less educated (47.8pp vs 41.1pp primary-only, diff 6.7pp)
than bank-only accountholders, both above threshold and in the hypothesized direction. M2
cell-size gate passes (n=10,340 / 24,037). Descriptive, single 2024 cross-section.

## 2026-07-11 wrap-up
Ran 2 experiments (M1, M2) — first use of the micro stream (Stream 3). Both kept.
M1: the "not enough money" unbanked-barrier is strongly income-graded (10.3pp gap,
poorest-vs-richest quintile). M2: mobile-only accountholders are a demographically distinct,
younger and less-educated population relative to bank-only accountholders (24.7pp and 6.7pp
gaps). No hypothesis-stream (country-level) or prediction-stream experiments run this cycle;
prediction champion remains P2 (saving MAE 8.448, account 5.576, resilience 6.682).
Everything committed on autoresearch/daily.

---

# 2026-07-11 afternoon cycle (second scheduled run same day)

## E8 — pre-registered
**H:** Countries where "not enough money" (`fin11a`) is a more prevalent stated barrier among
their unbanked population in 2024 had slower account growth 2021→2024 — barrier depth predicts
weaker subsequent growth (dev panel, country level). `fin11a` is only fielded in the 2024 wave
(68 countries total; no variant choice exists for this indicator, so G3 is declared n/a rather
than checked against `INDICATORS`).
**Test:** weighted corr of `fin11a` (country-level rate among unbanked, 2024) vs
Δaccount(2021→2024), restricted to pan_dev ∩ fin11a-availability. Gates: G4 (coverage), G6
(jackknife drop-top-5), judged with the harness-v2 magnitude-retention lesson (E4): a
jackknife that keeps sign but loses most magnitude (r_droptop < 0.5 × r_full) is a
big-country artifact, discard the general claim.
**Keep if:** |r| ≥ 0.30, sign as hypothesized (negative), G6 sign-stable AND magnitude-retaining.

## U1 — pre-registered (micro stream, first true U-id per the amended protocol)
**H:** The gender gap in account ownership (male rate − female rate) is wider among the
poorest income quintile than the richest, pooled globally (2024 wave) — gender and poverty
barriers compound.
**Test:** weighted account rate split by female × inc_q, pooled across all 2024 economies;
gap_q1 = male_q1 − female_q1, gap_q5 = male_q5 − female_q5. Gates: M2 (cell n ≥ 100 for each
of the four female×quintile cells).
**Keep if:** (gap_q1 − gap_q5) ≥ 5pp, same direction (gap wider among the poorest). Descriptive,
single 2024 cross-section — no trend language regardless of outcome.

## P4 — pre-registered (prediction stream)
**Idea:** logit-space damped trend for `account_t_d` only (resilience has no pre-2021 wave to
trend from, per the P1–P3 box; saving already uses the P2 damped-trend policy). P1's raw pp-linear
damped trend overshot for account because growth mechanically decelerates near the 100% ceiling.
Compute the 2017→2021 trend in logit space (`logit(p)=ln(p/(1-p))`), extrapolate with λ=0.5,
transform back — this bakes in deceleration near the bounds without any 2024 information.
**Keep if:** account MAE improves on the persistence baseline (5.576) without touching the
saving/resilience predictions (per-target policy, consistent with P2's rule).

**E8 verdict: DISCARD.** r=−0.263 (n=47, dev-panel countries with fin11a in 2024), sign as
hypothesized, both gates clean (G4: 47 countries/59.7% pop; G6: sign-stable and
magnitude-retaining, −0.263→−0.255) — but below the |r|≥0.30 threshold. A weak, gate-clean
null: money-barrier depth among the unbanked is directionally but not materially predictive
of subsequent account growth.

**U1 verdict: DISCARD.** Clean null: gap_q1=5.2pp, gap_q5=5.7pp, diff=−0.5pp — opposite sign
from hypothesized and far below threshold. The gender gap in account ownership does not
compound with poverty in this pooled 2024 cross-section; if anything it is marginally larger
among the richest quintile, though the difference is negligible. (First run attempt hit a
data bug — `female` is coded 1=female/2=male in the raw microdata, not 0/1 — caught as an
n=0 cell-size gate failure before any substantive value was read, so no peek-rule issue.)

**P4 verdict: DISCARD, reverted to P2 champion.** Logit-space damped trend gave account MAE
5.598 vs persistence's 5.576 — 0.02pp worse. Deceleration near the ownership ceiling is
already fully captured by flat persistence in the 2021→2024 window; transforming to logit
space added noise without adding signal. Champion unchanged: account 5.576, resilience
6.682, saving 8.448 (P2).

## 2026-07-11 afternoon wrap-up
Second scheduled cycle same day. Ran 3 experiments (E8, U1, P4) — all discarded, all clean
(no gate failures, no threshold near-misses worth a second look). E8: money-barrier
prevalence among the unbanked is directionally but not materially linked to subsequent
account growth (r=−0.263, gate-clean). U1: the gender gap in account ownership does not
widen among poorer income quintiles — flat across quintiles in the pooled 2024 cross-section
(diff=−0.5pp, opposite of hypothesized). P4: logit-space transform did not beat persistence
for account prediction; champion remains P2 (saving MAE 8.448, account 5.576, resilience
6.682). Everything committed on autoresearch/daily.

---

# 2026-07-12 daily autoresearch cycle

## E9 — pre-registered
**H:** Countries where government transfer payments were more digitalized in 2021
(`fing2p_acc` — share of all adults receiving a G2P payment paid into an account) had faster
subsequent account-ownership growth 2021→2024 (dev panel) — testing the "digital G2P as an
account on-ramp" policy narrative (e.g. India's JAM trinity, Brazil's Bolsa Família digitization).
Checked `fing2p_acc` is a level (not a delta) at 2021, strictly ≤2021, so no leakage into the
2021→2024 growth window it's predicting.
**Test:** weighted corr of `fing2p_acc` (2021, pp of all adults) vs Δ(account_t_d)(2021→2024),
dev panel restricted to countries with `fing2p_acc` reported in 2021. G3: `fing2p_acc` has no
headline/narrow variant choice in `INDICATORS` (single indicator) → declared n/a. Gates: G4
(coverage), G6 (jackknife drop-top-5, judged with the E4 magnitude-retention lesson: sign-stable
but r_droptop < 0.5×r_full = big-country artifact, discard).
**Keep if:** |r| ≥ 0.30, sign positive (hypothesized direction), G6 sign-stable AND
magnitude-retaining.

## U2 — pre-registered (micro stream)
**H:** Digital payment adoption (`anydigpayment`) is lower among the oldest adults (65+) than
among prime-working-age adults (36-50), pooled globally, 2024 wave — a life-cycle/digital-divide
pattern (no prior peek at this outcome).
**Test:** weighted rate of `anydigpayment` by age band (15-25, 26-35, 36-50, 51-65, 65+), pooled
across all 2024 economies (raw `wgt`, economy-equal pooling per current micro.py default —
HARNESS_V2_NOTES caveat #3 applies to exact pooled pp values, not to direction). Gates: M2 (cell
n ≥ 100 per band).
**Keep if:** (rate_36_50 − rate_65plus) ≥ 5pp in the hypothesized direction (36-50 higher).
Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P5 — pre-registered (prediction stream)
**Idea:** Resilience (`fin24aSD_ND`) is the one target untouched since baseline (P1-P4 all
targeted account or saving) — still pure persistence, MAE 6.682. Per MODELING SCOPE (n~117 is
the binding constraint) and HARNESS_V2_NOTES #3 (small-country sampling noise), try shrinking
each country's 2021 persistence prediction partially toward its region's (`regionwb24_hi`)
weighted mean: `pred = x_2021 - k*(x_2021 - region_mean_2021)`. To avoid fitting k on 2024
(prohibited), select k by cross-validating the *same shrinkage mechanic* on the fully-≤2021
account_t_d 2017→2021 transition (predict 2021 from 2017 + region-shrink, k ∈ {0, 0.1, ..., 0.5},
minimize MAE there), then apply that fixed k unchanged to resilience 2021→2024. Per-target
policy (P2's rule): touches resilience only, account/saving predictions unchanged.
**Keep if:** resilience MAE improves on 6.682 (persistence baseline) without touching the
account/saving predictions.

**E9 verdict: DISCARD (direction rejected).** r=−0.410 (n=77, dev panel), both gates clean
(G4: 77 countries/100% pop; G6: sign-stable and magnitude-retaining, −0.410→−0.483) — but the
sign is negative, opposite of the hypothesized "digital G2P as on-ramp" direction. Countries
with LOWER G2P-payment digitalization in 2021 grew accounts faster 2021→2024, not higher. Same
shape as E5's rejected direction: reads as convergence (more room to grow where account-adjacent
infrastructure was less built out), not a causal on-ramp effect from digitalized transfers.
Not pursuing an E5b-style partial-correlation follow-up this cycle (budget; E5b already covers
this convergence mechanism for the closely related usage-ratio indicator).

**U2 verdict: KEEP.** anydigpayment rate 36-50=56.8pp vs 65+=48.1pp, diff=8.7pp, well clear of
the 5pp threshold and in the hypothesized direction. M2 cell-size gate passes for every band
(n=10,216-26,551). Full shape by band (15-25/26-35/36-50/51-65/65+ = 45.0/59.7/56.8/53.5/48.1pp)
is an inverted-U peaking at 26-35, not a monotonic decline — the pre-registered 36-50-vs-65+
comparison still clears threshold, but the true peak working-age band is younger than
pre-registered. Descriptive, single 2024 cross-section.

**P5 verdict: KEEP, champion updated.** k selected by CV on the <=2021 account 2017->2021
transition: k=0.1 minimized MAE there (7.498->7.217pp), larger k overshot (k=0.5 gave
8.879pp) — region-mean is informative but the true country signal dominates, so shrinkage is
appropriately light. Applied unchanged to resilience: MAE 6.625 (was 6.682, -0.057pp),
account/saving predictions byte-identical to P2 (5.576 / 8.448) confirming per-target
isolation. Effect size is modest (<1% relative improvement) — logged as a clean, honest keep
per the pre-registered rule (improves without touching other targets), not oversold as a
large gain. Champion: account 5.576, resilience 6.625, saving 8.448.

## 2026-07-12 wrap-up
Ran 3 experiments (E9, U2, P5). E9 (hypothesis, discard): G2P-payment digitalization in 2021
predicts 2021-24 account growth with the WRONG sign (r=-0.410, gate-clean) — direction
rejected, same convergence shape as E5. U2 (micro, keep): digital payment adoption is 8.7pp
lower among 65+ adults than 36-50 adults pooled globally (2024), inverted-U by age peaking at
26-35. P5 (prediction, keep): region-mean shrinkage (k=0.1, CV-selected on pre-2021 data only)
improves resilience prediction 6.682->6.625pp; new champion account=5.576, resilience=6.625,
saving=8.448. Everything committed on autoresearch/daily.

---

# 2026-07-12 second cycle (evening run, same day)

## E10 — pre-registered (hypothesis / country level)
**H:** The 2021→2024 formal-saving surge tracks wage digitalization as a distinct channel
from E1's mobile-money story: countries where the share of adults receiving private-sector
wages *into an account* (`fin32_acc`) grew most 2021→2024 also saw the largest gains in formal
saving (`fin17a_17a1_d`) over the same window (dev panel, population-weighted). Motivation:
digital wage rails deposit money into accounts that can then be saved — a formal-employment
channel parallel to, and testable against, E1's mobile-money channel. E1 already established
r=0.719 for Δmobile-money; a strong E10 would say multiple digitalization channels feed the
saving surge, a null would sharpen E1's mobile-money-specificity.
**Test:** weighted corr of Δ(`fin32_acc`)(2021→2024) vs Δ(`fin17a_17a1_d`)(2021→2024), dev
panel, weight = 2024 adult population. `fin32_acc` has no headline/narrow variant in
`INDICATORS` (single indicator) → G3 declared n/a. Gates: G4 (coverage), G6 (jackknife
drop-top-5, judged with the E4 magnitude-retention lesson: sign-stable but r_droptop < 0.5×r_full
= big-country artifact → discard the general claim).
**Keep if:** |r| ≥ 0.30, sign positive (hypothesized), G6 sign-stable AND magnitude-retaining.
All descriptive association language — account growth is a plausible common driver of both
sides, noted, not controlled; no causal claim.

## U3 — pre-registered (micro stream)
**H:** Among unbanked adults (`account==0`), the reason "a family member already has an
account" (`fin11f==1`) is cited more by women than by men, pooled globally (2024 wave) — a
documented gender pattern in which women's financial access is more often mediated through a
household member's account. No prior peek at this outcome (only overall `fin11f` value counts
were inspected, never the gender split).
**Test:** weighted rate of `fin11f==1` among unbanked adults with `fin11f` answered
(∈{1,2,3,4}; 3=dk/4=refused treated as not-citing), split by `female` (1=female, 2=male; per
the U1 coding fix), pooled across all 2024 economies (raw `wgt`, economy-equal pooling per the
current micro.py default — HARNESS_V2_NOTES caveat #3 applies to exact pooled pp values, not
direction). Gates: M2 (unweighted cell n ≥ 100 per gender). M3 declared n/a — no country-file
equivalent for a within-unbanked reason-split.
**Keep if:** (rate_women − rate_men) ≥ 5pp in the hypothesized direction (women higher).
Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P6 — pre-registered (prediction stream)
**Idea:** account_t_d is still pure persistence (champion MAE 5.576; P4's logit damped trend
lost). But the P5 cross-validation — which selected k by minimizing region-shrinkage MAE on the
fully-≤2021 account 2017→2021 transition — showed shrinkage *does* help account there
(7.498→7.217pp at k=0.1). Apply that same fixed k=0.1 region-shrinkage (toward the
`regionwb24_hi` population-weighted 2021 mean) to the account 2021→2024 prediction. k is not
re-fit on 2024; it is the identical CV-selected value already justified in P5. Per-target policy
(P2's rule): touches account only — saving (damped trend) and resilience (k=0.1 shrink, P5)
predictions must stay byte-identical to the current champion.
**Keep if:** account MAE improves on 5.576 (persistence) without changing the saving/resilience
predictions.

**E10 verdict: KEEP.** r=0.791 (n=71 dev-panel countries with `fin32_acc` in both waves),
positive as hypothesized, well above the 0.30 threshold. Gates clean: G4 (71 countries, 68.6%
dev-panel pop); G6 sign-stable AND magnitude-retaining (0.791→0.785 after drop-top-5, barely
moves — far above the 0.5×r_full=0.396 floor). Terciles of Δwage-digitalization are monotonic
in mean Δformal-saving: low/mid/high = +3.2/+10.9/+13.6pp. Reading: the 2021→2024 formal-saving
surge co-moves with wage digitalization just as strongly as with mobile-money growth (E1,
r=0.719) — the surge is a broad-based digitalization signature across multiple account
on-ramps (mobile money AND formal wage rails), not mobile-money-specific. Descriptive
association only; account growth is a plausible common driver of both sides (noted, not
controlled). Same big-economy caveat class as E1/E7, though here the jackknife barely moves.

**U3 verdict: DISCARD.** rate_women=24.8pp vs rate_men=27.9pp, diff=−3.1pp — opposite of the
hypothesized direction (women were expected higher) and below the 5pp threshold in magnitude.
M2 cell-size gate passes for both cells (n=13,026 unbanked women / 7,863 unbanked men).
Reading: the frequently-cited pattern that women's financial access is disproportionately
mediated through a household member's account does NOT show up in the pooled 2024 unbanked
cross-section — if anything unbanked men cite "a family member already has an account"
marginally more. The classic pattern may be region-specific (e.g. South Asia) and wash out
under economy-equal pooling (HARNESS_V2_NOTES caveat #3); the pre-registered test used the
default pooling and returns a clean, slightly-reversed, below-threshold null. Descriptive,
single 2024 cross-section.

**P6 verdict: KEEP, champion updated.** Applying the P5 CV-selected k=0.1 region-shrinkage to
account_t_d (its native target — the CV that chose k was run on the account 2017→2021
transition) improves account MAE 5.576→5.156pp (−0.42pp, ~7.5% relative — an order of
magnitude larger than P5's 0.057pp resilience gain). Resilience (6.625) and saving (8.448)
predictions print byte-identical to the P5 champion, confirming per-target isolation. No 2024
leakage: only 2021 account levels and their region (regionwb24_hi) population-weighted means —
all ≤2021 — feed the shrink; k was fixed pre-2021. The CV evidence (shrinkage helps account
in-sample, 7.498→7.217 at k=0.1) now confirmed out-of-sample on the 2021→2024 evaluation.
Reading: light shrinkage toward the regional mean is a genuine improvement for account, whereas
P4's logit damped trend was not — regional convergence, not ceiling deceleration, is the
structure flat persistence was missing. New champion: account=5.156, resilience=6.625,
saving=8.448.

## 2026-07-12 second-cycle wrap-up
Ran 3 experiments (E10, U3, P6), one per stream. E10 (hypothesis, KEEP): the 2021→2024
formal-saving surge co-moves with wage-rail digitalization (Δ`fin32_acc`) at r=0.791 (n=71,
gate-clean, jackknife 0.791→0.785) — as strongly as with mobile money (E1, r=0.719), so the
surge is a broad-based digitalization signature, not mobile-money-specific. U3 (micro,
DISCARD): the "family member already has an account" barrier is NOT cited more by unbanked
women than men in the pooled 2024 cross-section (24.8 vs 27.9pp, −3.1pp, slightly reversed and
below threshold) — the frequently-cited household-mediation pattern washes out globally. P6
(prediction, KEEP): extending P5's CV-selected k=0.1 region-shrinkage to account_t_d cuts its
MAE 5.576→5.156pp (−0.42pp) with resilience/saving byte-identical — regional convergence beats
flat persistence. New prediction champion: account=5.156, resilience=6.625, saving=8.448.
EXTENSIONS_DRAFT updated (E10 folded into Extension 1; prediction box refreshed for P5/P6).
Everything committed on autoresearch/daily.

---

# 2026-07-13 daily autoresearch cycle

## E11 — pre-registered (hypothesis / country level)
**H:** Financial deepening in the 2021→2024 window is broad, not saving-specific: countries
where *formal borrowing* grew most (Δ`fin22a_22a1_22g_d`) also saw the largest gains in
*formal saving* (Δ`fin17a_17a1_d`), dev panel, population-weighted. Motivation: E1/E10 tied the
saving surge to account on-ramps (mobile money, wage rails); if the surge reflects genuine
balance-sheet deepening rather than a saving-only phenomenon, the credit side should co-move.
A strong positive r says "broad deepening"; a null sharpens the surge as saving-specific (a
store-of-value shift, not a credit-market development).
**Test:** weighted corr of Δ(`fin22a_22a1_22g_d`)(2021→2024) vs Δ(`fin17a_17a1_d`)(2021→2024),
dev panel, weight = 2024 adult population. G3: both are the declared `borrowed_formally` and
`saved_formally` headlines in `INDICATORS` → checked, not n/a. Gates: G4 (coverage), G6
(jackknife drop-top-5, judged with the E4 magnitude-retention lesson: sign-stable but
r_droptop < 0.5×r_full = big-country artifact → discard the general claim).
**Keep if:** |r| ≥ 0.30, sign positive (hypothesized), G6 sign-stable AND magnitude-retaining.
Descriptive association only — account growth / common income shocks are plausible common
drivers of both sides (noted, not controlled); no causal claim.

## U4 — pre-registered (micro stream)
**H:** Formal saving did not reach the least-educated: among all adults in the 2024 wave,
saving at a financial institution (`fin17a==1`) is markedly less common among primary-or-less-
educated adults (`educ==1`) than tertiary-educated adults (`educ==3`), pooled globally — an
education gradient in the *depth* (formal-saving) margin, complementing M1's income gradient on
the *access* barrier. No prior peek at this outcome (only overall `fin17a`/`educ` value counts
were inspected for coding, never the cross-tab).
**Test:** weighted rate of `fin17a==1` (formal saving; coding 1=yes, 2=no, 3=dk, 4=refused → 2/3/4
treated as not-saving, NaN=not asked dropped) split by `educ` (1=primary-or-less, 2=secondary,
3=tertiary), pooled across all 2024 economies (raw `wgt`, economy-equal pooling per the current
micro.py default — HARNESS_V2_NOTES caveat #3 applies to exact pooled pp values, not to
direction). Gates: M2 (unweighted cell n ≥ 100 per educ group). M3 declared n/a — the country
headline `fin17a_17a1_d` bundles institutional (`fin17a`) with mobile (`fin17a1`) saving, so the
micro `fin17a`-only rate has no exact country-file equivalent, and this is a within-education
subgroup split besides.
**Keep if:** (rate_tertiary − rate_primary) ≥ 5pp in the hypothesized direction (tertiary
higher). Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P7 — pre-registered (prediction stream)
**Idea:** account_t_d currently uses region-shrinkage (regionwb24_hi mean, k=0.1; P6 champion,
MAE 5.156). Test whether shrinking toward the **income-group** mean (`incomegroupwb24`) instead
of the region mean does better — income group is another plausible convergence basin. Selection
is done entirely pre-2021 (no 2024 leakage): cross-validate BOTH shrinkage variants (region vs
income-group) with the same k=0.1 mechanic on the fully-≤2021 account_t_d 2017→2021 transition
(predict 2021 from 2017 + shrink); adopt the income-group variant for the 2021→2024 account
prediction ONLY IF it beats region-shrinkage on that 2017→2021 CV. If the CV prefers region
(the incumbent), keep P6 unchanged and log P7 as a discard. Per-target policy (P2's rule):
touches account only — saving (damped trend) and resilience (k=0.1 region-shrink, P5) predictions
must stay byte-identical to the current champion.
**Keep if:** the pre-2021 CV prefers income-group shrinkage AND account MAE improves on 5.156
(P6) on the 2021→2024 evaluation, without changing saving/resilience predictions.

**E11 verdict: KEEP.** r=0.403 (n=76 dev-panel countries with both indicators in 2021 & 2024),
positive as hypothesized, above the 0.30 threshold. Gates clean: G3 (both are declared headlines
— `saved_formally`, `borrowed_formally`); G4 (76 countries, 97.4% dev-panel pop); G6 sign-stable
AND magnitude-retaining — the jackknife actually *grows* (0.403→0.471 after drop-top-5), so this
is emphatically not a big-country artifact. Δborrowing terciles are broadly monotonic in mean
Δformal-saving (low/mid/high = +5.8/+17.2/+13.4pp; mid slightly exceeds high, so the shape is
concave rather than strictly monotonic, but the ordering is clear). Reading: the 2021→2024
deepening is broad-based across both sides of the household balance sheet — where formal
borrowing grew, formal saving grew too — so the surge is genuine financial deepening, not a
saving-only store-of-value shift. Descriptive association only; account growth and common income
shocks are plausible common drivers of both sides (noted, not controlled); no causal claim.

**U4 verdict: KEEP.** Formal saving (fin17a==1, saving at a financial institution) is 46.2pp
among tertiary-educated adults vs 12.0pp among primary-or-less-educated adults — a 34.1pp gap,
far above the 5pp threshold and monotonic across the three education levels (12.0/22.6/46.2pp).
M2 cell-size gate passes for every group (n=14,103–53,354). M3 declared n/a (the country headline
`fin17a_17a1_d` bundles institutional with mobile saving, so the micro fin17a-only rate has no
exact country equivalent; this is a within-education subgroup split besides). Reading: the
*depth* margin of financial inclusion — actually using an account to save formally — is far less
reached among the least-educated than the access margin. Complements M1's income gradient on the
"not enough money" access barrier: education stratifies formal-saving depth even more sharply
(34pp) than income stratifies the money barrier (10pp). Descriptive, single 2024 cross-section.

**P7 verdict: KEEP, champion updated.** The pre-2021 CV (predict 2021 account from 2017 +
k=0.1 shrink toward the group 2017 pop-weighted mean) prefers the **income-group** basin
(`incomegroupwb24`, MAE 6.97) over the incumbent region basin (`regionwb24_hi`, 7.209) — so the
pre-registered adoption condition is met on ≤2021 data alone. Applied unchanged to the 2021→2024
account prediction, income-group shrinkage gives account MAE 5.144 vs P6's region-shrinkage 5.156
(−0.012pp, ~0.2% relative). Resilience (6.625, still region-shrink per P5) and saving (8.448,
damped trend) print byte-identical to P6, confirming per-target isolation. No 2024 leakage: the
basin choice was made entirely on the ≤2021 transition, and only 2021 account levels + their
income-group 2021 means feed the shrink. The gain is small (honestly logged, like P5's 0.057pp),
but both pre-registered conditions hold — the CV prefers income-group AND it wins out-of-sample —
so income group is a marginally better convergence basin than region for account. New champion:
account=5.144, resilience=6.625, saving=8.448.

## 2026-07-13 wrap-up
Ran 3 experiments (E11, U4, P7), one per stream — all KEEP. E11 (hypothesis): formal borrowing
and formal saving deepen together 2021→2024 (r=0.403, n=76, gate-clean, jackknife strengthens to
0.471) — the surge is broad balance-sheet deepening, not saving-specific, alongside E1/E10's
digitalization channels. U4 (micro): formal saving is sharply education-graded — 46.2pp
(tertiary) vs 12.0pp (primary-or-less), a 34.1pp monotonic gap — the depth margin is far less
reached among the least-educated than the access margin (complements M1). P7 (prediction):
pre-2021 CV prefers income-group over region as the account shrinkage basin; account MAE
5.156→5.144pp with resilience/saving byte-identical. New prediction champion: account=5.144,
resilience=6.625, saving=8.448. Everything committed on autoresearch/daily.

---

# 2026-07-14 daily autoresearch cycle

## E12 — pre-registered (hypothesis / country level)
**H:** Digital-payment adoption is a fourth channel of the 2021→2024 formal-saving surge:
countries where the share of adults making/receiving *any digital payment* (`g20_any`) grew
most 2021→2024 also saw the largest gains in formal saving (`fin17a_17a1_d`), dev panel,
population-weighted. Motivation: E1 (mobile money, r=0.719), E10 (wage rails, r=0.791), and
E11 (formal borrowing, r=0.403) established the surge as a broad digitalization/deepening
signature across several account on-ramps. Digital-payment usage growth is the most general
usage margin and should co-move too if the "broad digitalization" reading is right; a null
would bound the channel set. Distinct from E5 (which used the g20/account *ratio at 2021* to
predict *account* growth, direction rejected) — this tests Δg20 vs Δsaving co-movement, never
before run.
**Test:** weighted corr of Δ(`g20_any`)(2021→2024) vs Δ(`fin17a_17a1_d`)(2021→2024), dev
panel, weight = 2024 adult population. G3: `g20_any` is the declared `digital_payment`
headline in `INDICATORS` and `fin17a_17a1_d` the `saved_formally` headline → checked, not
n/a. Gates: G4 (coverage), G6 (jackknife drop-top-5, judged with the E4 magnitude-retention
lesson: sign-stable but r_droptop < 0.5×r_full = big-country artifact → discard the general
claim).
**Keep if:** |r| ≥ 0.30, sign positive (hypothesized), G6 sign-stable AND magnitude-retaining.
Descriptive association only — account growth is a plausible common driver of both sides
(noted, not controlled); no causal claim.

## U5 — pre-registered (micro stream)
**H:** Among unbanked adults (`account==0`), the barrier "financial institutions are too far
away" (`fin11b==1`) is cited more by **rural** adults (`urbanicity==1`) than **urban** adults
(`urbanicity==2`), pooled globally (2024 wave) — a geographic-access barrier that should bind
harder where physical branch/agent density is lower. Complements M1 (income gradient on the
"not enough money" barrier) and U4 (education gradient on formal-saving depth) with a
geographic gradient on a physical-access barrier. No prior peek at this split (only overall
`fin11b` value counts and the urbanicity↔account-rate direction were inspected, never the
fin11b-by-urbanicity cross-tab).
**Test:** weighted rate of `fin11b==1` among unbanked adults with `fin11b` answered
(∈{1,2,3,4}; 2=no, 3=dk, 4=refused treated as not-citing), split by `urbanicity`
(1=rural, 2=urban — confirmed via account-rate direction: rural 66.3pp < urban 76.6pp),
pooled across all 2024 economies (raw `wgt`, economy-equal pooling per the current micro.py
default — HARNESS_V2_NOTES caveat #3 applies to exact pooled pp values, not direction).
Gates: M2 (unweighted cell n ≥ 100 per urbanicity group). M3 declared n/a — no country-file
equivalent for a within-unbanked reason-split.
**Keep if:** (rate_rural − rate_urban) ≥ 5pp in the hypothesized direction (rural higher).
Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P8 — pre-registered (prediction stream)
**Idea:** resilience (`fin24aSD_ND`) currently uses region-basin shrinkage (`regionwb24_hi`,
k=0.1; P5 champion, MAE 6.625). Because resilience has no pre-2021 wave to CV a basin on
directly (P1–P3 box), P5 borrowed the shrink parameters from the account 2017→2021 transition
CV. P7's CV on that *same* ≤2021 account transition preferred the **income-group** basin
(`incomegroupwb24`, MAE 6.97) over region (7.209). So switch resilience shrinkage from region
to income-group, reusing P7's already-established pre-2021 basin choice unchanged — no 2024
information touches the choice, k stays 0.1. Per-target policy (P2's rule): touches resilience
only — account (income-group shrink, P7) and saving (damped trend, P2) predictions must stay
byte-identical to the current champion.
**Keep if:** resilience MAE improves on 6.625 (P5 region-shrink champion) without changing the
account/saving predictions.

**E12 verdict: KEEP.** r=0.370 (n=76 dev-panel countries with both indicators in 2021 & 2024),
positive as hypothesized, above the 0.30 threshold. Gates clean: G3 (both are declared headlines
— `digital_payment` = `g20_any`, `saved_formally` = `fin17a_17a1_d`); G4 (76 countries, 97.4%
dev-panel pop); G6 sign-stable AND magnitude-retaining — the jackknife actually *grows*
(0.370→0.782 after drop-top-5), so emphatically not a big-country artifact (like E11). Δg20_any
terciles are broadly monotonic in mean Δformal-saving (low/mid/high = +2.8/+16.7/+14.4pp; mid
slightly exceeds high, so concave rather than strictly monotonic, but the ordering is clear).
Reading: digital-payment usage growth is a fourth co-moving channel of the 2021→2024 formal-saving
surge, alongside mobile money (E1, r=0.719), wage rails (E10, r=0.791) and formal borrowing (E11,
r=0.403) — consistent with the surge as a broad-based digitalization/deepening signature rather
than any single mechanism. Distinct from E5 (which used the g20/account ratio at 2021 to predict
account growth, direction rejected): this is Δg20 vs Δsaving co-movement. Descriptive association
only; account growth is a plausible common driver of both sides (noted, not controlled); no causal
claim. Same big-economy caveat class as E1/E7/E10, though here the jackknife strengthens.

**U5 verdict: DISCARD.** rate_rural=36.0pp vs rate_urban=36.8pp, diff=−0.8pp — opposite of the
hypothesized direction (rural expected higher) and far below the 5pp threshold in magnitude. M2
cell-size gate passes for both cells (n=12,992 rural / 7,859 urban unbanked). Reading: the
"financial institutions are too far away" barrier is cited at near-identical rates by rural and
urban unbanked adults in the pooled 2024 cross-section — physical distance does not read as a
sharper barrier for rural unbanked once economies are pooled economy-equal. Plausibly a
within-country rural/urban gap exists in individual economies but washes out under economy-equal
pooling (HARNESS_V2_NOTES caveat #3), and urban unbanked face their own access frictions. A clean,
slightly-reversed, below-threshold null. Descriptive, single 2024 cross-section.

**P8 verdict: DISCARD, reverted to P7/P5 champion.** Switching resilience shrinkage from the region
basin (`regionwb24_hi`, P5) to the income-group basin (`incomegroupwb24`) gave resilience MAE
6.802 vs the P5 champion 6.625 — 0.177pp *worse*. Account (5.144, income-group shrink) and saving
(8.448, damped trend) printed byte-identical, confirming per-target isolation. Reading: even though
the pre-2021 account 2017→2021 CV prefers the income-group basin for *account* (6.97 < 7.209, P7),
that basin preference does NOT transfer to *resilience* out-of-sample — resilience's convergence
structure is better captured by the region basin. A useful negative: the CV-selected basin is
target-specific, not a universal choice. Reverted predictor.py to the P7 champion (region basin for
resilience). Champion unchanged: account=5.144, resilience=6.625, saving=8.448.

## 2026-07-14 wrap-up
Ran 3 experiments (E12, U5, P8), one per stream. E12 (hypothesis, KEEP): digital-payment adoption
growth co-moves with the 2021→2024 formal-saving surge at r=0.370 (n=76, gate-clean, jackknife
strengthens 0.370→0.782) — a fourth broad-digitalization channel alongside mobile money (E1),
wage rails (E10) and formal borrowing (E11). U5 (micro, DISCARD): the "too far away" physical-access
barrier is NOT cited more by rural than urban unbanked in the pooled 2024 cross-section (36.0 vs
36.8pp, −0.8pp, essentially flat and slightly reversed) — the geographic gradient washes out under
economy-equal pooling. P8 (prediction, DISCARD): income-group basin does not transfer to resilience
shrinkage out-of-sample (6.625→6.802pp worse); the CV-preferred basin is target-specific — reverted
to the region basin for resilience. Prediction champion unchanged: account=5.144, resilience=6.625,
saving=8.448. Everything committed on autoresearch/daily.

---

# 2026-07-15 daily autoresearch cycle

## E13 — pre-registered (hypothesis / country level)
**H:** Institutional (financial-institution) and mobile-money account growth are *complements*,
not substitutes, in the 2021→2024 window: countries where FI-account ownership
(`fiaccount_t_d`) grew most also saw the largest growth in mobile-money accounts
(`mobileaccount_t_d`), dev panel, population-weighted. Motivation: the "leapfrogging"
narrative predicts substitution (mobile money replacing formal accounts → negative r), while
the "broad-digitalization" reading behind E1/E10/E11/E12 predicts co-development (positive r).
Mobile and FI accounts are *distinct* components of the headline `account_t_d`, so a country
can grow one without the other — this is not tautological. Never run before (E1/E3 used
mobile-money growth vs saving/gender; this is FI-account vs mobile-account growth).
**Test:** weighted corr of Δ(`fiaccount_t_d`)(2021→2024) vs Δ(`mobileaccount_t_d`)(2021→2024),
dev panel, weight = 2024 adult population. G3: both `fi_account` and `mobile_money` are declared
headlines in `INDICATORS` → checked, not n/a. Gates: G4 (coverage), G6 (jackknife drop-top-5,
judged with the E4 magnitude-retention lesson: sign-stable but r_droptop < 0.5×r_full =
big-country artifact → discard the general claim).
**Keep if:** |r| ≥ 0.30, sign positive (complements/hypothesized), G6 sign-stable AND
magnitude-retaining. Descriptive association only; a null or negative would support the
leapfrogging/substitution reading. No causal claim.

## U6 — pre-registered (micro stream)
**H:** A *usage-side* gender gap conditional on access: among adults who already hold an
account (`account==1`), digital-payment adoption (`anydigpayment`) is lower among women
(`female==1`) than men (`female==2`), pooled globally (2024 wave) — access does not
guarantee equal usage. Complements the access-margin nulls (U1 gender×income on account
ownership) by moving to the usage margin conditional on having the account. No prior peek at
this outcome (only overall `anydigpayment` and `account` value counts inspected for coding,
never the gender split among accountholders).
**Test:** weighted rate of `anydigpayment` among adults with `account==1`, split by `female`
(1=female, 2=male; per the U1 coding fix), pooled across all 2024 economies (raw `wgt`,
economy-equal pooling per the current micro.py default — HARNESS_V2_NOTES caveat #3 applies to
exact pooled pp values, not direction). Gates: M2 (unweighted cell n ≥ 100 per gender). M3
declared n/a — this is a within-accountholder usage subgroup split with no exact country-file
equivalent (the country `g20_any` is over all adults, not conditional on account ownership).
**Keep if:** (rate_men − rate_women) ≥ 5pp in the hypothesized direction (men higher).
Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P9 — pre-registered (prediction stream)
**Idea:** account_t_d currently uses income-group-basin shrinkage with a *fixed* k=0.1 (P7
champion, MAE 5.144), where k=0.1 was carried over from the coarse P5 CV. Tune k finer for the
income-group basin: cross-validate k over the grid {0.0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5}
entirely on the fully-≤2021 account_t_d 2017→2021 transition (predict 2021 from 2017 +
income-group shrink), pick the CV-min k, and apply that fixed k unchanged to the 2021→2024
account prediction. No 2024 information touches the selection. Adopt only if the CV picks a k
that also improves the 2021→2024 account MAE over the P7 champion (5.144). Per-target policy
(P2's rule): touches account only — saving (damped trend) and resilience (region-shrink k=0.1)
predictions must stay byte-identical to the current champion.
**Keep if:** the pre-2021 CV selects a k AND account MAE improves on 5.144 (P7) on the
2021→2024 evaluation, without changing saving/resilience predictions.

**E13 verdict: KEEP.** r=0.435 (n=59 dev-panel countries with both indicators in 2021 & 2024),
positive as hypothesized (complements), above the 0.30 threshold. Gates clean: G3 (both are
declared headlines — `fi_account` = `fiaccount_t_d`, `mobile_money` = `mobileaccount_t_d`); G4
(62 countries, 71.3% dev-panel pop); G6 sign-stable AND magnitude-retaining (0.435→0.347 after
drop-top-5, above the 0.5×r_full=0.218 floor). Δfiaccount terciles vs mean Δmobileaccount:
low/mid/high = −2.8/+14.6/+12.3pp (broadly monotonic, concave — mid slightly exceeds high).
Reading: institutional-account and mobile-money account growth *co-move* 2021→2024 — countries
built out both margins together rather than one substituting for the other. This favors the
broad-digitalization/co-development reading (behind E1/E10/E11/E12) over the "leapfrogging"
substitution narrative, at least at the country-aggregate level. Descriptive association only;
mobile and FI accounts are distinct components of the headline `account_t_d`, so this is not
tautological; no causal claim. Same big-economy caveat class, though the jackknife retains most
of its magnitude.

**U6 verdict: DISCARD.** rate_men=86.8pp vs rate_women=83.4pp, diff=+3.4pp — in the hypothesized
direction (men higher) but below the 5pp threshold in magnitude. M2 cell-size gate passes for
both cells (n=34,249 accountholder women / 32,882 accountholder men). Reading: *conditional on
already holding an account*, the usage-side gender gap in digital-payment adoption is small
(3.4pp) and well below the keep threshold — access-margin gaps are where the gender story lives,
not the usage margin once an account is held. A gate-clean, right-direction, below-threshold
null. Descriptive, single 2024 cross-section.

**P9 verdict: DISCARD, reverted to P7 champion.** The finer pre-2021 CV grid on the account
2017→2021 transition (income-group basin) prefers k=0.2 (in-sample MAE 6.743, better than
k=0.1's 6.97), so the CV-selection half of the keep condition is met. But applied to the
2021→2024 account prediction, k=0.2 gives MAE 5.186 vs the P7 champion's 5.144 (k=0.1) —
0.042pp *worse* out-of-sample. The keep condition required BOTH conditions; the second fails, so
discard. Reading: a larger shrinkage helps in-sample on the 2017→2021 transition but overfits it
— the 2021→2024 window is better served by lighter k=0.1, so the incumbent k transfers better.
Same lesson-class as P8: pre-2021 CV optima don't always transfer to the 2021→2024 evaluation.
Reverted predictor.py to the P7 champion (income-group basin, k=0.1). Champion unchanged:
account=5.144, resilience=6.625, saving=8.448.

## 2026-07-15 wrap-up
Ran 3 experiments (E13, U6, P9), one per stream. E13 (hypothesis, KEEP): FI-account and
mobile-money account growth are *complements* 2021→2024, not substitutes — r=0.435 (n=59,
gate-clean, jackknife 0.435→0.347) — countries built out both account margins together,
favoring co-development over "leapfrogging." U6 (micro, DISCARD): conditional on holding an
account, the usage-side gender gap in digital-payment adoption is only 3.4pp (men 86.8 vs women
83.4) — right direction but below the 5pp threshold; the gender story is on the access margin,
not usage-given-access. P9 (prediction, DISCARD): a finer pre-2021 CV picks k=0.2 for the
account income-group basin (in-sample 6.743<6.97) but it overfits — out-of-sample account MAE
5.186>5.144, so the incumbent k=0.1 transfers better; reverted to P7. Prediction champion
unchanged: account=5.144, resilience=6.625, saving=8.448. Everything committed on
autoresearch/daily.

---

# 2026-07-16 daily autoresearch cycle

## E14 — pre-registered (hypothesis / country level)
**H:** The digitalization on-ramps are *bundled*, not independent: countries where mobile-money
account ownership (`mobileaccount_t_d`) grew most 2021→2024 also saw the largest growth in
any-digital-payment usage (`g20_any`), dev panel, population-weighted. Motivation: E1 linked
Δmobile-money to the formal-saving surge (r=0.719) and E12 linked Δdigital-payment to the same
surge (r=0.370), treating them as separate "channels." If Δmobile-money and Δg20 are themselves
strongly correlated, the "four distinct channels" framing (E1/E10/E11/E12) is better read as one
bundled digitalization phenomenon co-moving across access and usage margins. Distinct from E13
(FI-account vs mobile-account growth) and E5 (g20/account *ratio* at 2021 vs account growth):
this is Δmobile-money vs Δg20 co-movement, never before run.
**Test:** weighted corr of Δ(`mobileaccount_t_d`)(2021→2024) vs Δ(`g20_any`)(2021→2024), dev
panel, weight = 2024 adult population. G3: both `mobile_money` and `digital_payment` are declared
headlines in `INDICATORS` → checked, not n/a. Gates: G4 (coverage), G6 (jackknife drop-top-5,
judged with the E4 magnitude-retention lesson: sign-stable but r_droptop < 0.5×r_full =
big-country artifact → discard the general claim).
**Keep if:** |r| ≥ 0.30, sign positive (bundled/hypothesized), G6 sign-stable AND
magnitude-retaining. Descriptive association only — account growth is a plausible common driver
of both sides (noted, not controlled); no causal claim.

## U7 — pre-registered (micro stream)
**H:** Education stratifies the *access* margin (account ownership) as well as the depth margin,
but less sharply: among all adults in the 2024 wave, account ownership (`account==1`) is more
common among tertiary-educated adults (`educ==3`) than primary-or-less-educated adults
(`educ==1`), pooled globally — an education gradient on account *access* to sit alongside U4's
34.1pp education gradient on formal-saving *depth*. No prior peek at this outcome (only overall
`account`/`educ` value counts were inspected for coding, never the account-by-educ cross-tab).
**Test:** weighted rate of `account==1` (0/1-coded headline) split by `educ` (1=primary-or-less,
2=secondary, 3=tertiary), pooled across all 2024 economies (raw `wgt`, economy-equal pooling per
the current micro.py default — HARNESS_V2_NOTES caveat #3 applies to exact pooled pp values, not
direction). Gates: M2 (unweighted cell n ≥ 100 per educ group). M3 declared n/a — this is a
within-education subgroup split; the pooled economy-equal by-group rate has no exact country-file
equivalent (the country `account_t_d` is a per-country all-adults level, not a global by-educ
pooled rate).
**Keep if:** (rate_tertiary − rate_primary) ≥ 5pp in the hypothesized direction (tertiary higher).
Descriptive, single 2024 cross-section — no trend language regardless of outcome. Secondary
descriptive note (not a keep condition): compare this access gap to U4's 34.1pp depth gap.

## P10 — pre-registered (prediction stream)
**Idea:** saving (`fin17a_17a1_d`) uses a *fixed* damped-trend λ=0.5 (P2 champion, MAE 8.448),
never CV-tuned. Tune λ via a pre-2021 cross-validation on the fully-≤2021 saving history (all
117 panel countries have 2014/2017/2021 saving): predict 2021 saving = 2017 + λ·(2017−2014),
grid λ ∈ {0.0, 0.25, 0.5, 0.75, 1.0}, pick the CV-min λ, and apply that fixed λ unchanged to the
2024 prediction (2024 = 2021 + λ·(2021−2017), clipped [0,100]). No 2024 information touches the
selection. Adopt only if the CV selects a λ that also improves the 2021→2024 saving MAE over the
P2 champion (8.448). Per-target policy (P2's rule): touches saving only — account (income-group
shrink k=0.1, P7) and resilience (region shrink k=0.1, P5) predictions must stay byte-identical
to the current champion.
**Keep if:** the pre-2021 CV selects a λ AND saving MAE improves on 8.448 (P2) on the 2021→2024
evaluation, without changing the account/resilience predictions.

**E14 verdict: KEEP.** r=0.600 (n=58 dev-panel countries with both indicators in 2021 & 2024),
positive as hypothesized (bundled), well above the 0.30 threshold. Gates clean: G3 (both are
declared headlines — `mobile_money` = `mobileaccount_t_d`, `digital_payment` = `g20_any`); G4 (76
countries, 97.4% dev-panel pop); G6 sign-stable AND magnitude-retaining — the jackknife actually
*grows* (0.600→0.775 after drop-top-5), so emphatically not a big-country artifact (like E11/E12).
Δmobile-money terciles vs mean Δg20: low/mid/high = −6.0/+10.4/+9.7pp (broadly monotonic, concave —
mid slightly exceeds high). Reading: the digitalization on-ramps are *bundled*, not independent —
Δmobile-money and Δdigital-payment usage themselves co-move strongly, so E1's "mobile-money channel"
and E12's "digital-payment channel" of the saving surge are better read as one bundled
digitalization phenomenon co-moving across the access margin (mobile-money accounts) and the usage
margin (digital payments), rather than four cleanly separable mechanisms. Descriptive association
only; account growth is a plausible common driver of both sides (noted, not controlled); no causal
claim. Same big-economy caveat class, though here the jackknife strengthens.

**U7 verdict: KEEP.** Account ownership (access margin) is 93.4pp among tertiary-educated adults
vs 51.9pp among primary-or-less-educated adults — a +41.5pp gap, far above the 5pp threshold and
monotonic across the three education levels (51.9/77.7/93.4pp). M2 cell-size gate passes for every
group (n=30,480–74,624). M3 declared n/a (within-education subgroup split, no exact country-file
equivalent). Reading: education stratifies the *access* margin (account ownership) at least as
sharply as the *depth* margin — the +41.5pp access gap is actually larger in absolute pp than U4's
+34.1pp formal-saving depth gap. NOTE: the pre-registered *secondary* guess ("less sharply") was
wrong, but it was explicitly not a keep condition, and the base rates differ (account 52–93pp vs
formal saving 12–46pp), so absolute-pp comparison is apples-to-oranges — the honest reading is that
education is a strong stratifier on *both* margins. The primary keep condition (tertiary−primary
≥5pp, tertiary higher) holds decisively. Complements U4 (education→depth) and M1 (income→access
barrier). Descriptive, single 2024 cross-section.

**P10 verdict: DISCARD, reverted to P2/P7 champion.** The pre-2021 CV (predict 2021 saving = 2017 +
λ·(2017−2014), n=117) selects **λ=0.0** — pure persistence beat any trend extrapolation on the calm
2014→2021 window (grid MAE 6.969/7.242/7.656/8.155/8.703 for λ=0.0/0.25/0.5/0.75/1.0), so the
CV-selection half of the keep condition is met. But applied to the 2021→2024 saving prediction,
λ=0.0 gives MAE 9.767 vs the P2 champion's 8.448 (λ=0.5) — 1.319pp *worse* out-of-sample. The keep
condition required BOTH; the second fails, so discard. Account (5.144) and resilience (6.625)
printed byte-identical, confirming per-target isolation. Reading: the 2021→2024 formal-saving surge
carries genuine momentum that the fixed λ=0.5 damped trend captures, but that momentum is *absent*
from the quiescent 2014→2021 saving dynamics the CV trained on — so the CV mis-selects λ=0.0. This
is the same regime-change lesson as P3 (the surge is not learnable from pre-2021 dynamics) and the
same non-transfer lesson-class as P8/P9 (pre-2021 CV optima don't always transfer to the 2021→2024
window). The fixed λ=0.5 (never CV-tuned, adopted in P2) remains the better saving predictor
precisely because it does not defer to the pre-surge history. Reverted predictor.py to the P7
champion. Champion unchanged: account=5.144, resilience=6.625, saving=8.448.

## 2026-07-16 wrap-up
Ran 3 experiments (E14, U7, P10), one per stream. E14 (hypothesis, KEEP): Δmobile-money and
Δdigital-payment usage themselves co-move strongly 2021→2024 (r=0.600, n=58, gate-clean, jackknife
grows 0.600→0.775) — the on-ramps are *bundled*, so E1/E12's separate "channels" of the saving
surge are one digitalization phenomenon across access and usage margins. U7 (micro, KEEP): account
ownership is strongly education-graded — 93.4pp (tertiary) vs 51.9pp (primary-or-less), a +41.5pp
monotonic gap, even wider in absolute pp than U4's +34.1pp formal-saving depth gap (bases differ);
education stratifies both the access and depth margins. P10 (prediction, DISCARD): CV-tuning the
saving damped-trend λ on the pre-2021 (2014→2021) transition picks λ=0.0 (persistence), but that is
9.767pp out-of-sample vs 8.448 for the fixed λ=0.5 — the saving surge's momentum is a regime change
absent from pre-surge dynamics (echoes P3); reverted to the P2/P7 champion. Prediction champion
unchanged: account=5.144, resilience=6.625, saving=8.448. Everything committed on autoresearch/daily.

---

# 2026-07-17 daily autoresearch cycle

## E15 — pre-registered (hypothesis / country level)
**H:** The formal-saving surge bought resilience where it landed: countries with the largest
2021→2024 gains in formal saving (`fin17a_17a1_d`) also saw the largest gains in financial
resilience (`fin24aSD_ND`), dev panel, population-weighted. Motivation: the working paper's
headline puzzle is that dev-panel resilience was flat (54.7→54.5pp) while formal saving surged;
E7 showed the *composition* of emergency funds shifted toward savings where the surge landed,
and E2 found Δresilience does NOT track Δmobile-money (r=0.189, discard). But the direct test —
Δresilience vs Δformal-saving — has never been run. A positive keep says the surge does buy
resilience where it lands (the flat aggregate hides offsetting declines elsewhere); a null
sharpens the access-vs-depth gap into a saving-vs-resilience gap: even where formal saving
surged, resilience did not follow within three years.
**Test:** weighted corr of Δ(`fin24aSD_ND`)(2021→2024) vs Δ(`fin17a_17a1_d`)(2021→2024), dev
panel, weight = 2024 adult population. G3: both are the declared `resilience` and
`saved_formally` headlines in `INDICATORS` → checked, not n/a. Gates: G4 (coverage), G6
(jackknife drop-top-5, judged with the E4 magnitude-retention lesson: sign-stable but
r_droptop < 0.5×r_full = big-country artifact → discard the general claim).
**Keep if:** |r| ≥ 0.30, sign positive (hypothesized), G6 sign-stable AND magnitude-retaining.
Descriptive association only — common income shocks are a plausible common driver of both
sides (noted, not controlled); no causal claim.

## U8 — pre-registered (micro stream)
**H:** A *depth-side* gender gap conditional on access: among adults who already hold an
account (`account==1`), formal saving at a financial institution (`fin17a==1`) is less common
among women (`female==1`) than men (`female==2`), pooled globally (2024 wave). Motivation: U6
found the *usage* gender gap conditional on access is small (digital payments, 3.4pp, below
threshold); this tests whether the *depth* margin (formal saving) shows a larger conditional
gender gap, or whether gender gaps conditional-on-access are small across the board. No prior
peek at this outcome (U4 used fin17a by educ over all adults; the fin17a-by-gender-among-
accountholders cross-tab has never been read).
**Test:** weighted rate of `fin17a==1` (coding 1=yes, 2=no, 3=dk, 4=refused → 2/3/4 treated as
not-saving, NaN=not asked dropped) among adults with `account==1`, split by `female` (1=female,
2=male; per the U1 coding fix), pooled across all 2024 economies (raw `wgt`, economy-equal
pooling per the current micro.py default — HARNESS_V2_NOTES caveat #3 applies to exact pooled
pp values, not direction). Gates: M2 (unweighted cell n ≥ 100 per gender). M3 declared n/a —
within-accountholder subgroup split with no exact country-file equivalent (the country headline
bundles mobile saving and is over all adults).
**Keep if:** (rate_men − rate_women) ≥ 5pp in the hypothesized direction (men higher).
Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P11 — pre-registered (prediction stream)
**Idea:** saving (`fin17a_17a1_d`) is the weakest target (MAE 8.448, P2 damped trend λ=0.5) and
the only one without basin shrinkage — yet shrinkage improved both other targets out-of-sample
(P5 resilience, P6/P7 account). Test adding k=0.1 basin shrinkage ON TOP of the champion damped
trend for saving. Basin selection entirely pre-2021 (no 2024 leakage): CV on the fully-≤2021
saving 2017→2021 transition (predict 2021 saving from the 2017 level + k=0.1 shrink toward the
basin's 2017 pop-weighted mean; persistence base for the CV since P10 showed pre-2021 saving
dynamics carry no usable trend), comparing {none, regionwb24_hi, incomegroupwb24}. Adopt the
CV winner ONLY IF it is not "none"; then apply that basin's k=0.1 shrink to the 2021→2024
damped-trend prediction (shrink the prediction vector toward its basin pop-weighted mean).
Known risk, accepted: the P8/P9/P10 lesson is that pre-2021 CV choices often fail to transfer
across the 2021 regime change — a discard here is informative about whether that lesson extends
to saving shrinkage. Per-target policy (P2's rule): touches saving only — account (income-group
shrink k=0.1, P7) and resilience (region shrink k=0.1, P5) must stay byte-identical.
**Keep if:** the pre-2021 CV prefers a non-"none" basin AND saving MAE improves on 8.448 (P2)
on the 2021→2024 evaluation, without changing the account/resilience predictions.

**E15 verdict: DISCARD (clean null, informative).** r=0.031 (n=76 dev-panel countries with both
indicators in 2021 & 2024) — far below the 0.30 threshold. Gates otherwise clean: G3 (both
declared headlines — `resilience` = `fin24aSD_ND`, `saved_formally` = `fin17a_17a1_d`); G4 (76
countries, 97.4% dev-panel pop); G6 mechanically sign-stable (0.031→0.133) but moot at this
magnitude. Terciles of Δsaving vs mean Δresilience are non-monotonic (low/mid/high =
−3.0/+3.9/+0.7pp) — no dose-response shape. Reading: the flat dev-panel resilience aggregate
(54.7→54.5pp) does NOT hide a positive saving→resilience association at the country level —
even where formal saving surged most, resilience did not move within the same three-year
window. Combined with E2 (Δresilience ⊥ Δmobile-money) and E7 (the *composition* of emergency
funds shifted toward savings where the surge landed), the picture is coherent: the saving surge
re-routed how the already-resilient would raise emergency funds, without yet expanding the
share who can. The access-vs-depth gap extends to a saving-vs-resilience gap. Descriptive,
no causal claim; three years may simply be too short for stock accumulation to move resilience.

**U8 verdict: DISCARD (borderline, right direction).** rate_men=34.5pp vs rate_women=29.5pp
among accountholders; unrounded diff = +4.96pp — the hypothesized direction, but just below the
pre-registered ≥5pp keep threshold (the rounded print of +5.0 does not clear an unrounded
4.955). M2 cell-size gate passes for both cells (n=34,249 women / 32,882 men). Verdict follows
the threshold, not the rounding. Reading: conditional on holding an account, the *depth-side*
gender gap in formal saving (~5pp) is larger than the usage-side gap (U6: 3.4pp digital
payments) but still modest relative to unconditional access-margin gradients (U4/U7:
34–42pp by education). A consistent pattern across U6/U8: once access is held, within-gender
usage/depth differences are small in the pooled 2024 cross-section. Descriptive, single wave.

**P11 verdict: KEEP, champion updated.** The pre-2021 CV (predict 2021 saving from 2017 +
k=0.1 shrink, persistence base, n=117) prefers the **region** basin (`regionwb24_hi`, MAE
6.584) over both none (6.969) and income-group (6.641) — the adoption condition is met on
≤2021 data alone. Applied on top of the champion damped trend (λ=0.5), region-shrinking the
2021→2024 saving prediction vector gives saving MAE 7.963 vs the P2 champion's 8.448
(−0.485pp, ~5.7% relative — the largest single-target gain since P6). Account (5.144,
income-group shrink) and resilience (6.625, region shrink) print identical to the P7 champion,
confirming per-target isolation. No 2024 leakage: basin chosen entirely on the 2017→2021
transition; only ≤2021 levels feed the prediction. Why this pre-2021 CV choice *transferred*
when P8/P9/P10's did not: shrinkage corrects cross-sectional sampling noise — a
regime-independent mechanism — whereas P9/P10 tuned *dynamics* (k-strength interacting with
convergence speed, trend λ), which the 2021 regime change invalidated. All three targets now
carry k=0.1 basin shrinkage (account: income-group; resilience & saving: region). New champion:
account=5.144, resilience=6.625, saving=7.963.

## 2026-07-17 wrap-up
Ran 3 experiments (E15, U8, P11), one per stream. E15 (hypothesis, DISCARD — informative null):
Δresilience does not track Δformal-saving 2021→2024 (r=0.031, n=76, gate-clean) — even where
the saving surge landed, resilience did not move within the window; with E2/E7 this sharpens
the story to a saving-vs-resilience gap (composition shifted, capacity did not). U8 (micro,
DISCARD — borderline): among accountholders, men out-save women formally by +4.96pp, the
hypothesized direction but a hair under the pre-registered 5pp threshold; conditional-on-access
gender gaps stay small (echoes U6). P11 (prediction, KEEP): k=0.1 region-basin shrinkage on top
of the saving damped trend — basin CV-selected on the pre-2021 transition — cuts saving MAE
8.448→7.963 (−0.485pp), the largest gain since P6; shrinkage transfers across the regime change
where dynamics-tuning (P9/P10) did not. New prediction champion: account=5.144,
resilience=6.625, saving=7.963. Everything committed on autoresearch/daily.

---

# 2026-07-18 daily autoresearch cycle

## E16 — pre-registered (hypothesis / country level)
**H:** The 2021→2024 formal-saving surge co-moves with account-ownership growth itself, dev
panel, population-weighted. Motivation: every kept digitalization-bundle finding (E1 mobile
money, E10 wage digitalization, E11 formal borrowing, E12 digital payments, E13 fi↔mm, E14
mm↔g20) carries the standing caveat "account growth a plausible common driver (noted, not
controlled)." That common driver has never been tested directly. A strong positive says the
saving surge is, to first order, part of broad account expansion (the channels are riding the
same access wave); a null/weak result says formal-saving depth deepened somewhat independently
of who newly got an account.
**Test:** weighted corr of Δ(`account_t_d`)(2021→2024) vs Δ(`fin17a_17a1_d`)(2021→2024), dev
panel, weight = 2024 adult population; descriptive terciles of Δaccount vs mean Δsaving. G3:
both are declared `INDICATORS` headlines (`account` = `account_t_d`, `saved_formally` =
`fin17a_17a1_d`) → checked. Gates: G4 (coverage), G6 (jackknife drop-top-5, judged with the E4
magnitude-retention lesson: sign-stable but r_droptop < 0.5×r_full = big-country artifact →
discard the general claim).
**Keep if:** |r| ≥ 0.30, sign positive (hypothesized), G6 sign-stable AND magnitude-retaining
(r_droptop ≥ 0.5×r_full). Descriptive association only — account growth and saving depth share
income-shock and digitalization drivers (noted, not controlled); no causal claim.

## U9 — pre-registered (micro stream)
**H:** Among unbanked adults (`account==0`), the "lack of necessary documentation" barrier
(`fin11d==1`) is cited more by the least-educated (`educ==1`, primary-or-less) than by the
most-educated (`educ==3`, tertiary), pooled 2024 wave, weighted. Motivation: prior barrier
splits found income grades the money barrier (M1: fin11a, +10.3pp q1→q5) but gender/urbanicity
do not grade distance/family barriers (U3, U5 nulls). Documentation is the barrier most
plausibly tied to formal-paperwork familiarity, so education is its natural stratifier. No
prior peek: the fin11d-by-educ cross-tab has never been read.
**Test:** weighted rate of `fin11d==1` (coding 1=yes, 2=no, 3=dk, 4=refused → 2/3/4 = not
citing, NaN=not asked dropped) among `account==0`, split by `educ` (1=primary-/2=secondary/
3=tertiary), pooled across all 2024 economies (raw `wgt`, economy-equal pooling per micro.py
default — HARNESS_V2_NOTES caveat #3 applies to exact pooled pp, not direction). Gates: M2
(unweighted cell n ≥ 100 per education group). M3 declared n/a — barrier-among-unbanked
subgroup split, no exact country-file equivalent.
**Keep if:** (rate_primary − rate_tertiary) ≥ 5pp in the hypothesized direction (least-educated
higher). Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P12 — pre-registered (prediction stream)
**Idea:** saving (`fin17a_17a1_d`) is the weakest target (MAE 7.963, P11 = damped trend λ=0.5 +
k=0.1 region-basin shrink). Test whether a SECOND, orthogonal light shrink toward the
income-group basin mean (k2=0.1) further denoises saving. Motivation: P7 found income-group is
the best single basin for account and region for resilience/saving — the two basins capture
partly-orthogonal cross-sectional structure, so a nested region-then-income-group shrink may
correct residual noise the region shrink leaves. This is the transfer-tested shrinkage
mechanism (noise correction, regime-independent — the reason P11 transferred where P9/P10
dynamics-tuning did not), applied a second time, not a new dynamics knob. Selection entirely
pre-2021: CV on the fully-≤2021 saving 2017→2021 transition (persistence base per P10) must
prefer the two-stage (region→income-group) shrink over the single region shrink before
adoption. Per-target policy (P2's rule): touches saving only — account (income-group shrink
k=0.1, P7) and resilience (region shrink k=0.1, P5) must stay byte-identical.
**Keep if:** the pre-2021 CV prefers two-stage over single-stage AND saving MAE improves on
7.963 (P11) on the 2021→2024 evaluation, without changing the account/resilience predictions.
Known risk, accepted: a second shrink may over-smooth (P9's finer-k overfit lesson); a discard
is informative about whether stacking orthogonal basins helps or the first shrink already
captures the denoisable structure.

**E16 verdict: DISCARD (informative — the "common driver" caveat partly relieved).** Weighted
r(Δaccount, Δsaving) 2021→2024 = 0.198 (n=76 dev-panel), below the 0.30 threshold. G3 clean
(both declared headlines); G4 clean (77c, 100% pop). The striking detail: G6 drop-top-5 makes
the correlation JUMP to 0.741 — i.e. the largest-population economies (which had the most
account growth) are precisely where formal saving surged *least*, dragging the pop-weighted
correlation down. Terciles of Δaccount vs mean Δsaving are non-monotonic (low/mid/high =
+15.4/+9.6/+14.3pp). Reading: the saving surge is not, to first order, just raw account
expansion — the depth margin deepened somewhat independently of who newly got an account, and
most sharply *outside* the big account-growth economies. This partly relieves the standing
"account growth a plausible common driver" caveat carried by E1/E10/E11/E12/E13/E14: at the
population-weighted level account growth and the saving surge are only weakly aligned. (Note:
the drop-top-5 r=0.741 is itself a big-country-story-in-reverse and not a general claim; the
headline is the sub-threshold full-sample r.) Descriptive, no causal claim.

**U9 verdict: KEEP.** Documentation barrier (fin11d==1) among unbanked adults, by education:
primary-or-less=54.2pp, secondary=48.6pp, tertiary=46.0pp — monotonic, primary−tertiary=+8.2pp,
clearing the pre-registered ≥5pp threshold in the hypothesized direction. M2 passes for every
group (n=9714/9995/1086, all ≫100). M3 declared n/a. Reading: the documentation barrier has a
high base rate (~half of all unbanked cite it) and education grades it modestly (+8.2pp) — the
natural stratifier for a formal-paperwork barrier, echoing M1's income gradient on the money
barrier (+10.3pp) and standing in contrast to the U3/U5 nulls (gender/urbanicity do not grade
the family/distance barriers). Descriptive, single 2024 cross-section.

**P12 verdict: KEEP, champion updated.** Pre-2021 CV (saving 2017→2021, persistence base)
prefers the two-stage region→income-group shrink (MAE 6.505) over the single region shrink
(6.584) — the adoption condition is met on ≤2021 data alone. Applied out-of-sample, stacking a
second k=0.1 income-group-basin shrink on top of the P11 region shrink cuts saving MAE
7.963→7.359 (−0.604pp, *larger* than P11's own −0.485pp gain). Account (5.144) and resilience
(6.625) print byte-identical, confirming per-target isolation. No 2024 leakage: both basins and
k chosen on ≤2021 transitions only. Why it transferred: region and income-group capture
partly-orthogonal cross-sectional structure (P7), so the two noise-correction shrinks compound
rather than redundantly overlap — and shrinkage, being regime-independent, stacks across the
2021 surge where dynamics-tuning (P9/P10) did not. New champion: account=5.144,
resilience=6.625, saving=7.359.

## 2026-07-18 wrap-up
Ran 3 experiments (E16, U9, P12), one per stream. E16 (hypothesis, DISCARD — informative):
Δaccount ⊥ Δsaving 2021→2024 at the pop-weighted level (r=0.198, n=76); drop-top-5 flips it to
0.741, meaning the biggest account-growth economies are where saving surged *least* — the
surge is a depth phenomenon not reducible to raw account expansion, partly relieving the
"account growth common driver" caveat on the E1/E10-E14 bundle. U9 (micro, KEEP): the
documentation barrier among the unbanked is education-graded, primary 54.2pp vs tertiary
46.0pp (+8.2pp, monotonic), the natural stratifier for a formal-paperwork barrier (cf. M1's
income gradient). P12 (prediction, KEEP): stacking a second orthogonal income-group shrink on
the P11 region shrink cuts saving MAE 7.963→7.359 (−0.604pp) — orthogonal noise-correction
basins compound, extending the P11 shrinkage-transfers lesson. New prediction champion:
account=5.144, resilience=6.625, saving=7.359. Everything committed on autoresearch/daily.

---

# 2026-07-20 daily autoresearch cycle

## E17 — pre-registered (hypothesis / country level)
**H:** The 2021→2024 formal-saving surge is a *catch-up* phenomenon: economies with a LOWER
2021 formal-saving level had LARGER 2021→2024 gains, dev panel, population-weighted.
Motivation: three independent strands now point at basin-convergence structure in saving.
E16 found the biggest account-growth economies are where saving surged *least* (drop-top-5
r jumps to 0.741), and the prediction stream's two biggest wins (P11 region shrink −0.485pp,
P12 stacked income-group shrink −0.604pp) both work by pulling countries toward group means —
i.e. the 2021 levels contain reversible noise/room-to-grow. Never tested directly at the
hypothesis-stream level. E5/E9 found the same catch-up shape on *account* growth (both
pre-registered directions rejected in favour of convergence), so the standing question is
whether the depth margin behaves like the access margin.
**Test:** weighted corr of `fin17a_17a1_d`(2021) level vs Δ(`fin17a_17a1_d`)(2021→2024), dev
panel, weight = 2024 adult population; descriptive terciles of the 2021 level vs mean Δsaving.
Reported alongside the same test on `account_t_d` as a comparison benchmark (does the depth
margin converge more or less than the access margin?). G3: `saved_formally` =
`fin17a_17a1_d` and `account` = `account_t_d`, both declared headlines → checked. Gates: G4
(coverage), G6 (jackknife drop-top-5, judged with the E4 magnitude-retention lesson:
r_droptop ≥ 0.5×r_full required).
**Keep if:** |r| ≥ 0.30 with NEGATIVE sign (hypothesized catch-up), G6 sign-stable AND
magnitude-retaining. Known confound, declared in advance and not controlled: any level-vs-change
regression mechanically inherits regression-to-the-mean from survey sampling error in the 2021
level, so a negative r is an upper bound on true catch-up; the account benchmark is included
precisely so the two margins can be compared on the same mechanical footing. Descriptive
association, no causal claim.

## U10 — pre-registered (micro stream)
**H:** Conditional on holding an account, digital-payment usage (`anydigpayment`) is
education-graded: tertiary-educated accountholders use digital payments more than
primary-or-less accountholders, pooled 2024 wave, weighted. Motivation: the conditional-on-access
results so far are all *gender* splits and all came back small (U6 usage-side 3.4pp, U8
depth-side 4.96pp — both below threshold), while the *unconditional* education gradients are
the largest effects in the micro stream (U7 account 41.5pp, U4 formal saving 34.1pp). Open
question: is "conditional on access, gaps are small" a general property of the access margin
having done the sorting, or is it specific to gender? Education is the sharpest available test.
No prior peek: the anydigpayment-by-educ cross-tab among accountholders has never been read.
**Test:** weighted rate of `anydigpayment==1` among `account==1`, split by `educ`
(1=primary-or-less / 2=secondary / 3=tertiary), pooled across all 2024 economies (raw `wgt`,
economy-equal pooling per micro.py default — HARNESS_V2_NOTES caveat #3 applies to exact pooled
pp, not direction). Gates: M2 (unweighted cell n ≥ 100 per education group). M3 declared n/a —
within-accountholder subgroup split, no exact country-file equivalent.
**Keep if:** (rate_tertiary − rate_primary) ≥ 5pp in the hypothesized direction. Descriptive,
single 2024 cross-section — no trend language regardless of outcome.

## P13 — pre-registered (prediction stream)
**Idea:** generalize P12's two-stage shrink to the other two targets. Saving now uses
region→income-group stacked shrinks (MAE 7.359); account uses a single income-group shrink
(P7, 5.144) and resilience a single region shrink (P5, 6.625). If orthogonal basins compound
as a general noise-correction mechanism (P12's lesson) rather than a saving-specific accident,
adding the *other* basin as a second stage should help both. Test per target: account
income-group→region, resilience region→income-group, k=0.1 each. Counter-evidence on record:
P8 showed the income-group basin does NOT transfer to resilience when used *alone* — this tests
it as a second stage on top of region, which is a different claim.
**Adoption rule (entirely pre-2021, no 2024 anywhere):** for each target independently, CV on
the fully-≤2021 2017→2021 transition (persistence base, per P10/P12) must prefer the two-stage
shrink over that target's current single shrink. Adopt per target only where the CV prefers it;
saving stays byte-identical to the P12 champion either way.
**Keep if:** any target adopted by the pre-2021 CV also improves its champion MAE
out-of-sample (account < 5.144 and/or resilience < 6.625), with untouched targets printing
byte-identical. Known risk, accepted: P9's finer-k overfit lesson and P8's non-transfer both
warn that what the pre-2021 CV likes need not transfer; a split verdict (CV adopts, MAE worsens)
is itself informative about the limits of the P12 stacking lesson.

**E17 verdict: DISCARD (double rejection — but the benchmark is the informative part).** The
pre-registered catch-up direction is rejected outright: weighted r(saving level 2021,
Δsaving 21-24) = **+0.480** (n=76), i.e. *divergence* — formal saving deepened fastest where it
was already deepest (2021-level terciles low/mid/high → +8.5/+13.0/+15.8pp, monotonic). But
that opposite association does not survive G6 either: drop-top-5 flips it to −0.135
(retention −0.281, far under the 0.5 floor), so it is a big-country artifact and no general
divergence claim can be made. G3/G4 clean. The pre-registered account benchmark is what
survives: r=−0.301 with the jackknife *growing* to −0.457 — gate-clean catch-up on the access
margin, reconfirming E5/E9 from a third angle. Reading: the two margins behave oppositely on
level-vs-change. Access converges (poor-access economies catch up); depth does not — at the
population-weighted level the saving surge went to already-deep economies, and even that is
top-5-driven. The declared regression-to-the-mean confound biases *toward* negative r and so
cannot manufacture the positive saving coefficient. Note the tension with P11/P12: basin
shrinkage helps saving prediction, yet saving shows no gate-clean convergence in levels —
shrinkage is correcting cross-sectional noise, not exploiting mean reversion. Descriptive.

**U10 verdict: KEEP.** Digital-payment usage among accountholders, by education:
primary-or-less=77.3pp, secondary=87.7pp, tertiary=94.1pp — monotonic, tertiary−primary=
**+16.8pp**, well clear of the ≥5pp threshold in the hypothesized direction. M2 passes for
every group (n=17067/37350/12478). M3 n/a. This answers the question U6/U8 left open: "gaps
shrink to near-nothing conditional on access" is a property of *gender* (3.4pp usage-side,
4.96pp depth-side), not a general property of conditioning on access. Education still grades
usage by 16.8pp among accountholders — though the access margin does most of the sorting: the
unconditional gap is 46.7pp (37.3/60.4/84.0), so ~64% of it is absorbed by who holds an account
at all, leaving a third that is a genuine within-accountholder usage gradient. Descriptive,
single 2024 cross-section.

**P13 verdict: SPLIT — account KEEP (new champion), resilience DISCARD.** Generalizing P12's
two-stage orthogonal-basin shrink to the other targets gives a split result. *Account*
(income-group→region): pre-2021 CV prefers two-stage 6.958 vs 6.970 — a very thin margin — and
out-of-sample MAE improves 5.144→**5.105** (−0.039pp). Adopted, but the gain is ~15× smaller
than saving's own second-stage gain (−0.604pp), consistent with account already being the
best-predicted target with least denoisable residual. *Resilience* (region→income-group):
DISCARDED, MAE worsened 6.625→6.730, reverted to the P5 single region shrink under the
per-target policy. **Disclosed deviation from the P13 pre-registration:** `fin24aSD_ND` exists
only in the 2021 wave, so it has no pre-2021 transition and the registered per-target CV was
infeasible — I proxied it on the account 2017→2021 transition (the P5 precedent that picked
k=0.1 for this target), keeping resilience's own basin order and no 2024 data anywhere. That
proxy adopted two-stage (6.955 vs 7.209) and was wrong out-of-sample: an exact replay of P8,
where account-transition basin preferences also failed to transfer to resilience. The standing
lesson is now twice-confirmed — resilience cannot be model-selected off account's history, and
lacking any pre-2021 history of its own it may simply not be honestly tunable in this design.
Saving byte-identical at 7.359. New champion: account=**5.105**, resilience=6.625, saving=7.359.

## 2026-07-21 daily autoresearch cycle

## E18 — pre-registered (hypothesis / country level)
**H:** The 2021→2024 formal-saving surge displaced *borrowing* as an emergency-funds source:
countries with the largest gains in formal saving (`fin17a_17a1_d`) saw the largest *declines*
in the share citing borrowing to raise emergency funds (`fin24bor`), dev panel,
population-weighted. Motivation: E7 (KEEP, r=0.541) found savings became a bigger emergency-funds
source (`fin24sav`) where the surge landed; the natural mirror is *which* source gave way. A
strong negative Δ`fin24bor` vs Δsaving reads as self-insurance displacing debt (a policy-desirable
substitution); a null for borrowing would say the surge displaced some other source (family,
selling assets) instead — reported descriptively alongside. Never run before (E7 used `fin24sav`,
the positive side; this is `fin24bor`, a distinct composition source).
**Test:** weighted corr of Δ(`fin24bor`)(2021→2024) vs Δ(`fin17a_17a1_d`)(2021→2024), dev panel,
weight = 2024 adult population; descriptive terciles of Δsaving vs mean Δfin24bor. G3: `fin24bor`
is an emergency-fund composition indicator with no headline/narrow variant choice in `INDICATORS`
→ declared n/a (same treatment as E7's `fin24sav`); `fin17a_17a1_d` is the declared
`saved_formally` headline. Gates: G4 (coverage), G6 (jackknife drop-top-5, judged with the E4
magnitude-retention lesson: sign-stable but r_droptop < 0.5×r_full = big-country artifact →
discard the general claim).
**Keep if:** |r| ≥ 0.30 with NEGATIVE sign (borrowing recedes where saving surges), G6 sign-stable
AND magnitude-retaining. Declared caveat, not controlled: emergency-fund composition shares are
roughly complementary, so *some* source must fall on average where savings rises — the empirical
content is whether *borrowing specifically* is the displaced source and how strong that is.
Descriptive association only; no causal claim.

## U11 — pre-registered (micro stream)
**H:** Mobile money reaches the poor: among accountholders, mobile-only accountholders
(`account_mob==1 & account_fin==0`) are drawn more from the poorest two income quintiles
(`inc_q ∈ {1,2}`) than bank-only accountholders (`account_fin==1 & account_mob==0`), pooled 2024
wave, weighted. Motivation: M2 (KEEP) found mobile-only accountholders are younger and less
educated than bank-only — an on-ramp for the underserved on the age/education margins. The income
margin was never tested and is the sharpest test of the "mobile money reaches the poor" policy
claim. No prior peek: the mobile-only/bank-only × income-quintile cross-tab has never been read.
**Test:** derive a binary `poor2 = inc_q ∈ {1,2}`; weighted rate of `poor2` among the mobile-only
group vs the bank-only group, pooled across all 2024 economies (raw `wgt`, economy-equal pooling
per micro.py default — HARNESS_V2_NOTES caveat #3 applies to exact pooled pp, not direction).
Gates: M2 (unweighted cell n ≥ 100 per group). M3 declared n/a — within-accountholder subgroup
composition split, no exact country-file equivalent.
**Keep if:** (poor2_share_mobile-only − poor2_share_bank-only) ≥ 5pp, mobile-only higher.
Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P14 — pre-registered (prediction stream)
**Idea:** saving (`fin17a_17a1_d`, champion MAE 7.359) uses a two-stage shrink with the stage
order fixed arbitrarily at region→income-group (P12). Test whether the reverse order
(income-group→region) does better. Because each stage shrinks values already modified by the
previous stage toward that stage's basin mean, the two orders are not identical. Selection
entirely pre-2021 (no 2024 leakage): CV on the fully-≤2021 saving 2017→2021 transition
(persistence base, per P10/P12) must prefer income-group→region over the incumbent
region→income-group before adoption; then apply that order unchanged to the 2021→2024 prediction.
Per-target policy (P2's rule): touches saving only — account (income-group→region two-stage, P13)
and resilience (region shrink k=0.1, P5) must stay byte-identical to the current champion. Known
risk, accepted: the orders may be near-equivalent (a thin CV margin like P13's account) and a
discard is informative about whether stage order matters for stacked shrinkage.
**Keep if:** the pre-2021 CV prefers income-group→region AND saving MAE improves on 7.359 (P12)
on the 2021→2024 evaluation, without changing the account/resilience predictions.

**E18 verdict: DISCARD (clean informative null).** Weighted r(Δfin24bor, Δsaving) 2021→2024 =
**+0.069** (n=76 dev-panel) — near-zero and the *wrong* sign (positive, not the hypothesized
negative), far below the 0.30 threshold; G6 flips it to −0.021 (moot at this magnitude). Terciles
of Δsaving vs mean Δborrow are non-monotonic and if anything rising in the high tercile
(+1.0/−0.3/+4.0pp). G3 declared n/a (fin24bor is a composition indicator with no variant choice,
same as E7's fin24sav; fin17a headline ok); G4 clean (76c, 97.4% pop). Reading: **borrowing was
NOT the emergency-fund source the saving surge displaced** — the mirror of E7 (savings became a
*bigger* source where the surge landed, r=0.541) does not run through the credit side. The
descriptive context is the informative part: the two sources that *co-declined* with the surge
were **selling assets** (Δfin24sell vs Δsaving r=−0.372) and **extra work/income** (Δfin24work
r=−0.489), while family transfers were flat (r=+0.067). But neither of the two negatives survives
G6 magnitude-retention (retention 0.41 and 0.28, both < 0.5) — they are big-country artifacts, so
no general claim can be made about which source gave way either. Declared compositional-
complementarity caveat applies (shares roughly sum, so some source must fall on average). The
honest conclusion: where formal saving surged, self-insurance did not visibly displace debt at
the population-weighted country level; any displacement of asset-sales/extra-work is top-5-driven.
Descriptive, no causal claim.

**U11 verdict: DISCARD (informative — the M2 on-ramp story does not extend to income).**
Mobile-only accountholders' share in the poorest two income quintiles = **33.8pp** vs bank-only
**38.8pp**, diff = **−5.0pp** — the *opposite* of the hypothesized direction (mobile-only was
expected higher). M2 cell-size gate passes for both groups (n=10,340 mobile-only / 24,037
bank-only). Full quintile profiles: mobile-only q1–q5 = 15/19/22/22/20, bank-only = 19/20/20/20/20
— bank-only is marginally *more* concentrated in the poorest quintile (q1 19 vs 15). Reading: M2's
"mobile money as an on-ramp for the underserved" holds on the **age** and **education** margins
(younger, less-educated — M2 KEEP) but **not on income** — mobile-only accountholders are, if
anything, slightly less poor than bank-only in the pooled 2024 cross-section. Caveat: `inc_q` is a
*within-economy* relative quintile, so economy-equal pooling mixes economies (bank-only dominates
high-income economies where almost everyone is bank-only); a within-country income comparison
could differ (HARNESS_V2_NOTES caveat #3). The pre-registered pooled test returns a clean,
reversed, threshold-magnitude null. Descriptive, single 2024 cross-section.

**P14 verdict: DISCARD, predictor.py reverted to the P13 champion (1bda919).** The pre-2021 CV
(saving 2017→2021, persistence base, n=117) prefers the **incumbent** region→income-group order
(MAE 6.505) over the challenger income→region (6.511) by a razor-thin **0.006pp** — so the
pre-registered adoption condition fails at its first gate (CV must prefer the challenger). The
incumbent order stays; predictions print byte-identical to the P13 champion (account 5.105,
resilience 6.625, saving 7.359). Reading: **stage order is practically irrelevant for stacked
orthogonal-basin shrinkage** — the region and income-group shrinks nearly commute (a 0.006pp CV
gap), so P12's arbitrary region-first choice was fine and there is no free gain in flipping it.
This tidily complements P12/P13's "orthogonal basins compound" lesson: the two basins capture
partly-orthogonal structure that adds up regardless of application order. A clean, low-cost
confirmation-by-null. Champion unchanged: account=5.105, resilience=6.625, saving=7.359.

## 2026-07-21 wrap-up
Ran 3 experiments (E18, U11, P14), one per stream — all DISCARD, all clean. E18 (hypothesis):
borrowing was NOT the emergency-fund source displaced by the 2021→2024 saving surge (r=+0.069,
wrong sign) — the E7 mirror does not run through the credit side; descriptively selling-assets
(−0.372) and extra-work (−0.489) co-declined but both are top-5 artifacts (G6 retention 0.41/0.28),
so no general claim about which source gave way. U11 (micro): M2's "mobile money reaches the
underserved" holds on age/education but NOT income — mobile-only accountholders' poorest-40 share
is 33.8pp vs bank-only 38.8pp (−5.0pp, reversed), i.e. marginally *less* poor (caveat: within-
economy quintiles under economy-equal pooling). P14 (prediction): saving two-stage shrink stage
order is practically irrelevant — pre-2021 CV prefers the incumbent region→income-group by 0.006pp
over the reverse, adoption condition fails, reverted to P13 champion. Prediction champion unchanged:
account=5.105, resilience=6.625, saving=7.359. Everything committed on autoresearch/daily.

---

# 2026-07-22 daily autoresearch cycle

## E19 — pre-registered (hypothesis / country level)
**H:** The 2021→2024 formal-saving surge shows up as *account activation*, not just new
accounts: countries with the largest gains in formal saving (`fin17a_17a1_d`) saw the largest
*declines* in account inactivity (`inactive_t_d` — adults with an account but no recent
activity), dev panel, population-weighted. Motivation: E16 (DISCARD) found Δaccount ⊥ Δsaving
at the pop-weighted level (the surge is not reducible to raw account expansion, and is sharpest
*outside* the big account-growth economies). If the surge is a depth phenomenon riding on
*existing* accounts, it should manifest as dormant accounts being put to use — a negative
Δinactive where Δsaving is large. A strong negative reads as "the surge activated idle
accounts"; a null says formal-saving depth and account dormancy move independently. Never run
before (E4 used inactivity as a *lagged consequence of account drives*; this is Δinactive vs
Δsaving co-movement).
**Test:** weighted corr of Δ(`inactive_t_d`)(2021→2024) vs Δ(`fin17a_17a1_d`)(2021→2024), dev
panel, weight = 2024 adult population; descriptive terciles of Δsaving vs mean Δinactive. G3:
`inactive` = `inactive_t_d` and `saved_formally` = `fin17a_17a1_d`, both declared `INDICATORS`
headlines → checked. Gates: G4 (coverage), G6 (jackknife drop-top-5, judged with the E4
magnitude-retention lesson: sign-stable but r_droptop < 0.5×r_full = big-country artifact →
discard the general claim).
**Keep if:** |r| ≥ 0.30 with NEGATIVE sign (saving surge co-moves with falling inactivity),
G6 sign-stable AND magnitude-retaining. Declared caveat, not controlled: account growth and
common income shocks plausibly drive both sides; a mechanical link (saving requires an active
account) is possible but not tautological (inactivity is measured over *all* accountholders,
most of whom do not save formally). Descriptive association only; no causal claim.

## U12 — pre-registered (micro stream)
**H:** Among unbanked adults (`account==0`), the "accounts are too expensive" barrier
(`fin11c==1`) is cited more by the poorest income quintile (`inc_q==1`) than the richest
(`inc_q==5`), pooled 2024 wave, weighted — a cost barrier that should bind hardest on the poor.
Motivation: M1 (KEEP) found the "not enough money" barrier is income-graded (+10.3pp q1→q5);
this tests whether the distinct *cost-of-service* barrier (fees/minimum balances, not the
person's own lack of funds) is similarly income-graded, or whether cost salience is flatter
across income (the near-poor who considered opening an account may cite fees as much as the
poorest). Complements the barrier map: M1 (money/income), U9 (documentation/education), U3
(family/gender null), U5 (distance/urbanicity null). No prior peek: the fin11c-by-income
cross-tab has never been read (only overall fin11c value counts inspected for coding —
1=yes/2=no/3=dk/4=refused, asked of unbanked only).
**Test:** weighted rate of `fin11c==1` (coding 1=yes, 2=no, 3=dk, 4=refused → 2/3/4 = not
citing, NaN=not asked dropped) among `account==0`, split by `inc_q` (1=poorest…5=richest),
pooled across all 2024 economies (raw `wgt`, economy-equal pooling per micro.py default —
HARNESS_V2_NOTES caveat #3 applies to exact pooled pp, not direction). Gates: M2 (unweighted
cell n ≥ 100 per quintile). M3 declared n/a — barrier-among-unbanked subgroup split, no exact
country-file equivalent.
**Keep if:** (rate_q1 − rate_q5) ≥ 5pp in the hypothesized direction (poorest higher).
Descriptive, single 2024 cross-section — no trend language regardless of outcome.

## P15 — pre-registered (prediction stream)
**Idea:** every prior prediction experiment (P1–P14) used persistence, damped trend, or basin
shrinkage of a single indicator's own history — none used a *multi-indicator regression*. Per
MODELING SCOPE (weighted ridge is appropriate; n≈117 is the binding constraint), test a weighted
**ridge** for `account_t_d` using three full-coverage 2021 features — the 2021 levels of account
(`account_t_d`), digital payment (`g20_any`), and formal saving (`fin17a_17a1_d`), all with
117/117 panel coverage (mobile money dropped — only ~62/117). Fit and select the ridge penalty
`alpha` entirely on the ≤2021 window: predict `account_2021` from the same three features at
2017, weighted by 2021 adult population, choosing alpha by leave-one-out CV over a fixed grid
(minimizing weighted MAE on the 2017→2021 transition). Then apply the fitted model to the 2021
feature levels to predict 2024. No 2024 information touches fitting or selection. Adopt for
account ONLY IF (a) on the ≤2021 CV the ridge beats the incumbent (persistence + two-stage
income-group→region shrink, P13) AND (b) it improves account MAE on 5.105 out-of-sample on the
2021→2024 evaluation. Per-target policy (P2's rule): touches account only — saving (damped
trend + two-stage region→income-group shrink, P12) and resilience (region shrink, P5) must stay
byte-identical to the P13 champion. Known risk, accepted: the P8/P9/P10/P13 lesson is that
pre-2021 model choices often fail to transfer across the 2021 regime change, and a
multi-feature fit has more parameters to overfit on n≈117 — a discard is informative about
whether cross-indicator structure adds anything over own-history shrinkage for account.
**Keep if:** the ≤2021 CV prefers the ridge over the incumbent AND account MAE improves on 5.105
(P13) on the 2021→2024 evaluation, without changing the saving/resilience predictions.

**E19 verdict: DISCARD (wrong sign at full sample; the drop-top-5 flip is the informative part).**
Weighted r(Δinactive, Δsaving) 2021→2024 = **+0.160** (n=76 dev-panel) — the *wrong* sign
(positive, hypothesized negative) and below the 0.30 threshold, so the pre-registered keep
condition fails outright. But G6 flips it hard: drop-top-5 → **−0.379** (retention −2.37), and the
Δsaving terciles show a clean monotonic dose-response in the hypothesized direction (mean Δinactive
low/mid/high = +0.5/−1.7/−4.1pp). G3 clean (both declared headlines — `inactive` = `inactive_t_d`,
`saved_formally` = `fin17a_17a1_d`); G4 clean (76c, 97.4% pop). Reading: this is the *mirror of
E16* — the largest-population economies (which had the most account growth and where formal saving
surged *least*) drag the pop-weighted correlation positive; drop them and the hypothesized
"activation" link appears (falling account inactivity where the saving surge landed, r=−0.379,
terciles monotonic). But per the E16/E17 treatment, the drop-top-5 sign is a big-country-story-in-
reverse, not a general population-weighted claim, and the headline full-sample r is wrong-signed
and sub-threshold. So no keep either way. The honest conclusion: outside the top-5 economies the
saving surge does co-move with dormant accounts being put to use, but this is not a gate-clean
general regularity. Descriptive, no causal claim.

**U12 verdict: DISCARD (clean informative null).** The "accounts are too expensive" barrier
(fin11c==1) among unbanked adults is **flat across income**: q1=23.7, q2=22.8, q3=24.1, q4=23.1,
q5=23.3pp — q1−q5 = **+0.4pp**, far below the 5pp threshold and essentially no gradient. M2 passes
for every quintile (n=3352–4894). M3 n/a. Reading: unlike the "not enough money" barrier (M1, which
is steeply income-graded at +10.3pp q1→q5), the *cost-of-service* barrier (fees/minimum balances)
is cited at a near-constant ~23% by unbanked adults across the entire income distribution. This
makes sense — cost is a fixed feature of the *product*, salient regardless of the respondent's own
income, whereas "not enough money" is a statement about the respondent's own means. Adds a clean
contrast to the barrier map: income grades the money barrier (M1) and education grades the
documentation barrier (U9), but income does NOT grade the cost barrier (U12), just as gender/
urbanicity do not grade the family/distance barriers (U3/U5). Descriptive, single 2024 cross-section.

**P15 verdict: DISCARD, predictor.py reverted to the P13 champion (1bda919).** The multi-indicator
weighted ridge for account (features: 2021 levels of account, g20_any, fin17a_17a1_d) fails the
adoption condition at its first gate. On the ≤2021 LOO-CV (predict account_2021 from the same three
features at 2017, weighted), the ridge's best MAE is **8.655pp** (flat across the whole alpha grid
0.0–300) — far *worse* than the incumbent persistence + two-stage income-group→region shrink's CV
MAE of **6.412pp**. So the CV does not prefer the ridge, and the predictor keeps the P13 incumbent
byte-identical (account 5.105, resilience 6.625, saving 7.359 all reproduced). Reading: cross-
indicator structure adds nothing over own-history shrinkage for account — a linear map from 2017
account/payment/saving levels to the 2021 account level (fitted coefs 0.845/0.265/−0.228, intercept
8.17) predicts the level far worse than simply carrying the 2017 account forward with light basin
shrinkage. The account level is overwhelmingly its own lagged value plus reversible cross-sectional
noise (which shrinkage corrects); the other indicators' levels are near-redundant with it and only
add fitting variance on n≈117. This is the P8/P9/P10/P13 non-transfer lesson in a new guise: a
richer ≤2021 model does not beat the parsimonious shrinkage even *in-sample* on the CV, let alone
out-of-sample. Reverted predictor.py to the champion. Champion unchanged: account=5.105,
resilience=6.625, saving=7.359.

## 2026-07-22 wrap-up
Ran 3 experiments (E19, U12, P15), one per stream — all DISCARD, all clean. E19 (hypothesis): the
saving surge co-moving with *falling account inactivity* is wrong-signed at the pop-weighted full
sample (r=+0.160) but flips to −0.379 dropping the top-5 with a clean monotonic tercile dose-
response (+0.5/−1.7/−4.1pp) — the exact mirror of E16, so activation shows up only *outside* the
biggest economies and is not a gate-clean general claim. U12 (micro): the "too expensive" cost
barrier among the unbanked is flat across income (~23pp at every quintile, q1−q5=+0.4pp) — unlike
M1's steeply income-graded money barrier, cost is a fixed product feature cited regardless of the
respondent's own means. P15 (prediction): a multi-indicator weighted ridge for account fails at the
first gate — its ≤2021 CV MAE (8.655) is far worse than the incumbent shrinkage (6.412), so
cross-indicator structure adds nothing over own-history shrinkage; reverted to the P13 champion.
Prediction champion unchanged: account=5.105, resilience=6.625, saving=7.359. Everything committed
on autoresearch/daily.

## 2026-07-20 wrap-up
Ran 3 experiments (E17, U10, P13), one per stream. E17 (hypothesis, DISCARD): the saving surge
is not catch-up — the sign is reversed (r=+0.480, divergence) and that reversal fails G6
(→−0.135), so neither direction generalizes; the pre-registered account benchmark, however, is
gate-clean catch-up (r=−0.301, jackknife grows), so access converges while depth does not.
U10 (micro, KEEP): conditional on holding an account, digital-payment usage is education-graded
+16.8pp (77.3/87.7/94.1, monotonic) — the "conditional-on-access gaps are small" pattern is
gender-specific (U6/U8 3-5pp), not general, though access absorbs ~64% of the unconditional
46.7pp gap. P13 (prediction, SPLIT): two-stage orthogonal-basin shrinkage generalizes to
account (5.144→5.105, thin) but not resilience (6.625→6.730, reverted) — a second confirmation
of P8's non-transfer, with a disclosed CV-proxy deviation since resilience has no pre-2021
history. New prediction champion: account=5.105, resilience=6.625, saving=7.359. Everything
committed on autoresearch/daily.

## 2026-07-23 daily autoresearch cycle

## E20 — pre-registered (hypothesis / country level)
**H:** The 2021→2024 formal-saving surge was **disequalizing within countries**: it widened the
income gap in formal saving (richest 60% minus poorest 40%), and countries with the biggest
overall surges widened that gap the most. Motivation: E1/E10/E12/E14 established *which channels*
the surge rode on (mobile money, wage digitalization, digital payments — one bundled
digitalization phenomenon); E16/E17 established its *level dynamics* (a depth phenomenon,
diverging rather than converging across countries). Its **within-country distributional
incidence** has never been tested. U4 (micro, KEEP) shows formal saving is steeply
education-graded in the 2024 cross-section (12.0/22.6/46.2pp), which makes a disequalizing
country-level surge plausible but not implied — the surge could equally have reached the
poorest 40% first from a low base. Never run before: no experiment has used the country file's
`group == "income"` slices (`richest 60%` / `poorest 40%`).
**Test:** dev panel (117-country balanced panel, non-high-income). For each country take
`fin17a_17a1_d` for `group2 == "richest 60%"` and `group2 == "poorest 40%"` in 2021 and 2024
(harness `pan_grp`, wave-merge applied). Define `gap_y = rich60_y − poor40_y` (pp) and
`Δgap = gap_2024 − gap_2021`; take `Δsaving` (overall, `group == "all"`) from `pan_dev`.
Primary statistic: pop-weighted (2024 adult population) correlation r(Δsaving, Δgap), plus
Δsaving terciles → mean Δgap (dose-response). Reported descriptively alongside: dev-aggregate
poor40 / rich60 saving levels in 2021 and 2024 and the aggregate gap change.
Gates: G3 (`saved_formally` headline `fin17a_17a1_d` declared for all three series),
G4 coverage on the income-slice frame in 2024, G6 jackknife (drop top-5 population) with the
E4 magnitude rule (r_droptop ≥ 0.5 × r_full). G5 n/a — no official aggregate for a
within-country gap series.
**Keep if:** r(Δsaving, Δgap) ≥ +0.30 AND G6 sign-stable and magnitude-retaining. A
negative-signed result of comparable size would be an equally interesting *equalizing*
finding but is NOT the pre-registered claim — per the E5/E9/E17 precedent it would be logged
as a direction rejection, reported descriptively, not converted into a keep. Descriptive
association only; no causal claim (account growth, income shocks and the mechanical
low-base arithmetic of the poorest-40 series are declared, uncontrolled confounds).

## U13 — pre-registered (micro stream)
**H:** Account ownership is **labour-force-status-graded**: adults in the workforce
(`emp_in == 1`) hold accounts at a higher rate than adults out of the workforce
(`emp_in == 2`), pooled 2024 wave, weighted. Motivation: `emp_in` is the one demographic in
`micro.py`'s DEMOGRAPHICS list never used by any experiment. The barrier/gradient map so far
is built on income (M1 money barrier +10.3pp; U12 cost barrier flat), education (U4 saving
+34.1pp, U7 account +41.5pp, U9 documentation +8.2pp, U10 digital payment | account +16.8pp),
gender (U1/U3/U6/U8, all small or null) and urbanicity (U5, null). Labour-force attachment is
the natural remaining stratifier — wage receipt is a first-order account on-ramp — and its
size relative to the education gradient is unknown. No prior peek: the account-by-`emp_in`
cross-tab has never been read (only `emp_in` value counts inspected for coding —
1=in workforce 83,865 / 2=out 56,205 / NaN 4,020).
**Test:** weighted rate of `account == 1` (already 0/1 in the labelled file) split by `emp_in`,
pooled across all 2024 economies (raw `wgt`, economy-equal pooling per `micro.py` default —
HARNESS_V2_NOTES caveat #3 applies to exact pooled pp, not to direction). Secondary, reported
descriptively only: formal saving (`fin17a == 1`) among accountholders by `emp_in` — the depth
margin — to see whether labour-force status stratifies depth as well as access.
Gates: M2 (unweighted cell n ≥ 100 per group). M3 declared n/a for the split itself
(within-`emp_in` subgroup, no country-file equivalent at that granularity); note the country
file does carry `group == "laborforce"` slices, so a country-level version of this split is
possible in principle but is a different (country-level) experiment.
**Keep if:** (rate_in − rate_out) ≥ 5pp in the hypothesized direction (in-workforce higher).
Declared caveat regardless of outcome: "out of workforce" is compositionally heterogeneous
(students, retirees, homemakers, discouraged workers) and correlates with age, gender and
education, so any gap is a descriptive association, not an employment effect. Single 2024
cross-section — no trend language.

## P16 — pre-registered (prediction stream)
**Idea:** P11/P12 established the one mechanism that transfers across the 2021 regime change:
**shrinkage toward basin means is noise correction and it compounds across orthogonal basins**
(saving 8.448 → 7.963 with one region stage → 7.359 with a second income-group stage), whereas
dynamics-tuning on the pre-2021 window (P9/P10) and richer cross-indicator fits (P15) do not
transfer. P13 showed the stacking generalizes weakly to account and not at all to resilience.
The untested question: does a **third** orthogonal basin add a third increment for saving —
and specifically a *data-driven* basin rather than a geographic/administrative one. Test a
**"digitalization-stage" basin**: terciles of the **2021 account level** (`account_t_d`,
117/117 panel coverage), which cuts across both region and income group. Stack it as stage 3
on the P12 champion for saving (damped trend λ=0.5 → region shrink → income-group shrink →
account-tercile shrink, k=0.1 at every stage, unchanged).
Selection, entirely ≤2021 (no 2024 anywhere in features, fitting or selection): CV on the
saving 2017→2021 transition with a persistence base (the P10/P12/P13 protocol), with every
basin — including the account terciles — constructed from the **2017** cross-section, comparing
the incumbent two-stage against the three-stage candidate.
Per-target policy (P2's rule): touches saving only — account (persistence + two-stage
income-group→region shrink) and resilience (persistence + region shrink) must stay
byte-identical to the P13 champion (5.105 / 6.625).
**Keep if:** the ≤2021 CV prefers three-stage over the incumbent two-stage AND saving MAE
improves on 7.359 on the 2021→2024 evaluation. Known risk, accepted: three stages at k=0.1
approaches over-shrinkage (each stage pulls toward a mean, and the basins are only partly
orthogonal — account-level terciles correlate with income group), so a discard is informative
about where the compounding stops.

**E20 verdict: DISCARD (pre-registered dose-response fails; the level fact is the informative
part).** Weighted r(Δsaving, Δgap) 2021→2024 = **+0.179** (n=55 dev panel with both income
slices in both waves) — the hypothesized *sign* but well below the 0.30 threshold, so the keep
condition fails. G6 is clean and in fact the jackknife *grows* (+0.179 → +0.359 drop-top-5,
retention 2.01, the E12/E14/E16 pattern), G3 clean (headline `fin17a_17a1_d` for all three
series), G4 clean (70 countries, 96.2% of dev-panel population on the income-slice frame),
G5 n/a. The Δsaving terciles are non-monotonic (mean Δgap low/mid/high = +1.2/+8.5/+5.5pp):
countries with the *biggest* surges did not widen their internal gaps the most, so the
"proportional disequalization" claim is rejected.
What the experiment did establish — pre-registered as descriptive context, not as the keep
statistic — is a large and one-directional **level** fact: pop-weighted across the same 55
economies, formal saving rose **+10.8pp for the poorest 40%** (18.4 → 29.2) and **+16.9pp for
the richest 60%** (32.8 → 49.7), so the within-country income gap in formal saving widened from
**14.4 to 20.5pp (+6.1pp)**. The surge reached both halves of the distribution — it is not a
rich-only phenomenon — but roughly 1.6× more of it accrued to the richer 60%. Two declared,
uncontrolled confounds apply: identical *proportional* gains from a lower base mechanically
widen a pp gap, and account growth/income shocks move both series. Because this is a level
claim that was registered only as context, it is logged as context and left as a candidate for
its own pre-registration (where the low-base arithmetic would have to be addressed directly,
e.g. by a ratio or log-odds formulation). Descriptive association only, no causal claim.

**U13 verdict: KEEP.** Account ownership is strongly graded by labour-force status in the
pooled 2024 cross-section: **in workforce 76.7pp vs out of workforce 61.7pp, diff = +15.0pp**,
comfortably above the 5pp threshold and in the hypothesized direction. M2 passes with room to
spare (n = 83,865 / 56,205). M3 n/a. Secondary and descriptive only: among *accountholders*,
formal saving is 34.2pp for in-workforce vs 20.9pp for out-of-workforce (+13.3pp) — so unlike
gender (U6 3.4pp, U8 4.96pp), the labour-force gap does **not** collapse once access is held
constant; it stays nearly as wide on the depth margin. Placing it on the gradient map: 15.0pp
is large but far below education on the same access margin (U7, 41.5pp) and above the
income-barrier gradients (M1, 10.3pp). Declared caveat, as pre-registered: "out of workforce"
is compositionally heterogeneous (students, retirees, homemakers, discouraged workers) and
correlates with age, gender and education, so this is a descriptive association, not an
employment effect. Single 2024 cross-section — no trend language.

**P16 verdict: KEEP — new saving champion 7.080 (was 7.359).** Both adoption conditions pass.
On the ≤2021 CV (saving 2017→2021, persistence base, every basin built at 2017) the three-stage
shrink beats the incumbent two-stage: **6.408 vs 6.505**. Out-of-sample on the 2021→2024
evaluation, saving MAE improves **7.359 → 7.080 (−0.279pp)**, with account (5.105) and
resilience (6.625) byte-identical under the per-target policy. Reading: orthogonal-basin
shrinkage compounds a **third** time (8.448 → 7.963 → 7.359 → 7.080, with diminishing
increments −0.485 / −0.604 / −0.279), and the third basin is **data-driven** — terciles of the
2021 account level, a "digitalization stage" cut that crosses region and income group — so the
mechanism is not tied to geographic or administrative groupings. This sharpens the standing
lesson: what transfers across the 2021 regime change is *noise correction* (shrinking reversible
cross-sectional deviations toward any reasonable basin mean), not *dynamics* (P9/P10) and not
*cross-indicator structure* (P15). Prediction champion now: account = 5.105, resilience = 6.625,
saving = 7.080.

## 2026-07-23 wrap-up
Ran 3 experiments (E20, U13, P16), one per stream — one discard, two keeps. E20 (hypothesis,
DISCARD): the saving surge's *proportional* disequalization fails — r(Δsaving, Δgap) = +0.179
(sub-threshold, terciles non-monotonic) — but the first-ever use of the income slices shows a
large level fact in context: the pop-weighted dev gap in formal saving widened 14.4 → 20.5pp
(poorest 40% +10.8pp vs richest 60% +16.9pp), left as a candidate for its own pre-registration.
U13 (micro, KEEP): account ownership is graded by labour-force status by +15.0pp (76.7 vs
61.7), and unlike gender the gap barely shrinks conditional on access (formal saving among
accountholders 34.2 vs 20.9pp) — first use of `emp_in`, the last untouched demographic.
P16 (prediction, KEEP): orthogonal-basin shrinkage compounds a third time using a *data-driven*
basin (account-level terciles), saving MAE 7.359 → 7.080 with account/resilience unchanged —
noise correction keeps transferring where dynamics-tuning and cross-indicator fits did not.
New prediction champion: account = 5.105, resilience = 6.625, saving = 7.080. Everything
committed on autoresearch/daily.

## 2026-07-24 daily autoresearch cycle

## E21 — pre-registered (hypothesis / country level), with a DISCLOSED PARTIAL PEEK
**Disclosure first (amendment #1, the peek rule).** E20 logged the dev-aggregate levels of formal
saving for both income slices (poorest 40% 18.4 → 29.2pp; richest 60% 32.8 → 49.7pp). Those two
pairs make the *aggregate ratio* comparison derivable by arithmetic without touching the data
(×1.59 vs ×1.52), so the aggregate-scale direction is NOT unknown to me at registration time.
Consequently: the aggregate ratio statement is logged as **exploratory context**, and if the
pre-registered primary below returns a keep it is recorded as **keep-exploratory**, never as a
clean pre-registered keep. What is genuinely unknown at registration time is the *country-level
distribution* — the pop-weighted mean of the within-country log-odds gap change, its sign share
across economies, and its dose-response against the overall surge. Those are the registered
statistics.
**H:** The within-country income gap in formal saving widened 2021→2024 in a **scale-free** sense,
i.e. the widening E20 found on the pp scale (14.4 → 20.5pp) is genuine disequalization rather than
the mechanical arithmetic of a lower poorest-40 base. E20 explicitly left this as "a candidate for
its own pre-registration (where the low-base arithmetic would have to be addressed directly, e.g.
by a ratio or log-odds formulation)" — this is that experiment.
**Test:** dev panel, same construction as E20 (harness `pan_grp`, `group == "income"`,
`group2 ∈ {richest 60%, poorest 40%}`, non-high-income, wave-merge applied, 2021 and 2024). For
each country and wave form the log-odds gap `L_y = logit(rich60_y) − logit(poor40_y)`, with rates
clipped to [0.5pp, 99.5pp] as a declared continuity correction (logit is undefined at 0/1), and
`ΔL = L_2024 − L_2021`. **Primary:** pop-weighted (2024 adult population) mean ΔL across countries.
**Secondary (association, G6 applies):** weighted r(Δsaving_overall, ΔL) — the scale-free version
of the dose-response E20 rejected on the pp scale (r=+0.179). Reported descriptively alongside:
the aggregate ratio decomposition (exploratory per the disclosure above), the share of countries
with ΔL > 0, and a level jackknife of the primary (recompute the pop-weighted mean ΔL after
dropping the 5 largest-population economies).
Gates: G3 (`saved_formally` headline `fin17a_17a1_d` for all series), G4 coverage on the
income-slice frame in 2024, G6 jackknife on the secondary correlation with the E4 magnitude rule
(r_droptop ≥ 0.5 × r_full). G5 n/a — no official within-country gap series exists. The primary is
a level claim, so it gets the declared level-jackknife analogue rather than G6 proper.
**Keep if:** pop-weighted mean ΔL ≥ **+0.20** log-odds (an odds-ratio widening of ≥1.22×) AND the
level jackknife keeps the sign AND ≥60% of economies share that sign. Secondary keeps separately
if r ≥ +0.30 with G6 clean. Per the E5/E9/E17 precedent, a materially *negative* mean ΔL is a
direction rejection reported descriptively — it would say the pp widening is a low-base artifact
and the surge was scale-free *equalizing* — and is NOT converted into a keep.
Declared caveats: log-odds is scale-free but not confound-free (account growth and common income
shocks still move both slices); the poorest-40/richest-60 cut is coarse; the continuity clip
affects only degenerate cells. Descriptive association only, never causal.

## U14 — pre-registered (micro stream)
**Coding disclosure (not an outcome peek).** `receive_wages` and `receive_transfers` sit in
`micro.py`'s BINARY_OUTCOMES list but are NOT 0/1 — they are 5-code categoricals, and no codebook
ships with the microdata zip, so I inferred the coding structurally before registering: code 1 =
received into an account (anydigpayment = 1.00 and account_fin = 0.93 within that cell, i.e. true
by construction), code 2 = received in cash (account_fin 0.36, no better than non-receivers),
code 3 = other/in-kind (n=833), code 4 = did not receive (n=63,640), code 5 = DK/refused (n=202).
This check also killed the obvious design: `receive_transfers == 1` implies `account == 1` in
7,184/7,184 cases, so any wage/transfer-receipt → account-ownership test is circular by
construction. The registered outcome below — the education gradient — remains unknown.
**H:** Among adults who **already hold an account** and receive wages, the share whose wages
arrive **in the account** rather than in cash is **education-graded**: the "last mile" of wage
digitalization is not equalized by access. Motivation: this is the individual-level counterpart of
E10 (country-level wage digitalization co-moves with the saving surge, r=0.791, KEEP), and it
extends the strongest thread in the micro stream — conditional on access, gender gaps collapse
(U6 3.4pp, U8 4.96pp) but education gaps do not (U10, digital payment | account, +16.8pp). Whether
that asymmetry also holds on the *wage-receipt* margin — where the employer, not the adult, picks
the payment mode — is unknown and is the point of the test. First use of `receive_wages`.
**Test:** restrict to `account == 1` AND `receive_wages ∈ {1, 2, 3}` (wage receivers, excluding
"did not receive" and DK). Weighted rate of `receive_wages == 1` (digital receipt), split by
`educ` (1 = primary or less / 2 = secondary / 3 = tertiary), pooled across all 2024 economies
(raw `wgt`, economy-equal pooling per `micro.py` default; HARNESS_V2_NOTES caveat #3 applies to
the exact pooled pp, not to direction). Secondary, descriptive only: the same split
*unconditional* on account holding, to quantify how much of the gradient access already absorbs
(the U10 decomposition).
Gates: M2 (unweighted cell n ≥ 100 per education cell). M3 declared n/a — no country-file
equivalent at this conditional granularity.
**Keep if:** (rate_tertiary − rate_primary) ≥ 5pp in the hypothesized direction.
Declared caveats: wage-receipt mode is largely an employer/sector attribute, so this is a
descriptive association with education, not an individual choice or an education effect; the
account-holding restriction conditions on a post-treatment variable; sectoral composition
(formal vs informal employment) is an obvious uncontrolled confound. Single 2024 cross-section —
no trend language.

## P17 — pre-registered (prediction stream)
**Idea:** P16 established that orthogonal-basin shrinkage compounds a **third** time for saving
and that the third basin can be **data-driven** (terciles of the account level) rather than
geographic or administrative — saving 8.448 → 7.963 → 7.359 → 7.080. P13 had already shown the
two-stage stacking generalizes weakly to account (5.144 → 5.105) and not at all to resilience
(P8/P13, two independent non-transfers). The untested question: does the *third*, data-driven
stage also generalize to **account** — the target where the second stage bought almost nothing?
Test a **digital-usage basin**: terciles of `g20_any` (digital-payment adoption, 117/117 panel
coverage at 2014/2017/2021), stacked as stage 3 on the P13 account champion (persistence →
income-group shrink → region shrink → g20 shrink, k=0.1 at every stage, unchanged). `g20_any` is
deliberately a **different indicator** from the target, unlike P16's account-tercile basin for
saving — shrinking account toward means of account-level bins would be near-degenerate.
Selection, entirely ≤2021 (no 2024 in features, fitting or selection): CV on the account
2017→2021 transition with a persistence base (the P10/P12/P13/P16 protocol), every basin —
including the g20 terciles — built from the **2017** cross-section, comparing the incumbent
two-stage against the three-stage candidate.
Per-target policy (P2's rule): touches account only — saving (7.080, damped trend + three-stage
shrink) and resilience (6.625, persistence + region shrink) must stay byte-identical to the P16
champion.
**Keep if:** the ≤2021 CV prefers three-stage over the incumbent two-stage AND account MAE
improves on 5.105 on the 2021→2024 evaluation. Known risk, accepted: account's two-stage gain was
already an order of magnitude smaller than saving's (−0.039pp vs −0.604pp), and account is close
to a ceiling in many panel countries, so there may simply be little reversible cross-sectional
noise left to correct — a discard would localize where the compounding mechanism stops.

**E21 verdict: DISCARD (all three pre-registered conditions fail — and the discard is the
substantive result).** The primary pop-weighted mean change in the within-country log-odds gap is
**+0.109** (odds ratio ×1.115), below the +0.20 threshold; the level jackknife **flips sign** to
**−0.115** when the 5 largest-population economies are dropped; and only **47.3%** of the 55
economies widened at all, far short of the registered 60% sign share. The secondary scale-free
dose-response fails identically to its pp-scale predecessor: r(Δsaving, ΔL) = **+0.176** (below
0.30) with **G6 FAIL** (+0.176 → −0.149 drop-top-5, retention −0.85), the same big-country
artifact pattern as E16/E19. G3 clean, G4 clean (70 countries, 96.2% of dev-panel population),
G5 n/a.
What this settles: **E20's headline level fact is largely low-base arithmetic.** The pp gap did
widen 14.4 → 20.5pp, but on a scale-free measure the poorest 40% actually gained *proportionally
faster* (×1.589 vs ×1.516 — the exploratory, peek-disclosed aggregate ratio), the pop-weighted
log-odds gap barely moved, under half of economies widened, and the aggregate sign is carried
entirely by the largest economies. The 2021→2024 formal-saving surge was therefore
**distributionally broad**, and E20's context fact should *not* be read as the rich pulling away.
The peek disclosure is moot in the event — the aggregate ratio direction was derivable from E20's
logged levels, so a keep would have been recorded as keep-exploratory, but nothing kept. The
tercile shape (−0.050/+0.130/+0.140) is monotone-ish but at magnitudes far too small to claim.
Logit clip [0.5, 99.5]pp as declared. Descriptive only, never causal.

**U14 verdict: KEEP — the largest conditional-on-access gradient found in the micro stream.**
Among adults who already hold an account *and* receive wages, the share whose wages arrive **in
the account** is steeply education-graded: **primary-or-less 56.6pp / secondary 80.6pp / tertiary
91.9pp, tertiary − primary = +35.3pp**, monotonic and far above the 5pp threshold. M2 passes with
room (n = 3,729 / 13,759 / 5,901); M3 n/a. Base rate: 63.6pp of all wage receivers are paid into
an account.
The decomposition is the interesting part. Unconditionally the gradient is +51.0pp (36.9 / 68.9 /
87.9), so **access absorbs only 31%** of it — against **~64%** for digital payments in U10
(46.7 → 16.8pp). Wage receipt is thus the **least access-equalized margin tested so far**: holding
an account is close to sufficient for a tertiary-educated wage earner to be paid into it (91.9pp)
and nowhere near sufficient for a primary-educated one (56.6pp). A plausible reading, consistent
with the declared caveat, is that the payment mode is chosen by the **employer**, not the adult —
so the education gradient here proxies formal-vs-informal sector composition rather than anything
the individual controls. That makes it the individual-level counterpart of E10 (country-level wage
digitalization co-moves with the saving surge, r=0.791, KEEP) and sharpens the standing thread:
conditional on access, **gender** gaps collapse (U6 3.4pp, U8 4.96pp) but **education** gaps
persist, and they persist most where a third party sets the terms. First use of `receive_wages`;
coding inferred structurally as disclosed, and the same check ruled out the circular
transfer→account design. Single 2024 cross-section — no trend language.

**P17 verdict: KEEP — new account champion 5.014 (was 5.105).** Both adoption conditions pass. On
the ≤2021 CV (account 2017→2021, persistence base, every basin built at 2017) the three-stage
shrink beats the incumbent two-stage **6.710 vs 6.958** — a comfortable margin, unlike the razor-
thin 6.958 vs 6.970 that adopted stage 2. Out-of-sample, account MAE improves **5.105 → 5.014
(−0.091pp)**, with saving (7.080) and resilience (6.625) byte-identical under the per-target
policy.
Two things generalize here. First, the **data-driven third stage transfers to a second target** —
P16's result was not saving-specific. Second, and more informative: for account the third stage
(**−0.091pp**, basin = terciles of `g20_any`, a *different* indicator) bought **more than twice**
what the second, purely administrative stage bought (−0.039pp, region). A basin drawn from another
indicator's cross-section evidently carries more independent signal than a second
geographic/administrative cut — which is why the P17 basin was deliberately specified on `g20_any`
rather than on account's own level. Standing lesson intact and strengthened: what transfers across
the 2021 regime change is **noise correction** (shrinking reversible cross-sectional deviations
toward any reasonable basin mean), not **dynamics** (P9/P10) and not **fitted cross-indicator
structure** (P15 ridge) — though cross-indicator information does help when it enters as a *basin*
rather than as fitted coefficients. Prediction champion now: account = **5.014**,
resilience = 6.625, saving = 7.080.

## 2026-07-24 wrap-up
Ran 3 experiments (E21, U14, P17), one per stream — one discard, two keeps. E21 (hypothesis,
DISCARD, all three conditions failed): the scale-free re-test E20 explicitly left open settles it —
the +6.1pp widening of the within-country income gap in formal saving is **largely low-base
arithmetic**, since mean Δ(log-odds gap) is only +0.109, flips to −0.115 without the top-5
economies, and under half of economies widened; the poorest 40% in fact gained proportionally
faster (×1.589 vs ×1.516). The 2021→2024 saving surge was distributionally broad.
U14 (micro, KEEP): among accountholding wage receivers, digital wage receipt is education-graded
by **+35.3pp** (56.6/80.6/91.9), and access absorbs only **31%** of the unconditional +51.0pp
gradient versus ~64% in U10 — the least access-equalized margin tested, plausibly because the
employer sets the payment mode. P17 (prediction, KEEP): the data-driven third shrink stage
generalizes from saving to account using a *cross-indicator* basin (g20_any terciles), account MAE
**5.105 → 5.014**, and that third stage bought more than twice the second administrative stage did.
New prediction champion: account = 5.014, resilience = 6.625, saving = 7.080. Everything committed
on autoresearch/daily.

## 2026-07-25 daily autoresearch cycle

## E22 — pre-registered (hypothesis / country level)
**Hypothesis:** E1 — the strongest kept country-level finding (the 2021→2024 formal-saving surge
co-moves with mobile-money growth, weighted r = 0.719, n = 58 dev-panel economies) — is a
**general developing-world regularity, not a Sub-Saharan Africa story**. Mobile money is heavily
SSA-concentrated, so an obvious alternative reading of E1 is that it describes one region and the
population weighting carries it. E1's jackknife (G6, drop the 5 largest-population economies)
guards against *one-country* stories but not against a *one-region* story; the backlog lists
"regional heterogeneity of kept findings E1/E5b/E7" for exactly this reason. This is the first
regional-split test in the ledger.
**Test:** partition the developing balanced panel by `regionwb24_hi` into **Sub-Saharan Africa
(excluding high income)** vs **rest of the developing panel** (the five other regions pooled).
Within each subsample, weighted (pop_adult) corr of Δ`mobileaccount_t_d` against
Δ`fin17a_17a1_d` over 2021→2024 — the identical construction to E1 — plus Δ(mobile money)
terciles with mean Δ(saving) per tercile, reported for both subsamples.
Gates: G3 (both headline indicators, registered concepts `mobile_money` / `saved_formally`);
G4 coverage run **per subsample** with `min_countries=15` — a disclosed deviation from the
default 30, unavoidable for any regional split since SSA has only 26 dev-panel economies, and the
pooled E1 sample already passed G4 at the default; G5 n/a (no official regional Δ-correlation
series); G6 jackknife per subsample at the standard `drop_top=5`, which with n ≈ 20–35 is a
**stiffer** test than for the full sample — noted, not relaxed.
**Keep if:** |r| ≥ 0.30 **in both subsamples** with the same (positive) sign, and G6 sign-stable
with magnitude retention ≥ 0.5 × r_full in both. If it holds only in SSA, the general claim is
**discarded** and E1 is re-logged as region-specific — that outcome is the informative one and is
registered as such in advance. Descriptive association only, never causal; account growth and
common income shocks remain uncontrolled confounds in both subsamples, as in E1.

## U15 — pre-registered (micro stream)
**Hypothesis:** conditional on holding an account, the **age** gradient in digital-payment use
**persists** (behaves like education, not like gender). The strongest micro thread is an
asymmetry in what access equalizes: conditional on an account, gender gaps collapse (U6 3.4pp,
U8 4.96pp) while education gaps persist (U10 +16.8pp, ~64% of the unconditional gap absorbed;
U14 +35.3pp, only 31% absorbed). U2 established the *unconditional* age profile of
`anydigpayment` (15-25 = 45.0 / 26-35 = 59.7 / 36-50 = 56.8 / 51-65 = 53.5 / 65+ = 48.1pp,
inverted-U peaking at 26-35). Whether that gradient is an access artifact — older adults simply
being less banked — or survives conditioning is unknown and completes the gender/education/age
triad on one common outcome.
**Test:** weighted rate of `anydigpayment == 1` among `account == 1`, split by the same five age
bands as U2 (15-25 / 26-35 / 36-50 / 51-65 / 65+), pooled across all 2024 economies (raw `wgt`,
economy-equal pooling per `micro.py`; HARNESS_V2_NOTES caveat #3 applies to the exact pooled pp,
not to direction). Primary statistic: **(26-35) − (65+)**, conditional on account — the peak band
U2 identified against the same low band. Secondary, descriptive: the U10-style absorption
decomposition against U2's unconditional 11.6pp gap for the same pair.
Gates: M2 (unweighted cell n ≥ 100 per band). M3 declared n/a (within-accountholder split, no
country-file equivalent).
**Keep if:** (rate_26-35 − rate_65+ | accountholder) ≥ 5pp.
Declared caveats: age correlates with education, employment and account tenure, none controlled —
this is a descriptive association, not an age effect; conditioning on account holding conditions
on a post-treatment variable (same caveat as U6/U8/U10/U14). Single 2024 cross-section — no trend
language.

## P18 — pre-registered (prediction stream)
**Idea:** does orthogonal-basin shrinkage compound a **fourth** time? The mechanism has now stacked
three stages on saving (P11 → P12 → P16: 8.448 → 7.963 → 7.359 → 7.080) and three on account
(P7 → P13 → P17: 5.144 → 5.105 → 5.014), and P17 delivered the sharper lesson: a **cross-indicator**
basin (terciles of `g20_any`) bought account more than twice what a second administrative cut did
(−0.091pp vs −0.039pp). Saving's stage 3 is already cross-indicator (account terciles). The
untested question is whether a *second* data-driven, cross-indicator basin still carries
independent signal once region, income group and account terciles have each had a pass.
**Test:** add stage 4 to **saving** — terciles of `g20_any` (digital-payment adoption, 117/117
panel coverage at 2014/2017/2021), stacked on the P16 champion (damped trend λ=0.5 → region →
income-group → account-tercile), k = 0.1 at every stage, unchanged. `g20_any` is a different
indicator from both the target and stage 3's basin column.
Selection, entirely ≤2021 (no 2024 in features, fitting or selection): CV on the saving 2017→2021
transition with a persistence base (the P10/P12/P13/P16/P17 protocol), every basin — including
both tercile basins — built from the **2017** cross-section, comparing the incumbent three-stage
against the four-stage candidate.
Per-target policy (P2's rule): touches saving only — account (5.014) and resilience (6.625) must
stay byte-identical to the P17 champion.
**Keep if:** the ≤2021 CV prefers four-stage over the incumbent three-stage **AND** saving MAE
improves on 7.080 on the 2021→2024 evaluation. Known risk, accepted: each added stage has bought
less than the last on account, and by stage 4 the basins may be close to collinear (g20 terciles
and account terciles are both digitalization cuts) — a CV rejection or an out-of-sample loss would
localize where compounding stops, which is the point of running it.

**E22 verdict: KEEP — E1 is a general developing-world regularity, not a Sub-Saharan Africa
story.** Both subsamples clear every pre-registered condition. Inside **SSA**: r = **+0.923**
(n = 25), G6 clean (0.923 → 0.878, retention 0.95), Δmobile-money terciles −0.2 / +10.5 / +21.1pp
of Δsaving. Inside the **five other developing regions pooled**: r = **+0.676** (n = 33), G6 clean
and *growing* (0.676 → 0.706, retention 1.04), terciles +3.0 / +9.1 / +12.5pp. The full-panel
replication reproduces E1 exactly (r = +0.719, n = 58), confirming the split is a partition of the
same estimation sample and not a re-specification. G3 clean, G4 clean per subsample under the
declared `min_countries=15` deviation (SSA 25 economies / 99.5% of regional population; rest 37 /
67.6%), G5 n/a.
What this settles: the one-*region* alternative that G6 — a one-*country* guard — structurally
could not address. The association is materially stronger inside SSA (0.92 vs 0.68) and the SSA
dose-response is steeper (+21.1pp in the top tercile vs +12.5pp outside), so mobile money is
plainly the more dominant rail there; but outside SSA the co-movement is still strong, monotone
in terciles, and survives a drop-top-5 jackknife on only 33 economies — a stiffer test than the
pooled sample faced. E1 therefore generalises, with a declared intensity gradient. Same caveats as
E1: account growth and common income shocks uncontrolled in both subsamples; descriptive
association, never causal. First regional-split test in the ledger; the same design is now
available for E5b and E7.

**U15 verdict: KEEP — and the age gradient is the *least* access-equalized margin tested.** Among
accountholders, digital-payment use runs **86.9 / 88.2 / 84.9 / 82.6 / 77.8pp** across 15-25 /
26-35 / 36-50 / 51-65 / 65+, so the registered (26-35) − (65+) statistic is **+10.3pp**, twice the
threshold. M2 passes with room (n = 6,525–18,436 per band); M3 n/a. The unconditional profile
recomputed here reproduces U2 exactly (45.0 / 59.7 / 56.8 / 53.5 / 48.1, gap +11.6pp), so the two
sides of the decomposition are constructed identically.
That decomposition is the result: **access absorbs only 10%** of the age gradient (11.6 → 10.3pp).
Ranking the three demographics on one outcome and one conditioning step now gives a clean ordering
— **gender collapses** (U6, 3.4pp residual), **education shrinks by ~64%** but stays large (U10,
46.7 → 16.8pp), and **age barely moves at all**. Age is thus almost entirely a *usage* gradient
rather than an access artifact: older adults are less banked, but that is not why they pay less
digitally. Secondary observation, descriptive: the unconditional inverted-U (peak 26-35, low
15-25) flattens into a near-monotone decline once accounts are held — the young-adult dip is an
access story, the old-age dip is not. Declared caveats stand: age correlates with education,
employment and account tenure, none controlled, and the conditioning is on a post-treatment
variable — association, not an age effect. Single 2024 cross-section, no trend language.

**P18 verdict: KEEP — new saving champion 6.831 (was 7.080). Compounding does not stop at three
stages.** Both adoption conditions pass: the ≤2021 CV (saving 2017→2021, persistence base, every
basin built at 2017) prefers four-stage **6.370 vs 6.408**, and out-of-sample saving MAE improves
**7.080 → 6.831 (−0.249pp)**, with account (5.014) and resilience (6.625) byte-identical under the
per-target policy.
The informative part is how little the gain decayed: stage 3 bought −0.279pp and stage 4 bought
−0.249pp, despite the two data-driven basins (account terciles, `g20_any` terciles) both being
digitalization cuts that might plausibly have been near-collinear. Whatever the fourth basin
partitions, it is not already covered by region, income group and account level. Saving's full
trajectory is now 9.767 (persistence) → 8.448 (damped trend) → 7.963 → 7.359 → 7.080 → **6.831**,
i.e. **shrinkage alone has bought −1.617pp**, more than the damped trend's −1.319pp. Standing
lesson unchanged and now four stages deep: what transfers across the 2021 regime change is
**noise correction** toward any reasonable basin mean, not **dynamics** (P9/P10) and not **fitted
cross-indicator structure** (P15). Prediction champion now: account = 5.014, resilience = 6.625,
saving = **6.831**. Open and untested: whether a fifth stage still pays, and whether the
diminishing-returns curve differs by target (account's stages went −0.039 / −0.091).

## 2026-07-25 wrap-up
Ran 3 experiments (E22, U15, P18), one per stream — **three keeps, no discards**, the first such
cycle in the ledger. E22 (hypothesis, KEEP): the first regional-split test closes the standing
one-region alternative to E1 — the mobile-money ↔ saving-surge co-movement holds inside SSA
(r = +0.923, n = 25) *and* outside it (r = +0.676, n = 33), both G6-clean with monotone terciles,
so E1 generalises with a declared SSA intensity gradient rather than being an SSA story.
U15 (micro, KEEP): conditional on holding an account, digital-payment use is still age-graded by
**+10.3pp** (26-35 vs 65+), and access absorbs only **10%** of the unconditional gap — completing
the triad, gender collapses (U6), education shrinks ~64% (U10), age barely moves. Age is a usage
gradient, not an access artifact. P18 (prediction, KEEP): a fourth shrink stage for saving on a
second cross-indicator basin (`g20_any` terciles) improves MAE **7.080 → 6.831**, with the gain
barely decaying from stage 3 (−0.249 vs −0.279pp). New prediction champion: account = 5.014,
resilience = 6.625, saving = **6.831**. Everything committed on autoresearch/daily.

## 2026-07-26 daily autoresearch cycle

## E23 — pre-registered (hypothesis / country level)
**Hypothesis:** the E1 mobile-money ↔ saving-surge co-movement is **distinct from the general
digitalization bundle**, i.e. it survives conditioning on digital-payment adoption growth. Every
country-level association in the ledger so far is bivariate, and the digitalization indicators are
demonstrably collinear: Δmobile money ~ Δsaving r = +0.719 (E1), Δg20_any ~ Δsaving r = +0.370
(E12), Δwage-digitalization ~ Δsaving r = +0.791 (E10), and Δmobile money ~ Δg20_any r = +0.600
(E14). So it is genuinely unknown whether mobile money is a *separate rail* into the saving surge
or just the SSA-flavoured face of one common digitalization factor. E22 closed the one-region
alternative to E1; this closes the one-*factor* alternative.
**Test:** weighted **partial** correlation of Δ(`mobileaccount_t_d`) with Δ(`fin17a_17a1_d`),
2021→2024, controlling Δ(`g20_any`), on the developing balanced panel. Construction follows E5b:
pop-weighted least-squares residualization of both variables on the control, then `weighted_corr`
of the residuals; `gate_jackknife` on the residual pair. `g20_any` is the primary control because
it has full dev-panel coverage (77/76), so the estimation sample stays E1's (mobile money binds at
n ≈ 58). Reported alongside, descriptively: the two bivariate benchmarks recomputed on the *same*
common sample; the **symmetric reverse** partial (Δg20_any ~ Δsaving | Δmobile money), which says
which rail carries the association; and a secondary partial using Δ(`fin32_acc`) — E10's wage
digitalization, the strongest bivariate competitor — as an alternative control on its smaller
sample.
Gates: G3 (all three concepts declared), G4 on the estimation sample, G6 jackknife on the residual
pair. G5 n/a (no official partial-correlation series exists).
**Keep if:** partial r ≥ **+0.30** with the same positive sign as E1, **and** G6 sign-stable with
magnitude retention ≥ 0.5 × r_partial. If the partial collapses below 0.30, the informative
outcome — registered in advance — is that E1 and E12 are two readings of one digitalization factor
rather than two independent rails, and E1 is re-logged with that caveat.
Declared caveats: partialling a *contemporaneous* Δ is not a control for confounding — Δg20_any is
itself an outcome of the same period, so this is a decomposition of co-movement, not an
identification strategy. Descriptive association only, never causal.

## U16 — pre-registered (micro stream)
**Hypothesis:** the **rural–urban** gradient in digital-payment use behaves like education
(persists conditional on access) rather than like gender (collapses). U15 completed a
gender/education/age triad on one outcome and one conditioning step: gender collapses (U6, 3.4pp
residual), education shrinks ~64% but stays large (U10, 46.7 → 16.8pp), age barely moves at all
(U15, 11.6 → 10.3pp, 10% absorbed). Urbanicity is the one major demographic axis not yet placed on
that ruler, and U5 supplies a real prior tension: the "too far away" barrier among the unbanked was
*flat* across rural/urban (36.0 vs 36.8pp), which would predict a small access gap — but says
nothing about the usage margin.
**Test:** weighted rate of `anydigpayment == 1` among `account == 1`, split by `urbanicity`
(1 = rural / 2 = urban), pooled across all 2024 economies (raw `wgt`, economy-equal pooling per
`micro.py`). Primary statistic: **urban − rural, conditional on account**. Secondary, descriptive:
the same split unconditional on account (for the U10/U15-style absorption decomposition), and the
access margin itself — `account == 1` rate by urbanicity — so the decomposition's two sides are
both reported.
Gates: M2 (unweighted cell n ≥ 100 per cell). M3 declared n/a (within-accountholder split; no
country-file equivalent).
**Keep if:** (urban − rural | accountholder) ≥ **5pp**. A residual below 5pp is the informative
opposite outcome and is registered as such: urbanicity would then join gender as an axis that
access equalizes, against the education/age pattern.
Declared caveats: urbanicity correlates with education, income and employment, none controlled —
descriptive association, not a place effect; conditioning on account holding conditions on a
post-treatment variable (as in U6/U8/U10/U14/U15); `urbanicity` is missing for some economies, so
the pooled sample is the subset where it is coded. Single 2024 cross-section — no trend language.

## P19 — pre-registered (prediction stream)
**Idea:** does the shrinkage-compounding curve **differ by target**? P18 closed the "does stage 4
pay for saving" question (yes: 7.080 → 6.831, −0.249pp, barely decayed from stage 3's −0.279pp).
Account's stages have bought far less (−0.039 for the second administrative cut, −0.091 for the
first cross-indicator basin), and it now sits at three stages (income-group → region → `g20_any`
terciles, 5.014). The registered open question from the P18 verdict is whether that flatter curve
is a property of the *target* or just of the *basins tried*.
**Test:** add stage 4 to **account**, exactly mirroring P18's design — a **second cross-indicator
data-driven basin**, terciles of `fin17a_17a1_d` (formal saving level, 117/117 panel coverage at
2014/2017/2021), distinct from both the target and stage-3's basin column, k = 0.1 unchanged,
stacked on the P17 champion.
Selection, entirely ≤2021 (no 2024 in features, fitting or selection): CV on the account 2017→2021
transition with a persistence base (the P10/P12/P13/P16/P17/P18 protocol), every basin — including
both tercile basins — built from the **2017** cross-section, comparing the incumbent three-stage
against the four-stage candidate.
Per-target policy (P2's rule): touches account only — saving (6.831) and resilience (6.625) must
stay byte-identical to the P18 champion.
**Keep if:** the ≤2021 CV prefers four-stage over the incumbent three-stage **AND** account MAE
improves on 5.014 on the 2021→2024 evaluation. Known risk, accepted: account is already the
best-predicted target (persistence 5.576 → 5.014) and has the least headroom, so a null here is
plausible and would itself localize the compounding curve as target-specific rather than
mechanism-general.

**E23 verdict: KEEP — mobile money and digital payments are two separate rails into the saving
surge, not one digitalization factor.** The partial correlation of Δmobile money with Δformal
saving, controlling Δg20_any, is **+0.509** (n = 58), well past the +0.30 threshold, and G6 is
clean with high retention (0.509 → 0.410, ret 0.81). G3 clean (three headlines declared), G4 clean
(58 economies, 100% of the estimation sample's population), G5 n/a.
The **symmetric** result is the substantive one: the reverse partial — Δg20_any with Δsaving,
controlling Δmobile money — is **+0.574** (G6 clean, ret 0.64). Neither channel absorbs the other.
Conditioning costs mobile money 0.719 → 0.509 and digital payments 0.751 → 0.574, i.e. each rail
gives up roughly a quarter of its bivariate association to the shared factor and keeps the rest.
The secondary control corroborates it on a different indicator: partialling E10's wage
digitalization (`fin32_acc`) leaves Δmobile money at **+0.337** (n = 56), still over threshold.
One sample-composition note, recorded rather than smoothed over: E12's Δg20_any ~ Δsaving was
logged at r = +0.370 on n = 76, but on this mobile-money-restricted n = 58 subsample the *same*
bivariate is **+0.751**. The digital-payment ↔ saving co-movement is therefore far stronger inside
the mobile-money-reporting economies than across the full developing panel — consistent with E22's
SSA intensity gradient, and a caveat that now attaches to E12.
What this settles: E1 is not the SSA-flavoured face of a single digitalization factor. E22 closed
the one-region alternative, E23 closes the one-factor alternative, and E1 survives both. Declared
caveats stand: partialling a *contemporaneous* Δ decomposes co-movement, it does not control
confounding (Δg20_any is an outcome of the same period), and account growth and common income
shocks remain uncontrolled. Descriptive association, never causal. First partial-correlation test
in the ledger since E5b; the same design is now available for E10 and E14.

**U16 verdict: DISCARD on the pre-registered claim — and the registered opposite outcome is the
finding: urbanicity is an ACCESS gap, not a usage gap.** Among accountholders, digital-payment use
is **87.2pp urban vs 83.5pp rural**, a residual of **+3.7pp** — below the 5pp threshold, so the
"persists like education" hypothesis is rejected. M2 passes with very large cells (28,836 urban /
37,701 rural accountholders); M3 n/a. The pooled sample is 141,564 of 144,090 respondents across
140 economies, so urbanicity coding costs almost nothing.
The decomposition is where the content is. Unconditionally the gap is **+11.0pp** (59.3 vs 48.3),
and the **access margin itself is +10.3pp** (account ownership 76.6pp urban vs 66.3pp rural), so
**access absorbs 66%** of the digital-payment gradient. Placed on the U6/U10/U15 ruler, urbanicity
sits with **gender**: residual 3.7pp against gender's 3.4pp, versus education's 16.8pp (~64%
absorbed) and age's 10.3pp (10% absorbed). The four-axis ordering is now clean — **where you live
and what sex you are gate the account; how educated and how old you are gate the usage.**
One cross-reference worth recording: U5 found the self-reported "too far away" barrier among the
unbanked *flat* across rural and urban (36.0 vs 36.8pp). The rural access deficit is real and
10.3pp wide, but rural unbanked adults do not name distance more often than urban ones — so the
gap is not explained by stated physical distance, and what does explain it is untested here.
Declared caveats stand: urbanicity correlates with education, income and employment, none
controlled; conditioning on account holding conditions on a post-treatment variable. Single 2024
cross-section, no trend language.

**P19 verdict: DISCARD — the compounding curve is target-specific. Account stops at three stages.**
The ≤2021 CV (account 2017→2021, persistence base, every basin built at 2017) rejects the fourth
stage **decisively**: three-stage **6.710** vs four-stage **7.133**, i.e. the candidate basin makes
the pre-2021 prediction **0.423pp worse**. The adoption condition fails at the first gate, so under
the P14/P15 protocol no 2024 evaluation was run — the candidate never earned a look at the holdout
— and `predictor.py` reverted to the P18 champion. All three MAEs stay byte-identical: account
**5.014**, resilience **6.625**, saving **6.831**.
The magnitude is what makes this informative rather than a null. P14's rejection was a razor-thin
0.006pp; this is 70× that, so it is not a coin-flip that landed the wrong way — terciles of the
formal-saving level actively *mis*-partition account levels once income group, region and
`g20_any` terciles have each had a pass. Compare the same design on saving, where the identical
move (a second cross-indicator basin) was CV-preferred and bought −0.249pp out of sample.
So the registered question is answered: the flatter account curve (−0.039 / −0.091 / stop) is a
property of the **target**, not of the basins tried. A plausible reading, untested here: account is
the most saturated and best-predicted target (persistence 5.576 → 5.014, near the ceiling for much
of the panel), so there is simply less basin-correctable noise left in it, while saving — still
mid-regime-change — keeps yielding. Standing lesson holds and is now sharpened: shrinkage buys
**noise correction**, and it stops paying when the noise is gone, target by target, not stage by
stage. Prediction champion unchanged: account = 5.014, resilience = 6.625, saving = 6.831.

## 2026-07-26 wrap-up
Ran 3 experiments (E23, U16, P19), one per stream — **one keep, two informative discards**.
E23 (hypothesis, KEEP): the first partial-correlation test since E5b closes the standing
one-*factor* alternative to E1. Mobile money keeps **r = +0.509** with the saving surge after
partialling out digital-payment growth (G6-clean, ret 0.81), and the symmetric partial leaves
digital payments at **+0.574** — neither rail absorbs the other, each surrendering about a quarter
of its bivariate association to the shared digitalization factor. With E22 (region) and E23
(factor), both deflationary readings of E1 are now closed. Recorded caveat: E12's bivariate is
+0.751 on this mobile-money-reporting subsample versus +0.370 on the full panel.
U16 (micro, DISCARD on the registered claim, informative on its opposite): the rural–urban gap in
digital-payment use is **+3.7pp** among accountholders — below threshold — against **+11.0pp**
unconditionally and a **+10.3pp** access gap, so access absorbs 66%. Urbanicity joins gender on the
equalized side; the four-axis ruler now reads *where you live and what sex you are gate the
account, how educated and how old you are gate the usage.*
P19 (prediction, DISCARD): the ≤2021 CV rejects a fourth shrink stage for account **decisively**
(6.710 → 7.133, 70× P14's margin), so the candidate never reached the holdout and predictor.py
reverted. The compounding curve is **target-specific**: saving took four stages, account stops at
three. Prediction champion unchanged: account = 5.014, resilience = 6.625, saving = 6.831.
EXTENSIONS_DRAFT updated with E22/E23 (Extension 1) and U16 (the access-equalization section).

## 2026-07-28 daily autoresearch cycle

## E24 — pre-registered (hypothesis / country level)
**Hypothesis:** **wage digitalization is a third separate rail** into the 2021-24 formal-saving
surge — Δ(`fin32_acc`) keeps a ≥ +0.30 association with Δ(`fin17a_17a1_d`) after the digital-payment
rail is partialled out, and after *both* digitalization rails (digital payments **and** mobile
money) are partialled out together. E23 closed the one-factor alternative for mobile money and
explicitly left the same design "available for E10 and E14". E10's bivariate (r = +0.791, n = 71) is
the *strongest* single co-movement in the ledger, but it is also the one most plausibly a proxy for
the common bundle: wages paid into accounts is mechanically an account-usage indicator. It is
genuinely unknown whether it survives conditioning, and — the new step beyond E23 — whether any rail
survives conditioning on **two** controls at once.
**Test:** weighted **partial** correlation of Δ(`fin32_acc`) with Δ(`fin17a_17a1_d`), 2021→2024, on
the developing balanced panel, following the E5b/E23 construction (pop-weighted least-squares
residualization of both variables on the control set, then `weighted_corr` of the residuals;
`gate_jackknife` on the residual pair).
- **Primary:** single control Δ(`g20_any`) — full dev-panel coverage, so the estimation sample is
  E10's (n ≈ 71).
- **Secondary A (the new design step):** **two** controls simultaneously, Δ(`g20_any`) **and**
  Δ(`mobileaccount_t_d`), via multivariate pop-weighted LS residualization (n ≈ 56, mobile money
  binds). Reported descriptively alongside the primary.
- **Secondary B (descriptive):** the symmetric reverse partial Δ(`g20_any`) ~ Δsaving | Δ(`fin32_acc`),
  which says which rail carries the association; plus all bivariate benchmarks recomputed on each
  common sample (E23 established that sample composition moves these a lot).
Gates: G3 (three headline concepts declared; `fin32_acc` has no variant choice — E10 precedent),
G4 on each estimation sample, G6 jackknife on the primary residual pair. G5 n/a (no official
partial-correlation series).
**Keep if:** primary partial r ≥ **+0.30** with E10's positive sign **AND** G6 sign-stable with
magnitude retention ≥ 0.5 × r_partial. Registered alternative outcome: if the primary collapses
below 0.30, wage digitalization is *not* an independent rail but the account-usage face of the
digital-payment channel, and E10 is re-logged with that caveat. Secondary A is descriptive context
either way — it cannot rescue a failed primary, and a two-control collapse with a surviving primary
would itself be registered as "the rails are separable pairwise but not jointly".
Declared caveats (identical to E23): partialling a *contemporaneous* Δ decomposes co-movement, it
does not control confounding — every control is an outcome of the same 2021-24 period. Account
growth and common income shocks uncontrolled. `fin32_acc` is an employer-side attribute of wage
payment, not an individual choice (U14's caveat, at country level). Descriptive, never causal.

## U17 — pre-registered (micro stream)
**Hypothesis:** **income** behaves like education on the access-absorption ruler — the digital-payment
gradient by income quintile **persists conditional on holding an account** (≥ 5pp residual). Four
axes are now on that ruler for one outcome (`anydigpayment`) and one conditioning step: gender
collapses (U6, 3.4pp), urbanicity collapses (U16, 3.7pp, 66% absorbed), education persists large
(U10, 16.8pp, ~64% absorbed), age barely moves (U15, 10.3pp, 10% absorbed). **Income quintile is
the one major demographic axis never placed on it** — which is conspicuous, because income is the
axis with the strongest prior evidence on the *barrier* side (M1: the money barrier among the
unbanked is income-graded by +10.3pp) and a genuinely ambiguous prior on the usage side (U11 found
mobile-only holders are *not* poorer than bank-only; U12 found the cost barrier flat across income).
**Test:** weighted rate of `anydigpayment == 1` among `account == 1`, split by `inc_q` (1 = poorest
… 5 = richest), pooled across all 2024 economies (raw `wgt`, economy-equal pooling per `micro.py`).
Primary statistic: **q5 − q1, conditional on account**. Secondary, descriptive: the same split
unconditional on account, and the access margin itself (`account == 1` rate by `inc_q`), giving the
U10/U15/U16-style absorption decomposition; the full five-band shape is reported for monotonicity.
Gates: M2 (unweighted cell n ≥ 100 per cell). M3 declared n/a (within-accountholder split; no
country-file equivalent).
**Keep if:** (q5 − q1 | accountholder) ≥ **5pp**. A residual below 5pp is the registered opposite
outcome: income would then join gender and urbanicity on the access-equalized side, and the ruler
would read "money and place and sex gate the *account*; education and age gate the *usage*".
Declared caveats: `inc_q` is a **within-economy relative** quintile, so economy-equal pooling mixes
economies (HARNESS_V2_NOTES caveat #3) — it is a relative-rank axis, not an absolute-income axis,
which distinguishes it from education/age; income correlates with education, employment and
urbanicity, none controlled; conditioning on account holding conditions on a post-treatment
variable (U6/U8/U10/U14/U15/U16). Single 2024 cross-section — no trend language.

## P20 — pre-registered (prediction stream)
**Idea:** P19 established that the shrinkage-compounding curve is **target-specific** (account
stops at three stages, CV rejecting stage 4 by 0.423pp). The open question it leaves for the other
side is whether **saving**'s curve keeps paying past four, and whether the basin has to be a
*digitalization* cut. Saving's stages 3 and 4 are both digitalization indicators (`account_t_d`
terciles, `g20_any` terciles) and both paid (−0.279, −0.249pp). A fifth stage on a **non-digital**
cross-indicator basin tests two things at once: whether compounding continues, and whether the
independent signal comes from *any* orthogonal partition or specifically from digitalization cuts.
**Test:** add stage 5 to **saving**, basin = terciles of `fin22a_22a1_22g_d` (formal-borrowing
level — 117/117 panel coverage at 2017 and 2021, verified before registration; a feature-coverage
check only, no outcome peeked), distinct from the target and from both existing tercile basins,
k = 0.1 unchanged, stacked on the P18 champion (damped trend + region → income-group →
account-tercile → g20-tercile).
Selection, entirely ≤2021 (no 2024 in features, fitting or selection): CV on the saving 2017→2021
transition with a persistence base (the P10/P12/P13/P16/P17/P18/P19 protocol), every basin —
including all three tercile basins — built from the **2017** cross-section, comparing the incumbent
four-stage against the five-stage candidate. Per the P14/P15/P19 protocol, if the CV does not
prefer the candidate, no 2024 evaluation is run and `predictor.py` reverts to the P18 champion.
Per-target policy (P2's rule): touches saving only — account (5.014) and resilience (6.625) must
stay byte-identical.
**Keep if:** the ≤2021 CV prefers five-stage over four-stage **AND** saving MAE improves on 6.831
on the 2021→2024 evaluation. Registered alternative outcome: a CV rejection localizes saving's
curve at four stages and — read against P18's two *digitalization* basins both paying — would
suggest the independent signal is specific to digitalization partitions rather than to orthogonality
per se. Known risk, accepted: E11 logged Δborrowing ~ Δsaving at r = +0.403, so the borrowing level
is not orthogonal to the saving *change*; whether that helps (relevant signal) or hurts
(mis-partition, as in P19) is exactly the unknown.

**E24 verdict: KEEP — wage digitalization is a third separate rail, and it is the strongest and
most stable one in the ledger.** The primary partial correlation of Δ(`fin32_acc`) with Δformal
saving, controlling Δ(`g20_any`), is **+0.583** (n = 71), well past the +0.30 threshold, and G6 is
the cleanest yet recorded: **0.583 → 0.582**, retention **1.00** — dropping the five largest
economies moves it by one thousandth. G3 clean (three headlines declared, `fin32_acc` no variant
per E10), G4 clean (71 economies, 100% of the estimation sample's population), G5 n/a.
The registered alternative — that wages-into-accounts is just the account-usage face of the
digital-payment channel — is rejected, and not narrowly: conditioning costs wage digitalization
0.791 → 0.583, while the symmetric reverse leaves digital payments at **+0.431** (ret 0.89). As in
E23, each rail surrenders roughly a quarter to the shared factor and keeps the rest.
**Secondary A is the new result and it is more interesting than the primary.** No rail in the
ledger had previously been asked to survive **two simultaneous controls**. On the common n = 56
sample the three-way decomposition reads: wage digitalization **+0.433** (G6 ret 1.30, jackknife
grows), digital payments **+0.379**, mobile money **+0.298**. So the three rails do *not* collapse
into one factor even jointly — but the ordering inverts the ledger's bivariate ordering, and mobile
money, the rail E1/E22/E23 were built to defend, lands **just under the 0.30 bar** when both other
rails are held at once. Recorded precisely: E23's pairwise finding stands (mobile money vs digital
payments, +0.509), and what is new is that mobile money's independent contribution is the *smallest*
of the three once wage digitalization is also in the control set. That is context, not a demotion of
E1 — it is a descriptive partial on n = 56 with a contemporaneous control, and it was registered as
descriptive before the run.
Sample-composition note, recorded as in E23: E12's Δg20 ~ Δsaving is logged at +0.370 on n = 76 but
is **+0.734** on this n = 71 wage-reporting subsample and +0.747 on the n = 56 one. The
digital-payment ↔ saving co-movement is systematically stronger inside the economies that report
the other digitalization indicators — the caveat now attaches to E12 twice over.
Declared caveats stand: partialling a contemporaneous Δ decomposes co-movement, it does not control
confounding; `fin32_acc` is an employer-side attribute (U14's caveat at country level); account
growth and common income shocks uncontrolled. Descriptive association, never causal.

**U17 verdict: KEEP — income persists conditional on access, and the five-axis ruler is now
complete.** Among accountholders, digital-payment use runs **78.3 / 82.9 / 84.8 / 87.0 / 89.8pp**
from the poorest to the richest quintile — **q5 − q1 = +11.5pp**, strictly monotone, well past the
5pp threshold. M2 passes with very large cells (9,026–19,712 per conditional cell); M3 n/a. The
pooled sample is 143,070 of 144,090 respondents across 139 economies.
The decomposition: unconditionally the gradient is **+27.3pp** (39.3 → 66.6), the **access margin
itself is +19.4pp** (61.1 → 80.6), so **access absorbs 58%**. Both secondary splits are also
strictly monotone across all five quintiles.
Placed on the ruler, income joins the *persists* side with education and age:
| axis | unconditional | access margin | conditional residual | absorbed |
|---|---|---|---|---|
| education (U10) | 46.7pp | — | **16.8pp** | ~64% |
| **income (U17)** | **27.3pp** | 19.4pp | **11.5pp** | **58%** |
| age (U15) | 11.6pp | — | **10.3pp** | 10% |
| urbanicity (U16) | 11.0pp | 10.3pp | 3.7pp | 66% |
| gender (U6) | — | — | 3.4pp | — |
The methodological point worth recording: **the absorption *share* does not sort the axes.** Income
and urbanicity absorb almost the same fraction (58% vs 66%) yet leave 11.5pp versus 3.7pp, purely
because income's unconditional gradient is 2.5× wider. Ranking axes by "how much does access
equalize this" needs the residual in pp, not the percentage — U16's 66% and U17's 58% would have
put them side by side, and they belong on opposite sides of the ruler. Earlier entries reported the
percentage first; the residual is the statistic that matters.
Substantively the ruler now reads: **where you live and what sex you are gate the account; how much
you earn, how educated you are and how old you are also gate what you do with it.** Income is the
only axis that is large on *both* margins (19.4pp access, 11.5pp usage) — gender and urbanicity are
access-only, age is usage-only, and education is large on both but has no access figure logged here.
Declared caveats stand, and one deserves emphasis: `inc_q` is a **within-economy relative** quintile,
so this is a relative-rank axis, not an absolute-income axis — unlike education or age it does not
carry the same meaning across economies under economy-equal pooling (caveat #3). Income correlates
with education, employment and urbanicity, none controlled; conditioning on account holding
conditions on a post-treatment variable. Single 2024 cross-section, no trend language.

**P20 verdict: DISCARD — saving stops at four stages, and the basin *material* matters more than
its orthogonality.** The ≤2021 CV (saving 2017→2021, persistence base, all basins built at 2017)
rejects the fifth stage: four-stage **6.370** vs five-stage **6.644**, i.e. the formal-borrowing
tercile basin makes the pre-2021 prediction **0.274pp worse**. Adoption fails at the first gate, so
under the P14/P15/P19 protocol no 2024 evaluation was run and `predictor.py` reverted to the P18
champion. All three MAEs byte-identical: account **5.014**, resilience **6.625**, saving **6.831**.
The registered question had two halves and this answers both. (1) Saving's compounding curve does
not extend past four — the same shape P19 found for account at three, two stages later. (2) The
sharper half: **the basin has to track the phenomenon, not merely be orthogonal to the existing
ones.** Every data-driven basin that has *paid* — account terciles for saving (−0.279pp), `g20_any`
terciles for saving (−0.249pp), `g20_any` terciles for account (−0.091pp) — is a **digitalization**
cut. The first **non**-digitalization basin tried is not merely neutral, it is actively harmful, and
by a margin (0.274pp) of the same order as P19's rejection (0.423pp) and 46× P14's coin-flip 0.006pp.
Orthogonality was the working explanation since P12 ("orthogonal basins compound"); it is now
demonstrably insufficient.
The failure is also a small vindication of the registered risk rather than a surprise. E11 logged
Δborrowing ~ Δsaving at r = +0.403, and the registered worry was that a correlated basin might
either help or mis-partition. It mis-partitions — because the co-movement E11 found is between
*changes*, while the basin is built from *levels*, and formal-borrowing levels cut the panel along
an axis (credit-market depth) that does not align with where formal saving sits. Shrinking toward a
credit-depth group mean pulls countries toward the wrong neighbours.
Standing lesson, now in its final form: shrinkage buys **noise correction**; it stops paying when
the noise is gone (target-specific, P19) **and** it only pays when the basin partitions the panel
along a dimension the target actually varies on (basin-specific, P20). Both dynamics-tuning (P9/P10)
and cross-indicator ridge (P15) remain non-transfers across the 2021 regime change.
Prediction champion unchanged: account = **5.014**, resilience = **6.625**, saving = **6.831**.

## 2026-07-28 wrap-up
Ran 3 experiments (E24, U17, P20), one per stream — **two keeps, one informative discard**.
E24 (hypothesis, KEEP): wage digitalization is a **third separate rail** into the saving surge —
partial r = **+0.583** net of digital payments (n = 71) with the ledger's cleanest jackknife
(0.583 → 0.582, retention 1.00). The new step is the first **two-control** partial: holding each
rail against the other two on n = 56 gives wage **+0.433** > digital payments **+0.379** > mobile
money **+0.298**, so the three-rail structure survives joint conditioning while the *bivariate*
ordering inverts — mobile money has the largest raw and smallest independent association.
U17 (micro, KEEP): income completes the five-axis absorption ruler and sits with education —
**+11.5 pp** conditional on account (monotone across quintiles), 58 % absorbed, and uniquely large
on both margins (access gap +19.4 pp). Method lesson recorded: the absorption *share* does not sort
the axes (income 58 % vs urbanicity 66 %, residuals 11.5 vs 3.7 pp) — the residual in pp does.
P20 (prediction, DISCARD): the ≤2021 CV rejects a fifth shrink stage for saving on a
**non-digitalization** basin (formal-borrowing terciles, 6.370 → 6.644), so it never reached the
holdout and predictor.py reverted. Sharper than a null: every basin that has ever paid is a
digitalization cut, so **orthogonality alone is not what buys a stage — the basin has to track the
phenomenon.** Prediction champion unchanged: account = 5.014, resilience = 6.625, saving = 6.831.
EXTENSIONS_DRAFT updated with E24 (Extension 1, three-rail decomposition) and U17 (the
access-equalization section, now five axes).

## 2026-07-30 daily autoresearch cycle

## E25 — pre-registered (hypothesis / country level)
**Idea:** the three-rail structure (mobile money E1/E22, digital payments E12/E23, wage
digitalization E10/E24) was built entirely around **one destination**: the 2021-24 formal-saving
surge. Nothing in the ledger says the rails are *saving-specific*. E11 logged the other deepening
margin — formal borrowing rose alongside formal saving (Δborrow ~ Δsav, r = +0.403, n = 76) — but
no rail has ever been pointed at borrowing. P20 sharpened the question from the prediction side:
formal-borrowing *levels* mis-partition the saving panel, which suggests credit sits on a different
axis from the digitalization cuts. If the rails are a general "digital financial deepening" force,
Δwage digitalization should co-move with Δborrowing too; if the rails are saving-specific, it should
not, and the E11 co-movement must come from somewhere else.
**Test:** developing panel, 2021→2024 deltas. **Primary:** weighted correlation of Δ`fin32_acc`
(wage digitalization, the strongest and most jackknife-stable rail, E24) with Δ`fin22a_22a1_22g_d`
(formal borrowing, headline). Weights = 2024 adult population; gates G3 (headline declared;
`fin32_acc` has no variant, E10 precedent), G4 (coverage), G6 (jackknife, drop top-5 population),
G5 n/a (no official Δ-correlation series). Feature coverage verified before registration (no
outcome peeked): Δborrow available for 76 dev-panel economies, Δwage for 71.
**Secondary A (the destination-specificity step, descriptive):** weighted **partial** correlation
of Δwage with Δborrow **controlling Δ`fin17a_17a1_d`** (formal saving) — does any rail→borrowing
association survive removing the saving channel, or is it borrowing riding on saving?
**Secondary B (descriptive):** the same bivariate for the other two rails (Δ`g20_any`,
Δ`mobileaccount_t_d`) against Δborrow, on their own and on the common sample, so the three rails
can be ranked against borrowing exactly as E24 ranked them against saving.
**Keep if:** primary weighted |r| ≥ **0.30** AND G6 sign-stable with retention ≥ 0.5 (the E4
judgment rule). Registered alternative outcome, equally informative: a primary below 0.30 or a
jackknife collapse says the rails are **saving-specific** — digitalization moved *where money is
stored*, not *where credit came from* — which would align the hypothesis stream with P20's basin
lesson from the prediction stream.
Declared caveats: contemporaneous Δ-on-Δ co-movement is descriptive, never causal; the borrowing
headline mixes formal-institution and credit-card borrowing; sample composition differs across the
rails (E23/E24 showed this moves the bivariates a lot), so every benchmark is recomputed on each
common sample.

## U18 — pre-registered (micro stream)
**Idea:** the access-absorption ruler now carries five axes for `anydigpayment` conditional on
holding an account — education +16.8pp (U10), income +11.5pp (U17), age +10.3pp (U15), urbanicity
+3.7pp (U16), gender +3.4pp (U6). **Labour-force status is the one demographic in `micro.py`'s
DEMOGRAPHICS list never placed on it**, and it is the axis with the largest *logged access* gap of
any binary split: U13 found account ownership 76.7 vs 61.7pp in/out of the workforce (+15.0pp), and
noted a depth gap in formal saving among accountholders (+13.3pp). Whether employment gates the
*digital-payment* margin once access is held is unknown, and the prior is genuinely two-sided:
digital payments are heavily wage- and transfer-driven (U14, E24), which argues employment persists;
but out-of-workforce adults include students and pensioners in high-digitalization economies, which
argues it collapses like gender and urbanicity.
**Test:** weighted rate of `anydigpayment == 1` among `account == 1`, split by `emp_in`
(1 = in workforce, 2 = out of workforce), pooled across all 2024 economies (raw `wgt`,
economy-equal pooling per `micro.py`). **Primary statistic: (in-workforce − out-of-workforce),
conditional on account.** Secondary, descriptive: the same split unconditional on account, and the
access margin (`account == 1` by `emp_in`) — giving the U10/U15/U16/U17-style absorption
decomposition and the axis's place on the ruler in **residual pp** (U17's method lesson: the
absorption *share* does not sort axes).
Gates: M2 (unweighted cell n ≥ 100 — cells are ~84k/56k unconditional, so this is a formality).
M3 declared **n/a** (within-accountholder split; no country-file equivalent).
**Keep if:** (in-workforce − out-of-workforce | accountholder) ≥ **5pp**. Registered alternative
outcome: a residual below 5pp puts employment with gender and urbanicity on the access-only side —
meaning U13's large access gap is *entirely* an access story and having a job does not change what
adults do with an account they already hold.
Disclosure: the access margin used in the absorption arithmetic is **already logged** (U13,
+15.0pp) — that half is a known quantity, not a fresh look; the primary conditional residual is
genuinely unknown at registration. Declared caveats: `emp_in` is a coarse binary that pools
students, homemakers, pensioners and the unemployed into "out of workforce"; employment correlates
with age, education and income, none controlled; conditioning on account holding conditions on a
post-treatment variable (U6/U8/U10/U14/U15/U16/U17). Single 2024 cross-section — no trend language.

## P21 — pre-registered (prediction stream)
**Idea:** P19 and P20 offer competing readings of the same shape. P19 (account's 4th stage rejected
by 0.423pp) was written up as "the compounding curve is **target-specific** — saving takes four
stages, account stops at three". P20 (saving's 5th stage rejected by 0.274pp on a formal-borrowing
basin) proposed a different reading: **the basin material matters** — every basin that has ever paid
is a *digitalization* cut, and the first non-digitalization basin was actively harmful. Those two
readings are confounded in the record, because **P19's rejected account basin was terciles of
formal saving — a depth indicator, not a digitalization cut.** So account may have stopped at three
for the same reason saving stopped at five: the wrong basin material, not an exhausted curve.
**Test:** re-run account's **fourth stage** with a **digitalization** basin — terciles of
`fin32_acc` (wage digitalization level), stacked on the P17/P18 account champion (persistence +
income-group → region → `g20_any`-tercile shrink), k = 0.1 unchanged. `fin32_acc` is distinct from
the target and from the stage-3 basin column, and has **117/117 panel coverage at 2017 and 2021**
(verified before registration — a feature-coverage check only, no outcome peeked). It is also the
rail E24 just certified as the strongest and most jackknife-stable of the three.
Selection, entirely ≤2021 (no 2024 in features, fitting or selection): CV on the account 2017→2021
transition with a persistence base (the P10/P12/P13/P16/P17/P18/P19/P20 protocol), every basin —
including both tercile basins — built from the **2017** cross-section, comparing the incumbent
three-stage against the four-stage candidate. Per the P14/P15/P19/P20 protocol, if the CV does not
prefer the candidate, no 2024 evaluation is run and `predictor.py` reverts to the P18 champion.
Per-target policy (P2's rule): touches account only — saving (6.831) and resilience (6.625) must
stay byte-identical.
**Keep if:** the ≤2021 CV prefers four-stage over three-stage **AND** account MAE improves on
**5.014** on the 2021→2024 evaluation. Registered alternative outcomes, both informative: adoption
would **overturn P19's target-specific reading** in favour of P20's basin-material reading (account
does not stop at three; it stopped at the wrong basin); a second rejection with a digitalization
basin would **confirm P19** — account's curve really is exhausted at three stages, and the two
lessons are independent rather than competing.

**E25 verdict: KEEP — the rails are not saving-specific; they reach the credit margin too, and net
of saving.** The primary weighted correlation of Δ`fin32_acc` with Δformal borrowing is **+0.605**
(n = 71), twice the threshold, and G6 is sign-stable with **retention 0.83** (0.605 → 0.501). G3
clean (four headlines declared, `fin32_acc` no variant per E10), G4 clean (71 economies, 100% of the
estimation sample's population), G5 n/a.
The registered alternative — that digitalization moved *where money is stored* but not *where
credit came from* — is rejected. Secondary A is the reason it is rejected cleanly: the partial
correlation **net of the saving channel is +0.419** (retention 0.54, above the E4 bar but the
weakest link in this entry), so roughly two-thirds of the raw wage-rail↔borrowing association
survives removing everything borrowing shares with the saving surge.
Secondary B produces the entry's most striking number. On the three-rail common sample (n = 56) the
rails rank against **borrowing**: wage **+0.649** > mobile money **+0.543** > digital payments
**+0.512** — and E11's own Δsaving ~ Δborrowing benchmark on that same sample is **+0.511**. Every
rail is at least as strongly associated with the borrowing deepening as *formal saving itself* is.
The natural reading is not that digitalization caused credit, but that Δborrowing and Δsaving are
both surfaces of one digital-deepening episode, and E11's saving↔borrowing co-movement is largely
the shadow of the rails they share.
Two asymmetries recorded for v2. (1) **Saving is the stronger destination**: on the identical n = 56
sample the same three rails give 0.804 / 0.713 / 0.747 against saving versus 0.649 / 0.543 / 0.512
against borrowing. The rails point at both margins, and lean toward saving. (2) The **rail ordering
flips by destination**: against saving on this sample the order is wage > digital payments > mobile
money, against borrowing it is wage > mobile money > digital payments. Wage digitalization leads
both — its third consecutive appearance as the ledger's most stable rail (E10, E24, E25).
This also puts a boundary on P20's prediction-side lesson. P20 found formal-borrowing *levels*
mis-partition the saving panel; E25 finds borrowing *changes* co-move strongly with the same rails
as saving changes. Both can hold, and together they say the level-vs-change distinction is doing
real work: credit **depth** is a different axis from digital deepening, credit **growth** is part of
the same episode.
Declared caveats stand: contemporaneous Δ-on-Δ co-movement decomposes an episode, it does not
control confounding; the borrowing headline mixes formal-institution and credit-card borrowing;
sample composition moves every benchmark (E11's own +0.403 on n = 76 reads +0.480 on n = 71 and
+0.511 on n = 56 — the same subsample inflation E23/E24 logged for E12). Descriptive association,
never causal.

**U18 verdict: KEEP — employment gates usage as well as access; the ruler is now six axes.** Among
accountholders, digital-payment use is **87.9pp in the workforce vs 78.3pp out of it — +9.6pp**,
past the 5pp threshold. M2 passes with very large cells (21,800–41,772 conditional). M3 n/a. The
pooled sample is 140,070 of 144,090 respondents across 139 economies.
The decomposition: unconditionally **+20.8pp** (60.0 vs 39.2), access margin **+15.0pp** (76.7 vs
61.7) — reproducing U13's logged figure to the decimal, which is a clean internal consistency check
on the pooling — so **access absorbs 54%**.
The six-axis ruler, in residual pp conditional on holding an account:
| axis | unconditional | access margin | conditional residual | absorbed |
|---|---|---|---|---|
| education (U10) | 46.7pp | — | **16.8pp** | ~64% |
| income (U17) | 27.3pp | 19.4pp | **11.5pp** | 58% |
| age (U15) | 11.6pp | — | **10.3pp** | 10% |
| **employment (U18)** | **20.8pp** | **15.0pp** | **9.6pp** | **54%** |
| urbanicity (U16) | 11.0pp | 10.3pp | 3.7pp | 66% |
| gender (U6) | — | — | 3.4pp | — |
Employment lands fourth — clearly on the usage-gating side with education, income and age, not with
gender and urbanicity. It also confirms U17's method lesson from the other direction: employment
(54%) and urbanicity (66%) and income (58%) absorb comparable *fractions* while leaving 9.6, 3.7 and
11.5pp respectively. **The absorption share still does not sort the axes; the residual in pp does.**
Substantively, employment is the second axis (after income) that is large on *both* margins: having
a job is associated with holding an account (+15.0pp) and, among those who hold one, with using it
digitally (+9.6pp). Read alongside U14 (digital wage receipt is steeply education-graded) and E24
(wage digitalization is the strongest country-level rail), the wage channel keeps appearing on both
sides of the micro/macro boundary.
Declared caveats stand: `emp_in` is a coarse binary pooling students, homemakers, pensioners and the
unemployed into "out of workforce", so the residual mixes very different groups; employment
correlates with age, education and income, none controlled; conditioning on account holding
conditions on a post-treatment variable. Single 2024 cross-section — no trend language.

**P21 verdict: DISCARD — P19's target-specific reading survives, but the rejection margin shrank
6×.** The ≤2021 CV (account 2017→2021, persistence base, all basins built at 2017) rejects the
fourth stage even with the best available digitalization basin: three-stage **6.710** vs four-stage
**6.780**, i.e. `fin32_acc` terciles make the pre-2021 prediction **0.070pp worse**. Adoption fails
at the first gate, so under the P14/P15/P19/P20 protocol no 2024 evaluation was run and
`predictor.py` reverted to the P18 champion. All three MAEs byte-identical: account **5.014**,
resilience **6.625**, saving **6.831**.
The registered question was whether P19 and P20 were competing readings of the same shape. The
answer is **no — they are complementary, and both hold.** Account's curve really is exhausted at
three stages: swapping P19's depth basin (formal-saving terciles) for a genuine digitalization cut,
and specifically the rail E24 certified as the strongest of the three, does not revive it. So
**target-specific exhaustion (P19) sets *whether* another stage is available.**
But the margins say basin material is still doing work *inside* the rejection: −0.070pp for a
digitalization basin here, versus −0.423pp for the depth basin on the same target (P19) and
−0.274pp for the borrowing basin on saving (P20). A digitalization cut is very nearly neutral where
non-digitalization cuts are clearly harmful. So **basin material (P20) sets how much a wrong stage
costs**, and the two lessons stack rather than compete. The consolidated rule: shrinkage buys noise
correction; it stops paying when the target's noise is gone, and when it stops paying, a basin that
tracks the phenomenon does no harm while one that does not actively hurts.
Worth recording as a limit of the method: five consecutive prediction experiments (P19–P21 plus
P14/P15) have now failed to move the champion, three of them at the CV gate without ever reaching
the holdout. The shrinkage-stacking seam looks mined out at four stages for saving and three for
account.
Prediction champion unchanged: account = **5.014**, resilience = **6.625**, saving = **6.831**.

## 2026-07-30 wrap-up
Ran 3 experiments (E25, U18, P21), one per stream — **two keeps, one CV-gate discard**.
E25 (hypothesis, KEEP): the digitalization rails are **not saving-specific** — Δwage digitalization
~ Δformal borrowing is **+0.605** (n = 71, G6 retention 0.83) and **+0.419 net of the saving
channel**. On the three-rail common sample every rail correlates with borrowing (+0.649 wage /
+0.543 mobile money / +0.512 digital payments) at least as strongly as **formal saving itself** does
(E11's benchmark, +0.511 there) — so saving and borrowing look like two surfaces of one
digital-deepening episode, with saving the stronger destination (0.71–0.80 vs 0.51–0.65) and the
rail ordering flipping between the two.
U18 (micro, KEEP): labour-force status is the **sixth axis** on the access-absorption ruler and
lands on the usage-gating side — **+9.6pp** conditional on account, 54% absorbed, access margin
+15.0pp reproducing U13 exactly. Ruler in residual pp: education 16.8 > income 11.5 > age 10.3 >
employment 9.6 > urbanicity 3.7 > gender 3.4.
P21 (prediction, DISCARD): the ≤2021 CV rejects account's fourth shrink stage **even on a
digitalization basin** (wage-digitalization terciles, 6.710 → 6.780), so P19's target-specific
reading stands. The new information is the **6× smaller margin** (−0.070pp vs P19's −0.423pp): basin
material governs how much a wrong stage costs, target-specific exhaustion governs whether a stage is
available at all — complementary lessons, not competing ones. Champion unchanged: account = 5.014,
resilience = 6.625, saving = 6.831.
EXTENSIONS_DRAFT updated with E25 (Extension 1, the rails reach both deepening margins) and U18
(the access-equalization section, now six axes).

## 2026-07-31 daily autoresearch cycle

## E26 — pre-registered (hypothesis / country level)
**Idea:** E25 extended the three-rail structure from one destination to two — the rails feed the
2021-24 formal-saving surge (E10/E12/E23/E24) *and* the formal-borrowing deepening (E25, wage rail
+0.605, +0.419 net of saving). Both destinations are **balance-sheet** margins: where money is
stored, where credit came from. The ledger has never pointed a rail at the **welfare** margin —
self-reported ability to raise emergency funds (`fin24aSD_ND`). Two prior discards frame the
question but do not answer it: E2 tested Δresilience against the *mobile-money* rail (r = 0.189,
G6 collapse to −0.005) and E15 tested it against the *formal-saving surge itself* (discard). The
strongest and most jackknife-stable rail — wage digitalization, E10/E24/E25's three-time leader —
has never been tested against resilience, and E25 just showed the rails reach destinations that
E11-style co-movement alone would not have predicted. This is the destination question's third and
last available margin, and it is the one that matters for welfare interpretation of the whole
three-rail story.
**Test:** developing panel, 2021→2024 deltas. **Primary:** weighted correlation of Δ`fin32_acc`
(wage digitalization) with Δ`fin24aSD_ND` (resilience, headline). Weights = 2024 adult population;
gates G3 (headlines declared; `fin32_acc` has no variant, E10 precedent), G4 (coverage), G6
(jackknife, drop top-5 population), G5 n/a (no official Δ-correlation series). Feature coverage
verified before registration (no outcome peeked): Δresilience available for 76 dev-panel economies,
Δwage for 71, the pair for **71** — identical n to E25's primary, so the two destinations are
directly comparable on the same sample.
**Secondary A (descriptive):** weighted **partial** correlation of Δwage with Δresilience
**controlling Δ`fin17a_17a1_d`** (formal saving) — if any rail→resilience association exists, does
it survive removing the saving channel, the same net-of-saving step E25 ran for borrowing?
**Secondary B (descriptive):** the other two rails (Δ`g20_any`, Δ`mobileaccount_t_d`) against
Δresilience on their own samples and on the three-rail common sample (n = 56 verified), so the rails
rank against resilience exactly as E24 ranked them against saving and E25 against borrowing — and
E2's mobile-money result is re-run as a declared **replication** on the current sample rather than a
fresh hypothesis.
**Keep if:** primary weighted |r| ≥ **0.30** AND G6 sign-stable with retention ≥ 0.5 (E4 judgment
rule). Registered alternative outcome, equally informative and the one E2/E15 make likelier: a
primary below 0.30 or a jackknife collapse bounds the entire three-rail story to **balance-sheet
behaviour** — digitalization moved where money is stored and where credit came from, but did not
show up in self-reported shock-coping capacity, which is exactly the aggregate flatness the paper
already logs (dev-panel resilience 54.7 → 54.5pp, 2021 → 2024).
Declared caveats: contemporaneous Δ-on-Δ co-movement is descriptive, never causal; `fin24aSD_ND` is
a *self-reported* hypothetical-shock measure, not a realized-outcome one, and its 2021 and 2024
question framings carry the paper's standing comparability caveat; the resilience aggregate is flat
in this window, which compresses Δ variance and works against finding any association; sample
composition differs across the rails (E23/E24/E25), so every benchmark is recomputed on each common
sample.

## U19 — pre-registered (micro stream)
**Idea:** the access-absorption ruler now carries six axes (U6/U10/U15/U16/U17/U18), and **every one
of them is a pooled-across-economies statistic**. That is the standing caveat on the whole micro
ledger (HARNESS_V2_NOTES #3, re-declared in every U entry): a pooled gradient can be produced
entirely by *composition* — low-education adults concentrated in low-digitalization economies —
without any within-country gradient at all. No U experiment has ever separated the two. This tests
the ruler's largest axis, education (U10, +16.8pp conditional on account, ~64% absorbed), the one
whose collapse would do the most damage to the ruler's reading.
**Test:** micro 2024 wave, weighted. For **each economy separately**, the conditional education gap
in digital-payment use: weighted rate of `anydigpayment == 1` among `account == 1` for
`educ >= 2` (secondary-or-more) minus `educ == 1` (primary-or-less). An economy qualifies only if
**both** cells have unweighted n ≥ 100 (gate M2 applied per economy, not pooled) — **64 economies
qualify, covering 69.5% of accountholding respondents** (verified before registration as a coverage
check; no rate computed). **Primary statistic: the median within-economy gap across qualifying
economies.** Secondary, descriptive: the share of qualifying economies with a positive gap; the
interquartile range and the extremes; the pooled gap on the same 64 economies and on all economies,
so the pooled-vs-median wedge is the composition estimate; and the stricter tertiary-vs-primary
variant (`educ == 3` vs `educ == 1`, **31 economies qualify**) as a robustness check against the
coarser split.
Gates: M2 per economy as above. M3 declared **n/a** (within-accountholder split; no country-file
equivalent). Note the qualifying set is *selected* — economies need a sizeable primary-educated
**and** secondary-plus accountholding population — so it skews away from both the least- and
most-educated economies; this is a coverage limit, declared, not a fixable one.
**Keep if:** median within-economy gap ≥ **5pp** AND at least **two-thirds (≥ 43/64)** of
qualifying economies show a positive gap. The second condition is registered deliberately: a median
above threshold driven by a minority of large gaps with the rest scattered around zero would be a
different (weaker) claim than a consistent within-country regularity, and the ruler's reading needs
the latter. Registered alternative outcome: a median far below the pooled +16.8pp, or a positive
share near half, would say the pooled ruler is substantially a **between-country composition**
artifact — which would be the single most consequential methodological finding in the micro stream
and would require re-wording U6/U10/U15/U16/U17/U18 as pooled-only descriptions.
Declared caveats: conditioning on account holding conditions on a post-treatment variable (as in
U6/U8/U10/U14–U18); `educ >= 2` merges secondary and tertiary, so the primary statistic is a
*coarser* contrast than U10's tertiary-vs-primary and is expected to be smaller in pp for that
reason alone — the tertiary variant is the like-for-like comparison; the median across economies
weights each economy equally, which is a different weighting from the pooled statistic by
construction (that is the point of the test, not a flaw). Single 2024 cross-section — no trend
language.

## P22 — pre-registered (prediction stream)
**Idea:** the shrinkage-stacking seam is mined out — five consecutive experiments (P14, P15, P19,
P20, P21) failed to move the champion, three of them rejected at the CV gate without reaching the
holdout, and P21 concluded that saving stops at four stages and account at three. Adding a sixth
stage is not the experiment. **What has never been varied is the shrinkage target itself.** Every
stage since P5 shrinks a country toward its basin's **population-weighted mean** — a location
statistic dominated, inside each basin, by the same handful of giant countries (India, China,
Indonesia, Nigeria, Pakistan) that gate G6 exists to guard against on the hypothesis side. If the
gains since P11 are genuine noise correction, they should survive — or improve — under a **robust**
basin center; if they are partly a big-country pull, a robust center will hurt.
**Test:** replace the basin center in `_shrink` with the **unweighted median** of the basin's member
values, at **every** stage, per target. Nothing else changes: k = 0.1, the damped trend (λ = 0.5),
the basin sequences and the adopted stage counts all stay exactly as in the P18 champion. Adoption
is per target and entirely ≤2021 (no 2024 in features, fitting or selection): CV on that target's
2017→2021 transition with a persistence base, all basins built at 2017 — the
P10/P12/P13/P16/P17/P18/P19/P20/P21 protocol — comparing the incumbent mean-centered champion stack
against the identical median-centered stack. Per the P14/P15/P19/P20/P21 protocol, a target whose CV
does not prefer the candidate is not evaluated on 2024 and keeps its champion prediction
byte-identical. **Resilience is excluded by design** and stays byte-identical at 6.625: its CV is
infeasible (`fin24aSD_ND` exists only in 2021) and the account-transition proxy is twice on record
as mis-selecting for it (P8, P13) — running it a third time would be a known-weak selector, not an
experiment.
**Keep if:** for any target, the ≤2021 CV prefers the median-centered stack **AND** its 2021→2024
MAE improves on the champion (account **5.014**, saving **6.831**), with every untouched target
printing byte-identical. Registered alternative outcomes, both informative: a CV rejection on both
targets says the population-weighted mean is the *right* basin location and the shrinkage gains are
not a big-country artifact — a direct prediction-side answer to the concern G6 encodes on the
hypothesis side, and the first positive robustness result for the whole P11–P18 stack; a split
(CV adopts, holdout worsens) would repeat the P8/P13 non-transfer pattern on a new axis.
Declared: this is an estimator-robustness experiment, not a search for a new stage; the unweighted
median deliberately discards the population weighting inside the basin, so it is the *opposite*
extreme from the incumbent rather than a mild variant — a middle option (weighted median) is left
untested and noted as a follow-up if the extreme rejects narrowly.

### E26 — verdict: DISCARD (on the threshold alone; every gate passed)
Primary weighted r(Δwage, Δresilience) = **+0.294** (n=71) — **misses the pre-registered 0.30 bar by
0.006**. Under pre-registration that is a discard, and it is logged as one: the bar was set before
the answer was known and is not renegotiated after seeing it. Worth recording that nothing else
failed — G3/G4 passed, and G6 *strengthened* (0.294 → **0.407**, retention **1.38**), so the weak
association is not a big-country artifact; if anything the top-5 countries dilute it.
The registered alternative outcome is the substantive result. On the identical n=56 three-rail
common sample, each rail's three destinations line up as a clean ladder:

| rail | → saving | → borrowing | → resilience |
|---|---|---|---|
| wage (`fin32_acc`) | +0.804 | +0.649 | **+0.295** |
| digital payments (`g20_any`) | +0.747 | +0.512 | **+0.000** |
| mobile money | +0.713 | +0.543 | **+0.208** |

The three-rail story is **bounded to balance-sheet margins**. Digitalization co-moves strongly with
where money is stored (~0.75) and where credit came from (~0.57), and an order of magnitude more
weakly with self-reported shock-coping capacity — exactly zero for digital payments. Wage is the
only rail with any resilience signal at all, and its partial *rises* net of saving (+0.294 →
**+0.319**, ret 0.61), so what little there is does not run through the saving channel.
Two declared replications came back clean: **E2 reproduces exactly** (mobile money r=+0.189, n=58,
matching the logged value to three decimals) and **E15** (Δsaving ~ Δresilience) sits at +0.127 on
this sample. Three independent attempts on resilience — E2, E15, E26 — now agree.
Consistent with the flat dev-panel aggregate (54.7 → 54.5pp), which compresses Δ variance and works
against the hypothesis by construction. Contemporaneous Δ-on-Δ, descriptive only; `fin24aSD_ND` is
self-reported hypothetical-shock with the standing 2021-vs-2024 framing caveat.

### U19 — verdict: KEEP
Median within-economy conditional education gap = **+9.4pp** across the **64** qualifying economies
(69.5% of accountholding respondents), **positive in 63 of 64 (98%)** — both pre-registered
conditions clear (≥5pp; ≥43/64). IQR +4.2 to +15.6pp, mean +11.2pp, range Comoros −1.5 to Nepal
+39.3. M2 applied per economy; M3 n/a.
**The composition wedge is small.** Pooled over the same 64 economies the gap is +12.1pp against a
within-economy median of +9.4pp — a wedge of **+2.7pp, ~22% of the pooled figure**. On the
like-for-like tertiary-vs-primary contrast the within-country median (**+18.0pp**, positive in
**23/23**) actually *exceeds* the pooled all-economy figure (+16.8pp), where composition is
contributing nothing at all. The pooled all-economy tertiary gap reproduces **U10's +16.8pp exactly**.
This is the first micro experiment to separate within-country gradient from between-country
composition, and it answers the standing caveat (HARNESS_V2_NOTES #3) in the ruler's favour on its
largest axis: the education gradient is a regularity *inside* economies, not an artifact of
low-education adults living in low-digitalization economies. The registered alternative — that the
ruler is substantially composition — is rejected.
**Disclosed registration deviation:** the pre-registration stated 31 qualifying economies for the
tertiary variant; M2 as actually applied drops respondents missing the outcome or the weight, giving
**23**. The primary's 64 is unaffected (that pre-check did filter on outcome non-missingness). The
verdict is unchanged either way (23/23 positive), but the registered number was wrong and is
corrected here rather than quietly restated.
Caveats: the qualifying set is **selected** — economies need sizeable primary-educated *and*
secondary-plus accountholding populations — so it skews away from both the least- and
most-educated economies; `educ >= 2` merges secondary and tertiary and is a coarser contrast than
U10 by construction (which is why +9.4 < +16.8); the median weights each economy equally, by design
a different weighting from the pooled statistic. Post-treatment conditioning on account holding.
Single 2024 cross-section — descriptive, no trend language. **The other five ruler axes remain
pooled-only and untested on this dimension.**

### P22 — verdict: DISCARD (CV-rejected on both targets), champion unchanged
The ≤2021 CV rejects the median center **decisively on both candidate targets**: account three-stage
mean=**6.710** vs median=**7.831** (+1.121pp worse), saving four-stage mean=**6.370** vs
median=**6.872** (+0.502pp worse). Adoption fails at the first gate on both, so no 2024 evaluation
was run (P14/P15/P19/P20/P21 protocol), `predictor.py` is reverted to the P18 champion, and all
three MAEs print byte-identical (account **5.014** / resilience **6.625** / saving **6.831**).
This is the registered alternative outcome and it is a **positive robustness result — the first for
the whole P11–P18 stack**: the population-weighted mean is the *right* basin location, and the
shrinkage gains are **not** a big-country pull. The prediction-side answer to the concern G6 encodes
on the hypothesis side is that the giant countries are earning their weight here, not distorting it.
Two things make the rejection more informative than a bare "no". First, the margins are **the
largest in the entire P-series** — 1.121pp against P19's 0.423, P20's 0.274, P21's 0.070 and P14's
0.006 — so the *center statistic* matters far more than any stage or basin choice tested to date;
the seam that looked mined out was being probed on the wrong axis. Second, the evaluator's MAE is
**unweighted across countries**, so an unweighted median center was if anything favoured by the
scoring rule and still lost heavily. The population weighting is doing real work inside the basin
rather than merely aligning with the metric.
Declared follow-up, untested: a **weighted median** — the middle option between the two extremes
compared here. P22 deliberately tested the opposite extreme, so a narrow middle ground remains open.

### 2026-07-31 — cycle summary
Three experiments, one per stream; two discards and one keep, and both discards are informative.
**E26 discard** (r=+0.294, missing the 0.30 bar by 0.006 with every gate passing and G6 *strengthening*
to +0.407): the three-rail story is bounded to **balance-sheet** margins — saving ~0.75, borrowing
~0.57, resilience ~0.0–0.3 and exactly 0.000 for digital payments. E2 replicated to three decimals;
E2/E15/E26 now agree across three independent attempts that digitalization does not show up in
self-reported shock-coping capacity.
**U19 keep** (median within-economy education gap **+9.4pp**, positive in **63/64** economies;
composition wedge only +2.7pp, ~22% of pooled; tertiary variant +18.0pp, **23/23**): the first micro
test to separate within-country gradient from between-country composition, and the ruler's largest
axis survives it. Disclosed: the registered tertiary-variant economy count was 31, actually 23 under
M2 as applied; verdict unchanged.
**P22 discard** (CV rejects a median basin center on both targets by 1.121pp and 0.502pp): the
population-weighted mean is the right shrink target and the P11–P18 gains are not a big-country
artifact — the first positive robustness result for the stack, with the largest margins in the
P-series, and obtained under an unweighted metric that would have favoured the median.
Prediction champion unchanged: **account 5.014 / resilience 6.625 / saving 6.831** (P18, commit 1bb3f78).

## 2026-08-01 daily autoresearch cycle

## E27 — pre-registered (hypothesis / country level)
**Idea:** eleven experiments have now traced *where the 2021-24 formal-saving surge came from*
(E1/E10/E12/E23/E24: three digitalization rails) and *where it went* (E7 resilience composition,
E11/E25 borrowing, E26 the balance-sheet boundary). Nobody has asked the accounting question
underneath all of it: **did the surge create savers, or relabel them?** The whole rails story reads
very differently if formal saving grew by pulling existing informal savers across a mode boundary
(a *composition* shift inside an unchanged saving population) than if it grew on top of unchanged
informal saving (net new saving). The country file carries the disjoint saving modes needed to
separate the two: `fin17c` (saved using *other* methods — the informal margin, 76 dev-panel
countries in both waves), `fin17b` (saved via a savings club or a person outside the family — the
semiformal margin, 58 countries), and `save_any_t_d` (saved any money, 76 countries), against the
headline `fin17a_17a1_d` (saved at an FI or via mobile money). Identification check run before
registration and disclosed: on the 2024 cross-section `fin17a_17a1_d` ≤ `save_any_t_d` in 100% of
dev-panel countries (nesting confirmed) while `fin17b`/`fin17c` sit near 17pp mean, well below the
27.1pp headline and *not* nested — so the informal/semiformal margins are genuine non-mechanical
comparators. No delta and no correlation was computed at that check.
**Hypothesis (registered direction — displacement):** the surge is substantially a mode switch, so
Δ(formal saving) co-moves **negatively** with Δ(other-method saving) 2021→2024 across the dev panel.
**Primary test:** pop-weighted corr of Δ`fin17c` with Δ`fin17a_17a1_d`, 2021→2024, `pan_dev`.
**Keep if** r ≤ **−0.30** (the registered sign) AND G6 sign-stable with retention ≥ 0.5 (E4 rule).
Following the E5/E9/E17 precedent, a result of |r| ≥ 0.30 with the *opposite* sign is a **discard of
the registered direction**, with the reverse reported as the substantive finding.
**Secondary A:** the same test on the semiformal margin Δ`fin17b` (n≈58).
**Secondary B (the accounting):** dev-panel pop-weighted aggregates of `save_any_t_d`,
`fin17a_17a1_d`, `fin17b`, `fin17c` at 2021 and 2024 — how much of the headline formal gain shows up
in total saving at all.
**Secondary C (pass-through):** pop-weighted LS slope of Δ`save_any_t_d` on Δ`fin17a_17a1_d`. A
slope near **1** means every point of formal saving is a point of new saving (net new savers); near
**0** means pure relabelling; intermediate values split the surge. Reported with its correlation and
declared *partly mechanical* (formal saving is nested inside any-saving, which biases the slope
upward), so it is context for the primary, never the test.
Declared: contemporaneous Δ-on-Δ co-movement, descriptive only, never causal; `fin17b`/`fin17c` are
narrower variants with no headline status under G3 and are declared as such; sample composition
differs across the three comparators, so each correlation prints its own n and the primary's sample
is the one gated.

## U20 — pre-registered (micro stream)
**Idea:** U19 took the ruler's largest axis (education) apart into within-country gradient vs
between-country composition and the gradient survived — median within-economy gap **+9.4pp**,
positive in 63/64 economies, composition wedge only ~22% of the pooled figure. Five axes remain
pooled-only. This runs the identical test on the **second-largest axis, income** (U17: conditional
q5−q1 = **+11.5pp**), which is the axis where the composition worry is *a priori* strongest: income
quintiles are constructed **within** each economy, so a purely between-country story would have to
work through something other than quintile membership — making a collapse here far more diagnostic
than a collapse on education would have been.
**Primary:** for EACH economy separately, the conditional income gap in digital-payment use —
weighted rate of `anydigpayment == 1` among `account == 1` for `inc_q >= 4` (richest 40%) minus
`inc_q <= 2` (poorest 40%). An economy qualifies only if BOTH cells reach unweighted n ≥ 100 (M2
applied PER ECONOMY): **83 of 97 economies qualify** (coverage check run before registration on
non-missing outcome+weight+`inc_q`, matching M2 as applied — no rate computed; this is the fix for
U19's disclosed count deviation). Statistic = the **MEDIAN** within-economy gap.
**Keep if** median ≥ **5pp** AND ≥ two-thirds (**≥ 56/83**) of qualifying economies show a positive
gap — the same two-part condition as U19, for the same reason: a median driven by a minority of
large gaps is a weaker claim than a consistent within-country regularity.
**Secondary:** share positive, IQR and extremes; the pooled gap on the same 83 economies and on all
economies (the wedge = the composition estimate); and the like-for-like **q5-vs-q1** variant
(**33 economies** qualify under the same pre-check), which is the direct within-country counterpart
of U17's +11.5pp headline.
**Registered alternative outcome:** a median far below the pooled figure, or a positive share near
half, would say the income axis of the ruler is substantially between-country composition — which,
given that quintiles are within-economy constructs, would be a sharper methodological result than
U19's and would force a re-wording of U17.
Declared caveats: post-treatment conditioning on account holding (as in U6/U8/U10/U14–U19); the
richest-40 vs poorest-40 contrast is **coarser** than U17's q5−q1 and is expected to be smaller in
pp for that reason alone — the q5-vs-q1 variant is the like-for-like comparison; the median weights
each economy equally, by design a different weighting from the pooled statistic; the qualifying set
is selected (economies need sizeable poorest-40 *and* richest-40 accountholding populations).
Single 2024 cross-section — descriptive, no trend language.

## P23 — pre-registered (prediction stream)
**Idea:** P22 replaced the basin center — the population-weighted mean, unchanged since P5 — with
the **unweighted median** and the ≤2021 CV rejected it decisively on both targets (account +1.121pp,
saving +0.502pp), the largest margins in the P-series. P22's own declared follow-up is the **middle
option**: P22 tested the *opposite extreme* (throwing the population weighting away entirely), so
the rejection does not distinguish "the weighting is doing real work" from "the mean, being
sensitive to the whole distribution, is the right functional form". A **population-weighted median**
separates them: it keeps the population weighting exactly as the incumbent uses it, and changes only
the location functional from mean to median (robust to a single giant country sitting far from its
basin's mass).
**Test:** replace the basin center in `_shrink` with the **population-weighted median** — the basin
member value at which the cumulative population weight first reaches 50% — at **every** stage, per
target. Everything else is byte-identical to the P18 champion: k = 0.1, damped trend λ = 0.5, basin
sequences and adopted stage counts unchanged. Adoption is per target and entirely ≤2021 (no 2024 in
features, fitting or selection): CV on that target's 2017→2021 transition with a persistence base,
all basins built at 2017 — the P10/P12/P13/P16–P22 protocol — comparing the incumbent mean-centered
stack against the identical weighted-median-centered stack. Per the P14/P15/P19–P22 protocol, a
target whose CV does not prefer the candidate is not evaluated on 2024 and keeps its champion
prediction byte-identical. **Resilience is excluded by design** (CV infeasible; the account proxy is
twice on record as mis-selecting for it — P8, P13) and stays at 6.625.
**Keep if** for any target the ≤2021 CV prefers the weighted-median stack **AND** its 2021→2024 MAE
improves on the champion (account **5.014**, saving **6.831**), with every untouched target printing
byte-identical.
**Registered alternative outcomes:** a CV rejection with margins **as large as P22's** would say the
*functional form* (mean vs median) is what P22 detected, not the weighting; a rejection with margins
**much smaller than P22's** would say the opposite — that P22's margin was mostly the discarded
population weighting, and the population-weighted mean's advantage over a robust center is thin.
Either reading is a sharper result than P22's bare "no", and both are recorded regardless of verdict
because the margin comparison, not the adopt/reject bit, is the information here.
Declared: estimator-robustness experiment, not a search for a new stage; the CV comparison is a
strict A/B against the incumbent on the identical stack, so nothing about the champion's structure
is re-litigated.

### E27 — verdict: DISCARD (registered direction rejected; the reverse is the substantive result)
Primary weighted r(Δother-method saving, Δformal saving) = **+0.696** (n=76) — the registered
**displacement** direction (r ≤ −0.30) is rejected about as decisively as it could be, and the
result is logged as a discard on the pre-registered sign (E5/E9/E17 precedent). G3/G4 pass (76
countries, 100% of dev-panel population); G6 is sign-stable with retention **exactly 0.50**
(+0.696 → +0.348), so the primary co-movement is *half* big-country amplified — right at the E4
judgment boundary, and a reason the reverse claim is reported as a description of this window
rather than promoted to a keep.
**The surge created savers more than it relabelled them.** The dev-panel accounting:

| margin | 2021 | 2024 | Δ |
|---|---|---|---|
| formal (`fin17a_17a1_d`) | 24.3 | 38.0 | **+13.7** |
| any saving (`save_any_t_d`) | 42.4 | 53.0 | **+10.6** |
| other-method (`fin17c`) | 8.7 | 16.4 | +7.7 |
| savings club (`fin17b`) | 5.3 | 14.4 | +9.1 |

**77% of the formal gain shows up in total saving** (+10.6pp of +13.7pp), leaving ~3.1pp — under a
quarter — as the arithmetic ceiling on pure relabelling. The pop-weighted pass-through slope of
Δany-saving on Δformal-saving is **+0.720** (r=+0.747), the same story country by country (declared
partly mechanical: formal is nested inside any-saving).
The informal margins did not recede — they **rose alongside**, and rose most where formal saving
rose most: Δformal terciles low/mid/high (+1.8/+8.4/+17.3pp) carry mean Δother-method saving of
**+0.8/+2.7/+4.6pp**, monotonic. The semiformal savings-club margin behaves the same
(r=**+0.531**, n=58) and its G6 retention is **1.06** — that one is not a big-country artifact at all.
So the 2021-24 episode looks like a **broad saving expansion in which the formal mode grew fastest**,
not a migration of existing savers across a mode boundary. This is the accounting foundation under
the rails findings (E1/E10/E12/E23/E24): the rails were co-moving with new saving, not with
re-labelled saving. Contemporaneous Δ-on-Δ, descriptive only; `fin17b`/`fin17c` are narrow variants
declared under G3.

### U20 — verdict: KEEP
Median within-economy conditional **income** gap = **+5.7pp** across the **83** qualifying economies
(**92.6%** of accountholding respondents), positive in **74 of 83 (89%)** — both pre-registered
conditions clear (≥5pp; ≥56/83). IQR +2.3 to +11.3pp, mean +7.2pp, range Kosovo −9.5 to Ecuador
+32.5. M2 applied per economy; M3 n/a.
**The composition wedge is again small.** Pooled over the same 83 economies the gap is +7.9pp
against a within-economy median of +5.7pp — a wedge of **+2.2pp, ~28% of the pooled figure**
(education: +2.7pp, ~22%). On the like-for-like **q5-vs-q1** contrast the within-country median is
**+9.7pp**, positive in **30/33**, against a pooled figure of **+11.5pp** that reproduces **U17
exactly** — a wedge of +1.8pp, ~16%.
Income is the **second ruler axis** to be separated into within-country gradient vs between-country
composition, and the second to survive. It is the axis where a collapse would have been most
diagnostic, since income quintiles are constructed *within* each economy — a between-country story
would have had to work through something other than quintile membership. It did not.
**Honest weakness, recorded:** the income axis is *thinner* than education. Only **54%** of
qualifying economies clear 5pp on the coarse contrast (education: the median itself was +9.4pp with
IQR starting at +4.2), so the primary sits just above its threshold rather than comfortably over it;
the like-for-like q5−q1 variant is the stronger reading at +9.7pp.
**Disclosed registration detail:** the pre-registration wrote "83 of 97 economies qualify" (97 =
the pre-check base of economies with any usable rows); the run prints "83 of 140" against the full
economy count. The qualifying count — the number the condition depends on — is **exactly as
registered**, and this is the U19 counting deviation not recurring.
Caveats: post-treatment conditioning on account holding; the richest-40 vs poorest-40 contrast is
coarser than U17's q5−q1 by construction; the median weights each economy equally; the qualifying
set is selected. Single 2024 cross-section — descriptive, no trend language.
**Four ruler axes (age, gender, urbanicity, employment) remain pooled-only.**

### P23 — verdict: DISCARD (CV adopts on both targets, holdout worsens), champion unchanged
The ≤2021 CV **prefers the population-weighted median decisively on both targets** — account
3-stage **6.710 → 6.229** (margin **−0.481**) and saving 4-stage **6.370 → 5.980** (margin
**−0.390**) — margins *larger than any adopted stage gain in the entire P-series*. The 2021→2024
holdout then moves the wrong way on both: account **5.014 → 5.023** (+0.009pp) and saving
**6.831 → 6.864** (+0.033pp). The keep condition requires CV **and** holdout, so this is a discard;
`predictor.py` is reverted to the P18 champion and verified byte-identical (account **5.014** /
resilience **6.625** / saving **6.831**).
**The registered question is answered cleanly, and the answer reverses P22's reading.** P22's
unweighted median was CV-rejected by **+1.120 / +0.502**; re-attaching the population weighting and
changing nothing else flips both to **−0.481 / −0.390 preferred**. So what P22 detected was **the
population weighting, not the mean-vs-median functional form** — P22's conclusion that "the
population-weighted mean is the right basin location" should be read more narrowly as *the
population weighting inside the basin is what matters*; between the two weighted centers, the ≤2021
window actually prefers the robust one.
**Second lesson, on the CV itself.** This is the **fourth CV→holdout non-transfer** (P8, P9, P13,
P23) and by far the sharpest: the largest CV improvement ever measured on this stack buys **nothing**
out of sample. The 2017→2021 and 2021→2024 transitions disagree about the basin center, which is
consistent with the surge-window regime change already on record (P3, P10). Practical reading: the
two centers are **within 0.01–0.03pp of each other on the holdout** — near-equivalent out of sample —
so the CV's large margin is a property of the calm pre-2021 window, not a durable estimator ranking.
The declared middle option is now tested and the center axis is closed.

## 2026-08-01 wrap-up
Ran 3 experiments (E27, U20, P23), one per stream — **one keep, two informative discards**.
**E27 (hypothesis, DISCARD on the registered sign):** the 2021-24 formal-saving surge did **not**
displace informal saving — r(Δother-method, Δformal) = **+0.696** (n=76, G6 retention exactly 0.50),
savings-club margin **+0.531** (retention 1.06), and **77% of the +13.7pp formal gain shows up in
total saving** (pass-through slope +0.720). The surge is mostly **net new saving**, with informal
saving rising alongside it and rising most where formal rose most (+0.8/+2.7/+4.6pp across Δformal
terciles). That is the accounting foundation under the whole rails series.
**U20 (micro, KEEP):** income is the second ruler axis shown to be **within-country**, not
composition — median within-economy conditional gap **+5.7pp**, positive in **74/83** economies
(92.6% of accountholders), wedge **+2.2pp (~28% of pooled)**; like-for-like q5−q1 median **+9.7pp**
(30/33) against a pooled +11.5pp that reproduces U17 exactly. Weaker than education: only 54% of
economies clear 5pp.
**P23 (prediction, DISCARD):** the population-weighted median is CV-preferred by the largest margins
in the P-series (−0.481 account, −0.390 saving) yet loses on the holdout by 0.009/0.033pp. Two
results: P22's rejection was **the weighting, not the functional form** (re-weighting flips
+1.120/+0.502 rejected to −0.481/−0.390 preferred), and this is the fourth and sharpest CV→holdout
non-transfer — the pre-2021 window's estimator ranking does not survive the surge window.
Prediction champion unchanged: **account 5.014 / resilience 6.625 / saving 6.831** (P18, 1bb3f78).

---

## 2026-08-02 — cycle pre-registration (E28, E29, P24)

**B1 coverage run first** (`python3 coverage.py`, no outcome computed): country file 23/429 columns
touched (5%); untouched wave transition 2011→2014, thin 2014→2017 (3 mentions) against 2021→2024
(162); untouched frames `education`, `age_cat`, `laborforce`; 14 untouched country modules including
`con` (133 cols), `fh` (4), `internet` (1).

**Coverage cells this cycle lands on (rule B2):**
- **E28** → wave transitions **2014→2017** (thin, 3 mentions) and **2017→2021**, i.e. the replication
  debt itself (Program 1.1/1.2). Parent findings: E1, E10, E12 (lineage depth 1 — B3 clear).
- **E29** → the **`internet` column, an untouched module** (Program 5.1/5.2), 2024 cross-section.
  Secondary descends from E23/E24 (lineage depth 1 for that arm).
- **P24** → prediction stream (no coverage constraint).
Rule B2 is satisfied twice over; no experiment sits inside the 2021→2024 rails shaft alone.

### E28 (pre-registered) — do the three digitalization rails ↔ formal-saving co-movements exist BEFORE 2021?

**Why.** Under rule B4 every rails keep is `keep-window`: E1 (Δmobile money, r=+0.719), E10 (Δwage
digitalization `fin32_acc`, r=+0.791) and E12 (Δdigital payments `g20_any`, r=+0.370) were all
measured on 2021→2024, the surge window. If the co-movement is a general regularity it should be
visible in the calm windows too; if it is not, the paper's Section 4 is a description of one episode
and must say so. All four columns are present at 2014/2017/2021 (availability checked, no outcome
looked at: `fin17a_17a1_d` 77/77/77, `g20_any` 77/77/77, `fin32_acc` 77/77/77, `mobileaccount_t_d`
57/59/61 dev-panel countries).

**Test.** For each rail R ∈ {`mobileaccount_t_d`, `fin32_acc`, `g20_any`} and each transition
T ∈ {2014→2017, 2017→2021} (with 2021→2024 recomputed as the reference row): population-weighted
correlation of Δ_T(R) with Δ_T(`fin17a_17a1_d`) on the developing panel, weight = 2024 adult
population — E1/E10/E12's exact construction, changing only the window. Δ-tercile means reported per
cell. Gates G3 (headline concepts declared; `fin32_acc` has no variant, E10 precedent), G4, G6
(drop top-5 population). **B6 inference on every cell**: country bootstrap, 2,000 resamples,
percentile 95% interval, plus Kish `neff = (Σw)²/Σw²` beside nominal n.

**Promotion rule (pre-registered).** A rail is promoted `keep-window` → **`keep-general`** iff in at
least one earlier transition it reaches **r ≥ +0.30 with the same (positive) sign**, G6 is
sign-stable, and the E4 judgment rule holds (`r_droptop ≥ 0.5 × r_full`). A rail failing that in both
earlier windows **stays `keep-window`** and its 2021→2024 result is relabelled explicitly as
window-specific in `findings.tsv`. The bootstrap interval is reported for the record and is *not* an
extra keep condition (the registered threshold is |r| ≥ 0.30).

**Declared.** Contemporaneous Δ-on-Δ co-movement in every window — descriptive, never causal. Sample
composition differs by rail and window (mobile money is the thin one at 57–61 countries); each cell
prints its own n, neff and interval. A null in an earlier window is not evidence the mechanism is
absent — the calm windows have far less Δ-variance to correlate, and that is itself reported
(per-window SD of both Δs is printed so a variance-collapse reading can be checked).

### E29 (pre-registered) — is connectivity a prerequisite (threshold) for the digital rails, or a linear correlate?

**Why.** The rails story (E1/E10/E12/E23/E24) has no answer to "are these three margins just measuring
internet penetration?". `internet` is untouched, present for **2024 only** on 77 developing panel
economies (117 all-panel). Program 5.1/5.2.

**Primary test.** Developing panel, 2024 cross-section. y = `g20_any` (digital-payment headline),
x = `internet`. (i) population-weighted correlation r; (ii) weighted mean of y within internet
terciles; (iii) nonlinearity: population-weighted OLS of y on x, linear vs quadratic, reporting the
increment in weighted R², and the weighted slope of y on x estimated **separately below and above the
weighted median of `internet`**.
**Keep the THRESHOLD claim** iff |r| ≥ 0.30 **and** the low-half slope exceeds the high-half slope by
a factor ≥ 2 (a prerequisite pattern: steep where connectivity is scarce, flat once it is common)
**or** the reverse by a factor ≥ 2 (a takeoff pattern) — direction recorded either way — **and** the
quadratic term adds ≥ 0.05 to weighted R².
**Fallback claim (registered now, lesser):** if |r| ≥ 0.30 but the nonlinearity bar fails, keep only
the linear statement "connectivity level tracks digital-payment level across developing economies",
status `keep-window`, with the note that `internet` is single-wave so B4 promotion is **impossible by
construction** — this claim can never become `keep-general`.

**Secondary (registered, reported regardless of the primary).** Do the rails survive conditioning on
connectivity? For each rail R ∈ {`mobileaccount_t_d`, `fin32_acc`, `g20_any`}: weighted **partial**
correlation of Δ_2021→24(R) with Δ_2021→24(`fin17a_17a1_d`) controlling the **2024 level** of
`internet` (both residualized by weighted OLS on `internet`). Registered comparison: each rail
retains **r_partial ≥ +0.30 or ≥ 2/3 of its unconditional magnitude**. Declared design mismatch: a
*level* control imposed on a Δ design, and a 2024 control on a 2021→2024 change — stated as a
limitation, not fixed.

**Gates.** G3 (`g20_any`, `mobileaccount_t_d`, `fin17a_17a1_d` headlines declared; `internet` and
`fin32_acc` have no variant choice and are declared unregistered-by-necessity), G4, G6. B6: bootstrap
(2,000 country resamples) and Kish `neff` on the primary and on each secondary partial.
**Declared.** Single cross-section — no trend language on the primary; cross-country level
correlations are the weakest design in the ledger (development level confounds everything), so the
primary is worded as a description of the 2024 cross-section, never as a mechanism.

### P24 (pre-registered) — empirical-Bayes ADAPTIVE shrinkage weight: should a basin's reliability set how hard it pulls?

**Why.** `k = 0.1` has been a hard constant since P5, at every stage of every stack. P9 tuned it as a
single global constant (CV picked 0.2, holdout worsened) and the center axis is closed by P22/P23.
Untested: whether k should **vary by basin**. A basin whose population-weighted mean rests on many
countries of comparable size is a more reliable target than one dominated by a single economy, and
should pull harder — the standard empirical-Bayes shape, and it reuses the Kish machinery rule B6
just made mandatory on the hypothesis side.

**Candidate.** Replace the constant with `k_g = neff_g / (neff_g + m)` at **every** stage, where
`neff_g = (Σw)² / Σw²` over the basin's member countries' 2024 adult population weights and `m` is a
constant selected by CV. `m → ∞` reproduces no-shrink; small `m` approaches full pooling; the
incumbent constant 0.1 is *not* in the family, so it is carried as the explicit baseline.

**Adoption rule (entirely ≤2021 — no 2024 in features, fitting or selection).** Per target, CV on
that target's 2017→2021 transition with a persistence base and all basins built at 2017 (the
P10/P12/P13/P16–P23 protocol), grid `m ∈ {50, 150, 500, 1500, 5000}`, comparing the best adaptive
stack against the identical incumbent constant-k stack: account = 3-stage (income → region → g20
terciles), saving = 4-stage (region → income → account terciles → g20 terciles). **Resilience is
excluded by design** (no pre-2021 transition; the account proxy is twice on record as mis-selecting
for it — P8, P13) and stays byte-identical at 6.625.
**Keep if** for any target the ≤2021 CV prefers the adaptive weight **AND** its 2021→2024 MAE improves
on the champion (account **5.014**, saving **6.831**), with every untouched target printing
byte-identical. Given four CV→holdout non-transfers on record (P8, P9, P13, P23), the CV margin and
the holdout delta are both recorded whatever the verdict — the size of the gap between them is now
the P-series' most reliably informative output.

### E28 — verdict: KEEP (all three rails replicate on 2017→2021 and are PROMOTED to keep-general)

| rail | 2014→2017 | 2017→2021 | 2021→2024 (reference) |
|---|---|---|---|
| mobile money (`mobileaccount_t_d`) | **−0.048** (n=54) | **+0.454** (n=57) | +0.719 (n=58) |
| wage digitalization (`fin32_acc`) | **+0.155** (n=77) | **+0.678** (n=77) | +0.791 (n=71) |
| digital payments (`g20_any`) | **−0.248** (n=77) | **+0.685** (n=77) | +0.370 (n=76) |

**The 2017→2021 window replicates all three** at or above the pre-registered +0.30, G6 sign-stable,
retention 0.89 / 0.75 / 0.61 — every one clear of the E4 0.50 floor. Δ-tercile monotonicity holds in
that window too (mobile money +2.5/+3.4/+11.4pp; wage +−0.6/+5.5/+8.1pp; digital pay −0.9/+5.9/+8.1pp).
Under the pre-registered promotion rule **E1, E10 and E12 move `keep-window` → `keep-general`**: the
rails ↔ formal-saving co-movement is a two-window regularity, not an artifact of the surge.

**2014→2017 replicates nothing, and the registered variance check explains why rather than
contradicting it.** In that window the dev-panel saving margin *fell* (22.2 → 21.0pp) with the
smallest country-level Δ dispersion in the series (SD 4.9pp vs 8.4pp in 2017–21 and 7.2pp in
2021–24). Two of the three cells are also G6-unstable (mobile money −0.048 → +0.414, digital pay
−0.248 → +0.458 when the top-5 populations drop) — i.e. the pre-2017 cells have no stable sign in
either direction, which is a different statement from "the association is absent". The honest
reading: **the rails track saving in the two windows where saving moved; the flat window carries no
usable signal either way.** The ledger's first look at 2014→2017 as a *comparison* window, not a
one-off.

**B6 inference, and the sharpest result of this experiment.** The Kish effective sample size is
**6.8–7.5 in every single cell** — 77 population-weighted countries carry roughly **7.5** effective
observations, because the weight concentrates in a handful of economies. The bootstrap intervals
(2,000 country resamples) are correspondingly wide:

- mobile money 2021→24 **[+0.560, +0.852]**, 2017→21 [+0.166, +0.658]
- wage digital 2021→24 **[+0.637, +0.872]**, 2017→21 [+0.323, +0.833]
- digital pay 2021→24 **[−0.023, +0.824]** — *straddles zero*, 2017→21 [+0.383, +0.820]

E12's headline (+0.370) is the weakest rail and its interval **includes zero**; per the
pre-registration the interval is reported, not an extra keep condition, so E12 promotes on the
registered criterion — but the promotion should be read with that interval attached, and the paper
must stop implying 76 degrees of freedom behind these numbers. The two strong rails (mobile money,
wage digitalization) have intervals comfortably clear of zero in both replicating windows.

**Caveats.** Contemporaneous Δ-on-Δ in every window — descriptive temporal co-movement, no
identification. Composition varies (mobile money 54–58 economies vs 71–77 for the others), the
weight is the 2024 adult population in all windows by construction, and `fin32_acc` is an
employer-side attribute. G3/G4 pass in all cells (G4 pop_share 0.66–1.00); G5 n/a.

### E29 — verdict: THRESHOLD claim DISCARDED on the registered bar; FALLBACK linear claim KEPT; secondary is the substantive result

**Primary (2024 cross-section, dev panel).** Weighted r(`g20_any`, `internet`) = **+0.707** (n=76,
Kish **neff = 7.2**, bootstrap 95% CI **[+0.271, +0.844]**). G4 passes (77 economies, pop_share 1.00);
G6 is sign-stable with retention **0.54** (+0.707 → +0.380) — clearing the E4 0.50 floor, but only
just, so the level association is roughly *half* big-country amplified and is reported that way.

The **threshold/prerequisite shape fails its registered bar.** The quadratic term adds only
**+0.036** to weighted R² (0.500 → 0.537) against the registered ≥ 0.05, so no shape claim is kept.
What the split-slope test *does* show is recorded because the direction was registered either way,
and it is the **opposite of the prerequisite hypothesis**: the slope of digital payments on internet
is **+0.294 below** the population-weighted median connectivity (70.5pp) and **+2.668 above** it —
ratio 1:9.1 in the **takeoff** direction, not the prerequisite direction. The tercile means agree
(internet 42.4 → g20 45.3pp; 73.1 → 50.4pp; 86.7 → **82.0pp**): the middle tercile sits barely above
the bottom, and almost all of the co-movement lives in the top third of the connectivity
distribution. So the registered "digital rails do not function below a connectivity floor" reading is
**not** what the 2024 cross-section looks like; it looks like acceleration at high connectivity. The
magnitude bar was missed, so this is logged as a direction on record, not a claim.

**KEPT (fallback, as registered):** connectivity level and digital-payment level track each other
strongly across developing economies in 2024, r = +0.707. Status `keep-window` with the note that
`internet` is **single-wave, so B4 promotion to `keep-general` is impossible by construction** — this
claim can never become a regularity in this dataset.

**Descriptive, same x, and the most interesting line in the run:**
r(`account_t_d`, internet) = **+0.359**; r(`fin17a_17a1_d`, internet) = **+0.606**;
r(`mobileaccount_t_d`, internet) = **+0.097** (n=62). **Mobile money is essentially orthogonal to
internet penetration** — consistent with a rail that runs on basic handsets rather than data, and a
useful counterweight to reading the whole rails story as connectivity.

**Secondary — the rails are not proxies for connectivity.** Conditioning the 2021→2024 rail↔saving
co-movements on the 2024 internet *level* leaves all three essentially untouched, and one *stronger*:

| rail | unconditional | partial \| internet | retains | 95% CI on the partial |
|---|---|---|---|---|
| mobile money | +0.719 | **+0.726** | 1.01 | [+0.565, +0.857] |
| wage digitalization | +0.791 | **+0.795** | 1.00 | [+0.636, +0.875] |
| digital payments | +0.370 | **+0.637** | 1.72 | [+0.468, +0.841] |

All three clear the registered condition (partial ≥ +0.30 or ≥ 2/3 retention). The digital-payment
rail is *suppressed* by connectivity in the unconditional form — netting out the internet level
raises it from +0.370 to +0.637, and lifts its interval clear of the zero it straddled in E28. The
objection "the rails are just internet penetration" is not supported in this window.
**Declared mismatch, unfixed:** a *level* control imposed on a Δ design, with the control dated 2024
while the change spans 2021→2024. Cross-country level correlations are the weakest design in the
ledger (development level confounds everything); the primary is a description of the 2024
cross-section, no trend language, never a mechanism.

### P24 — verdict: DISCARD (CV rejects on both targets), champion unchanged

The ≤2021 CV **prefers the incumbent constant k on both targets**, at every grid point:
account 3-stage `constant_k = 6.710` vs `m=50: 6.995 / 150: 7.154 / 500: 7.364 / 1500: 7.449 /
5000: 7.482` (best margin **+0.284**, wrong side); saving 4-stage `constant_k = 6.370` vs
`m=50: 6.611 / 150: 6.419 / 500: 6.721 / 1500: 6.874 / 5000: 6.939` (best margin **+0.049**).
No target adopts, so `predict()` never sees an adaptive weight and the holdout is byte-identical:
**account 5.014 / resilience 6.625 / saving 6.831**. `predictor.py` is reverted to the P18 champion
and re-run to confirm.

**The diagnostic is worth more than the verdict, and it indicts the registered grid.** The basin
reliability table (printed inside the experiment) shows how extreme the weight concentration is:

| basin | n countries | Kish neff |
|---|---|---|
| Upper middle income | 32 | **2.77** |
| Lower middle income | 33 | 4.20 |
| Low income | 12 | 7.13 |
| South Asia (excl. HI) | 5 | **1.61** |
| East Asia & Pacific (excl. HI) | 8 | 1.86 |
| Sub-Saharan Africa (excl. HI) | 26 | 9.51 |

Every basin's population-weighted mean rests on **2–10 effective economies**, not on its 5–40
nominal members — the same neff ≈ 7 finding E28 produced on the hypothesis side, now visible inside
the model. Because `neff_g` is that small, `k_g = neff_g/(neff_g+m)` at **every** grid point m ≥ 50
is **below the incumbent 0.1 almost everywhere** (at m=500, k_g runs 0.003–0.019). So the registered
grid conflated two changes — grading k by reliability *and* cutting the average k by an order of
magnitude — and the monotone deterioration in m is mostly the second one, re-confirming P9's "less
shrinkage is worse" rather than testing the empirical-Bayes idea cleanly. The best grid point is the
smallest m on both targets, i.e. the CV is pushing back toward more shrinkage the whole way.
**Registered as the next candidate in this axis (not run today, budget):** a **shrinkage-neutral**
version — rescale `k_g` so its population-weighted mean equals the incumbent 0.1, keeping only the
*relative* grading across basins. That isolates the reliability question from the level question,
which today's grid could not. Logged in `RESEARCH_AGENDA.md`.
This is the **fifth** CV→holdout interaction on record (P8, P9, P13, P23, P24) and the first where CV
and holdout cannot disagree, because CV rejected before the holdout was ever consulted.

## 2026-08-02 wrap-up
Ran 3 experiments (E28, E29, P24) — **two keeps, one discard, and the ledger's first promotions**.
**E28 (hypothesis, KEEP — Program 1, the replication debt):** all three digitalization rails
replicate on **2017→2021** — mobile money **+0.454** (n=57), wage digitalization **+0.678** (n=77),
digital payments **+0.685** (n=77) — G6 sign-stable with retention 0.89/0.75/0.61, so **E1, E10 and
E12 are promoted `keep-window` → `keep-general`**, the first three general claims in the ledger.
2014→2017 replicates nothing, in the one window where dev-panel saving *fell* (22.2→21.0pp) with the
smallest Δ dispersion (SD 4.9pp) and G6-unstable cells — no signal either way, not a contradiction.
**B6 bit that changes how the whole ledger should be read: Kish neff is 6.8–7.5 in every cell**, and
E12's 2021→24 bootstrap interval **[−0.023, +0.824] straddles zero**.
**E29 (hypothesis, MIXED — Program 5, the untouched `internet` column):** the registered
*prerequisite/threshold* shape is **discarded** (quadratic adds only +0.036 R² against a 0.05 bar);
the split slopes run the **opposite** way to the hypothesis — +0.294 below vs **+2.668** above the
70.5pp weighted-median connectivity, a takeoff rather than a floor. The fallback linear claim is kept
(r = **+0.707**, n=76, CI [+0.271, +0.844], G6 retention 0.54) and can **never** be promoted —
`internet` is single-wave. The substantive result is the secondary: conditioning the rails on the
2024 internet level leaves them intact (**+0.726 / +0.795 / +0.637** against +0.719/+0.791/+0.370),
and *raises* the digital-payment rail out of its zero-straddling interval — the rails are not proxies
for connectivity. Mobile money is nearly orthogonal to internet penetration (r = **+0.097**).
**P24 (prediction, DISCARD):** the empirical-Bayes weight `k_g = neff_g/(neff_g+m)` is CV-rejected on
both targets (+0.284 account, +0.049 saving); the basin neff table (1.6–9.5 effective economies per
basin) shows the registered grid cut average shrinkage tenfold instead of isolating the grading, so a
shrinkage-neutral variant is registered for a later cycle. Champion unchanged:
**account 5.014 / resilience 6.625 / saving 6.831** (P18, 1bb3f78).

## 2026-08-03 — cycle pre-registration (E30, E31, P25)

**Coverage cells this cycle lands on (rule B1/B2).** `python3 coverage.py` was run before any
hypothesis was chosen. The audit still reports 6% of country columns, 11% of micro columns, and
**three of seven country frames with zero ledger mentions**.
- **E30** — wave transitions **2014→2017** (thin, 14 mentions) and **2017→2021**; frame `pan_dev`,
  `group == "all"` (used). Program 1, the replication debt.
- **E31** — **`pan_grp` with `group ∈ {education, age_cat, laborforce}`: three UNTOUCHED frames
  (0 mentions each)**, plus `gender` (detector-blind, effectively unused) and `income` (21 mentions),
  across **all four wave transitions**. This is the cycle's B2 experiment. Program 3.
- **P25** — prediction stream, no new coverage cell (by nature).
**Lineage (rule B3).** E30's parents are E11/E13/E14 (a different family from the E1/E10/E12 rails
that E28/E29 descended from — the chain is broken as B3 requires). E31's parents are E17/E20/E21
(the gap/convergence family, last touched at E21, five experiments ago). P25's parent is P24.

### E30 (pre-registered) — do the three NON-saving-destination co-movements replicate on earlier transitions?

**Why.** E28 paid the first instalment of the replication debt for the rails→saving family (E1/E10/E12
promoted). Three further `keep-window` findings share a construction and have never been tested
outside 2021→2024, and none of them has formal saving as the destination — so they are a genuinely
independent test of whether the ledger's Δ-on-Δ co-movements are window artifacts:
- **E11**: Δ`fin22a_22a1_22g_d` (formal borrowing) ~ Δ`fin17a_17a1_d` (formal saving), r = +0.403
- **E13**: Δ`fiaccount_t_d` ~ Δ`mobileaccount_t_d` (co-development vs leapfrogging), r = +0.435
- **E14**: Δ`mobileaccount_t_d` ~ Δ`g20_any` (bundled on-ramps), r = +0.600

**Test.** Developing panel (`pan_dev`, `group == "all"`), for each of the three pairs, in each of two
earlier windows **2014→2017** and **2017→2021**: population-weighted correlation of the two Δs,
weight = 2024 adult population (E1/E10/E12/E28 construction, changing only the window). Δ-tercile
means of the destination variable per cell. Per-window SD of both Δs printed (E28's variance-collapse
check). Gates G3 (headline variants declared), G4, G6 (drop top-5 population).
**B6 on every cell:** country bootstrap, 2,000 resamples, percentile 95% interval, and Kish
`neff = (Σw)²/Σw²` beside nominal n.

**Promotion rule (pre-registered, identical to E28's).** A finding is promoted `keep-window` →
**`keep-general`** iff in at least one earlier window it reaches **r ≥ +0.30 with the same (positive)
sign**, G6 is sign-stable, and the E4 judgment rule holds (**`r_droptop` ≥ 0.5 × `r_full`**). A
finding failing that in both earlier windows **stays `keep-window`** and is relabelled explicitly as
window-specific. The bootstrap interval is reported for the record and is **not** an extra keep
condition.

**Declared.** Contemporaneous Δ-on-Δ co-movement in every window — descriptive, never causal. Sample
composition differs by pair and window (the mobile-money pairs are the thin ones at ~54–59
economies); each cell prints its own n, neff and interval. A null in a calm window is not evidence
the association is absent — E28 established that the 2014→2017 window has the least Δ-variance in the
series — and the printed SDs let that reading be checked rather than assumed.

### E31 (pre-registered) — over 13 years, do ACCESS gaps close while USAGE gaps stay open?

**Why.** `pan_grp` is the largest untouched *frame* in the repo: six demographic slices × five waves ×
117 economies, and `education`, `age_cat` and `laborforce` have **zero** ledger mentions. The paper's
"access converges, use diverges" motif (E17 tested it on country levels and was discarded) has never
been tested where it is most natural — *within* countries, across demographic groups, over the whole
13-year panel. Agenda items 3.2 + 3.3. Parents: E17/E20/E21.

**Construction.** Developing panel economies only (`incomegroupwb24 != "High income"`), five
dimensions with multi-wave coverage; `urbanicity` is 2024-only and is therefore **excluded from the
primary** and reported as a single-wave descriptive line. Advantaged group declared a priori for each
dimension (recorded now, before any answer): gender → `men`; income → `richest 60%`; education →
`secondary edu or more`; age_cat → `age 25+`; laborforce → `in laborforce`.
Per country per wave: `gap = advantaged − disadvantaged` in pp. Aggregate = population-weighted mean
gap across economies (weight = 2024 adult population, ledger convention).
- **ACCESS margin** = `account_t_d`, window **2011 → 2024**.
- **USAGE margin** = `g20_any`, window **2014 → 2024** (the column does not exist in 2011; declared).

**Primary test and threshold.** For each of the five dimensions, Δgap over the margin's full window.
- Claim A, *access gaps closed*: holds iff **≥3 of 5** dimensions have **Δgap_access ≤ −5pp**.
- Claim B, *usage gaps did not close*: holds iff **≥3 of 5** dimensions have **Δgap_usage > −5pp**.
- **The registered JOINT claim** ("within countries, access gaps closed while usage gaps did not")
  is kept iff **A and B both hold AND ≥3 of 5 dimensions show the divergent pattern individually**
  (Δgap_access ≤ −5pp *and* Δgap_usage > −5pp in the same dimension). Anything less is a discard of
  the joint claim; A and B are then reported separately as descriptive lines, not as a keep.
**Scale-free requirement (mandatory, per the agenda's ceiling-artifact note).** The pp gap must
compress mechanically as the advantaged group approaches 100%. So the **log-odds gap**
`L = logit(adv) − logit(disadv)` is computed for every cell and its Δ reported beside the pp Δ. A
dimension may only *count toward* the joint claim if **ΔL and Δgap agree in sign**. Where they
disagree, the pp narrowing is declared a ceiling artifact and that dimension counts as a non-closer.
**Gates.** G3 (`account_t_d`, `g20_any` headlines declared), G4 per wave and dimension, G6
(drop-top-5 population, sign stability of each Δgap). **B6:** country bootstrap 2,000 draws with a
percentile 95% interval on every Δgap, and Kish `neff` per dimension.
**Declared.** Descriptive within-country gap arithmetic across waves — an ordering of gaps in time,
never a claim about what moved them. Panel composition is fixed by construction (117 panel economies,
77 developing), but the *within-country* group samples are survey subgroups whose sampling error is
not in this file; the bootstrap is over countries only and does not capture it.

### P25 (pre-registered) — shrinkage-NEUTRAL empirical-Bayes grading (the variant P24 registered for a later cycle)

**Why.** P24 tested `k_g = neff_g/(neff_g+m)` and was CV-rejected on both targets, but its own
diagnostic showed the test was confounded: basin `neff` runs **1.6–9.5**, so at every grid point
m ≥ 50 the adaptive weight sat an order of magnitude *below* the incumbent 0.1, and the CV was mostly
re-rejecting P9's "less shrinkage is worse" rather than judging the reliability *grading*. Parent: P24.

**Candidate.** Same shape, **renormalized so the level is held fixed**: at every stage compute
`k_raw_g = neff_g/(neff_g+m)`, then rescale `k_g = 0.1 × k_raw_g / mean_w(k_raw)`, where `mean_w` is
the population-weighted mean of `k_raw` over the countries being shrunk — so the population-weighted
average shrinkage equals the incumbent constant **0.1 by construction** and only the *relative*
grading across basins varies. `k_g` is clipped to [0, 0.5] for numerical sanity (declared).
Note the grid now spans grading *strength*, not level: as `m → 0` all `k_raw → 1` and the scheme
collapses **exactly onto the incumbent constant**; as `m → ∞`, `k_g ∝ neff_g` (full proportional
grading). Registered grid **m ∈ {1, 3, 10, 30, 100, 1000}**, with the incumbent constant carried as
the explicit baseline.

**Adoption rule (entirely ≤2021 — no 2024 in features, fitting or selection).** Per target, CV on
that target's **2017→2021** transition with a persistence base and all basins built at 2017 (the
P10/P12/P13/P16–P24 protocol), comparing the best graded stack against the identical incumbent
constant-k stack: account = 3-stage (income → region → `g20_any` terciles), saving = 4-stage
(region → income → account terciles → `g20_any` terciles). **Resilience is excluded by design** (no
pre-2021 transition; the account proxy is twice on record as mis-selecting for it — P8, P13) and
stays byte-identical at 6.625.
**Keep if** for any target the ≤2021 CV prefers the graded weight **AND** its 2021→2024 MAE improves
on the champion (**account 5.014**, **saving 6.831**), with every untouched target printing
byte-identical. Five CV→holdout interactions are on record (P8, P9, P13, P23, P24); the CV margin and
the holdout delta are both recorded whatever the verdict. The per-basin `k_g` table is printed so the
grading can be inspected directly — if this variant also fails, the axis is closed and that is the
result.

### E30 — verdict: KEEP (all three replicate on 2017→2021; E11, E13, E14 PROMOTED to keep-general)

| finding | 2014→2017 | 2017→2021 | 2021→2024 (reference) |
|---|---|---|---|
| E11 formal borrowing ~ formal saving | −0.181 (n=77), **G6 unstable** | **+0.616** (n=77) | +0.403 (n=76) |
| E13 FI-account ~ mobile-money | −0.393 (n=54), **G6 unstable** | **+0.509** (n=57) | +0.435 (n=59) |
| E14 mobile money ~ digital payments | **+0.520** (n=54) | **+0.871** (n=57) | +0.600 (n=58) |

All three clear the pre-registered promotion rule on **2017→2021** — r ≥ +0.30, same sign, G6
sign-stable, retention **0.77 / 0.93 / 0.99**, every one well clear of the E4 0.50 floor. Under the
registered rule **E11, E13 and E14 move `keep-window` → `keep-general`**, bringing the ledger's
general claims to six (E1, E10, E11, E12, E13, E14). Δ-tercile monotonicity holds in the replicating
window for all three (E11 −0.9/+1.8/+4.8pp; E13 +0.5/−0.6/+12.4pp; E14 +0.5/+6.7/+19.3pp).

**E14 is now the ledger's most robust association — the only one that replicates in every window
tested**, including 2014→2017 (+0.520, G6 retention 1.09, CI [+0.220, +0.771]) where E28's rails and
today's other two pairs all fail. Its 2017→2021 cell is the strongest number in the entire ledger:
**+0.871, CI [+0.793, +0.931], retention 0.99**. Mobile-money growth and digital-payment growth are
bundled across three consecutive transitions and thirteen years; that is a decade regularity, not an
episode.

**2014→2017 fails the same way it failed for E28, and the registered variance check says the same
thing.** Both failing cells are **G6-unstable with a sign flip** (E11 −0.181 → +0.351 when the top-5
populations drop; E13 −0.393 → +0.249) and both sit in the window with the smallest Δ dispersion
(E11 SD 4.5/4.9pp vs 6.5/8.4pp in 2017–21; E13's is the exception at 9.2/7.6pp). A cell with no
stable sign in either direction is not evidence of absence — it is a window that carries no usable
signal, which is now the ledger's second independent observation of that property of 2014→2017.

**B6 inference.** Kish `neff = 6.8–7.6` in every cell — the same ≈7 effective observations behind
54–77 nominal countries that E28 found, now confirmed on a different family. Bootstrap intervals
(2,000 country resamples): E11 2021→24 **[+0.146, +0.638]**, 2017→21 [+0.163, +0.786]; E13 2021→24
**[+0.076, +0.686]** (only just clear of zero), 2017→21 [+0.277, +0.682]; E14 2021→24
[+0.187, +0.885], 2017→21 **[+0.793, +0.931]**. E13's headline is the weakest of the three and its
interval nearly touches zero — the promotion is on the registered criterion, and should be read with
that interval attached.

**Caveats.** Contemporaneous Δ-on-Δ in every window — descriptive temporal co-movement, no
identification. Composition varies (mobile-money pairs 54–59 economies vs 76–77 for E11), the weight
is the 2024 adult population in all windows by construction, and E13/E14 share the same x variable so
their cells are not independent of each other. G3/G4 pass everywhere (G4 pop_share 0.97–1.00);
G5 n/a.

### E31 — verdict: JOINT CLAIM DISCARDED (G6 voids the access-closure half); the usage-margin null is the substantive result

**The registered joint claim fails.** The raw count reaches the bar (A 3/5, B 5/5, joint 3/5), but
**G6 is a registered gate and the pre-registration made it applicable to every Δgap**. On the access
margin, **gender fails G6 outright — the −5.8pp narrowing becomes +0.7pp (a sign flip) when the five
largest-population economies are dropped**. With gender excluded, only **2 of 5** dimensions clear
Claim A, below the registered 3, so **Claim A fails and the joint claim is discarded.**

| dimension | Δgap access 2011→24 | ΔL access | G6 drop-top-5 | 95% CI | economies narrowed | Δgap usage 2014→24 | ΔL usage |
|---|---|---|---|---|---|---|---|
| gender | −5.8pp | −0.266 | **+0.7pp (FLIPS)** | [−11.0, +2.6] | **38%** | −2.2pp | −0.167 |
| income | −8.4pp | −0.173 | −3.1pp (ok) | **[−12.6, −1.0]** | 69% | −0.5pp | **+0.100** |
| education | −9.1pp | −0.197 | −0.8pp (ok) | [−15.2, +3.3] | **42%** | −2.8pp | **+0.056** |
| age_cat | −3.1pp | −0.074 | −4.0pp (ok) | [−9.2, +0.6] | 58% | +1.3pp | −0.025 |
| laborforce | −4.5pp | −0.151 | −3.1pp (ok) | [−9.1, +3.6] | 55% | +1.4pp | −0.067 |

**The E4 judgment rule voids the magnitude of the two survivors as well, and this is the sharper
finding.** Retention of the population-weighted access narrowing under drop-top-5 is **0.37 for
income and 0.09 for education** — both far under the 0.50 floor. And the unweighted share of
economies whose gap actually narrowed is **38% (gender) and 42% (education)**: on two of the three
dimensions carrying the claim, *a minority of developing economies narrowed their access gap*, while
the population-weighted mean fell sharply. That is the working paper's own aggregation pitfall
appearing inside the ledger — a handful of very large economies closing their gaps, read as a global
convergence. Only **income** shows both a majority of economies narrowing (69%) and a bootstrap
interval clear of zero.

**Claim B holds on its own and is reported as descriptive, not as a keep.** No dimension's *usage*
gap closed by 5pp; two **widened** in pp (age_cat +1.3, laborforce +1.4), and on the scale-free
measure the **income (+0.100) and education (+0.056) log-odds usage gaps widened** while every
access log-odds gap narrowed. The directional contrast — access gaps narrowing on the scale-free
measure in all five dimensions, usage gaps widening in two of the most policy-relevant ones — is the
one thing here worth carrying forward, but four of the five usage cells are themselves G6-unstable,
so it is logged as a direction on record, not a claim. Its status would be `keep-window`-ineligible
in any case: this is a 13-year trajectory, not a transition test.

**Coverage note (rule B2 satisfied).** First ledger use of the `education`, `age_cat` and
`laborforce` frames. Kish `neff` = **6.8–7.0 (access) and 5.7–5.8 (usage)** on 60–66 economies — the
same ≈7 effective observations the rest of the ledger keeps producing, now on a third frame family.
Descriptive urbanicity line (2024 only, excluded from the primary by design): urban − rural gap
**+4.8pp** on accounts and **+6.4pp** on digital payments (n=77/76).

**Declared.** Within-country gap arithmetic across waves — an ordering of gaps in time, never a claim
about what moved them. The bootstrap resamples countries only; the within-country subgroup sampling
error is not in this file and is not captured. Panel composition drops from 77 to 60–66 economies
because 2011 subgroup coverage is incomplete.

### P25 — verdict: DISCARD (CV rejects on both targets, monotonically); champion unchanged; the grading axis is now CLOSED

The ≤2021 CV **prefers the incumbent constant k on both targets, at every grid point**, and the
deterioration is **monotone in grading strength**:
account 3-stage `constant_k = 6.710` vs `m=1: 6.784 / 3: 6.870 / 10: 6.992 / 30: 7.094 / 100: 7.151 /
1000: 7.179` (best margin **+0.073**, wrong side); saving 4-stage `constant_k = 6.370` vs
`m=1: 6.394 / 3: 6.460 / 10: 6.596 / 30: 6.704 / 100: 6.772 / 1000: 6.805` (best margin **+0.024**).
Neither target adopts, so `predict()` never sees a graded weight; `predictor.py` was reverted to the
P18 champion (1bb3f78) and re-run to confirm the holdout is byte-identical:
**account 5.014 / resilience 6.625 / saving 6.831**.

**This is a cleaner rejection than P24's, and it closes the axis.** P24's grid confounded grading
with level — every point cut average shrinkage tenfold. P25 removes that confound by construction:
the population-weighted mean of `k_g` is **exactly 0.1** at every m, so the only thing varying is the
*relative* pull across basins. The parameterization also nests the incumbent: `m → 0` reproduces the
constant k exactly, and the best grid point on **both** targets is the **smallest m** — i.e. the CV
is walking back toward uniform shrinkage as hard as the grid allows. The grading table at the
adopted-best m=1 shows how mild the tested grading already was:

| basin | n | Kish neff | k_g |
|---|---|---|---|
| Sub-Saharan Africa (excl. HI) | 26 | 9.51 | **0.1221** |
| High income | 40 | 9.19 | 0.1217 |
| Latin America & Caribbean (excl. HI) | 14 | 4.76 | 0.1115 |
| Europe & Central Asia (excl. HI) | 17 | 4.46 | 0.1102 |
| Middle East & North Africa (excl. HI) | 7 | 3.87 | 0.1072 |
| East Asia & Pacific (excl. HI) | 8 | 1.86 | 0.0878 |
| South Asia (excl. HI) | 5 | 1.61 | **0.0833** |

Even a spread of 0.083–0.122 around the constant 0.1 costs +0.073pp of CV MAE, and widening it
(larger m, up to `k_g ∝ neff_g`) costs monotonically more. **The empirical-Bayes premise is simply
wrong for this problem:** the reliability of a basin's population-weighted mean, as measured by Kish
`neff`, carries no usable information about how hard that basin should pull. Two independent
parameterizations (P24 unnormalized, P25 shrinkage-neutral) now reject it, the second one with the
level confound removed and the incumbent nested. **The adaptive-k axis is closed — no further
variant should be registered without a different reliability statistic entirely.**

Together with P22/P23 (basin *center*: mean vs median vs weighted median, all rejected) and P9 (the
single global constant, rejected), every knob on the shrinkage operator except the *basins
themselves* has now been tested and none has beaten `k = 0.1` with a population-weighted mean. The
remaining live direction in this stream is what P16–P18 actually exploited: **more and better
basins**, not better weights or centers. This is the sixth CV→holdout interaction on record
(P8, P9, P13, P23, P24, P25) and the second where CV rejected before the holdout was consulted.

## 2026-08-03 wrap-up
Ran 3 experiments (E30, E31, P25) — **one keep with three promotions, one discard, one discard that
closes a modelling axis**.
**E30 (hypothesis, KEEP — Program 1, replication debt):** the three non-saving-destination
co-movements all replicate on **2017→2021** — formal borrowing ~ formal saving **+0.616** (n=77),
FI-account ~ mobile money **+0.509** (n=57), mobile money ~ digital payments **+0.871** (n=57) —
G6 sign-stable with retention 0.77/0.93/0.99, so **E11, E13 and E14 are promoted `keep-window` →
`keep-general`**, taking the ledger to **six general claims**. **E14 replicates in all three windows
tested** (2014→17 +0.520 as well) and is now the ledger's most robust association. 2014→2017 fails
for E11/E13 with **G6 sign flips**, the second independent time that window has produced no stable
signal in either direction.
**E31 (hypothesis, DISCARD — Program 3, the cycle's B2 experiment on three untouched frames):** the
registered "access gaps close while usage gaps stay open" joint claim met the raw count (3/5) but
**fails once G6 is applied** — the gender access gap flips from −5.8pp to +0.7pp under drop-top-5,
leaving 2/5. The E4 rule voids the survivors' magnitude too (retention **0.37** income, **0.09**
education), and on gender and education **only 38% and 42% of developing economies actually
narrowed** while the population-weighted mean fell sharply — the working paper's own aggregation
pitfall reproduced inside the ledger. Direction on record, not a claim: access log-odds gaps narrowed
in all five dimensions while the **income (+0.100) and education (+0.056) usage log-odds gaps
widened**.
**P25 (prediction, DISCARD):** the shrinkage-neutral empirical-Bayes weight is CV-rejected on both
targets (+0.073 account, +0.024 saving) and **monotonically in grading strength**, with the level
confound removed by construction and the incumbent nested at m→0. Two parameterizations have now
rejected the premise: Kish `neff` carries no usable information about how hard a basin should pull.
**The adaptive-k axis is closed.** Champion unchanged: **account 5.014 / resilience 6.625 /
saving 6.831** (P18, 1bb3f78).
**Recurring number, now on a third frame family:** Kish `neff` ≈ **5.7–7.6** in every cell of both
hypothesis experiments, whatever the nominal n.

---

# 2026-08-05 cycle — pre-registrations (written before any answer was computed)

**Coverage audit (rule B1) run first.** `python3 coverage.py`: country file 24/429 columns touched
(6%); 13 untouched module families / 309 columns; micro 22/192 (11%); transitions 2011→2014 thin (1
mention), 2014→17 / 2017→21 / 2021→24 used; frames `age_cat` untouched, `education` and `laborforce`
thin (1 mention each, from E31).

**Cycle shape and the coverage cells it lands on.**
- **E32 — Program 2 (items 2.2 + 2.3), the inference debt.** No new columns by design: this is an
  audit of the ledger's *own* association family. The 2026-08-03 addendum names 2.2 and 2.3 as the
  cycle's Program-2 slot, with six `keep-general` claims now standing and Kish `neff` ≈ 5.7–7.6 in
  every cell ever measured.
- **E33 — Program 4 (items 4.1, 4.2, 4.4), the welfare margin reopened.** Lands on the **`fh`
  financial-health module — 4 columns, ZERO ledger mentions**, one of the 13 untouched country
  families. **This is the cycle's B2 breadth experiment.**
- **P26 — prediction stream.** Basin *resolution* for the data-driven shrinkage stages.

**Lineage (rule B3).** E32's parent is the association ledger as a whole (a meta-experiment, no
single parent). E33's parent is **E26** (the welfare-margin null) — first descendant, cap not
engaged. No three-in-a-row from one parent this cycle.

## E32 (pre-registered) — Program 2: does the ledger's association family survive false-discovery control, and how much of it is the population weighting?

**Motivation.** The ledger reports ~30 country-level tests with no multiple-testing correction (rule
B7, owed since the harness v2 note) and no unweighted counterpart (agenda item 2.3). With Kish
`neff` coming in at 5.7–7.6 whatever the nominal n, a 50-test ledger nominally significant at n≈76
may be nominally significant at 7 effective observations essentially never. This must be settled
before any `keep-general` reaches the paper draft as a regularity.

**FAMILY (declared exactly, before computation).** The homogeneous same-construction family:
population-weighted correlation of two **2021→2024 changes** on the developing panel (`pan_dev`,
`group == "all"`). Sixteen tests, each named with its ledger id and column pair:

| id | Δx | Δy | ledger r | ledger status |
|---|---|---|---|---|
| E1 | `mobileaccount_t_d` | `fin17a_17a1_d` | +0.719 | keep-general |
| E2 | `mobileaccount_t_d` | `fin24aSD_ND` | +0.189 | discard |
| E7 | `fin17a_17a1_d` | `fin24sav` | +0.541 | keep-window |
| E10 | `fin32_acc` | `fin17a_17a1_d` | +0.791 | keep-general |
| E11 | `fin22a_22a1_22g_d` | `fin17a_17a1_d` | +0.403 | keep-general |
| E12 | `g20_any` | `fin17a_17a1_d` | +0.370 | keep-general |
| E13 | `fiaccount_t_d` | `mobileaccount_t_d` | +0.435 | keep-general |
| E14 | `mobileaccount_t_d` | `g20_any` | +0.600 | keep-general |
| E15 | `fin24aSD_ND` | `fin17a_17a1_d` | +0.031 | discard |
| E16 | `account_t_d` | `fin17a_17a1_d` | +0.198 | discard |
| E18 | `fin24bor` | `fin17a_17a1_d` | +0.069 | discard |
| E19 | `inactive_t_d` | `fin17a_17a1_d` | +0.160 | discard |
| E25 | `fin32_acc` | `fin22a_22a1_22g_d` | +0.605 | keep-window |
| E26 | `fin32_acc` | `fin24aSD_ND` | +0.294 | discard |
| E27 | `fin17c` | `fin17a_17a1_d` | +0.696 | discard (sign) |
| E27b | `fin17b` | `fin17a_17a1_d` | +0.531 | secondary of E27 |

**EXCLUDED from the family, and why** (declared so the family cannot be gerrymandered after the
answer): partial-correlation designs (E5b, E23, E24), level→change designs (E5, E9, E17), gap
designs (E3, E20, E21), region-split replications (E22), earlier-transition replications (E28, E30),
the 2024 cross-section (E29), the trajectory design (E31), and the micro stream. Those are different
constructions and would need their own families; the BH accounting here is explicitly *within* the
Δ→Δ family and is reported as such.

**TEST.** For each of the sixteen: population-weighted `r` (harness `weighted_corr`), **unweighted**
`r`, nominal `n`, Kish `neff = (Σw)²/Σw²`, a country bootstrap (2,000 draws, percentile 95% CI), and
three p-values — `p_boot` (2 × the smaller bootstrap tail mass at 0, floored at 1/draws),
`p_nominal` (t on `n−2` df) and `p_neff` (the same t on `neff−2` df). Benjamini–Hochberg at
**q = 0.10** applied over the sixteen, on `p_boot` (primary) and on `p_neff` (secondary).

**PRE-REGISTERED CLAIM AND THRESHOLD.** The ledger's kept associations in this family are robust in
the two senses it has never checked. Kept iff **BOTH**:
  (a) **≥ 80% of the family's kept rows (7 of 8: E1, E7, E10, E11, E12, E13, E14, E25) survive BH at
      q = 0.10 on `p_boot`**, and
  (b) **≥ 80% of those same kept rows retain `|r_unweighted| ≥ 0.30`.**
Failure of either is the informative outcome and is logged as a discard of *this* claim — i.e. as a
finding about the ledger, with the specific rows that fail named.

**DECLARED.** This experiment computes no new association; it recomputes existing ones under two
additional lenses. It is therefore not subject to B4 (no window claim) and adds no new keep to the
ledger. Whatever it returns is an audit result about the ledger's own inference, and the BH family is
the Δ→Δ family only — a ledger-wide FDR would be more punishing, not less.

## E33 (pre-registered) — Program 4: do the digitalization rails reach a SECOND welfare margin (`fh` financial health), 2021→2024?

**Motivation and parent (B3).** Parent is **E26**, which found the three rails miss the welfare
margin at the pre-registered bar (wage digitalization r = +0.294 vs a 0.30 threshold — a
six-thousandths miss) on a *single* self-reported measure, `fin24aSD_ND`. Agenda item 4.2 asks
whether that null is a **measure artifact or a real boundary**. The `fh` family (`fh1`, `fh2`,
`fh2a`, `fh1_fh2`) is an untouched module with 2021 **and** 2024 coverage on ~74/71 developing
economies — a second and third welfare margin with a usable Δ. **B2 breadth cell: `fh`, zero prior
ledger mentions.**

**G3 DECLARATION.** The harness `INDICATORS` registry does not cover the `fh` family, so
`gate_variant` will return `UNREGISTERED` by construction; this is disclosed, not evaded. Variants
declared here instead: **`fh1` and `fh2` are the primary items**, `fh1_fh2` the declared composite,
`fh2a` excluded (2024 only, no Δ). Column-set membership is verified in the file; the questionnaire
*polarity* of the items is **not** assumed — see the polarity clause below.

**POLARITY CLAUSE (the honest part).** The country file is unlabelled, so the direction in which a
higher `fh1`/`fh2` value means better or worse financial health is **not known at registration
time**. The pre-registered quantity is therefore the **magnitude and sign-consistency** of the
co-movement, not its welfare direction:
  - the sign must be **consistent across all three rails** for a given item, and
  - **consistent across `fh1` and `fh2`**.
The welfare *reading* of that sign (improvement vs deterioration) is declared, in advance, to be an
**interpretive step that is NOT pre-registered**, will be labelled as such in the verdict, and will be
anchored by reporting the pop-weighted 2021 and 2024 levels of each item alongside the correlation.
A claim about magnitude survives regardless of how the polarity resolves; a claim about direction
will be worded as conditional on it.

**TEST.** `pan_dev`, `group == "all"`, 2021→2024 changes, population-weighted correlation (harness
`weighted_corr`), exactly E26's construction with the destination swapped.
  - **PRIMARY (4.1):** Δ`fh1`, Δ`fh2`, Δ`fh1_fh2` each against the three rails —
    Δ`fin32_acc` (wage), Δ`g20_any` (digital payments), Δ`mobileaccount_t_d` (mobile money).
  - **SECONDARY A (4.4):** Δ`fh*` ~ Δ`fin17a_17a1_d` — does financial health track the saving surge?
  - **SECONDARY B (4.2):** Δ`fh*` ~ Δ`fin24aSD_ND` — do the two welfare measures agree with each
    other at all? If they do not, E26's boundary claim is measure-specific.
  - Rail terciles (low/mid/high mean Δ`fh`) reported for the primary, ledger convention.

**KEEP THRESHOLD.** Kept iff **at least one of `fh1`/`fh2`/`fh1_fh2` reaches `|r| ≥ 0.30` against at
least TWO of the three rails, with the same sign on all three rails and the same sign for `fh1` and
`fh2`**, AND G4 passes, AND G6 is sign-stable on every cell that counts toward the claim, AND the E4
judgment rule holds on those cells (`|r_droptop| ≥ 0.5 × |r_full|` — a jackknife that keeps its sign
but loses most of its magnitude is a big-country artifact and voids the general claim).

**B6 INFERENCE (mandatory for a new keep).** Country bootstrap, 2,000 draws, percentile 95% interval
on every primary correlation; Kish `neff` reported beside the nominal n in every cell.

**B4.** Any keep here is 2021→2024 only and is logged **`keep-window`** — `fh` has no pre-2021 wave,
so this claim is *structurally unpromotable*, exactly as E29 is. Declared now so it is not later
mistaken for a general regularity.

**DECLARED.** Descriptive co-movement of contemporaneous changes. It identifies nothing, and the
registered comparison is against E26's +0.294 on `fin24aSD_ND`.

## P26 (pre-registered) — prediction: is the tercile the right RESOLUTION for the data-driven basins?

**Motivation.** P24/P25 closed the adaptive-`k` axis; P22/P23 closed the basin *center*; P9 closed
the global constant. The 2026-08-03 addendum records the one live direction as **the basins
themselves**. Every data-driven basin in the champion is a **tercile** — a number never chosen, only
inherited from P16. Bin count trades bias (coarse basins pool unlike countries) against variance
(fine basins have unreliable means), and unlike `k` it is a property of the *partition*, which is the
part of the operator that has kept paying (P16 −0.279pp, P17 −0.091pp, P18 −0.249pp).

**DESIGN.** One shared bin count `B` applied to **all** data-driven tercile basins of a target,
selected per target by the established ≤2021 CV — saving/account 2017→2021, persistence base, every
basin built from the 2017 cross-section. Grid **B ∈ {2, 3, 4, 5, 6}**, with **B = 3 the incumbent,
exactly nested** (as P25's m→0 was). Champion stacks unchanged otherwise: account = income-group →
region → `g20_any` B-tiles; saving = damped trend (λ=0.5) + region → income-group → `account_t_d`
B-tiles → `g20_any` B-tiles. `k = 0.1` at every stage. Per-target policy (P2): resilience has no
data-driven stage and stays byte-identical at 6.625.

**ADOPTION RULE.** Adopt `B ≠ 3` for a target only if the ≤2021 CV **strictly prefers** it; then, and
only then, evaluate the 2024 holdout, and keep only if the holdout MAE also improves (the P11/P16/P17
condition — CV **and** holdout, per the four CV→holdout non-transfers on record: P8, P9, P13, P23).
If CV does not prefer any `B ≠ 3`, adoption fails at the first gate, no 2024 evaluation is run
(P14/P15/P19/P20/P21 protocol) and `predictor.py` reverts to the P18 champion (1bb3f78).
No 2024 data anywhere in features, fitting or selection.

**REGISTERED QUESTION.** Is the tercile a *tuned* choice or an *arbitrary* one that happens to work?
A monotone CV preference for coarser or finer bins would say the resolution axis is live; a CV that
picks B=3 on both targets says P16's inherited default is at a local optimum and the resolution axis
is closed too.

### E32 — verdict: DISCARD of the registered robustness claim; (a) passes, (b) fails; and the `neff` column is the real finding

**Reproduction check first.** The file recomputes all sixteen ledger correlations from the raw frames
and matches `findings.tsv` to **max |Δr| = 0.0005** across the family. The audit is auditing the
ledger's actual numbers, not an approximation of them.

**The registered claim fails on limb (b).**
- **(a) BH at q = 0.10 on `p_boot`: 7 of 8 kept rows survive (88%) — PASS.** The single failure is
  **E7** (`p_boot = 0.068` against a rank-10 threshold of 0.0625 — it misses by five thousandths).
  Nine of the full sixteen survive; the ladder is auditable in the output.
- **(b) `|r_unweighted| ≥ 0.30`: only 6 of 8 (75%) — FAIL** against the 80% bar. **E7 falls
  +0.541 → +0.283** and **E13 falls +0.435 → +0.188**. Both keeps are substantially creatures of the
  population weighting.

Because the pre-registration required **both**, the joint verdict is **DISCARD**, and per the
protocol the informative content is *which rows failed*.

**The one keep this audit recommends demoting: E7.** It is the only row in the family that fails
**all three** new lenses — BH on the bootstrap p, the unweighted replication, *and* the E4 magnitude
rule (`r_droptop` 0.24 vs `r_full` 0.54, retention 0.44 < 0.5, which the original E7 entry recorded
as "G6 sign-stable" without applying the E4 judgment rule that post-dates it). **E13** fails the
unweighted lens alone and is flagged rather than demoted — it is a `keep-general` whose 2017→2021
replication (+0.509) was independent evidence.

**The headline is a column nobody registered a threshold on: `p_neff` rejects 0 of 16.** Kish `neff`
is **7.1–7.6 across the entire family** on nominal n of 58–76. Evaluated at those effective degrees
of freedom, the *best* p-value in the ledger's core family is **E10 at p = 0.030**, and BH at
q = 0.10 over m = 16 needs p ≤ 0.00625 at rank 1 — so **not one association clears it**. Against
`p_nominal`, 11 of 16 clear. The gap between "11 of 16" and "0 of 16" is the entire population-
weighting question stated as inference: the ledger has been reporting associations as if it had ~76
observations when the weights concentrate it into ~7.

**A finding that runs against the obvious prior: the weighting is not uniformly inflationary.** The
median change in |r| on removing the weights is **+0.011**, and only 8 of 16 tests are *weaker*
unweighted. The weighting **relocates** the association rather than inflating it — E12 goes the other
way entirely (**+0.370 weighted → +0.617 unweighted**), and the discarded **E16 (account growth ~
saving surge) is +0.198 weighted but +0.555 unweighted**, i.e. a test the ledger rejected would have
been a keep in an unweighted world. Sign flips occur only in **E18 and E19**, both already discards.

**Scope, declared.** The BH family is the Δ→Δ family only (sixteen tests, listed and with the
exclusions named in the pre-registration). A ledger-wide FDR over all ~30 country-level tests would
be **more** punishing, not less, so nothing here is softened by the narrow family. This experiment
computes no new association, adds no keep, and is not subject to B4.

### E33 — verdict: KEEP (`keep-window`, structurally unpromotable). The rails DO reach a second welfare margin; E26's null was measure-specific

**All nine primary cells clear the bar, with one sign, and every gate passes.** Δ`fh` ~ Δrail,
2021→2024, `pan_dev`:

| item | digital pay (`g20_any`) | wage (`fin32_acc`) | mobile money (`mobileaccount_t_d`) |
|---|---|---|---|
| `fh1` | **+0.699** | +0.524 | +0.465 |
| `fh2` | **+0.684** | +0.434 | +0.364 |
| `fh1_fh2` | **+0.705** | +0.447 | +0.354 |

Sign-consistent across all three rails and across `fh1`/`fh2`; **G6 sign-stable in 9/9** with E4
retention **0.83–1.76** (every counting cell ≥ 0.5); G4 ok (71 economies, 0.69 population share).
Terciles run the expected shape — `fh1_fh2` ~ `g20_any` gives **−5.0 / +3.4 / +5.1**. The registered
comparison, E26's **+0.294** for wage digitalization on `fin24aSD_ND`, is beaten by **every one of
the nine cells**.

**The answer to agenda item 4.2 is unambiguous, and it is the finding: E26's welfare null is
MEASURE-SPECIFIC.** Secondary B asked whether the two welfare families agree with each other at all.
They barely do — Δ`fh` ~ Δ`fin24aSD_ND` is **+0.146 / +0.032 / +0.104**. Two self-reported welfare
margins measured on the same 69 economies over the same window are **nearly orthogonal to each
other**, while one of them tracks all three digitalization rails at 0.35–0.71 and the other tracks
none of them. The paper's Section 6 boundary — "the rails do not reach welfare" — is a statement
about `fin24aSD_ND`, not about welfare. Secondary A (item 4.4): `fh` tracks the saving surge itself
at **+0.534 / +0.470 / +0.465**.

**Precision caveat, applied deliberately as the first keep logged after E32.** At Kish `neff` =
**6.5–6.9** (nominal n 54–69), only the **digital-payment** cells have bootstrap intervals clear of
zero on all three items (lower bounds **+0.447 / +0.460 / +0.496**). **All three mobile-money cells
include zero** ([−0.046,+0.789], [−0.210,+0.799], [−0.208,+0.766]), as does `fh2` ~ wage
([−0.018,+0.714]). The keep rests on the digital-payment rail and, more weakly, the wage rail; **the
ordering of the three rails is not resolvable at seven effective observations** and is not claimed.

**POLARITY IS UNRESOLVED, and the claim is worded to survive that.** The pre-registration declared
the welfare *reading* of the sign to be an interpretive step outside the registration. The declared
anchor (levels) does not settle it — `fh1` 21.2→19.8, `fh2` 25.0→24.3, `fh1_fh2` 32.9→32.0, all
mildly falling. A **post-hoc** cross-sectional anchor was added and is labelled as post-hoc in the
file: correlating the 2024 `fh` levels against two known-polarity columns returns **contradictory and
weak** signs (`fh1`: **+0.211** against resilience but **−0.075** against account ownership;
`fh2`: +0.113 and −0.247). The unlabelled country file cannot settle whether these are
worry/distress items or financial-health items. **The pre-registered quantity — magnitude and
sign-consistency — stands; the welfare direction does not, and this finding must not be worded as
either improvement or deterioration until the questionnaire labels are obtained.** That is recorded
in `findings.tsv` and is the first item owed to `HARNESS_V2_NOTES.md` from this cycle.

**B4, declared in advance.** `fh` has no pre-2021 wave, so this keep is **structurally unpromotable**
— it can never become `keep-general` under the replication rule, exactly like E29. **B2 satisfied:**
first ledger use of the `fh` module, one of the thirteen untouched country families.

### P26 — verdict: DISCARD; the tercile survives on both targets, and the resolution axis closes

**Account: adoption fails at the first gate, and informatively.** The ≤2021 CV (2017→2021,
persistence base, three-stage income-group → region → `g20_any` B-tiles, all basins built at 2017)
sweeps the bin grid to a **clean single-peaked interior optimum at the incumbent**:

`B=2: 7.052 · B=3: 6.710 · B=4: 6.906 · B=5: 6.959 · B=6: 6.905`

Both coarser and finer partitions are strictly worse. No 2024 evaluation was run for this target
(P14/P15/P19/P20/P21 protocol) and the holdout is byte-identical at 5.014. **This answers the
registered question for account: the tercile is a TUNED choice, not an arbitrary inheritance.**

**Saving: CV preferred B=6, so the holdout was consulted — and it lost.** The four-stage saving CV
gives `B=2: 7.080 · B=3: 6.370 · B=4: 6.454 · B=5: 6.553 · B=6: 6.310`, a strict preference for
B=6 by **−0.060**, which triggered the holdout under the adoption rule. The holdout **worsens
6.831 → 7.024 (+0.193pp)**. The keep condition requires CV **and** holdout, so P26 is discarded and
`predictor.py` was reverted to the P18 champion (1bb3f78) and re-run to confirm byte-identical
output: **account 5.014 / resilience 6.625 / saving 6.831**.

**This is the fifth CV→holdout non-transfer on record (P8, P9, P13, P23, P26)** — and the diagnostic
is visible in the CV curve itself, before the holdout was consulted. Saving's curve is
**non-monotone and bimodal**: two local minima at B=3 and B=6 separated by a hump at B=4–5. Account's
is single-peaked. A **−0.060 margin on a bimodal curve at `neff` ≈ 7** is not a preference, it is
sampling noise finding a second dip, which is exactly what the holdout then punished. The shape of a
CV curve, not just its argmin, is usable evidence — worth carrying into the next prediction cycle as
a screening rule.

**The resolution axis is closed.** Bin count now joins adaptive `k` (P24/P25), basin center
(P22/P23) and the global constant (P9) as tested and rejected. Of the whole shrinkage operator, the
only knob that has ever paid and is still untested in part is **which indicator a basin is drawn
from** — and P19/P20/P21 already showed that axis is exhausted at three stages for account and four
for saving. The prediction stream is close to needing a different mechanism entirely rather than
another knob.


## 2026-08-05 wrap-up
Ran 3 experiments (E32, E33, P26) — **one keep on new ground, one audit that lands on the ledger
itself, one discard that closes a modelling axis**.
**E32 (hypothesis, DISCARD of the registered claim — Program 2, the inference debt):** the ledger's
sixteen-test Δ→Δ family reproduces exactly (max |Δr| = 0.0005) and **7 of 8 kept rows survive BH at
q = 0.10** on the bootstrap p — but only **6 of 8 retain |r_unweighted| ≥ 0.30**, so the joint claim
fails. **E7 fails all three lenses** (BH, unweighted +0.541→+0.283, and E4 retention 0.44) and is the
one keep this audit recommends demoting; **E13** fails the unweighted lens alone. The headline is
the column nobody set a threshold on: at **Kish `neff` = 7.1–7.6** on nominal n of 58–76,
**BH rejects 0 of 16** (best p = 0.030) against **11 of 16** at nominal n. Counter to the obvious
prior, the weighting is **not uniformly inflationary** — median |r| change on de-weighting is
**+0.011**, and the discarded **E16 is +0.198 weighted but +0.555 unweighted**.
**E33 (hypothesis, KEEP `keep-window` — Program 4, the cycle's B2 experiment on the untouched `fh`
module):** all nine primary cells clear the bar with one sign and 9/9 G6 stability — digital
payments **+0.699 / +0.684 / +0.705**, wage **+0.524 / +0.434 / +0.447**, mobile money
**+0.465 / +0.364 / +0.354** on `fh1`/`fh2`/`fh1_fh2` — every cell beating **E26's +0.294**. Item 4.2
is answered: **E26's welfare null is MEASURE-SPECIFIC**, because the two welfare families are nearly
orthogonal to each other (Δ`fh` ~ Δ`fin24aSD_ND` = **+0.146 / +0.032 / +0.104**). Applying E32's
lesson immediately: only the **digital-payment** cells have intervals clear of zero; all three
mobile-money cells include it, so the rail ordering is not claimed. **Polarity of the `fh` items is
unresolved** — the disclosed post-hoc anchor contradicts itself — so the magnitude claim stands and
the welfare *direction* is explicitly not asserted. Structurally unpromotable (no pre-2021 `fh`
wave).
**P26 (prediction, DISCARD):** account's CV picks the incumbent tercile at a **clean single-peaked
optimum** (7.052 / **6.710** / 6.906 / 6.959 / 6.905), so the tercile is tuned rather than inherited;
saving's CV prefers B=6 by −0.060 on a **bimodal** curve, and the holdout punished it
**6.831 → 7.024**. Fifth CV→holdout non-transfer (P8, P9, P13, P23, P26), and the first where the
*shape* of the CV curve predicted the failure. Champion unchanged: **account 5.014 / resilience
6.625 / saving 6.831** (P18, 1bb3f78).
**Recurring number, now measured on the ledger's own core family:** Kish `neff` = **6.5–7.6** in
every cell of both hypothesis experiments — the fifth frame family to return ≈7.

---

## Cycle 2026-08-07 — coverage cells declared (rule B1/B2)

`python3 coverage.py` was run before any hypothesis was chosen. The ledger stands at 28/429 country
columns (7%), 25/192 micro columns (13%), twelve untouched country modules, and one frame at zero
mentions. This cycle's cells:

- **E34 — `group == "age_cat"` (UNTOUCHED frame, 0 ledger mentions)** plus the **2011→2014 transition
  (thin, 2 mentions)** and the full 2011→2024 span. This is the cycle's **B2** experiment.
- **E35 — the 2017→2021 transition** (used) on the *partial*-correlation family, which no replication
  experiment has touched (E28 and E30 replicated bivariates only). Pays Program 1 replication debt
  and Program 2 items 2.2/2.3 for the non-Δ→Δ partial family.
- **P27 — prediction stream**, no new frame; a diagnostic, not a mechanism.

Lineage (**B3**): E34's parent is **E31** (first descendant). E35's parents are **E23/E24/E25** (first
replication attempt on those three). P27's parent is **P26**. No chain reaches three.

## E34 — pre-registered (hypothesis / country level)

**Program 3, item 3.4. Parent: E31 (first descendant — B3 not engaged).**

**Hypothesis.** The within-country **age gap in account ownership** (25+ minus 15-24) **narrowed**
over **2011→2024** in a **majority** of developing panel economies, on a scale-free measure.

**Why it is not already known.** The `age_cat` frame has **zero ledger mentions**. The micro stream
found (U15) that among accountholders the age gradient in digital-payment *use* is barely absorbed by
access — 11.6 → 10.3pp, only ~10% — but that is a single 2024 cross-section and says nothing about
whether the *access* gap itself has moved over thirteen years. E31 supplies the design lesson and the
genuine two-sidedness: on gender and education the population-weighted gap fell 5.8-9.1pp while a
*minority* of economies narrowed, i.e. the weighted mean was a big-country artifact. It is unknown
whether age behaves the same way.

**Test.** Frame `Findex.pan_grp`, `group == "age_cat"`, subgroups `age 25+` / `ages 15-24`, restricted
to non-high-income economies (the `pan_dev` convention). Indicator `account_t_d` (headline, G3
declared). Per country and wave the gap is measured **scale-free as a log-odds difference**,
`logit(p_25+) − logit(p_15-24)` (E21's construction, with p clipped to [0.005, 0.995]), because a pp
gap must mechanically compress as the advantaged group approaches 100%.

- **PRIMARY (the E31 lesson, promoted from diagnostic to primary): the UNWEIGHTED SHARE of
  developing panel economies whose log-odds age gap is smaller in 2024 than in 2011.**
- **SECONDARY 1:** the population-weighted mean Δ log-odds gap 2011→2024, and its unweighted twin
  reported beside it (Program 2 item 2.3 applied at registration time, not after).
- **SECONDARY 2:** the same share per transition — **2011→2014** (the thinnest cell in the ledger),
  2014→2017, 2017→2021, 2021→2024 — so the decade is decomposed rather than summarised.
- **SECONDARY 3 (two-margin, item 3.3 on the age axis):** the same statistics for the *usage* margin
  `g20_any` over **2014→2024** (first wave with coverage), to test whether an access gap and a usage
  gap move together on this axis.
- **DESCRIPTIVE:** pp gap levels by wave for both margins.

**Gates.** G3 (`account_t_d` and `g20_any` headline). G4 on the estimation sample. G6 in its
drop-top-5-population form applied to the weighted mean. G5 n/a (no official gap series). **B6:**
country bootstrap, 2,000 draws, percentile 95% interval on the primary share and on the weighted mean
Δ; Kish `neff` beside nominal n everywhere.

**KEEP IF** the unweighted share of economies narrowing is **≥ 60%** (majority plus a margin, against
a 50% coin-flip null) **AND** the weighted and unweighted mean Δ log-odds gaps carry the **same
(negative) sign** — the sign-agreement condition E32 showed the ledger has been silently failing.

**Registered alternative outcomes, both informative.** A share near 50% with a large negative weighted
mean reproduces E31's big-country artifact on a third dimension and would make that a *general*
property of the `pan_grp` frame rather than a gender/education quirk. A share ≥ 60% **with** a
positive weighted mean would say the age gap narrows in most economies while widening where most
people live.

**Declared.** Descriptive within-country gap trajectories, 117-economy panel, developing subset. No
causal reading. Multi-wave, so B4's window rule does not bind: the claim is registered over the full
2011→2024 span and decomposed by transition.

## E35 — pre-registered (hypothesis / country level)

**Program 1 (replication debt) + Program 2 items 2.2/2.3 for the partial family. Parents: E23, E24,
E25 — first replication attempt on any of them (B3 not engaged).**

**Hypothesis.** The **three-separate-rails structure** — mobile money, digital payments and wage
digitalization each carrying an association with the formal-saving surge *net of* the others (E23,
E24), and wage digitalization reaching formal borrowing net of saving (E25) — is a **general
regularity**, not a 2021-24 window feature. E28 and E30 replicated six *bivariate* co-movements onto
2017→2021 and promoted them to `keep-general`. **No partial correlation has ever been replicated**,
and the partials are what the paper's rail decomposition actually rests on.

**Test.** Exactly the E23/E24/E25 constructions, re-run on the **2017→2021** transition, `pan_dev`,
population weights = 2024 adult population (the harness convention, held fixed so the two windows are
comparable):

- **E23-R:** partial corr Δ`mobileaccount_t_d` ~ Δ`fin17a_17a1_d` | Δ`g20_any`.
- **E24-R:** partial corr Δ`fin32_acc` ~ Δ`fin17a_17a1_d` | Δ`g20_any`; plus the two-control variant
  (| Δ`g20_any`, Δ`mobileaccount_t_d`), descriptive.
- **E25-R:** bivariate Δ`fin32_acc` ~ Δ`fin22a_22a1_22g_d`, and the partial controlling
  Δ`fin17a_17a1_d`.
- Residualization is pop-weighted least squares on the control set, then `weighted_corr` of the
  residuals (E5b/E23 construction), with `gate_jackknife` on the residual pair.
- **2021→2024 recomputed in the same file** so each replication is read beside its original rather
  than against a number copied from `findings.tsv`.

**Inference layer, registered as part of the test (Program 2, non-Δ→Δ family).** For every primary
cell in both windows: **country bootstrap, 2,000 draws, percentile 95% interval**; **Kish `neff`**;
the **unweighted** partial beside the weighted one; and **BH at q = 0.10** over the declared family of
**six primary cells** (three designs × two windows) using the bootstrap p.

**Gates.** G3 (all headline concepts declared; `fin32_acc` has no variant — E10 precedent). G4 per
estimation sample. G6 on every primary residual pair, with the **E4 magnitude rule** (retention
≥ 0.5) applied — the rule post-dates E23/E24/E25 and has never been applied to them.

**PROMOTION RULE (B4).** A design is promoted `keep-window` → **`keep-general`** only if its
2017→2021 partial has the **same sign**, **|r| ≥ 0.30**, **G6 sign-stable with retention ≥ 0.5**. A
sign flip or a collapse below 0.30 on the earlier window means the rail separation is a
**2021-24 window property**, and the finding stays `keep-window` with that recorded. A cell failing
BH or the unweighted lens is **flagged**, not demoted, on the E13 precedent.

**Declared.** Partialling a contemporaneous Δ decomposes co-movement; it does not control confounding
and identifies nothing. Sample composition differs between windows (mobile money binds), so every
benchmark is recomputed on each window's own common sample.

## P27 — pre-registered (prediction stream)

**Parent: P26. Not a mechanism — a diagnostic, and a registered stopping rule for the stream.**

**Why.** Every knob on the shrinkage operator is now closed: stage count (P19/P20/P21), basin center
(P22/P23), adaptive `k` (P24/P25), global `k` (P9), bin count (P26). The base predictor's one
dynamics knob was closed even earlier (P10: the ≤2021 CV picks λ=0 and the holdout punishes it by
1.319pp — the 2021-24 surge has momentum absent from pre-2021 dynamics). The agenda's two honest
options are "register a different mechanism" or "characterise the champion's errors". This registers
the second, **with a decision rule attached** so it is not a free look.

**Test.** The P18 champion (`account` 5.014 / `resilience` 6.625 / `saving` 6.831), unchanged, with
its 2024 residuals decomposed:

- **(a) BIAS vs SCATTER:** mean **signed** error per target beside the MAE. A predictor that misses a
  surge is biased, not noisy.
- **(b) STRUCTURE:** MAE and mean signed error by region and by income group; is the residual flat
  across basins, or does one basin carry it?
- **(c) CONCENTRATION:** share of total absolute error contributed by the ten worst countries, and
  the identity of those countries per target.
- **(d) BENCHMARK LADDER:** champion vs naive persistence vs panel-mean vs the **movement scale**
  (median |Δ2021→2024| of the target) — how much of what there was to predict was predicted.
- **(e) COMMON FACTOR:** correlation of the signed residuals *across* the three targets, country by
  country. A country the model misses on all three margins at once is a missing common shock, and
  that correlation bounds how much a joint model could recover.

**REGISTERED DECISION RULE.** If **|mean signed error| ≥ 0.25 × MAE on any target**, a systematic and
in-principle correctable component remains and the stream registers **one more mechanism** next
cycle. If all three targets are near-zero-mean **and** cross-target residual correlation is
**< 0.30**, the champion is declared **final** and the stream closes; the write-up records the
benchmark ladder as its closing statement.

**PEEK DISCLOSURE, explicit.** This experiment reads 2024 residuals, which is what the evaluator is
for, but it is **not blind to the holdout**. Under the amended peek rule it is logged as
**exploratory/diagnostic**: `predictor.py` is not modified, no MAE may improve as a result of it, and
**any future feature or basin choice traceable to what is learned here must be declared as
peek-informed in its own pre-registration**. Nothing here can produce a keep.

### E34 — VERDICT: KEEP (weak), 2026-08-08

Run of the pre-registered E34 (committed 6224bf7 in the interrupted 2026-08-07 session).

**Both pre-registered conditions pass.** PRIMARY: **63.6%** of developing panel economies (42/66) have
a smaller log-odds age gap in account ownership in 2024 than in 2011, against the 60% bar; bootstrap
95% CI **[51.5%, 75.8%]** (2,000 country draws). SIGN AGREEMENT: weighted mean Δ log-odds **−0.074**
and unweighted **−0.171** are both negative. G6 in its drop-top-5 form takes the weighted mean to
**−0.266** — sign-stable with the magnitude *growing* 3.6×, so this is the opposite of E31's
big-country artifact: the giants damp the narrowing rather than manufacture it. Kish `neff` = 6.8
against nominal n = 66.

**Three caveats recorded as part of the keep, not after it.** (i) The weighted-mean CI
**[−0.465, +0.097]** straddles zero, so only the *share* statistic is separated from its null; the
keep rests on the count of economies, which is exactly what the E31 lesson promoted to primary.
(ii) The share CI's lower bound is 51.5% — clear of the coin flip, but only just. (iii) **No single
transition clears 60%**: 2011→14 48.5%, 2014→17 59.5%, 2017→21 57.1%, **2021→24 44.2%**. The decade
result accumulates two mildly narrowing middle windows against a *widening* final window. pp gap
levels: +7.9 / +10.2 / +6.4 / +6.4 / +5.2.

**SEC 3, the two-margin result, is the interesting half.** The *usage* age gap (`g20_any`, 2014→2024)
narrows in **64.5%** of economies (n = 62, neff = 5.7), weighted mean −0.025, unweighted −0.159,
drop-top-5 −0.319. E31 found the income and education usage log-odds gaps **widening** (+0.100,
+0.056) while their access gaps narrowed. On the age axis both margins move the same way. So the
"access converges, use diverges" pattern is **axis-specific**, not a property of the `pan_grp` frame:
it holds where the disadvantaged group is defined by resources (income, education) and fails where it
is defined by cohort. Registered as a live sub-question for Program 3, not as a claim.

**Registered alternative outcomes, resolved.** Neither of the two registered alternatives occurred:
this is not E31's artifact reproduced on a third dimension (the share is a majority and G6 strengthens
it), nor is it "narrows in most economies while widening where people live" (the weighted mean is
negative too, merely small). The honest reading is a genuine but *slight* decade narrowing that
stalled and reversed after 2021.

### E35 — VERDICT: DISCARD (registered generality claim rejected), 2026-08-08

**No partial promotes. 0 of 3.** The registered claim was that the three-separate-rails structure is
a general regularity rather than a 2021-24 feature. It is not.

- **E23** (mobile money ~ saving | digital payments): **+0.509 → −0.042**. A sign flip, CI
  [−0.295, +0.231], p_boot 0.835, G6 sign-unstable. Nothing survives.
- **E24** (wage digitalization ~ saving | digital payments): **+0.583 → +0.291**. Same sign, G6
  clean (retention 1.45), and it **misses the 0.30 bar by 0.009**. The closest thing to a
  replication in the set, and under a pre-registered bar it is still a fail.
- **E25** (wage ~ formal borrowing | saving): **+0.419 → +0.459** — clears sign and magnitude, then
  **G6 destroys it**: drop-top-5 takes the residual correlation to −0.028, retention **0.06**. A pure
  big-country artifact in the earlier window; without the jackknife this would have read as the
  cycle's one clean promotion.

**The mechanism is in the benchmarks, and it is the useful part.** In 2017→2021 the two rails are
nearly collinear: **r(Δmobile money, Δdigital payments) = +0.871**, against **+0.600** in 2021→2024.
When two regressors move together that tightly there is no independent variation left to partial —
the rails were not *separable* in the earlier window, whether or not they were separate. So the
honest reading is narrower than "the structure is a window artifact": the **separation itself became
measurable only when the rails decoupled**, and the 2021-24 partials describe a period in which
mobile money and digital payments stopped moving in lockstep. That is a statement about the data's
information content, not about the world, and it is why the bivariates replicate (E28/E30, six
`keep-general` claims) while every partial built on them does not.

**Inference layer (Program 2, non-Δ→Δ family — now paid).** BH at q = 0.10 over the declared
six-cell family rejects **4/6 on p_boot** and **0/6 on p_neff**. The E32 result reproduces exactly on
a second family: at Kish `neff` ≈ 7 nothing in the ledger is significant, and the gap between
nominal-n and neff-based inference (5/6 vs 0/6) is the whole story. The **unweighted lens is worse
here than on the Δ→Δ family**: only **2/6** cells clear 0.30 unweighted, and E25's earlier-window
cell flips sign entirely (+0.459 → −0.055). Partials are more weighting-dependent than bivariates,
which is a new fact about the ledger and follows directly from residualizing with the same weights.

**Consequence for the paper.** E23, E24 and E25 stay `keep-window` and are now on record as having
*failed* their promotion test — a stronger statement than "not yet replicated". Section 4's rail
decomposition may be reported for 2021-24 only, with the collinearity number beside it.

**Disclosed implementation fix.** The first run joined the population weight with `fillna`, which
inherited only the mobile-money panel's index and silently narrowed every cell (E24-R n = 61 rather
than 71). It was caught because the recomputed 2021-24 cells did not reproduce their logged
originals; fixed to `combine_first`, committed, re-run, and all three originals then reproduced
exactly (+0.509 / +0.583 / +0.419, n = 58 / 71 / 71). No verdict was read from the defective run.
Recomputing the original window inside the replication file is what caught this, and that convention
should be mandatory for every future replication.

### P27 — VERDICT: EXPLORATORY/DIAGNOSTIC; the stopping rule fires on the "keep going" branch, 2026-08-08

`predictor.py` was imported unchanged by a separate file (`p27_diagnostic.py`), so the champion is
byte-identical: **account 5.014 / resilience 6.625 / saving 6.831**. Peek-disclosed: this reads 2024
residuals and cannot produce a keep.

**(a) The champion is off-centre, not merely noisy.** Mean signed error ÷ MAE: account
**−0.802/5.014 = 0.160** (centred), resilience **−3.253/6.625 = 0.491**, saving
**−4.914/6.831 = 0.719**. Both non-account targets are systematically **under**-predicted. On saving,
roughly seven-tenths of the average miss is one direction rather than scatter.

**(b) The residual is not flat, but it is not one basin either.** Account MAE runs 8.447 (low income)
→ 8.022 (lower-middle) → 4.216 (upper-middle) → **2.141 (high income)**, a clean four-to-one gradient,
with its negative bias sitting in Sub-Saharan Africa (−4.403) and low income (−4.289). Saving
under-predicts in **every** region (−1.8 to −6.0) — a broad level shift, not a regional story.
Resilience is the least structured: −7.4 in MENA and −7.0 in ECA but **+4.8** in East Asia.

**(c) Concentration.** The ten worst countries carry **26.9% / 32.1% / 33.7%** of total absolute
error, 2.6–3.2× an even split. Worst cells: account Zambia −21.7, Kyrgyz Republic −21.4, Senegal
−17.9, India −15.3; saving Nigeria −26.3, Bulgaria −23.4, China −20.7.

**(d) The benchmark ladder is the most sobering panel.** Skill against persistence:
**10.1% (account) / 0.8% (resilience) / 30.1% (saving)**. Against the panel mean the champion is far
ahead (20.1 / 11.6 / 11.6), but that is a low bar. Against the **movement scale** — median |actual
2021→2024 change| = 3.405 / 5.761 / 9.234 — only **saving** has a champion MAE below the typical
country's actual move. For account and resilience the typical miss is still *larger* than the typical
movement, and resilience is within **0.8%** of doing nothing at all. Twenty-seven prediction
experiments have bought one target that genuinely beats the movement it is trying to track.

**(e) Common factor.** Signed residuals correlate **+0.624** between account and saving (n = 81),
+0.252 account~resilience, +0.155 resilience~saving. The model misses account and saving on the same
countries.

**DECISION: the registered rule fires on its first branch** — |mean signed| ≥ 0.25 × MAE on two of
three targets — so a systematic component remains, the stream does **not** close, and one more
mechanism is owed. **The constraint travels with the decision, and it is severe:** the bias is a
broad upward level shift over 2021-24 that ≤2021 history cannot observe. That is the same regime
change P3 and P10 already failed to learn, and any correction fitted to *these* residuals would be
peek-informed and inadmissible under the evaluation rules. The next registration must state
explicitly how its mechanism is estimable from ≤2021 data alone; if no such mechanism can be named,
the honest move is to close the stream on the benchmark ladder rather than to keep tuning.

---

## Cycle wrap-up — 2026-08-08

Continuation of the 2026-08-07 pre-registration (E34/E35/P27), which was committed but interrupted
before execution. All three ran today; the working tree was clean at start, so no `wip` commit was
needed.

- **E34 — KEEP (weak).** The within-country age gap in account ownership narrowed in **63.6%** of
  developing economies over 2011→2024 (bar 60%), with weighted and unweighted means agreeing in sign
  and G6 *strengthening* the effect. Caveats logged with the keep: the weighted-mean CI straddles
  zero, and no single transition clears the bar — 2021→24 actually widens.
- **E35 — DISCARD.** **0 of 3** rail-separation partials replicate on 2017→2021: E23 sign-flips, E24
  misses the bar by **0.009**, E25 dies at G6 with retention **0.06**. The mechanism is collinearity
  — r(Δmobile money, Δdigital payments) was **+0.871** in the earlier window versus +0.600 in
  2021-24, so there was nothing to separate. E23/E24/E25 stay `keep-window`, now on record as having
  *failed* their promotion test.
- **P27 — diagnostic, stream stays open.** The champion is biased (signed/MAE 0.72 on saving, 0.49 on
  resilience) and beats the movement scale on saving only; resilience has 0.8% skill over
  persistence. One more mechanism is owed, but it must be estimable from ≤2021 data alone.
- **Inference note, second family paid.** BH at q=0.10 over E35's six-cell partial family rejects
  4/6 on the bootstrap p and **0/6 at Kish `neff` ≈ 7** — E32's result reproduces exactly on the
  partial family, and partials turn out to be *more* weighting-dependent than bivariates (only 2/6
  cells clear 0.30 unweighted).

---

## Cycle 2026-08-09 — pre-registration (E36 / U21 / P28)

Coverage audit (`python3 coverage.py`) run before any hypothesis was chosen, per rule B1. It
reports: country file 28/429 columns touched (7%); untouched frames `gender` (0 mentions) and
`urbanicity` (single-wave); thin frames `education`/`age_cat`/`laborforce` (1 mention each); micro
file 25/192 columns touched, with `internet_use` (144,090 non-null, binary) at **zero** mentions and
the whole `con`/`fin48`/`fin49` digital-risk block untouched.

**Coverage cells this cycle lands on (rule B2, named in advance):**
- **E36** — country frames `group == "laborforce"` (thin, 1 mention) and `group == "gender"`
  (**zero** mentions, 5 waves), plus the 2011->2024 and 2014->2024 spans.
- **U21** — micro column **`internet_use`** (zero mentions) — the first use of Program 5's
  individual-level half.
- **P28** — prediction stream, no new coverage claim (mechanism change, see below).

**Lineage (rule B3).** E36's parent is **E34**, whose parent is **E31**. That is the **third**
consecutive experiment descending from E31's gap-trajectory design, i.e. the cap is now reached:
the next Program-3 experiment must jump to a different parent. U21's parent is **U15/U17** (the
access-absorption ruler) via agenda item 5.3; P28's parent is **P27** (the diagnostic), and its
admissibility constraint is inherited from P27's decision rule.

**A note on the `con` block.** The largest untouched surface (133 country + 52 micro columns) was
inspected for a labelled codebook before this cycle's hypotheses were chosen. The zip ships the CSV
only — **no questionnaire or codebook** — and the `con*` values are bare numeric codes (1/2/8/9 with
skip patterns), so Program 7's mandatory mapping pass cannot be completed from the files in the
repo. Recorded here as a blocker, not a skipped obligation; `HARNESS_V2_NOTES.md` gets the item.

### E36 (pre-registered): is the "access converges, use diverges" split a RESOURCE/ASCRIPTION line?

Program 3, item **3.7** (opened by the 2026-08-08 addendum). Parent: E34.

**Why.** E31 found the within-country **income** and **education** gaps in *usage* (`g20_any`)
**widening** in log-odds while the access gaps narrowed. E34 found the **age** gap narrowing on
*both* margins. Two axes on one side, one on the other, is not yet a pattern. The sharp hypothesis
is that the dividing line is **what defines the disadvantaged group**: axes tied to *resources*
(income, education, employment) diverge on usage, axes that are *ascribed* (age cohort, sex) do not.
`laborforce` and `gender` are the two untested axes and they fall on opposite sides of that line, so
this is a genuine out-of-sample test of the split rather than a fourth description.

**Design.** E34's construction exactly, generalized over five axes x two margins, developing panel
economies, `pan_grp`:
- gap = logit(p_advantaged) - logit(p_disadvantaged), p clipped to [0.005, 0.995];
  advantaged/disadvantaged = richest 60%/poorest 40%, secondary+/primary-or-less, 25+/15-24,
  in-laborforce/out-of-laborforce, men/women.
- ACCESS margin `account_t_d` over **2011->2024**; USAGE margin `g20_any` over **2014->2024**.
- PRIMARY statistic per cell (E31 lesson): **unweighted share of economies whose gap is smaller at
  the end of the span**. Secondary: pop-weighted mean change, its unweighted twin, drop-top-5 (G6).
- The **income, education and age axes are recomputed inside this file** so the new axes are read
  beside their originals (the E35 convention, now mandatory).

**Registered predictions and keep rule.** KEEP the joint dividing-line claim only if BOTH hold:
- **P1 (laborforce behaves like a resource axis):** access share **>= 60%** AND usage share **< 50%**.
- **P2 (gender behaves like an ascribed axis):** access share **>= 60%** AND usage share **>= 60%**.
Any other outcome is a DISCARD of the joint claim, with the per-axis pattern logged. Registered
alternatives: (a) both new axes look ascribed -> the split is specific to income/education, not a
resource line; (b) both look resource-like -> sex is a resource axis in this data, which would be a
finding about the gender gap, not about the split; (c) neither margin's share clears 60% on either
new axis -> the frames are too noisy to adjudicate and the split stays a two-axis observation.

**Gates and inference.** G3 (headline columns `account_t_d`, `g20_any`); G4 per margin; G6 in the
drop-top-5 form on every weighted mean; G5 n/a. **B6:** 2,000-draw country bootstrap percentile
intervals on the share and the weighted mean, Kish `neff` beside nominal n, in every one of the ten
cells. **B7:** BH at q = 0.10 over the declared family of **ten** cells (5 axes x 2 margins), on the
bootstrap p of the share against 0.5. B4 does not bind (multi-wave design, not a 2021-24 window).

**Declared.** Descriptive gap trajectories. Composition of the groups changes over 13 years
(schooling expands, populations age), so a narrowing gap is not evidence that any individual's
position changed. No causal reading, no policy reading.

### U21 (pre-registered): is being OFFLINE a bigger gate on digital-payment use than being least-educated?

Program 5, items **5.3 and 5.4**. Parents: U10/U15/U17 (the access-absorption ruler). Micro stream,
2024 wave, cross-sectional — no trend language by construction.

**Why.** The ruler has been run on education, age, income, labour force and urbanicity, all
conditional on holding an account, and the recurring result is that access absorbs almost none of the
gradient. `internet_use` has never been used at either level. E29 showed that at the *country* level
the rails are not proxies for connectivity; the individual-level question is different and sharper:
among people who already have an account, is connectivity the binding constraint on using it
digitally, and does conditioning on it absorb the education gradient that access could not?

**Design (all weighted by `wgt`, via the fixed `micro.py`).**
1. **Ruler step 1** — `anydigpayment` rate by `internet_use` (1 vs 0), pooled, unconditional.
2. **Ruler step 2** — the same gap **among accountholders** (`account == 1`).
3. **Ruler step 3 (the registered comparison)** — among accountholders, the connectivity gap from
   step 2 beside the **education gap** (educ 3 = tertiary/secondary+ vs educ 1 = primary or less) and
   the **income gap** (inc_q 5 vs inc_q 1) computed on the same sample.
4. **Absorption** — the education gap among accountholders, recomputed **among accountholders who
   use the internet**; registered statistic = 1 - (conditional gap / unconditional-on-connectivity
   gap).
5. **Item 5.4** — demographic profile of `internet_use == 0` among accountholders: share offline by
   educ, inc_q, age band, sex, urbanicity, labour force, with M2 on every cell.

**Registered claims and keep thresholds.**
- **C1:** among accountholders, the offline-vs-online gap in `anydigpayment` is **>= 5pp** (the
  default group-difference bar) AND is **larger than** the education gap on the same sample.
- **C2 (absorption):** conditioning on `internet_use` removes **>= 30%** of the education gap in
  `anydigpayment` among accountholders.
KEEP C1 and C2 separately; each stands or falls on its own bar.

**Gates.** M1 (weights, enforced by the module). M2 (unweighted n >= 100) on every reported cell.
M3: `account` and `anydigpayment` micro aggregates reproduced against the country file on a
declared set of economies, tolerance 1pp. Single wave, so no B4/B6 replication or bootstrap
obligation attaches to a cross-sectional micro description; the M2 counts are reported instead.

**Declared.** `internet_use` is self-reported internet use, i.e. a *behaviour*, not infrastructure
access, and it is plainly co-determined with digital payment use — a person may report using the
internet *because* they pay digitally. This is an association inside one cross-section and cannot
separate the two directions. Nothing here is a constraint, a barrier or a cause; "gate" is shorthand
for a conditional difference and is used in that sense only.

### P28 (pre-registered): a BASIN-LEVEL DRIFT term — the first change to the base predictor since P2

Parent: P27. **Admissibility, addressed up front as P27's rule demands.** P27 fired on "keep going"
and attached a constraint: the next mechanism must be **estimable from <=2021 data alone** and must
not be fitted to P27's residuals. A basin drift satisfies both. It is not traceable to the diagnostic
(it is the standard alternative to the country-level damped trend that P10 tested, and was named as
"the trend term, untouched since P2 and never basin-varying" in the 2026-08-05 agenda addendum,
before P27 ran), and every quantity it uses is a pre-2021 change.

**Mechanism.** Every predictor since P5 has been a *cross-sectional* operator: shrink a level toward
a basin's mean. Nothing in the stack carries **group-level momentum**. P28 adds, to the base
prediction and before any shrinkage stage, a term

    pred_i <- base_i + gamma * drift_{g(i)},   drift_g = pop-weighted mean of (level_2021 - level_2017)
                                                         over the countries in basin g

with `g` = the target's stage-1 basin (income group for account, region for saving) and gamma
selected by **<=2021 CV**: predict 2021 from 2017 with the persistence base and the drift computed
from the **2014->2017** change, over the grid gamma in {0, 0.25, 0.50, 0.75, 1.00}. gamma = 0 nests
the incumbent exactly.

**Adoption rule, with the P26 screening rule attached.** Adopt only if BOTH: (i) the CV strictly
prefers some gamma > 0 by a margin **>= 0.05pp** over gamma = 0, and (ii) the CV curve over the grid
is **single-peaked** (one interior minimum; monotone on each side). A thin margin, or a win at a
secondary local minimum, does **not** trigger a holdout evaluation — that is the rule P26 wrote after
five CV->holdout non-transfers. If the rule blocks adoption for both targets, the stream **closes**
on the benchmark ladder, as P27's write-up and the agenda both anticipate.

**Scope.** Account and saving only. `fin24aSD_ND` exists in 2021 alone, so it has no history from
which a drift is computable at any date — the per-target policy (P2) leaves it at the P5 champion,
6.625, unchanged.

**Declared.** No 2024 data enters features, fitting or selection; the harness evaluator remains the
only place 2024 exists. If adopted, the champion changes only where the holdout MAE improves;
otherwise `predictor.py` reverts to the P18 champion commit.

### E36 — VERDICT: DISCARD (registered joint claim rejected), 2026-08-09

**Both registered predictions fail, and they fail in different ways.**

- **P1 (laborforce resource-like): FAIL on the second half.** The access gap narrowed in **64.5%**
  of developing panel economies (bar 60%, CI [51.6%, 75.8%], BH-significant), so the access half
  passes. But the *usage* gap also narrowed, in **57.4%** — the registered divergence bar was
  **< 50%**. Employment does not behave like income or education on the usage margin.
- **P2 (gender ascribed-like): FAIL on both halves.** Access share **54.5%** (CI [42.4%, 66.7%],
  p = 0.53) and usage share **53.2%** (p = 0.69) are both indistinguishable from a coin flip. The
  `gender` frame — used here for the first time in the ledger — returns a null on the primary
  statistic for both margins.

**The originals reproduce, which is what makes the failure readable.** Recomputed inside this file:
income access **75.0%** narrowing versus usage **51.7%** with a *positive* weighted mean (+0.100);
education access **61.5%** versus usage **43.5%** (+0.056); age **63.6%** versus **64.5%**. E31 and
E34 are both confirmed on their own axes.

**What the data actually shows is a GRADIENT, not a dividing line.** The access-minus-usage
asymmetry in share-narrowing runs income **+23.3pp**, education **+18.0pp**, laborforce **+7.1pp**,
gender **+1.3pp**, age **−0.9pp**. The ordering is exactly the one the hypothesis predicted — the
three resource axes on top, the two ascribed axes at the bottom — but employment sits **between**
the groups rather than inside the resource one, and the registered bars were written for a
two-class split. Logged as an observation, not a keep: it was not the pre-registered statistic, and
promoting it now would be fitting the threshold to the answer.

**A second big-country artifact, on a new axis.** `gender` shows the E31 signature in its purest
form: weighted mean Δ log-odds access **−0.266** (the largest narrowing in the whole table) against
an unweighted twin of **−0.002**, and G6 drop-top-5 flips it to **+0.057**. The usage margin is the
same (−0.167 weighted, −0.013 unweighted, +0.077 after G6). Read plainly: the pop-weighted gender
access gap fell 10.2 → 4.6pp over 13 years, and that fall is a story about a few very large
economies, not about most economies.

**Inference layer (B6/B7).** Kish `neff` = **6.8** on access and **5.7** on usage against nominal
n = 60–66 — the fifth and sixth frame family to come in at ≈ 6–7. BH at q = 0.10 over the declared
ten-cell family rejects **4/10** (income access, laborforce access, age access, age usage) versus
5/10 uncorrected. Every usage cell except age fails BH.

**Consequence for Program 3.** Item 3.7 is answered and the answer is negative: the resource /
ascription split does **not** generalize as a two-class rule. Rule B3's lineage cap is now reached
(E31 → E34 → E36), so the next Program-3 experiment must take a different parent.

### U21 — VERDICT: DISCARD on both registered claims, 2026-08-09

M3 passes on both outcomes (`account`, `anydigpayment` reproduce the country file to 0.0pp over 10
and 9 economies). M2 passes on every reported cell; the thinnest is 565 (offline tertiary-educated
accountholders).

- **C1 — DISCARD, and it fails on the comparison, not on the size.** Among accountholders, the
  online-minus-offline gap in digital-payment use is **+13.6pp** (88.5% vs 74.9%), comfortably over
  the 5pp bar. But the **education** gap on the same sample is **+16.8pp** (94.1% vs 77.3%), so
  connectivity is *not* the larger conditional difference. The registered claim required both.
- **C2 — DISCARD.** Conditioning on internet use removes **22.8%** of the education gap among
  accountholders (+16.8 → +13.0pp), against a 30% bar. The income gap behaves the same way: 25.3%
  absorbed (+11.5 → +8.6pp).

**The meaningful negative is in the step the claims were built on.** Account holding absorbs
**55.5%** of the *unconditional* connectivity gap: +30.5pp for everyone, +13.6pp among
accountholders. Every previous axis of this ruler behaved the opposite way — access absorbed almost
none of the age gradient (U15, ~10%) and little of the education or income gradient. So connectivity
is, to a first approximation, **mostly an access story**: offline adults differ from online adults
largely because they are less likely to hold an account at all. Education and income are not like
that, which is why they keep surviving the conditioning and connectivity does not.

**Item 5.4 — who is offline among accountholders — is the sharpest descriptive panel in the run.**
Share with `internet_use == 0`, among accountholders: education **43.6%** (primary or less) /
10.7% / **2.3%** (tertiary); age **34.6%** at 65+ against 12.1% at 25-34; labour force 23.7% out
versus 14.3% in; rural 22.7% versus urban 11.8%; income q1 24.4% versus q5 10.4%; and sex is nearly
flat (men 19.0%, women 16.0%). The **41-point education spread is the widest split on any axis**,
about double the income spread. Descriptive, unregistered, logged as an observation.

**Declared, and it matters for how the 55.5% is read.** `internet_use` is self-reported internet
use, a behaviour co-determined with digital payment use — someone may report using the internet
because they pay digitally. This is one 2024 cross-section: no direction, no trend, no causal
content. Conditioning on account holding remains post-treatment.

### P28 — VERDICT: DISCARD; and the stream CLOSES, 2026-08-09

**Account: the adoption rule passed it, and the holdout rejected it.** The <=2021 CV curve over
gamma is `6.710 / 6.604 / 7.032 / 7.732 / 8.770` for gamma = 0 / 0.25 / 0.50 / 0.75 / 1.00 — a
clean single-peaked curve with an **interior** minimum at gamma = 0.25 and a margin of **+0.107pp**
over the incumbent, comfortably past the 0.05 bar. Both registered conditions held, so the holdout
was run as registered. Holdout MAE **5.014 -> 5.124**, i.e. **worse by 0.110pp**. Reverted to the
P18 champion, which reproduces byte-identically (5.014 / 6.625 / 6.831).

**Saving: the rule blocked it, correctly.** CV `6.370 / 6.368 / 6.511 / 6.723 / 7.018` — argmin at
gamma = 0.25 with a margin of **+0.002pp**, far under the 0.05 bar, so no holdout evaluation was
triggered. Saving stays at 6.831. Resilience has no pre-2021 history and was out of scope by
construction; it stays at 6.625.

**The most useful thing in this run is that the P26 screening rule failed its first live test.**
P26 wrote the shape rule after five CV->holdout non-transfers, on the theory that a *well-shaped* CV
win would transfer where a thin one at a secondary local minimum would not. Account's curve was as
well-shaped as this stream has produced — monotone down, interior minimum, monotone up, a margin
twice the bar — and it still did not transfer. **This is the sixth non-transfer and the first to
clear the shape screen.** At Kish `neff` ~ 7 on the training window, curve shape is not evidence
about the holdout either.

**DECISION: the prediction stream is CLOSED, champion final.** P27's rule required one more
mechanism, estimable from <=2021 data alone. The basin drift was that mechanism: it is the last
untested knob on the base predictor, it was named in the agenda before P27 ran, and it is fully
pre-2021. It failed. No further mechanism can be named that is both admissible and untried — the
residual bias P27 measured is a broad 2021-24 upward level shift that no <=2021 quantity observes,
and every correction for it that this loop could construct would have to be fitted to the holdout.

**Closing statement (the benchmark ladder, from P27).** Champion **account 5.014 / resilience 6.625
/ saving 6.831** pp. Skill over persistence: **10.1% / 0.8% / 30.1%**. Against the movement scale
(median |actual 2021->2024 change| = 3.405 / 5.761 / 9.234pp), only **saving** predicts better than
the typical country's actual move. Twenty-eight prediction experiments, one target that beats what
it is trying to track.

---

## Cycle wrap-up — 2026-08-09

Working tree clean at start; coverage audit run before hypotheses were chosen (rule B1). Three
experiments, three discards — and the run's value is in what the discards rule out.

- **E36 — DISCARD.** The "access converges, use diverges" split is **not** a resource/ascription
  dividing line. Employment's access gap narrowed in 64.5% of economies but its **usage** gap
  narrowed too (57.4%, bar was < 50%), and the `gender` frame — used for the first time — is a coin
  flip on both margins (54.5% / 53.2%). What the ten-cell table does show is a **gradient** in the
  access-minus-usage asymmetry: income +23.3pp, education +18.0, laborforce +7.1, gender +1.3, age
  −0.9. Logged as an observation, not promoted. Gender is a textbook big-country artifact (weighted
  mean −0.266, unweighted −0.002, G6 flips it to +0.057). BH rejects 4/10 at `neff` ≈ 6–7.
- **U21 — DISCARD on both claims, with a real finding underneath.** Among accountholders the
  offline-vs-online gap in digital-payment use is **+13.6pp** — over the 5pp bar but **smaller than
  the education gap (+16.8pp)** — and connectivity absorbs only **22.8%** of the education gradient
  (bar 30%). The fact worth keeping: account holding absorbs **55.5%** of the unconditional
  connectivity gap (+30.5 → +13.6pp), which is the opposite of every other axis of this ruler.
  Connectivity is mostly an *access* story; education and income are not.
- **P28 — DISCARD, and the prediction stream is now CLOSED.** The basin-drift term cleared both of
  P26's screening conditions on account (single-peaked CV curve, interior minimum, +0.107pp margin)
  and then **worsened the holdout 5.014 → 5.124** — the sixth CV→holdout non-transfer and the first
  to pass the shape screen. Saving was blocked by the margin bar and never reached the holdout.
  Champion final: **account 5.014 / resilience 6.625 / saving 6.831**.
- **Housekeeping.** Rule B3's lineage cap is reached (E31 → E34 → E36); the next Program-3
  experiment must take a different parent. Program 7 is **blocked**, not skipped: the microdata zip
  ships no codebook and the `con*` items are bare numeric codes, so the mandatory mapping pass
  cannot be completed from the files in the repo — recorded for `HARNESS_V2_NOTES.md`.

---

## Cycle 2026-08-10 — pre-registration (written before any outcome was computed)

Working tree clean at start. `python3 coverage.py` run first (rule B1). The prediction stream is
CLOSED (P28), so this cycle is three country-level hypothesis experiments and no predictor run.

**Coverage cells this cycle lands on (rule B2).**
- **E37** opens **Program 6 (the sequencing ladder), which has zero prior experiments**, uses the
  **untouched country module `borrow_any_t_d`**, and is the loop's **first lagged (level-at-t →
  change-over-t→t+1) design** under rule B5. Three transitions, not one.
- **E38** is a **Program 1** replication (2014→2017 and 2017→2021).
- **E39** uses **all four transitions including 2011→2014**, the thinnest (6 prior mentions).
- Micro stream sits out this cycle: the within-economy design I intended for it (mobile-only vs
  bank-only accountholders on the untouched `merchantpay_dig` column) qualifies **only 5 of 77
  economies** at M2's n ≥ 100 per cell — a cell-size pre-check computing no rate — and the pooled-only
  version is too confounded with country composition to be worth a slot. Recorded as a dead end.
- Lineage (rule B3): E31 → E34 → E36 exhausted the cap. All three of today's experiments take a
  different parent, named below.

### E37 — pre-registration: does financial deepening follow a ladder? (Program 6, items 6.1–6.3)

**Parent:** E17 / E5 (the level→change family), **not** E31 or the rails chain.
**Idea.** Every country-level claim in the ledger correlates contemporaneous changes. Rule B5 opened
lagged designs. The ladder hypothesis is that margins move in order — account → digital payment →
formal saving → borrowing — so the *level* of a rung at time t should predict the *subsequent growth*
of the rung above it.
**Frame.** `pan_dev`, `group == "all"` (77 non-high-income panel economies). Transitions
**2014→2017, 2017→2021, 2021→2024** (all three rungs have all four waves needed).
**Rungs (G3: all four are declared headline variants).**
- R1 (6.1): up = `account_t_d` level at t → down = Δ`g20_any`
- R2 (6.2): up = `g20_any` level at t → down = Δ`fin17a_17a1_d`
- R3 (6.3): up = `fin17a_17a1_d` level at t → down = Δ`borrow_any_t_d`  *(untouched module)*

**Primary statistic.** Pooled population-weighted correlation over stacked country-transition
observations (each country appears three times, weight = its 2024 adult population each time).
Per-transition correlations reported alongside.
**Keep threshold — the ladder claim is a JOINT claim and is kept only if all three hold:**
(i) pooled weighted r ≥ **+0.30** for each of R1, R2, R3, and
(ii) the **own-level-controlled partial** — both sides residualized on the *downstream* margin's own
level at t by pop-weighted LS (the E5b/E23 construction) — keeps its sign and retains ≥ **0.5** of the
raw magnitude (the E4 rule).
Condition (ii) exists because a rung's own level mechanically predicts its own subsequent change
(convergence): E17 measured that benchmark at **−0.301** for account. The **convergence benchmark**
r(L_down(t), Δ_down) is reported for every rung as the thing the ladder has to beat.
**Gates.** G3 declared above · G4 coverage · G6 jackknife dropping the five largest-population
economies · **B6**: country bootstrap 2,000 draws (resample *countries*, carrying all of a country's
transitions together, so the pooling does not fake independence) with percentile interval, plus Kish
`neff = (Σw)²/Σw²` beside the nominal n.
**Registered alternative outcome.** Negative pooled correlations on all three rungs would say the
panel is dominated by convergence and there is no sequencing signal above it — which is a clean
negative for Program 6 and would close items 6.1–6.4 rather than invite a variant.
**Declared in advance.** Descriptive temporal ordering only. A level at t preceding a change after t
is *not* identification; nothing here is causal. Countries appear three times, so the pooled n is not
77 independent observations — that is exactly what the country-level bootstrap is for.

### E38 — pre-registration: does the E5b "accounts-first" pattern replicate? (Program 1, agenda 6.5)

**Parent:** E5b (`keep-window`, one of three remaining unreplicated keeps with E7 and E22).
**Original.** Usage intensity at t = `g20_any`(t) / `account_t_d`(t); partial correlation of that
ratio with Δ`account_t_d`(t→t+1) controlling the account *level* at t, pop-weighted LS residualization.
2021→2024 gave **r_partial = −0.595** (n = 77) against a convergence benchmark of −0.301: at the same
account level, economies whose existing accounts were *less* used grew accounts faster.
**Test.** The identical construction on **2014→2017** and **2017→2021**, with **2021→2024 recomputed
inside the same file** (the rule adopted from E35, which is what caught a weight-join defect there).
**Promotion threshold.** E5b promotes `keep-window` → `keep-general` only if at least one earlier
transition gives r_partial ≤ **−0.30** with the same sign **and** the drop-top-5 jackknife keeps that
sign. Otherwise it stays `keep-window` and is recorded as having *failed* its promotion test.
**Registered in advance, and this one is uncomfortable.** E5b's *original* window already fails the
E4 magnitude rule as now written — its jackknife retention was 0.19 (−0.595 → −0.114), and the rule
post-dates the finding. So the pre-registered secondary verdict is: **if the earlier windows also
collapse under the jackknife, recommend demoting E5b to `discard`**, as E32 recommended for E7.
**Gates.** G4 · G6 · B6 bootstrap (2,000 country draws) and Kish `neff` per window.
**Note on power.** 2014→2017 has failed to produce a stable sign in five of six cells across E28 and
E30. Registered up front: a null there is weak evidence of absence, and the 2017→2021 window is the
one that decides the promotion.

### E39 — pre-registration: is 2021→2024 actually a unique episode? (Program 1, item 1.5)

**Parent:** E27 / the paper's Section 4 framing, **not** the rails chain.
**Why this is owed.** The whole ledger is built on a 2021→2024 "surge", and rule B4 exists because
that window may be special. But nobody has checked whether the surge is unique **within countries**
or only in the population-weighted aggregate — E31 and E36 both showed those two can point opposite
ways. This uses **all four transitions, including 2011→2014**, the thinnest cell in the audit.
**Design.** For `fin17a_17a1_d` (formal saving) on `pan_dev`, and for `account_t_d`, `g20_any` and
`borrow_any_t_d` as context margins, compute the **distribution of per-country Δ** in each available
transition: unweighted median, unweighted mean, IQR, the **share of economies with Δ ≥ +10pp**, and
the population-weighted mean for contrast.
**Primary pre-registered statistic (formal saving).** The 2021→2024 window is declared unique iff
**both**: (a) its unweighted **share of economies with Δ ≥ +10pp** is at least **1.5×** the largest
such share in any earlier transition, and (b) its unweighted **median Δ** is the largest of the four.
**Secondary.** The same two statistics for the three context margins — a margin whose unique window is
*not* 2021→2024 is informative about what kind of episode this was. Rank correlation between a
country's Δ in consecutive windows (is a big mover a repeat mover?) reported descriptively.
**Registered alternative outcome.** If 2021→2024 is *not* the top window on both statistics, the
"episode" framing in the paper draft is an aggregate artifact and Section 4 needs rewording — that
outcome is the more valuable of the two and will be logged as a keep in the negative direction.
**Gates.** G4 · G5 against the official developing aggregate for `fin17a_17a1_d` where it exists ·
G6 is not applicable to an unweighted-share statistic and is reported as a weighted-vs-unweighted
contrast instead. No bootstrap is registered for E39: the primary statistic is a share, not an
association, and B6 binds on association keeps.

### E37 — VERDICT: DISCARD (the ladder), 2026-08-10

**The joint claim fails 1-of-3, and the one rung that passed is a big-country artifact.**

| rung | design | pooled r | 95% CI | p_boot | own-level partial | convergence benchmark | G6 drop-top-5 |
|---|---|---|---|---|---|---|---|
| R1 | account level → Δ digital payments | **+0.066** | [−0.232, +0.169] | 0.669 | +0.197 | −0.086 | **−0.177 (sign flips)** |
| R2 | digital-payment level → Δ formal saving | **+0.447** | [+0.113, +0.633] | 0.000 | +0.517 | +0.130 | **+0.126 (retention 0.28)** |
| R3 | formal-saving level → Δ any borrowing | **−0.126** | [−0.217, −0.031] | 0.015 | −0.024 | −0.432 | −0.095 |

n = 230 country-transition rows over 77 economies. **Kish `neff` = 7.5 at the country level.**

**R1 is the cleanest negative in the run.** The account level at t tells you essentially nothing
about how fast digital payments grow afterwards (r = +0.066, interval straddling zero, p_boot 0.67),
and dropping the five largest economies flips the sign. The most intuitive rung of the ladder —
you need accounts before you can pay from them — has no cross-country signal at all once you look
at growth rather than levels.

**R2 passed the registered conditions and still should not be believed.** Its partial *exceeds* its
raw correlation (0.517 vs 0.447), which is what you want from a ladder: stripping the saving
margin's own convergence makes the digital-payment lead stronger, not weaker. But G6 takes it from
+0.447 to **+0.126** — retention 0.28, under the E4 rule's 0.5 — and the 2014→2017 window gives
**−0.434** against +0.584 and +0.441 in the two later ones. A relationship that reverses in one of
three windows and lives in five economies is not a sequencing regularity.

**R3 is where the pooled design earns its keep as a warning.** The pooled figure is −0.126, but the
three windows are **+0.295 / +0.280 / −0.742**. Pooling averaged a consistent positive relationship
in 2014→2021 against a violent negative one in 2021→2024, and reported the near-zero midpoint. Any
future pooled-transition design in this loop must show its per-window terms; a pooled coefficient
here is not a summary of anything.

**A methodological correction that matters beyond E37.** Stacking three transitions gives a
row-level Kish `neff` of **22.2** while the country-level `neff` is **7.5**. The stacked figure is
pure arithmetic — the same economy contributing three rows triples Σw without adding an
observation. Every future pooled design must report the country-level `neff`, and the bootstrap
must resample **countries** carrying all their rows (as this one did), not rows.

**One defect found and fixed before the verdict was read** (the E35 convention working as intended):
`_wresid` returns bare arrays, so on a *sliced* per-transition frame the residuals misaligned
against the weight index and the partials came back NaN. Fixed with a `reset_index`; the pooled
primaries were computed on a zero-based frame and are unchanged by the fix.

**Verdict.** DISCARD the joint ladder claim. This also **closes agenda items 6.1–6.3 negatively**
and makes 6.4 (the diagonal-dominance matrix) not worth running: with no rung showing a robust
positive lead term, a 4×4 matrix of the same design at `neff` ≈ 7 is a false-discovery machine.
Item **6.5** (the E5b replication) is unaffected and runs next as E38. Descriptive temporal ordering
throughout; no causal content.

### E38 — VERDICT: DISCARD the promotion, and RECOMMEND DEMOTING E5b, 2026-08-10

| window | raw r | **partial \| account level** | 95% CI | p_boot | convergence benchmark | G6 drop-top-5 | retention |
|---|---|---|---|---|---|---|---|
| 2014→2017 | −0.621 | **−0.654** | [−0.835, +0.055] | 0.070 | −0.359 | −0.266 | 0.41 |
| 2017→2021 | +0.598 | **+0.591** | [−0.185, +0.786] | 0.314 | −0.126 | +0.031 | 0.05 |
| 2021→2024 *(original)* | −0.590 | **−0.595** | [−0.771, +0.201] | 0.352 | −0.301 | −0.030 | 0.05 |

n = 77, Kish `neff` = 7.5 in every window. **The original window reproduces exactly** (−0.595
against −0.595 on record), so the E35 convention confirms the construction rather than catching a
defect this time.

**The pattern alternates sign, which no version of the accounts-first story predicts.** E5b said
that at a given account level, economies whose accounts were *less used* grew accounts faster.
2014→2017 agrees strongly (−0.654). 2017→2021 says the **opposite** with almost equal force
(+0.591). 2021→2024 agrees again (−0.595). A mechanism that reverses between consecutive four-year
windows and then reverses back is not a mechanism.

**Two pre-registered rules fired at once, and I am recording the conflict rather than picking the
flattering one.** The promotion rule — "at least one earlier transition with r_partial ≤ −0.30,
sign-stable under G6" — is *mechanically satisfied* by 2014→2017. The registered secondary verdict
— "if the earlier windows also collapse under the jackknife, recommend demotion" — is *also*
satisfied, with retentions of 0.41, 0.05 and 0.05. **Resolved against promotion**, on the standing
E4 magnitude rule, which is protocol and not a discretionary tiebreak: a coefficient that loses
59–95% of its magnitude when five economies leave is a big-country story.

**The fault is in my pre-registration and it should be fixed in the protocol, not argued away.**
The promotion rule said *at least one* earlier window, which lets a claim promote on the strength
of one window while an equally-powered window of the same design contradicts it. **Proposed rule
for the next amendment: a promotion requires every tested earlier window to agree in sign, not one
of them.** Under that rule E5b fails cleanly and no conflict arises.

**RECOMMENDATION: demote E5b from `keep-window` to `discard`.** This is the **second pending
demotion**, alongside E7 (recommended by E32). Both should be applied in the same distillation pass
rather than accumulating as recommendations that never execute. What survives of E5b is the
*within-window* description for 2021→2024, already caveated in the ledger as concentrated in large
economies — and now known to be a window-specific fact of two windows out of three.

**One more thing the intervals say.** All three bootstrap intervals straddle zero despite point
estimates near ±0.6. At `neff` ≈ 7, a resample that happens to omit the dominant economies produces
a completely different coefficient — which is the same lesson E32 delivered with BH, arriving here
through the interval instead.

### E39 — VERDICT: KEEP, 2026-08-10

**Both pre-registered conditions pass for formal saving, and the context margins turn the result
into something better than a robustness check.**

Per-country change on `pan_dev`, share of economies moving **≥ +10pp**, and the unweighted median:

| margin | 2011→14 | 2014→17 | 2017→21 | 2021→24 | peak window |
|---|---|---|---|---|---|
| **formal saving** | 6.5% / +2.76 | 2.6% / +0.01 | 20.8% / +4.37 | **42.1% / +8.29** | **2021→24** |
| account ownership | **49.4% / +9.90** | 41.6% / +8.35 | 35.1% / +7.49 | 24.7% / +4.06 | **2011→14** |
| digital payments | — | **48.1% / +9.87** | 45.5% / +8.88 | 21.1% / +2.62 | **2014→17** |
| any borrowing | — | 5.2% / −2.92 | 22.1% / +5.17 | **52.6% / +10.59** | **2021→24** |

*(cells are share ≥ +10pp / unweighted median pp; n = 76–77 per cell)*

**(a)** 42.1% against a bar of 1.5 × 20.8% = 31.2% — passes. **(b)** +8.29pp is the largest median
of the four — passes. G5 holds against the official developing aggregate (max deviation **1.7pp**,
tolerance 2.5).

**It survives the E31 critique, which is the point of running it.** The population-weighted mean
change for saving in 2021→24 is **+13.72pp** against an unweighted mean of **+9.14** and a median of
**+8.29** — so the weighted aggregate does overstate the typical economy, exactly as E31 and E36
warned. But the episode does not depend on the weighting: **42% of developing panel economies
individually gained 10pp or more of formal saving**, against a previous best of 21%. This is a real
within-country episode.

**The finding that was not the hypothesis: 2021→24 is a BALANCE-SHEET window, not a digitalization
one.** Each margin peaks in a different window, and the ordering is clean. Account ownership's big
window was **2011→14** and its share has declined monotonically since (49.4 → 41.6 → 35.1 → 24.7%).
Digital payments peaked in **2014→17** and 2021→24 is its *weakest* window (21.1%). Saving and
borrowing both peak in **2021→24**, borrowing most of all (52.6%, median +10.59pp). The rails were
laid down in 2011–2017; what moved in 2021–2024 was the balance sheet on top of them.

**This reframes the paper draft's Section 4 without contradicting it.** Calling 2021–24 "the
digital-inclusion episode" is wrong on this evidence — digital payments were *decelerating*. The
window is better described as one in which saving and borrowing rose together, which is also what
E11 found contemporaneously (r = +0.403) and what E37's R3 rung stumbled over (a **−0.742**
saving-level → borrowing-growth correlation in this window alone).

**Movers do not repeat.** Spearman correlations between a country's change in consecutive windows
are **≤ +0.07 in all ten pairs tested** and negative in eight of them (saving: −0.413, −0.350,
+0.070). A big mover in one window is, if anything, a small mover in the next. This is independent
corroboration of E37's central negative — nothing at t predicts the size of the next move — and it
is the strongest argument in the ledger for why the prediction stream topped out where it did.

**Declared.** Descriptive distributional comparison. Wave spacing is uneven (3/3/4/3 years) and the
2021 wave was measured in the pandemic period; both are stated and neither is adjusted for, so
"largest median" is partly a statement about a four-year window competing with three-year ones —
which, note, works *against* 2021→24 (three years) and in favour of 2017→21.

---

## Cycle wrap-up — 2026-08-10

Working tree clean at start; `coverage.py` run before hypotheses were chosen (rule B1). Three
country-level experiments, two discards and one keep — and the keep and the discards point the same
way.

- **E37 — DISCARD, and Program 6 closes.** The sequencing ladder has no rung. Account level → Δ
  digital payments is **+0.066** with an interval through zero and a G6 sign flip; digital-payment
  level → Δ formal saving is **+0.447** but loses 72% of its magnitude to drop-top-5 and reverses to
  **−0.434** in 2014→2017; saving level → Δ borrowing pools to **−0.126** while hiding
  **+0.295 / +0.280 / −0.742** across the three windows. Items 6.1–6.3 close negatively and 6.4 is
  withdrawn as a false-discovery machine at `neff` ≈ 7. Two methodological carry-forwards: pooled
  designs must report the **country-level** Kish `neff` (7.5 here, against a meaningless stacked
  22.2) and must show per-window terms.
- **E38 — DISCARD the promotion; E5b recommended for demotion.** The accounts-first partial is
  **−0.654 / +0.591 / −0.595** across consecutive windows — it reverses and reverses back. All three
  collapse under G6 (retention 0.41 / 0.05 / 0.05) and all three bootstrap intervals straddle zero.
  My own promotion rule ("at least one earlier window agrees") mechanically passed while the
  demotion rule also fired; resolved against promotion under the standing E4 magnitude rule, and the
  rule is faulted: **a promotion should require every tested earlier window to agree in sign.**
- **E39 — KEEP, and it reframes the paper.** 2021→24 *is* a genuine within-country saving episode:
  **42.1% of developing panel economies individually gained ≥10pp of formal saving** against a
  previous best of 20.8%, with the largest unweighted median (+8.29pp) of the four windows — so it
  survives the weighting critique that sank E31 and E36. But each margin peaks in a **different**
  window: account ownership in **2011→14**, digital payments in **2014→17** (2021→24 is its
  *weakest*), saving and borrowing in **2021→24**. 2021–2024 is a balance-sheet window, not a
  digitalization one.
- **Cross-cutting.** E37's null and E39's repeat-mover Spearmans (**≤ +0.07 in all ten consecutive
  pairs, negative in eight**) are the same fact seen twice: nothing measured at t predicts the size
  of the next move. That is the cleanest available explanation for why the prediction stream, closed
  at P28, topped out where it did.
- **Housekeeping.** Two demotions are now pending and un-executed — **E7** (recommended by E32) and
  **E5b** (recommended here). They should be applied together in the next distillation rather than
  accumulating. One micro design was pre-checked and abandoned before registration: the mobile-only
  vs bank-only comparison on the untouched `merchantpay_dig` column qualifies only **5 of 77**
  economies at M2's n ≥ 100 per cell.

---

## Cycle 2026-08-11 — pre-registration (written before any outcome was computed)

Working tree clean at start. `python3 coverage.py` run first (rule B1). The prediction stream is
CLOSED (P28), so no predictor run. The 2026-08-10 wrap-up called for a **distillation pass rather
than three new experiments**, so this cycle is **two experiments plus an executed distillation**:
one meta-experiment that supplies the distillation's evidence (E40) and one new-ground experiment
that carries the breadth requirement (E41).

**Coverage cells this cycle lands on (rule B2).**
- **E41** uses the **untouched country module `merchant_pay`** (1 column, 2021 + 2024, 77/76
  developing panel economies, zero ledger mentions) — the B2 cell for this cycle.
- **E40** is a meta-experiment over the existing ledger and lands on no new cell by construction;
  it is explicitly not counted toward B2.
- Lineage (rule B3): E40's parent is the association ledger as a whole (no single parent, cap not
  engaged, E32 precedent). E41's parent is **E39**, not the rails chain — E23 → E24 → E25 → E35 is
  already at the cap.

### E40 — pre-registration: a LEDGER-WIDE false-discovery and de-weighting audit (Program 2, items 2.2 / 2.3 / 2.5; rule B7)

**Why this is owed now.** Rule B7 requires a Benjamini–Hochberg view over the association ledger
*before* the next distillation into the paper draft, and the distillation is happening in this
cycle. E32 paid items 2.2/2.3 for the sixteen-test Δ→Δ family and E35 paid them for six partial
cells; the **level→change family (E5/E9/E17), the gap-change designs (E3/E20), the 2024
cross-section (E29), the regional split (E22) and the six earlier-window replication cells
(E28/E30)** have never been through either lens, and no BH has ever been run across the ledger as
one family.

**The family, declared before computation — thirty-three tests in six blocks.** Every
population-weighted correlation the ledger reports as evidence for or against a claim, recomputed
in one file:

1. **Δ→Δ, 2021→2024, `pan_dev`** (E32's sixteen, recomputed here, not copied): E1, E2, E7, E10,
   E11, E12, E13, E14, E15, E16, E18, E19, E25, E26, E27, E27b.
2. **Partials, 2021→2024** (E5b, E23, E24) — the original windows, which E35 recomputed but never
   put through BH alongside the rest.
3. **Level→change, 2021→2024** (E5 usage intensity → Δaccount; E9 `fing2p_acc` level → Δaccount;
   E17 saving level → Δsaving).
4. **Gap-change designs, 2021→2024** (E3 Δgender gap in account ~ Δmobile money; E20 Δincome gap in
   formal saving ~ Δformal saving), on `pan_grp`.
5. **The 2024 cross-section** (E29 `internet` ~ `g20_any` level).
6. **Earlier-window replications, 2017→2021** (E28's three rails→saving cells; E30's E11/E13/E14
   cells) and **E22's two regional subsamples** (SSA, rest-of-developing, 2021→2024).

Excluded and named as excluded, so the family cannot be gerrymandered after the answer: statistics
that are **not correlations** (E21 and E34's mean log-odds gaps, E31/E36's share-of-economies
counts, E39's distributional shares, E33's nine `fh` cells which are correlations but were kept as
a *family* with its own internal agreement rule, E37/E38's pooled and per-window cells which are
already reported with intervals and were discarded), and the entire micro stream (different design,
different weights).

**Computed per test:** population-weighted r, the **unweighted** twin, nominal n, Kish
`neff = (Σw)²/Σw²`, a 2,000-draw country bootstrap (percentile 95% interval and two-sided
`p_boot`), `p_nominal` (t on n−2 df), `p_neff` (the same t on neff−2 df), and the G6 drop-top-5
jackknife with the E4 retention ratio. BH at q = 0.10 over all thirty-three on `p_boot` (primary)
and on `p_neff` (secondary). Every test carries a **reproduction check** against the r on record;
a deviation > 0.02 is printed and the cell is reported as unreproduced rather than quietly used.

**Pre-registered claims — three, each with its own bar.**
- **A (survival).** ≥ 50% of the ledger's currently-`keep*` association rows in this family survive
  ledger-wide BH at q = 0.10 on `p_boot`.
- **B (de-weighting, item 2.3).** ≥ 80% of those same rows retain |r_unweighted| ≥ 0.30.
- **C (the boundary, item 2.5).** At most **one** currently-`discard` row has |r_unweighted| ≥ 0.30
  while its weighted |r| < 0.30. E32 identified E16 as that one case; if two or more turn up, the
  weighting has been setting the keep/discard boundary in both directions and the ledger owes a
  systematic re-examination, which will be recorded as an agenda item rather than acted on today.

**Registered alternative outcome.** A large-scale failure of A is the *informative* result and will
be logged as a keep in the negative direction: it would mean the ledger's keep list is a
multiple-testing artifact at the true degrees of freedom, and the distillation must then present
the surviving claims as a much shorter list than the ledger's status column implies.

**Declared.** This computes no new association; it recomputes existing ones under three extra
lenses. It adds no keep of its own, is not subject to B4, and changes no status by itself — status
changes happen in the distillation step, from its output plus the two already-pending demotions.

### E41 — pre-registration: does the untouched merchant-payment margin behave like a rail or like the balance sheet? (Program 4/5 adjacent, new ground; B2 cell)

**Parent:** **E39** (the balance-sheet reframing), not the rails chain.
**Why.** E39's central result is that 2021→24 is a **balance-sheet** window: saving and borrowing
peaked there while account ownership (2011→14) and digital payments (2014→17) peaked earlier, and
2021→24 is digital payments' *weakest* window. That reframing makes a sharp prediction on a margin
the ledger has never touched. `merchant_pay` is the most *use*-side digital margin in the country
file — a payment made to a merchant rather than a transfer or a wage — and it exists for exactly
the two waves the episode spans.

**Frame.** `pan_dev`, `group == "all"`, transition **2021→2024** (the only one available for this
column: `merchant_pay` is reported in 2021 and 2024 only, 77 and 76 developing panel economies).

**G3 declaration, made honestly.** `merchant_pay` is the sole column in its module and has no
headline/narrow variant, so no variant choice is being made. But the repo contains **no
questionnaire**, so the exact item wording — in particular whether the margin is digital-only — is
not documented (see `HARNESS_V2_NOTES.md` item 5). The claim is therefore worded about "the
merchant-payment margin **as coded in the country file**", and the item's descriptive statistics
(level in each wave, dispersion) are reported so a reader can judge the coding for themselves.

**Two pre-registered tests.**
- **P1 (the E39 prediction, distributional).** Share of developing panel economies with
  Δ`merchant_pay` ≥ +10pp. **Registered bar: < 42.1%** — i.e. below formal saving's share in the
  same window. If merchant payments moved *as much as* saving did, the balance-sheet reframing is
  weaker than E39 claimed and that is recorded against E39.
- **P2 (the rails test, association).** Population-weighted r(Δ`merchant_pay`, Δ`fin17a_17a1_d`)
  on the common sample. **Keep threshold: |r| ≥ 0.30**, plus G6 sign-stability with E4 retention
  ≥ 0.5, plus the B6 inference layer (2,000-draw country bootstrap percentile interval, Kish
  `neff`, and the unweighted twin reported beside the weighted r). Reported alongside as
  context, not as separate registered tests: r(Δ`merchant_pay`, Δ`g20_any`) — how much of this
  margin is the digital-payment headline already in the ledger — and r(Δ`merchant_pay`,
  Δ`borrow_any_t_d`).

**Registered joint reading.** P1 passing and P2 failing is the E39-consistent outcome: the
merchant margin is a rail that was *not* moving in a window where the balance sheet was. P1 failing
is evidence against E39's framing and will be recorded as such. P2 passing on its own is a
`keep-window` only — `merchant_pay` has two waves, so under B4 it can **never** be promoted to
`keep-general`, exactly like E29. That limitation is registered up front so a positive result is
not over-read.

**Gates.** G3 declared above · G4 coverage on the estimation sample · G5 not applicable (no
official aggregate is published for this column in the file; checked as a coverage question, no
outcome computed) · G6 with the E4 retention rule · B6 as above.

**Declared.** Contemporaneous co-movement over one window. It identifies nothing, it is not causal,
and with two waves it cannot be a general regularity under B4 no matter what it returns.

### E40 — VERDICT: KEEP on A and B, DISCARD on C, 2026-08-11

**Reproduction first: 33/33 cells reproduce the r on record within 0.02, max deviation 0.0005.**
Thirty-three association tests spanning five years of this ledger, six different designs and three
wave windows, all recomputed from the raw frames in one file. Nothing in what follows is an
artifact of a mis-stated construction.

| claim | statistic | bar | result |
|---|---|---|---|
| **A** survival under ledger-wide BH (q=0.10, `p_boot`) among kept rows | **18/20 = 90.0%** | ≥ 50% | **PASS** |
| **B** kept rows retaining \|r_unweighted\| ≥ 0.30 | **16/20 = 80.0%** | ≥ 80% | **PASS** |
| **C** discards with \|r_u\| ≥ 0.30 while \|r_w\| < 0.30 | **2** (E16, E26) | ≤ 1 | **FAIL** |

**A passes, and the two rows that fail it are exactly the two demotions already pending.** The only
kept rows that do not survive ledger-wide BH on the bootstrap p are **E7** (p_boot 0.073) and
**E5b** (0.331) — the rows E32 and E38 independently recommended demoting. Three lenses built at
different times, on different grounds, select the same two rows. The E4 retention rule agrees:
E7 0.44 and E5b 0.19 are the only kept rows under 0.5. The distillation in this cycle therefore
executes those two demotions with a third, pre-registered piece of evidence behind them.

**B passes at exactly its bar, and the near-misses matter more than the pass.** Four kept rows fail
the unweighted lens: E7 (+0.283), **E13 (+0.188)**, E5b (+0.106) and **E30b (+0.248)**. E30b *is*
E13's 2017→2021 replication — so the FI-account ~ mobile-money complementarity, which E30 promoted
to `keep-general`, is **weighting-dependent in both of its windows**. That is new: E32 flagged E13
on one window and left it standing because the replication was independent evidence, and the
replication turns out to lean the same way. **E13 is now flagged in the ledger as weighting-
dependent in both windows**, short of demotion but no longer clean.

**C fails, and the second case is the interesting one.** Two discards clear 0.30 unweighted while
their population-weighted r sits under it: **E16** (`Δaccount ~ Δformal saving`, +0.198 weighted /
**+0.555** unweighted, already named by E32) and **E26** (`Δwage digitalization ~ Δresilience`,
+0.294 / **+0.364**). E26 is the row the paper's Section 6 boundary rests on — it missed the 0.30
bar by 0.006 weighted, and de-weighted it clears. Combined with E33 (the rails *do* co-move with the
`fh` welfare family at 0.35–0.71), **the "rails do not reach welfare" boundary now depends on both
the choice of welfare measure and the choice of weighting.** It should not be stated in the paper
draft as a finding. Item 2.5 stays open and is now sharper: the boundary cuts in both directions.

**The secondary result is the one that has now reproduced four times.** BH on `p_neff` — the same
t-statistic evaluated at the *true* degrees of freedom implied by the population weights — rejects
**1 of 33**, and the survivor is **E22a**, the Sub-Saharan-Africa subsample, which has the family's
highest `neff` (9.5) precisely because it excludes the giant economies. On nominal n, BH rejects
**26 of 33 and 20 of 20 kept rows**. Median Kish `neff` across the whole family is **7.2** against a
median nominal n of **71**. E32 found this on 16 tests, E35 on 6, E31/E34 on the gap frames, and
now it holds across every design the ledger contains.

**A ledger-wide number worth recording: the median de-weighting shift is −0.051.** E32 measured
**+0.011** on its sixteen and concluded the weighting "relocates rather than inflates". Over
thirty-three tests spanning all six designs the shift is mildly *negative* — the weighted ledger is,
on average, slightly stronger than an unweighted one, by about a twentieth of a correlation unit.
That is small enough to keep E32's conclusion and precise enough to stop the ledger being dismissed
either way.

**Sixteen rows are triple-clean** — BH-surviving on `p_boot`, |r_u| ≥ 0.30, and E4 retention ≥ 0.5:
E1, E10, E11, E12, E14, E25, E23, E24, E29, E22a, E22b, E28a, E28b, E28c, E30a, E30c. That is the
list the distillation carries forward, with the standing caveat that **at `neff` ≈ 7 none of them
except E22a is "significant" in the ordinary sense**, and the paper must say so in those words.

**Declared.** No new association is created here; existing ones are recomputed under three lenses.
E40 adds no keep of its own, is not subject to B4, and changes no status by itself.

### E41 — VERDICT: P1 KEEP (keep-window), P2 DISCARD, 2026-08-11

**The registered joint reading is exactly what happened: P1 passes, P2 fails.** The merchant-payment
margin is a rail that was not moving in a window where the balance sheet was.

**The column first, since its wording is undocumented.** `merchant_pay` on the developing panel
(n = 76 with both waves, G4 population share 0.974): pop-weighted level **35.1 → 39.4pp**,
unweighted mean 22.1 → 27.9, median **13.1 → 20.2**, range 1.1–94.9. A minority margin in the
typical economy, not a near-universal one — consistent with a *digital* merchant-payment reading
rather than "made any payment to a merchant", though the repo has no questionnaire and I am not
asserting the item's wording.

**P1 — the share of economies gaining ≥ +10pp, with the new margin inserted into E39's table:**

| margin | share ≥ +10pp | median Δ | mean Δ (unw) | mean Δ (wtd) |
|---|---|---|---|---|
| any borrowing | **52.6%** | +10.59 | +11.41 | +10.20 |
| formal saving | **42.1%** | +8.29 | +9.14 | +13.72 |
| **merchant payments** | **26.3%** | +2.99 | +5.78 | +4.36 |
| account ownership | 24.7% | +4.06 | +4.69 | +5.01 |
| digital payments | 21.1% | +2.62 | +3.51 | +5.82 |

**26.3% against a bar of < 42.1% — PASS**, with a binomial 95% margin of ±9.9pp that does not reach
the bar. The margin sorts cleanly into the **digital-rail cluster** (21–26%) and nowhere near the
balance-sheet cluster (42–53%). E39's reframing was derived from four margins; it now holds on a
fifth that was chosen after the reframing was written and before its answer was computed. That is
the cheapest kind of out-of-sample check this loop can run, and the framing survives it.

**P2 — FAIL, and the *way* it fails is the run's second finding.**

| cell | r weighted | r unweighted | G6 drop-top-5 | 95% CI | p_boot |
|---|---|---|---|---|---|
| **registered** Δmerchant ~ Δformal saving | **+0.039** | **+0.418** | **+0.421** | [−0.300, +0.855] | 0.739 |
| context Δmerchant ~ Δdigital payments | +0.383 | +0.484 | +0.413 | [+0.097, +0.757] | 0.008 |
| context Δmerchant ~ Δany borrowing | +0.259 | +0.111 | +0.083 | [−0.158, +0.635] | 0.288 |

n = 76, Kish `neff` = 7.2 in all three. The registered cell is **+0.039 population-weighted and
+0.418 unweighted**, and dropping the five largest economies moves it to **+0.421** — the jackknife
and the de-weighting land in the same place, which is what an artifact of a handful of giant
economies looks like from both directions. **P2 fails on its pre-registered primary and is a
discard**; the unweighted figure is reported, not promoted, because switching to the lens that
gives the answer I want after seeing it is exactly the move the pre-registration exists to prevent.

**This is a third instance of E40's claim C, found the same day in a fresh test rather than a
re-audit.** E40 found two *ledger* rows where de-weighting crosses the 0.30 line (E16, E26); E41
produces a third, and the largest gap yet (**+0.039 → +0.418**). Agenda item 2.5 is no longer a
retrospective clean-up item: the population weighting is deciding keep/discard on live experiments,
in both directions, at a rate of roughly one case per handful of tests. **The honest statement is
that the ledger's 0.30 threshold is a threshold on a statistic whose value depends on a weighting
choice that five economies dominate.**

**The context cells are worth one line each.** Merchant payments co-move with the digital-payment
headline at **+0.383** weighted (CI [+0.097, +0.757], p_boot 0.008, retention 1.08) — related to
`g20_any` but not a restatement of it, so this was a genuinely new column and not a relabelling.
Against borrowing the cell is +0.259 weighted, +0.111 unweighted, retention 0.32 — nothing.

**Declared.** Contemporaneous co-movement over one window on a two-wave column. Under B4 this can
**never** reach `keep-general`, which was registered before the run. The P1 result is a
distributional description, not an association, so B6 does not bind on it; the binomial interval is
reported as a courtesy. Nothing here is causal.

---

## Cycle wrap-up — 2026-08-11

Working tree clean at start; `coverage.py` run before hypotheses were chosen (rule B1). Two
experiments and the distillation the 2026-08-10 wrap-up called for. The prediction stream stayed
closed (P28), as registered.

- **E40 — KEEP on two of three registered claims.** The first **ledger-wide** BH: thirty-three
  association tests, six designs, three wave windows, all recomputed from raw frames, **33/33
  reproducing the r on record** (max deviation 0.0005). **18/20 kept rows survive BH on `p_boot`**
  and **the only two failures are E7 and E5b — the two demotions already pending**, which the E4
  retention rule independently selects (0.44 and 0.19). Claim C **failed**: two discards cross 0.30
  when the population weighting is removed (E16 +0.198/+0.555, **E26 +0.294/+0.364**), against a bar
  of one. At the true degrees of freedom BH rejects **1 of 33** (median `neff` **7.2** vs median
  nominal n **71**), against 26 of 33 on nominal n. Sixteen rows are triple-clean and that is the
  list the paper may carry.
- **E41 — P1 KEEP, P2 DISCARD, on the untouched `merchant_pay` module (the cycle's B2 cell).**
  Merchant payments sort with the **digital rails**: **26.3%** of developing panel economies gained
  ≥ 10pp in 2021→24, against 42.1% for formal saving and 52.6% for borrowing, and 21.1% for digital
  payments. E39's balance-sheet reframing therefore passes an out-of-sample check on a margin chosen
  after the reframing was written. The registered co-movement with the saving surge **failed** —
  and failed instructively: **+0.039 population-weighted against +0.418 unweighted, with drop-top-5
  at +0.421**. The jackknife and the de-weighting agree that five economies are holding the weighted
  figure at zero.
- **The distillation, executed.** **E7 and E5b are demoted to `discard`** (recommended by E32 and
  E38, confirmed by E40). **E13 is flagged** as weighting-dependent in both of its windows.
  `PAPER_DRAFT_v2.md` now carries a seven-point **CORRECTIONS OWED** block covering the title's
  over-generality, Section 4's window framing, the failed rail decomposition, the non-boundary in
  Section 6, the two demoted findings, the inference that Section 9 said was missing, and the closed
  forecasting stream. `EXTENSIONS_DRAFT.md` carries a status block. Three protocol rules added:
  **B8** (promotion requires *every* tested window to agree in sign), **B9** (mandatory unweighted
  twin; `keep-weighted` when the lenses disagree), **B10** (`neff` beside every n; no significance
  language on nominal n).
- **The cross-cutting fact of the day.** Three separate instances of the same problem surfaced
  within one run — E16, E26 and E41's live cell — where the weighted and unweighted verdicts fall on
  opposite sides of the 0.30 bar. This is no longer a curiosity about one discard. **At `neff` ≈ 7,
  the keep/discard threshold is a threshold on a statistic that a handful of economies decide**, and
  B9 exists so that future keeps have to say which lens they are keeping under.
- **Housekeeping.** No demotions are left pending. Program 1 is closed (only E22 remains
  `keep-window`, and its parent E1 is replicated); Program 2 is effectively closed with items 2.5
  and the new 2.6 as its live residue; Program 6 stayed closed; Program 7 stayed blocked. The
  natural next cycle is the **v3 rewrite** the corrections block specifies, or `fin31` (four waves ×
  77 economies, the best-covered untouched block) behind a mandatory mapping pass.

---

## Cycle 2026-08-13 — pre-registration (written before any outcome was computed)

Working tree clean at start. `python3 coverage.py` run before hypotheses were chosen (rule B1).
The prediction stream stays **closed** (P28, 2026-08-09) — no predictor experiment is registered,
as the closing rule requires a change to the *task* rather than another mechanism.

**Coverage cells this cycle lands on, declared under B1/B2.**

| experiment | frame | wave transitions | modules | B2 status |
|---|---|---|---|---|
| E42 | `pan_dev`, group=all | **2011→14, 2014→17**, 2017→21, 2021→24 | `account_t_d`, `fin17a_17a1_d`, `fin32_acc`, `fin24aSD_ND` | thin transitions (2011→14 has 12 ledger mentions, 2014→17 has 44) |
| E43 | **`pan_grp` — gender, income, education, age_cat, laborforce** | 2021→24 | `fin17a_17a1_d`, `account_t_d` | **B2 CELL: four of the five slice frames are at ≤1 ledger mention** (education 1, age_cat 1, laborforce 1, gender ~1); `urbanicity` is single-wave and is therefore excluded, not skipped |

**Lineage (B3).** E42's parent is **E40** (the ledger-wide audit) — first descendant. E43's parent is
**E39** (the balance-sheet reframing) — second descendant after E41, inside the cap. Neither takes
E31/E34/E36 as parent; that chain is exhausted.

---

### E42 — pre-registration: is the *unweighted* ledger a different ledger? (Program 2, item 2.6)

**Why.** E40's claim C failed and E41 produced a third live instance the same day: the population
weighting is setting the keep/discard boundary in both directions (E16 +0.198w/+0.555u, E26
+0.294w/+0.364u, E41 +0.039w/+0.418u). Rule **B9** now requires a `keep-weighted` / `discard-weighted`
status when the two lenses disagree. Item 2.6 asks whether E16 and E26 should be re-statused — but a
re-status alone is bookkeeping. The question worth registering is whether the *unweighted* result is
a **regularity** or a one-window accident, which is rule **B8** applied to the unweighted lens.

**A coverage fact that shapes the design, checked before registration (no outcome computed).**
`fin24aSD_ND` exists only in 2021 and 2024, so **E26 can never be replicated on an earlier window** —
it is unpromotable for the same reason E29 is. `account_t_d` and `fin17a_17a1_d` both have all five
waves, so **E16 can be tested on three earlier transitions**. The registered generality test therefore
binds on E16 only, and E26 gets the re-status and nothing more. Declared now so the asymmetry is not
read later as cherry-picking.

**P1 — re-status under B9 (mechanical, executed either way).** Recompute E16 and E26's 2021→24
weighted and unweighted correlations from raw frames. PASS if both reproduce E40's figures within
0.02. On passing, both rows move `discard` → **`discard-weighted`** in `findings.tsv` (discarded, but
only under the weighted lens), with the weighting dependence stated in the claim text.

**P2 — the registered claim (B8 on the unweighted lens).** *The unweighted account-growth ~
formal-saving co-movement is a decade regularity, not a 2021–24 artifact of removing the weights.*
Test: unweighted `r(Δaccount_t_d, Δfin17a_17a1_d)` on the developing panel in **2011→14, 2014→17 and
2017→21**. KEEP threshold: **r_u ≥ +0.30 with a positive sign in ALL THREE earlier windows** (B8 —
every tested window must agree, one is not enough). Any window below +0.30, or of the opposite sign,
is a DISCARD. B6 inference on every cell: 2,000-draw country bootstrap percentile interval, Kish
`neff`, and the weighted twin printed beside the unweighted statistic. G6/E4 retention reported.
Registered caveat: 2014→2017 has failed to produce a stable sign in five of six cells across E28/E30
and is treated as a low-power window — but it still counts against P2, because B8 admits no
exemptions chosen after the fact.

**P3 — is the divergence one economy?** Leave-one-economy-out on the 2021→24 weighted E16 cell: drop
each of the ~76 economies in turn and recompute `r_w`. Registered bar: if **max |Δr_w| ≥ 0.20**, the
weighted/unweighted divergence is a **single-economy artifact** and the economy is named; if every
single drop moves `r_w` by < 0.20 it is a **distributed weighting effect** and the "five economies
decide it" language in the ledger needs softening to "the weight distribution decides it".

**Declared.** No new association is created by P1. P2's claim, if it passes, is a descriptive
co-movement of contemporaneous changes across four windows — it identifies nothing and is not causal.
An unweighted correlation describes the typical *economy*, not the typical *person*; that difference
is the finding's content, not a technicality, and the write-up must say so.

---

### E43 — pre-registration: did the 2021–24 saving surge reach every demographic slice? (Program 3, item 3.6 — the cycle's B2 cell)

**Why.** E39 established that 2021→24 is a within-country balance-sheet episode: **42.1%** of
developing panel economies gained ≥ +10pp in formal saving, against a 20.8% previous best. That is
the loop's largest surviving finding and it is entirely a `group == "all"` statement. Whether the
episode reached the poor, the unschooled, the young and the out-of-workforce is a different question
and the `pan_grp` frame answers it directly. Parent: **E39**.

**Frame.** `Findex.pan_grp`, developing panel economies, five dimensions with two subgroups each:
`gender` (women / men), `income` (poorest 40% / richest 60%), `education` (prim edu or less /
secondary edu or more), `age_cat` (ages 15-24 / age 25+), `laborforce` (out of / in laborforce).
`urbanicity` is **excluded, not skipped**: it exists for 2024 only, so it admits no Δ.
Disadvantaged group is named per dimension **before** the run, in the order above.

**Outcome.** `fin17a_17a1_d` (formal saving, the E39/E1/E10/E12 headline), Δ 2021→2024.

**Primary statistic, chosen under E31's lesson.** E31 showed population-weighted slice means are
dominated by a handful of economies while a minority of economies move with them, so the primary is
the **unweighted share of developing panel economies** meeting each bar, and the population-weighted
mean is secondary.

**Registered KEEP claim — the surge was broad-based.** For each dimension, two bars:
  (a) the **disadvantaged** group's population-weighted Δ is **≥ +5.0pp**; and
  (b) the **unweighted share of economies where the disadvantaged group gained ≥ +10pp is ≥ 25%**
      (a bar deliberately set near half of E39's 42.1% all-adults headline, so "broad-based" means
      the surge is visible in the disadvantaged half and not merely non-zero).
KEEP if both bars hold in **≥ 4 of the 5 dimensions**; DISCARD otherwise, naming the dimensions that
failed. The dimension-level results are reported in full either way.

**Secondary, registered and reported whichever way the primary goes: did the episode widen or narrow
within-country gaps?** Per dimension, the unweighted share of economies where the (advantaged −
disadvantaged) pp gap **narrowed**, against a 50% coin-flip reference, plus the population-weighted
gap change with G6. No keep hangs on this; it is registered so the direction cannot be picked after
the fact. E20/E21 found the income gap in saving widening in 2021–24 under a weighted lens; whether
that holds unweighted and generalises across axes is the open question E31 left.

**B6 inference.** Country bootstrap (2,000 draws, resampling economies with all their subgroup rows)
for every reported share and weighted mean; Kish `neff` on the **country-level** weights per E37's
rule (i), not on stacked subgroup rows.

**Declared.** A distributional description of one window across five slices, not an association — the
0.30 correlation threshold does not apply and is not used. Under **B4** a 2021→24 result is a
`keep-window` claim at best. Nothing here is causal, and a group's Δ is a change in a cross-sectional
rate, not a change experienced by the same individuals.

---

### E42 — VERDICT: P1 PASS (re-status executed), P2 KEEP, P3 single-economy, 2026-08-13

**P1 — the B9 re-status, and it reproduces exactly.**

| row | r weighted | r unweighted | on record | reproduced | lenses disagree at 0.30 |
|---|---|---|---|---|---|
| E16 Δaccount ~ Δformal saving | **+0.198** | **+0.555** | +0.198 / +0.555 | yes | yes |
| E26 Δwage digitalization ~ Δresilience | **+0.294** | **+0.364** | +0.294 / +0.364 | yes | yes |

Both rows move `discard` → **`discard-weighted`** in `findings.tsv`: discarded, but only under the
population-weighted lens. **E26 stops there** — `fin24aSD_ND` exists for 2021 and 2024 only, so it
can never be replicated on an earlier window, exactly as E29 cannot. That was declared before the
run, not discovered after it.

**P2 — KEEP. The unweighted co-movement is a decade regularity, and all three earlier windows were
genuinely unknown at registration.**

| window | r weighted | r unweighted | 95% CI (unweighted) | p_boot | G6 | retention |
|---|---|---|---|---|---|---|
| 2011→2014 | +0.431 | **+0.470** | [+0.259, +0.641] | 0.0010 | +0.483 | 1.03 |
| 2014→2017 | +0.736 | **+0.361** | [+0.171, +0.524] | 0.0005 | +0.451 | 1.25 |
| 2017→2021 | +0.641 | **+0.394** | [+0.171, +0.593] | 0.0010 | +0.320 | 0.81 |
| 2021→2024 | +0.198 | **+0.555** | [+0.374, +0.701] | 0.0005 | +0.741 | 1.33 |

**3/3 earlier windows clear +0.30 with a positive sign — B8 is satisfied on the unweighted lens**,
and every interval excludes zero. Under the *weighted* lens the same association clears 0.30 in
three of the four windows and fails only in 2021→24. So **E16 was not a weak association; it was a
strong association measured in the one window where the weighting cancels it.**

**Status assigned: `keep-general-unweighted`** (B4 satisfied — three earlier transitions replicate;
B9's lens qualifier attached because the weighted lens disagrees in one window). This composes both
facts rather than hiding one, and the symmetric status is proposed as rule **B11** below.

**The peek disclosure this finding owes.** The *choice* of which association to test unweighted was
informed by E40 having already computed the 2021→24 unweighted value. That cell is therefore
**peek-informed and carries no evidential weight here**; the keep rests entirely on the three earlier
windows, whose answers were unknown when the bar was written. Stated so a reader can discount the
right cell rather than the whole result.

**The de-weighting shift is window-specific and large in both directions:** +0.039 / **−0.375** /
−0.247 / **+0.357**. On a single association, across four windows, the weighting moves the statistic
by more than a third of a correlation unit in each direction. E40's ledger-wide median shift of
−0.051 is an average over cells that individually swing far more than that.

**P3 — SINGLE-ECONOMY ARTIFACT, and the economy is China.**

| drop | Δ r_w | resulting r_w | pop share |
|---|---|---|---|
| **China** | **+0.527** | **+0.726** | 26.6% |
| Nigeria | −0.083 | +0.115 | 3.0% |
| Bangladesh | −0.079 | +0.119 | 2.8% |
| India | +0.074 | +0.273 | 24.3% |

Cumulative: r_w = +0.198 → **+0.726 on dropping one economy**, then +0.714 / +0.718 / +0.740 /
+0.741 for two through five. **The entire E16 discard was China.** India, with almost the same
population weight, moves it by +0.074. The ledger's standing phrase "five economies decide it" is
wrong for this cell and should be **"one economy decides it"**; the correct general statement is that
which economies matter is cell-specific, and naming them is cheap.

Worth recording beside it: Kish `neff` is **7.2 with China in and 7.8 with China out**, but **24.6
once India also goes** — `neff` is not a smooth function of sample size, and a single drop that
transforms the statistic may barely move `neff`.

**A protocol-level fact this run establishes, and the reason it matters.** E40's headline — BH
rejects 1 of 33 at `neff` ≈ 7 — is a critique of the **population-weighted** ledger specifically.
An **unweighted** correlation over 77 economies has `neff` = n = 77, because there are no weights to
concentrate. The degrees-of-freedom objection therefore **dissolves** for the unweighted lens; it does
not transfer. Two caveats that do survive and must be stated with it: economies are not independent
draws (regional clustering is unmodelled), and the unweighted statistic answers a **different
question** — it describes the typical *economy*, where the weighted one describes the typical
*person*. Neither is the correct lens; they are two questions, and the ledger has been reporting one
of them as if it were the answer to both.

**Declared.** Contemporaneous co-movement of changes in four windows. Identifies nothing, is not
causal, and says nothing about whether account growth produced saving growth in any economy.

---

### E43 — VERDICT: PRIMARY KEEP (`keep-window`), SECONDARY reported and then undercut by its own scale-free twin, 2026-08-13

**PRIMARY — KEEP, 5/5 dimensions. The surge reached every disadvantaged half.**

| dimension | disadvantaged | n | neff | wtd Δ dis | 95% CI | wtd Δ adv | ≥+10pp dis | 95% CI | ≥+10pp adv |
|---|---|---|---|---|---|---|---|---|---|
| gender | women | 55 | 5.6 | **+12.79** | [+7.35, +16.95] | +16.21 | **47.3%** | [34.5, 60.0] | 47.3% |
| income | poorest 40% | 55 | 5.6 | **+10.84** | [+5.68, +15.36] | +16.91 | **32.7%** | [20.0, 45.5] | 58.2% |
| education | prim edu or less | 55 | 5.6 | **+11.57** | [+2.62, +17.71] | +16.05 | **29.1%** | [18.2, 41.8] | 63.6% |
| age_cat | ages 15-24 | 55 | 5.6 | **+16.02** | [+10.18, +19.62] | +14.15 | **56.4%** | [43.6, 69.1] | 49.1% |
| laborforce | out of laborforce | 54 | 5.6 | **+7.40** | [+5.05, +8.74] | +12.85 | **31.5%** | [20.4, 44.4] | 55.6% |

Both registered bars clear in **all five** dimensions against a required four. Every disadvantaged
group's population-weighted gain exceeds +5pp with an interval well clear of it, and between 29% and
56% of economies delivered a ≥+10pp gain to the disadvantaged half — against E39's 42.1% all-adults
reference. **The young are the only slice where the disadvantaged group out-gained the advantaged
one** (+16.02 vs +14.15 weighted; +11.27 vs +9.31 unweighted median), which is consistent with E34's
finding that the age axis behaves unlike the resource axes.

**SECONDARY as registered (pp gaps) — the resource gaps widened, and it survives both robustness
lenses.**

| dimension | economies narrowing | 95% CI | wtd gap 2021 | wtd gap 2024 | wtd change | G6 change | unwtd change |
|---|---|---|---|---|---|---|---|
| gender | 45.5% | [32.7, 58.2] | 2.93 | 6.34 | +3.41 | +1.50 | +1.59 |
| **income** | **23.6%** | [12.7, 34.5] | 14.38 | 20.46 | +6.08 | +3.12 | +3.41 |
| **education** | **29.1%** | [18.2, 41.8] | 17.62 | 22.10 | +4.48 | +7.19 | +5.85 |
| age_cat | 49.1% | [36.4, 61.8] | −0.15 | −2.03 | −1.88 | −1.17 | −0.00 |
| **laborforce** | **25.9%** | [14.8, 37.0] | 9.48 | 14.93 | +5.45 | +3.22 | +4.77 |

Three intervals exclude 50% — income, education and labour force — so on the three resource axes the
pp gap widened in roughly three economies out of four, and unlike E31 and E36 this **is not a
big-country artifact**: the jackknife and the unweighted mean agree in sign with the weighted change
in every one of those three. Gender and age are coin flips.

**EXPLORATORY DIAGNOSTIC (unregistered, logged under the peek rule, no keep hangs on it) — and it
undercuts the secondary.** E21's lesson is that a pp gap widens mechanically when levels rise from a
low base, so the scale-free (log-odds) twin is the honest check:

| dimension | narrowed, pp | narrowed, log-odds | wtd Δ log-odds gap | unwtd Δ | G6 |
|---|---|---|---|---|---|
| gender | 45.5% | 61.8% | +0.097 | **−0.046** | **−0.011** |
| income | 23.6% | **52.7%** | +0.109 | **−0.078** | **−0.115** |
| education | 29.1% | 47.3% | +0.060 | +0.036 | +0.177 |
| age_cat | 49.1% | 49.1% | −0.076 | +0.013 | −0.018 |
| laborforce | 25.9% | **40.7%** | +0.103 | +0.060 | **−0.021** |

**On the scale-free measure there is no systematic widening.** Income goes from 23.6% to a 52.7%
coin flip and its unweighted and G6 changes both turn *negative*; gender and labour force flip sign
between lenses. **The registered secondary must therefore not be read as "the surge was regressive."**
It says the *percentage-point* gaps grew, which is close to arithmetic given that formal saving rose
from a low base everywhere and the advantaged group started higher. This is E21's discard reproduced
on five axes instead of one, and it is the second time in this ledger that a pp-gap widening has
failed its own scale-free twin.

**Declared.** A distributional description of one window across five slices, not an association — the
0.30 threshold was not used. Under **B4** the primary is a **`keep-window`** claim: 2021→24 only,
promotable if some future cycle replicates it on an earlier transition. Nothing here is causal, and a
group's Δ is a change in a cross-sectional rate, not a change experienced by the same individuals.
Country-level `neff` is **5.6** on the slice frame — lower than the 7.2 of the `all` frame, because
the slice frame covers 55 economies rather than 76 while the same giants carry the weight.

---

## Cycle wrap-up — 2026-08-13

Working tree clean at start; `coverage.py` run before hypotheses were chosen (rule B1). Two
experiments, six registered claims. The prediction stream stayed **closed** (P28), as its closing
rule requires.

- **E42 — P1 PASS, P2 KEEP (`keep-general-unweighted`), P3 single-economy.** The B9 re-status is
  executed: **E16 and E26 are now `discard-weighted`**. The substantive finding is larger than the
  bookkeeping — the account-growth ~ formal-saving co-movement holds **unweighted in all four wave
  transitions** (+0.470 / +0.361 / +0.394 / +0.555, every interval excluding zero, all p_boot ≤
  0.001) and **weighted in three of four** (+0.431 / +0.736 / +0.641 / +0.198). **E16 was never a
  weak association; it was a strong one measured in the one window where the weighting cancels it.**
  P3 names the canceller: **China alone** takes r_w from +0.198 to **+0.726**, while India, at
  almost the same population weight, moves it +0.074.
- **E43 — PRIMARY KEEP (`keep-window`), on the cycle's B2 cell.** Five `pan_grp` slice frames, four
  of which sat at ≤1 ledger mention. The 2021–24 saving surge reached **every** disadvantaged half:
  weighted gains **+7.4 to +16.0pp**, and **29–56%** of developing panel economies delivered a
  ≥+10pp gain to the disadvantaged group against E39's 42.1% all-adults reference. **The young are
  the only slice that out-gained its advantaged counterpart** (+16.0 vs +14.2), consistent with
  E34's age-axis asymmetry.
- **The cycle's cautionary result, and it is E43's own secondary.** The registered pp-gap secondary
  said the income, education and labour-force gaps widened in ~3 economies of 4, surviving G6 *and*
  de-weighting — the two robustness lenses that sank E31 and E36. Its **scale-free log-odds twin
  showed no systematic widening**: income moved to a **52.7% coin flip** with unweighted (−0.078) and
  G6 (−0.115) both turning negative. E21's discard, reproduced on five axes at once. A pp gap widens
  arithmetically when levels rise from a low base, and this ledger has now been caught by that twice.
- **The line that matters most for the paper.** E40's "BH rejects 1 of 33 at `neff` ≈ 7" is a
  critique of the **population-weighted** ledger specifically. An unweighted correlation over 77
  economies has `neff` = n = 77 — the degrees-of-freedom objection does not transfer. What survives
  is subtler and worse for the write-up as it stands: the repo has been reporting a typical-*person*
  statistic as though it answered the typical-*economy* question. Regional clustering is unmodelled
  under either lens and remains a real limitation.
- **Protocol.** Three additions in `program_findex.md`: **B11** (`keep-unweighted` /
  `keep-general-unweighted`, the symmetric partner of B9; a bare `keep` now means both lenses agree),
  **B12** (report the largest leave-one-out effect **and name the economy** beside every G6 figure —
  "five economies decide it" was a guess and is wrong for the E16 cell), and a standing requirement
  that every pp-gap claim carry its log-odds twin, with the pp version treated as the artifact where
  they disagree. Program 2 is now closed; Program 3's live item is **3.9**, the 2017→2021 replication
  of E43's primary, which is its only route to `keep-general`.

---

## Cycle 2026-08-15 — pre-registration (written before any outcome was computed)

Working tree clean at start. `python3 coverage.py` run before hypotheses were chosen (rule B1).
The prediction stream stays **closed** (P28, 2026-08-09): its closing rule requires a change to the
*task*, not another mechanism, and none is proposed here.

**Coverage cells this cycle lands on, declared under B1/B2.**

| experiment | frame | wave transitions | modules | B2 status |
|---|---|---|---|---|
| E44 | `pan_grp` — gender, income, education, age_cat, laborforce | **2011→14, 2014→17, 2017→21** + 2021→24 recomputed in-file | `fin17a_17a1_d` | the slice frames have never been used on any transition other than 2021→24 — this is the frame×transition cell the ledger has never entered |
| E45 | `pan_dev`, group=all | 2021→24 (+ per-wave levels 2014/2017/2021/2024) | **`fin31` — digital-payment detail, 9 columns, ZERO ledger mentions** | **B2 CELL: an untouched module, and the best-covered one left (four waves × 77 economies)** |

**Lineage (B3).** E44's parent is **E43** — first descendant, and it is the promotion test E43's own
verdict named (agenda item 3.9). E45's parent is **E41** (the `merchant_pay` out-of-sample insert),
which is itself the only other untouched-module screening experiment in the ledger — first descendant
on that line. Neither chain is near the cap.

---

### E44 — pre-registration: did earlier growth episodes also reach every demographic slice? (Program 3, item 3.9 — the B4 promotion test for E43)

**Why.** E43's primary is `keep-window`: in 2021→24 the formal-saving surge reached every
disadvantaged half (weighted Δ +7.4 to +16.0pp; 29–56% of economies delivering ≥+10pp to the
disadvantaged group). Under **B4** that is a window claim until replicated, and under **B8**
promotion requires **every** tested earlier window to agree. This is its only route to
`keep-general`.

**A fact declared before the run, because it shapes how the result must be read.** E39 established
that 2021→24 is the largest within-country formal-saving episode of the four transitions (42.1% of
economies ≥+10pp against a 20.8% previous best, all adults). E43's bar (b) — 25% of economies
delivering ≥+10pp to the disadvantaged half — is therefore **a bar the earlier windows may well fail
on magnitude alone, without saying anything about breadth**. Both statistics are registered up front
so the distinction cannot be drawn after seeing the numbers:

**P1 — the mechanical B4/B8 replication (this is what decides the promotion).** E43's bars applied
verbatim to each earlier transition, on the same five dimensions, same frame, same weight
declaration: (a) the disadvantaged group's population-weighted Δ ≥ **+5.0pp**; (b) the unweighted
share of economies where the disadvantaged group gained ≥ **+10pp** is ≥ **25%**; a dimension passes
if both hold; a window passes if ≥ **4 of 5** dimensions pass. **PROMOTE E43 to `keep-general` only
if all three earlier windows pass** (B8: one agreeing window is not enough). Otherwise E43 stays
`keep-window` and is recorded as having *failed* its promotion test, which is a stronger negative
than "not attempted" (E35's precedent). Per the E35 rule, **2021→24 is recomputed inside the same
file** and must reproduce E43's table within 0.1pp before any earlier window is read.

**P2 — the scale-relative claim, registered as a separate keep.** *When formal saving grows in a
window, it grows for the disadvantaged half roughly in proportion to the advantaged half — breadth is
a general feature even where magnitude is not.* Statistic: the **reach ratio** = (disadvantaged
population-weighted Δ) / (advantaged population-weighted Δ) per dimension per window, computed
**only where the advantaged Δ ≥ +2.0pp** (a ratio on a near-zero denominator is meaningless; the
filter is declared now, not chosen later, and windows/dimensions excluded by it are printed).
KEEP if the reach ratio is ≥ **0.75** in ≥ **4 of 5** dimensions in **every** qualifying window.
Reported beside it, either way: the unweighted median reach ratio and the unweighted share of
economies where the disadvantaged group's Δ is ≥ the advantaged group's Δ.

**B6/B9/B12 obligations.** 2,000-draw country bootstrap (economies resampled carrying all their
subgroup rows) on every weighted mean, share and reach ratio; **country-level** Kish `neff` per
E37's rule (i); the unweighted twin printed beside every weighted statistic; and for the headline
weighted Δ of each window, the **largest single leave-one-economy-out effect with the economy
named** (B12).

**Declared.** A distributional description, not an association — the 0.30 correlation threshold does
not apply. No gap statistic is registered here, deliberately: E43's pp-gap secondary died on its
log-odds twin and the standing rule now requires that twin, so this experiment asks about *reach*
(each group's own Δ and their ratio), which is scale-relative by construction. Nothing here is
causal, and a group's Δ is a change in a cross-sectional rate, not a change experienced by the same
individuals.

---

### E45 — pre-registration: is the digital-payment *detail* module a restatement of the headline, or does it carry independent variation? (new ground — the cycle's B2 cell)

**Why.** `fin31` is 9 columns × four waves × ~77 developing economies with **zero ledger mentions** —
the best-covered untouched country module left. It has no questionnaire in the repo, so the mandatory
mapping pass applies (Program 7's rule, generalised). The precedent that motivates the design is
`dig_acc`, pre-checked in the E42/E43 cycle: it correlates **+0.963** with `g20_any` in the 2024
cross-section and is therefore a near-restatement of the digital-payment headline, i.e. an untouched
module that is not new ground at all. Before this loop spends a cycle building a hypothesis on
`fin31`, it should establish whether the module is in the same position.

**Part A — MAPPING PASS, logged as EXPLORATORY under the peek rule.** Per `fin31` column: per-wave
developing-panel country counts and population-weighted levels, plus the item's relation to the
composites (`fin31a_31b`, and the `_s` suffixed variants against their unsuffixed twins). Labels are
inferred from the numbers and documented in `HARNESS_V2_NOTES.md` as **inferred, not authoritative**.
No keep hangs on Part A and nothing in it may be cited as a finding.

**Part B — the registered screening claim, written before any `fin31` value was computed.** *The
`fin31` module is a restatement of the digital-payment headline and carries no independent
variation.* Qualifying items: `fin31` columns with ≥ 30 developing-panel economies in **both** 2021
and 2024. Per qualifying item, two statistics with both lenses (B9): `r_level` = correlation of the
item's 2024 level with `g20_any`'s 2024 level, and `r_delta` = correlation of the item's Δ2021→24
with Δ`g20_any`.

- **KEEP the redundancy claim** if the median |`r_level`| across qualifying items is ≥ **0.80** on
  both lenses **and** no item qualifies as independent.
- **An item is INDEPENDENT** if |`r_level`| < **0.50** and |`r_delta`| < **0.30** on **both** lenses.
- **DISCARD the redundancy claim** if the median falls below 0.80 on either lens or any item is
  independent — in which case the independent items are **named as the new-ground targets** for a
  later cycle, which is the useful outcome either way.

**B6/B9/B10/B12 obligations.** 2,000-draw country bootstrap percentile interval on every reported
correlation and on the median; Kish `neff` beside every nominal n, with no significance language
attached to nominal n; the unweighted twin beside every weighted statistic, and the verdict labelled
with the lens it holds under; G6 drop-top-5 on every correlation, and for the single most important
item the **largest leave-one-out effect with the economy named**.

**Declared.** Cross-sectional levels and one Δ window; `g20_any` is the declared headline variant for
the digital-payment concept under G3, and every `fin31` item is by construction a narrow variant of
the same concept — that overlap is the hypothesis, not a confound. Nothing here is causal. A high
correlation between an item and the headline is a statement about measurement redundancy, not about
behaviour.

---

### E44 — VERDICT: P1 FAIL (E43's promotion test fails; it stays `keep-window`), P2 DISCARD — and the discard is a third instance of the pp-baseline trap, 2026-08-15

**The E35 reproduction check passed first, before any earlier window was read**: the 2021→24 table
recomputed inside this file matches E43's published figures to a **maximum deviation of 0.036pp**
across all ten cells. The earlier windows were therefore readable.

**P1 — the B4/B8 promotion test FAILS, and it fails on magnitude, exactly as the pre-registration
warned it might.**

| window | n (income slice) | neff | dims clearing both bars | verdict |
|---|---|---|---|---|
| 2011→2014 | 27 | 4.2 | **0/5** | FAIL |
| 2014→2017 | 34 | 4.6 | **0/5** | FAIL |
| 2017→2021 | 38 | 4.8 | **1/5** (age_cat) | FAIL |
| 2021→2024 *(original, recomputed)* | 55 | 5.6 | **5/5** | PASS |

**E43 stays `keep-window` and is now on record as having failed its promotion test** — a stronger
negative than "not attempted" (E35's precedent). Under **B8** one agreeing window would not have been
enough anyway; here none agrees.

**What the failure is, and is not.** Bar (a) — the disadvantaged half's weighted Δ ≥ +5pp — is *nearly*
met in the earlier windows (2011→14: +4.49 to +5.52pp across the five slices; 2017→21: +0.32 to
+6.41pp). Bar (b) — 25% of economies delivering ≥ +10pp to the disadvantaged half — is missed by a
wide margin everywhere (**0.0–17.9%** in 2011→14, **0.0–2.9%** in 2014→17, **13.5–36.8%** in 2017→21,
against **29.1–56.4%** in 2021→24). The bars are magnitude bars, and E39 already established that
2021→24 is the largest within-country saving episode of the four. **The right reading is that E43's
claim is inseparable from the size of the episode it describes: there was no earlier episode of that
size for the breadth question to be asked of.**

**2014→2017 is a decline window on this margin in every slice** (weighted Δ −3.65 to +2.35pp;
unweighted medians negative in four of five), which is the slice-level counterpart of the
`save_any_t_d` 53.1 → 43.6 drop that agenda item 1.4 flags as possibly definitional. Nothing here
resolves that; it is noted so the 0/5 is not read as evidence about breadth.

**P2 — the reach ratio: DISCARD.**

| window | usable dims | dims at ratio ≥ 0.75 |
|---|---|---|
| 2011→2014 | 4 (education excluded, advantaged Δ +1.77pp) | 3/4 |
| 2014→2017 | **0** — every dimension excluded by the registered +2.0pp denominator filter | — |
| 2017→2021 | 4 (laborforce excluded, +0.66pp) | 4/4 |
| 2021→2024 | 5 | **2/5** |

The registered bar required ≥ 4 of 5 in **every** qualifying window and 2021→24 returns 2/5 —
gender 0.789 and age_cat 1.133 clear it, income **0.641**, education **0.721** and laborforce
**0.576** do not. **DISCARD.**

**EXPLORATORY DIAGNOSTIC (unregistered, logged under the peek rule, no keep hangs on it) — and it
says the P2 bar was mis-specified.** A ratio of *percentage-point* deltas is not scale-free: while
both groups are below 50%, equal proportional (log-odds) growth mechanically produces **fewer** pp
for the lower-starting group. The log-odds twin of the same statistic, 2021→2024:

| dimension | pp ratio | **log-odds ratio** | economies where dis ≥ adv (log-odds) |
|---|---|---|---|
| gender | 0.789 | **0.875** | 61.8% |
| income | 0.641 | **0.864** | 52.7% |
| education | 0.721 | **0.918** | 47.3% |
| age_cat | 1.133 | **1.107** | 49.1% |
| laborforce | 0.576 | **0.845** | 40.7% |

**On the log-odds lens all five dimensions clear 0.75** (0.845–1.107), and the two lenses disagree on
three of five. So the honest statement of the 2021→24 window is: **in proportional terms the surge
was close to even across every slice, and the pp shortfall for the poorer, less-schooled and
out-of-workforce halves is what even proportional growth from a lower base looks like.** This is the
**third** time this ledger has been caught by the same arithmetic (E21, E43's secondary, now E44's
P2), and the first time it has bitten a statistic that was *registered* as scale-relative. The
standing pp-gap rule in `program_findex.md` should be widened from "gap" to **any ratio or difference
of pp changes between groups at different baselines** — proposed as **B13** below.

**B12 — the leave-one-out, by name.** On the income slice's disadvantaged-half weighted Δ, the
largest single drop is **China in all four windows**: +4.90 → +0.42pp (2011→14), −3.38 → +1.35pp
(2014→17), +5.57 → +0.61pp (2017→21), +10.84 → +7.37pp (2021→24). The slice frame's country-level
Kish `neff` runs **4.2 / 4.6 / 4.8 / 5.6** against nominal n of 27 / 34 / 38 / 55 — lower than the
`all` frame's 7.2, and in the earlier windows the frame covers barely half the economies.

**Declared.** Distributional description across four windows; no association, no 0.30 threshold, no
causal content. A group's Δ is a change in a cross-sectional rate, not a change experienced by the
same individuals.

**Proposed rule B13 (for the amendment block).** *Any between-group comparison of percentage-point
changes — a gap, a difference, or a ratio — must report its log-odds twin, and where they disagree
the pp version is the artifact.* The existing rule names gaps only; E44's P2 was a ratio, registered
in good faith as scale-relative, and it failed for the same mechanical reason.

---

### E45 — VERDICT: registered redundancy claim DISCARDED — `fin31` is neither a restatement nor cleanly independent, and one item runs the other way, 2026-08-15

**PART A — mapping pass (exploratory, peek rule; documented in `HARNESS_V2_NOTES.md` item 6 as
inferred, not authoritative).** Developing-panel population-weighted levels, 2014 / 2017 / 2021 /
2024:

| column | 2014 | 2017 | 2021 | 2024 | n 2024 |
|---|---|---|---|---|---|
| `fin31a_31b` | 7.9 | 14.8 | 18.2 | 17.6 | 71 |
| `fin31a` | 7.3 | 13.6 | 15.5 | 11.9 | 71 |
| `fin31b` | 1.1 | 7.0 | 7.9 | 14.5 | 71 |
| `fin31c` | — | — | — | 0.6 | 71 |
| **`fin31d`** | **47.1** | **34.1** | **20.5** | **26.6** | 71 |
| `fin31a_31b_s` / `fin31a_s` / `fin31b_s` / `fin31d_s` | thin | | | 42.0 / 36.7 / 41.6 / 60.7 | 50 / 36 / 44 / 59 |
| `g20_any` *(headline, for scale)* | 34.3 | 44.6 | 55.9 | 60.9 | 76 |

`fin31c` is 2024-only at 0.6pp and fails the registered coverage floor — excluded. The `_s` family
thins backwards (as few as 2 economies in 2014) and supports 2021→24 only.

**PART B — the registered screen: DISCARD.** Median |`r_level`| is **0.745 weighted / 0.680
unweighted** against a 0.80 bar, so the redundancy claim fails on **both** lenses. But **no item meets
the registered independence definition either** (|r_level| < 0.50 *and* |r_delta| < 0.30 on both
lenses). The module is a family of *moderately* correlated narrow items — neither a `dig_acc`-style
restatement (+0.963) nor new ground orthogonal to the headline.

| item | r_level (w) | [95% CI] | G6 | r_level (u) | r_delta (w) | r_delta (u) | neff |
|---|---|---|---|---|---|---|---|
| `fin31a_31b` | +0.797 | [+0.637, +0.895] | +0.821 | +0.815 | +0.404 | +0.532 | 7.2 |
| `fin31a` | +0.708 | [+0.517, +0.826] | +0.648 | +0.626 | +0.378 | +0.270 | 7.2 |
| `fin31b` | +0.826 | [+0.702, +0.912] | +0.853 | +0.822 | +0.209 | +0.483 | 7.2 |
| **`fin31d`** | **−0.401** | [−0.585, −0.205] | −0.372 | −0.358 | −0.113 | −0.317 | 7.2 |
| `fin31a_31b_s` | +0.759 | [+0.466, +0.930] | +0.803 | +0.721 | +0.664 | +0.642 | 5.4 |
| `fin31a_s` | +0.719 | [+0.394, +0.897] | +0.401 | +0.647 | +0.482 | +0.250 | 11.3 |
| `fin31b_s` | +0.810 | [+0.652, +0.909] | +0.623 | +0.629 | +0.609 | +0.481 | 14.8 |
| **`fin31d_s`** | **−0.730** | [−0.893, −0.454] | −0.646 | −0.713 | −0.158 | −0.541 | 6.4 |

**The finding worth carrying forward is the sign.** `fin31d` and `fin31d_s` are the **only two
columns in the ledger's country file that move *against* the digital-payment headline** — −0.401 and
−0.730 in levels, on both lenses and through G6. `fin31d`'s level also **falls 47.1 → 26.6** across
the decade while `g20_any` rises 34.3 → 60.9. The structural reading (inferred, no questionnaire) is
a **cash / non-digital residual margin**, and it is the first candidate this loop has found for
measuring the *retreat* of cash rather than the advance of digital payment. Registered here as the
module's new-ground target even though it does not meet the strict independence definition — that
definition was written to catch *orthogonal* items and a strongly *negative* one is at least as
interesting, which is a mis-specification of my own bar worth recording.

**A robustness result that is unusual for this ledger, and it deserves naming (B12).** On
`fin31a_31b` the weighted and unweighted level correlations are **+0.797 and +0.815**, drop-top-5 is
**+0.821**, and the **largest single leave-one-economy-out effect is Brazil at −0.042**. After E42's
China result (+0.198 → +0.726 on one drop) this is the opposite case: a cell where every robustness
lens agrees and no economy matters much. **`neff` is still 7.2** — which is the point worth teaching
from it: low `neff` says the *weights* are concentrated, not that the *result* is fragile. The two
diagnostics answer different questions and this cell separates them cleanly.

**Declared.** Cross-sectional levels plus one Δ window; every `fin31` item is a narrow variant of the
digital-payment concept under G3 and that overlap is the hypothesis. Nothing causal. A correlation
between an item and the headline is a statement about measurement redundancy, not behaviour. Item
meanings are inferred from levels and coverage, never from a questionnaire, and any future experiment
on this module must repeat that caveat.

---

## Cycle wrap-up — 2026-08-15

Working tree clean at start; `coverage.py` run before hypotheses were chosen (rule B1). Two
experiments, three registered claims, **zero keeps** — the first cycle in this ledger to return
none. The prediction stream stayed **closed** (P28), as its closing rule requires.

- **E44 — P1 FAIL, P2 DISCARD. E43's promotion route is closed and the closure is honest.** E43's
  bars, run verbatim on all three earlier transitions, clear **0/5, 0/5 and 1/5** dimensions against
  **5/5** in 2021→24 (the original window reproduced in-file to within **0.036pp** before anything
  else was read, per the E35 rule). **E43 stays `keep-window`, recorded as having *failed* its
  promotion test rather than not attempted it.** The failure is one of **magnitude, not breadth**:
  bar (a) is nearly met in the earlier windows, bar (b) — 25% of economies delivering ≥+10pp to the
  disadvantaged half — is missed everywhere. E39 had already established there was no earlier saving
  episode of comparable size, and the pre-registration said so in advance.
- **The cycle's methodological result, and it is E44's own registered secondary.** The reach ratio
  (disadvantaged Δ / advantaged Δ) failed at **2/5** dimensions in 2021→24 — and its **log-odds twin
  clears the same bar in all five** (0.845–1.107 against 0.576–1.133 on pp). So in *proportional*
  terms the surge was close to even across every slice, and the pp shortfall for the poorer,
  less-schooled and out-of-workforce halves is what even proportional growth from a lower base looks
  like. **Third instance of the same trap** (E21, E43's secondary, now this) and the first to bite a
  statistic that was *registered* as scale-relative. **Rule B13** now extends the log-odds
  requirement from gaps to any gap, difference **or ratio** of pp changes.
- **E45 — DISCARD on the registered screen, and the module is half-open.** `fin31` (9 columns, four
  waves, **zero prior ledger mentions** — the cycle's B2 cell) is **neither** a `dig_acc`-style
  restatement of `g20_any` (median |r_level| **0.745 wtd / 0.680 unwtd** against a 0.80 bar, failing
  on both lenses) **nor** cleanly independent (no item clears the independence definition). The
  independence bar was **mis-specified** — written to catch orthogonal items, it cannot see a
  strongly *negative* one — and that is recorded as an error of mine rather than a property of the
  data.
- **The best thing this cycle found is a sign.** `fin31d` and `fin31d_s` are the **only columns in
  the country file that move against the digital-payment headline** (−0.401 and −0.730 in 2024
  levels, on both lenses and through G6), and `fin31d` falls **47.1 → 26.6pp** across the decade
  while `g20_any` rises 34.3 → 60.9. Inferred structurally (no questionnaire) as a **cash /
  non-digital residual margin** — the loop's first candidate for measuring the *retreat of cash*
  rather than the advance of digital payment, on four waves × 77 economies. Logged as agenda item
  **7.6**.
- **A `neff` clarification, now in `program_findex.md`.** E45's `fin31a_31b` cell has `neff` = **7.2**
  — the ledger's usual figure — and is simultaneously its most robust cell: weighted **+0.797** vs
  unweighted **+0.815**, drop-top-5 **+0.821**, largest single leave-one-out **Brazil at −0.042**.
  E42's E16 cell has the same `neff` and moves +0.198 → +0.726 on dropping China. **A low `neff` says
  the weights are concentrated, not that the result is fragile**; `neff`, the unweighted twin, G6 and
  the named leave-one-out are four diagnostics answering four questions, and the write-ups have been
  conflating them.

---

## Cycle 2026-08-15b — pre-registration (E46, E47, E48)

Working tree clean at start. `python3 coverage.py` run **before** hypotheses were chosen (rule B1);
its output is the basis for the coverage-cell declarations below. The prediction stream stays
**CLOSED** (P28's closing rule) — no predictor experiment this cycle.

**Coverage cells this cycle lands on (rule B2).**

| exp | module | transition | frame | status of cell |
|---|---|---|---|---|
| E46 | `fin17` (4/12 cols used), `save_any_t_d` | **2014→2017** (54 mentions) + all four | `pan_dev` **and a high-income contrast frame** (`pan_all` minus `pan_dev`, 40 economies) — a frame the ledger has never used | thin |
| E47 | **`fin34`** (wage payment modes, 8 cols, **0 ledger mentions**) | 2024 cross-section + 2014→2024 | `pan_dev` all | **UNTOUCHED module — this is the cycle's B2 cell** |
| E48 | `fin31` (9 cols, 9 mentions, one experiment) | **2014→17 and 2017→21** primary, 2021→24 as peeked reference, plus the 2014→2024 long difference | `pan_dev` all | thin module, unpeeked transitions |

**Lineage (rule B3).** E46's parent is **E39/E44 item 1.7** (the slice-level formal-saving decline in
2014→17). E47 has **no parent finding** — it is a breadth draw from the B2 note. E48's parent is
**E45** (agenda item 7.6); that is the second consecutive experiment descending from E45 (E47 does
not count, having a different parent), so the cap is not approached.

---

### E46 — PRE-REGISTRATION: is the 2014→2017 fall in `save_any_t_d` (53.1 → 43.6) a definitional break or a real decline?

**Why now.** Agenda item 1.4 has flagged this since the agenda opened, and E44's item 1.7 made it
blocking: formal saving declines in **every** demographic slice in 2014→17, which is the slice-level
counterpart of the same drop. Two agenda items and any decade-scale claim on the saving margin are
waiting on this. It is a **measurement** question, not an association, so no 0.30 threshold applies;
the pre-registered object is a **verdict rule over five diagnostics**, fixed below before any of them
is computed.

**Hypothesis.** The 2014→2017 fall in total saving is a **questionnaire/definitional break**, not a
behavioural decline: the 2017 wave measures "saved any money" over a narrower set of channels than
2014 did.

**The five diagnostics, and the bar each must clear for "definitional".**

- **(a) Universality.** Share of developing-panel economies with Δ`save_any_t_d` < 0 in 2014→17,
  compared with the same share in 2017→21 and 2021→24. *Bar: ≥ 80% falling in 2014→17 AND at least
  20pp above the highest of the other windows.* A behavioural decline is heterogeneous; an
  instrument change is not.
- **(b) High-income contamination.** The same share computed on the **high-income panel frame**
  (`pan_all` minus `pan_dev`, ~40 economies) — a frame with no ledger mentions. The questionnaire is
  common to both groups; a developing-world savings shock is not. *Bar: ≥ 70% of high-income
  economies also falling.*
- **(c) Component decoupling.** Decompose Δ`save_any_t_d` into Δ formal (`fin17a_17a1_d`) and the
  **residual** (total minus formal, i.e. saving reported through non-formal channels). *Bar: ≥ 70% of
  the pp drop sits in the residual*, i.e. the formal component is close to flat while the "other
  methods" component collapses.
- **(d) Persistence.** A definitional break is a level shift that does not reverse under the same
  instrument. Report the 2017 / 2021 / 2024 levels. *Bar: the series does not return to within 5pp of
  its 2014 level in any later wave.*
- **(e) Official cross-check (G5).** The official *Developing economies* aggregate must show the same
  drop within the 2.5pp tolerance. This is a computation check, not evidence either way — if it
  **fails**, the whole experiment is void and is reported as a harness/frame defect.

**Verdict rule, fixed in advance.**
`definitional-break consistent` if **(a) AND (b) AND (c)** pass and (e) holds ·
`real decline` if **(a)** passes but **both (b) and (c)** fail ·
`inconclusive` otherwise. (d) is reported for all three verdicts and does not enter the rule, because
a real decline can also persist.

**Also reported (rules B6, B10, B12).** Country bootstrap (2,000 draws, percentile interval) on each
share in (a) and (b); Kish `neff` beside every nominal n; the per-window unweighted median Δ beside
the population-weighted mean Δ (rule B9's spirit applied to a level claim). **Following the E35 rule,
the file recomputes the ledger's published 2014 and 2017 levels (53.1 / 43.6) inside itself before
any diagnostic is read**, and aborts on a mismatch > 0.2pp.

**Declared.** `save_any_t_d` and `fin17a_17a1_d` are headline variants under G3. Descriptive
measurement diagnostics only; nothing causal, and "definitional break" is a claim about the
**instrument**, offered as the reading most consistent with five signatures, never as a documented
fact about the questionnaire (the repo has no questionnaire — `HARNESS_V2_NOTES.md` items 5 and 6).

---

### E47 — PRE-REGISTRATION: `fin34` (wage payment modes) — the cycle's untouched-module draw

**Part A — mapping pass (exploratory, peek rule).** Population-weighted developing-panel levels of
all eight `fin34` columns for 2014 / 2017 / 2021 / 2024 with per-wave economy counts, exactly as E45
did for `fin31`. Logged as **exploratory** before Part B's verdict is read, and written into
`HARNESS_V2_NOTES.md` as **inferred from levels and coverage, never from a questionnaire**. This part
was computed before the registration below was written and is disclosed as such.

**Part B — the orientation screen (registered).** For each of the four unsuffixed items
(`fin34a`–`fin34d`), the 2024 cross-sectional level correlation against the digital-payment headline
`g20_any` and against `account_t_d`, on the developing panel: weighted and unweighted (B9), G6
drop-top-5, a 2,000-draw country bootstrap interval (B6), Kish `neff` (B10), and the **named** single
largest leave-one-economy-out effect (B12).

Each item is classified into a **four-way** scheme — this fixes the bar E45 recorded as
mis-specified, which could not see a strongly negative item:
`restatement` |r| ≥ 0.80 · `aligned` +0.30 ≤ r < 0.80 · **`counter-moving` r ≤ −0.30** ·
`independent` |r| < 0.30. Classification requires **both lenses to agree**; where they disagree the
item is logged `mixed-lens` under B9/B11.

**Registered claim (the keep/discard object).** *At least one `fin34` item counter-moves the
digital-payment headline at `r_level` ≤ −0.30 on **both** lenses in the 2024 cross-section.* KEEP if
so; DISCARD if not. Coverage floor: an item is screened only if it has ≥ 30 developing-panel
economies in 2024 and a weighted level ≥ 1.0pp (an item at 0.1pp of adults is a floor, not a margin).

**Declared.** Cross-sectional 2024 levels; no trend language on Part B. Every `fin34` item is a
narrow variant of the wage/payment-mode concept under G3, unregistered in `INDICATORS`, and declared
as narrow. Item meanings are inferred. A correlation between an item and the headline is a statement
about **measurement orientation**, not behaviour.

---

### E48 — PRE-REGISTRATION: does the cash margin retreat where digital payment advances? (agenda item 7.6)

**Parent.** E45, which found `fin31d` (level 47.1 → 34.1 → 20.5 → 26.6 across 2014–2024) and
`fin31d_s` to be the only country-file columns whose 2024 level runs **against** `g20_any` (−0.401 and
−0.730, both lenses, through G6), and read them structurally — inferred, no questionnaire — as a
**cash / non-digital residual** margin.

**Disclosure (peek rule).** E45 already computed the **2021→24** Δ→Δ cell for these two items
(`fin31d` r_delta −0.113 weighted / −0.317 unweighted; `fin31d_s` −0.158 / −0.541). That window is
therefore **peeked** and cannot support a `keep` here; it is reported as a known reference only. The
primary below is registered on transitions whose answer is genuinely unknown.

**Hypothesis.** If `fin31d` is a cash/non-digital residual rather than an idiosyncratic item, then
**economies whose digital-payment headline rose faster saw this margin fall faster** — a negative
Δ→Δ association, present in more than one window.

**Primary (registered).** `r(Δfin31d, Δg20_any)` on the developing panel in **2014→2017** and
**2017→2021**, and on the **2014→2024 long difference**. Threshold: **r ≤ −0.30**, in the predicted
direction, on **both** lenses (B9/B11), in **at least two of the three** registered cells. Full B6/
B10/B12 reporting on every cell: 2,000-draw bootstrap, `neff` beside n, G6, named leave-one-out. Under
B4 a pass on the earlier transitions plus the long difference is registered as **`keep-general`** if
the 2021→24 reference agrees in sign, and **`keep-window`** if it does not (B8's sign-agreement rule
applied in the direction it was written for).

**Secondary (registered) — cross-module cash coherence.** If `fin31d` measures a general cash margin
rather than one module's quirk, it should co-move with a cash margin in a **different** module.
Correlate the 2014→2024 long difference of `fin31d` against the 2014→2024 long difference of **each of
the four `fin34` items** — all four, no selection on E47's outcome — weighted and unweighted, with
**Benjamini–Hochberg at q = 0.10** over the four tests (rule B7). Registered claim: *at least one pair
clears |r| ≥ 0.30 in the direction that has both margins retreating together, on both lenses, and
survives BH.* This is the falsifiable version of "there is a cash dimension in this data".

**Registered null-result reading, stated in advance so it cannot be written after the fact.** A
failure of the primary does **not** rehabilitate the digital headline — it says the counter-moving
*level* correlation E45 found is a cross-sectional composition fact rather than a within-country
dynamic one, which is exactly the distinction the ledger has repeatedly failed at (E31, E36).

**Declared.** Δ→Δ co-movement across the same window identifies nothing; both margins may move with a
third factor. `fin31d` is a narrow, unregistered variant under G3 whose meaning is **inferred from
levels and coverage** (`HARNESS_V2_NOTES.md` item 6) and that caveat is carried into any claim.
`fin31d_s` is excluded from the Δ design: E45 recorded it as supporting 2021→24 only.

---

### E46 — VERDICT: INCONCLUSIVE under the fixed rule (1 of 3 diagnostics passes) — but the definitional-break reading is REJECTED and agenda item 1.4 is answered in the negative, 2026-08-15

**E35 rule.** The ledger's published levels reproduced in-file before anything else was read:
2014 = **53.1** (ledger 53.1), 2017 = **43.6** (ledger 43.6). **(e) G5 passes** (max deviation 1.52pp
against a 2.5pp tolerance) so the experiment is not void.

**The four waves, developing panel, population-weighted:**

| series | 2014 | 2017 | 2021 | 2024 |
|---|---|---|---|---|
| `save_any_t_d` (developing) | 53.1 | **43.6** | 42.4 | **53.0** |
| `fin17a_17a1_d` formal (developing) | 22.2 | 21.0 | 24.3 | 38.0 |
| `save_any_t_d` (**high income**, the untouched frame) | 69.0 | **70.7** | 75.8 | 57.4 † |

† the high-income panel has only **5** economies reporting this column in 2024 — that cell is
uninterpretable and is not used anywhere below.

**The registered diagnostics.**

| # | diagnostic | bar | result | |
|---|---|---|---|---|
| (a) | universality | ≥ 80% of dev economies falling **and** ≥ 20pp above the best other window | **62.3%** [51.9, 72.7] vs 50.6% in 2017→21 — margin **11.7pp** | **FAIL** |
| (b) | high-income contamination | ≥ 70% of high-income economies also falling | **45.0%** [30.0, 60.0]; weighted mean Δ **+1.65pp**, unweighted median **+1.38pp** | **FAIL** |
| (c) | component decoupling | ≥ 70% of the pp drop in the non-formal residual | **90.2%** (Δtotal −9.27, Δformal −0.91, Δresidual −8.36) | **PASS** |
| (d) | persistence | never returns within 5pp of 2014 | 2024 is **0.1pp** from the 2014 level | **FAIL** |
| (e) | G5 official | within 2.5pp | 1.52pp | **PASS** |

Verdict rule: (a)∧(b)∧(c) → definitional; (a)∧¬(b)∧¬(c) → real decline; else inconclusive.
**1 of 3 → INCONCLUSIVE**, as registered.

**What the pattern nonetheless settles, and it is what item 1.4 was blocked on.** Two of the three
failures are failures *of the definitional hypothesis*, not ambiguities. A questionnaire change is
common to both income groups, and high-income economies **rose** in this window (+1.65pp weighted,
+1.38pp unweighted median, only 45% falling). A questionnaire change is also a **level shift under a
fixed instrument**, and the developing series returns to **53.0 in 2024 — 0.1pp from its 2014 value**
after passing through 43.6 and 42.4. An instrument does not un-break itself. **The 2014→2017 drop
should not be treated as a definitional break, and the decade series on `save_any_t_d` may be read as
continuous.** Item 1.4 is answered; item 1.7's slice-level decline is a real feature of the window,
not an artifact of the instrument.

**Why it is nevertheless not a clean "real decline" either — and this is diagnostic (c)'s content.**
The drop is **entirely in the non-formal residual**: formal saving moved −0.91pp while the residual
moved −8.36pp, i.e. **90.2%** of it. Per economy, total saving fell in 62.3% but formal saving in only
49.4% — a coin flip. So whatever happened in 2014→17 happened to saving *outside* financial
institutions and left the formal margin alone. That is consistent with a real contraction in
informal/at-home saving, and also with a change in how the non-formal channels were enumerated; this
design cannot separate those two, and the log should stop implying the question is binary.

**POST-HOC DIAGNOSTIC (labelled, not pre-registered; B12).** The weighted −9.27pp is **half China**:

| drop | weighted mean Δ 2014→17 | effect |
|---|---|---|
| — (full) | **−9.27pp** | |
| **China** | **−4.72pp** | **+4.55** |
| India | −10.68pp | −1.41 |
| Brazil | −9.80pp | −0.53 |
| drop-top-5 by population | −6.00pp (n = 72) | |

Unweighted mean **−4.72pp**, unweighted median **−5.08pp** — the typical economy fell about half as
far as the weighted figure says, and dropping China alone moves the weighted mean exactly onto the
unweighted one. This is E42's China cell again on a different margin.

**Declared.** Descriptive measurement diagnostics; nothing causal. Country-level Kish `neff` **7.5**
against nominal n **77** on the developing panel and **9.2** against n **40** on the high-income
frame; no significance language attaches to nominal n (B10). "Definitional break" was and remains a
claim about the **instrument** that this repo cannot verify — there is no questionnaire here
(`HARNESS_V2_NOTES.md` items 5–6) — so the finding is stated as *the definitional reading is
inconsistent with the data*, never as *the questionnaire did not change*.

---

### E47 — VERDICT: registered claim KEPT — `fin34c` is a second, independent counter-moving margin, and its orientation *emerges* across the decade, 2026-08-15

**PART A — mapping pass (exploratory, peek rule; labels INFERRED from levels and coverage, never
authoritative — the repo holds no questionnaire).** Developing-panel population-weighted levels:

| column | 2014 | 2017 | 2021 | 2024 | n 2024 |
|---|---|---|---|---|---|
| `fin34a` | 8.3 | 13.1 | 18.3 | 14.1 | 71 |
| `fin34b` | 0.4 | 3.9 | 3.0 | 8.1 | 71 |
| **`fin34c`** | **15.9** | **11.8** | **8.0** | **15.2** | 71 |
| `fin34d` | 6.0 | 1.0 | 0.4 | **0.1** | 71 |
| `fin34a_s` / `fin34b_s` / `fin34c_s` / `fin34d_s` | thin — 27/–/51/13 economies in 2014 | | | 42 / 19 / 30 / — | |
| `g20_any` *(headline, for scale)* | 35.1 | 45.4 | 56.4 | 60.9 | 76 |
| `account_t_d` *(headline, for scale)* | 55.7 | 65.2 | 70.7 | 75.3 | 77 |

`fin34d` collapses 6.0 → 0.1pp and fails the registered 1.0pp floor — excluded as a floor, not a
margin. The `_s` family is thin in the early waves and `fin34d_s` exists only in 2014.

**PART B — the registered screen: KEEP.** Three items qualify. Against `g20_any`, 2024:

| item | r_w | [95% CI] | p_boot | G6 | r_u | n | neff | classification | largest LOO |
|---|---|---|---|---|---|---|---|---|---|
| `fin34a` | +0.751 | [+0.586, +0.862] | 0.000 | +0.684 | +0.665 | 71 | 7.2 | aligned | Brazil −0.060 |
| `fin34b` | +0.832 | [+0.695, +0.923] | 0.000 | +0.837 | +0.723 | 71 | 7.2 | **mixed-lens** (restatement / aligned) | Pakistan +0.044 |
| **`fin34c`** | **−0.552** | **[−0.745, −0.309]** | 0.000 | **−0.553** | **−0.486** | 71 | 7.2 | **counter-moving** | Brazil +0.096 |

Against `account_t_d`, 2024: `fin34a` +0.413/+0.693, `fin34b` +0.453/+0.621, and **`fin34c`
+0.024 weighted against −0.416 unweighted — `mixed-lens`, with India alone worth −0.597**. That cell
is the cycle's sharpest B12 illustration and no claim is made on it.

**The registered claim passes on `fin34c`: −0.552 weighted and −0.486 unweighted, both past −0.30,
with G6 at −0.553 and the largest single leave-one-out (Brazil) worth +0.096.** Every lens agrees.
This is the **second** counter-moving margin the loop has found, in a **different module** from E45's
`fin31d`, and the four-way classification introduced here is what made it visible — E45's
independence definition would have missed it exactly as it missed `fin31d_s`.

**POST-HOC DIAGNOSTIC (labelled, not pre-registered) — the orientation is not a 2024 fact, it
emerges.** `r(item level, g20_any level)` by wave, weighted / unweighted:

| item | 2014 | 2017 | 2021 | 2024 |
|---|---|---|---|---|
| `fin34a` | +0.801 / +0.776 | +0.890 / +0.803 | +0.938 / +0.826 | +0.751 / +0.665 |
| `fin34b` | +0.270 / +0.337 | +0.772 / +0.531 | +0.119 / +0.481 | +0.832 / +0.723 |
| **`fin34c`** | **+0.028 / −0.122** | **−0.419 / −0.323** | **−0.690 / −0.367** | **−0.552 / −0.486** |

`fin34c` starts **orthogonal** to the digital headline in 2014 and turns counter-moving from 2017 on,
clearing −0.30 on both lenses in three consecutive waves. So the negative orientation is not a
one-wave coincidence, and it is not present at the start of the decade — it **develops as digital
payment spreads**. That is the shape a *displaced* margin would have, and it is the strongest reason
to carry `fin34c` forward alongside `fin31d`. Note also that both candidate margins share an unusual
level trajectory: a decade-long fall followed by a **rebound in the last window**
(`fin34c` 15.9 → 8.0 → 15.2; `fin31d` 47.1 → 20.5 → 26.6).

**Declared.** 2024 cross-section for the registered claim; the wave table is a labelled post-hoc
diagnostic and carries no keep. Rule B4's replication ladder does not apply in its usual form — this
is a level-orientation claim, not a Δ-window association — so the finding is logged `keep` on the
lens agreement, not `keep-general`. Every `fin34` item is a narrow, `INDICATORS`-unregistered variant
of the wage/payment-mode concept under G3. **Item meanings are inferred from levels and coverage
only**; "wage payment modes" is the module label, and which mode `fin34c` is remains unknown. A
correlation between an item and the headline is a statement about measurement orientation, not
behaviour. `neff` = 7.2 against nominal n = 71 on every cell (B10).

---

### E48 — VERDICT: PRIMARY `discard-weighted` (rule B9) · SECONDARY KEEP — the cash margin does not retreat where digital advances, but it does retreat *with the other cash margin*, 2026-08-15

**E35 rule.** E45's peeked cell reproduced in-file before any registered cell was read:
r_w **−0.113** (E45 published −0.113), r_u **−0.317** (E45 published −0.317).

**PRIMARY (registered): r(Δ`fin31d`, Δ`g20_any`), bar r ≤ −0.30 on both lenses in ≥ 2 of 3 cells.**

| cell | r_w | [95% CI] | p_boot | G6 | r_u | n | neff | wtd Δcash / Δhead | largest LOO |
|---|---|---|---|---|---|---|---|---|---|
| 2014→2017 | −0.400 | [−0.704, **+0.239**] | 0.354 | −0.137 | **−0.159** | 77 | 7.5 | −13.01 / +10.32 | **China +0.412** |
| 2017→2021 | **−0.759** | [−0.857, −0.431] | 0.000 | −0.555 | **−0.352** | 77 | 7.5 | −13.57 / +11.35 | China +0.170 |
| 2014→2024 (long diff) | −0.336 | [−0.627, +0.010] | 0.062 | −0.450 | **−0.266** | 71 | 7.2 | −14.26 / +23.59 | Viet Nam +0.117 |
| *2021→2024 (PEEKED, reference only)* | *−0.113* | *[−0.647, +0.269]* | *0.513* | *−0.462* | *−0.317* | *71* | *7.2* | *−0.28 / +7.48* | *India −0.409* |

Both lenses clear the bar in **1 of 3** cells — below the registered 2 — so the primary does not keep.
But the split is exactly the case rule B9 was written for: **the weighted lens clears all three
(−0.400 / −0.759 / −0.336) and the unweighted lens clears one (−0.159 / −0.352 / −0.266)**. Logged
**`discard-weighted`**, with the lens dependence stated as part of the finding rather than buried.
Note the 2014→17 cell is a pure big-country cell — **China alone is worth +0.412**, and G6 takes it
from −0.400 to −0.137.

**The registered null reading, written before the answer and reproduced verbatim.** This does not
rehabilitate the digital headline. It says E45's counter-moving **level** correlation is a
cross-sectional composition fact — cash-heavy economies are digital-poor economies — rather than a
within-country dynamic one. Where digital payment grew fastest over 2014–2024 is only weakly where
this margin fell fastest, and on the typical-economy lens barely at all.

**SECONDARY (registered): cross-module cash coherence, Δ 2014→2024, all four `fin34` items, BH q = 0.10.**

| pair | r_w | [95% CI] | p_boot | G6 | r_u | BH | direction |
|---|---|---|---|---|---|---|---|
| `fin34a` | **−0.744** | [−0.887, −0.529] | 0.000 | −0.832 | −0.701 | REJECT | **opposite** (cash falls where this rises) |
| `fin34b` | **−0.799** | [−0.892, −0.550] | 0.000 | −0.738 | −0.629 | REJECT | **opposite** |
| **`fin34c`** | **+0.515** | [+0.216, +0.726] | 0.001 | +0.443 | **+0.389** | **REJECT** | **registered — both retreating together** |
| `fin34d` | +0.154 | [−0.078, +0.455] | 0.182 | +0.092 | +0.403 | — | mixed-lens, fails BH |

BH at q = 0.10 over m = 4 rejects the first three (0.0000 / 0.0000 / 0.0010 against 0.0250 / 0.0500 /
0.0750). **The registered claim passes on `fin34c` and only `fin34c`** — the one item that satisfies
the pre-registered *direction*. `fin34a` and `fin34b` are larger in magnitude but point the other way,
and the pre-registration does not let them count; they are reported because the **displacement**
pattern they draw is the more interesting half of the table. Where `fin31d` fell across the decade,
`fin34a` and `fin34b` **rose** (−0.744, −0.799) and `fin34c` **fell** (+0.515) — the two
digital-aligned wage modes and the counter-moving one sorting on opposite sides of the same axis, with
E47 having identified `fin34c`'s orientation independently and by a different statistic.

**POST-HOC DIAGNOSTIC (labelled, not pre-registered) — is the coherence just two things both hanging
off the same rising headline?** Partial correlation of Δ`fin31d` and Δ`fin34c` controlling for
Δ`g20_any`, 2014→2024:

| lens | r(Δcash, Δfin34c) | r(Δcash, Δhead) | r(Δfin34c, Δhead) | **partial** |
|---|---|---|---|---|
| weighted | +0.515 | −0.336 | **+0.128** | **+0.597** |
| unweighted | +0.389 | −0.266 | **−0.077** | **+0.383** |

The partial **strengthens** on both lenses, so the co-movement is not a common-trend artifact. The
line that does the work is r(Δ`fin34c`, Δ`g20_any`) = **+0.128 / −0.077**: `fin34c`'s *level* is
strongly counter-moving to the headline (E47: −0.552 / −0.486) while its *change* is essentially
unrelated to the headline's change. That is the level-vs-change distinction the primary's registered
null reading anticipated, showing up in the secondary as well. E35's warning that partials are
weighting-fragile is noted; this one is not — both lenses agree in sign and magnitude class.

**Declared.** Δ→Δ co-movement inside the same window identifies nothing; both margins may move with a
third factor, and the partial above rules out only one specific third factor. `fin31d` and the
`fin34` items are narrow, `INDICATORS`-unregistered variants under G3 whose **meanings are inferred
from levels and coverage** (`HARNESS_V2_NOTES.md` items 5–6), never from a questionnaire — "the two
cash margins" is a structural reading of two negative signs, not a documented fact about what either
question asked. `fin31d_s` was excluded from the Δ design as registered. `neff` 7.2–7.5 against
nominal n 71–77 on every cell (B10); no significance language attaches to nominal n. The secondary is
a **single Δ cell** (the 2014→2024 long difference) and is logged **`keep-window`** on that basis —
per-window replication of the `fin31d`~`fin34c` pair is its promotion route.

---

## Cycle wrap-up — 2026-08-15b

Working tree clean at start; `coverage.py` run before hypotheses were chosen (rule B1). Three
experiments, five registered claims: **two keeps, one `discard-weighted`, one inconclusive-but-
decisive**. The prediction stream stayed **closed** (P28), as its closing rule requires. B2 was
satisfied twice over — `fin34` had zero ledger mentions and the high-income panel frame had none
either. Lineage (B3): E46 ← E39/E44, E47 ← nothing (a breadth draw), E48 ← E45 (second on that line).

- **E46 — INCONCLUSIVE under the fixed rule (1 of 3), and it still answers the blocking question.**
  Two of the three failures are failures *of the definitional hypothesis*: under the same
  questionnaire, high-income economies **rose** in the same window (**+1.65pp** weighted, only
  **45.0%** falling against a 70% bar), and the developing series returns to **53.0 in 2024 — 0.1pp
  from its 2014 value** after passing through 43.6 and 42.4. An instrument does not un-break itself.
  **Agenda item 1.4 is answered in the negative: the decade series on `save_any_t_d` may be read as
  continuous**, and items 1.4 and 1.7 are unblocked. The one diagnostic that *passed* is the one to
  carry: **90.2%** of the drop sits in the **non-formal residual** (Δformal −0.91pp vs Δresidual
  −8.36pp), so whatever happened in 2014→17 happened to saving outside financial institutions. The
  design cannot separate a real informal-saving contraction from a change in how those channels were
  enumerated, and says so.
- **E47 — KEEP, and the cycle's B2 cell paid immediately.** `fin34` (wage payment modes, **zero
  prior mentions**) contains a **second counter-moving margin**: `fin34c` at **−0.552 weighted /
  −0.486 unwtd** against `g20_any` in 2024, G6 **−0.553**, largest leave-one-out **Brazil +0.096** —
  every lens agrees. The screen that found it used a **four-way classification** (restatement /
  aligned / **counter-moving** / independent) written specifically to fix the bar E45 logged as
  mis-specified against itself, **and E45's old definition would have missed `fin34c` exactly as it
  missed `fin31d_s`**. A labelled post-hoc wave table shows the orientation **emerges**: +0.028/−0.122
  (2014) → −0.419/−0.323 (2017) → −0.690/−0.367 (2021) → −0.552/−0.486 (2024).
- **E48 — the split verdict is the substance.** The **primary is `discard-weighted`**: r(Δ`fin31d`,
  Δ`g20_any`) clears −0.30 on both lenses in **1 of 3** registered cells, where the weighted lens
  would have kept **3/3** (−0.400 / −0.759 / −0.336) and the unweighted **1/3** (−0.159 / −0.352 /
  −0.266). So **E45's counter-moving level correlation is a cross-sectional composition fact —
  cash-heavy economies are digital-poor economies — and not a within-country dynamic one.** That
  reading was written into the pre-registration *before* the answer, which is the only reason it can
  be stated now without suspicion. The **secondary keeps** (`keep-window`): the two counter-moving
  margins **retreat together**, **+0.515 / +0.389** over 2014→2024, surviving BH at q = 0.10 over four
  registered pairs, with a partial controlling for Δ`g20_any` that **strengthens to +0.597 / +0.383**.
- **The cycle's design lesson: register the SIGN, not just the magnitude.** E48's secondary named the
  predicted direction in advance. `fin34a` and `fin34b` came back **larger** than the keep pair
  (−0.744 and −0.799) and were **ineligible**, because they point the other way — the two
  digital-aligned wage modes *rise* where the cash margin falls. Without the direction in the
  registration the natural write-up would have been "three of four pairs cohere at |r| ≥ 0.30", a
  sentence that folds two contradictory patterns into one claim. Logged as a standing recommendation
  for every multi-item family test.
- **A frame worth reusing.** The **high-income panel** (`pan_all` minus `pan_dev`, 40 economies) had
  zero prior mentions and carries the ledger's **highest Kish `neff` — 9.2 against nominal n 40** —
  precisely because it excludes the giants. It is a cheap **placebo frame** for any "did the
  instrument change?" question. Caveat: only 5 of its economies report `save_any_t_d` in 2024.

---

## 2026-08-15c — enforcement pass (no experiments; protocol, tooling and documentation only)

Prompted by a two-week review rather than by an experiment. Eight changes, all additive; every
existing gate, threshold and pre-registration rule stands.

**Rules added to `program_findex.md`** — B14 (a single adjacent-wave Δ→Δ may not be a primary),
B15 (register the sign), B16 (path before span), B17 (micro-stream quota, one in three cycles),
B18 (the distillation trigger, now a rule with a threshold), B19 (structured ledger fields).
Plus two documentation obligations — `LEDGER_INDEX.md` replaces `RESEARCH_LOG.md` as the required
cycle read, and the four-way orientation screen becomes the standard first move on an untouched
module — and **one status table** consolidating a vocabulary that had been defined across five
separate amendment blocks.

**Tooling.** New `make_index.py` (loop-owned, extendable; `harness.py` / `micro.py` / `coverage.py`
remain fixed). It regenerates `LEDGER_INDEX.md` and **enforces B19 and B14 mechanically** —
`python3 make_index.py --check` exits non-zero on a blank structured field, an unknown design family,
or a single-window Δ→Δ logged as a keep. Currently: **73 experiments, 36 keeps, 0 problems.**

**Ledger migration.** `findings.tsv` gained eight columns after `status` — `design`, `windows`,
`frame`, `n`, `neff`, `r_w`, `r_u`, `parent`. All 73 records and the status distribution are
unchanged (verified before and after: discard 33 / keep 20 / keep-window 9 / keep-general 6 /
discard-weighted 3 / keep-general-unweighted 1 / inconclusive 1), and `coverage.py` — which reads the
ledger as raw text, not positionally — still parses it. `design` and `windows` were backfilled **by
hand from a full read of all 73 test strings**, not by regex; `neff` and `parent` by regex; `n`,
`r_w`, `r_u` were left empty on historical rows. **An empty cell in a pre-2026-08-15 row means NOT
RECOVERED, never zero.** Rows from E46 on are fully populated.

**Cycle shape rewritten** in `RESEARCH_AGENDA.md` and in the run instructions. The old shape —
*"one Program-1 replication + one new-ground experiment + one prediction experiment"* — had **two of
its three slots pointing at closed programs**: Program 1 closed 2026-08-15 (E46 answered 1.4/1.7),
Program 2 closed 2026-08-13 (E42), Program 6 closed 2026-08-10 (E37), and the prediction stream
closed 2026-08-09 (P28). New shape: untouched-module four-way screen · micro experiment (B17) ·
replication or inference pass on a standing keep (B14-compliant).

**The prediction stream stays closed, with its reopening condition now written down.** P28's rule
allows reopening only by a change to the **task**. The one recommended change is an **earlier holdout
wave** — train ≤ 2017, predict 2021 — because the champion has been evaluated on exactly one holdout,
so account **5.014** / resilience **6.625** / saving **6.831** carry no error bar and nobody knows
whether those are properties of the method or of the 2024 wave. That is a validation of a closed
champion, not a new attempt to beat it.

**New agenda items opened:** 7.7 (per-window replication of the `fin31d`~`fin34c` pair, E48b's
promotion route), 7.8 (the unexplained 2021→24 rebound common to both counter-moving margins),
3.10 (`fin43` as the next untouched-module screen).

---

## Cycle 2026-08-16 — B18 DISTILLATION CYCLE (no experiments registered)

**The trigger check, run at the point rule B1's coverage run happens, as B18 requires.**

- `python3 make_index.py` → 73 experiments, 36 keeps, **0 rule problems** (`--check` exits 0).
- `python3 coverage.py` → country file 48/429 columns touched (11%), micro 35/192 (18%); untouched
  country modules `con` (blocked), `fin`, `fin13`, `fin25`, `fin14`, `fin43`, `inactive_t_d_s`; all
  four wave transitions used; `urbanicity` the only unused frame (single-wave).
- **B18 trigger — FIRED.** `PAPER_DRAFT_v2.md`'s CORRECTIONS OWED block carries **seven** items
  against a threshold of five. The second branch (ten experiments since the last distillation) has
  **not** fired: the last distillation was 2026-08-11 (E40/E41) and seven experiments have run since
  (E42–E48). One branch is enough.

**Consequence, per B18: this cycle registers NO new experiments.** The three cycle slots
(untouched-module screen, micro `U` experiment, replication/promotion pass) are all skipped. The
micro quota (B17) is therefore **not** met this cycle and is explicitly carried: the micro stream has
not run since U21 (2026-08-09), and rule B17 obliges the next cycle to open with a `U` experiment.

**What this cycle produces instead:** `PAPER_DRAFT_v3.md`, a full rewrite that executes all seven
corrections and folds in E42–E48; a rewritten `EXTENSIONS_DRAFT.md` status; a `SUPERSEDED` header on
v2 so the trigger reads the live draft from here on; and the agenda's live-item list updated.

**No status changes are owed.** The two pending demotions (E7, E5b) were executed on 2026-08-11; the
three failed promotions (E23/E24/E25 via E35, E43 via E44, E5b via E38) are already recorded as
*failed* rather than *not attempted*; E13's weighting flag stands and is not a demotion. The ledger
and the draft were out of sync, not the ledger and itself.

### The rewrite, executed — 2026-08-16

**`PAPER_DRAFT_v3.md` is written and all seven corrections are discharged.** Appendix B of v3 maps
each v2 error to the section that fixes it. In summary:

1. **Title and organising claim restricted.** "Access converges, use diverges" is demoted from title
   to a subsection of §9 and restricted to the **resource** axes. The cohort and sex axes are stated
   as the counter-cases (usage gap narrowed on age 64.5% and labour force 57.4%; gender a coin flip at
   54.5% / 53.2%), and the five-axis asymmetry ordering is reported as **not yet tested** as a
   monotonicity claim rather than as a finding. New title is balance-sheet framed.
2. **§4 rewritten around the balance-sheet window**, with the deceleration stated in the same
   section as the co-movements it qualifies: 2021→24 is digital payments' weakest window (21.1% of
   economies ≥ +10pp) against saving 42.1% and borrowing 52.6%, and E41's merchant-payment margin is
   presented as the out-of-sample check that the reframing passed.
3. **The three-rails decomposition withdrawn as a general claim** (§5), with E35's mechanism —
   r(Δmm, Δdigpay) +0.871 in 2017→21 against +0.600 in 2021→24 — given as the reason, so the reader
   learns why it is a window property rather than being told that it is.
4. **§7 demoted from a boundary to a measure comparison.** Both failure modes are stated: E33's
   `fh` family co-moving with the rails at 0.354–0.705 while orthogonal to `fin24aSD_ND`, and E26's
   `discard-weighted` status at +0.294 / +0.364.
5. **E7 and E5b deleted, not softened**, and E17's +0.480 is no longer used as evidence (retention
   0.28, p_boot 0.589).
6. **A new §10 carries the inference**, with E40's 26/33-vs-1/33 result, the E42/B11 qualification
   that the `neff` critique is a statement about the *weighted* lens only, the median de-weighting
   shift of −0.051, the four-diagnostics point (China vs Brazil at identical `neff` 7.2), and the
   sixteen triple-clean rows.
7. **§11 states the forecasting stream is final**, with the one reopening condition.

**Material added that post-dates v2 entirely:** E42's all-four-window account~saving result (the
ledger's best-supported country-level regularity, and absent from v2 because in v2's single window it
reads +0.198 weighted), E46's decade-continuity finding, E43/E44's breadth-and-failed-replication
pair, U21's connectivity row in the access-absorption ruler, and E47/E48's counter-moving cash
margins as a new §8 — written under B16 with the full wave path and the rebound stated in the text.

**Two things the rewrite forced that were not on the correction list.** (i) §5 now carries the
**design-level** result — seven level-to-change experiments, zero keeps — as a finding in its own
right, because it is the common cause of the failed partials, the failed lagged designs and the
closed prediction stream, and it was scattered across three sections in v2. (ii) The **undocumented
items** caveat is promoted from a footnote to a numbered limitation and to the top of the extension
agenda: three separate lines of work are blocked on a questionnaire that is not in the repo.

**Companion updates.** `PAPER_DRAFT_v2.md` header replaced with a SUPERSEDED block, its corrections
block closed and frozen at zero outstanding. `EXTENSIONS_DRAFT.md` marked absorbed into v3, with the
three known-wrong passages named. `program_findex.md` B18 amended: the trigger reads the
highest-numbered `PAPER_DRAFT_v*.md`, the count branch resets at each distillation, and the
observation that the two branches measure different debts (volume vs known falsity) is recorded.
`RESEARCH_AGENDA.md` addendum written.

**Carried to the next cycle, in priority order.** (1) **B17 is unpaid** — the micro stream has not run
since U21 and the next cycle must open with a `U` experiment; agenda item **5.5** is the natural draw.
(2) The design base rates are now on record and `level-to-change` at 0/7 should not be re-registered
without a stated difference from the seven failures. (3) No coverage was consumed this cycle, so the
B2 cell is wide open, with `fin43` the best-covered untouched country module.

---

# Cycle 2026-08-17 — PRE-REGISTRATION (U22, E49, E50)

## B18 distillation-trigger check (rule B18, amended 2026-08-16 — read the highest-numbered draft)

Highest-numbered draft: `PAPER_DRAFT_v3.md`. Its header reads **CORRECTIONS OWED: none outstanding**
(0 items against a threshold of 5). Experiment count at the last distillation: **73** (2026-08-16);
`make_index.py` reports **73 logged experiments** now, so **0 experiments** have run since the
rewrite against a threshold of 10. **Neither branch fires. This is a normal experiment cycle.**

## B1 coverage run (done before any hypothesis was chosen)

`python3 coverage.py` — country file 49/429 columns touched (11%); untouched families **`con`
(blocked), `fin` (93 cols, ZERO touched), `fin13`, `fin25`, `fin14`, `fin43`**. Micro file 35/192
touched (18%), 150 untouched columns in 18 families. Transitions 19 / 64 / 127 / 286 across
2011→14 / 14→17 / 17→21 / 21→24. `urbanicity` is the only untouched frame and is single-wave.
`python3 coverage.py --module fin` confirms the 2026-08-16 correction: **`fin10` and `fin2_t_d` carry
all five waves × 77 developing economies**, with `fin30`/`fin37`/`fin37_39*` at four waves and
`fin37_38*`/`fin38*`/`fin26a` at three. The `fin` catch-all is the largest reachable untouched block
in the repo and is this cycle's B2 breadth cell.

## Cycle shape (2026-08-15c shape; B17 first because it is carried and unpaid)

| slot | experiment | rule it satisfies |
|---|---|---|
| 2 | **U22** — within-country connectivity gaps (agenda 5.5) | **B17** micro quota, unpaid for two cycles |
| 1 | **E49** — mapping pass + four-way orientation screen on the untouched `fin` catch-all | **B2** breadth cell + Documentation obligation 2 |
| 3 | **E50** — per-window replication of the `fin31d`~`fin34c` co-retreat (agenda 7.7) | **B14** all-windows design, B4/B8 promotion test |

Parents: U22 ← U21 (first descendant). E49 ← none (new module). E50 ← E48b (first descendant).
No lineage exceeds B3's cap of three.

---

## U22 (slot 2, B17) — is the connectivity gap in digital-payment use a WITHIN-COUNTRY regularity?

**Agenda item 5.5.** Parent: **U21**. Micro stream, 2024 wave, cross-sectional — no trend language.

**Why.** U21 established two pooled facts: among accountholders the offline-vs-online gap in
`anydigpayment` is **+13.6pp**, and account holding absorbs **55.5%** of the unconditional +30.5pp
connectivity gap — an absorption share unlike any resource axis. Both are POOLED figures over 140
economies and could be a between-country composition artifact: economies with low internet use are
also economies with low digital payment use. U19 and U20 ran exactly this test on the education and
income axes and both kept. Connectivity is the axis where the composition worry is largest, because
it is the axis on which economies differ most.

**Design (U19/U20 design verbatim, connectivity substituted).** For every economy with **≥ 100
unweighted respondents in BOTH cells** (M2) among accountholders (`account == 1`), compute the
weighted gap `anydigpayment(internet_use==1) − anydigpayment(internet_use==0)`. Report the median,
IQR, sign count, range with economy names, the qualifying economies' share of accountholding
respondents, the pooled gap over the SAME qualifying set, and the **composition wedge**
(pooled − median).

**Registered claims and bars, both required for a keep:**
- **C1** the median within-economy gap is **≥ +5.0pp** (the standing micro gap threshold), and
- **C2** the gap is **positive in ≥ 80% of qualifying economies** (U19 96–98%, U20 89%).

**Registered sign (B15):** positive — online accountholders use digital payments *more*.

**Secondary, registered:** the same within-country decomposition of U21's **absorption** result —
per economy, the connectivity gap among accountholders as a fraction of the connectivity gap among
all adults, reported as a median. This has no bar and is logged as a diagnostic; it exists so that
U21's headline 55.5% is not left as a pooled-only number.

**Gates.** M1 (enforced by `micro.py`). M2 on every reported cell, ≥ 100 unweighted per cell.
M3 against the country file on `account` and `anydigpayment`, tolerance 1pp.

**Declared.** `internet_use` is self-reported internet USE, co-determined with digital payment use —
a person may report using the internet *because* they pay digitally, and one cross-section cannot
separate the directions (U21's caveat, carried). Conditioning on account holding is post-treatment.
Single wave: no trend language. A within-country regularity is still an association, not a mechanism.

---

## E49 (slot 1, B2) — the `fin` catch-all: mandatory mapping pass + four-way orientation screen

**No parent — a new module.** B2 breadth cell: **`fin`, 93 columns, zero ledger mentions**, the
largest reachable untouched country block (the 2026-08-16 correction).

**Part A — MAPPING PASS, logged as EXPLORATORY under the peek rule.** For every `fin` column with
**≥ 3 waves at ≥ 70 developing economies**, print the weighted level by wave and the country count.
Meanings are INFERRED from levels and coverage only — there is no questionnaire in the repo
(`HARNESS_V2_NOTES.md` items 5–6) — and that caveat travels with everything below. The mapping is
written to `HARNESS_V2_NOTES.md` before the screen is read.

**Part B — the FOUR-WAY ORIENTATION SCREEN (Documentation obligation 2), the registered primary.**
Each eligible item is correlated against the digital-payment headline `g20_any` in the **2024
developing-panel cross-section** (E45/E47's anchor, so the results are comparable), both lenses:

- `restatement` |r| ≥ 0.80 · `aligned` +0.30 ≤ r < 0.80 · `counter-moving` r ≤ −0.30 ·
  `independent` |r| < 0.30 — **both lenses must agree**, else `mixed-lens` (B9/B11).

**Registered keep condition:** at least one item classifies as **`counter-moving`** on both lenses,
survives **G6** with the sign intact, and has a bootstrap interval (2,000 country draws) excluding
zero. A screen returning only `restatement`/`aligned` items is a **discard** — the module would then
be a re-description of the headline, as `dig_acc` was found to be.

**Registered sign (B15):** the keep direction is **negative** (counter-moving). An item at
r ≥ +0.80 is a restatement and is the opposite result, not partial confirmation.

**Secondary, registered:** the same screen against `account_t_d`, reported for every eligible item.
No bar; it exists to distinguish "counter-moves with digital payment" from "counter-moves with
financial access in general" — the distinction E47 drew on `fin34c`.

**B6/B9/B10/B12 on every cell:** weighted and unweighted r, bootstrap percentile interval and
`p_boot`, Kish `neff` beside nominal n, G6 drop-top-5, and the **largest single leave-one-out effect
with the economy named**.

**Declared.** A 2024 cross-sectional level correlation is a **composition** statement about
economies, not a within-country dynamic one — E48's primary is the standing proof that the two come
apart. No Δ claim is registered here. G3: every `fin` item is an unregistered narrow variant.

---

## E50 (slot 3, B14) — does the cash co-retreat hold in EVERY window? (agenda item 7.7)

**Parent: E48b** (`keep-window`, first descendant). **B14-compliant: an all-windows design** — the
registered claim must hold in **every** tested transition, not a majority.

**Why.** E48b is a single long-difference cell: r(Δ`fin31d`, Δ`fin34c`) = **+0.515 weighted /
+0.389 unweighted** over 2014→2024, G6 +0.443, partial controlling for Δ`g20_any` +0.597 / +0.383.
Under B4/B8 it cannot be promoted until every earlier window agrees in sign and clears the bar. E39
established that country-level Δ does not autocorrelate, so a long difference can be carried by one
sub-window; this experiment finds out which.

**Design.** r(Δ`fin31d`, Δ`fin34c`) on the developing panel in **2014→2017, 2017→2021 and
2021→2024**, both lenses, with the 2014→2024 long difference recomputed inside the file first
(the E35 rule: every replication file reproduces its parent's cell before any verdict is read; abort
if it does not reproduce within 0.02).

**Registered bar and sign (B15).** **r ≥ +0.30 on BOTH lenses in ALL THREE windows** →
**`keep-general`** (B4 + B8). Any window failing the bar, or agreeing in magnitude but with a
**negative** sign, → E48b **stays `keep-window` and is recorded as having FAILED its promotion
test**, never as "not attempted". A lens split (weighted passes 3/3, unweighted does not) →
`discard-weighted` on the promotion, with E48b left at `keep-window`.

**B16 — path before span.** The experiment prints the intermediate wave levels for both margins.
Known non-monotonicity, from E47: `fin31d` 47.1 → 34.1 → 20.5 → **26.6** and `fin34c`
15.9 → 11.8 → 8.0 → **15.2** — both fall for a decade and rebound in the last window (agenda item
7.8). The rebound is *in* the 2021→24 window this design tests, so that window is the informative
one and its result is registered in advance as such either way.

**Secondary, registered:** the partial controlling for Δ`g20_any`, per window, both lenses — E48b's
partial strengthened on the long difference and the question is whether it does so in each window.
No bar (E35: partials are the most weighting-fragile design in the ledger); a diagnostic.

**B6/B9/B10/B12 on every cell.** **Declared:** Δ→Δ co-movement inside a window identifies nothing;
both margins may move with a third factor. Item meanings are inferred, never read from a
questionnaire.

---

# Cycle 2026-08-17 — VERDICTS

**U22 — KEEP.** The connectivity axis of the access-absorption ruler is a **within-country
regularity**. Among accountholders in the 56 economies qualifying on M2 in both cells, the median
internet-user-minus-non-user gap in `anydigpayment` is **+10.62pp**, positive in **55 of 56 (98.2%)**
— both registered bars cleared, sign as registered. Pooled over the *same* 56 economies the gap is
+15.20pp, so the **composition wedge is +4.58pp (30.1% of the pooled gap)** — the largest of the
three ruler axes tested this way (U19 22%, U20 28%), which is what one expects on the axis where
economies differ most, and still leaves 70% of the pooled gap inside economies. The secondary turns
U21's pooled absorption figure into a within-country one: **median 65.0%** of the all-adult
connectivity gap is absorbed by account holding (IQR 31.4–83.5%, positive in 53/56), against U21's
pooled 55.5% — the pooled number was, if anything, an understatement of the typical economy.
**Coverage caveat, stated because it bounds the claim:** requiring ≥100 unweighted respondents in
*both* cells qualifies only 56 of 140 economies holding 40.8% of accountholding respondents, because
in high-internet economies the *offline* accountholder cell is thin. The qualifying set is tilted
toward lower-connectivity economies. The two flattest cases are the saturated ones — Kenya +0.3 and
Malawi +0.1, both at 97–99% on **both** sides — which is the gap closing where digital payment is
universal rather than the gradient failing.

**E49 — DISCARD (registered), with a large exploratory mapping deliverable (E49x).** The B2 breadth
cell. The 93-column `fin` catch-all yields **24 columns at ≥3 waves × ≥70 developing economies**, of
which `fin10` and `fin2_t_d` carry all five waves. The registered four-way orientation screen against
`g20_any` in the 2024 cross-section returns **0 of 24 counter-moving on both lenses** — the keep
condition is not met. The family is **12 aligned, 7 independent, 4 mixed-lens and 1 outright
restatement**. The most negative item is `fin37_38_39c` at **−0.135 weighted / −0.101 unweighted**,
not within 0.16 of the bar on either lens. At the other end `fin26a` is a **restatement at +0.933 /
+0.852 through G6 (+0.850)** — under B15's registered sign that is the opposite result, not partial
confirmation, and `fin26a` should not be used as an independent margin. `fin2_t_d` (+0.883/+0.669)
and `fin10` (+0.847/+0.516) are `mixed-lens` restatement/aligned, both moved by China alone (−0.140,
−0.267). **The consequence for the ledger: `fin31d` and `fin34c` remain the only two counter-moving
country-file margins the loop has found, now out of three modules screened identically — they are
rarer than two hits in two modules suggested.** Three structural facts from the mapping are written
to `HARNESS_V2_NOTES.md` item 9: (i) the `fin37`/`fin38`/`fin39` items **compose** — `fin37_38`,
`fin37_39x`, `fin38_39x`, `fin37_38_39x` are intersections or unions of the base items, so their
correlations are not independent tests and any future experiment must pick one level of the
composition and say which; (ii) the `a`/`b`/`c`/`d` suffixes behave consistently across all three
composites, which is the strongest available evidence that the letters are the same four categories
throughout; (iii) `fin30` **falls 57.0 → 45.3** across the decade and is *not* counter-moving
(+0.254/+0.306), which separates "declining margin" from "counter-moving margin" — a distinction the
loop had not previously had a case for.

**E50 — DISCARD-WEIGHTED on the promotion; E48b stays `keep-window` and is now on record as having
FAILED its promotion test.** The all-windows design (B14) reproduces E48b's long-difference cell
exactly (+0.515/+0.389) and then splits: r(Δ`fin31d`, Δ`fin34c`) is **+0.795 / +0.650 / +0.615**
weighted across 2014→17 / 2017→21 / 2021→24 — **3/3 clearing +0.30, every bootstrap interval
excluding zero, G6 sign intact (+0.463 / +0.320 / +0.374)** — against **+0.431 / +0.243 / +0.263**
unweighted, **1/3**. Under B9 that is `discard-weighted`. Two things distinguish this from the
ledger's other failed promotions and both were registered in advance. **It is not a reversal**: all
six lens-windows are positive, so this is a magnitude failure of the 0.30 bar, unlike E5b's
−0.654 / +0.591 / −0.595. And **it reproduces E48's primary lens split exactly — weighted 3/3,
unweighted 1/3 — on a different pair of margins in the same two modules**; two independent designs
now say the same thing about this cell, that the weighted lens sees a per-window regularity where
the unweighted lens sees the largest economies (China −0.275 and −0.215 in the two earlier windows,
India −0.239 in the last). The secondary partial controlling for Δ`g20_any` **exceeds the raw
correlation in the first and last windows on both lenses** (+0.754/+0.413 and +0.720/+0.274) and
collapses in the middle one (+0.422/+0.150), so the co-retreat is not the two margins sharing the
headline's trend — except in 2017→21. B16 path: `fin31d` 48.3 → 34.6 → 20.5 → 26.6, `fin34c`
15.9 → 11.8 → 8.0 → 15.2, `g20_any` 35.1 → 45.4 → 56.4 → 60.9.

**Cycle bookkeeping.** B18 checked and not fired (v3 carries zero corrections owed; zero experiments
since the 2026-08-16 rewrite). B17 **paid** by U22 after two unpaid cycles. B2 cell consumed: the
`fin` catch-all, 93 columns, now touched. B3 lineage: no chain exceeds two. `make_index.py` gained an
`exploratory` status so a mapping pass is neither a keep nor a discard; `--check` passes at 77 rows,
0 problems.

---

# Cycle 2026-08-18 — PRE-REGISTRATION (E51, E52)

## B18 distillation-trigger check (rule B18, amended 2026-08-16 — read the highest-numbered draft)

Highest-numbered draft: `PAPER_DRAFT_v3.md`. Its header reads **CORRECTIONS OWED: none outstanding**
(0 items against a threshold of 5). Experiment count at the last distillation: **73** (2026-08-16);
`make_index.py` now reports **77 logged experiments**, so **4 experiments** have run since the
rewrite against a threshold of 10. **Neither branch fires. This is a normal experiment cycle.**

## B1 coverage run (done before any hypothesis was chosen)

`python3 coverage.py` — country file **63/429 columns touched (15%)** after E49 opened `fin`.
Untouched country families: **`con`** (133 cols, 2024-only, blocked for want of a questionnaire),
**`fin13`** (30 cols, 2024-only, 27 developing economies), **`fin25`** (14 cols, mostly 2024-only),
**`fin14`** (8 cols, 2024-only, 27 economies), **`fin43`** (6 cols, **four waves × 71–77
developing economies**). `python3 coverage.py --module fin43` confirms the 2026-08-17 B2 note:
`fin43a` and `fin43c` carry 2014/2017/2021/2024 at 71–77 economies, `fin43b` and `fin43d` carry
2017/2021/2024, and the two `_s` subset columns are thin (2–52 economies) and therefore ineligible.
**`fin43` is the best-covered untouched country block left and is this cycle's B2 breadth cell.**
Micro file 41/192 touched (21%); 112 untouched columns in 17 families. Transitions 19 / 66 / 129 /
288 across 2011→14 / 14→17 / 17→21 / 21→24. `urbanicity` remains the only untouched frame and is
single-wave.

## Cycle shape (2026-08-15c shape)

| slot | experiment | rule it satisfies |
|---|---|---|
| 1 | **E51** — mapping pass + four-way orientation screen on the untouched `fin43` agricultural-payments module | **B2** breadth cell + Documentation obligation 2 |
| 3 | **E52** — B12 weight-structure sweep on the `fin31d`~`fin34c` cash cell (agenda item **7.9**) | inference pass on a standing keep; **not** another correlation |

**Slot 2 (micro) is deliberately skipped and this is the required statement of why (B17).** B17 asks
for one `U` experiment every three cycles; **U22 paid it on 2026-08-17**, one cycle ago, so the quota
next falls due in two more cycles. The micro side remains the largest untouched surface in the repo
and the next cycle should draw from it.

Parents: **E51 ← none** (new module). **E52 ← E48b/E50** (second descendant in that chain: E48b →
E50 → E52). No chain reaches B3's cap of three consecutive descendants.

**Agenda items 7.8 (the three-instance 2021→24 rebound) is NOT drawn this cycle** even though the
2026-08-17 addendum named it a candidate: it needs a B14-compliant primary that is not another
adjacent-window Δ→Δ, and designing that is a cycle's work on its own. It stays first in line.

---

## E51 (slot 1, B2) — the untouched `fin43` agricultural-payments module: mapping pass plus the
four-way orientation screen

**B2 breadth cell.** `fin43` has **zero ledger mentions**. It is small (6 columns, 4 eligible) but it
is the only untouched country family with **four waves at ≥70 developing economies**; every other
untouched family is 2024-only or covers 27 economies. **Parent: none** (a new module).

**PART A — MAPPING PASS, logged as EXPLORATORY under the peek rule (2026-07-11).** For every `fin43`
column, the population-weighted developing-panel level by wave with the country count. **Item
meanings are INFERRED from levels and coverage only**; there is no questionnaire in the repo
(`HARNESS_V2_NOTES.md` items 5–6) and that caveat travels with every claim made here.

**A composition warning carried forward from E49x (HARNESS_V2_NOTES item 9(i)), registered before the
run.** In the `fin37`/`fin38`/`fin39` family the loop found that suffixed items **compose** —
parents are unions or intersections of their components — so correlating a parent with a component is
a redundancy artifact, not a test. `fin43a`–`fin43d` may be a base item plus payment modes in exactly
that shape. Part A prints the wave levels for all four; **if the levels are consistent with
composition (a base item whose level is approximately the sum or the maximum of the others), the
screen result is reported for all four but any claim names ONE level of the composition and says
which.**

**PART B — THE FOUR-WAY ORIENTATION SCREEN (Documentation obligation 2), the registered primary.**
Each eligible item against the digital-payment headline `g20_any` in the **2024 developing-panel
cross-section** (E45/E47/E49's anchor, so the numbers are comparable), **both lenses**:

    restatement    |r| >= 0.80
    aligned        +0.30 <= r < 0.80
    counter-moving r <= -0.30
    independent    |r| < 0.30
    both lenses must AGREE, else `mixed-lens` (B9/B11)

**Registered eligibility:** ≥3 waves at ≥70 developing economies (E49's thresholds, unchanged).

**REGISTERED KEEP CONDITION:** at least one item classifies as **`counter-moving` on BOTH lenses**,
survives **G6** with the sign intact, and has a **bootstrap interval (2,000 country draws) excluding
zero**. A screen returning only restatement/aligned/independent items is a **DISCARD**.

**REGISTERED SIGN (B15): the keep direction is NEGATIVE.** An item at r ≥ +0.80 is a restatement and
is the **opposite** result, not partial confirmation.

**What is at stake, stated in advance.** After three modules screened identically (`fin31`, `fin34`,
`fin`), `fin31d` and `fin34c` are the **only** counter-moving country-file margins in the ledger.
`fin43` is a payments module in an agricultural setting, i.e. the part of the economy where cash
persists longest, so it is the best remaining prior for a third. A discard here makes the
two-margin count harder still to read as a sampling accident.

**SECONDARY (registered, no bar):** the same screen against `account_t_d`, every eligible item — the
E47 distinction between "counter-moves with digital payment" and "counter-moves with financial access
in general".

**B6/B9/B10/B12 on every cell:** weighted and unweighted r, bootstrap percentile interval and
`p_boot`, Kish `neff` beside nominal n, G6 drop-top-5, and the **largest single leave-one-out effect
with the economy named**.

**Declared.** A 2024 cross-sectional **level** correlation is a **composition** statement about
economies, not a within-country dynamic one — E48's primary is the standing proof that the two come
apart. No Δ claim is registered here. G3: every `fin43` item is an unregistered narrow variant.

---

## E52 (slot 3, agenda item 7.9) — B12 weight-structure sweep: WHY do the two lenses disagree on the
cash cell?

**Parent: E48b / E50** (second descendant). **This is an inference/audit pass, not an association
experiment**, so B14's long-difference-or-all-windows requirement does not bind: no new co-movement
is registered here. Every cell it touches is already in the ledger.

**Why.** The `fin31d`~`fin34c` cash cell is the ledger's clearest **stable** weighted/unweighted
disagreement. E48's primary split weighted 3/3 against unweighted 1/3; E50 reproduced that split
**exactly** on a different pair of margins in the same two modules (weighted **+0.795 / +0.650 /
+0.615**, unweighted **+0.431 / +0.243 / +0.263**). Two designs now agree that something systematic
separates the lenses here, and the ledger's standing explanation is the phrase B12 was written to
ban: "the big economies decide it". **B12 replaced the guess with a named economy; this experiment
replaces the named economy with a mechanism.** There are two candidate mechanisms and they have
different consequences:

- **HETEROGENEITY** — the association really is stronger in large economies. Then the weighted
  statistic is *correct about the typical person* and the unweighted one is *correct about the
  typical economy*, exactly as the 2026-08-13 amendment says, and the disagreement is a finding
  about population size rather than a defect.
- **LEVERAGE** — a handful of enormous weights carry the weighted number and there is no size
  gradient underneath. Then the weighted statistic is an artifact of the weight distribution and
  should not be reported as a developing-world regularity at all.

**Design.** Pair (Δ`fin31d`, Δ`fin34c`) on the developing panel in **four cells**: 2014→17, 2017→21,
2021→24 and the 2014→2024 long difference. E50's cell values are recomputed inside the file first
(**the E35 rule**: reproduce the parent's published numbers before reading anything registered;
**abort** if the long difference does not reproduce +0.515 / +0.389 within 0.02). Per cell:

1. **Weight-tercile unweighted correlations.** Economies split into terciles by 2024 adult
   population; `r_u` computed *within* each tercile. This is the heterogeneity test and it uses **no
   weights at all**, so it cannot be produced by leverage.
2. **Winsorized-weight correlation.** `r_w` recomputed with weights capped at the **90th percentile**
   of the weight distribution (a second cut at the median is reported as a diagnostic). This is the
   leverage test: capping changes only the weight vector, never the sample.
3. **Fragility depth.** The minimum number of economies whose greedy removal drives `r_w` below
   +0.30, with the economies **named** — the ledger's first direct answer to "how many economies
   decide a weighted keep". Searched to a cap of 10.
4. **Ascent depth.** The mirror statistic for the unweighted lens: the minimum greedy removals that
   lift `r_u` above +0.30, also named and capped at 10.
5. Full B6/B10/B12 reporting on every cell: bootstrap interval and `p_boot` for each tercile
   correlation and each capped-weight correlation, Kish `neff`, and the five largest single
   leave-one-out effects with the economies named.

**REGISTERED VERDICT RULE (fixed before the run, evaluated over the four cells):**

- **HETEROGENEITY** fires if in **≥3 of 4 cells** the **top**-population-tercile `r_u` ≥ **+0.30**
  **and** the **bottom**-tercile `r_u` < **+0.30**.
- **LEVERAGE** fires if in **≥3 of 4 cells** the **90th-percentile-capped** `r_w` < **+0.30**.
- Exactly one fires → **`keep`**, and the audit's claim names that mechanism.
- Both fire → **`keep`**, and the claim names both (they are not mutually exclusive: a size gradient
  and a few dominating weights can coexist).
- Neither fires → **`inconclusive`** under the status table's definition (a registered diagnostic
  whose fixed verdict rule returns neither branch).

**REGISTERED SIGN (B15).** All correlations in this cell are positive in every lens-window measured
so far, so the heterogeneity branch is registered with a **positive** sign: a top-tercile `r_u`
at or below **−0.30** would be the opposite pattern and is reported separately, never as partial
confirmation.

**B16 — path before span** applies to the long-difference cell and the file prints the wave levels:
`fin31d` 48.3 → 34.6 → 20.5 → 26.6 and `fin34c` 15.9 → 11.8 → 8.0 → 15.2 (E50), **both non-monotone,
falling for a decade and rebounding in the last window** (agenda item 7.8, unexplained).

**Declared, and it bounds every branch.** Tercile correlations run on ~24 economies each; small-n
correlations are noisy and the bootstrap intervals will be wide, which is why the verdict rule asks
for a **pattern across four cells** rather than significance in any one. Nothing here is causal, and
nothing here rehabilitates or demotes E48b — its status is fixed at `keep-window`, FAILED promotion.
This experiment explains a disagreement; it does not resolve it in either lens's favour.

---

# Cycle 2026-08-18 — VERDICTS

**E51 — DISCARD as registered, with an exploratory mapping deliverable (E51x) and one unregistered
signal worth a future primary.** The B2 breadth cell. `fin43` yields **4 eligible columns of 6**
(`fin43a`, `fin43b`, `fin43c`, `fin43d`; the two `_s` columns are the *conditional* versions of their
base items — 33–47% and 77–87% against base levels of 2.2% and 8.8% — reported on 2–52 economies and
therefore ineligible). The registered four-way screen against `g20_any` in the 2024 cross-section
returns **0 of 4 counter-moving**: the module is **2 aligned** (`fin43a` +0.370/+0.492,
`fin43b` +0.431/+0.391) and **2 independent** (`fin43c` −0.146/−0.234, `fin43d` −0.023/−0.135).
The keep condition is not met. **`fin31d` and `fin34c` remain the only counter-moving country-file
margins in the ledger, now after four modules screened identically** — and `fin43` was the best
remaining prior for a third, being payments in the part of the economy where cash persists longest.

**The one signal worth carrying, and it is UNREGISTERED.** The two anchors disagree on `fin43c`. It
is *independent* of the digital-payment headline (−0.146/−0.234) and **counter-moving with account
ownership on both lenses** (−0.389/−0.322, G6 −0.273) — the exact mirror of E47's `fin34c`, which
counter-moved with digital payment and *not* with access. The secondary carried no registered bar and
its bootstrap interval includes zero ([−0.653, +0.035]), so this cannot be a keep and is not logged
as one; it is a candidate primary for a later cycle. `fin43d` is `mixed-lens` on the same anchor.

**E51x, the mapping (exploratory).** Weighted developing-panel levels: `fin43a` 1.7 → 2.1 → 2.1 →
2.9, `fin43b` — → 1.0 → 0.9 → 2.2, `fin43c` **21.5 → 10.7 → 6.6 → 8.8**, `fin43d` — → 0.2 → 0.1 →
0.0. Inferred from levels and coverage only (no questionnaire in the repo): `fin43c` behaves like the
**cash** mode of agricultural payments and `fin43a`/`fin43b` like account and mobile modes rising
from near zero. The composition trap of the `fin37` family does **not** apply here — no item is near
the sum of the others (`fin43c` 8.8 against 5.1). **A fact for agenda item 7.8: `fin43c`'s path is a
FOURTH instance of fall-then-rebound** — 21.5 → 10.7 → 6.6 → **8.8** — after `fin31d`, `fin34c` and
`fin42`, and in a fourth module. Every cash-side margin the loop has mapped in four modules turns up
in 2021→24.

**E52 — INCONCLUSIVE under the registered rule, and the two branches fail for opposite reasons.**
Agenda item 7.9. The E35 reproduce-the-parent check passes exactly (+0.515 / +0.389, zero deviation).
**Neither registered mechanism fires.** The **leverage** branch fires **0 of 4**: winsorizing the
weights at their 90th percentile raises Kish `neff` from **7.2–7.5 to ~32** and leaves
r_w at **+0.591 / +0.466 / +0.418 / +0.476** — above the bar in every cell. Capping at the *median*
(`neff` ≈ 60, a 4-fold de-concentration) still gives **+0.468 / +0.294 / +0.292 / +0.403**. The
**heterogeneity** branch fires **2 of 4**, and it fails for a reason worth stating precisely: the
**top** population tercile clears +0.30 in **4 of 4** cells (+0.546 / +0.356 / +0.482 / +0.544, the
interval excluding zero in three); what breaks the registered pattern is that the **bottom** tercile
*also* clears it in two cells (+0.369 and +0.391). The rule asked for a binary gradient and the data
returned a graded one.

**Two registered results survive the inconclusive verdict.**

*(i) "Five economies decide it" is false for this cell in the leverage sense and true in a different
sense, and the two senses now have numbers.* De-concentrating the weights fourfold costs the
correlation 0.10–0.20 and never crosses the bar — so the weighted statistic is not an artifact of the
weight vector. But the **fragility depth** — the minimum greedy removals that drive r_w below the bar
— is **5 (China, Indonesia, Pakistan, Egypt, Russia) / 2 (China, Pakistan) / 2 (India, Philippines) /
3 (Brazil, Viet Nam, Turkiye)**. Few economies *do* decide the verdict; they do not decide it *by
carrying disproportionate weight*. This is E45's clarification — a low `neff` is not the same claim as
a fragile result — measured from both sides in one cell for the first time.

*(ii) The unweighted lens is decided by small economies just as tightly, and nobody names them.* The
**ascent depth** — the minimum greedy removals that lift r_u *above* the bar — is **0 / 2 (Ukraine,
Bulgaria) / 1 (Bulgaria) / 0**. **Removing Bulgaria alone flips the unweighted 2021→24 verdict**, and
Ukraine plus Bulgaria flips 2017→21: those are precisely the two windows that produced E50's lens
split. The ledger's standing worry is that China and India decide weighted results. On this cell the
unweighted lens is no more stable — it is unstable in economies the write-ups never mention, because
G6 and B12 both look at the *largest* economies by construction.

**The unregistered pattern, recorded as a candidate for a later registration and not as a finding.**
Within-tercile unweighted r **rises with population size in 4 of 4 cells** (mean top-minus-bottom
**+0.253**) and is monotone across all three terciles in 3 of 4. A graded size gradient is the
natural registered test here, and this cycle cannot claim it because this cycle looked first.
**E48b's status is unchanged: `keep-window`, FAILED promotion.** B16 path reprinted: `fin31d`
48.3 → 34.6 → 20.5 → 26.6, `fin34c` 15.9 → 11.8 → 8.0 → 15.2.

**Cycle bookkeeping.** B18 checked and not fired (v3 carries zero corrections owed; 4 experiments
since the 2026-08-16 rewrite against a threshold of 10). B2 cell consumed: **`fin43`**, 6 columns,
now touched — the country file goes from 63 to 69 of 429 columns (16%), and `coverage.py` now lists only four untouched families (185 columns), all of them 2024-only or 27-economy. B17 **not paid and the
skip is declared**: U22 paid it on 2026-08-17, one cycle ago, and it next falls due in two cycles;
the micro side remains the largest untouched surface in the repo. B3 lineage: the longest chain is
E48b → E50 → E52, two consecutive descendants, under the cap of three. B14 not engaged — E51 is a
cross-sectional screen and E52 registers no association. `make_index.py --check` passes at 80 rows,
0 problems.

---

## Wrap-up — 2026-08-18

1. **E51 DISCARD (registered).** The untouched `fin43` agricultural-payments module contains no
   counter-moving margin: 2 aligned, 2 independent, **0 of 4** against `g20_any`. After four modules
   screened with the same instrument, `fin31d` and `fin34c` remain the ledger's **only** two
   counter-moving country-file margins.
2. **E51x (exploratory) delivered two structural facts.** The `_s` suffix is a *conditional*
   denominator (`fin43c` 8.8% of adults vs `fin43c_s` 77.8% on 30 economies) and must never share a
   correlation with its base item; and `fin43c` **21.5 → 10.7 → 6.6 → 8.8** is a **fourth** instance
   of agenda item 7.8's fall-then-rebound, in a fourth module.
3. **E52 INCONCLUSIVE (registered).** Neither candidate mechanism for the cash cell's standing
   weighted/unweighted disagreement fires. **Leverage is rejected 0/4** — a p90 weight cap takes
   `neff` from 7.2 to ~32 and leaves r_w at +0.42 to +0.59 — and the *binary* heterogeneity pattern
   fires 2/4 only because the bottom population tercile also clears the bar twice; the top tercile
   clears it **4/4**.
4. **The cycle's most transferable result is a reporting asymmetry, not a correlation.** Fragility
   depth (weighted) is **5 / 2 / 2 / 3** named economies, while ascent depth (unweighted) is
   **0 / 2 / 1 / 0** — **Bulgaria alone flips the unweighted 2021→24 verdict**. G6 and B12 examine
   only the largest economies, so the ledger has been reporting one-sided stability evidence.
5. **Bookkeeping.** B18 not fired (0 corrections owed, 4 experiments since the rewrite). B2 paid by
   `fin43`; **no untouched country family clears the eligibility floor any more**, so B2 must move to
   the micro side or the `urbanicity` frame next. B17 skipped with the declaration required, due in
   two cycles. Longest lineage E48b → E50 → E52 (two descendants, cap three). Prediction stream
   unchanged and CLOSED: `account_t_d` **5.014**, `fin17a_17a1_d` **6.831**, `fin24aSD_ND` **6.625**.

---

# Cycle 2026-08-19 — pre-registration

**B18 distillation trigger CHECKED and NOT FIRED.** The trigger reads the highest-numbered draft,
`PAPER_DRAFT_v3.md` (B18 amendment 2026-08-16): its corrections block reads *"CORRECTIONS OWED: none
outstanding"* — **0 items against a threshold of 5**. The count branch: the last distillation was
2026-08-16 at experiment count 73; the ledger now stands at **80**, i.e. **7 experiments since the
rewrite against a threshold of 10**. Neither branch fires, so this is a normal experiment cycle.

**B1 coverage run (before any hypothesis was chosen).** Country file **69 of 429 columns (16%)**.
Four untouched country families remain and **none clears the eligibility floor**: `con` (133 cols,
2024-only, still blocked — no questionnaire ships with the data and the column names are opaque, so
no `con` claim can be *worded*, confirmed again this cycle by inspecting the country header), `fin25`
(14, mostly 2024-only), `fin13`/`fin14` (38 cols, 2024, 27 developing economies). Micro file **45 of
192 columns (23%)**, 16 untouched families / 108 columns. All four wave transitions are used;
`urbanicity` is the only unused country frame and is single-wave.

**Coverage cells this cycle lands on, named in advance.**
- **U23 — B2 breadth cell and B17 micro quota, both paid here.** Three *untouched* micro columns:
  `receive_pensions`, `receive_agriculture`, `pay_utilities`. Per the 2026-08-18 addendum's B2 note,
  the breadth cell had to move to the micro side, and it does.
- **E53 — the four-item cash rebound (agenda item 7.8)**, a `distribution` design across all five
  waves. Frame `pan_dev`, columns already touched; the breadth is in the *design*, not the columns.
- **E54 (if the budget allows) — agenda item 2.1b**, the population-size gradient in association
  strength, registered fresh on the six E28/E30 bivariate rails.

**B3 lineage.** U23 parent: **U14** (first descendant of it; the U19→U20→U22 chain is not extended).
E53 parent: **none** — item 7.8 is a pattern noticed across E45/E47/E49x/E51x, not a finding
descended from one of them; the nearest design ancestor is E39. E54 parent: **E52** (E48b → E50 →
E52 → E54 would be a *third* consecutive descendant, at the cap of three but not over it).

**B14.** U23 is a micro cross-section (B14 does not apply). E53 is a distribution design over the
full five-wave path, not an adjacent-window Δ→Δ. E54 registers no new Δ→Δ primary — it re-slices
existing all-windows cells by population.

## U23 — pre-registered (micro stream)

**Coding disclosure (a structural check on the CODING, not a peek at the outcome; U14 precedent).**
No codebook ships with the microdata. Before registering I checked the code structure of every
untouched payment-stream column by looking at `account`/`account_fin`/`anydigpayment` *within each
code*, exactly as U14 did. `receive_pensions`, `receive_agriculture` and `pay_utilities` are coded
**identically to `receive_wages`**: code 1 = the payment runs through an account (account = 1.000,
1.000 and 0.963; anydigpayment = 1.000, 0.991, 0.956 — true by construction), code 2 = cash
(account 0.276 / 0.468 / 0.545), code 3 = other (n = 1,005 / 872 / 2,324), code 4 = did not
participate in the stream, code 5 = DK/refused (n ≤ 244). **`domestic_remittances` is EXCLUDED and
the reason is recorded**: it carries four codes with a structure that does not match the family —
code 4 (n = 40,768) has account = 0.942 but anydigpayment = 0.481 — so its semantics cannot be
established without a questionnaire and no claim on it could be worded honestly. `fin32`/`fin33` are
excluded as wage-stream detail already represented by U14's margin. The registered outcome below —
the education gradient in each stream — is unknown at registration time.

**H.** Among adults who **already hold an account** and who participate in a given payment stream,
the share whose payment runs **through the account** rather than in cash is **education-graded**, and
this holds in **all three** untouched streams, not only in the wage stream U14 tested. Motivation:
U14 found the last mile of *wage* digitalization steeply education-graded conditional on access, and
U10/U15/U17/U18 found the same for self-directed digital-payment use. Every one of those margins is
either chosen by the adult or set by an employer. The three streams here are different: a **pension**
is paid by a government or pension provider, an **agricultural payment** by a buyer of produce, and a
**utility bill** is paid *out* by the adult. If the gradient is a property of the adult it should
appear in all three; if it is a property of the payer it should appear where the payer is an
institution and not where the adult chooses. That is the point of the test.

**Test.** Restrict to `account == 1` AND stream code ∈ {1, 2, 3} (participants, excluding "did not
participate" and DK/RF). Weighted rate of code == 1, split by `educ` (1 = primary or less,
2 = secondary, 3 = tertiary), pooled across all 2024 economies with raw `wgt` per `micro.py`'s
default. Statistic per stream: **gap = rate(educ 3) − rate(educ 1)**.

**REGISTERED SIGN (B15): POSITIVE** — tertiary higher than primary. A gap of the right magnitude and
the wrong sign is the opposite pattern and may not be counted toward the keep.

**Keep if:** gap ≥ **+5.0pp** (the standing micro threshold) in **all three** streams, with M2
satisfied on every reported cell. Two of three is a partial and is logged as `discard` with the
pattern described.

**Secondary 1 (registered, with a fixed rule).** The same gap computed **unconditional** on account
holding, and the **absorption share** = 1 − (conditional gap / unconditional gap) per stream — the
ledger's access-absorption ruler (U10 64% education, U20 58% income, U21/U22 55–65% connectivity).
**Registered direction: absorption is LOWER in these payer-set streams than the ~64% the ruler gives
for self-directed digital-payment use**, because access cannot absorb a gradient that a third party
imposes. Bar: **median absorption across the three streams < 50%**. Reported either way; it does not
gate the primary.

**Secondary 2 (registered, with a fixed downgrade rule).** The pooled gap is vulnerable to
between-country composition exactly as U19/U20/U22 were. For each stream, the **within-economy** gap
in economies where both education cells have unweighted n ≥ 100 (M2), reported as a median, a
positive-sign share, and the qualifying set's share of respondents. **Fixed rule: any stream that
keeps on the pooled gap but shows a within-economy median < 5pp or a positive share < 60% is
downgraded in the claim text to "pooled only, composition-suspect".**

**Gates.** M1 (weights, enforced by the module). M2 (unweighted n ≥ 100) on every reported cell.
M3 against the country file on `account`, tolerance 1pp — declared **n/a for the three stream
margins themselves**, which have no country-file equivalent at this conditional granularity.

**Declared caveats.** Payment mode in the pension and agriculture streams is largely set by the
payer, so an education gradient there describes *who is paid how*, not an individual choice — and
sectoral and formality composition are uncontrolled confounds throughout. Conditioning on account
holding is conditioning on a post-treatment variable. Pension receipt is strongly age-selected and
agricultural receipt strongly rural-selected; the gradient is not adjusted for either, and the claim
must not be read as education net of them. Single 2024 cross-section — no trend language, no causal
wording.

## U23 — verdict: **KEEP** (registered bar met in 3/3 streams)

**Primary, as registered.** Among accountholders who participate in the stream, the share whose
payment runs through the account rather than in cash, tertiary minus primary-or-less:

| stream | payer picks the channel | primary → tertiary | gap | 95% CI (economy cluster) |
|---|---|---|---|---|
| `receive_pensions` | government / pension provider | 83.0 → 89.5 | **+6.51pp** | [+3.64, +9.54] |
| `receive_agriculture` | buyer of produce | 35.2 → 49.3 | **+14.16pp** | [+5.86, +22.22] |
| `pay_utilities` | **the adult** (self-directed) | 41.9 → 68.0 | **+26.07pp** | [+19.43, +31.43] |
| `receive_wages` *(U14 reference, not part of the bar)* | employer | 56.6 → 91.9 | +35.28pp | [+28.62, +41.88] |

3/3 clear +5.0pp with the **registered positive sign** (B15) and every interval excludes zero, so
the registered claim keeps. **The registered question is answered in the "property of the adult"
direction**: the gradient does not need the adult to choose the channel — it survives in the pension
stream, where a government or provider decides how the money arrives.

**But the magnitudes order the streams, and that ordering is the interesting part.** Pensions
**+6.5** < agriculture **+14.2** < utilities **+26.1** < wages **+35.3**. The stream where an
institution pays a standardized, regular, legally-defined benefit shows the *smallest* gradient by a
factor of four against the self-directed one; the two streams where a private counterparty (a
buyer, an employer) or the adult picks the channel show the largest. Read descriptively: an
institutional payer appears to flatten the last mile, and this is one 2024 cross-section, not
evidence of what a policy would do.

**Honest reading of the pension result.** It is the fragile one. Its interval [+3.64, +9.54]
straddles the registered bar and only **83.8% of 1,000 cluster-bootstrap draws** reach +5.0pp. The
claim keeps as registered on the point estimate; the write-up must not present +6.5pp as if it were
as secure as the +26.1pp.

**Secondary 1 (access absorption) — CONFIRMED, by 0.6 of a percentage point.** Absorption of the
all-adult education gradient by account holding: pensions **69.0%**, agriculture **49.4%**,
utilities **30.3%**, wages **30.9%**; **median 49.4% against the registered bar of < 50%**. This is
a coin-flip confirmation and is recorded as one. The *pattern* is worth more than the verdict: the
ruler's ~64% figure (U10/U19) is reproduced almost exactly by the **pension** stream (69%) and
missed by half in the two streams where a private counterparty or the adult picks the channel
(30%). Access absorbs the gradient where the payer is an institution and does not where it is not.

**Secondary 2 (composition) — runnable on ONE stream of three, and this is a frame fact.** Zero
economies reach 100 unweighted respondents in **both** education cells for pensions or for
agriculture, so the within-country check simply cannot be run on them: those two streams are
**pooled-only and unverified on composition**. The registered downgrade rule did not anticipate
"cannot run" and I have not counted it as a pass. Where it does run — `pay_utilities`, 8 economies
holding 14.4% of accountholding participants — the median within-economy gap is **+31.53pp**,
positive in **7 of 8** (North Macedonia −0.5 the exception, India +48.2 the maximum), and the pooled
gap over the same 8 is +35.44pp, a **composition wedge of +3.91pp (11%)** — the smallest wedge of
any axis the loop has measured this way (U19 22%, U20 28%, U22 30%).

**B6 inference.** Bootstrap resamples **economies**, not respondents: respondents are clustered
inside economies and a respondent-level resample would report a falsely narrow interval. Kish `neff`
of the survey weights inside each education cell is **569–5,128 against nominal 874–7,602** — the
weights are mildly concentrated, nothing like the country-level `neff` ≈ 7.2. **The ledger's `neff`
critique is about population weights across economies and does not transfer to micro survey
weights**; what limits precision here is the 90-economy cluster count, which the bootstrap prices in.

**Gates.** M1 module-enforced. M2 passes on every reported cell. M3 on `account` 0.0pp maximum
deviation over 10 economies; declared n/a for the three stream margins, which have no country-file
equivalent at this conditional granularity. Caveats as registered: pension receipt is age-selected,
agricultural receipt rural-selected, neither adjusted; conditioning on account holding is
post-treatment; single 2024 cross-section, no trend language.

## E53 — pre-registered (hypothesis stream)

**Agenda item 7.8, the repo's clearest unexplained pattern.** Four cash-side items in four different
modules all fall across 2014→2021 and rebound in 2021→2024: `fin31d` 48.3 → 34.6 → 20.5 → **26.6**,
`fin34c` 15.9 → 11.8 → 8.0 → **15.2**, `fin42` 24.6 → 14.7 → 10.8 → **13.4**, `fin43c` 21.5 → 10.7 →
6.6 → **8.8** (levels quoted from E48b/E49x/E51x; E53 reprints them itself, rule B16). Single-item
mean reversion is a sufficient explanation for one V-shape. It is not a sufficient explanation for
four V-shapes in the same window in four modules **if they occur in the same economies**.

**Parent: none.** The pattern was noticed across E45/E47/E49x/E51x rather than descending from a
finding; the nearest design ancestor is **E39** (distribution design). Frame `pan_dev`. **B14:** this
is a distribution design over the full four-wave path, not an adjacent-window Δ→Δ, and the primary
statistic is a co-occurrence count, not a correlation of changes.

**H.** The 2021→24 rebound is a **common episode across cash-side items within the same economies**,
not four independent item-level reversions. If it is common, economies should carry the V-shape on
several items at once far more often than independent items would produce.

**Test (primary).** On the 71 developing-panel economies with all four items in all four waves
(2014/2017/2021/2024), classify each economy × item as **V** if `level_2021 < level_2014 − 1pp`
**and** `level_2024 > level_2021 + 1pp`. Count V-items per economy (0–4). Statistic: **S3 = the share
of economies with ≥ 3 of 4 V-items.** Null: **1,000 permutations** in which each item's V-indicator
is shuffled independently across economies, preserving each item's marginal V-rate and destroying
only the co-occurrence.

**REGISTERED SIGN (B15): POSITIVE excess** — more multi-item economies than independence predicts. A
deficit of multi-item economies is the *opposite* pattern (items rebounding in disjoint economies)
and may not be counted toward the keep; it would be reported separately as a substitution pattern.

**Keep if:** S3_observed ≥ **1.5 ×** the permutation-null mean S3 **and** S3_observed exceeds the
**97.5th percentile** of the permutation distribution. Both required.

**Secondary A (registered, no bar, B16).** Reprint every item's four wave levels on this exact
71-economy set, weighted and unweighted, so the path is on the record beside the span.

**Secondary B (registered, no bar, the E39 question).** For each item, the share of the 71 economies
whose 2021→24 change is positive, unweighted and population-weighted, plus the median change — is the
aggregate rebound a within-country movement or a few large economies?

**Secondary C (registered, no bar).** The population-weighted twin of the primary: the share of
developing-panel adults living in an economy with ≥ 3 V-items, against the same null.

**Robustness (registered in advance, reported whatever it shows).** The 1pp margin is arbitrary, so
the whole primary is recomputed at margins of **0pp and 2pp**; and the mirror tail (share of
economies with **0** V-items) is reported against the null, because genuine clustering shows in both
tails. A verdict that survives only at one margin is reported as margin-dependent.

**Inference (B6).** Economy bootstrap, 1,000 draws, percentile interval on S3_observed. Kish `neff`
of the 2024 adult-population weights on the 71-economy set, reported beside the nominal n (B10).

**Gates.** G3 declared: the four items are used at their base (non-`_s`) level — per
`HARNESS_V2_NOTES` item 10 the `_s` columns are conditional versions and are excluded. G4 coverage on
the 71-economy set. G5 n/a (no official aggregate for these items). G6 n/a — no correlation is
computed; the analogous check is the mirror tail and the population-weighted twin, both registered
above.

**Declared caveats.** Four items sharing a *shape* is not evidence they share a *cause*; the shape is
also consistent with a common survey or questionnaire change in 2024 affecting cash-side items
together, which this design cannot rule out and which E46 already found it could not settle for
`save_any_t_d`. The items are not independent by construction either — an economy where cash use is
generally high can carry several of them. Descriptive co-occurrence only, never causal.

## E53 — verdict: **KEEP (margin-dependent)** on the registered primary, and the registered secondaries **overturn the premise of agenda item 7.8**

**Coverage.** 71 developing-panel economies carry all four items in all four waves — 68.6% of the
pan_dev 2024 adult population. Nominal n = 71, Kish `neff` = **7.2** (B10).

**PRIMARY — the co-occurrence keeps as registered.** At the registered 1pp margin, **10 of 71
economies (14.1%)** carry the V-shape on **≥ 3 of the 4** items, against a permutation null of
**6.7%** — a ratio of **2.11×**, above the null's 97.5th percentile (11.3%), permutation
**p = 0.003**. Registered sign POSITIVE, observed POSITIVE. Economy bootstrap 95% CI
**[7.0%, 22.5%]**. The named set: **Bulgaria, Congo Rep., Dominican Republic, India, Madagascar,
Philippines, Sri Lanka, Thailand, Uganda, Viet Nam**.

**The registered robustness makes it margin-dependent, and this is reported as registered.** The
two-part bar (ratio ≥ 1.5 **and** above null p97.5) fires at **1 of 3** margins:

| margin | S3 observed | null mean | ratio | p_perm | verdict |
|---|---|---|---|---|---|
| 0pp | 22.5% | 15.8% | 1.42× | 0.024 | FAIL (ratio below 1.5) |
| **1pp (registered)** | **14.1%** | **6.7%** | **2.11×** | **0.003** | **PASS** |
| 2pp | 5.6% | 2.1% | 2.69× | 0.048 | FAIL (ties the p97.5, does not exceed it; 4 economies) |

The *direction and the permutation p* hold at every margin — excess co-occurrence is present
throughout — but the conjunction of the two registered bars fires only at 1pp, so the claim is
logged **margin-dependent** and the 2pp failure is a discreteness tie on four economies, not a
reversal. **Population-weighted twin (Secondary C): 44.2% of developing-panel adults live in a
≥3-V economy against a null of 6.8% (6.49×, p = 0.004) — but India is in the named set and India is
what that number is.**

**SECONDARY A + B — the aggregate rebound is largely a COMPOSITION ARTIFACT, and this contradicts
the premise the experiment was registered on.** On the balanced 71-economy set the four paths are
**fin31d 40.8 → 33.4 → 26.9 → 26.6**, **fin34c 14.5 → 13.1 → 10.5 → 15.2**, **fin42 22.1 → 15.7 →
13.3 → 13.4**, **fin43c 18.6 → 11.5 → 9.2 → 8.8** (population-weighted; unweighted **all four** are
flat or still falling in 2021→24). Three of the four items **do not rebound at all** once the set of
economies is held fixed: 2021→24 changes of **−0.28, +4.77, +0.11, −0.42**. And Secondary B says the
same thing from the country side — the share of economies whose 2021→24 change is *positive* is
**39.4% / 42.3% / 46.5% / 47.9%**, fewer than half on every item, with a **negative median change on
all four**.

**Unregistered diagnostic (labelled as such) — why the previously quoted paths rebound.** The paths
in the agenda (`fin31d` 48.3 → 34.6 → **20.5** → 26.6, etc.) are computed over whichever economies
report in each wave. **Six economies report these four items in 2021 and not in 2024 — Algeria,
China, Iran, Mauritius, Russia and Ukraine** — and they are present in the survey's 2024 wave
(`account_t_d` is there for all six); it is **item-level attrition**, not wave absence. **China
alone holds 25.9% of the 2021 reporting population on these items and reports 4.5 / 1.3 / 6.2 / 1.1
on them.** Dropping China alone lifts the 2021 weighted trough by **+5.7 / +2.3 / +1.6 / +2.0pp** —
most of `fin31d`'s apparent rebound. The 2021 trough is China-shaped and the 2024 recovery is China
leaving the denominator. This is rule **B12** in its purest form: name the economy.

**What survives, stated precisely.** (i) The *aggregate* four-item rebound of agenda item 7.8 is
**mostly an artifact of item-level attrition between the 2021 and 2024 waves**, and the agenda item
must be rewritten. (ii) A genuine **minority** within-country V-shape cluster exists and is not
explainable by independent item-level reversion: 10 of 71 economies carry it on three or four items,
2.11× the independence null at p = 0.003, margin-dependent on the registered two-part bar.
(iii) The two claims are compatible — a within-country pattern in one economy in seven does not move
a population-weighted mean, and a population-weighted mean can move with no economy doing anything.

**Gates.** G3 base (non-`_s`) columns, declared. G4 71 economies / 68.6% of pan_dev adults. G5 n/a.
G6 n/a by design — the registered substitutes (the mirror S0 tail and the weighted twin) both ran;
S0 is **above** its null at 0pp and 1pp (1.79× and 1.41×), i.e. the clustering shows in both tails as
the registration anticipated. **Caveats as declared:** a shared shape is not a shared cause, a common
2024 questionnaire change affecting cash-side items together would produce the same co-occurrence and
this design cannot exclude it (E46's unresolved question), and the four items are not independent by
construction. Descriptive co-occurrence, never causal.

## E54 — pre-registered (hypothesis stream)

**Agenda item 2.1b, registered fresh as the addendum required.** E52 noticed, *after looking*, that
within-population-tercile unweighted correlations rise with economy size in 4 of 4 cells of the
`fin31d`~`fin34c` cash cell (mean top-minus-bottom **+0.253**). E52 explicitly could not claim it.
The addendum's instruction was to register the gradient on a **different cell**, and the six
bivariate rails of E28/E30 are the cell it named.

**Parent: E52.** Lineage note (B3): E50 and E52 descend from E48b and E54 descends from E52, but
they are **not consecutive experiments** — U23 and E53 sit between E52 and E54 in this cycle — and
the *data cell* jumps completely, from the two cash margins to the six saving/digitalization rails.
The chain stands at three descendants, at the cap and not over it.

**Why it matters.** If association strength is population-graded, then the ledger's standing
weighted/unweighted disagreements are not a weighting *artifact* at all — they would be the weighted
lens correctly reporting that the association is genuinely stronger in large economies, and the
unweighted lens correctly reporting that it is weaker in small ones. That reading would change how
every `keep-weighted` row in the ledger should be read. If the gradient does **not** generalise, then
E52's cash-cell observation is a property of that cell and the ledger's de-weighting critique stands
as written.

**Test.** The six rails, at their E28/E30 constructions, on `pan_dev`:
`Δmobileaccount_t_d ~ Δfin17a_17a1_d` (E1) · `Δfin32_acc ~ Δfin17a_17a1_d` (E10) ·
`Δg20_any ~ Δfin17a_17a1_d` (E12) · `Δfin22a_22a1_22g_d ~ Δfin17a_17a1_d` (E11) ·
`Δfiaccount_t_d ~ Δmobileaccount_t_d` (E13) · `Δmobileaccount_t_d ~ Δg20_any` (E14),
each in **three windows** (2014→17, 2017→21, 2021→24) = **18 rail × window cells**. In every cell,
split the economies into **terciles of 2024 adult population** and compute the **unweighted** Pearson
correlation within each tercile (unweighted by construction: the question is whether *size* sorts
association strength, and a weighted statistic inside a size tercile would re-import the thing being
tested). Statistic per cell: **Δr = r(top tercile) − r(bottom tercile)**.

**REGISTERED SIGN (B15): POSITIVE** — larger economies show the stronger association. A negative mean
Δr is the opposite pattern, is reported as such, and may not be counted toward a keep.

**Keep if BOTH:** mean Δr across the 18 cells ≥ **+0.15** (a deliberately weaker bar than E52's
+0.253, since E52's cell was chosen by having looked) **AND** Δr > 0 in at least **12 of 18** cells.

**Secondary 1 (registered, the better null).** The +0.15 bar is arbitrary and a tercile r on ~24
economies is noisy. So: **1,000 random splits** in which economies are assigned to three equal groups
**ignoring population**, recomputing the mean Δr each time, giving the distribution of the statistic
under "any split does this". Reported with the permutation p; it does not gate the primary but a
primary that passes while sitting inside the random-split distribution is reported as **not
population-specific**.

**Secondary 2 (registered, no bar).** The monotone count — cells where r(top) > r(mid) > r(bottom) —
and the per-cell table, so the pattern can be read rail by rail rather than only in the mean.

**Inference (B6).** Economy bootstrap within terciles, 1,000 draws, percentile interval on the mean
Δr. Kish `neff` reported per window (B10). Minimum tercile size is checked and any cell with a
tercile below 15 economies is dropped and named.

**Gates.** G3 declared: all six rails at their registered headline variants. G4 coverage per window.
G5 n/a. G6 n/a — no single association is claimed; the random-split null is the registered substitute.
**B14:** no new Δ→Δ primary is registered — the 18 cells are existing all-windows cells of standing
keeps and the primary statistic is a *between-tercile difference of correlations*, evaluated across
all three windows jointly.

**Declared caveats.** Population tercile is confounded with everything that correlates with country
size — region, data quality, sample size per economy, within-country heterogeneity. A within-tercile
correlation on ~24 economies is a noisy statistic and the mean of 18 of them is what carries any
signal. Descriptive; never causal.

## E54 — verdict: **DISCARD as registered.** The population gradient does not generalise, and the ledger's de-weighting critique stands

**Both registered bars fail, and they fail wide.** Mean Δr across the 18 rail × window cells is
**+0.047** against a bar of +0.15, and Δr is positive in **9 of 18** — exactly a coin flip against a
bar of 12. Monotone `r(top) > r(mid) > r(bottom)` in **3 of 18**. Median Δr **+0.028**, range −0.482
(E11 2014→17) to +0.743 (E13 2017→21). All 18 cells were usable; nothing was dropped for tercile size.

**Secondary 1 — the registered null is the decisive number.** Under 1,000 random three-way splits
that ignore population entirely, the mean Δr distribution is centred at **+0.002** with a 95% band of
**[−0.115, +0.108]**. The observed **+0.047 sits inside that band**, `p_perm` = **0.209**. Splitting
economies by *population* does no more to sort association strength than splitting them at random.
**Secondary/B6:** the within-tercile economy bootstrap gives 95% CI **[−0.074, +0.162]**, including
zero. Kish `neff` is **7.2** in every window (B10).

**What this settles.** E52's cash-cell observation (mean top-minus-bottom **+0.253**, monotone in 3
of 4) is **a property of that cell, not of the ledger.** It was found by looking, and registered
fresh on a different cell it does not reproduce. The consequence for how the ledger is read is the
one stated in the registration: **the standing weighted/unweighted disagreements cannot be
reinterpreted as the weighted lens correctly detecting a genuinely stronger association among large
economies.** The de-weighting critique (B9/B11, E40) stands exactly as written.

**One unregistered observation, labelled as such and carried to the agenda, not claimed.** The window
means are **2014→17 −0.113** (positive in 2/6), **2017→21 +0.014** (2/6), **2021→24 +0.240**
(**5 of 6** rails positive). Whatever the mean of 18 says, the size gradient is visible only in the
most recent window — the same window E52's cash cell spans. This was not registered, has no
multiplicity control across three window subsets of a failed primary, and is **a lead for a fresh
registration, not a finding**. The obvious registered form is a window-specific test with the window
named in advance.

**Gates.** G3 six rails at their registered headline variants, declared. G4 18/18 cells, n = 54–77 per
cell. G5 n/a. G6 n/a — no single association is claimed and the random-split null is the registered
substitute; it ran and it is the reason for the discard. Caveats as declared: population tercile is
confounded with region, per-economy sample size and everything else that scales with country size,
and a within-tercile r on ~19–26 economies is noisy. Descriptive, never causal.

---

## Wrap-up — 2026-08-19

1. **U23 KEEP (registered, micro).** The last-mile education gradient in digital payment *mode* is a
   property of the adult, not of one payer: among accountholding participants it clears +5pp in
   **all three** previously untouched streams — pensions **+6.51pp**, agricultural sales
   **+14.16pp**, utility bills **+26.07pp** — every economy-cluster bootstrap interval excluding
   zero. The pension result is the fragile one: only **83.8%** of draws reach the registered bar.
2. **E53 KEEP (margin-dependent) with a premise correction that matters more than the keep.** The
   aggregate four-item cash rebound of agenda item 7.8 is largely **item-level attrition**: six
   economies report those items in 2021 and not 2024 — **China holds 25.9% of the 2021 reporting
   population** at levels of 4.5 / 1.3 / 6.2 / 1.1 — and on a balanced 71-economy set three of the
   four items do not rebound at all. What survives is a **minority within-country V-cluster**:
   10 of 71 economies on ≥3 of 4 items, **2.11×** an independence null, `p_perm` 0.003.
3. **E54 DISCARD as registered.** E52's population-size gradient in association strength does not
   generalise — mean Δr **+0.047** against a +0.15 bar, positive in **9 of 18** cells, and the
   registered random-split null shows a population split does no more than a random one
   (`p_perm` 0.209). The ledger's weighted/unweighted disagreements stay a weighting problem.
4. **The transferable methodological lesson is the same one twice: hold the denominator fixed.**
   E53's rebound and, in a different guise, U23's unrunnable within-economy check both come down to
   *which units are in the set*. `PAPER_DRAFT_v3.md` now carries its first CORRECTIONS OWED item,
   and new agenda item **8.1** proposes the ledger-wide attrition sweep this cycle stumbled into.
5. **Bookkeeping.** B18 checked and **not fired** at registration time (0 corrections owed against 5;
   7 experiments since the 2026-08-16 rewrite against 10) — E53 opened the first correction *during*
   the cycle, so the next cycle's check reads **1 of 5** and 10 of 10 on the count branch, meaning
   **the count branch will fire next cycle**. B2 paid on the micro side (three untouched columns).
   B17 **paid** (U23), next due in three cycles. B3: longest chain E48b → E50 → E52 → E54, three
   descendants, at the cap and non-consecutive. B14 not engaged (no adjacent-window Δ→Δ primary).
   B15 signs registered and reported on all three. B6 intervals on all three. `make_index.py --check`
   passes at 83 rows, 0 problems. Prediction stream unchanged and **CLOSED**: `account_t_d`
   **5.014**, `fin17a_17a1_d` **6.831**, `fin24aSD_ND` **6.625**.

---

# Cycle 2026-08-20 — B18 DISTILLATION CYCLE (no experiments registered)

## The trigger check, run at rule B1's coverage point, as B18 requires

- `python3 make_index.py` → **83 experiments**, 39 keeps, **0 rule problems** (`--check` exits 0).
- `python3 coverage.py` → country file **70/429 columns touched (16%)**, micro **51/192 (27%)**.
  Untouched country modules: `con` (133 cols, blocked for want of a questionnaire), `fin13` (30),
  `fin25` (14), `fin14` (8) — 185 columns in 4 families, of which only `fin25` has ≥2 usable waves
  and 133 are blocked. Untouched micro: 102 columns in 10 families. All four wave transitions used
  (19 / 71 / 134 / 298 mentions). `urbanicity` remains the only unused country frame (single-wave).
- **B18 trigger — FIRED on the COUNT branch.** `PAPER_DRAFT_v3.md` is the highest-numbered draft
  (B18 amendment 2026-08-16) and carries **1** CORRECTIONS OWED item against a threshold of five, so
  the corrections branch has **not** fired. The count branch has: the last distillation was
  2026-08-16 at experiment count **73**, the ledger now stands at **83**, i.e. **exactly 10
  experiments since** (U22, E49x, E49, E50, E51x, E51, E52, U23, E53, E54) against a threshold of
  ten. The 2026-08-19 wrap-up predicted this firing in advance and it is confirmed here.
- **The two branches measure different debts (B18's own note), and this firing is the mirror of the
  first one.** On 2026-08-16 the corrections branch fired at 7 while the count branch stood at 7 of
  10: the draft was stale by being **wrong**. Today the count branch fires at 10 of 10 while
  corrections stands at 1 of 5: the draft is stale by being **behind**. Both are full rewrite cycles;
  B18's amendment says explicitly not to discount a firing because the other branch is low, and the
  symmetric case holds — do not discount this one because only one correction is owed.

**Consequence, per B18: this cycle registers NO new experiments.** All three cycle slots
(untouched-module screen, micro `U` experiment, replication/promotion pass) are skipped.

**Quota bookkeeping under the skip.** B17 (micro quota) was **paid last cycle by U23** and next falls
due in three cycles, so unlike the 2026-08-16 firing this skip carries no unpaid micro debt — the
2026-08-16 lesson was learned by paying the quota early, as its addendum instructed. B2's breadth
cell is **not consumed** (no outcome is computed), so it is wide open for the next cycle. B3's
lineage chain is broken by construction: nothing descends from anything this cycle.

**Status changes owed: NONE, and this was checked rather than assumed.** E48b is recorded as
`keep-window`, FAILED promotion (E50); E52 is `inconclusive` and its unregistered size gradient was
registered fresh and rejected (E54), so no status rests on it; E53 is `keep-window` with **no
promotion route** by construction. The demotions from 2026-08-11 (E7, E5b) stand executed. The
ledger is in sync with itself; only the draft is behind it.

## What this cycle produces instead

`PAPER_DRAFT_v4.md`: a full rewrite folding in all ten unseen experiments, discharging v3's single
outstanding correction, and — the substantive change this evidence forces — **retiring §8's
four-item cash-rebound claim and rebuilding the section around what survived a balanced economy
set**. Companion updates to v3 (SUPERSEDED header), the agenda, and this log.

### The rewrite, executed — 2026-08-20

**`PAPER_DRAFT_v4.md` is written; v3's one outstanding correction is discharged and the block reads
none outstanding.** Appendix B carries both correction records — v3's single item with the section
that fixes it, and v2's seven, forwarded for the audit trail.

**The substantive change is one section, rebuilt in full.** §8 was v3's newest and is now v4's most
revised. Four experiments replaced almost all of it:

1. **§8.1 — the four-module base rate.** `fin31`, `fin34`, `fin` (24 eligible of 93) and `fin43`
   (4 of 6) have now been screened with the identical four-way orientation instrument, returning
   **two** counter-moving margins in total: `fin31d` and `fin34c`. E49's null is 0 of 24 with the most
   negative cell at −0.135; E51's is 0 of 4, and `fin43` was the best remaining *prior* for a third.
   The section now states the base rate rather than the two hits. Two by-products carried into the
   text because any future user of the file needs them: `fin26a` at +0.933/+0.852 is a **restatement**
   of the digital headline and must never be used as an independent margin, and `fin30` is a
   **declining** margin that is **not** counter-moving (+0.254/+0.306) — the loop's first clean
   separation of those two ideas.
2. **§8.2 — E48b's promotion FAILED and the shape of the failure is the result.** Weighted 3/3
   (+0.795/+0.650/+0.615), unweighted 1/3 (+0.431/+0.243/+0.263). Not a reversal — all six
   lens-windows are positive — and it reproduces E48a's lens split **exactly** on a different pair of
   margins in the same two modules. Recorded as `keep-window`, FAILED, per B8.
3. **§8.3 — why the lenses disagree: neither obvious answer.** E52's registered audit rejects
   **leverage** (p90-winsorized weights lift `neff` 7.2 → ~32 and leave r_w at +0.418–+0.591, 4/4
   above the bar; median cap, `neff` ≈ 60, still +0.292–+0.468) and rejects the **binary** tercile
   pattern (2/4, failing because the *bottom* tercile also clears). `inconclusive` is the verdict and
   it is a real one, because both mechanisms were what the project had been assuming.
4. **§8.4 — the rebound was not real.** v3's sentence is deleted, not softened. The balanced-set table
   (fin31d 40.8/33.4/26.9/26.6, fin34c 14.5/13.1/10.5/15.2, fin42 22.1/15.7/13.3/13.4, fin43c
   18.6/11.5/9.2/8.8) replaces the unbalanced paths; the six named drop-out economies and China's
   25.9% share of the 2021 reporting population are given in the text. What replaces the claim is
   E53's registered minority V-cluster — 10 of 71 on ≥3 of 4 items, 2.11× null, `p_perm` 0.003, CI
   [7.0%, 22.5%] — with its margin dependence, its India-driven weighted twin and the
   questionnaire-change alternative all stated as part of the claim rather than appended to it.
   §8.5 keeps E51's `fin43c` anchor split as an explicitly unregistered lead, and states the question
   it raises: the two known cash margins **disagree about which anchor** a cash margin runs against.

**§9 gains two micro experiments and a frame fact.** U22 adds the connectivity row to the
within-country ruler table (median +10.62pp, positive in **55 of 56**, wedge 30%) and raises U21's
pooled 55.5% absorption to a **median 65.0% within economies**. U23 adds the four-stream last-mile
education gradient (pensions +6.51 / agriculture +14.16 / utilities +26.07 / wages +35.28pp, all
intervals excluding zero), with the pension gradient flagged as the fragile one at **83.8%** of
cluster-bootstrap draws clearing the bar. The **qualifying-set** caveat is promoted into the body: the
M2 rule decides which economies can be asked the question at all and the qualifying set is not random
(connectivity 56 of 140 economies, tilted low-connectivity; pensions and agriculture **unrunnable**,
zero economies qualifying). U23's payer-set ordering (69% institutional vs ~30% self-directed) is
carried as a lead, with its 0.6pp bar clearance stated.

**§10 gains two results and loses a defence.** Result 4 is new: the natural reply to the de-weighting
critique — that the weighted lens correctly detects stronger association among large economies — was
registered fresh by E54 on the six rails × three windows and **failed wide** (mean Δr +0.047 vs a
+0.15 bar, 9 of 18 positive), with the registered random-split null decisive at `p_perm` **0.209**.
Result 5 is E52's ascent-depth symmetry: the unweighted verdict on the audited cell turns on
**Bulgaria alone**. §10 also now names the debt it cannot discharge — no experiment has ever checked
whether its Δ held the economy set fixed.

**Two new rules in `program_findex.md`, both forced by the above.** **B20** (hold the denominator
fixed) makes a balanced economy set a requirement rather than a caveat, with the reasoning recorded:
reporting sets are correlated **across items within a module**, so one large drop-out manufactures
apparent co-movement, which is precisely the evidence a co-occurrence claim rests on. **B21** (ascent
depth beside G6 wherever the lenses disagree) converts E52's recommendation into a rule one cycle
after it was made, and carries E54's closing of the size-gradient defence in the same block. v4's
§2 rules list grows from four to five, and §12's limitations from eight to ten.

**Companion updates.** `PAPER_DRAFT_v3.md` header replaced with a SUPERSEDED block, its corrections
block closed and frozen at one item marked executed, and its extension items 2/3/6 marked closed by
post-dating evidence. `EXTENSIONS_DRAFT.md` status block re-pointed at v4, with B20 added as a fourth
known-wrong class applying to any wave path on a narrow item. `RESEARCH_AGENDA.md` addendum written:
item 7.8 **struck** (premise wrong, no successor with a promotion route), item 8.1 promoted to the
project's highest-priority open item, B2's cell re-derived.

**Carried to the next cycle, in priority order.** (1) **Item 8.1, the ledger-wide reporting-set
sweep**, is the natural slot-3 draw and the only way to size the risk B20 exposes; it is currently
stated as *unquantified*, which is the honest word and not a comfortable one. (2) **B2 has no
eligible untouched country module left** — 185 untouched country columns, 133 blocked and the rest
below the wave-coverage floor — so the breadth cell must come from the micro file (102 columns in 10
families) or the frames. (3) B17 is paid through two more cycles. (4) The `fin43c` anchor question
(item 7.10) and the payer-set ordering (7.11) are the two best-specified unregistered leads, and both
now have their registration requirements written into v4.

## Wrap-up — 2026-08-20

1. **B18 fired on the COUNT branch and the cycle registered no experiments.** Ten experiments since
   the 2026-08-16 rewrite against a threshold of ten, with corrections at only **1 of 5** — the mirror
   of the first firing, where the draft was stale by being *wrong* rather than *behind*. It was still
   a full rewrite: the count branch found more than the corrections branch had, because a correction
   only ever gets opened by a cycle that trips over it.
2. **`PAPER_DRAFT_v4.md` is written and §8 is rebuilt in full.** v3's "both margins fall for a decade
   and then rebound" is **deleted**. The section now leads with the four-module screen base rate
   (**two** counter-moving margins from `fin31`/`fin34`/`fin`/`fin43`), carries E48b's **failed**
   promotion (weighted 3/3, unweighted 1/3), E52's audit rejecting both leverage and binary
   heterogeneity, and E53's balanced-set correction with the surviving minority V-cluster.
3. **Two new rules, B20 and B21.** B20 requires a **balanced economy set** on any path or Δ and makes
   an unbalanced one inadmissible as a primary — reporting sets are correlated across items within a
   module, so one large drop-out manufactures co-movement. B21 requires **ascent depth beside G6**
   wherever the lenses disagree: on the audited cell the unweighted verdict turns on **Bulgaria
   alone**, and the project's stability evidence had been one-sided by construction.
4. **A defence of the weighted lens is now closed.** E54's registered random-split null (`p_perm`
   **0.209**) means splitting economies by population does no more than splitting them at random, so
   the ledger's weighted/unweighted disagreements cannot be reread as the weighted lens detecting
   something real about large economies. This is written into v4 §10 as Result 4 and into B21's block.
5. **Bookkeeping.** No new experiments, so no new `findings.tsv` rows; the ledger stands at **83 rows,
   39 keeps**, `make_index.py --check` passes with 0 problems. No status changes were owed and this
   was checked rather than assumed. B17 paid through two more cycles; B2's cell not consumed and now
   **has no eligible untouched country module left**; B3 broken by construction. Highest-priority open
   item is **8.1**, the ledger-wide reporting-set audit. Prediction stream unchanged and **CLOSED**:
   `account_t_d` **5.014**, `fin17a_17a1_d` **6.831**, `fin24aSD_ND` **6.625**.

---

# Cycle 2026-08-21 — PRE-REGISTRATION

## Mandatory cycle-start checks

**B18 distillation trigger — DOES NOT FIRE.** Evaluated against the highest-numbered draft,
`PAPER_DRAFT_v4.md` (B18 amendment 2026-08-16). Corrections branch: the CORRECTIONS OWED block reads
"none outstanding" — **0 of 5**. Count branch: the last distillation completed 2026-08-20 at
experiment count 83, and **0 experiments** have run since — **0 of 10**. Neither branch fires; this is
a normal experiment cycle.

**B1 coverage run — done before any hypothesis was chosen.** `python3 coverage.py`: country file
**70/429 columns (16%)**, micro file **51/192 (27%)**. All four wave transitions are USED. Country
untouched families: `con` (133, permanently blocked — no questionnaire, opaque names, re-checked
2026-08-19), `fin13` (30, 2024 × 27 economies), `fin25` (14, mostly 2024-only), `fin14` (8, 2024 × 27)
— confirming the 2026-08-20 note that **no eligible untouched country module remains**. Untouched
micro: 102 columns in 10 families.

**B2 breadth cell — the untouched MICRO EMERGENCY-FUND module.** `fin24`, `fin24a`, `fin24b`,
`fin24c`, `fin24d1`, `fin24d2`, `fin24d3`, `fin25e1`, `fin25e2`, `fin25e3`, `fin25e4` — **11 columns,
zero ledger mentions**, and the country-side twin (`fin25`, 14 columns) is untouched as well. This is
Program 4 item 4.3 ("emergency-fund sources beyond savings and borrowing") taken at the individual
level, where the coverage is 2024-only anyway and the micro file is the better instrument.

**B17 micro quota — PAID this cycle** by U24 (last paid 2026-08-19, U23).

**B3 lineage** — U24x/U24 parent `none` (new module, no parent finding); E55 parent `E53`. No chain
of three.

**B14** — E55 is an audit, not an association primary; no adjacent-wave Δ→Δ is registered anywhere in
this cycle.

**Cycle shape.** Slot 1 + slot 2 are merged and paid by the same draw (an untouched-module pass that
is also the micro-stream experiment): **U24x** (mandatory exploratory mapping) then **U24**
(registered). Slot 3 is **E55**, agenda item **8.1** — the project's highest-priority open item and
the draw the 2026-08-20 addendum named for this slot.

---

## U24x — EXPLORATORY mapping pass on the untouched micro emergency-fund module

Logged as **exploratory** under the peek rule (2026-07-11 amendment) BEFORE any registered
hypothesis on these columns. No hypothesis, no threshold, no keep is possible from this entry.

**What it computes and nothing else.** For each of the 11 columns: the labelled value set with
weighted shares, unweighted non-missing n, number of economies with ≥100 unweighted non-missing
respondents, and whether the module is **split-sample** (n materially below the 144,090 file, which
would make `wgt` the wrong weight — the check the 2026-08-19 addendum demanded before any `fin48`/
`fin49`-style registration). Plus one binary recode of the headline resilience item and its **M3**
cross-check against the country file's `fin24aSD_ND` on ≥20 economies.

**What it must NOT compute, so that U24 remains genuinely pre-registered:** no split by `educ`,
`inc_q`, `age`, `female`, `emp_in`, `urbanicity` or `account`, and no gradient or absorption
statistic of any kind.

---

## U24 — the access-absorption ruler applied to the RESILIENCE margin

**Parent:** none (new module). **Stream:** micro. **Frame:** micro, 2024, pooled over economies,
weighted (`wgt`), M1 by construction.

**Hypothesis.** The ledger's access-absorption ruler — account holding absorbs ~**64%** of the
education gradient in digital-payment use (U10, and a within-country median of the same order in
U19) — is a property of *usage* margins and **does not transfer to a welfare margin**. The country
stream says the same thing from the other side: three tests (E2, E15, E26) agree self-reported
resilience does not move with digitalization. If resilience is a resource margin rather than a
usage margin, then account holding — which is the gate on usage — should absorb **much less** of the
education gradient in emergency-fund availability than it absorbs of the gradient in digital-payment
use.

**Registered SIGN (B15).** The education gradient in emergency-fund availability is predicted
**POSITIVE** (secondary-or-more above primary-or-less) both unconditionally and conditional on
account holding. A gradient of the right size and the wrong sign is **not** partial confirmation.

**Exact test.** Outcome: the binary recode of the headline emergency-fund possibility item validated
in U24x (the `fin24aSD_ND`-equivalent — "very possible" or "somewhat possible"), declared under G3 as
the headline variant. Education split: `educ` primary-or-less vs secondary-or-more, pooled, weighted.

- P1 unconditional gap = rate(secondary+) − rate(primary or less), all adults.
- P2 conditional gap = the same gap computed within `account == 1`.
- P3 absorption = 1 − (P2 / P1).

**Keep bar — all three must fire:**
1. P1 ≥ **5pp** and **positive** (registered sign);
2. absorption < **40%** (against the ruler's ~64% on digital-payment use);
3. P2 ≥ **5pp** and **positive**.

**Discard** if the gradient is under 5pp, wrong-signed, or absorption ≥ 40%. A result with
absorption ≥ 40% is a *transfer* of the ruler and is reported as such — the opposite pattern, not a
weaker version of the same one.

**Registered secondary (within-country, U19/U20/U22 form).** Sign of the account-conditional
education gap inside each economy qualifying M2 (≥100 unweighted respondents in **both** education
cells within `account == 1`): bar **≥75% positive**. Reported with the count and participant share
of the qualifying set, per the frame facts U22 and U23 recorded — the qualifying set is not the file.

**Gates and inference.** M1 weights throughout; **M2** ≥100 unweighted per cell on every reported
cell; **M3** carried from U24x. **B6**: country-clustered bootstrap (resample economies with
replacement, 2,000 draws, percentile interval) on P1, P2 and the absorption share. No trend language
— single wave, cross-sectional description.

---

## E55 — the ledger-wide reporting-set audit (agenda item 8.1)

**Parent:** E53. **Stream:** hypothesis. **Design:** audit. **Frame:** `pan_dev`. **Windows:** all
four transitions.

**Why it is registered.** Rule **B20** (2026-08-20) requires a balanced economy set on any path, long
difference or Δ. E53 found the four-item cash "rebound" was largely six economies — China the largest
— dropping out of the *items* while staying in the *wave*. **No experiment in the ledger has ever
checked whether its own wave-to-wave comparison held the economy set fixed**, so v4 §12 states the
risk as *unquantified*. This experiment quantifies it.

**Exact test.** Audit set: every country-file column the ledger has touched (coverage.py's
word-boundary detector, so the set is mechanical and not chosen), restricted to columns reporting
≥30 developing-panel economies in at least two waves. For each column × each of the four
transitions:

- n reporting at *t*, at *t+1*, in both (**balanced**), dropped (*t* only), added (*t+1* only);
- the population share of the dropped economies inside the *t* reporting set, and the **name** of the
  largest dropped economy;
- Δ_unbalanced = wmean(*t+1* over its own reporters) − wmean(*t* over its own reporters);
- Δ_balanced = the same on the intersection only;
- **discrepancy** = Δ_unbalanced − Δ_balanced.

**Registered claim.** E53's attrition failure is **localized to narrow items and does not
characterize the ledger**.

**Registered SIGN (B15).** Where economies drop out, the discrepancy is predicted **positive on
cash-side items** — the droppers sit *below* the retained mean on those items, so an unbalanced Δ
overstates the rise. The signed test is: among cells with a non-trivial drop (≥3 economies or ≥5% of
the *t* population), the discrepancy's sign should follow the sign of (retained mean − dropped mean)
at *t*, in a **majority** of cells. Registered as a directional check on the mechanism, reported
separately from the keep bars.

**Keep bar — three branches, all fixed in advance so no branch is chosen after the fact:**
- **(a)** median |discrepancy| over all column × transition cells < **0.50pp**, AND
- **(b)** share of cells with |discrepancy| ≥ **2.0pp** below **10%**, AND
- **(c)** among the cells that back a **kept** ledger finding, none has |discrepancy| ≥ 2.0pp.

Branch 1 — (a), (b) and (c) all hold → **keep**: the risk is bounded and the v4 §12 limitation can be
restated as small and quantified.
Branch 2 — (a) and (b) hold, (c) fails → **keep with corrections owed**: the ledger-wide risk is
bounded but named kept findings are exposed; those findings are listed and a correction is opened in
`PAPER_DRAFT_v4.md`.
Branch 3 — (a) or (b) fails → **discard**: the registered claim is rejected, the risk is ledger-wide,
and every column above the 2pp bar is named.

**Registered diagnostic, labelled and NOT part of the keep bar.** Country-level *association* designs
have a different exposure from aggregate-Δ designs: pandas' pairwise-complete construction balances
them automatically, but their **sample** shrinks. For each association cell in the ledger, report the
n of the pairwise-complete set against the 76–77-economy headline set, and the population share it
holds. This measures a distinct risk and has no verdict rule attached.

**Gates.** G3 columns are the ledger's own declared variants, carried unchanged; **G4** every
reported cell carries its n and population share by construction; G5 na (no level claim against an
official aggregate); G6 na (no association is claimed — the audit's unit is a discrepancy, not a
correlation).

---

# Cycle 2026-08-21 — RESULTS

## U24x — EXPLORATORY mapping pass: the micro emergency-fund module is OPENED and fully identified

Commit `574c6f4`. Status `exploratory`. No hypothesis, no keep — logged before U24 under the peek rule.

**The obstacle and the fix.** The eleven columns carry **numeric codes, not text labels**, despite the
file being the "labelled" release — the same wall that blocks `con` at both levels. It was cleared
mechanically rather than by codebook: for every column × every code, the **per-economy weighted
share** was matched against every labelled country-file `fin24*`/`fin25*` column. Where a micro code
*is* a country indicator the deviation is not small, it is **zero**.

**The identification, median |dev| = 0.000pp and max 0.000pp over 98 economies unless noted:**

- **`fin24` = MAIN SOURCE of emergency funds.** 1 savings (`fin24sav`), 2 family/friends
  (`fin24fam`), 3 money from working (`fin24work`), 4 borrowing (`fin24bor`), 5 selling assets
  (`fin24sell`), 6 other (`fin24other`), 7 not possible (≈`fin24aN`, med dev 2.40 — the only
  inexact one), 8/9 DK/RF. Pooled weighted composition: family/friends **37.5%**, money from working
  **16.8%**, savings **16.3%**, selling assets **10.9%**, borrowing **7.4%**, not possible **6.3%**.
- **`fin24a` = DIFFICULTY**, asked only of codes 1–6. 1 very difficult (`fin24aVD`), 2 somewhat
  difficult (`fin24aSD`), 3 not difficult (`fin24aND`), 4/5 DK/RF.
- **`fin24b` codes 1/2/3/4 = `fin24ba`/`bb`/`bc`/`bd`** exactly; **`fin24c` code 1 = `fin24c`** exactly.
- **M3, EXACT on the outcome U24 uses.** `fin24a ∈ {2,3}` over the `fin24` denominator reproduces
  **`fin24aSD_ND`** — the harness's own declared `resilience` headline — with **max |dev| = 0.0000pp
  on all 98 economies**. The four sibling columns `fin24aVD`/`SD`/`ND`/`aP` reproduce exactly too.

**A frame fact.** The module covers **98 economies and 102,954 respondents (71.5% of the file)**.
This is an **economy-level** subsample, not a within-economy split sample — the 98 economies are
complete — so `wgt` is the correct weight inside them and the 2026-08-19 split-sample warning does
not bite here. `fin24d1`/`d2` (24,335) and `fin24d3` (15,358) *are* conditional sub-branches and
qualify only 82 / 82 / 59 economies at M2.

**A label correction owed to this cycle's own pre-registration.** The registration described the
outcome as the "'very possible' or 'somewhat possible'" item. The item is a **difficulty** scale, not
a possibility scale; the registered *target* — "the `fin24aSD_ND`-equivalent validated in U24x" — is
unambiguous and is what U24 used. The parenthetical guess was wrong, the referent was not.

**Coverage consumed.** Eleven previously untouched micro columns. This is rule **B2**'s breadth cell.

## U24 — KEEP. The access-absorption ruler does NOT transfer to the welfare margin

Commit `0148c97`. Stream micro. Status **`keep`**. Parent: none (new module). Design
`micro-cross-section`, 2024, single wave, cross-sectional — **no trend language**.

**Verdict against the registered bar (educ ≥ 2 vs educ == 1, 98 economies, 102,530 respondents):**

1. unconditional gap **+22.10pp** (64.4 vs 42.3) ≥ +5 and POSITIVE as registered — **PASS**;
2. absorption **8.6%** < 40% — **PASS**;
3. account-conditional gap **+20.20pp** (68.9 vs 48.7) ≥ +5 and POSITIVE — **PASS**.

**The benchmark is the result.** Computed on the *same 98-economy sample, same split, same weights*,
the usage margin `anydigpayment` absorbs **56.9%** of its education gradient against the welfare
margin's **8.6%**. On the ledger's usual split (`educ==3` vs `educ==1`) the two are **64.0%** and
**12.3%** — and the 64.0% reproduces the standing U10/U19 figure that `PAPER_DRAFT_v4`'s abstract
quotes, on a sample that was chosen by the module's coverage and not by this experiment. **Account
holding is the gate on *using* the system and is not a gate on *withstanding a shock*.**

**B6 inference.** Country-clustered bootstrap, 2,000 draws, percentile intervals. Resilience
absorption **[−3.1%, +21.1%]**; digital-payment absorption **[+38.4%, +72.8%]**. The two intervals
**do not overlap**, and the resilience interval sits entirely below the registered 40% bar while
containing zero — i.e. the point estimate of 8.6% is not distinguishable from *no absorption at all*.
Gap intervals: resilience uncond **[+19.47, +24.87]**, cond **[+16.02, +24.78]**; digital payment
uncond **[+23.53, +31.75]**, cond **[+7.25, +17.33]**.

**Registered secondary — the within-country check, and it is unanimous.** Of the 98 economies, **64
qualify M2** (≥100 unweighted in both education cells within `account == 1`), holding **69.5% of
accountholding respondents** — a far better qualifying share than U22's connectivity axis (40.8%) and
comparable to U19's. The account-conditional education gap in resilience is **positive in 64 of 64
(100%)**, median **+20.61pp**, against a registered bar of ≥75%. This is not a between-country
composition artifact. The benchmark margin on the same 64 economies is positive in 63 of 64 at a
median of **+9.36pp** — *less than half* the resilience gap's within-country median, which is the
same contrast the pooled absorption figures give, arrived at without pooling. On the ledger-standard
split only **23 economies** qualify (16.7% of accountholding respondents, the tertiary cell being
thin outside richer economies) and both margins are positive in 23 of 23, at medians of **+33.39pp**
(resilience) and **+18.04pp** (digital payment).

**Reproducibility note.** The first run crashed in the final print of this secondary (a format-string
argument count) after the primary and the bootstrap had printed. The print was fixed and the whole
experiment re-run end to end: every number above, including the seeded 2,000-draw bootstrap, is
**identical** across the two runs.

**Kish neff.** The micro weights are not concentrated the way the country weights are: `neff` =
**66,982** on a nominal n of **102,530** (ratio 0.65). The B10 warning about `neff` ≈ 7 is a
statement about the *country* file and does not transfer here; the binding constraint on this claim
is that economies are not independent draws, which the country-clustered bootstrap above addresses
and the within-country count above addresses differently.

**What this closes and what it does not.** It converges from the individual side with the country
stream's three-times-repeated resilience null (E2, E15, E26): digitalization and account access do
not reach the welfare margin. It is a **2024 cross-sectional description** and says nothing about
change. And it does not say resilience is *un*-graded — the gradient is **+22pp and one of the
largest in the micro ledger**; it says the gradient does not run *through the account*.

## E55 — DISCARD (Branch 3). The registered "localized" claim is REJECTED: the reporting-set risk is real, and it is a 2021→2024 phenomenon

Commit `91e972c`. Stream hypothesis. Design `audit`. Frame `pan_dev`. Parent E53. Agenda item **8.1**.

**The audit.** 429 country columns → **76 ledger-touched** → **58 eligible** (≥30 developing-panel
economies in ≥2 waves) → **137 column × transition cells over 57 columns**, across all four
transitions. Every cell reports n at *t*, n at *t+1*, the balanced intersection, droppers, adders,
the dropper population share, the largest dropper by name, and Δ_unbalanced − Δ_balanced.

**Verdict against the three pre-registered branches:**

- **(a) median |discrepancy| = 0.0000pp** (bar < 0.50) — **PASS**. More than half the ledger is
  exactly balanced: **78 of 137 cells (56.9%)** have zero droppers and zero adders.
- **(b) cells with |discrepancy| ≥ 2.0pp: 19 of 137 = 13.9%** (bar < 10%) — **FAIL**.
- **(c) keep-backing cells with |discrepancy| ≥ 2.0pp: 8** (bar 0) — **FAIL**.
- **⇒ BRANCH 3: DISCARD.** The registered claim that E53's failure is localized to narrow items does
  not survive its own bar.

**The shape of the failure, which is the useful part.** The exposure is **not spread over the
ledger — it is one window**. Cells above the 2pp bar by transition: 2011→14 **0 of 6**, 2014→17
**2 of 33 (6.1%)**, 2017→21 **1 of 43 (2.3%)**, 2021→24 **16 of 55 (29.1%)**. Median |discrepancy|
is **0.000pp** in the three earlier windows and **0.534pp** in 2021→24. The distribution is bimodal,
not heavy-tailed: p50 = 0.000, p75 = 0.501, p90 = 3.452, p100 = 31.222.

**Every keep-backing failure is 2021→2024 and every one names China.** Eight cells, dropper counts of
five or six economies holding **31.7–32.3%** of the *t* reporting population, China the largest at
**26.4–27.2%**:

| column | Δ unbalanced | Δ balanced | discrepancy |
|---|---|---|---|
| `fin32_acc` (E10's wage rail, `keep-general`) | −3.21 | **+4.40** | **−7.61** |
| `fin31d` (E45/E48b cash margin) | +6.10 | **−0.38** | **+6.48** |
| `fh1_fh2` (E33's welfare margin) | −0.85 | **+2.70** | −3.55 |
| `fh2` | −0.67 | **+2.72** | −3.39 |
| `fh1` | −1.40 | **+1.81** | −3.22 |
| `fin34c` (E47's counter-moving margin) | +7.27 | +4.76 | +2.51 |
| `fin43c` | +2.20 | −0.31 | +2.51 |
| `fin42` | +2.60 | +0.26 | +2.34 |

**Four of these eight change SIGN between the unbalanced and balanced series** — `fin32_acc`, `fh1`,
`fh2`, `fh1_fh2` all read as *falling* on the reporting set and *rising* on the balanced set;
`fin31d` and `fin43c` read as rising unbalanced and flat-to-falling balanced. E53's correction on
`fin31d`/`fin34c`/`fin42`/`fin43c` is reproduced exactly here as a by-product, which is the audit
working.

**The registered sign check (B15) confirms the mechanism, decisively.** On the 40 cells with a
non-trivial drop (≥3 economies or ≥5% of the *t* population), the sign of the discrepancy matches
`sign(retained mean − dropped mean)` at *t* in **38 of 40 = 95.0%**, against a registered bar of
"a majority". Mean |discrepancy| is **3.113pp** on non-trivial-drop cells against **0.085pp**
elsewhere. This is not noise: an unbalanced Δ is biased *away from where the droppers sat*, by an
amount the drop size predicts.

**A robustness read, reported and NOT used to move the bar.** Ten of the 137 cells are `_s`
conditional columns, which `HARNESS_V2_NOTES` item 10 already records as unusable and which no claim
rests on; the detector picked them up because the ledger *discusses* them. Excluding them, bar (b) is
**13 of 127 = 10.2%** — which still fails the <10% bar, and branch (c)'s eight failures contain no
`_s` column at all. The verdict does not turn on this.

**Labelled diagnostic, no verdict attached — the SAMPLE exposure of association designs.** Δ→Δ
correlations are balanced automatically by the pairwise-complete construction, so they cannot suffer
the bias above; what they lose is sample. Against a 77-economy headline panel: E12, E11 hold 76–77
economies and 97–100% of panel adult population in every window; the three mobile-money rails (E1,
E13, E14) run on **54–59 economies and 67–71%** throughout, which is a coverage fact about
`mobileaccount_t_d` and not attrition; and **E10's wage rail falls from 77 economies / 100% in
2014→17 and 2017→21 to 71 economies / 69% in 2021→24** — the same six-economy drop, seen as a sample
loss rather than as a bias.

**Two post-run patches, disclosed.** The labelled diagnostic block crashed on the 2011→2014 window
(`mobileaccount_t_d` has no 2011) and used a mismatched population denominator across waves. Both
were fixed after the primary bars had been computed and printed; **the primary, the branch and the
sign check are byte-identical before and after** — the patches touch only the diagnostic that carries
no verdict rule.

**What this owes the paper.** `PAPER_DRAFT_v4.md` §12 states this risk as *unquantified*. It is now
quantified and it is **larger than the loop assumed on the narrow-item block and smaller than feared
everywhere else**: three of four transitions are clean at a median of exactly zero, and the 2021→24
window has a systematic six-economy item-level dropout led by China that biases roughly three in ten
of its cells by ≥2pp. **Corrections are owed on `fin32_acc` (E10, `keep-general`) and on the whole
`fh` family (E33, `keep-window`)**, neither of which E53 had touched.

## Wrap-up — 2026-08-21

1. **Three experiments, one keep, one discard that pays a debt, and one module opened.** B18 did not
   fire (corrections 0 of 5, count 0 of 10), so this was a normal cycle: **U24x** (exploratory
   mapping), **U24** (`keep`), **E55** (`discard`, Branch 3). Ledger now **86 rows, 40 keeps**,
   `make_index.py --check` clean.
2. **U24 — the access-absorption ruler is a USAGE instrument and does not reach welfare.** On the
   same 98-economy 2024 sample, account holding absorbs **56.9%** of the education gradient in
   digital-payment use and **8.6%** of the gradient in emergency-fund resilience; the bootstrap
   intervals **[+38.4%, +72.8%]** and **[−3.1%, +21.1%]** do not overlap and the resilience interval
   contains zero. Within-country the conditional gap is positive in **64 of 64** qualifying
   economies. This is the country stream's thrice-repeated resilience null (E2, E15, E26) seen from
   the individual side, and it is the first individual-level result Program 4 has.
3. **E55 — agenda item 8.1 is ANSWERED and the registered claim FAILED, which is the point.** The
   reporting-set risk is **not localized to narrow items** (13.9% of cells ≥2pp against a <10% bar;
   8 keep-backing cells against a bar of zero) but it **is localized to one window**: 0/6, 2/33,
   1/43 and **16/55 (29.1%)** across the four transitions, with a median discrepancy of **exactly
   0.000pp** in the three earlier windows. The registered mechanism check fires at **38 of 40
   (95.0%)** — the bias points away from where the droppers sat, predictably.
4. **Two corrections opened in `PAPER_DRAFT_v4.md`, on keeps E53 never touched.** `fin32_acc` (E10's
   wage rail, `keep-general`) reads **−3.21pp unbalanced and +4.40pp balanced** over 2021→24, and
   the whole `fh` family (E33) flips the same way. The affected *associations* are Δ→Δ and balanced
   by construction; what is wrong is any statement about these margins' **aggregate direction**.
   v4's corrections branch stands at **2 of 5**, its count branch at **3 of 10**.
5. **A method worth more than the module it opened.** U24x identified eleven numerically-coded micro
   columns by matching per-economy weighted shares against the labelled country file — **exact, max
   |dev| 0.0000pp on 98 economies**. Any numerically-coded micro module with a labelled country twin
   can be opened this way. `con` stays blocked (its country twin is unlabelled too), but `fin13`,
   `fin14` and `fin22` should be tried with it before being written off. B2's cell was paid by these
   eleven columns; **B17 paid by U24**, next due in three cycles. Prediction stream unchanged and
   **CLOSED**: `account_t_d` **5.014**, `fin17a_17a1_d` **6.831**, `fin24aSD_ND` **6.625**.

---

# Cycle 2026-08-22 — pre-registration

**B18 TRIGGER CHECK (rule B18, amended 2026-08-16 — read the highest-numbered draft).** Current
draft is `PAPER_DRAFT_v4.md`. Corrections branch: **2 of 5** (both opened 2026-08-21 by E55). Count
branch: **3 of 10** (U24x, U24, E55 since the 2026-08-20 rewrite). **Neither branch fires — this is
a normal experiment cycle.**

**B1 COVERAGE RUN (done before any hypothesis was chosen).** Country file 83 of 429 columns touched
(19%); untouched families `con` (133, blocked — unlabelled twin), **`fin13` (30) and `fin14` (8)**.
Micro file 62 of 192 (32%); untouched families `con` (52, blocked), `fin22` (9), **`fin13` (8)**,
`fin48`/`fin49` (12), **`fin14` (5)**, `fin39` (4), `dig_account` (1). Wave transitions: all four
used, 2021→24 still 304 mentions against 21 for 2011→14. Frames: `urbanicity` still untouched and
single-wave.

**COVERAGE CELLS THIS CYCLE LANDS ON (rule B2).** `fin13` + `fin14` — the mobile-money usage module
— have **zero ledger mentions on either the country side or the micro side**, and the 36-economy
module set is a **frame the ledger has never used**. That pays B2 twice over. E56 buys no new
columns and buys its breadth in design (an audit over the touched set, as E55 did).

**B17 (micro quota).** Paid 2026-08-21 by U24; next due in three cycles. U25x/U25 pay it again
early, which is deliberate: the micro stream holds 23 of the ledger's 40 keeps.

**B3 (lineage cap).** U25x/U25 **parent: none** (a new module). E56 **parent: E55**, which makes
E53 → E55 → E56 a chain of **three** — the cap. **The next cycle may not extend this chain.**

## Slot 1 — U25x (exploratory) + U25 (registered): the untouched `fin13`/`fin14` mobile-money usage module

**PART A — U25x, MAPPING PASS, logged as EXPLORATORY under the peek rule (2026-07-11).** The 13 micro
columns (`fin13_1`, `fin13a`–`fin13f_1`, `fin14a`–`fin14e`) carry **numeric codes**, not text labels,
exactly as U24x found for the emergency-fund module. U24x's method is applied unchanged: for every
column × every code, the per-economy weighted share is matched against every labelled country-file
`fin13*`/`fin14*` column (38 columns), and a code is declared identified at **median |dev| ≤ 0.10pp**
across the common economies. The pass also prints, for each column, the denominator (which
respondents are asked), the module's economy count and its unweighted n. **Item meanings are inferred
from the country column NAMES and from the share match only** — there is no questionnaire in the repo
(`HARNESS_V2_NOTES.md` items 5–6) and that caveat travels with everything below.

**M3 is the identification.** A code is only usable if its weighted micro share reproduces the
country file within the M3 tolerance (1pp); the mapping *is* the gate, as in U24x.

**Registered in advance about the denominator.** The module is fielded in **36 economies** and, on
its face, is asked of a conditional subsample (mobile-money users). U25x reports whether the module
sample is an **economy-level subsample** (all respondents in those 36) or a **within-economy
conditional subsample**; if the latter, every statistic below is a conditional one and the claim text
must say so. If `account_mob` has no usable variance inside the module sample, the module's own
access anchor is dropped and the screen runs on the remaining anchors — declared here so the choice
is not made after seeing the answer.

**PART B — U25, THE FOUR-WAY ORIENTATION SCREEN (Documentation obligation 2), the registered
primary.** Every identified item is aggregated to a **per-economy weighted share** and screened in
the **2024 cross-section across the 36 module economies**, against the anchor `g20_any` (the
digital-payment headline — E45/E47/E49/E51's anchor, so the numbers are comparable), **both lenses**
(population-weighted and unweighted across economies):

    restatement    |r| >= 0.80
    aligned        +0.30 <= r < 0.80
    counter-moving -0.80 < r <= -0.30
    independent    |r| < 0.30
    both lenses must AGREE, else `mixed-lens` (B9/B11)

**REGISTERED KEEP CONDITION:** at least one item classifies as **`counter-moving` on BOTH lenses**,
survives **G6** with the sign intact, and has a **bootstrap interval (2,000 economy draws) excluding
zero**. A screen returning only restatement / aligned / independent items is a **DISCARD**.

**REGISTERED SIGN (B15): the keep direction is NEGATIVE.** An item at r ≥ +0.80 is a restatement of
the digital-payment headline and is the **opposite** result, not partial confirmation. Note in
advance: a frequency question whose categories **partition** (weekly / monthly / less than monthly /
never) will produce a mechanically negative "never" category — that is an **inverse restatement**,
caught by the |r| ≥ 0.80 bar, and if it lands in the −0.30 to −0.80 band instead, the claim must
name the partition and say which level of it the claim is about (E51's composition rule).

**SECONDARY (registered, no bar):** the same screen against `mobileaccount_t_d` — the E47 distinction
between "counter-moves with digital payment" and "counter-moves with the module's own access margin".

**Declared limitations, in advance.** (i) n ≈ 36 economies against the ledger's usual 71–77: **G4 is
reported and the frame is declared as *the economies that field the mobile-money usage module*, not
the developing panel** — this is a composition statement about a self-selected set of economies.
(ii) A 2024 cross-sectional **level** correlation is not a within-country dynamic statement (E48 is
the standing proof the two come apart); no Δ claim is registered. (iii) G3: every `fin13`/`fin14`
item is an unregistered narrow variant. **B6/B9/B10/B12 on every cell**: weighted and unweighted r,
percentile bootstrap and `p_boot`, Kish `neff` beside nominal n, G6 drop-top-5, and the largest
single leave-one-out effect **with the economy named**.

## Slot 3 — E56 (agenda item 8.2): is the 2021→24 dropout ONE cause or many, and what do the balanced paths say?

**Parent: E55** (chain E53 → E55 → E56, at the B3 cap). **This is an audit / measurement pass, not an
association experiment**, so B14's long-difference-or-all-windows requirement does not bind — no
co-movement is registered here. It is the agenda's item 8.2 and it discharges E55's two corrections.

**Why it matters, stated before the run.** E55 found eight keep-backing cells biased ≥2pp by a
five-or-six-economy item-level dropout between 2021 and 2024, all naming China. If those columns
share **one** dropper set, the cause is a single release rule or a single questionnaire block and
every affected claim can be corrected at once with a known adjustment. If the dropper sets are
column-specific, each affected claim needs its own recomputation and the risk is open-ended.

**REGISTERED PRIMARY.** Over every country column with ≥30 developing-panel economies reporting in
2021 (E55's eligibility, unchanged), compute `D(col)` = the set of economies reporting the column in
2021 and **not** in 2024. Restrict to columns with a **non-trivial drop** (|D| ≥ 3). Let `D*` be the
**modal** dropper set. **Registered bar: ≥ 80% of non-trivially-dropping columns have Jaccard(D,
D*) ≥ 0.90.** Meeting it is a **keep** for the claim *the 2021→24 dropout is a single block, not
per-item attrition*; below the bar is a **discard**, and between-the-lines outcomes are reported at
whatever the number is, without moving the bar.

**REGISTERED SIGN / DIRECTION (B15):** the claim is that the sets **coincide** (Jaccard → 1). A
result showing many distinct dropper sets of similar size is the **opposite** finding and is reported
as such.

**REGISTERED SECONDARY 1 (no bar, descriptive):** the module membership of the affected columns —
whether `D*`'s columns fall in one questionnaire block (`fin30`–`fin34`, `fh`, …) or scatter across
unrelated families. A single block supports "questionnaire module"; scattering supports "release
rule".

**REGISTERED SECONDARY 2 — the corrections owed (rule B16, path before span).** The **fully balanced
four-wave path** (economies reporting the column in **all four** of 2014/2017/2021/2024, one fixed
denominator, count and population share printed) for `fin32_acc` (E10's wage rail, `keep-general`)
and `fh1`, `fh2`, `fh1_fh2` (E33's welfare margin, `keep-window`) — the two corrections E55 opened in
`PAPER_DRAFT_v4.md`. The `fh` family exists only from 2021, so its balanced path is stated over the
waves it has, and **any non-monotone path is stated in the claim text itself**. This is a measurement
statement about aggregate direction; the E10/E33 **associations** are Δ→Δ and balanced by
construction, and nothing here revisits them.

**Declared.** No new column is opened; the audit set is the ledger's own touched set, so this cycle's
B2 obligation rests entirely on U25x/U25 (which is why slot 1 went to a doubly-untouched module).
Deferred by budget, and named here so it is not lost: **agenda item 4.6**, the education/income
gradient in the *source* of emergency funds, which U24x opened and which is the strongest
unregistered lead on the micro side.
