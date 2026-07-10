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
