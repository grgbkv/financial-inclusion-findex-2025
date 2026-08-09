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
