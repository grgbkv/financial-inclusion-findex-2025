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
7. **`fin34` mapping (E47, 2026-08-15) — INFERRED from the numbers, NOT authoritative.** Same caveat
   as item 6: no questionnaire in the repo, so this is structural identification only. The module
   label is "wage payment modes"; *which* mode each letter is remains unknown, and no behavioural
   reading may be attached to any of them. Developing-panel population-weighted levels,
   2014 / 2017 / 2021 / 2024:

   | column | 2014 | 2017 | 2021 | 2024 | reading |
   |---|---|---|---|---|---|
   | `fin34a` | 8.3 | 13.1 | 18.3 | 14.1 [71] | tracks the digital headline closely (r_level +0.751/+0.665 in 2024; +0.80 to +0.94 weighted in every wave) — a digital-aligned wage mode |
   | `fin34b` | 0.4 | 3.9 | 3.0 | 8.1 [71] | the fastest riser in the module; **`mixed-lens`** against the headline (+0.832 wtd / +0.723 unwtd — restatement on one lens, aligned on the other) |
   | **`fin34c`** | **15.9** | **11.8** | **8.0** | **15.2** [71] | **the module's counter-moving item: r_level −0.552 wtd / −0.486 unwtd vs `g20_any` in 2024, through G6 (−0.553), largest leave-one-out Brazil +0.096. The orientation EMERGES — +0.028/−0.122 (2014), −0.419/−0.323 (2017), −0.690/−0.367 (2021), −0.552/−0.486 (2024). Reads as a non-digital wage mode.** Against `account_t_d` it is `mixed-lens` (+0.024 wtd / −0.416 unwtd) with **India alone worth −0.597** |
   | `fin34d` | 6.0 | 1.0 | 0.4 | **0.1** [71] | **collapses to a floor — 0.1pp of adults in 2024, fails a 1.0pp coverage floor. Unusable as a margin.** |
   | `fin34a_s` / `fin34b_s` / `fin34c_s` / `fin34d_s` | 39.0 / — / 62.9 / 33.4 | | | 47.9 [42] / 44.5 [19] / 57.9 [30] / — | as with `fin31`, the `_s` suffix has different coverage and systematically higher levels — **different items, not the same concept measured twice**. `fin34d_s` exists only in 2014 (13 economies); `fin34b_s` only from 2017 and thin |

   Design note: the four unsuffixed items are 77 economies × four waves (71 in 2024) and support Δ
   designs and earlier-window replication. The `_s` family does not.
8. **Two counter-moving margins, in two modules (E45 + E47 + E48), 2026-08-15.** `fin31d` and
   `fin34c` are the only country-file items found so far whose *level* runs against `g20_any` on both
   lenses. Their decade changes correlate **+0.515 wtd / +0.389 unwtd**, and the partial controlling
   for Δ`g20_any` **strengthens** to +0.597 / +0.383. But E48's primary is `discard-weighted`: neither
   margin's *change* tracks the headline's *change* on the unweighted lens. **Anyone building on this:
   the counter-moving finding is a level/composition fact plus a cross-module change fact, and
   explicitly NOT a "digital displaces cash within countries" fact.** The structural label "cash" is a
   reading of two negative signs and nothing more.
