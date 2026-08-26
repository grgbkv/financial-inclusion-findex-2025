# 04_Paper — *Access Without Depth* (paper one of two)

> **Access Without Depth: Financial Inclusion 2011–2024 and Aggregation Pitfalls in the Global
> Findex Database 2025**

**[Read the PDF](findex_2025_working_paper.pdf)** · [.docx](findex_2025_working_paper.docx)

This is the **finished** paper, written from the notebook analysis. It is not the same work as
the draft in `05_AutoResearch/` — see [*Two papers, and they are different*](#two-papers-and-they-are-different).

## The argument

Beyond the decade of trends, the paper formalises **four aggregation pitfalls** in the Findex
country file:

| | pitfall | what it does |
|---|---|---|
| **P1** | disaggregation-row leakage | published group rows averaged in with country rows |
| **P2** | unbalanced composition | a changing country set read as a behavioural trend |
| **P3** | indicator-variant substitution | a narrow variant standing in for a headline definition |
| **P4** | coverage-driven missingness | averaging only surveyed economies where an item is conditional |

Each biases a level by only **1–2 percentage points in isolation**. The paper's point is what
happens in combination: plausible combinations of them **reverse the sign of headline trends**.
That is demonstrated on the original thesis analysis, whose recipes are reproduced exactly.

## Everything in it regenerates

```bash
cd 04_Paper
python3 make_paper_assets.py   # -> paper_stats.json + figures_print/*.png
python3 build_paper.py         # -> findex_2025_working_paper.docx
```

`paper_stats.json` is the single source of truth: every statistic quoted in the text is read from
it rather than typed, so the prose cannot drift from the data. `build_paper.py` emits the `.docx`;
the **PDF was exported from Word** and is the version of record.

`figures_print/` is deliberately **not** on the repo's shared visual system — restyling a
published paper's figures without being able to rebuild its PDF would make the two disagree. See
[`03_Outputs/README.md`](../03_Outputs/README.md).

## Two papers, and they are different

| | this folder | `05_AutoResearch/` |
|---|---|---|
| **Title** | *Access Without Depth* | *A balance-sheet window* |
| **Question** | what happened 2011–2024, and how aggregation choices distort the answer | what the 2021–24 saving surge was made of, and what co-moves with it |
| **Method** | one analysis, validated series by series | 98 pre-registered experiments, kept and discarded |
| **Status** | finished; PDF of record | live draft, v5, rewritten whenever the ledger outgrows it |
| **Reproduces from** | `paper_stats.json` | `findings.tsv` + the fixed harness |

They share a dataset and a methodology, and nothing else. The second grew out of the first — the
pitfall taxonomy above became the rigor gates the research loop cannot skip — but it asks a
different question and reaches its own conclusions. Neither supersedes the other.
