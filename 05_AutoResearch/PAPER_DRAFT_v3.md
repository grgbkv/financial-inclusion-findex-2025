# A balance-sheet window: formal saving, digital rails and resource-graded use in developing economies, 2021–2024

**Working-paper draft v3 (2026-08-16).** Descriptive evidence from a pre-registered experiment
ledger over the Global Findex 2025 database (117-economy balanced panel, 2011–2024) and the 2024
individual-level file (144,090 respondents, 140 economies).

**Status of this draft.** v3 replaces v2 (2026-08-01) in full. Every empirical statement is traceable
to a numbered, pre-registered experiment in `findings.tsv` / `results_prediction.tsv`, run under the
protocol in `program_findex.md` and indexed one line per experiment in `LEDGER_INDEX.md`. Nothing
here is causal. Unlike v2, this draft has an inference layer (Section 10) and it is unflattering.

**CORRECTIONS OWED: none outstanding.** v2's seven-item block is executed here and is reproduced as
Appendix B, item by item, with the section that discharges each. The next distillation trigger (rule
B18) reads *this* file.

---

## Abstract

Between 2021 and 2024 formal saving in developing economies rose 13.7 percentage points (24.3% →
38.0% of adults), the largest movement of any financial-inclusion margin in the four wave transitions
Findex has measured since 2011. We document what that episode was made of, what moved with it, and
where it stopped, from a ledger of 73 pre-registered tests of which 37 were discarded.

Four findings. **First**, within the window the surge is predominantly *new* saving rather than a
relabelling of informal saving: 77% of the formal gain appears in total saving, and informal saving
rose alongside it, fastest where formal rose fastest (r = +0.696, n = 76); the registered
displacement hypothesis is rejected in sign. **Second**, the window is a *balance-sheet* window, not
a digital-inclusion one. Each margin has its own peak transition — account ownership 2011→14, digital
payments 2014→17, saving and borrowing 2021→24 — and 2021→24 is digital payments' **weakest** window,
with 21.1% of economies gaining ≥10pp against 42.1% for saving and 52.6% for borrowing. The
digitalization margins that co-move with the surge were themselves decelerating in the window where
the correlation is measured. **Third**, six bivariate co-movements between saving and digitalization
margins replicate across transitions and one — account growth with formal-saving growth — holds in
all four (unweighted +0.361 to +0.555, every bootstrap interval excluding zero); every *partial*, and
every *level-to-change* design in the ledger, failed replication. **Fourth**, individual-level 2024
data show conditioning on account ownership absorbs 64% of the education gap in digital-payment use,
58% of the income gap and 10% of the age gap, and the surviving education and income gradients are
within-country regularities (median within-economy gaps +9.4pp in 63 of 64 economies and +5.7pp in 74
of 83), not between-country composition.

Two methodological results govern how all of the above should be read. Across thirty-three
association tests spanning six designs, Benjamini–Hochberg at q = 0.10 rejects **26 of 33** on nominal
n and **1 of 33** on the Kish effective n; median `neff` is **7.2** against a median nominal n of 71.
And the population weighting decides the keep/discard boundary in both directions at roughly one case
per handful of tests, so every association here is reported under two lenses. These are descriptive
regularities on about seven effective observations, and no significance language is attached to any
of them.

---

## 1. Introduction

The 2025 Global Findex release documents a large increase in formal saving in developing economies
between the 2021 and 2024 waves. This paper asks what that increase was made of, what moved with it,
and where it stopped.

The contribution is descriptive and deliberately bounded. There is no instrument, no policy
discontinuity and no within-country repeated observation of individuals; almost every association
reported here is a co-movement of country-level changes. What the paper offers instead is *discipline
over a large hypothesis space*: 73 hypotheses were registered with a stated keep threshold before the
answer was computed, every one — kept or discarded — is logged with its effect size, gate results,
both weighting lenses and its effective sample size, and 37 were discarded. Applied cross-country
work on Findex rarely reports its discards; the informative nulls in Sections 7 and 9 are the part of
this paper we would most like readers to take.

**What changed from v2, stated up front.** v2 organised itself around a slogan — "access converges,
use diverges" — and around a decomposition of the saving surge into three separate digitalization
rails. Fourteen subsequent experiments broke both. The slogan holds on the *resource* axes (income,
education) and fails on cohort and sex, where the usage gap narrowed too. The rail decomposition
failed replication on the previous transition, because the rails were nearly collinear there. And the
window itself turned out to be misdescribed: it is the window in which the *balance sheet* moved,
while the digital margins that correlate with it were slowing down. v3 is organised around what
survived that, which is less than v2 claimed and better supported.

## 2. Data and method

**Country panel.** The Global Findex 2025 country file, restricted to the 117 economies observed in
all five waves (2011, 2014, 2017, 2021, 2024). The 2022 partial wave is merged into 2021 before any
computation. The developing subpanel (77 economies, excluding high-income) is the estimation frame
for every result in Sections 3–9 unless stated; the high-income complement (40 economies) is used
once, in Section 3, as a placebo frame.

**Individual data.** The 2024 microdata release (144,090 respondents, 140 economies), used only for
2024 cross-sectional description in Section 8. All statistics are survey-weighted. Under the data
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
interpreted. Mobile money is reported by 57–62 economies.*

**Table 2 — Change per wave transition, developing panel (pp)**

| | 2011→14 | 2014→17 | 2017→21 | 2021→24 |
|---|---|---|---|---|
| Account | **+13.4** | +9.5 | +5.4 | +4.6 |
| Saved formally | +4.6 | −1.2 | +3.3 | **+13.7** |
| Mobile money | — | +4.2 | +10.0 | +9.8 |
| Digital payment | — | +10.2 | +11.0 | +4.5 |

**Method and gates.** Each hypothesis was registered with a test, a predicted **sign** and a keep
threshold (default: |r| ≥ 0.30 for associations, ≥ 5pp for group differences) before computation.
Four automated gates apply: G3, the indicator variant must be declared against a registry of
headline/narrow variants; G4, minimum country and population coverage; G5, computed aggregates must
track published official aggregates within tolerance; G6, an association must keep its sign when the
five largest-population economies are dropped. A judgment rule added after the fourth experiment also
discards associations that keep their sign but lose more than half their magnitude under that
jackknife. Individual-level claims additionally require an unweighted cell size of at least 100 and,
where a country-file equivalent exists, agreement with it within 1pp.

**Four rules adopted after v2 that change what may be claimed.** They are stated here because most of
the differences between v2 and v3 follow mechanically from them.

1. **Two lenses, always.** Every association reports its population-weighted and unweighted
   correlation. The weighted statistic describes the typical *person*; the unweighted one the typical
   *economy*. Neither is the correct lens, and where they disagree against the threshold the finding
   is logged `keep-weighted` / `keep-unweighted` / `discard-weighted` and the dependence is part of
   the claim.
2. **Effective n beside nominal n.** Every association carries its Kish effective sample size,
   `neff = (Σw)²/Σw²`, and no significance language is attached to nominal n.
3. **Name the economy.** A jackknife on the five largest economies is reported alongside the largest
   *single* leave-one-out effect and the economy responsible, because "five economies decide it" is a
   hypothesis about a cell and not a property of the frame.
4. **A scale-free twin on every between-group comparison in percentage points.** Gaps, differences
   and ratios of pp changes all inherit the same arithmetic artifact while both groups sit below 50%,
   and where the log-odds twin disagrees the pp version is the artifact. This trap sprang three times
   in the ledger before it became a rule.

**Ledger size.** 73 experiments: 50 country-level (22 keeps) and 23 individual-level (14 keeps), plus
28 forecasting experiments in a separate stream.

## 3. What the surge was made of, and whether the decade series can be read at all

If formal saving rose because existing informal savers moved across a mode boundary, the episode is a
composition shift and its welfare content is small. If it rose on top of unchanged informal saving, it
is new saving.

**Within the window, it is new saving.** Formal saving rose 13.7pp and total saving rose 10.6pp, so
**77% of the formal gain is visible in total saving**, leaving at most 3.1pp available for pure
relabelling. The non-mechanical test is the informal margin, which is not nested in the formal one:
other-method saving rose 8.7 → 16.4pp and its change co-moves *positively* with the formal change
(r = +0.696, n = 76). The registered hypothesis had been displacement (r ≤ −0.30) and is rejected in
sign as well as magnitude. Economies in the top tercile of formal-saving growth (+17.3pp) added
+4.6pp of other-method saving; the bottom tercile (+1.8pp) added +0.8pp. The semiformal savings-club
margin behaves identically (r = +0.531, n = 58) and its jackknife is stable (retention 1.06) where
the primary's sits on the boundary (0.50) — the primary co-movement is approximately half carried by
the largest economies. (E27.)

**v2 called the decade-scale reading "the most important caveat in the paper". It has since been
tested, and the caveat is smaller than v2 thought.** Total saving reads 53.1 (2014), 43.6 (2017),
42.4 (2021), 53.0 (2024), so a 2014→2024 difference is flat while formal saving rises ~16pp — the
signature of relabelling, opposite to the within-window verdict. The question was whether the
2014→2017 fall is a real decline or a definitional break in the instrument. Five diagnostics were
registered with the verdict rule fixed in advance; the rule returns **inconclusive** (1 of 3 pass),
but two of the three failures are failures *of the definitional hypothesis*:

- Under the **same questionnaire**, high-income economies **rose** in the same window (+1.65pp
  weighted, with only 45.0% of them falling against a 70% bar).
- The developing series **returns to 53.0 in 2024, 0.1pp from its 2014 value**, after passing through
  43.6 and 42.4. An instrument does not un-break itself.

**Read the decade series on this margin as continuous.** What the passing diagnostic adds, and no
write-up should drop: **90.2% of the 2014→17 drop sits in the non-formal residual** (Δformal −0.91pp
against Δresidual −8.36pp); per economy, total saving falls in 62.3% but formal in 49.4%. Whatever
happened in 2014→17 happened to saving *outside* financial institutions. The design cannot separate a
real informal-saving contraction from a change in how non-formal channels were enumerated, and does
not pretend to. (E46. The high-income panel used as the placebo frame has 40 economies and `neff`
9.2 — the highest in the ledger, precisely because it excludes the giant economies — but only 5
economies reporting this margin in 2024, so it supports early-wave contrasts and not 2024 ones.)

## 4. What kind of window this was

**v2 described 2021–24 as a digital-inclusion episode. That is wrong, and the correction is the
single largest change in this draft.** Measuring each margin's biggest transition by the unweighted
share of economies gaining ≥10pp — a within-country statistic, immune to the weighting critique that
sinks aggregate comparisons — every margin peaks in a *different* window:

| margin | peak transition | share of economies ≥ +10pp in 2021→24 |
|---|---|---|
| Account ownership | 2011→14 | — |
| Digital payments | 2014→17 | **21.1%** (its weakest window) |
| Formal borrowing | 2021→24 | **52.6%** |
| Formal saving | 2021→24 | **42.1%** (previous best 20.8%) |
| Merchant payments | — | 26.3% |

The saving episode is genuinely a within-country episode and not an aggregate artifact: 42.1% of
economies gained ≥10pp against a previous best of 20.8%, it has the largest unweighted median of the
four windows, and G5 agreement with published aggregates holds at 1.7pp. But it sits beside an
*even larger* borrowing episode, and beside digital payments' slowest three years on record. (E39.)

**The reframing passed an out-of-sample check.** Merchant payments — an untouched column, chosen
*after* the balance-sheet reframing had been written — sorts with the digital rails at 26.3% rather
than with the balance sheet. A margin picked to test the new frame landed where the new frame
predicted. (E41; the column reads 35.1 → 39.4pp population-weighted, unweighted median 13.1 → 20.2,
n = 76.)

**The consequence for Section 5, which must be carried with every sentence of it:** the digitalization
margins that co-move with the saving surge were themselves *decelerating* in the window where the
co-movement is measured. Any reading in which digital rails drove the surge has to explain why the
rails were slowing while the thing they supposedly drove was posting a record.

## 5. What moves with the surge: six bivariates, and nothing finer

**The six co-movements that replicated.** Each was registered on 2021→24 and then re-run on earlier
transitions; each is reported weighted / unweighted.

| pair | 2021→24 | earlier window | status |
|---|---|---|---|
| Mobile money ~ formal saving (E1) | +0.719 | +0.454 | `keep-general` |
| Wages into account ~ formal saving (E10) | +0.791 | +0.678 | `keep-general` |
| Digital payments ~ formal saving (E12) | +0.370 | +0.685 | `keep-general` |
| Formal borrowing ~ formal saving (E11) | +0.403 | +0.616 | `keep-general` |
| FI account ~ mobile-money account (E13) | +0.435 | — | `keep-general`, **flagged** |
| Mobile money ~ digital payments (E14) | +0.600 | +0.871 | `keep-general` |

**E13 is flagged and may not be used as a headline:** it fails the unweighted lens in *both* of its
windows (+0.188 and +0.248), so the complementarity reading — that mobile-money and bank accounts
co-develop rather than one leapfrogging the other — rests on the population weighting twice over.

**It is not one region.** Mobile money is SSA-concentrated, and the G6 jackknife guards against
one-*country* stories, not one-*region* stories. Re-running E1's construction inside each half gives
r = **0.92** within SSA (n = 25) and **0.68** across the five other developing regions pooled
(n = 33), with monotone tercile gradients in both. This cell is also, on the inference in Section 10,
**the only one of thirty-three that survives multiple-testing correction at the true degrees of
freedom** — precisely because excluding the giant economies raises `neff` to 9.5. (E22.)

**The one association that holds in all four transitions.** Account-ownership growth and formal-saving
growth co-move at **+0.470 / +0.361 / +0.394 / +0.555 unweighted** across 2011→14, 2014→17, 2017→21
and 2021→24, every bootstrap interval excluding zero, and at **+0.431 / +0.736 / +0.641 / +0.198**
weighted — clearing the threshold in three of four windows there too. This is the ledger's
best-supported country-level regularity and v2 did not contain it, because in the single window v2
looked at, the weighted statistic reads +0.198 and the hypothesis was discarded. **Dropping China
alone moves that cell from +0.198 to +0.726; dropping India, with almost the same population weight,
moves it to +0.273.** It was never a weak association; it was a strong one measured in the one window
where one economy cancels it. (E42, `keep-general-unweighted`.)

**v2's three-separate-rails decomposition is withdrawn as a general claim.** The three partials
(mobile money net of digital payments +0.509; digital payments net of mobile money +0.583; wage
digitalization net of digital payments +0.605) **do not replicate on 2017→2021 — 0 of 3** — and the
mechanism is legible: r(Δ mobile money, Δ digital payments) is **+0.871** in 2017→21 against +0.600
in 2021→24. The rails were nearly collinear in the earlier window and there was no independent
variation left to partial. The decomposition describes the window in which the rails **decoupled**,
and is reported here as a window property with no generality claimed. (E23/E24/E25, failed by E35.)

**A design-level result that deserves its own line.** Across the whole ledger, **seven level-to-change
experiments have produced zero keeps**, and the reason has been measured directly: the Spearman
correlation between an economy's change in one window and its change in the next is **≤ +0.07 in all
ten pairs tested and negative in eight** (formal saving −0.413 / −0.350 / +0.070). Country-level
wave-to-wave change is dominated by wave-specific variation. Nothing observable at *t* predicts the
size of the next move. This single fact explains the failed partials, the failed lagged designs, and
the forecasting result in Section 11, and it is why a single adjacent-window Δ→Δ correlation is no
longer admissible as a primary anywhere in this project.

## 6. Who the surge reached

**It reached every demographic half — in this window.** Across the five usable demographic slices of
the country panel (income, education, age, labour force, gender), the disadvantaged half gained
formal saving in every one: weighted Δ **+7.4 to +16.0pp**, with 29.1–56.4% of economies delivering
≥+10pp to the disadvantaged group against E39's 42.1% all-adults reference. **The young are the only
slice to out-gain their counterpart** (+16.0 vs +14.2). (E43, `neff` 5.6.)

**It does not replicate, and the failure is instructive rather than damning.** The same bars run
verbatim on all three earlier transitions clear in **0 of 5, 0 of 5 and 1 of 5** dimensions. The
failure is one of *magnitude*, declared in advance: the level bar is nearly met everywhere (+4.49 to
+6.41pp across slices), while the breadth bar — 25% of economies delivering ≥+10pp to the
disadvantaged half — is missed everywhere (0.0–36.8%). Section 4 already established 2021→24 as the
largest within-country saving episode of the four; **there was no earlier episode of that size for
the breadth question to be asked of.** E43 stays a window claim and is on record as having *failed*
its promotion test, which is a stronger statement than "not yet attempted". No further replication of
it should be registered. (E44. Note the slice frame covers only 27 / 34 / 38 economies in the three
earlier transitions against 55 in 2021→24, at `neff` 4.2 / 4.6 / 4.8 — these windows are thin in this
frame in a way the all-adults frame is not.)

**Nobody should write "the surge was regressive."** A registered percentage-point gap statistic showed
the income, education and labour-force gaps widening in roughly three economies out of four, surviving
both the jackknife and de-weighting — and its scale-free log-odds twin showed **no systematic widening
at all**, with income at a 52.7% coin flip. Levels rose from a low base almost everywhere in this
window, and under those conditions a pp gap widens arithmetically. This is the third instance of the
same trap in the ledger, which is why the log-odds twin is now mandatory. (E43 secondary; the same
artifact appeared in E21 and again in a ratio-of-changes statistic registered in good faith as
scale-relative.)

## 7. Where the episode stops: a measure comparison, not a boundary

**v2 called this "the paper's sharpest null" and claimed the episode stops at the balance sheet. That
overstated it in two separate ways, and the claim is demoted here to a comparison between measures.**

The self-reported resilience measure — ability to raise emergency funds in 30 days — does not move
with any digitalization margin:

| test | r (weighted) | n |
|---|---|---|
| Mobile money → resilience (E2) | +0.189 | 58 |
| Formal saving → resilience (E15) | +0.031 | 76 |
| Wage digitalization → resilience (E26) | +0.294 | 71 |

On an identical n = 56 sample the destinations form a clean ladder — digitalization co-moves with
where money is held (~0.75) and where credit comes from (~0.57), and an order of magnitude more
weakly with reported capacity to absorb a shock:

| margin | → saving | → borrowing | → resilience |
|---|---|---|---|
| Wages into an account | +0.804 | +0.649 | +0.295 |
| Any digital payment | +0.747 | +0.512 | **+0.000** |
| Mobile money | +0.713 | +0.543 | +0.208 |

**The first problem is that the null is measure-specific.** The financial-health items — a second
welfare margin available for 2021 and 2024, untouched in v2 — **co-move with all three rails at
0.354–0.705** while being **nearly orthogonal to the resilience measure** (+0.03 to +0.15). Two
self-reported welfare measures on the same economies in the same waves disagree with each other about
whether welfare moved. (E33.) Note that the polarity of the financial-health items is **not
established** — the repo has no questionnaire for them — so no welfare *direction* may be asserted
from them; what can be asserted is the disagreement.

**The second problem is that the row the boundary rested on is weighting-dependent.** E26 reads
**+0.294 weighted and +0.364 unweighted** — it fails the threshold as a person-weighted statistic and
clears it as an economy-weighted one. It is logged `discard-weighted`, and a boundary claim cannot
rest on a cell that changes verdict with the choice of lens.

**What survives.** Digitalization margins co-move strongly with balance-sheet quantities and weakly
or not at all with *this* self-reported hypothetical. Whether that is a boundary of the episode or a
property of the instrument is unresolved, and v3 does not resolve it. The developing-panel resilience
aggregate is flat (54.7 → 54.5), which compresses the available variance and works against detection,
and the 2021 base wave was fielded under pandemic conditions.

**Two further nulls worth recording.** Gender-gap closure over the window is essentially orthogonal to
mobile-money growth (r = +0.008) despite substantial cross-country variation in gap changes (sd
7.4pp) (E3); and the within-country income gap in formal saving did not widen in proportion to the
surge, on either the pp or the log-odds formulation (E20/E21).

## 8. A counter-moving margin: the retreat of cash

The ledger's newest line of work is the first that measures the *retreat of cash* rather than the
advance of digital payment, and it is included here because it is the only place where the loop's
breadth discipline produced something the headline indicators cannot see.

Two country-file items move **against** the digital-payment headline in the 2024 cross-section, in two
different modules, found by two different statistics:

| item | r vs digital-payment headline, 2024 (wtd / unwtd) | jackknife | largest single leave-one-out |
|---|---|---|---|
| Digital-payment detail item `fin31d` | −0.401 / −0.730 (`_s` variant) | through G6 | — |
| Wage-payment mode `fin34c` | **−0.552 / −0.486** | −0.553 | Brazil **+0.096** |

**The orientation emerges rather than being fixed.** `fin34c` against the headline by wave reads
**+0.028 / −0.122 (2014) → −0.419 / −0.323 (2017) → −0.690 / −0.367 (2021) → −0.552 / −0.486 (2024)**.
It starts orthogonal and turns counter-moving as digital payment spreads. (E47.)

**Both margins fall for a decade and then rebound, and the claim must say so.** `fin31d` reads
**47.1 → 34.1 → 20.5 → 26.6** and `fin34c` **15.9 → 11.8 → 8.0 → 15.2**, against a digital-payment
headline rising 34.3 → 60.9. A 2014→2024 long difference reports a fall of ~20 and ~1 points and
erases the reversal completely. **The 2021→24 rebound is common to both items in both modules and is
unexplained.**

**What is a level fact and what is a dynamic fact.** The counter-movement is a *cross-sectional
composition* fact — cash-heavy economies are digital-poor economies — and **not** a within-country
dynamic one: r(Δ`fin31d`, Δ headline) clears −0.30 on both lenses in only **1 of 3** registered cells,
where the weighted lens alone would have kept 3 of 3 (−0.400 / −0.759 / −0.336) against the
unweighted 1 of 3 (−0.159 / −0.352 / −0.266). That split was written into the pre-registration as the
reading *before* the answer was computed, which is the only reason it can be stated now. (E48a,
`discard-weighted`.)

**What does hold dynamically is that the two cash margins retreat together**: r(Δ`fin31d`, Δ`fin34c`)
= **+0.515 / +0.389** over 2014→2024, surviving multiple-testing correction over four registered
pairs, with a partial controlling for the digital-payment change that *strengthens* to +0.597 /
+0.383. The two digital-aligned wage modes run the other way (−0.744, −0.799) — larger in magnitude
than the keep pair and **ineligible**, because the pre-registration named the predicted sign and they
point the opposite way. All four items sort onto opposite sides of one axis. (E48b, a single
long-difference cell awaiting per-window replication.)

**A standing caveat on this whole section.** These item meanings are inferred from their levels and
coverage, never from a questionnaire — the repo has none for these modules. "Cash margin" is a
structural reading, not a documented label.

## 9. Individual-level evidence: how much does access absorb?

The country-level claim that the binding margin is now use rather than entry has an individual
counterpart measurable directly in the 2024 cross-section. For each dimension we compute the
unconditional gap in digital-payment use, the gap conditional on holding an account, and the implied
share of the unconditional gap the access margin absorbs.

**Table 3 — Digital-payment use, 2024 (144,090 respondents; weighted %, pp gaps)**

| dimension | unconditional gap | conditional on account | absorbed by access |
|---|---|---|---|
| Education (tertiary − primary) | +46.7 | **+16.8** | 64% |
| Income (q5 − q1) | +27.3 | **+11.5** | 58% |
| Labour force (in − out) | +20.8 | **+9.6** | 54% |
| Age (26-35 − 65+) | +11.6 | **+10.3** | **10%** |
| Connectivity (online − offline) | +30.5 | **+13.6** | **56%** |
| Urbanicity (urban − rural) | +11.0 | +3.7 | 66% |
| Gender (male − female) | — | +3.4 | — |

Access absorbs a majority of the education, income, employment, urbanicity and connectivity gaps but
leaves large residuals for the first three; it absorbs almost none of the **age** gap, which is
therefore a usage phenomenon end to end. Gender and urbanicity fall below the 5pp threshold
conditional on access and were discarded as claims — the gender gap in this data is an access-margin
phenomenon, and once inside, women and men use digital payments at nearly the same rate (86.8 vs
83.4).

**The connectivity row is the one that reframes the ruler.** Being online is the *only* axis of the
seven where account holding absorbs most of the gap (55.5%), and the residual connectivity gap
(+13.6pp) is **smaller than the education gap on the same sample** (+16.8pp); conditioning on
connectivity absorbs only 22.8% of the education gradient. Connectivity is mostly an access story;
the resource axes are not. Descriptively, the offline share among accountholders runs 43.6% among the
primary-educated-or-less against 2.3% among the tertiary, 34.6% at 65+, and 22.7% rural against 11.8%
urban. (U21.)

**The access margin itself is steeply graded**: account ownership runs 51.9 / 77.7 / 93.4% across the
three education levels and 61.7 vs 76.7% by labour-force status. Formal saving among all adults runs
12.0 / 22.6 / 46.2% by education, and among wage-receiving accountholders digital wage receipt runs
56.6 / 80.6 / 91.9%.

**These gradients are within-country, not composition.** The obvious objection to any pooled
cross-economy gradient is that it could be produced entirely by low-education or low-income adults
living in low-digitalization economies. The two largest axes were tested by computing the conditional
gap separately inside every economy with at least 100 unweighted respondents in both cells:

| axis | median within-economy gap | positive in | pooled | composition wedge |
|---|---|---|---|---|
| Education (secondary+ − primary) | **+9.4pp** | 63 of 64 economies | +12.1 | +2.7pp (22%) |
| Income (richest-40 − poorest-40) | **+5.7pp** | 74 of 83 economies | +7.9 | +2.2pp (28%) |

On the like-for-like contrasts the within-country medians are +18.0pp (tertiary vs primary, positive
in 23 of 23) and +9.7pp (q5 vs q1, positive in 30 of 33), against pooled figures of +16.8 and +11.5.
Composition contributes little and in the education case nothing at all. The income axis is thinner:
only 54% of qualifying economies clear 5pp on the coarse contrast. Four axes — age, gender,
urbanicity, employment — remain untested on this dimension. (U19, U20.)

**Barriers among the unbanked** are graded by education and income but not by cost or distance.
Documentation is cited by 54.2% of primary-educated unbanked adults against 46.0% of the tertiary;
"not enough money" by 35.7% of the poorest quintile against 25.3% of the richest. Cost is flat across
income (23.7 / 22.8 / 24.1 / 23.1 / 23.3) and distance is flat across rural–urban (36.0 vs 36.8) —
two supply-side barriers that do not bind hardest for the groups the demand-side literature usually
expects.

**Where "access converges, use diverges" holds and where it does not.** v2 used that phrase as its
title and applied it to every axis. On the 13-year country panel the *usage* gap narrowed as well as
the access gap on **age** (64.5% of economies) and on **labour force** (57.4%), and the **gender**
frame is a coin flip on both margins (54.5% access, 53.2% usage). The divergence claim holds where
disadvantage is defined by **resources** — income and education — and fails where it is defined by
cohort or sex. What is left across all five axes is an *ordering* of the access-minus-usage
asymmetry — income +23.3pp > education +18.0 > labour force +7.1 > gender +1.3 > age −0.9 — which has
**never been tested as a monotonicity claim** and is not asserted here. (E31, E34, E36.)

**A weighting warning attached to that whole panel.** The gender axis is the purest large-economy
artifact in the ledger: a population-weighted mean change in the log-odds access gap of −0.266 against
an **unweighted −0.002**, with the jackknife flipping the sign to +0.057. The population-weighted
gender access gap fell 10.2 → 4.6pp over 13 years; in the typical economy it barely moved. (E36.)

*Caveats specific to this section.* Conditioning on account ownership conditions on an outcome, so the
"absorbed" shares are a decomposition of observed rates and not a mediation estimate. Pooled
statistics weight economies roughly equally rather than by population. Single cross-section: no
statement here is a trend.

## 10. Inference: what thirty-three tests look like under correction

v2's Section 9 said the paper had no inference. It now does, computed ledger-wide over **thirty-three
association tests in six design families**, all recomputed from raw frames — **33 of 33 reproduced the
correlation on record within 0.02**, which is the first thing such an audit should establish and
rarely is.

**Result 1 — the effective sample size, not the nominal one, is what these tests have.** Median Kish
`neff` is **7.2** against a median nominal n of **71**. Benjamini–Hochberg at q = 0.10 rejects **26 of
33 on nominal n** and **1 of 33 on `neff`**. The single survivor is the SSA regional split of E1,
whose `neff` is 9.5 *because* it excludes the giant economies. **No significance language may be
attached to nominal n anywhere in this paper**, and none is.

**Result 2 — but that critique is about the weighted lens only, and v2's successor drafts must not
overstate it.** An unweighted correlation over 77 economies has `neff` = n = 77, because there are no
weights to concentrate. The honest framing is that this project has been reporting the typical-*person*
statistic as though it answered the typical-*economy* question — not that its associations are
undersupported across the board. Two caveats survive under either lens: economies are not independent
draws, and **regional clustering is unmodelled anywhere in this project**, which is a genuine
unaddressed limitation.

**Result 3 — the weighting relocates results rather than inflating them, and it decides the
keep/discard boundary in both directions.** The median de-weighting shift ledger-wide is **−0.051** —
the weighted ledger is on average very slightly *stronger*. But at the level of individual cells the
lens changes the verdict at roughly one case per handful of tests, in both directions: two ledger
discards cross the threshold when de-weighted, and the ledger's best all-windows result (Section 5)
is unweighted-only. **A low `neff` says the weights are concentrated; it does not say the result is
fragile.** The clearest illustration is two cells with the identical `neff` of 7.2: one moves from
+0.198 to +0.726 on dropping China, the other reads +0.797 weighted, +0.815 unweighted, +0.821 under
the jackknife, with a largest single leave-one-out of **Brazil at −0.042**. Effective n, the
unweighted twin, the jackknife and the named leave-one-out are four different diagnostics answering
four different questions.

**Result 4 — what survives everything.** Sixteen rows are **triple-clean**: BH-surviving on the
bootstrap p, |r| ≥ 0.30 unweighted, and jackknife retention ≥ 0.5. Of the twenty kept association rows
at audit time, 18 survive BH on the bootstrap p and the **only two failures were the two demotions
already pending** — which is the closest thing to external validation the protocol has produced.

**Two findings from v2 were demoted to discards on this evidence and their sentences are deleted, not
softened:** savings becoming a larger emergency-funds source where saving surged, and the
"accounts-first" partial in which 2021 usage intensity predicted slower subsequent account growth.
The latter reads **−0.654 / +0.591 / −0.595** across consecutive windows and **+0.106 unweighted** —
it reverses between adjacent windows and reverses back. v2's convergence claim (2021 level predicting
subsequent growth, +0.480) also carries a jackknife retention of 0.28 and a bootstrap p of 0.589 and
is not used in v3 as evidence.

## 11. Forecasting: closed, and what closing it taught

A parallel exercise asked how much of the 2024 cross-section is predictable from history ≤2021, with
2024 quarantined inside the evaluator. Persistence (2024 = 2021) gives mean absolute errors of 5.58pp
for account ownership, 6.68pp for resilience and 9.77pp for formal saving. The champion — a damped
trend for saving, then shrinkage of each economy toward its region, income-group and indicator-tercile
basin means at 10% per stage — gives **5.014 / 6.625 / 6.831pp**, i.e. skill over persistence of
**10.1% / 0.8% / 30.1%**.

**The stream is closed after 28 experiments and this section is final.** Three things it establishes:

1. **Only saving is predicted better than the typical economy actually moves.** Against median
   |actual Δ| of 3.405 / 5.761 / 9.234pp, resilience has **0.8% skill after twenty-eight experiments**
   and account ownership's error exceeds the median move.
2. **The champion is biased, not merely noisy** — signed error over MAE is 0.72 on saving and 0.49 on
   resilience, both under-predicting, and the account and saving signed residuals correlate +0.624.
   The bias is a broad upward 2021–24 level shift invisible to ≤2021 history, and any correction
   fitted to it would be peek-informed and inadmissible.
3. **Model selection on this panel does not survive the surge boundary.** There were **six
   cross-validation-to-holdout non-transfers**, one of them after passing a screen designed
   specifically to catch the previous five. At `neff` ≈ 7 the *shape* of a CV curve is no more
   informative about the holdout than its argmin.

The post-hoc account of all three is Section 5's repeat-mover result: consecutive-window Spearman of
per-economy changes is ≤ +0.07 in all ten pairs and negative in eight. **Reopening this stream
requires a change to the task**, not another mechanism on it; the one change worth making is an
earlier holdout wave, which would give these three MAEs their first error bar.

## 12. Limitations

In the order a referee will raise them.

1. **Effective sample size.** The population-weighted results have a median `neff` of 7.2. They are
   descriptive regularities on about seven effective observations. See Section 10 for what that does
   and does not imply.
2. **Regional clustering is unmodelled** under either lens. Economies are not independent draws.
3. **Almost everything is contemporaneous co-movement.** Partialling contemporaneous changes
   decomposes co-movement; it identifies nothing. The one class of design that would give temporal
   ordering — level or change at *t* against subsequent change — has been tried seven times and has
   never returned a keep (Section 5).
4. **The 2021 base wave.** Fieldwork conditions and survey mode changed for many economies during the
   pandemic, and most changes reported here difference against that wave.
5. **Window dependence.** Of the country-level keeps, nine remain single-window claims. Every partial
   and every level-to-change design that was tested on an earlier window failed.
6. **Undocumented items.** Section 8's modules, and the financial-health items in Section 7, are
   identified structurally from levels and coverage; the repo has no questionnaire for them. The
   consumer-protection and digital-risk module — the largest unused block in the data — is
   **unreachable** for the same reason.
7. **Micro design.** Survey design (PSU, strata) is not used, so any future standard errors on
   Section 9 will be understated unless it is; pooled statistics weight economies roughly equally.
8. **No external covariates.** Nothing outside Findex enters — no GDP, no regulation — so competing
   explanations cannot be held constant. Connectivity is the one exception and it is 2024-only.

## 13. Extension agenda

Stated as testable designs, in the order the evidence makes them valuable.

1. **The individual-level file is the largest reachable unused surface**: 154 columns in 19 families
   with no mentions, against a stream that holds 14 of the ledger's keeps. Utility payments,
   borrowing sources and agricultural payments are all present and untouched.
2. **Per-window replication of the two cash margins' co-retreat** (Section 8), currently a single
   long-difference cell, and an account of the 2021→24 rebound common to both.
3. **The 2021→24 rebound in both counter-moving margins** is unexplained and is the sharpest open
   question the breadth work produced.
4. **The access-minus-usage ordering** across five demographic axes (Section 9) needs a pre-registered
   monotonicity statistic against an independent measure of how resource-linked each axis is — five
   separate share tests are not an ordering claim.
5. **An earlier forecasting holdout** (train ≤2017, predict 2021) to give the champion MAEs their
   first error bar. This is a validation of a closed result, not an attempt to beat it.
6. **Agricultural payments** (four waves × 71 economies) is the best-covered untouched country module
   and the natural next module screen.
7. **Obtain the questionnaire.** Three separate lines of work — the financial-health polarity, the
   cash-margin labels, and the entire consumer-protection module — are blocked on a document that is
   not in the repo. This is the highest-value non-analytical task available.

---

## Appendix A — experiment ledger

All 73 experiments, with verdicts, both lenses, effective n and parent finding, are in `findings.tsv`,
indexed one line each in `LEDGER_INDEX.md`; the forecasting stream is in `results_prediction.tsv`;
every pre-registration and verdict is in `RESEARCH_LOG.md` in chronological order.

| stream | keeps | discards / other | total |
|---|---|---|---|
| Country level (E-series) | 22 | 28 | 50 |
| Individual level (U-series) | 14 | 9 | 23 |
| Forecasting (P-series) | champion final at P28 | 6 CV→holdout non-transfers | 28 |

Status vocabulary: `keep-general` (replicated across transitions with sign agreement, 6 rows),
`keep-general-unweighted` (1), `keep` (20), `keep-window` (a kept association on one transition, 9),
`inconclusive` (1), `discard-weighted` (the two lenses disagree and the finding fails as registered,
3), `discard` (33).

Discards used in this paper as substantive findings: E2, E3, E15, E16, E17, E18, E20, E21, E26, E27,
E31, E35, E36, E38, E44, E48a, U1, U5, U6, U8, U12, U16, U21.

## Appendix B — v2's corrections, and where each is discharged

| # | v2's error | discharged in |
|---|---|---|
| 1 | Title and Section 5 over-general: "access converges, use diverges" fails on cohort and sex | Title; §9 closing subsection |
| 2 | Section 4 framed 2021–24 as a digital-inclusion window | §4 (rewritten as a balance-sheet window, with the deceleration stated) |
| 3 | The three-rails decomposition failed replication and is a window property | §5 (withdrawn as a general claim, mechanism given) |
| 4 | Section 6's welfare "boundary" is measure-specific and weighting-dependent | §7 (demoted to a measure comparison) |
| 5 | Two findings in use had been demoted to `discard` | §10 (sentences deleted; the demotions and their evidence stated) |
| 6 | The missing inference now exists and is harsh | §10 (new section) |
| 7 | Section 8 (forecasting) is final and should say so | §11 (stated as closed, with the one reopening condition) |

Beyond the seven, v3 adds material that post-dates v2 entirely: the all-four-window
account~saving result (§5), the decade-continuity finding on total saving (§3), the demographic
breadth of the surge and its failed replication (§6), the connectivity row of the access ruler (§9),
and the counter-moving cash margins (§8).
