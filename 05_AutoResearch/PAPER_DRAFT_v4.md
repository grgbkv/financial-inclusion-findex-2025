# A balance-sheet window: formal saving, digital rails and resource-graded use in developing economies, 2021–2024

> **SUPERSEDED 2026-08-25 by `PAPER_DRAFT_v5.md`.** This file is kept as the historical record and
> must not be cited. Its CORRECTIONS OWED block below is **closed and frozen at two items, BOTH
> EXECUTED in v5**: item 1 (the reporting-set limitation stated as unquantified) is discharged by v5
> §10 Result 7 and §12 item 3; item 2 (the two standing keeps whose aggregate 2021→24 direction is
> wrong on a balanced set) is discharged by v5 §2 Table 1 and §7. Two further statements in this file
> are known wrong and are corrected in v5 rather than here: "the counter-moving margins are
> payment-mode items" (v5 §8.1) and E22's regional intensity reading (v5 §5).

**Working-paper draft v4 (2026-08-20).** Descriptive evidence from a pre-registered experiment
ledger over the Global Findex 2025 database (117-economy balanced panel, 2011–2024) and the 2024
individual-level file (144,090 respondents, 140 economies).

**Status of this draft.** v4 replaces v3 (2026-08-16) in full. Every empirical statement is traceable
to a numbered, pre-registered experiment in `findings.tsv` / `results_prediction.tsv`, run under the
protocol in `program_findex.md` and indexed one line per experiment in `LEDGER_INDEX.md`. Nothing
here is causal.

**Why v4 exists.** Rule B18's *count* branch fired: ten experiments have run since v3 was written
(U22, E49x, E49, E50, E51x, E51, E52, U23, E53, E54), against a threshold of ten. v3 was stale by
being **behind**, where v2 had been stale by being **wrong**. In the event the ten experiments did
both jobs — they discharge v3's one outstanding correction and they retire a claim v3 made in its
newest section.

**CORRECTIONS OWED: 2 items, opened 2026-08-21 by E55.** v3's single inherited item — §8's
"2021→24 rebound" paragraph — was executed in this draft; the passage is deleted rather than softened
and §8 is rebuilt around what survives a balanced economy set. v3's own discharge table for v2's
seven items is carried forward as Appendix B. The next distillation trigger (B18) reads *this* file,
and its corrections branch now stands at **2 of 5**.

1. **§12's reporting-set limitation is no longer "unquantified", and its size on 2021→24 is larger
   than this draft assumes.** E55's ledger-wide sweep (137 column × transition cells over 57 columns)
   finds three of the four transitions clean at a **median discrepancy of exactly 0.000pp**, and the
   2021→24 window carrying a systematic six-economy item-level dropout led by **China (26–27% of the
   reporting population)** that biases **29.1%** of its cells by ≥2pp. Wherever §12 says the risk is
   unquantified, it must instead say: *quantified, concentrated in one window, and material there*.
2. **Two standing keeps are exposed and their aggregate wave-to-wave movements change sign on a
   balanced set.** `fin32_acc` (E10's wage rail, `keep-general`) reads **−3.21pp** unbalanced and
   **+4.40pp** balanced over 2021→24, a discrepancy of −7.61pp — the largest non-`_s` figure in the
   audit. The whole `fh` family (E33's second welfare margin, `keep-window`) flips the same way:
   `fh1` −1.40 → +1.81, `fh2` −0.67 → +2.72, `fh1_fh2` −0.85 → +2.70. **Neither was touched by
   E53.** The E10/E33 *associations* are Δ→Δ correlations and are balanced by construction, so what
   is wrong is any statement in this draft about the **aggregate direction** of these margins over
   2021→24 — those must be recomputed on the balanced 71/69-economy set before they are repeated.
   **UPDATE 2026-08-22 — E56 has computed the replacement numbers; the execution is owed at the next
   distillation, so this item stays open and the corrections branch stays at 2 of 5.** On a fixed
   denominator: `fin32_acc` **8.04 → 10.35 → 12.03 → 16.43** (71 economies, 68.6% of developing-panel
   adult population), a **monotone rise whose largest step is the 2021→24 window** (+2.31, +1.68,
   **+4.40**) that the unbalanced series reports as a −3.21pp retreat; `fh1` **17.88 → 19.69**
   (+1.81), `fh2` **21.69 → 24.41** (+2.72), `fh1_fh2` **29.39 → 32.09** (+2.70), all on 69
   economies / 67.0% of panel population. All four last-window deltas **change sign** between the
   unbalanced and balanced series.

**A third fact E56 adds to item 1, which sharpens rather than corrects it.** The 2021→24 dropout is
**one six-economy release block** — Algeria, China, Iran, Mauritius, Russia, Ukraine, **31.4%** of
developing-panel adult population, all six present in the 2024 wave — and it spans **ten column
families across the payments section** (`fin30`–`fin43`, `fing2p`, `g20_made`/`g20_received`) rather
than one questionnaire module. Among the **63 usable** non-trivially-dropping columns there are only
**three distinct dropper sets in total**. `g20_any` is the only column inside an affected family that
stays stable, which is why the headline-based ledger was safe.

---

## Abstract

Between 2021 and 2024 formal saving in developing economies rose 13.7 percentage points (24.3% →
38.0% of adults), the largest movement of any financial-inclusion margin in the four wave transitions
Findex has measured since 2011. We document what that episode was made of, what moved with it, and
where it stopped, from a ledger of 83 logged experiments — 81 pre-registered tests, of which 40 were
discarded and 2 returned inconclusive, plus 2 mandatory exploratory mapping passes.

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
58% of the income gap and 10% of the age gap; the surviving education, income and connectivity
gradients are *within-country* regularities, positive inside 63 of 64, 74 of 83 and 55 of 56
qualifying economies respectively; and the last-mile education gradient in payment *mode* holds in
four independent payment streams, so it is a property of the adult rather than of one payer.

Three methodological results govern how all of the above should be read. Across thirty-three
association tests spanning six designs, Benjamini–Hochberg at q = 0.10 rejects **26 of 33** on nominal
n and **1 of 33** on the Kish effective n; median `neff` is **7.2** against a median nominal n of 71.
The population weighting decides the keep/discard boundary in both directions at roughly one case
per handful of tests, so every association here is reported under two lenses — and a registered
attempt to reread those disagreements as the weighted lens correctly detecting stronger association
among large economies was **rejected**: splitting economies by population does no more than splitting
them at random. Finally, a decade path in this data is computed over whichever economies report the
item in each wave, and on one four-item family holding the economy set fixed **removes the pattern
the path appeared to show**. These are descriptive regularities on about seven effective
observations, and no significance language is attached to any of them.

---

## 1. Introduction

The 2025 Global Findex release documents a large increase in formal saving in developing economies
between the 2021 and 2024 waves. This paper asks what that increase was made of, what moved with it,
and where it stopped.

The contribution is descriptive and deliberately bounded. There is no instrument, no policy
discontinuity and no within-country repeated observation of individuals; almost every country-level
association reported here is a co-movement of changes. What the paper offers instead is *discipline
over a large hypothesis space*: 81 hypotheses were registered with a stated keep threshold, and from
2026-08-15 a stated predicted **sign**, before the answer was computed; every one — kept or discarded
— is logged with its effect size, gate results, both weighting lenses and its effective sample size;
and 42 of the 81 were discarded or returned inconclusive. Applied cross-country work on Findex
rarely reports its discards; the informative nulls in Sections 7, 8 and 9 are the part of this paper
we would most like readers to take.

**What changed from v3, stated up front.** v3's newest section reported two country-file margins that
run *against* the digital-payment headline and stated that both "fall for a decade and then rebound",
calling the rebound the sharpest open question the breadth work had produced. Four subsequent
experiments took that apart. Two more modules were screened with the same instrument and produced no
third counter-moving margin. The per-window replication of the two margins' co-retreat **failed** on
the unweighted lens. The weight-structure audit found the disagreement is not leverage and not a
binary large-economy effect. And the rebound itself turned out to be **largely item-level attrition**:
six economies, China among them, report those items in 2021 and not in 2024 while remaining in the
2024 wave, and on a balanced economy set three of the four items do not rebound at all. What survives
is narrower, was registered in advance, and is stated as such in §8.

## 2. Data and method

**Country panel.** The Global Findex 2025 country file, restricted to the 117 economies observed in
all five waves (2011, 2014, 2017, 2021, 2024). The 2022 partial wave is merged into 2021 before any
computation. The developing subpanel (77 economies, excluding high-income) is the estimation frame
for every result in Sections 3–8 unless stated; the high-income complement (40 economies) is used
once, in Section 3, as a placebo frame.

**Individual data.** The 2024 microdata release (144,090 respondents, 140 economies), used only for
2024 cross-sectional description in Section 9. All statistics are survey-weighted. Under the data
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

*Country coverage varies by indicator and wave, and §8 shows this is not a footnote: the wage series
is computed on 77 economies through 2021 and 71 in 2024, so its aggregate decline (19.6 → 16.4) is
partly compositional and is not interpreted. Mobile money is reported by 57–62 economies.*

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

**Five rules adopted since v2 that change what may be claimed.** They are stated here because most of
the differences between successive drafts follow mechanically from them. The fifth is new in v4.

1. **Two lenses, always.** Every association reports its population-weighted and unweighted
   correlation. The weighted statistic describes the typical *person*; the unweighted one the typical
   *economy*. Neither is the correct lens, and where they disagree against the threshold the finding
   is logged `keep-weighted` / `keep-unweighted` / `discard-weighted` and the dependence is part of
   the claim.
2. **Effective n beside nominal n.** Every association carries its Kish effective sample size,
   `neff = (Σw)²/Σw²`, and no significance language is attached to nominal n.
3. **Name the economy.** A jackknife on the five largest economies is reported alongside the largest
   *single* leave-one-out effect and the economy responsible, because "five economies decide it" is a
   hypothesis about a cell and not a property of the frame. §10 adds the symmetric statistic: the
   smallest economies whose removal moves the *unweighted* verdict, which no gate had ever looked at.
4. **A scale-free twin on every between-group comparison in percentage points.** Gaps, differences
   and ratios of pp changes all inherit the same arithmetic artifact while both groups sit below 50%,
   and where the log-odds twin disagrees the pp version is the artifact. This trap sprang three times
   in the ledger before it became a rule.
5. **Hold the denominator fixed, and say what it is.** *(New in v4, forced by §8.)* An aggregate wave
   path is computed over whichever economies report the item in that wave. Where an item's reporting
   set changes between waves, the path confounds the level with the composition of reporters — and
   because reporting sets are correlated across items within a module, several items can appear to
   move together for that reason alone. Any path or Δ claim must state whether the economy set is
   balanced, and a claim resting on an unbalanced one is not admissible.

**Ledger size.** 83 experiments: 58 country-level (23 keeps, including two exploratory mapping
passes that can produce no keep) and 25 individual-level (16 keeps), plus 28 forecasting experiments
in a separate stream.

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
tested, and the caveat is smaller than v2 thought — on this margin.** Total saving reads 53.1 (2014),
43.6 (2017), 42.4 (2021), 53.0 (2024), so a 2014→2024 difference is flat while formal saving rises
~16pp — the signature of relabelling, opposite to the within-window verdict. The question was whether
the 2014→2017 fall is a real decline or a definitional break in the instrument. Five diagnostics were
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

**A qualification v4 must attach to the previous paragraph, from §8.** The headline saving margins
are reported by 76–77 economies in every wave, so their paths are effectively balanced and rule 5
above does not bite here. That is a property of the headline set, not of the file: the four
cash-side items in §8 lose six reporters between 2021 and 2024, and the resulting path artifact is
large enough to have produced a claim in v3. Decade-scale readings of *non-headline* items in this
data are not safe by default.

## 4. What kind of window this was

**v2 described 2021–24 as a digital-inclusion episode. That is wrong, and the correction was the
single largest change in v3.** Measuring each margin's biggest transition by the unweighted share of
economies gaining ≥10pp — a within-country statistic, immune to the weighting critique that sinks
aggregate comparisons — every margin peaks in a *different* window:

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
overstated it in two separate ways, and the claim was demoted in v3 to a comparison between
measures.**

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
property of the instrument is unresolved, and v4 does not resolve it. The developing-panel resilience
aggregate is flat (54.7 → 54.5), which compresses the available variance and works against detection,
and the 2021 base wave was fielded under pandemic conditions.

**Two further nulls worth recording.** Gender-gap closure over the window is essentially orthogonal to
mobile-money growth (r = +0.008) despite substantial cross-country variation in gap changes (sd
7.4pp) (E3); and the within-country income gap in formal saving did not widen in proportion to the
surge, on either the pp or the log-odds formulation (E20/E21).

## 8. The cash side: two counter-moving margins, a failed promotion, and a path that was not real

This section is **rewritten in full**. v3 reported the same two margins and then said that both "fall
for a decade and then rebound", calling the shared rebound the sharpest open question the breadth
work had produced. Four experiments since have replaced almost all of it. The section is kept — and
kept long — because the sequence is the most instructive thing in the ledger about how a
cross-country descriptive claim fails.

### 8.1 What the screen found, across four modules

The instrument is a **four-way orientation screen**: each item in a module is correlated with the
digital-payment headline in the 2024 developing-panel cross-section and sorted as `restatement`
(|r| ≥ 0.80), `aligned` (+0.30 ≤ r < 0.80), `counter-moving` (r ≤ −0.30) or `independent`
(|r| < 0.30), with **both lenses required to agree** — otherwise `mixed-lens`. Every module gets a
mandatory exploratory mapping pass first, logged before the screen is read.

Four modules have now been screened identically. Two counter-moving margins have been found, and
only two:

| module | cols screened | counter-moving | rest |
|---|---|---|---|
| `fin31` digital-payment detail | 9 | **`fin31d`** | — |
| `fin34` wage-payment modes | 8 | **`fin34c`** | — |
| `fin` catch-all | 24 eligible of 93 | **0** | 12 aligned, 7 independent, 4 mixed-lens, 1 restatement |
| `fin43` agricultural payments | 4 eligible of 6 | **0** | 2 aligned, 2 independent |

| item | r vs digital-payment headline, 2024 (wtd / unwtd) | jackknife | largest single leave-one-out |
|---|---|---|---|
| `fin31d` | −0.401 / −0.730 (`_s` variant) | through G6 | — |
| `fin34c` | **−0.552 / −0.486** | −0.553 | Brazil **+0.096** |

**The orientation emerges rather than being fixed.** `fin34c` against the headline by wave reads
**+0.028 / −0.122 (2014) → −0.419 / −0.323 (2017) → −0.690 / −0.367 (2021) → −0.552 / −0.486 (2024)**.
It starts orthogonal and turns counter-moving as digital payment spreads. (E47.)

**The two nulls are the informative part, and they were registered as such.** The `fin` catch-all is
the file's largest untouched block and returned **0 of 24** counter-moving, with the most negative
weighted cell at −0.135 — not within 0.16 of the bar on either lens. `fin43` was the best remaining
*prior* for a third counter-moving margin, being payments in the part of the economy where cash
persists longest, and returned **0 of 4**. Two margins out of four modules screened with the same
rule is a much weaker base rate than "we found two in the first two modules we looked at" implies,
and both nulls were pre-registered with the null reading written down in advance. (E49, E51.)

**Two by-products of the screens that any future user of this file needs.** `fin26a` correlates with
the digital headline at **+0.933 / +0.852** — it is a *restatement* of the headline, a second
`dig_acc`, and must never be used as an independent margin. And `fin30` falls **57.0 → 45.3** across
the decade while correlating **+0.254 / +0.306** with the headline: it is a **declining** margin that
is **not counter-moving**. The ledger's first clean separation of those two ideas, and a caution
against reading a falling level as evidence of opposition. (E49x, E49.)

### 8.2 The co-retreat, and its failed promotion

The two counter-moving margins retreat together: r(Δ`fin31d`, Δ`fin34c`) = **+0.515 / +0.389** over
2014→2024, with a partial controlling for the digital-payment change that *strengthens* to +0.597 /
+0.383. The two digital-aligned wage modes run the other way (−0.744, −0.799) — larger in magnitude
than the keep pair and **ineligible**, because the pre-registration named the predicted sign and they
point the opposite way. All four items sort onto opposite sides of one axis. (E48b.)

**The all-windows promotion test FAILED, and the shape of the failure is the result.** Run per
window, the pair reads:

| window | r weighted | r unweighted | G6 | largest leave-one-out |
|---|---|---|---|---|
| 2014→17 | +0.795 | +0.431 | +0.463 | China −0.275 |
| 2017→21 | +0.650 | +0.243 | +0.320 | China −0.215 |
| 2021→24 | +0.615 | +0.263 | +0.374 | India −0.239 |

Weighted **3 of 3**, unweighted **1 of 3**. E48b is left at `keep-window`, recorded as **FAILED**
promotion, and the co-retreat is a population-weighted per-window regularity plus a span fact on the
unweighted lens. Two things make this more informative than a bare failure. It is **not a reversal** —
all six lens-windows are positive, so it is a magnitude failure of the 0.30 bar rather than an
E5b-style sign flip. And it **reproduces E48a's lens split exactly (weighted 3/3, unweighted 1/3) on
a different pair of margins in the same two modules**, with China and India carrying it. (E50.)

The companion cross-sectional/dynamic distinction from v3 stands: the counter-movement is a
*cross-sectional composition* fact — cash-heavy economies are digital-poor economies — and **not** a
within-country dynamic one. r(Δ`fin31d`, Δ headline) clears −0.30 on both lenses in only **1 of 3**
registered cells, where the weighted lens alone would have kept 3 of 3 (−0.400 / −0.759 / −0.336)
against the unweighted 1 of 3 (−0.159 / −0.352 / −0.266). That split was written into the
pre-registration as the reading *before* the answer was computed. (E48a, `discard-weighted`.)

### 8.3 Why the lenses disagree here: neither of the two obvious answers

Because the same lens split now appears from two independent designs on the same cell, it was worth
a registered audit rather than another correlation. Two mechanisms were registered with fixed firing
rules; **neither fired**, and the verdict is `inconclusive`. That is a real result, because both
mechanisms are what the ledger had been assuming.

**It is not leverage.** Winsorizing the population weights at their 90th percentile lifts `neff` from
7.2 to about 32 and leaves the weighted correlation at **+0.591 / +0.466 / +0.418 / +0.476** across
the four cells — above the bar in 4 of 4. Capping at the *median* (`neff` ≈ 60) still gives
+0.468 / +0.294 / +0.292 / +0.403. De-concentrating the weights by a factor of four in effective n
costs this cell 0.10–0.20 of correlation and never crosses the bar. **"Five economies decide it" is
false for this cell in the leverage sense.**

**It is not a binary large-economy effect either.** The registered pattern — top population tercile
in, bottom tercile out — holds in only 2 of 4 cells, and it fails because the **bottom** tercile also
clears +0.30 in two cells, not because the top fails.

**What the audit did establish is a symmetry the gates were blind to.** G6 and the named
leave-one-out look only at the largest economies, by construction. The mirror statistic — the fewest
*small* economies whose removal lifts the **unweighted** correlation above the bar — shows the
unweighted verdict is decided just as tightly: **removing Bulgaria alone lifts the 2021→24 unweighted
r above +0.30**, and Ukraine plus Bulgaria does it for 2017→21 — precisely the two windows that
produced E50's lens split. On the weighted side the corresponding fragility depth is 5 / 2 / 2 / 3
named economies. The ledger's standing worry has been that big economies decide weighted results;
this cell says the unweighted lens is no more stable, it is merely unstable in economies nobody
names. (E52. Both depth statistics are now reported on any cell where the lenses disagree; §10 states
the general consequence.)

### 8.4 The rebound was not real: item-level attrition, and what survived

**v3's sentence "both margins fall for a decade and then rebound, and the claim must say so" is
withdrawn.** The quoted paths — `fin31d` 47.1 → 34.1 → **20.5** → 26.6 and `fin34c` 15.9 → 11.8 →
**8.0** → 15.2 — are computed over whichever economies report the item in each wave. **Six economies
report these items in 2021 and not in 2024 — Algeria, China, Iran, Mauritius, Russia, Ukraine — and
all six are present in the 2024 wave**, with `account_t_d` recorded for each. This is item-level
attrition inside the file, not economies leaving the survey.

The magnitude is decisive. **China alone holds 25.9% of the 2021 reporting population on these four
items, at levels of 4.5 / 1.3 / 6.2 / 1.1** — far below every other large reporter — so its departure
from the 2024 denominator mechanically lifts the series. Dropping China from 2021 alone raises that
year's trough by **+5.7 / +2.3 / +1.6 / +2.0pp**, i.e. by most of the apparent rebound.

On the **balanced 71-economy set** (all four items in all four waves) the paths are:

| item | 2014 | 2017 | 2021 | 2024 | Δ 2021→24 |
|---|---|---|---|---|---|
| `fin31d` | 40.8 | 33.4 | 26.9 | 26.6 | **−0.28** |
| `fin34c` | 14.5 | 13.1 | 10.5 | 15.2 | **+4.77** |
| `fin42` | 22.1 | 15.7 | 13.3 | 13.4 | **+0.11** |
| `fin43c` | 18.6 | 11.5 | 9.2 | 8.8 | **−0.42** |

**Three of the four items do not rebound at all**, and unweighted all four are flat or still falling.
The share of economies whose 2021→24 change is positive is **39.4 / 42.3 / 46.5 / 47.9%** — under half
on every item, with a negative median change on all four. A four-item aggregate rebound in four
different modules was, to a first approximation, one large low-level reporter leaving the
denominator. (E53's registered Secondary A/B plus one labelled diagnostic.)

**What survives is a minority, within-country, and was registered in advance.** Define an economy as
carrying the V-shape on an item if its 2021 level is below its 2014 level by more than a margin *and*
its 2024 level is above its 2021 level by more than the same margin. On the balanced set, **10 of 71
economies (14.1%) carry the V on at least 3 of the 4 items**, against a permutation null — shuffling
each item's V-indicator independently across economies — of 6.7%. That is **2.11×** the null, above
its 97.5th percentile of 11.3%, `p_perm` **0.003**, bootstrap CI **[7.0%, 22.5%]**. The named set is
**Bulgaria, Congo Rep., Dominican Republic, India, Madagascar, Philippines, Sri Lanka, Thailand,
Uganda, Viet Nam**.

**Three caveats are part of the claim, not attached to it.** The keep is **margin-dependent**: the
two-part bar fires at the registered 1pp margin and not at 0pp (1.42×, ratio bar missed) or 2pp
(2.69× but tying the null's 97.5th percentile on four economies), although the direction and
`p_perm` (0.024 / 0.003 / 0.048) hold at all three. The population-weighted twin reads 44.2% against
a 6.8% null — that number is India, and it should not be quoted without the name. And **a shared
shape is not a shared cause**: a common 2024 questionnaire change touching cash-side items together
would produce the same co-occurrence, and this design cannot exclude it. The claim is `keep-window`
with **no promotion route** — it is about the 2021→24 window by construction and cannot be replicated
on an earlier transition. (E53.)

### 8.5 One lead, explicitly not a finding

`fin43c` is *independent* of the digital-payment headline (−0.146 / −0.234) and **counter-moving with
account ownership on both lenses** (−0.389 / −0.322, G6 −0.273, CI [−0.653, +0.035]). That is the
mirror image of `fin34c`, which counter-moves with digital payment and not with access. The
account-anchored cell carried no registered bar and its interval includes zero, so this is a lead. It
does raise a question the section cannot answer: **the two known cash margins disagree about which
anchor a "cash margin" should run against**, and any registered successor must name the anchor in
advance. (E51 secondary.)

**A standing caveat on this whole section.** These item meanings are inferred from their levels and
coverage, never from a questionnaire — the repo has none for these modules. "Cash margin" is a
structural reading, not a documented label, and §8.4's alternative explanation (a questionnaire
change) is unfalsifiable here for exactly that reason.

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

**The connectivity row reframes the ruler.** Being online is the *only* axis of the seven where
account holding absorbs most of the gap (55.5% pooled), and the residual connectivity gap (+13.6pp)
is **smaller than the education gap on the same sample** (+16.8pp); conditioning on connectivity
absorbs only 22.8% of the education gradient. Connectivity is mostly an access story; the resource
axes are not. Descriptively, the offline share among accountholders runs 43.6% among the
primary-educated-or-less against 2.3% among the tertiary, 34.6% at 65+, and 22.7% rural against 11.8%
urban. (U21.)

**Three of the ruler's axes have now been shown to be within-country, not composition.** The obvious
objection to any pooled cross-economy gradient is that it could be produced entirely by low-education,
low-income or offline adults living in low-digitalization economies. Each axis was tested by
computing the conditional gap separately inside every economy with at least 100 unweighted
respondents in *both* cells:

| axis | median within-economy gap | positive in | pooled over the same set | composition wedge |
|---|---|---|---|---|
| Education (secondary+ − primary) | **+9.4pp** | 63 of 64 | +12.1 | +2.7pp (22%) |
| Income (richest-40 − poorest-40) | **+5.7pp** | 74 of 83 | +7.9 | +2.2pp (28%) |
| Connectivity (online − offline) | **+10.62pp** | **55 of 56 (98.2%)** | +15.20 | +4.58pp (**30%**) |

On the like-for-like contrasts the education and income within-country medians are +18.0pp (tertiary
vs primary, positive in 23 of 23) and +9.7pp (q5 vs q1, positive in 30 of 33), against pooled figures
of +16.8 and +11.5. Composition contributes a minority everywhere and in the education case almost
nothing. The connectivity wedge is the largest of the three, consistent with connectivity being the
axis on which economies differ most — but 70% of its pooled gap is still within-economy. The
connectivity axis also *raises* U21's absorption figure: the pooled 55.5% becomes a **median 65.0%
within economies** (positive in 53 of 56), so the pooled number understated the typical economy.
(U19, U20, U22.)

**A frame fact that constrains all within-country micro work here, and that no earlier draft
stated.** Requiring 100 unweighted respondents in *both* cells is not a formality — it decides which
economies can be asked the question at all, and the qualifying set is not random. Connectivity
qualifies **56 of 140 economies holding 40.8% of accountholding respondents**, because wherever
internet use is high the *offline* accountholder cell is thin; the qualifying set is therefore tilted
toward lower-connectivity economies, and the median is a statement about them. The two saturated
cases in the set (Kenya +0.3, Malawi +0.1, both 97–99% on each side) show the gradient closing where
digital payment is universal. Where the same requirement cannot be met at all, the check is simply
unrunnable — see the pension and agriculture streams below. (U22, U23.)

**The last-mile gradient is a property of the adult, not of one payer.** Among adults who hold an
account and participate in a given payment stream, the share whose payments run *through the account
rather than in cash* is education-graded in **all four** streams tested, three of them previously
untouched columns:

| stream | tertiary − primary gap | cluster-bootstrap CI | absorbed by account holding |
|---|---|---|---|
| Pensions | **+6.51pp** (83.0 → 89.5) | [+3.64, +9.54] | 69.0% |
| Agricultural sales | **+14.16pp** (35.2 → 49.3) | [+5.86, +22.22] | 49.4% |
| Utility bills | **+26.07pp** (41.9 → 68.0) | [+19.43, +31.43] | 30.3% |
| Wages (reference, U14) | **+35.28pp** | [+28.62, +41.88] | 30.9% |

All four intervals exclude zero and all four clear the registered 5pp bar with the sign registered in
advance. Bootstrapping over **economies** rather than respondents — respondents are clustered, and a
respondent-level resample would understate the interval — the **pension gradient is the fragile one**:
it clears the bar in only **83.8%** of draws, and the claim must say the pension gradient is both the
smallest and the least certain. (U23.)

**An ordering across payment streams, offered as a lead and not a finding.** Account holding absorbs
**69.0%** of the education gradient where the payer is a public institution (pensions), **49.4%**
where it is a buyer (agriculture), and only **30.3%** and **30.9%** where the adult initiates or
receives directly (utilities, wages). The ruler's standing ~64% figure from U10/U19 is reproduced
almost exactly by the one stream with an institutional payer and missed by half where there is none.
The registered secondary that produced this cleared its bar by **0.6pp** and is a coin flip; the
*pattern across streams* deserves a fresh registration with the ordering named in advance, and is not
claimed here.

**The composition check is unrunnable for two of the four streams.** **Zero** economies reach 100
unweighted respondents in both education cells for pensions or agricultural sales, so those two
gradients are pooled-only and **unverified on composition** — a weaker state than the registered
downgrade rule contemplated, and recorded as such rather than counted as a pass. `pay_utilities`
qualifies 8 economies (14.4% of participants): median within-economy gap **+31.53pp**, positive in 7
of 8, composition wedge **+3.91pp (11%)** — the smallest wedge of any axis measured this way.

**The access margin itself is steeply graded**: account ownership runs 51.9 / 77.7 / 93.4% across the
three education levels and 61.7 vs 76.7% by labour-force status. Formal saving among all adults runs
12.0 / 22.6 / 46.2% by education, and among wage-receiving accountholders digital wage receipt runs
56.6 / 80.6 / 91.9%.

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
"absorbed" shares are a decomposition of observed rates and not a mediation estimate. Pension receipt
is age-selected and agricultural receipt rural-selected, with no adjustment for either. Pooled
statistics weight economies roughly equally rather than by population. Note that the low-`neff`
critique in §10 does **not** transfer to this section: the Kish `neff` of the *survey* weights inside
these cells runs 569–5,128 against nominal 874–7,602, because it is a statement about population
weights across economies, not about survey weights within them. Single cross-section: no statement
here is a trend.

## 10. Inference: what the ledger looks like under correction

v2's Section 9 said the paper had no inference. It now does, computed ledger-wide over **thirty-three
association tests in six design families**, all recomputed from raw frames — **33 of 33 reproduced the
correlation on record within 0.02**, which is the first thing such an audit should establish and
rarely is.

**Result 1 — the effective sample size, not the nominal one, is what these tests have.** Median Kish
`neff` is **7.2** against a median nominal n of **71**. Benjamini–Hochberg at q = 0.10 rejects **26 of
33 on nominal n** and **1 of 33 on `neff`**. The single survivor is the SSA regional split of E1,
whose `neff` is 9.5 *because* it excludes the giant economies. **No significance language may be
attached to nominal n anywhere in this paper**, and none is.

**Result 2 — that critique is about the weighted lens only.** An unweighted correlation over 77
economies has `neff` = n = 77, because there are no weights to concentrate. The honest framing is that
this project has been reporting the typical-*person* statistic as though it answered the
typical-*economy* question — not that its associations are undersupported across the board. Two
caveats survive under either lens: economies are not independent draws, and **regional clustering is
unmodelled anywhere in this project**.

**Result 3 — the weighting relocates results rather than inflating them, and it decides the
keep/discard boundary in both directions.** The median de-weighting shift ledger-wide is **−0.051** —
the weighted ledger is on average very slightly *stronger*. But at the level of individual cells the
lens changes the verdict at roughly one case per handful of tests, in both directions: two ledger
discards cross the threshold when de-weighted, and the ledger's best all-windows result (§5) is
unweighted-only. **A low `neff` says the weights are concentrated; it does not say the result is
fragile.** The clearest illustration is two cells with the identical `neff` of 7.2: one moves from
+0.198 to +0.726 on dropping China, the other reads +0.797 weighted, +0.815 unweighted, +0.821 under
the jackknife, with a largest single leave-one-out of **Brazil at −0.042**. Effective n, the
unweighted twin, the jackknife and the named leave-one-out are four different diagnostics answering
four different questions.

**Result 4 — the obvious defence of the weighted lens was registered and REJECTED, and this is new in
v4.** If the weighted lens were simply detecting an association that is genuinely stronger among
large economies, its disagreements with the unweighted lens would be informative rather than
distortionary. That hypothesis was suggested by an unregistered pattern in §8.3's audit — within-tercile
unweighted correlation rising with population size in 4 of 4 cells, mean top-minus-bottom **+0.253** —
and was then registered **fresh on a different cell**: the six bivariate rails of §5 × three windows,
eighteen cells, with the bar (mean Δr ≥ +0.15 and positive in ≥ 12 of 18) and the sign fixed in
advance. It fails wide. Mean Δr is **+0.047**, positive in **9 of 18**, monotone across terciles in 3
of 18, bootstrap CI **[−0.074, +0.162]**. The registered control is decisive: against a 1,000-draw
null that splits economies **at random** rather than by population, the population split sits inside
the null band ([−0.115, +0.108], `p_perm` **0.209**). Splitting by size does no more than splitting by
nothing. **The ledger's weighted/unweighted disagreements cannot be reread as the weighted lens seeing
something real about large economies; the de-weighting critique stands as written.** (E54. One
labelled, unregistered observation is carried without being claimed: the window means are −0.113,
+0.014 and **+0.240** for 2014→17, 2017→21 and 2021→24, with 5 of 6 rails positive in the last window
only — a subset of a failed primary, with no multiplicity control.)

**Result 5 — the stability diagnostics have been one-sided, and are no longer.** G6 and the named
leave-one-out both look only at the *largest* economies, so the ledger has been able to say
"the result survives dropping the giants" and has never been able to say anything about the small
ones. The mirror statistic — how few small economies must be removed to move the *unweighted* verdict
— was computed for the first time in §8.3 and gives **1** (Bulgaria) and **2** (Ukraine + Bulgaria)
on the two cells whose lens split motivated the audit, against weighted fragility depths of 2–5 named
economies on the same cells. **Neither lens is the stable one.** Both depths are reported from here on
wherever the lenses disagree. (E52.)

**Result 6 — what survives everything.** Sixteen rows are **triple-clean**: BH-surviving on the
bootstrap p, |r| ≥ 0.30 unweighted, and jackknife retention ≥ 0.5. Of the twenty kept association rows
at audit time, 18 survive BH on the bootstrap p and the **only two failures were the two demotions
already pending** — which is the closest thing to external validation the protocol has produced.

**Two findings from v2 were demoted to discards on this evidence and their sentences are deleted, not
softened:** savings becoming a larger emergency-funds source where saving surged, and the
"accounts-first" partial in which 2021 usage intensity predicted slower subsequent account growth.
The latter reads **−0.654 / +0.591 / −0.595** across consecutive windows and **+0.106 unweighted** —
it reverses between adjacent windows and reverses back. v2's convergence claim (2021 level predicting
subsequent growth, +0.480) also carries a jackknife retention of 0.28 and a bootstrap p of 0.589 and
is not used in v3 or v4 as evidence.

**A debt this section owes and cannot yet discharge.** The audit above tests every association for
multiplicity, weighting and jackknife sensitivity. It tests **none** of them for the failure §8.4
found: whether the economy set was held fixed between the waves being differenced. No experiment in
the ledger has ever checked this, and it is now the highest-priority open item (§13).

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

The post-hoc account of all three is §5's repeat-mover result: consecutive-window Spearman of
per-economy changes is ≤ +0.07 in all ten pairs and negative in eight. **Reopening this stream
requires a change to the task**, not another mechanism on it; the one change worth making is an
earlier holdout wave, which would give these three MAEs their first error bar.

## 12. Limitations

In the order a referee will raise them.

1. **Effective sample size.** The population-weighted results have a median `neff` of 7.2. They are
   descriptive regularities on about seven effective observations. See §10 for what that does and does
   not imply — including that the obvious defence of the weighted lens has been registered and
   rejected (§10, Result 4).
2. **Neither lens is the stable one.** The unweighted verdict on the one cell where it has been
   measured turns on **one** small economy (§10, Result 5). The ledger's stability evidence before
   this cycle was one-sided by construction.
3. **Unbalanced reporting sets, ledger-wide and unaudited.** §8.4 shows an aggregate path over an
   unbalanced economy set producing a pattern that vanishes when the set is held fixed, and that the
   attrition was concentrated in the single largest, lowest-level reporter. **No other experiment in
   the ledger has been checked for this**, and the headline indicators' near-complete coverage is not
   a guarantee for the narrow items. This is the largest known unquantified risk in the project.
4. **Regional clustering is unmodelled** under either lens. Economies are not independent draws.
5. **Almost everything at country level is contemporaneous co-movement.** Partialling contemporaneous
   changes decomposes co-movement; it identifies nothing. The one class of design that would give
   temporal ordering — level or change at *t* against subsequent change — has been tried seven times
   and has never returned a keep (§5).
6. **The 2021 base wave.** Fieldwork conditions and survey mode changed for many economies during the
   pandemic, and most changes reported here difference against that wave.
7. **Window dependence.** Of the country-level keeps, ten remain single-window claims, and two
   promotion attempts have now failed rather than gone unattempted (E43 via E44, E48b via E50).
8. **Undocumented items.** §8's modules, and the financial-health items in §7, are identified
   structurally from levels and coverage; the repo has no questionnaire for them. This is not only a
   labelling problem: §8.4's alternative explanation for the V-cluster — a 2024 questionnaire change
   touching cash-side items together — is unfalsifiable without one. The consumer-protection and
   digital-risk module, 133 country columns and 52 individual-level ones, is **unreachable** for the
   same reason, and was re-checked this cycle and confirmed blocked.
9. **Micro design.** Survey design (PSU, strata) is not used, so any standard errors on §9 will be
   understated unless it is; the intervals reported there are economy-cluster bootstraps, which is the
   right unit but not the full design. Two of the four payment streams in §9 are unverified on
   composition because no economy meets the cell-size rule on both sides.
10. **No external covariates.** Nothing outside Findex enters — no GDP, no regulation — so competing
    explanations cannot be held constant. Connectivity is the one exception and it is 2024-only.

## 13. Extension agenda

Stated as testable designs, in the order the evidence makes them valuable. Items 2, 3 and 6 of v3's
agenda are **closed** — the per-window replication was run and failed (§8.2), the rebound was
overturned (§8.4), and agricultural payments was screened and returned a null (§8.1).

1. **A ledger-wide reporting-set audit.** For every column used in a Δ or path claim, the count and
   population share of economies reporting at *t* and not at *t+1*, and the difference between the
   unbalanced and balanced series. §8.4 found one such artifact by accident and it had already reached
   a draft. This is cheap, mechanical, and it is the natural successor to §10's multiplicity audit.
   **Highest priority.**
2. **The individual-level file is the largest reachable unused surface**: 102 columns in 10 families
   with no mentions, against a stream holding 16 of the ledger's 39 keeps at a 64% keep rate. Reachable
   families include borrowing sources, emergency funds, utility-payment detail and digital-risk
   exposure (the last a split-sample module — check the weights before registering).
3. **The payer-set ordering in access absorption** (§9): 69% for an institutional payer against ~30%
   where the adult transacts directly, from a secondary that cleared its bar by 0.6pp. Register the
   ordering in advance across the four streams.
4. **The anchor question for cash margins** (§8.5): `fin34c` counter-moves with digital payment and
   not with access; `fin43c` does the reverse. A registered primary must name its anchor in advance,
   and `fin43c` carries four waves.
5. **The access-minus-usage ordering** across five demographic axes (§9) needs a pre-registered
   monotonicity statistic against an independent measure of how resource-linked each axis is — five
   separate share tests are not an ordering claim.
6. **An earlier forecasting holdout** (train ≤2017, predict 2021) to give the champion MAEs their
   first error bar. This is a validation of a closed result, not an attempt to beat it, and it is the
   only condition under which that stream reopens.
7. **Obtain the questionnaire.** Three lines of work — the financial-health polarity, the cash-margin
   labels, and the entire consumer-protection module — are blocked on a document that is not in the
   repo, and §8.4 added a fourth use for it. This is the highest-value non-analytical task available.

---

## Appendix A — experiment ledger

All 83 experiments, with verdicts, both lenses, effective n and parent finding, are in `findings.tsv`,
indexed one line each in `LEDGER_INDEX.md`; the forecasting stream is in `results_prediction.tsv`;
every pre-registration and verdict is in `RESEARCH_LOG.md` in chronological order.

| stream | keeps | discards / other | total |
|---|---|---|---|
| Country level (E-series) | 23 | 35 | 58 |
| Individual level (U-series) | 16 | 9 | 25 |
| Forecasting (P-series) | champion final at P28 | 6 CV→holdout non-transfers | 28 |

Status vocabulary and counts: `keep-general` (replicated across transitions with sign agreement, 6),
`keep-general-unweighted` (1), `keep` (22), `keep-window` (a kept association on one transition or one
long-difference cell, 10), `inconclusive` (a registered diagnostic whose fixed verdict rule returns
neither branch, 2), `discard-weighted` (the two lenses disagree and the finding fails as registered,
4), `discard` (36), `exploratory` (a mandatory mapping pass that can produce no keep, 2).

**Design families and their base rates**, which no single experiment shows and which should inform
what gets registered next: `micro-cross-section` 25 experiments / 16 keeps · `delta-delta` 19/9 ·
`level-to-change` **7/0** · `measurement` 7/1 · `partial` 6/3 · `gap-trajectory` 6/2 ·
`delta-delta-multi` 5/3 · `audit` 4/1 · `distribution` 2/2 · `level-cross-section` 1/1 ·
`long-difference` 1/1.

Discards and inconclusives used in this paper as substantive findings: E2, E3, E15, E16, E17, E18,
E20, E21, E26, E27, E31, E35, E36, E38, E44, E46, E48a, E49, E50, E51, E52, E54, U1, U5, U6, U8, U12,
U16, U21. **Twenty-nine of them** — the discard column is where most of §§7–10 comes from.

## Appendix B — the correction record

**v3's outstanding item, discharged here.**

| # | v3's error | discharged in |
|---|---|---|
| 1 | §8's "2021→24 rebound" paragraph: the quoted four-item paths are computed over an unbalanced economy set and the rebound is largely item-level attrition | §8.4 (passage deleted; balanced paths, the six named economies and China's 25.9% share given; the surviving minority V-cluster stated with its margin dependence). §12's open question inherits the fix; the general rule is §2's new rule 5 |

**v2's seven items, carried from v3's Appendix B for the record.**

| # | v2's error | discharged in |
|---|---|---|
| 1 | Title and organising claim over-general: "access converges, use diverges" fails on cohort and sex | Title; §9 closing subsection |
| 2 | §4 framed 2021–24 as a digital-inclusion window | §4 (rewritten as a balance-sheet window) |
| 3 | The three-rails decomposition failed replication and is a window property | §5 (withdrawn as a general claim) |
| 4 | §6's welfare "boundary" is measure-specific and weighting-dependent | §7 (demoted to a measure comparison) |
| 5 | Two findings in use had been demoted to `discard` | §10 (sentences deleted) |
| 6 | The missing inference now exists and is harsh | §10 |
| 7 | §8 (forecasting) is final and should say so | §11 |

**Material new in v4 that post-dates v3 entirely:** the two module nulls and the four-module base rate
for counter-moving margins (§8.1); E48b's failed per-window promotion and its exact reproduction of an
earlier lens split (§8.2); the weight-structure audit rejecting both leverage and binary heterogeneity,
and the ascent-depth statistic (§8.3, §10 Result 5); the attrition correction and the surviving
V-cluster (§8.4); the connectivity axis of the within-country ruler and its qualifying-set caveat
(§9); the four-stream last-mile education gradient and the payer-set ordering (§9); and the
registered rejection of the population-gradient defence of the weighted lens (§10, Result 4).
