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

## Prediction box — the surge was a regime change, not a trend (P1–P3)

A fixed forecasting task (predict each country's 2024 value from waves ≤ 2021) quantifies
how *new* the 2024 wave's information is:

| Target | Persistence MAE | Best model MAE | What worked |
|---|---:|---:|---|
| Account ownership | 5.58 pp | 5.58 pp | nothing beat persistence (growth decelerates; trend overshoots) |
| Resilience | 6.68 pp | 6.68 pp | nothing (no 2017 history for the indicator) |
| Formal saving | 9.77 pp | **8.45 pp** | damped trend (λ=0.5) |

A mobile-money-informed growth model fit on the 2017→2021 transition **failed** (9.75 pp):
the contemporaneous saving–mobile-money correlation of Extension 1 was not forecastable from
the previous transition. The surge is genuinely new 2024-wave information — a regime change,
consistent with the definitional expansion plus post-pandemic saving behavior.

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
