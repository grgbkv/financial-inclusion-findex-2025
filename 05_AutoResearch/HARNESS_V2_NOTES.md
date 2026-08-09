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
