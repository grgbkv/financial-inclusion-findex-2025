# Parked ideas — capture only, not scheduled

## 2026-07-11 — Literature into the org / domain model in the MLX lab (Georgy)

Idea as stated: select and add the current financial-inclusion economics literature to "the
trained model" — i.e., combine dataset + microdata + reports + outside literature, and use
lab #6 (autoresearch-mlx, local GPU training) with that corpus.

Two distinct executions hiding inside it, to be decided when picked up:

**(a) Train the tiny model ON the domain corpus** — swap autoresearch-mlx's generic corpus
for a financial-inclusion text corpus (Findex reports 2011-2025, key papers, policy reports).
The loop mechanics work unchanged (val_bpb on held-out domain text). Honest expected value:
a learning/portfolio experiment about domain adaptation in small LMs — the resulting 11M-param
model imitates domain prose but cannot know facts or reason; it will not advance the Findex
research itself. Legitimate use of the gym; Karpathy's README explicitly invites corpus swaps.

**(b) Give the research org ACCESS TO the literature** (retrieval, not training) — build a
curated corpus (papers, Findex reports, working papers incl. our own) with search, and add a
protocol step: before pre-registering, check prior evidence; after a keep, position the
finding against the literature (replicates / contradicts / novel). This is the version with
real research payoff: novelty checks, literature-grounded pre-registrations, and citations
for EXTENSIONS_DRAFT v2. No GPU involved; the "model" consuming the literature is the frontier
agent running the org.

Recommendation recorded at capture time: (b) is the substance, (a) is the gym. They are
complementary, not competing.
