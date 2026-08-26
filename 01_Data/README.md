# 01_Data — the source file

`GlobalFindexDatabase2025.csv` — the World Bank's Global Findex Database 2025 country file
(15 MB, committed so the whole analysis reproduces from a clean clone).

| | |
|---|---|
| **Rows** | one per economy × survey wave × demographic slice |
| **Waves** | 2011, 2014, 2017, 2021, 2024 |
| **Economies** | 162 surveyed; **117** appear in every wave (the balanced panel) |
| **Indicator columns** | 429 |
| **Also inside** | the World Bank's own published aggregate rows (world, regions, income groups), identified by a null `regionwb24_hi` |

## Two things about this file that shape everything else

**The official aggregates are in the same file as the country rows.** Averaging without
filtering mixes published aggregates into a country mean and double-counts. Every consumer in
this repo splits them apart first — `regionwb24_hi.notna()` is the country side. The aggregate
rows are then used deliberately, as the validation layer drawn on top of every headline chart.

**The 2021 round ran into 2022 for 16 economies.** They carry `year == 2022`. Every script here
merges 2022 into the 2021 wave before anything else, following World Bank practice. Forgetting
this splits one wave into two and invents a trend.

## The path is load-bearing

Four scripts resolve this file's location relative to their own: the research harness
(`05_AutoResearch/harness.py` and `micro.py`), the paper's asset builder, and the figure builder.
The two harness modules are frozen by the research protocol and are not edited while experiments
run, so the path they point at is effectively part of the interface. Moving the file breaks all
four at once.

## Not in this repository

The Findex 2025 **individual-level microdata** (144,090 respondents), used by the micro stream in
`05_AutoResearch/`, is licensed for research use with no redistribution. It is gitignored, has
never been committed at any point in this repository's history, and must be obtained from the
[World Bank Microdata Library](https://microdata.worldbank.org/) to re-run those experiments.
Only aggregates and findings derived from it are published here.

**Citation.** Klapper, L., Singer, D., Starita, L., & Norris, A. (2025). *The Global Findex
Database 2025: Connectivity and Financial Inclusion in the Digital Economy.* Washington, DC:
World Bank.
