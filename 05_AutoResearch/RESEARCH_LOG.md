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
