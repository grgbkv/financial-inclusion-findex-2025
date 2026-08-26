"""Regenerate every repo-facing figure, in light and dark, through one visual system.

    python3 03_Outputs/build_figures.py

Writes 03_Outputs/figures/*.png (light) and 03_Outputs/figures/dark/*.png (dark). Filenames
are unchanged from the previous hand-styled set so every existing link keeps working.

Methodology is the repository's standing one and is NOT re-decided here: the 117-economy
balanced panel, the 2022 fieldwork merged into the 2021 wave, population-weighted aggregation,
and the World Bank's own published aggregates drawn on top as a validation layer. The series
definitions match 04_Paper/make_paper_assets.py line for line, so the figures and the working
paper cannot drift apart.

Out of scope: 04_Paper/figures_print/. Those belong to a published paper whose PDF of record
cannot be rebuilt here (build_paper.py emits .docx only; the PDF was exported from Word), so
restyling them would leave the repo internally inconsistent. They stay as the paper printed them.
"""
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "style"))
import findex_style as fs                                             # noqa: E402
import matplotlib.pyplot as plt                                       # noqa: E402

DATA = os.path.join(HERE, "..", "01_Data", "GlobalFindexDatabase2025.csv")
YEARS = [2011, 2014, 2017, 2021, 2024]
DP_YEARS = [2014, 2017, 2021, 2024]

# ------------------------------------------------------------------ data (repo methodology)
df = pd.read_csv(DATA, low_memory=False)
df["year"] = df["year"].replace(2022, 2021)
countries = df[df["regionwb24_hi"].notna()].copy()
officials = df[df["regionwb24_hi"].isna()].copy()
c_all = countries[countries["group"] == "all"]
waves = c_all.groupby("countrynewwb")["year"].nunique()
panel = waves[waves == 5].index
pan_all = c_all[c_all["countrynewwb"].isin(panel)]
pan_dev = pan_all[pan_all["incomegroupwb24"] != "High income"]
pan_grp = countries[countries["countrynewwb"].isin(panel)]


def wmean(d, col, w="pop_adult"):
    s = d.dropna(subset=[col, w])
    return np.nan if s.empty else np.average(s[col], weights=s[w])


def series(frame, col, years=YEARS):
    return pd.Series({y: wmean(frame[frame["year"] == y], col) for y in years}).dropna() * 100


def off(entity, col, years=YEARS):
    d = officials[(officials["countrynewwb"] == entity) & (officials["group"] == "all")]
    return pd.Series({y: d.loc[d["year"] == y, col].squeeze() for y in years}).astype(float).dropna() * 100


REGIONS = {                       # three developing regions carry the three categorical hues
    "Sub-Saharan Africa (excluding high income)": "Sub-Saharan Africa",
    "South Asia (excluding high income)": "South Asia",
    "Latin America & Caribbean (excluding high income)": "Latin America & Caribbean",
}
BENCH = "High income"             # rendered as the neutral benchmark, not a fourth category
SRC = "Global Findex 2025 · %d-economy balanced panel, population-weighted · hollow diamonds = World Bank published aggregate" % len(panel)
SRC_NO_OFF = "Global Findex 2025 · %d-economy balanced panel, population-weighted" % len(panel)

FIGS = {}


def figure(name):
    def deco(fn):
        FIGS[name] = fn
        return fn
    return deco


# --------------------------------------------------------------------------- 1 account
@figure("fig1_account_ownership")
def _(p):
    s, o = series(pan_all, "account_t_d"), off("world", "account_t_d")
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    fs.line(ax, s, p["series"][0], label="Balanced panel (%d economies)" % len(panel))
    fs.official(ax, o, p, label="World Bank world aggregate")
    fs.value_labels(ax, s, p, fmt="{:.0f}%")
    fs.finish(ax, p, xticks=YEARS, ylim=(40, 90),
              title="Account ownership rose 28 points in thirteen years")
    ax.legend(loc="lower right")
    fs.caption(fig, p, SRC)
    return fig


# --------------------------------------------------------------------------- 2 regional
@figure("fig2_regional_account")
def _(p):
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    b = series(pan_all[pan_all["regionwb24_hi"] == BENCH], "account_t_d")
    fs.line(ax, b, p["benchmark"], ms=3.5, lw=1.6, ls=(0, (5, 2)))
    fs.end_label(ax, b, BENCH, p["benchmark"], weight="normal")
    for (reg, short), col in zip(REGIONS.items(), p["series"]):
        s = series(pan_all[pan_all["regionwb24_hi"] == reg], "account_t_d")
        fs.line(ax, s, col, ms=3.5)
        fs.end_label(ax, s, "%s  %.0f%%" % (short, s.iloc[-1]), col)
    fs.finish(ax, p, xticks=YEARS, xlim=(2010.4, 2032.5),
              title="South Asia and Sub-Saharan Africa converged fastest")
    fs.caption(fig, p, SRC_NO_OFF + " · High income dashed: the benchmark, not a peer region")
    return fig


# --------------------------------------------------------------------------- 3 mobile money
@figure("fig3_mobile_money")
def _(p):
    mmf = pan_all.copy()
    mmf["mm0"] = mmf["mobileaccount_t_d"].fillna(0)
    world = series(mmf, "mm0", DP_YEARS)
    ssa = series(pan_all[pan_all["regionwb24_hi"] == list(REGIONS)[0]], "mobileaccount_t_d", DP_YEARS)
    o = off("world", "mobileaccount_t_d", DP_YEARS)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    fs.line(ax, world, p["series"][0], label="World (non-surveyed economies counted as zero)")
    fs.line(ax, ssa, p["series"][1], marker="s", label="Sub-Saharan Africa")
    fs.official(ax, o, p, label="World Bank world aggregate")
    fs.value_labels(ax, ssa, p, fmt="{:.0f}%")
    fs.finish(ax, p, xticks=DP_YEARS, ylim=(0, 52), xlim=(2013.4, 2024.8),
              title="Mobile money is a Sub-Saharan African story")
    ax.legend(loc="upper left")
    fs.caption(fig, p, SRC + " · averaging only surveyed economies would overstate the world figure ~2x")
    return fig


# --------------------------------------------------------------------------- 4 digital payments
@figure("fig4_digital_payments")
def _(p):
    s = series(pan_dev, "g20_any", DP_YEARS)
    o = off("Developing economies", "g20_any", DP_YEARS)
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    fs.line(ax, s, p["series"][0], label="Developing balanced panel")
    fs.official(ax, o, p, label="World Bank developing aggregate")
    fs.value_labels(ax, s, p, fmt="{:.0f}%")
    fs.finish(ax, p, xticks=DP_YEARS, ylim=(0, 75),
              title="Digital payments reached 61% of adults in developing economies")
    ax.legend(loc="lower right")
    fs.caption(fig, p, SRC)
    return fig


# --------------------------------------------------------------------------- 5 regional DP
@figure("fig5_regional_digital_payments")
def _(p):
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    b = series(pan_all[pan_all["regionwb24_hi"] == BENCH], "g20_any", [2014, 2017, 2021])
    fs.line(ax, b, p["benchmark"], ms=3.5, lw=1.6, ls=(0, (5, 2)))
    fs.end_label(ax, b, "High income (series ends 2021)", p["benchmark"], weight="normal")
    for (reg, short), col in zip(REGIONS.items(), p["series"]):
        s = series(pan_all[pan_all["regionwb24_hi"] == reg], "g20_any", DP_YEARS)
        fs.line(ax, s, col, ms=3.5)
        fs.end_label(ax, s, "%s  %.0f%%" % (short, s.iloc[-1]), col)
    fs.finish(ax, p, xticks=DP_YEARS, xlim=(2013.5, 2032.0),
              title="Digital-payment adoption by region")
    fs.caption(fig, p, SRC_NO_OFF + " · the high-income line stops in 2021: only 5 of 40 panel economies report the item in 2024")
    return fig


# --------------------------------------------------------------------------- 6 saving/borrowing
@figure("fig6_saving_borrowing")
def _(p):
    sav, bor = series(pan_dev, "fin17a_17a1_d"), series(pan_dev, "fin22a_22a1_22g_d", DP_YEARS)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    fs.line(ax, sav, p["series"][0], label="Saved formally")
    fs.line(ax, bor, p["series"][1], marker="s", label="Borrowed formally")
    fs.official(ax, off("Developing economies", "fin17a_17a1_d"), p,
                label="World Bank developing aggregate")
    fs.official(ax, off("Developing economies", "fin22a_22a1_22g_d", DP_YEARS), p)
    fs.value_labels(ax, sav.iloc[:-1], p, fmt="{:.0f}%")
    fs.end_label(ax, sav, "%.0f%%" % sav.iloc[-1], p["series"][0], dx=11)
    ax.annotate("+%.1f pp\n2021 to 2024" % (sav.iloc[-1] - sav.iloc[-2]), (2018.9, 35),
                ha="center", fontsize=8.5, color=p["series"][0], fontweight="semibold")
    fs.finish(ax, p, xticks=YEARS, ylim=(0, 44), xlim=(2010.4, 2025.4),
              title="Formal saving surged in the last wave")
    ax.legend(loc="lower right")
    fs.caption(fig, p, SRC)
    return fig


# --------------------------------------------------------------------------- 7 inactivity
@figure("fig7_inactivity")
def _(p):
    ratio = (series(pan_dev, "inactive_t_d", DP_YEARS) / series(pan_dev, "account_t_d", DP_YEARS)) * 100
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    bars = ax.bar([str(y) for y in ratio.index], ratio.values, width=0.55,
                  color=p["series"][0], zorder=3)
    for b in bars:
        ax.annotate("%.0f%%" % b.get_height(), (b.get_x() + b.get_width() / 2, b.get_height()),
                    textcoords="offset points", xytext=(0, 5), ha="center",
                    fontsize=8.5, color=p["ink_soft"])
    fs.finish(ax, p, ylabel="% of accountholders", ylim=(0, max(ratio) * 1.25),
              title="Dormant accounts as a share of accounts held")
    fs.caption(fig, p, SRC_NO_OFF + " · developing panel; inactive_t_d divided by account_t_d")
    return fig


# --------------------------------------------------------------------------- 8 resilience
@figure("fig8_resilience")
def _(p):
    rp, ro = series(pan_dev, "fin24aSD_ND", [2021, 2024]), off("Developing economies", "fin24aSD_ND", [2021, 2024])
    x = np.arange(2)
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    b1 = ax.bar(x - 0.17, rp.values, 0.30, color=p["series"][0], label="Balanced panel", zorder=3)
    b2 = ax.bar(x + 0.17, ro.values, 0.30, color=p["benchmark"], label="World Bank aggregate", zorder=3)
    for bars in (b1, b2):
        for b in bars:
            ax.annotate("%.0f%%" % b.get_height(), (b.get_x() + b.get_width() / 2, b.get_height()),
                        textcoords="offset points", xytext=(0, 5), ha="center",
                        fontsize=8.5, color=p["ink_soft"])
    ax.set_xticks(x, ["2021", "2024"])
    fs.finish(ax, p, ylim=(0, 76), xlim=(-0.6, 1.6), title="Resilience is the unfinished agenda")
    ax.legend(loc="upper center", ncol=2)
    fs.caption(fig, p, SRC_NO_OFF + " · adults who could raise emergency funds; broadly flat while access expanded")
    return fig


# --------------------------------------------------------------------------- 9/10 gaps
def _gap_figure(p, hi_key, lo_key, hi_lab, lo_lab, title, note):
    hi = series(pan_grp[pan_grp["group2"] == hi_key], "account_t_d")
    lo = series(pan_grp[pan_grp["group2"] == lo_key], "account_t_d")
    gap = hi - lo
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.3), gridspec_kw={"width_ratios": [3, 2]})
    fig.suptitle(title, x=0.0, ha="left", fontsize=11, fontweight="bold", color=p["ink"], y=1.04)
    fs.line(a1, hi, p["series"][0], marker="s", ms=4, label=hi_lab)
    fs.line(a1, lo, p["series"][1], ms=4, label=lo_lab)
    a1.fill_between(hi.index, hi.values, lo.values, color=p["series"][1], alpha=0.10, zorder=2)
    fs.finish(a1, p, xticks=YEARS)
    a1.legend(loc="lower right")
    bars = a2.bar([str(y) for y in gap.index], gap.values, width=0.55, color=p["series"][1], zorder=3)
    for b in bars:
        a2.annotate("%.1f" % b.get_height(), (b.get_x() + b.get_width() / 2, b.get_height()),
                    textcoords="offset points", xytext=(0, 4), ha="center",
                    fontsize=8, color=p["ink_soft"])
    fs.finish(a2, p, ylabel="gap, percentage points", ylim=(0, max(gap) * 1.3))
    a2.tick_params(axis="x", labelsize=8)
    fig.subplots_adjust(wspace=0.45)
    fs.caption(fig, p, SRC_NO_OFF + " · " + note)
    return fig


@figure("fig9_gender_gap")
def _(p):
    return _gap_figure(p, "men", "women", "Men", "Women",
                       "The gender gap in account ownership halved",
                       "within-country group rows, population-weighted across the panel")


@figure("fig10_income_gap")
def _(p):
    return _gap_figure(p, "richest 60%", "poorest 40%", "Richest 60%", "Poorest 40%",
                       "The income gap is the wider divide",
                       "richest 60% minus poorest 40% of households, account ownership")


# --------------------------------------------------------------------------- run
def main():
    out_light = os.path.join(HERE, "figures")
    out_dark = os.path.join(out_light, "dark")
    os.makedirs(out_dark, exist_ok=True)
    for mode, out in (("light", out_light), ("dark", out_dark)):
        p = fs.apply(mode)
        for name, fn in FIGS.items():
            fig = fn(p)
            fig.savefig(os.path.join(out, name + ".png"))
            plt.close(fig)
        print("%-5s -> %s (%d figures)" % (mode, os.path.relpath(out, HERE), len(FIGS)))


if __name__ == "__main__":
    main()
