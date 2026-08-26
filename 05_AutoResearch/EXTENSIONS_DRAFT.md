# Extensions draft — autoresearch session, 2026-07-11 (branch `autoresearch/jul11`)

> ## STATUS BLOCK — updated 2026-08-25. THIS FILE IS ABSORBED INTO `PAPER_DRAFT_v5.md`.
>
> **Retired 2026-08-25:** the two passages below that read E22 as "a general developing-world
> regularity with a declared SSA intensity gradient" are **withdrawn**. E22's all-windows promotion
> was run (E58) and **failed** — both failures sit in 2014→17 — and the intensity ordering
> **reverses** in 2017→21 (SSA +0.405 against +0.675 outside). E22 stays `keep-window` and the
> regional-intensity sentence must not be reused. See `PAPER_DRAFT_v5.md` §5.
>
> **Everything in this file that still stands is now written into `PAPER_DRAFT_v5.md` (2026-08-25),
> which supersedes `PAPER_DRAFT_v2.md`, `PAPER_DRAFT_v3.md` and this extensions file as the place candidate material
> is carried.** The prose below dates from **2026-07-11, at experiment 27**, and fifty-six
> experiments have run since; it is retained as the audit trail for what was proposed and when, not
> as a live backlog. **Do not lift any passage below into a write-up without checking it against v4.**
>
> Specifically, three things in the text below are known-wrong and are corrected in v4: the
> three-separate-rails decomposition (failed replication, §5), the welfare "boundary" (demoted to a
> measure comparison, §7), and every "digitalization signature" phrasing (the window is a
> balance-sheet window, §4). Two demoted findings — E7 and E5b — appear below and are discards.
>
> New candidate material produced after this file was written lives in v4 §8 (the cash side, rebuilt
> in full on 2026-08-20 after its rebound premise was overturned) and v4 §13 (the live extension
> agenda). A **fourth** known-wrong class was added on 2026-08-20 and applies to any passage below
> quoting a wave path on a narrow item: rule **B20** now requires a balanced economy set, and paths
> computed over whoever reports in each wave are not admissible. **Live agenda items are tracked in
> `RESEARCH_AGENDA.md`, not here.**
>
> ---
>
> ### Previous status block — 2026-08-11 distillation (historical)
>
> Everything after this block was written on **2026-07-11**, at experiment 27. Fourteen
> experiments have run since, and this file has **not** been rewritten. Under rule B4 an extension
> may enter the paper as a regularity only if it is `keep-general`; under the new rules B8/B9/B10 it
> must also agree in sign across every tested window, report its unweighted twin, and carry its Kish
> `neff`. Applying those rules to this file:
>
> **Still standing (the six replicated bivariates, E28/E30).** E1 (mobile money ~ saving, +0.719,
> replicated +0.454), E10 (wage rail, +0.791 / +0.678), E11 (borrowing ~ saving, +0.403 / +0.616),
> E12 (digital payments, +0.370 / +0.685), E14 (mobile money ~ digital payments, +0.600 / +0.871).
> E22's regional split stands (SSA +0.923, rest +0.676) and is the **only** cell in the entire
> ledger that survives Benjamini–Hochberg at the *true* degrees of freedom (E40) — because
> excluding the giant economies is what raises `neff` to 9.5.
>
> **Standing but flagged.** E13 (FI ~ mobile-money complementarity, +0.435) is `keep-general` but
> **weighting-dependent in both windows** — unweighted +0.188 and +0.248 (E40). Do not present it
> as a headline.
>
> **WITHDRAWN — do not carry into the paper.**
> - The **three-separate-rails decomposition** (E23/E24/E25, quoted at length below) **failed its
>   replication**: 0 of 3 promoted on 2017→2021 (E35), because the rails were near-collinear
>   (+0.871) in the earlier window. It is a description of the window in which they decoupled.
> - **E7** (savings as a growing emergency-funds source) and **E5b** (the accounts-first partial)
>   were **demoted to `discard`** on 2026-08-11 (E32/E38 recommended, E40 confirmed).
> - The **welfare boundary** (E26) is measure-specific (E33) and weighting-dependent
>   (+0.294 weighted / +0.364 unweighted, E40). It is not a boundary.
>
> **Reframed.** 2021→24 is a **balance-sheet** window, not a digital-inclusion one: account
> ownership peaked 2011→14, digital payments 2014→17, saving and borrowing 2021→24 (E39), and a
> fifth margin picked after that reframing — merchant payments — sorts with the rails at 26.3%
> rather than with the balance sheet (E41). Every "digitalization signature" phrasing below is
> written about a window in which the digitalization margins were **decelerating**.
>
> **The number that governs all of it.** Median Kish `neff` across thirty-three association tests is
> **7.2** (median nominal n = 71), and ledger-wide BH rejects **1 of 33** at `neff` (E40). These are
> descriptive regularities on about seven effective observations. Nothing below may be written up
> with significance language.


Candidate material for a working-paper v2, produced by an autonomous pre-registered
experiment loop over the Findex 2025 panel (protocol: `program_findex.md`; every attempt —
kept and discarded — is in `findings.tsv` / `results_prediction.tsv`; each experiment is a
commit on this branch). All results are descriptive associations on the 117-country balanced
panel (77 developing), population-weighted, gated by the paper's pitfall checklist.

## Extension 1 — the saving surge rode mobile-money rails *geographically* (E1)

The paper showed the 2021→2024 formal-saving surge (+14 pp in developing economies) and its
definitional mobile-money component (~4 pp). The panel shows the surge is also geographically
concentrated where mobile-money adoption grew: weighted r = 0.72 between country-level
Δsaving and Δmobile-money (n = 58; jackknife-stable, 0.80 without the top-5 population
countries). Countries in the top tercile of mobile-money growth gained **+14.8 pp** of formal
saving; the bottom tercile gained **+2.2 pp**. Proposed use: a geographic decomposition
subsection following the surge finding, with a Δsaving-vs-Δmm scatter.

**And it is not a Sub-Saharan Africa story (E22).** Because mobile money is SSA-concentrated, the
obvious alternative reading of E1 is that it describes one region which population weighting then
carries — an alternative the jackknife gate cannot address, since dropping the five largest
*countries* leaves a region intact. Splitting the developing panel and re-running E1's exact
construction inside each half: within SSA, r = **0.92** (n = 25, jackknife 0.88), with Δmobile-money
terciles gaining −0.2 / +10.5 / **+21.1 pp** of formal saving; within the five other developing
regions pooled, r = **0.68** (n = 33, jackknife *grows* to 0.71), terciles +3.0 / +9.1 / **+12.5 pp**.
The association is materially stronger and steeper inside SSA, but it is unambiguously present
outside it and survives a drop-top-5 jackknife on only 33 economies — a stiffer test than the
pooled sample faced. E1 should therefore be written up as a general developing-world regularity
with a declared SSA intensity gradient, not as a regional finding.

**The channel is not mobile-money-specific (E10).** The surge co-moves just as strongly with
the growth of *digital wage rails*: weighted r = 0.79 between Δsaving and Δ(share of adults
paid private-sector wages into an account) 2021→2024 (n = 71; jackknife barely moves,
0.79 → 0.79 without the top-5). Terciles of Δwage-digitalization gain +3.2 / +10.9 / +13.6 pp
of formal saving. Reading: the surge is a broad-based digitalization signature across multiple
account on-ramps (mobile money *and* formal wage rails), not one rail — account growth is a
plausible common driver of both sides (descriptive, not controlled).

A *third* digitalization channel co-moves too (E12). Δ(any digital payment, `g20_any`) tracks
Δ(formal saving) 2021→2024 at weighted r = 0.37 (n = 76; jackknife *strengthens* to 0.78
without the top-5). Terciles of Δdigital-payment gain +2.8 / +16.7 / +14.4 pp of formal
saving. So the surge co-moves with the broadest usage margin (any digital payment) as well as
with mobile money and wage rails — three account on-ramps, one signature.

**But they are genuinely separate rails, not one factor read three ways (E23).** The obvious
deflationary reading of E1/E10/E12 is collinearity: the digitalization indicators move together
(Δmobile money ~ Δdigital payment, r = 0.60, E14), so three correlations may be one. They are not.
Partialling Δ(any digital payment) out of the mobile-money association leaves weighted **r = 0.51**
(n = 58, jackknife 0.51 → 0.41), and the symmetric partial — digital payments net of mobile money —
leaves **r = 0.57** (→ 0.37 without the top-5). Each rail surrenders roughly a quarter of its
bivariate association to the shared factor and keeps the rest; neither absorbs the other. The
wage-rail control points the same way (Δmobile money net of Δwage digitalization, r = 0.34,
n = 56). Together with the regional split below, this closes both deflationary readings of E1: it
is neither one region (E22) nor one factor (E23). One caveat to record alongside E12: on this
mobile-money-reporting subsample the Δdigital-payment ~ Δsaving bivariate is 0.75 rather than the
0.37 estimated on the full panel, so that channel is markedly stronger where mobile money is
reported. Partialling a *contemporaneous* Δ decomposes co-movement; it controls nothing and
identifies nothing.

**The wage rail is the strongest and steadiest of the three (E24).** Applying the same partial to
E10's wage-digitalization channel: Δ(wages into accounts) keeps weighted **r = 0.58** with Δ(formal
saving) after Δ(any digital payment) is partialled out (n = 71), and the jackknife is the cleanest
in the ledger — 0.583 → 0.582, i.e. dropping the five largest economies moves it by a thousandth.
The symmetric partial leaves digital payments at 0.43. Pushing the design one step further than
E23, all three rails can be held against each other **at once**: on the common sample (n = 56) the
partial of each channel net of the *other two* is **wage 0.43 > digital payments 0.38 > mobile
money 0.30**, the last just at the threshold. So the three-rail structure survives joint
conditioning, but the ordering inverts the bivariate one: mobile money has the largest raw
association with the surge (0.72) and the smallest independent one. Stated as description, with the
standing caveat that partialling contemporaneous Δs decomposes co-movement rather than identifying
anything, and that `fin32_acc` is an employer-side attribute of how wages are paid.

**And E1 is not a Sub-Saharan Africa story (E22).** Splitting the developing panel by region and
re-running E1's construction inside each gives r = **0.92** within SSA (n = 25, jackknife 0.92 →
0.88; Δmobile-money terciles gain −0.2 / +10.5 / +21.1 pp of saving) and r = **0.68** across the
five other developing regions pooled (n = 33, jackknife *grows* to 0.71; terciles +3.0 / +9.1 /
+12.5 pp). The association is materially stronger and steeper inside SSA — mobile money is plainly
the dominant rail there — but it holds outside it too, on a stiffer test than the pooled sample
faced. G6 guards against one-*country* stories; this is the guard against one-*region* stories.

**And the deepening is broad, not saving-specific (E11).** Formal *borrowing* and formal
*saving* grew together across the panel 2021→2024: weighted r = 0.40 between Δ(formal
borrowing) and Δ(formal saving) (n = 76; jackknife *strengthens* to 0.47 without the top-5, so
this is no big-country artifact). Reading: the surge reflects genuine balance-sheet deepening
on both sides of the household ledger, not a one-sided store-of-value shift — reinforcing the
digitalization-channel story above.

**And the rails reach that second margin too — they are not saving-specific (E25).** The three-rail
structure was built entirely around one destination; pointed at formal *borrowing* instead, it still
holds. Δ(wages into accounts) co-moves with Δ(formal borrowing) at weighted **r = 0.61** (n = 71,
jackknife 0.61 → 0.50), and **0.42 net of the saving channel** — most of the association survives
partialling out everything borrowing shares with the saving surge. On the three-rail common sample
(n = 56) every rail is associated with the borrowing deepening — wage **0.65** > mobile money
**0.54** > digital payments **0.51** — and E11's own Δsaving ~ Δborrowing correlation on that same
sample is **0.51**, i.e. *no weaker than the rails themselves*. The reading offered for v2 is not
that digitalization caused credit, but that the saving and borrowing margins are two surfaces of one
digital-deepening episode, and E11's co-movement is largely the shadow of the rails they share.
Two asymmetries are worth a sentence: saving is the **stronger** destination (0.80 / 0.71 / 0.75
against saving versus 0.65 / 0.54 / 0.51 against borrowing, identical sample), and the rail
**ordering flips** between destinations (wage > digital payments > mobile money for saving; wage >
mobile money > digital payments for borrowing). Wage digitalization leads both — its third
appearance as the steadiest rail in the ledger (E10, E24, E25). Standing caveats: contemporaneous
Δ-on-Δ decomposition, not identification; the borrowing headline mixes formal-institution and
credit-card borrowing; subsample composition inflates every benchmark (E11's 0.40 on n = 76 reads
0.48 on n = 71 and 0.51 on n = 56).

## Extension 2 — resilience composition moves before resilience levels (E7, with E2 as the null)

Headline resilience was flat (54.7 → 54.5 panel), and mobile-money growth shows **no robust
link** to resilience *changes* (E2: r = 0.19, collapses to −0.005 without top-5 — a clean
null). But the *composition* of resilience is shifting: reliance on **savings as the source
of emergency funds** rose from 17.9 to 20.3 pp of adults in developing economies, and grew
most where formal saving surged (r = 0.54, n = 76). Reading: the access → saving →
resilience pipeline's middle stage is now visible in the data; the last stage is not yet.
This sharpens the paper's "access without depth" argument with a mechanism-in-progress.

## Extension 3 — the accounts-first growth signature (E5b)

Among developing panel countries at *similar account levels* in 2021, those whose accounts
were used less intensively (lower digital-payments-to-account ratio) added **more** accounts
by 2024: weighted partial r = −0.60 controlling for the account level (vs −0.30 for plain
convergence). Caveat: the magnitude concentrates in large economies (−0.11 without the
top-5, sign stable). Reading: mass account-expansion runs ahead of usage infrastructure —
the access-vs-depth gap has a visible growth signature, not just a level signature.

## Extension 4 — who the access-vs-depth gap leaves behind (micro layer, 2024 cross-section)

The individual-level 2024 wave (144,090 respondents, 140 economies; all weighted, gated by
cell-size and country-file reproduction) locates the gap demographically:

- **Access barrier is income-graded (M1).** Among the unbanked, "not enough money" is cited by
  35.7 pp of the poorest income quintile vs 25.3 pp of the richest — monotonic, 10.3 pp gap.
- **Depth barrier is education-graded, and steeper (U4).** Formal saving (saving at a financial
  institution) reaches **46.2 pp** of tertiary-educated adults but only **12.0 pp** of the
  primary-or-less-educated — a 34.1 pp monotonic gap. The *depth* margin is stratified even more
  sharply by education than the *access* margin is by income.
- **Mobile money is the young/underbanked on-ramp (M2).** Mobile-only accountholders are far
  younger (65 vs 41 pp aged ≤35) and somewhat less educated than bank-only holders.
- **Digital-payment use falls off with age (U2).** Adoption is an inverted-U by age, peaking at
  26–35 (59.7 pp) and lowest at 65+ (48.1 pp), 8.7 pp below the prime working-age band.
- **The documentation barrier is education-graded (U9).** Among the unbanked, "lack of necessary
  documentation" is cited by **54.2 pp** of the primary-or-less-educated vs **46.0 pp** of the
  tertiary-educated — monotonic, 8.2 pp gap — the natural stratifier for a formal-paperwork
  barrier, mirroring M1's income gradient on the money barrier.
- **Labour-force attachment gates both margins (U13).** Adults in the workforce hold accounts at
  **76.7 pp** vs **61.7 pp** for adults out of it — a 15.0 pp access gap — and, unusually, the gap
  barely narrows once access is held constant: among *accountholders*, formal saving is 34.2 pp
  for the in-workforce vs 20.9 pp for the out-of-workforce (13.3 pp). Compositional caveat: "out
  of workforce" pools students, retirees, homemakers and discouraged workers and correlates with
  age, gender and education, so this is an association, not an employment effect.

Reading: the paper's "access without depth" theme has a consistent demographic signature —
income gates *access*, education gates *depth*, age gates *digital usage*, and labour-force
attachment gates both margins at once. All are single-wave 2024 cross-sectional descriptions
(no trend claims).

## Prediction box — the surge was a regime change, not a trend (P1–P3)

A fixed forecasting task (predict each country's 2024 value from waves ≤ 2021) quantifies
how *new* the 2024 wave's information is:

| Target | Persistence MAE | Best model MAE | What worked |
|---|---:|---:|---|
| Account ownership | 5.58 pp | **5.01 pp** | three-stage income-group→region→digital-payment-tercile shrinkage, k=0.1 each (P7+P13+P17) |
| Resilience | 6.68 pp | **6.63 pp** | light region-mean shrinkage, k=0.1 (P5) |
| Formal saving | 9.77 pp | **6.83 pp** | damped trend (λ=0.5) + four-stage region→income-group→account-tercile→digital-payment-tercile shrinkage, k=0.1 each (P2+P11+P12+P16+P18) |

A mobile-money-informed growth model fit on the 2017→2021 transition **failed** (9.75 pp):
the contemporaneous saving–mobile-money correlation of Extension 1 was not forecastable from
the previous transition. The surge is genuinely new 2024-wave information — a regime change,
consistent with the definitional expansion plus post-pandemic saving behavior. What *does*
help account and resilience is shrinking each country's 2021 value slightly toward a group
mean (k = 0.1, selected by cross-validation on the fully pre-2021 account transition, never on
the 2024 test wave): a mild convergence prior beats flat persistence, while a logit-space
ceiling-deceleration model (P4) did not — the missing structure is convergence, not saturation.
The convergence basin matters slightly: for account, the same pre-2021 CV prefers the
*income-group* mean over the *regional* mean (P7, 5.16 → 5.14 pp), while resilience still uses
the regional mean (P5). Saving, too, gains from shrinkage layered on the damped
trend, and here the effect *stacks*: a first region-mean shrink (P11, 8.45 → 7.96 pp) and then
a second, orthogonal income-group-mean shrink (P12, 7.96 → 7.36 pp; the same second stage helps account only marginally, 5.144 → 5.105, and fails outright on resilience, P13) each help, because the two
convergence basins capture partly-independent cross-sectional structure. A *third* stage
compounds too, and it need not be a geographic or administrative grouping: shrinking toward the
mean of the country's **2021 account-level tercile** — a "digitalization stage" basin that cuts
across region and income group — takes saving from 7.36 to **7.08 pp** (P16), with diminishing
increments across the three stages (−0.49 / −0.60 / −0.28). That data-driven third stage is not
saving-specific: the same construction applied to account ownership, shrinking toward the mean of
the country's 2021 **digital-payment-adoption tercile**, improves it from 5.11 to **5.01 pp**
(P17) — and it buys more than twice what account's second, purely administrative stage did
(−0.091 vs −0.039 pp). A basin drawn from a *different* indicator's cross-section evidently
carries more independent signal than a second geographic or administrative cut. And the stacking
does not stop at three: a **fourth** stage for saving, shrinking toward the mean of the country's
2021 digital-payment tercile on top of the account-tercile stage, takes it from 7.08 to
**6.83 pp** (P18), with the increment barely decaying (−0.28 then −0.25) even though both
data-driven basins are digitalization cuts that might have been near-collinear. Over the whole
sequence, shrinkage alone has bought saving −1.62 pp against the damped trend's −1.32 pp — the
noise correction is now the larger half of the model. Notably, the same
cross-indicator information fails when it enters as fitted coefficients instead: a weighted ridge
on 2021 levels of account, digital payments and saving loses outright to own-history shrinkage on
the pre-2021 CV (P15). Cross-indicator structure helps as a *basin*, not as a regressor — which is
what one expects if the mechanism is noise correction rather than signal extraction. The contrast
with the
failed attempts to *re-tune* the shrinkage strength or the trend on pre-2021 data (P8–P10) is
instructive: shrinkage corrects cross-sectional sampling noise, a regime-independent mechanism
that transfers across the 2021 break (and compounds across orthogonal basins), whereas anything
tuned to pre-2021 *dynamics* does not.

### What access equalizes, and what it does not (U4, U7, U10, U14, U15, U16-U19)

Education is the sharpest stratifier in the 2024 micro cross-section, and it does not stop at
the account door. Unconditionally the digital-payment gap between tertiary and primary-educated
adults is 46.7 pp (37.3 → 84.0). Conditioning on holding an account absorbs about two-thirds of
it, but 16.8 pp remains (77.3 / 87.7 / 94.1, monotonic) — a genuine within-accountholder usage
gradient (U10). That contrasts sharply with gender, where conditioning on access leaves almost
nothing (3.4 pp usage-side, 5.0 pp depth-side; U6, U8). "Access does the sorting" is a
gender-specific finding, not a general one: for education, both margins bind.

The margin where access equalizes *least* is the one the adult does not control. Among adults who
already hold an account and receive wages, the share whose wages arrive **in** that account is
56.6 / 80.6 / 91.9 pp across primary / secondary / tertiary education — a **35.3 pp** gradient
that survives conditioning on access almost intact: the unconditional gap is 51.0 pp, so access
absorbs only **31 %** of it, against ~64 % for digital payments (U14 vs U10). A natural reading,
though not one this design can test, is that wage-receipt mode is set by the **employer**, so the
education gradient here proxies formal-versus-informal sector composition rather than anything the
individual chooses. This is the individual-level counterpart of the country-level finding that
wage digitalization co-moves with the saving surge (E10, r = 0.79), and it locates the binding
constraint on the employer's side of the transaction rather than the household's.

**A clean ordering emerges (U15).** Running the same conditioning step — the digital-payment rate
unconditionally, then among accountholders only — across all three demographics on one outcome
gives how much of each gap access explains: **gender ≈ all of it** (the residual is 3.4 pp, U6),
**education ≈ two-thirds** (46.7 → 16.8 pp, U10), **age ≈ none** (11.6 → 10.3 pp between the 26-35
peak and the 65+ band, U15). Among accountholders the age profile runs 86.9 / 88.2 / 84.9 / 82.6 /
77.8 pp across the five bands. Older adults *are* less banked, but that is not why they pay less
digitally: age is almost purely a usage gradient, where gender is almost purely an access one. A
second, descriptive detail points the same way — the unconditional inverted-U (a dip among 15-25s,
peak at 26-35) flattens into a near-monotone decline once accounts are held, so the young-adult dip
is an access story and the old-age dip is not. Policy-relevant reading, offered as description
only: opening accounts closes the gender gap in digital payments and much of the education gap,
and does close to nothing for the age gap. All caveats of a single cross-section apply, and age
correlates with education, employment and account tenure, none of which is controlled here.

**A fourth axis completes the ruler, and it sits on the access side (U16).** Where a person lives
behaves like sex, not like schooling: the rural–urban gap in digital payments is 11.0 pp
unconditionally (48.3 rural / 59.3 urban) but only **3.7 pp** among accountholders (83.5 / 87.2) —
access absorbs **66 %** of it, and the residual is essentially gender's (3.4 pp). The access margin
itself is the whole story: account ownership runs 66.3 pp rural against 76.6 pp urban, a 10.3 pp
gap. The four axes therefore sort cleanly into two pairs: **where you live and what sex you are
gate the account; how educated and how old you are gate the usage.** One tension worth flagging
rather than resolving — among the unbanked, the self-reported "too far away" barrier is *flat*
across rural and urban (36.0 / 36.8 pp, U5), so the rural access deficit is not explained by stated
physical distance, and what does explain it is untested here. Urbanicity correlates with education,
income and employment, none controlled; single cross-section throughout.

**The fifth axis is the one that binds on both margins (U17).** Income quintile — the last major
demographic not yet on the ruler — behaves like education, not like sex or place. Digital-payment
use among accountholders runs 78.3 / 82.9 / 84.8 / 87.0 / 89.8 pp from the poorest to the richest
within-economy quintile, a **+11.5 pp** residual (strictly monotone) against a +27.3 pp
unconditional gap, so access absorbs 58 %. What distinguishes income is that it is large on *both*
sides of the decomposition: the access margin itself is +19.4 pp (61.1 → 80.6 pp account ownership).
Gender and place are access-only, age is usage-only, income is both.
One methodological point earned here and worth carrying into v2: **the absorption percentage does
not sort these axes; the residual in pp does.** Income absorbs 58 % and urbanicity 66 % — nearly the
same share — yet they leave 11.5 pp and 3.7 pp respectively, because income's unconditional gradient
is 2.5× wider. Ranked by what access actually fails to close: education 16.8 > income 11.5 > age
10.3 ≫ urbanicity 3.7 ≈ gender 3.4 pp. Note also that `inc_q` is a *within-economy relative* rank,
not an absolute income level, so under economy-equal pooling it does not carry quite the same
meaning across economies as education or age do — a caveat specific to this axis.

**The sixth axis is a job (U18).** Labour-force status behaves like income: large on both margins.
Digital-payment use among accountholders is 87.9 pp for adults in the workforce against 78.3 pp for
those out of it — a **+9.6 pp** residual against a +20.8 pp unconditional gap, so access absorbs
54 %; the access margin itself is +15.0 pp (76.7 / 61.7 pp account ownership), reproducing U13's
figure to the decimal. Employment therefore joins education, income and age on the usage-gating side
rather than gender and urbanicity on the access-only side. It also re-makes the ruler's methodological
point from the opposite direction: employment (54 %), income (58 %) and urbanicity (66 %) absorb
comparable *shares* while leaving 9.6, 11.5 and 3.7 pp — the residual is what sorts them. The full
ranking by what access fails to close: **education 16.8 > income 11.5 > age 10.3 > employment 9.6 ≫
urbanicity 3.7 ≈ gender 3.4 pp.** Read with U14 (digital wage receipt steeply education-graded) and
E24/E25 (wage digitalization the steadiest country-level rail), the wage channel keeps surfacing on
both sides of the micro/macro boundary. Caveat specific to this axis: `emp_in` is a coarse binary
that pools students, homemakers, pensioners and the unemployed, so the residual mixes very different
groups; employment correlates with age, education and income, none controlled.

**Is the ruler a within-country regularity, or between-country composition? (U19)** Every axis above
is pooled across economies, which leaves one live alternative: the gradients could be produced
entirely by composition — low-education adults concentrated in low-digitalization economies — with
no gradient *inside* any country. U19 tests the largest axis directly, computing the conditional
education gap **separately in each economy** and applying the n ≥ 100 cell rule per economy (64
economies qualify, 69.5% of accountholding respondents). The median within-economy gap is
**+9.4 pp, positive in 63 of 64 economies (98%)**; pooled over those same economies it is +12.1 pp,
so composition accounts for only **+2.7 pp, about a fifth** of the pooled figure. On the
like-for-like tertiary-vs-primary contrast the within-country median is **+18.0 pp, positive in all
23** qualifying economies — *above* the pooled +16.8 pp, i.e. composition contributes nothing there.
The education gradient is a regularity inside economies, not an artifact of where educated adults
live. Two limits are worth stating in v2: the qualifying set is selected (economies need sizeable
primary-educated *and* secondary-plus accountholding populations, which trims both tails of the
education distribution), and **the other five axes remain pooled-only** — U19 licenses the
within-country reading for education, not yet for income, age, employment, urbanicity or gender.

## Honest nulls worth one sentence each

- Mobile-money growth ⇏ resilience gains within the window (E2; replicated exactly at
  r = +0.189 on the current sample by E26).
- Neither does the saving surge itself: Δresilience is orthogonal to Δformal-saving
  (r = 0.03, E15) — the composition of emergency funds shifted (E7) before the share who can
  raise them moved.
- **The digitalization rails stop at the balance sheet (E26).** On one common sample of 56
  economies, each rail's three destinations form a clean ladder: wage digitalization co-moves with
  Δformal-saving at +0.80 and Δformal-borrowing at +0.65, but with Δresilience at only +0.30;
  digital payments give +0.75 / +0.51 / **exactly 0.00**; mobile money +0.71 / +0.54 / +0.21. The
  wage rail's primary (r = +0.294, n = 71) missed the pre-registered 0.30 bar by 0.006 with every
  gate passing and the jackknife *strengthening* to +0.407, so it is logged as a discard rather than
  a keep — but the pattern is the point: digitalization tracks **where money is stored and where
  credit came from**, an order of magnitude more weakly than it tracks self-reported shock-coping
  capacity. Three independent attempts (E2, E15, E26) now agree on that boundary, and it is
  consistent with the flat dev-panel resilience aggregate (54.7 → 54.5 pp).
- Gender-gap changes 2021→2024 are large (σ = 7.4 pp) but orthogonal to mobile-money growth (E3).
- No systematic reversion of the unusually narrow 2021 income gap proportional to the
  earlier poorest-40 jump (E6).
- The dormancy "J-curve" after account drives is real population-weighted but is a
  large-country (India-drive) phenomenon, not a cross-country regularity (E4).
- The saving surge is *not* just account expansion: Δaccount and Δformal-saving are only weakly
  aligned at the population-weighted level (r = 0.20, E16), and the largest account-growth
  economies are precisely where saving surged least (drop-top-5 flips r to 0.74) — the depth
  margin deepened somewhat independently of who newly got an account.
- Convergence is a property of the *access* margin only: 2021 account level predicts
  2021→2024 account growth at r = −0.30 with the jackknife growing (gate-clean catch-up,
  reconfirming E5/E9), while the same test on formal saving gives r = +0.48 — the wrong sign for
  catch-up, and one that flips to −0.14 without the five largest economies, so no general claim
  in either direction survives (E17). Depth does not converge the way access does. Note this
  sits alongside, not against, the prediction stream's shrinkage gains: shrinkage is correcting
  cross-sectional noise, not exploiting mean reversion in levels.
- **The saving surge was distributionally broad — the apparent widening is an artifact of scale
  (E20 + E21).** Two related claims were tested and both fail. The surge did not disequalize in
  proportion to its size: countries with the largest surges did not widen their internal income
  gap in saving the most (r = +0.18, terciles non-monotonic, E20). And the widening itself does
  not survive a change of scale. On the percentage-point scale the gap between the richest 60 %
  and poorest 40 % grew from 14.4 to 20.5 pp (formal saving +10.8 pp for the poorest 40 %,
  +16.9 pp for the richest 60 %, pop-weighted across 55 developing panel economies) — but E21,
  pre-registered specifically to address the low-base confound, finds the pop-weighted mean
  change in the **log-odds** gap is only +0.109, **flips sign to −0.115** when the five largest
  economies are dropped, and is shared by **fewer than half** (47.3 %) of economies. In
  proportional terms the poorest 40 % in fact gained *faster* (×1.59 vs ×1.52). The pp widening
  is therefore largely the arithmetic of a lower base, and the level fact should **not** be
  written up as the rich pulling away. Methodologically this is the cleanest example in the loop
  of why a pp gap between two groups at very different bases needs a scale-free companion
  statistic before it carries any weight.

## Methods note for v2

The loop enforced the paper's pitfall taxonomy as automated gates (indicator-variant
declaration, coverage thresholds, official-aggregate cross-checks, jackknife stability) plus
pre-registration of every hypothesis before testing; discards are logged, not hidden. One
gate-design lesson: sign-stability alone is too weak a jackknife criterion (E4 passed the
letter while violating the intent) — v2 of the harness should require magnitude retention.

### Prediction robustness — the shrinkage basins are not a big-country artifact (P22)

The prediction box's one transferable mechanism is orthogonal-basin shrinkage, which pulls each
country's forecast toward its basin's **population-weighted mean**. That location statistic is
dominated inside each basin by a handful of giant countries — the same concern gate G6 encodes on
the hypothesis side. P22 swapped it for an unweighted **median** at every stage and let the ≤2021
cross-validation choose. It rejected the robust center decisively on both targets (account 6.710 →
7.831; saving 6.370 → 6.872), by **the largest margins in the whole prediction series**. The
population-weighted mean is the right basin location and the gains stacked since P11 are not a
big-country pull. The result is sharper than it looks because the evaluation metric is *unweighted*
across countries, so the median center was if anything favoured by the scoring rule and still lost.
