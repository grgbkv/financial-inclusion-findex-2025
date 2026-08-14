# Harness v2 ledger — accumulating design fixes (apply in one versioned pass, not mid-run)

1. G6 jackknife: require magnitude retention (r_droptop >= 0.5 x r_full), not just sign
   stability (lesson E4).
2. Multiple-testing budget: familywise/FDR accounting across the growing findings ledger
   before scaling past ~3 experiments/day.
3. micro.py pooled weighting: `wgt` is within-economy representative; pooling raw wgt across
   economies weights economies roughly equally, NOT by population. Pooled "global" micro rates
   (affects U1/U2 = findings rows M1/M2) should offer pop-scaled weights
   (wgt x pop_adult / economy sample n) as the default for global claims, with the
   economy-equal variant as a labeled alternative. Directions of U1/U2 are robust to this;
   exact pooled pp values carry the caveat.
4. Prediction stream: add a strict holdout discipline note — repeated test-set evaluation is
   the autoresearch game, but champion claims should also report leave-one-wave-out fit.
5. Item labels are missing for two families the agenda depends on. (a) The `fh1`/`fh2` financial-
   health polarity is still unsettled (owed since E33) — no welfare *direction* may be asserted
   until it is. (b) **Program 7 is blocked at its first step**: the microdata zip
   (`WLD_2024_FINDEX_v02_M_CSV.zip`) contains the CSV and nothing else — no questionnaire, no
   codebook — and the 133 country + 52 micro `con*` columns are bare numeric codes (1/2/8/9 with
   skip filters, verified 2026-08-09). The mandatory mapping pass cannot be completed from the
   files in the repo, so the largest untouched block stays untouchable until the WB questionnaire
   is fetched into `microdata/`. Structural identification (filter populations, response scales)
   is possible without it; item *meaning* is not, and guessing meaning would be worse than
   leaving the block alone.
6. **`fin31` mapping (E45, 2026-08-15) — INFERRED from the numbers, NOT authoritative.** The module
   has no questionnaire in the repo, so this is structural identification only; item *meaning* below
   is a reading of coverage and levels, and any experiment citing it must repeat that caveat.
   Developing-panel population-weighted levels, 2014 / 2017 / 2021 / 2024 (n economies in brackets):

   | column | 2014 | 2017 | 2021 | 2024 | reading |
   |---|---|---|---|---|---|
   | `fin31a_31b` | 7.9 | 14.8 | 18.2 | 17.6 [71] | composite of a and b; r(composite, `fin31a`) = +0.893 |
   | `fin31a` | 7.3 | 13.6 | 15.5 | 11.9 | a digital-payment channel, rising then falling |
   | `fin31b` | 1.1 | 7.0 | 7.9 | 14.5 | a second channel, still rising in 2021→24 |
   | `fin31c` | — | — | — | 0.6 [71] | **2024-only and at 0.6pp — unusable, fails the coverage floor** |
   | `fin31d` | 47.1 | 34.1 | 20.5 | 26.6 | **falls while `g20_any` rises 34.3 → 60.9 — reads as a CASH / non-digital residual, and it is the one item that correlates NEGATIVELY with the headline (−0.401 levels)** |
   | `fin31a_31b_s`, `fin31a_s`, `fin31b_s`, `fin31d_s` | see log | | | 42.0 / 36.7 / 41.6 / 60.7 | the `_s` suffix has different coverage (36–59 economies) and systematically higher levels than its unsuffixed twin — **treat suffixed and unsuffixed as DIFFERENT items, never the same concept measured twice** |

   Coverage note that matters for design: the unsuffixed items are 77 economies × four waves; the
   suffixed ones thin sharply backwards (2 economies for `fin31b_s` in 2014), so the `_s` family
   supports 2021→24 only.
