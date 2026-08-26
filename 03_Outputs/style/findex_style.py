"""The repository's shared chart visual system: one palette, one typography, two modes.

Every repo-facing figure is rendered through this module so the set reads as one system
rather than ten independent charts. The palette is not a taste choice -- it is checked by
`validate_palette.py` (six checks: lightness band, chroma floor, CVD separation, normal-vision
floor, contrast vs surface), and the choices below record what that check forced.

Three categorical hues, and no fourth. Blue, orange and aqua validate on all pairs in both modes
(worst CVD dE 9.2 light / 9.4 dark; worst normal-vision dE 24.0 / 20.9). A fourth categorical
hue does not: every fourth-slot candidate fails the normal-vision floor of 15 in at least one
mode. So the fourth line in the regional charts -- High income -- is rendered as a NEUTRAL
BENCHMARK rather than a fourth category, which is also what it is: the ceiling the other
regions are converging toward.

The official-aggregate overlay is an annotation rather than a series. World Bank published
aggregates appear on every validated figure as hollow diamonds in neutral ink. Giving them a
categorical hue failed the checks (orange vs red: normal-vision dE 7.1) and was the wrong idea
anyway -- they are a reference layer, so they wear reference ink everywhere.

Aqua sits below the 3:1 contrast line in light mode (2.74:1 against the surface), which is the
condition under which a series owes the reader a visible direct label instead. `end_label` is
there so that label comes for free.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- palette
LIGHT = {
    "surface": "#fcfcfb",
    "ink": "#0b0b0b",
    "ink_soft": "#52514e",
    "ink_faint": "#8a8985",
    "grid": "#d8d7d2",
    "series": ["#2a78d6", "#eb6834", "#1baf7a"],   # fixed order, never cycled
    "benchmark": "#3d3d3a",                          # High income / reference series
    "official": "#52514e",                           # WB published aggregate markers
}
DARK = {
    "surface": "#1a1a19",
    "ink": "#ffffff",
    "ink_soft": "#c3c2b7",
    "ink_faint": "#8a8981",
    "grid": "#3a3a37",
    "series": ["#3987e5", "#d95926", "#199e70"],
    "benchmark": "#d5d4cb",
    "official": "#c3c2b7",
}
MODES = {"light": LIGHT, "dark": DARK}


def palette(mode="light"):
    return MODES[mode]


def apply(mode="light", base_size=9.5):
    """Install the mode's rcParams. Sans-serif, recessive axes, no top/right spines."""
    p = MODES[mode]
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans"],
        "font.size": base_size,
        "axes.titlesize": base_size + 1.5,
        "axes.titleweight": "bold",
        "axes.labelsize": base_size - 0.5,
        "axes.edgecolor": p["grid"],
        "axes.labelcolor": p["ink_soft"],
        "axes.facecolor": p["surface"],
        "figure.facecolor": p["surface"],
        "savefig.facecolor": p["surface"],
        "text.color": p["ink"],
        "xtick.color": p["ink_soft"],
        "ytick.color": p["ink_soft"],
        "xtick.labelsize": base_size - 1,
        "ytick.labelsize": base_size - 1,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": p["grid"],
        "grid.linestyle": "-",
        "grid.linewidth": 0.7,
        "grid.alpha": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "legend.frameon": False,
        "legend.fontsize": base_size - 1,
        "lines.linewidth": 2.0,          # 2px lines, per the mark spec
        "lines.solid_capstyle": "round",
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.22,
    })
    return p


# --------------------------------------------------------------------------- marks
def line(ax, s, color, label=None, marker="o", ms=4.5, **kw):
    """A 2px line with >=8px markers (ms is a radius-ish size in points: 4.5 -> 9px)."""
    return ax.plot(s.index, s.values, marker=marker, ms=ms, color=color,
                   label=label, zorder=3, **kw)


def official(ax, s, p, label=None):
    """The WB published aggregate: hollow diamonds in neutral ink. Same on every figure."""
    return ax.plot(s.index, s.values, ls="none", marker="D", ms=5, mfc="none",
                   mec=p["official"], mew=1.3, label=label, zorder=4)


def end_label(ax, s, text, color, dx=9, dy=0, weight="semibold"):
    """Direct label at the series end. Mandatory for any aqua series (relief rule)."""
    ax.annotate(text, (s.index[-1], s.iloc[-1]), textcoords="offset points",
                xytext=(dx, dy), ha="left", va="center", fontsize=8.5,
                color=color, fontweight=weight, zorder=5)


def value_labels(ax, s, p, dy=8, fmt="{:.0f}", every=None, color=None):
    """Selective value labels -- never a number on every point unless `every` says so.
    Text wears ink tokens, not the series color, unless a color is passed explicitly."""
    pts = s if every is None else s.iloc[::every]
    for x, y in pts.items():
        ax.annotate(fmt.format(y), (x, y), textcoords="offset points", xytext=(0, dy),
                    ha="center", fontsize=8, color=color or p["ink_soft"], zorder=5)


def finish(ax, p, ylabel="% of adults", xticks=None, ylim=None, xlim=None, title=None):
    if title:
        ax.set_title(title, color=p["ink"], loc="left", pad=10)
    ax.set_ylabel(ylabel)
    if xticks is not None:
        ax.set_xticks(xticks)
    if ylim:
        ax.set_ylim(*ylim)
    if xlim:
        ax.set_xlim(*xlim)
    ax.tick_params(length=0)
    for sp in ("bottom",):
        ax.spines[sp].set_color(p["grid"])
    return ax


def caption(fig, p, text, width=96):
    """Source/method text under the plot -- the figure explains itself.

    WRAPPED, and that is not cosmetic: with `savefig.bbox="tight"` a long single-line caption
    widens the saved canvas and squashes the plot into the left half of the image. Wrapping
    keeps the figure's aspect ratio the one the subplot asked for.
    """
    import textwrap
    body = "\n".join(textwrap.wrap(text, width=width))
    fig.text(0.0, -0.02, body, fontsize=7.5, color=p["ink_faint"], ha="left", va="top",
             linespacing=1.5)
