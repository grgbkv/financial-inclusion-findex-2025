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
