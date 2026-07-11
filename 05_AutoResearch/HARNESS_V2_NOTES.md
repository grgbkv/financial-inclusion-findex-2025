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
