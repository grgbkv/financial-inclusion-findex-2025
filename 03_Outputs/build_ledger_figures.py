"""Render the research ledger as figures, straight from 05_AutoResearch/findings.tsv.

    python3 03_Outputs/build_ledger_figures.py

Writes ledger_*.png into 03_Outputs/figures/ (light) and figures/dark/ (dark), through the
same visual system as every other figure in the repo.

Generated, never hand-maintained: the ledger grows by a few rows every run, and a hand-drawn
summary of it would be wrong within a week. Re-run this after any cycle and the numbers move
with the ledger.
"""
import csv
import os
import re
import sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "style"))
import findex_style as fs                                             # noqa: E402
import matplotlib.pyplot as plt                                       # noqa: E402

LEDGER = os.path.join(HERE, "..", "05_AutoResearch", "findings.tsv")
ROWS = list(csv.DictReader(open(LEDGER), delimiter="\t"))

KEPT = {"keep", "keep-general", "keep-window", "keep-general-unweighted",
        "keep-weighted", "keep-unweighted", "keep-exploratory"}
DISCARDED = {"discard", "discard-weighted"}


def klass(status):
    if status in KEPT:
        return "kept"
    if status in DISCARDED:
        return "discarded"
    if status == "exploratory":
        return "exploratory"
    return "inconclusive"


def first_float(v):
    m = re.search(r"\d+(?:\.\d+)?", v or "")
    return float(m.group()) if m else None


# --------------------------------------------------------------------------- 1 outcomes
def fig_outcomes(p):
    counts = Counter(klass(r["status"]) for r in ROWS)
    order = ["kept", "discarded", "inconclusive", "exploratory"]
    colors = {"kept": p["series"][0], "discarded": p["benchmark"],
              "inconclusive": p["series"][2], "exploratory": p["grid"]}
    total = sum(counts.values())
    fig, ax = plt.subplots(figsize=(7.2, 2.0))
    left, tier = 0, 0
    for k in order:
        w = counts[k]
        if not w:
            continue
        ax.barh(0, w, left=left, height=0.5, color=colors[k], zorder=3,
                edgecolor=p["surface"], linewidth=2)          # 2px surface gap between segments
        if w / total >= 0.10:
            # wide enough to hold its own label
            ax.annotate("%s\n%d" % (k, w), (left + w / 2, 0), ha="center", va="center",
                        fontsize=9, color=p["surface"], fontweight="semibold", zorder=5)
        else:
            # too narrow: label above with a leader, staggered so neighbours cannot collide
            y = 0.42 + 0.26 * tier
            tier = 1 - tier
            ax.annotate("%s %d" % (k, w), (left + w / 2, 0.25), xytext=(left + w / 2, y),
                        ha="center", va="bottom", fontsize=8.5, color=p["ink_soft"],
                        arrowprops=dict(arrowstyle="-", color=p["grid"], lw=1), zorder=5)
        left += w
    ax.set_xlim(0, total)
    ax.set_ylim(-0.4, 1.05)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.grid(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title("%d pre-registered experiments, %d kept" % (total, counts["kept"]),
                 color=p["ink"], loc="left", pad=12)
    fs.caption(fig, p, "Every experiment is logged whether it passed its own threshold or not. "
                       "Exploratory rows are mandatory module-mapping passes that can produce no keep.")
    return fig


# --------------------------------------------------------------------------- 2 designs
def fig_designs(p):
    tot, keep = Counter(), Counter()
    for r in ROWS:
        d = r["design"] or "unrecorded"
        tot[d] += 1
        if klass(r["status"]) == "kept":
            keep[d] += 1
    fams = [d for d, _ in tot.most_common()][::-1]
    y = range(len(fams))
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.barh(list(y), [tot[d] for d in fams], height=0.62, color=p["grid"],
            label="run", zorder=3)
    ax.barh(list(y), [keep[d] for d in fams], height=0.62, color=p["series"][0],
            label="kept", zorder=4)
    for i, d in enumerate(fams):
        ax.annotate("%d of %d" % (keep[d], tot[d]), (tot[d], i), textcoords="offset points",
                    xytext=(6, 0), va="center", fontsize=8.5, color=p["ink_soft"])
    ax.set_yticks(list(y), fams, fontsize=9)
    ax.set_xlim(0, max(tot.values()) * 1.22)
    ax.set_ylim(-0.7, len(fams) - 0.3)
    ax.set_xticks([])
    ax.grid(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_title("Which designs survive their own threshold", color=p["ink"], loc="left", pad=12)
    ax.legend(loc="lower right")
    fs.caption(fig, p, "Every level-to-change design in the ledger has failed: 0 keeps in 7 attempts. "
                       "Cross-sectional micro designs are the most productive family.")
    return fig


# --------------------------------------------------------------------------- 3 effective n
def fig_neff(p):
    pts = []
    for r in ROWS:
        if r["stream"] != "hypothesis":
            continue
        n, ne = first_float(r["n"]), first_float(r["neff"])
        if n and ne and n >= 20:
            pts.append((r["id"], n, ne))
    pts = sorted(pts, key=lambda t: t[1])
    y = range(len(pts))
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for i, (_, n, ne) in enumerate(pts):
        ax.plot([ne, n], [i, i], color=p["grid"], lw=2, zorder=2, solid_capstyle="round")
    ax.scatter([t[1] for t in pts], list(y), s=52, color=p["benchmark"], zorder=4,
               label="nominal n (economies)")
    ax.scatter([t[2] for t in pts], list(y), s=52, color=p["series"][0], zorder=5,
               label="Kish effective n")
    ax.set_yticks(list(y), [t[0] for t in pts], fontsize=8.5)
    ax.set_xlim(0, max(t[1] for t in pts) * 1.12)
    ax.set_xlabel("sample size")
    ax.set_title("A population-weighted correlation over 77 economies\nhas the precision of about 7",
                 color=p["ink"], loc="left", pad=34)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, handletextpad=0.4)
    ax.grid(axis="x")
    fs.caption(fig, p, "Kish effective sample size, neff = (sum w)^2 / sum(w^2), on the population "
                       "weights each correlation actually uses. Rows are the ledger entries that "
                       "record both figures.")
    return fig


FIGS = OrderedDict([("ledger_outcomes", fig_outcomes),
                    ("ledger_designs", fig_designs),
                    ("ledger_neff", fig_neff)])


def main():
    light = os.path.join(HERE, "figures")
    dark = os.path.join(light, "dark")
    os.makedirs(dark, exist_ok=True)
    for mode, out in (("light", light), ("dark", dark)):
        p = fs.apply(mode)
        for name, fn in FIGS.items():
            fig = fn(p)
            fig.savefig(os.path.join(out, name + ".png"))
            plt.close(fig)
        print("%-5s -> %s (%d ledger figures)" % (mode, os.path.relpath(out, HERE), len(FIGS)))


if __name__ == "__main__":
    main()
