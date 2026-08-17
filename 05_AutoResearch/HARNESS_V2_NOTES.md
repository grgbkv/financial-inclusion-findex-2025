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
9. **`fin` catch-all mapping (E49, 2026-08-17) — EXPLORATORY, INFERRED from the numbers, NOT
   authoritative.** Same caveat as items 6 and 7: no questionnaire in the repo, so this is structural
   identification only, and the module has no label at all in `coverage.py` — it is the residue left
   after every `finNN` prefix with a label is stripped out. **93 columns, of which 24 clear ≥ 3 waves
   at ≥ 70 developing economies**; the other 69 are 2024-only, 27-economy, or `_s`-suffixed and thin.
   Developing-panel population-weighted levels (countries in brackets), and the 2024 four-way
   orientation against `g20_any` (weighted / unweighted):

   | column | waves | 2011 | 2014 | 2017 | 2021 | 2024 | vs `g20_any` 2024 | class |
   |---|---|---|---|---|---|---|---|---|
   | `fin2_t_d` | **5** | 24.0 | 32.9 | 41.6 | 44.7 | 50.5 [77] | +0.883 / +0.669 | `mixed-lens` restatement/aligned |
   | `fin10` | **5** | 6.9 | 10.0 | 10.7 | 16.5 | 18.3 [77] | +0.847 / +0.516 | `mixed-lens` restatement/aligned (drop China −0.267) |
   | `fin26a` | 3 | — | — | 16.3 | 29.1 | 34.6 [76] | +0.933 / +0.852 | **`restatement`** — a re-description of the digital headline; do not use as an independent margin |
   | `fin30` | 4 | — | 57.0 | 54.2 | 49.1 | 45.3 [71] | +0.254 / +0.306 | `mixed-lens` independent/aligned — **the module's one large declining margin** (−11.7pp over the decade) and it is *not* counter-moving |
   | `fin42` | 4 | — | 24.6 | 14.7 | 10.8 | 13.4 [71] | −0.001 / −0.089 | `independent` — falls 24.6 → 10.8 then rebounds to 13.4, the same last-window rebound as `fin31d`/`fin34c` (agenda 7.8) |
   | `fin42_acc` | 4 | — | 2.1 | 2.8 | 2.6 | 4.0 [71] | +0.435 / +0.477 | `aligned` |
   | `fin37` | 4 | — | 13.0 | 12.4 | 16.6 | 16.6 [71] | +0.317 / +0.395 | `aligned` |
   | `fin37_38` | 3 | — | — | 16.4 | 20.1 | 20.1 [71] | +0.376 / +0.486 | `aligned` |
   | `fin38` | 3 | — | — | 7.0 | 6.9 | 5.5 [71] | +0.288 / +0.339 | `mixed-lens` independent/aligned |
   | `fin37_39_acc` / `fin37_38_39_acc` / `fin38_39_acc` | 4/3/3 | — | 7.2 | 7.8 / 10.4 / 4.9 | 10.6 / 13.1 / 5.1 | 11.8 / 14.3 / 4.2 [71] | +0.436 / +0.502 / +0.414 (wtd) | all `aligned` |
   | `fin37_39a` / `fin37_38_39a` / `fin38_39a` | 4/3/3 | — | 4.9 | 6.6 / 8.9 / 4.4 | 9.0 / 11.3 / 4.7 | 10.5 / 12.9 / 3.9 [71] | +0.403 / +0.461 / +0.424 | all `aligned` |
   | `fin37_39b` / `fin37_38_39b` / `fin38_39b` | 4/3/3 | — | 0.2 | 0.6 / 0.8 / 0.3 | 2.2 / 2.4 / 0.6 | 2.4 / 2.8 / 0.8 [71] | +0.716 / +0.719 / +0.445 | all `aligned`, the `b` items being the module's fastest risers off a near-zero base |
   | `fin37_39c` / `fin37_38_39c` / `fin38_39c` | 4/3/3 | — | 4.8 | 2.2 / 3.1 / 1.4 | 2.6 / 3.0 / 0.8 | 2.2 / 2.6 / 0.7 [71] | −0.131 / −0.135 / −0.083 | all `independent` — the **only** items with a negative weighted sign, and none reaches −0.30 on either lens |
   | `fin37_39d` / `fin37_38_39d` / `fin38_39d` | 4/3/3 | — | 3.6 | 1.1 / 1.3 / 0.4 | 0.8 / 1.0 / 0.2 | 0.5 / 0.6 / 0.2 [71] | +0.071 / +0.090 / +0.012 | `independent`, but **all three are at or below a 1.0pp weighted level in 2024 and fail the `fin34d` usability floor** |

   **Structure that is safe to state.** The `fin37` / `fin38` / `fin39` items compose: `fin37_38`,
   `fin37_39x`, `fin38_39x` and `fin37_38_39x` are intersections or unions of the base items, which
   is why they classify together and why their correlations are not independent tests. **Any future
   experiment on this family must pick ONE level of the composition and say which**; correlating a
   parent with its own component is the redundancy trap E45 was written to catch. The `a`/`b`/`c`/`d`
   suffixes behave consistently across all three composites (a and b rise and are aligned, c and d
   fall and are independent-to-slightly-negative), which is the strongest structural evidence in the
   table that the letters are the same four categories throughout.

   **What the screen did NOT find.** No `fin` item is counter-moving against the digital headline on
   both lenses. Against `account_t_d` the `c` items go further negative on the weighted lens
   (`fin37_39c` −0.283, `fin37_38_39c` −0.261) and stay near zero unweighted (−0.119, −0.101), with
   **India alone worth +0.19 and +0.16** — a weighting artifact, not a margin.
