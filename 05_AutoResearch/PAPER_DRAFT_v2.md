# Access converges, use diverges: the 2021–2024 financial-inclusion episode in developing economies

**Working-paper draft v2 (2026-08-01).** Descriptive evidence from a pre-registered experiment
ledger over the Global Findex 2025 database (117-country balanced panel, 2011–2024) and the 2024
individual-level file (144,090 respondents, 140 economies).

**Status of this draft.** Every empirical statement below is traceable to a numbered, pre-registered
experiment in `findings.tsv` / `results_prediction.tsv`, run under the protocol in
`program_findex.md`. Nothing here is causal. Section 9 lists what is missing before submission —
principally statistical inference, which this draft does not yet have.

---

## Abstract

Between 2021 and 2024 formal saving in developing economies rose by 13.7 percentage points
(24.3% → 38.0% of adults), the largest movement of any financial-inclusion margin in the four wave
transitions Findex has measured since 2011, and it happened while account-ownership growth continued
to decelerate (+13.4pp in 2011–14, +4.6pp in 2021–24). We document four features of this episode
from a ledger of 50 pre-registered tests. First, within the window the surge is predominantly *new*
saving rather than a relabelling of informal saving: 77% of the formal gain appears in total saving,
and informal saving rose alongside it, fastest where formal rose fastest. Second, the surge
co-moves strongly with three digitalization margins — mobile-money adoption (weighted r = 0.72),
wage digitalization (0.79) and digital-payment use (0.37) — that are not reducible to one another
under mutual partialling, and it is not confined to Sub-Saharan Africa (SSA r = 0.92; rest of the
developing panel r = 0.68). Third, the surge is a *usage* phenomenon, not an *access* phenomenon:
account growth barely co-moves with it (r = 0.20), account levels converge across countries
(r = −0.30 between level and subsequent growth) while formal saving diverges (+0.48). Fourth, the
episode stops at the balance sheet. It extends to formal borrowing (r = 0.61 from the wage margin)
but not to self-reported ability to raise emergency funds, where three independent tests return
0.19, 0.03 and 0.29, and where the developing-panel aggregate is flat (54.7% → 54.5%). Individual-level
data for 2024 show why the access margin cannot carry the story on its own: conditioning on account
ownership absorbs only 64% of the education gap in digital-payment use, 58% of the income gap and
10% of the age gap, and the surviving education and income gradients are within-country regularities
(median within-economy gaps of +9.4pp in 63 of 64 economies and +5.7pp in 74 of 83), not
between-country composition. A companion forecasting exercise shows that simple population-weighted
shrinkage toward region and income-group basins reduces 2024 out-of-sample error against a
persistence baseline by 30% for formal saving and 10% for account ownership.

---

## 1. Introduction

The 2025 Global Findex release documents a large increase in formal saving in developing economies
between the 2021 and 2024 waves. This paper asks what that increase was made of, what moved with it,
and where it stopped.

The contribution is descriptive and it is deliberately bounded. We have no instrument, no policy
discontinuity and no within-country repeated observations of individuals; every association reported
here is a contemporaneous co-movement of country-level changes across a single three-year window.
What the paper offers instead is *discipline over a large hypothesis space*: 50 hypotheses were
pre-registered with a stated keep threshold before the answer was computed, every one — kept or
discarded — is logged with its effect size and gate results, and roughly half were discarded. Applied
cross-country work on Findex rarely reports its discards; the informative nulls in Section 6 are the
part of this paper we would most like readers to take.

The organising claim is a contrast between two margins. **Access is converging**: account ownership
grows fastest where it is lowest, its growth decelerates wave over wave, and it is now high enough in
much of the developing panel that further movement is bounded by ceiling. **Use is diverging**:
formal saving grew *fastest where it was already highest*, and the individual-level gradients in
digital-payment use that survive conditioning on account ownership are large, persistent and present
inside almost every economy we can measure them in. A decade of access policy has, on this reading,
substantially solved the entry problem and left an unequal usage problem behind it.

## 2. Data and method

**Country panel.** The Global Findex 2025 country file, restricted to the 117 economies observed in
all five waves (2011, 2014, 2017, 2021, 2024). The 2022 partial wave is merged into 2021 before any
computation. The developing subpanel (77 economies, excluding high-income) is the estimation frame
for every result in Sections 3–6. All aggregates are weighted by adult population; all correlations
are population-weighted. Table 1 gives the aggregate series.

**Individual data.** The 2024 microdata release (144,090 respondents, 140 economies), used only for
2024 cross-sectional description in Section 7. All statistics are survey-weighted. Under the data
licence no individual records are reproduced.

**Table 1 — Developing panel (77 economies), population-weighted % of adults**

| | 2011 | 2014 | 2017 | 2021 | 2024 |
|---|---|---|---|---|---|
| Account (any) | 42.3 | 55.7 | 65.2 | 70.7 | 75.3 |
| Financial-institution account | 42.3 | 54.7 | 63.6 | 68.0 | 71.0 |
| Mobile-money account | — | 3.9 | 8.1 | 18.1 | 27.9 |
| Any digital payment | — | 35.1 | 45.4 | 56.4 | 60.9 |
| Wages paid into an account | — | 12.0 | 14.4 | 19.6 | 16.4 |
| **Saved formally** | **17.6** | **22.2** | **21.0** | **24.3** | **38.0** |
| Saved any money | — | 53.1 | 43.6 | 42.4 | 53.0 |
| Saved, other method | — | 9.0 | 10.2 | 8.7 | 16.4 |
| Saved via a savings club | — | — | — | 5.3 | 14.4 |
| Borrowed formally | — | 15.7 | 15.6 | 22.6 | 23.2 |
| Borrowed any | — | 47.8 | 44.4 | 49.5 | 59.6 |
| Inactive account | — | 7.0 | 11.1 | 8.9 | 6.1 |
| Resilience (funds in 30 days) | — | — | — | 54.7 | 54.5 |

*Country coverage varies by indicator and wave; the wage series is computed on 77 economies through
2021 and 71 in 2024, so its aggregate decline (19.6 → 16.4) is partly compositional and is not
interpreted here. Mobile money is reported by 57–62 economies.*

**Table 2 — Change per wave transition, developing panel (pp)**

| | 2011→14 | 2014→17 | 2017→21 | 2021→24 |
|---|---|---|---|---|
| Account | **+13.4** | +9.5 | +5.4 | +4.6 |
| Saved formally | +4.6 | −1.2 | +3.3 | **+13.7** |
| Mobile money | — | +4.2 | +10.0 | +9.8 |
| Digital payment | — | +10.2 | +11.0 | +4.5 |

Table 2 states the paper's premise in two rows: account growth has decelerated monotonically for a
decade, and the 2021–24 formal-saving movement is roughly three times any earlier transition.

**Method and gates.** Each hypothesis was registered with a test and a keep threshold (default:
population-weighted |r| ≥ 0.30 for associations, ≥ 5pp for group differences) before computation.
Four automated gates applied: G3, the indicator variant must be declared against a registry of
headline/narrow variants; G4, minimum country and population coverage; G5, computed aggregates must
track the published official aggregates within tolerance; G6, an association must keep its sign when
the five largest-population economies are dropped. A judgment rule added after the fourth experiment
also discards associations that keep their sign but lose more than half their magnitude under that
jackknife. Individual-level claims additionally require an unweighted cell size of at least 100 (M2)
and, where a country-file equivalent exists, agreement with it within 1pp (M3).

The ledger contains **50 experiments: 26 keeps and 24 discards** (country level 12/16; individual
level 14/8).

## 3. The surge was mostly new saving, inside this window

If formal saving rose because existing informal savers moved across a mode boundary, the episode is a
composition shift and its welfare content is small. If it rose on top of unchanged informal saving,
it is new saving. The accounting separates the two.

Formal saving rose 13.7pp; total saving rose 10.6pp; **77% of the formal gain is visible in total
saving**, leaving at most 3.1pp — under a quarter — available for pure relabelling. The
population-weighted slope of the change in total saving on the change in formal saving is +0.72
(r = 0.75, n = 76); this is partly mechanical, since formal saving is nested inside total saving, and
is reported as context.

The non-mechanical test is the informal margin itself, which is not nested in the formal one. It did
not recede: other-method saving rose 8.7 → 16.4pp and its change co-moves *positively* with the
formal change (r = **+0.696**, n = 76). The registered hypothesis had been displacement (r ≤ −0.30);
it is rejected in sign as well as magnitude. Countries in the top tercile of formal-saving growth
(+17.3pp on average) added +4.6pp of other-method saving; the bottom tercile (+1.8pp) added +0.8pp.
The semiformal savings-club margin behaves identically (r = +0.531, n = 58), and its jackknife is
stable (retention 1.06) where the primary's is borderline (0.50) — the primary co-movement is
approximately half carried by the largest economies. (Experiment E27.)

**A decade-scale qualification, which we consider the most important caveat in the paper.** Table 1
shows total saving at 53.1% in 2014, 42.4% in 2021 and 53.0% in 2024, against formal saving of 22.2%,
24.3% and 38.0%. Over 2014–2024 the *total* saving rate is flat while the formal rate rises ~16pp —
which is the signature of relabelling, the opposite of the within-window verdict. Both statements can
hold: total saving fell sharply between 2014 and 2021 and the 2021–24 recovery restored the earlier
level with a much more formal composition. But it means the E27 result is a statement about the
2021–24 window and not about the decade, and the earlier transitions have not been tested. This is
the first item on the extension agenda (Section 10), and it also raises a comparability question
about the total-saving series between the 2014 and 2017 waves that we have not resolved.

## 4. What moved with it: three digitalization margins

The formal-saving change co-moves with three digitalization measures across the developing panel
(population-weighted, 2021→2024):

| margin | r | n | tercile gradient in Δ formal saving | jackknife |
|---|---|---|---|---|
| Mobile-money account (E1) | **+0.719** | 58 | +2.2 / +11.6 / +14.8pp | 0.72 → 0.80 |
| Wages into an account (E10) | **+0.791** | 71 | +3.2 / +10.9 / +13.6pp | 0.791 → 0.785 |
| Any digital payment (E12) | +0.370 | 76 | +2.8 / +16.7 / +14.4pp | 0.37 → 0.78 |

Two deflationary readings were tested and rejected on their own terms.

*It is not one region.* Mobile money is concentrated in Sub-Saharan Africa, and the G6 jackknife
guards against one-*country* stories, not one-*region* stories. Re-running E1's construction inside
each half of the panel gives r = **0.92** within SSA (n = 25) and r = **0.68** across the five other
developing regions pooled (n = 33), with monotone tercile gradients in both. The association is
markedly steeper inside SSA and unambiguously present outside it. (E22.)

*It is not one factor read three ways.* The digitalization margins move together — mobile money and
digital-payment growth correlate at 0.60 (E14) and FI-account and mobile-money account growth are
complements rather than substitutes (0.435, E13), so "leapfrogging" is not what this panel shows.
Under mutual partialling each margin retains an independent association with the saving change:
mobile money net of digital payments 0.51, digital payments net of mobile money 0.57 (E23); wage
digitalization net of digital payments 0.58 (E24). Holding all three against each other on the common
sample (n = 56) gives wage 0.43 > digital payments 0.38 > mobile money 0.30 — an ordering that
inverts the bivariate one, since mobile money has the largest raw and smallest independent
association.

**We would not defend that three-way ranking in print.** The three margins inter-correlate 0.60–0.75,
are measured on the same two survey waves, and plausibly share measurement error; with n = 56 and no
standard errors, the gap between 0.43 and 0.38 is not a result. The defensible claim from E23/E24 is
the weaker one: the co-movement is not reducible to a single margin. Partialling contemporaneous
changes decomposes co-movement; it identifies nothing.

## 5. Access converges, use diverges

Four results in the ledger, none of which was registered with this framing, converge on it.

1. **Account growth and saving growth barely co-move.** r = 0.198 (n = 76), below threshold and
   discarded as a hypothesis (E16). Whatever the surge rode on, it was not the extensive margin.
2. **Access converges.** The 2021 account level predicts subsequent account growth at r = −0.301
   (n = 77): lower-access economies grew faster (E17, benchmark arm).
3. **Formal saving diverges.** The same test on saving gives r = **+0.480** — economies that already
   saved more formally in 2021 gained *more* by 2024. The registered catch-up hypothesis is rejected
   in sign (E17).
4. **Usage intensity in 2021 predicts slower subsequent account growth** at a given account level
   (partial r = −0.595, n = 77; E5b) — consistent with an accounts-first pattern in which access ran
   ahead of use. We flag this one as weak: its jackknife magnitude collapses to −0.114, so it is
   substantially a large-economy pattern and should be read as such.

The account series in Table 2 is the backdrop: +13.4, +9.5, +5.4, +4.6pp across the four transitions,
with the developing panel at 75.3% and the full panel at 78.9% in 2024. Access growth is decelerating
into a ceiling while the depth margin has just posted its largest movement on record.

## 6. Breadth and boundary: what the episode did and did not reach

**It is not saving-specific.** Formal borrowing deepened alongside formal saving (r = 0.403, E11), and
the wage margin co-moves with the borrowing change at r = 0.605, retaining 0.419 net of the saving
channel (E25). On the three-margin common sample every digitalization measure correlates with
borrowing (0.51–0.65) about as strongly as formal saving itself does. Saving and borrowing look like
two faces of one balance-sheet deepening.

**It shifted the composition of emergency funds.** Where formal saving surged, savings became a
larger reported source of emergency funds (r = 0.541; dev-panel aggregate 17.9 → 20.3pp, E7). But it
did *not* displace borrowing as a source (r = +0.069; E18) — the sources expanded together.

**It did not reach self-reported resilience.** This is the paper's sharpest null and it is
triangulated three ways, each pre-registered separately:

| test | r | n |
|---|---|---|
| Mobile money → resilience (E2) | +0.189 | 58 |
| Formal saving → resilience (E15) | +0.031 | 76 |
| Wage digitalization → resilience (E26) | +0.294 | 71 |

E26 missed its 0.30 threshold by 0.006 and is logged as a discard on that basis; notably its
jackknife *strengthened* to 0.407, so the weak association is not a large-economy artifact. On an
identical n = 56 sample the destinations form a clean ladder:

| margin | → saving | → borrowing | → resilience |
|---|---|---|---|
| Wages into an account | +0.804 | +0.649 | +0.295 |
| Any digital payment | +0.747 | +0.512 | **+0.000** |
| Mobile money | +0.713 | +0.543 | +0.208 |

Digitalization co-moves strongly with where money is held (~0.75) and where credit comes from
(~0.57), and an order of magnitude more weakly with reported capacity to absorb a shock. The
developing-panel resilience aggregate is flat over the window (54.7 → 54.5), which compresses the
variance available and works against detection; the measure is a self-reported hypothetical, and the
2021 wave was fielded under pandemic conditions. With those caveats stated, three independent tests
agree, and we report the null as the substantive finding it is.

**Two further nulls worth recording.** Gender-gap closure over the window is essentially orthogonal to
mobile-money growth (r = 0.008, E3), despite substantial cross-country variation in gap changes
(sd 7.4pp). And the within-country income gap in formal saving did not widen in proportion to the
surge (r = 0.179, E20), nor on a scale-free log-odds formulation (mean +0.109 in odds terms, below
the registered bar, E21). The surge was neither systematically pro-poor nor systematically
regressive in this window.

## 7. Individual-level evidence: how much does access absorb?

Section 5's country-level claim — that the binding margin is now use, not entry — has an individual
counterpart that can be measured directly in the 2024 cross-section. For each demographic dimension
we compute the unconditional gap in digital-payment use, the gap conditional on holding an account,
and the implied share of the unconditional gap that the access margin absorbs.

**Table 3 — Digital-payment use, 2024 (144,090 respondents; weighted %, pp gaps)**

| dimension | unconditional gap | conditional on account | absorbed by access |
|---|---|---|---|
| Education (tertiary − primary) | +46.7 | **+16.8** | 64% |
| Income (q5 − q1) | +27.3 | **+11.5** | 58% |
| Labour force (in − out) | +20.8 | **+9.6** | 54% |
| Age (26-35 − 65+) | +11.6 | **+10.3** | **10%** |
| Urbanicity (urban − rural) | +11.0 | +3.7 | 66% |
| Gender (male − female) | — | +3.4 | — |

(U10, U17, U18, U15, U16, U6.) Two readings follow. Access absorbs a majority of the education,
income, employment and urbanicity gaps but leaves large residuals for the first three; it absorbs
almost none of the age gap, which is therefore a *usage* phenomenon end to end. Gender and
urbanicity fall below the 5pp threshold conditional on access and were discarded as claims — the
gender gap in this data is an access-margin phenomenon, and once inside, women and men use digital
payments at nearly the same rate (86.8 vs 83.4). The same holds for the gender gap in account
ownership across income quintiles, which is flat (5.2pp in q1 vs 5.7pp in q5, U1).

**The access margin itself is steeply graded**: account ownership runs 51.9 / 77.7 / 93.4% across the
three education levels (U7) and 61.7 vs 76.7% by labour-force status (U13). Formal saving among all
adults runs 12.0 / 22.6 / 46.2% by education (U4), and among wage-receiving accountholders, digital
wage receipt runs 56.6 / 80.6 / 91.9% (U14).

**These gradients are within-country, not composition.** The obvious objection to any pooled
cross-economy gradient is that it could be produced entirely by low-education or low-income adults
living in low-digitalization economies. We tested the two largest axes by computing the conditional
gap separately inside every economy with at least 100 unweighted respondents in both cells:

| axis | median within-economy gap | positive in | pooled | composition wedge |
|---|---|---|---|---|
| Education (secondary+ − primary) | **+9.4pp** | 63 of 64 economies | +12.1 | +2.7pp (22%) |
| Income (richest-40 − poorest-40) | **+5.7pp** | 74 of 83 economies | +7.9 | +2.2pp (28%) |

On the like-for-like contrasts the within-country medians are +18.0pp (tertiary vs primary, positive
in 23 of 23) and +9.7pp (q5 vs q1, positive in 30 of 33), against pooled figures of +16.8 and +11.5.
Composition contributes little and in the education case nothing at all. (U19, U20.) The income axis
is the thinner of the two: only 54% of qualifying economies clear 5pp on the coarse contrast.
Four axes — age, gender, urbanicity, employment — remain untested on this dimension.

**Barriers among the unbanked** are graded by education and income but not by cost or distance.
Documentation is cited by 54.2% of primary-educated unbanked adults against 46.0% of tertiary
(U9); "not enough money" by 35.7% of the poorest quintile against 25.3% of the richest (M1). Cost is
flat across income (23.7 / 22.8 / 24.1 / 23.1 / 23.3, U12) and distance is flat across
rural–urban (36.0 vs 36.8, U5) — two supply-side barriers that the demand-side literature often
expects to bind hardest for exactly the groups where they do not.

*Caveats specific to this section.* Conditioning on account ownership conditions on an outcome, so
the "absorbed" shares are a decomposition of observed rates and not a mediation estimate. Pooled
statistics weight economies roughly equally rather than by population. Single cross-section: no
statement here is a trend.

## 8. Forecasting as a discipline check

A parallel exercise asked how much of the 2024 cross-section is predictable from history ≤2021, with
2024 quarantined inside the evaluator. Persistence (2024 = 2021) gives mean absolute errors of 5.58pp
for account ownership, 6.68pp for resilience and 9.77pp for formal saving. Adding a damped trend for
saving and then shrinking each country toward its region, income-group and indicator-tercile basin
means (10% per stage) gives **5.01 / 6.63 / 6.83pp**.

Three lessons transfer to the descriptive sections. (i) The saving surge is not extrapolable: a model
fitted to the calm 2017→2021 transition mis-predicts it (P3, P10), which is direct evidence that
2021–24 is a regime break rather than a continuation — and therefore that Section 3's window
qualification matters. (ii) Shrinking toward *population-weighted* basin means beats an unweighted
median decisively (P22), and a population-weighted median is preferred by the training-window CV but
does not improve the holdout (P23): large economies carry genuine signal about their neighbours here,
which is worth setting against the jackknife scepticism applied throughout Sections 4–6. (iii) Four
times now, a selection made on the pre-2021 window has failed to transfer to 2021–24 (P8, P9, P13,
P23). Model selection on this panel is not stable across the surge boundary.

## 9. What this draft does not have

Stated plainly, in the order a referee will raise them.

1. **No inference.** No standard errors, no p-values, no multiple-testing correction across 50 tests.
   The 0.30 threshold is a convention, not a test. Worse, population-weighted correlations on 76
   countries where five economies carry much of the weight have an effective sample size closer to
   15–25 than 76. Bootstrap intervals and Kish effective-n are the first thing to add; false keeps at
   this threshold are likely.
2. **One window.** Every country-level result except two uses 2021→2024. Three earlier transitions
   are available and untested. Section 3 already shows this is not a formality.
3. **The 2021 base wave.** Fieldwork conditions and survey mode changed for many economies during the
   pandemic. Every change reported here differences against that wave.
4. **Contemporaneous changes only.** No lag structure anywhere, so no temporal ordering claim is
   available, only co-movement.
5. **Collinear regressors.** Section 4's partials are between measures correlating 0.60–0.75 with
   shared measurement error.
6. **Weighting.** Population weighting is doing substantial work; unweighted replications are not
   reported. The G6 jackknife is a partial substitute at best, and one headline (E27's primary) sits
   exactly at its retention boundary.
7. **Micro design.** Survey design (PSU, strata) is not used, so any future standard errors will be
   understated unless it is; pooled weighting treats economies as roughly equal.
8. **No external covariates.** Nothing outside Findex enters — no GDP, no connectivity, no
   regulation — so competing explanations cannot be held constant.

## 10. Extension agenda

In priority order, and each stated as a testable design rather than an aspiration:

1. **Replicate Sections 4–6 on the 2011→14, 2014→17 and 2017→21 transitions.** Determines whether the
   digitalization–deepening structure is a regularity or an artifact of one episode, and resolves the
   decade-scale saving question raised in Section 3.
2. **Add inference:** bootstrap intervals, effective sample size, and false-discovery control across
   the ledger; unweighted replication of every headline.
3. **Exploit the demographic-group panel.** The country file carries gender, age, education,
   labour-force, income and urbanicity slices for all five waves — a 13-year within-country
   inequality panel that this draft uses only in two experiments. The natural question is whether
   inclusion gaps follow an inverted-U against the access level: widening while adoption is early and
   elite-led, narrowing as it saturates.
4. **Reopen the welfare margin.** Section 6's boundary rests on one self-reported measure. The
   financial-health items are available for 2021 and 2024 on 90 economies and have not been touched.
5. **Test the connectivity prerequisite.** Internet access is available for 2024 at country and
   individual level; the rails results in Section 4 currently have no answer to the objection that
   they proxy connectivity.
6. **Lagged designs.** Whether the level of one margin predicts subsequent growth of the next —
   account → payments → saving → credit — is testable across five waves and would upgrade the
   evidence from co-movement to temporal ordering.
7. **The consumer-protection module.** The 2024 file carries an extensive fraud, trust and
   digital-risk module, entirely unused here, which is the natural place to look for the downside of
   the episode this paper documents.

---

## Appendix A — experiment ledger

All 50 experiments, with verdicts, are in `findings.tsv` (country level and individual level) and
`results_prediction.tsv` (forecasting), and every pre-registration and verdict is in
`RESEARCH_LOG.md` in chronological order. Summary:

| stream | keep | discard | total |
|---|---|---|---|
| Country level (E-series) | 12 | 16 | 28 |
| Individual level (U-series) | 14 | 8 | 22 |
| Forecasting (P-series) | 10 adopted | 13 reverted | 23 |

The forecasting count is by experiment (P1–P23); `results_prediction.tsv` logs one row per
experiment × target, so its 13 keep / 16 discard rows include per-target outcomes of the same
experiment and the three persistence baselines.

Discards used in this paper as substantive findings: E2, E3, E15, E16, E17, E18, E20, E21, E26, E27,
U1, U5, U6, U8, U12, U16.
