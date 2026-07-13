# Extensions draft — autoresearch session, 2026-07-11 (branch `autoresearch/jul11`)

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

**The channel is not mobile-money-specific (E10).** The surge co-moves just as strongly with
the growth of *digital wage rails*: weighted r = 0.79 between Δsaving and Δ(share of adults
paid private-sector wages into an account) 2021→2024 (n = 71; jackknife barely moves,
0.79 → 0.79 without the top-5). Terciles of Δwage-digitalization gain +3.2 / +10.9 / +13.6 pp
of formal saving. Reading: the surge is a broad-based digitalization signature across multiple
account on-ramps (mobile money *and* formal wage rails), not one rail — account growth is a
plausible common driver of both sides (descriptive, not controlled).

**And the deepening is broad, not saving-specific (E11).** Formal *borrowing* and formal
*saving* grew together across the panel 2021→2024: weighted r = 0.40 between Δ(formal
borrowing) and Δ(formal saving) (n = 76; jackknife *strengthens* to 0.47 without the top-5, so
this is no big-country artifact). Reading: the surge reflects genuine balance-sheet deepening
on both sides of the household ledger, not a one-sided store-of-value shift — reinforcing the
digitalization-channel story above.

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

Reading: the paper's "access without depth" theme has a consistent demographic signature —
income gates *access*, education gates *depth*, and age gates *digital usage*. All are
single-wave 2024 cross-sectional descriptions (no trend claims).

## Prediction box — the surge was a regime change, not a trend (P1–P3)

A fixed forecasting task (predict each country's 2024 value from waves ≤ 2021) quantifies
how *new* the 2024 wave's information is:

| Target | Persistence MAE | Best model MAE | What worked |
|---|---:|---:|---|
| Account ownership | 5.58 pp | **5.14 pp** | light income-group-mean shrinkage, k=0.1 (P7) |
| Resilience | 6.68 pp | **6.63 pp** | light region-mean shrinkage, k=0.1 (P5) |
| Formal saving | 9.77 pp | **8.45 pp** | damped trend (λ=0.5) (P2) |

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
the regional mean (P5).

## Honest nulls worth one sentence each

- Mobile-money growth ⇏ resilience gains within the window (E2).
- Gender-gap changes 2021→2024 are large (σ = 7.4 pp) but orthogonal to mobile-money growth (E3).
- No systematic reversion of the unusually narrow 2021 income gap proportional to the
  earlier poorest-40 jump (E6).
- The dormancy "J-curve" after account drives is real population-weighted but is a
  large-country (India-drive) phenomenon, not a cross-country regularity (E4).

## Methods note for v2

The loop enforced the paper's pitfall taxonomy as automated gates (indicator-variant
declaration, coverage thresholds, official-aggregate cross-checks, jackknife stability) plus
pre-registration of every hypothesis before testing; discards are logged, not hidden. One
gate-design lesson: sign-stability alone is too weak a jackknife criterion (E4 passed the
letter while violating the intent) — v2 of the harness should require magnitude retention.
