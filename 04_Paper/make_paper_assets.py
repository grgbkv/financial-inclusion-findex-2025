"""Compute every statistic cited in the working paper and render print-grade figures.

Single source of truth: writes paper_stats.json and figures_print/*.png.
Run from 04_Paper/:  python3 make_paper_assets.py
"""
import json
import os

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- style
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10.5,
    'axes.titlesize': 12,
    'axes.labelsize': 10.5,
    'axes.grid': True,
    'grid.linestyle': '--',
    'grid.alpha': 0.35,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})
FIG = os.path.join(os.path.dirname(__file__), 'figures_print')
os.makedirs(FIG, exist_ok=True)

# ---------------------------------------------------------------- data
DATA = os.path.join(os.path.dirname(__file__), '..', '01_Data', 'GlobalFindexDatabase2025.csv')
df = pd.read_csv(DATA, low_memory=False)
df_raw_years = df.copy()                     # before wave merge (for pitfall P2/compound demos)
df['year'] = df['year'].replace(2022, 2021)

countries = df[df['regionwb24_hi'].notna()].copy()
official = df[df['regionwb24_hi'].isna()].copy()

YEARS = [2011, 2014, 2017, 2021, 2024]
c_all = countries[countries['group'] == 'all']
waves = c_all.groupby('countrynewwb')['year'].nunique()
panel = waves[waves == 5].index
pan_all = c_all[c_all['countrynewwb'].isin(panel)]
pan_dev = pan_all[pan_all['incomegroupwb24'] != 'High income']
pan_grp = countries[countries['countrynewwb'].isin(panel)]


def wmean(d, col, w='pop_adult'):
    s = d.dropna(subset=[col, w])
    return np.nan if s.empty else np.average(s[col], weights=s[w])


def series(frame, col, years=YEARS):
    return pd.Series({y: wmean(frame[frame['year'] == y], col) for y in years}).dropna() * 100


def off_series(entity, col, years=YEARS):
    d = official[(official['countrynewwb'] == entity) & (official['group'] == 'all')]
    return pd.Series({y: d.loc[d['year'] == y, col].squeeze() for y in years}).astype(float).dropna() * 100


S = {}  # everything cited in the paper

# ---------------------------------------------------------------- core panel facts
S['n_economies'] = int(c_all['countrynewwb'].nunique())
S['n_panel'] = int(len(panel))
S['n_panel_dev'] = int(pan_dev['countrynewwb'].nunique())
S['panel_coverage_2024'] = round(float(
    pan_all[pan_all['year'] == 2024]['pop_adult'].sum()
    / c_all[c_all['year'] == 2024]['pop_adult'].sum()) * 100, 1)
S['economies_per_wave'] = {int(y): int(n) for y, n in
                           c_all.groupby('year')['countrynewwb'].nunique().items()}
S['n_delayed_2022'] = int(df_raw_years.loc[df_raw_years['year'] == 2022, 'countrynewwb'].nunique())

# account ownership
acc_p = series(pan_all, 'account_t_d')
acc_o = off_series('world', 'account_t_d')
S['account_panel'] = acc_p.round(1).to_dict()
S['account_official'] = acc_o.round(1).to_dict()
S['account_maxdev'] = round(float((acc_p - acc_o).abs().max()), 1)

# adults with accounts, absolute (billions), panel
adults = {}
for y in [2011, 2024]:
    d = pan_all[pan_all['year'] == y].dropna(subset=['account_t_d', 'pop_adult'])
    adults[y] = float((d['account_t_d'] * d['pop_adult']).sum() / 1e9)
S['adults_with_accounts_bn'] = {y: round(v, 2) for y, v in adults.items()}

# regional account
REG = {
    'High income': 'High income',
    'Sub-Saharan Africa (excluding high income)': 'Sub-Saharan Africa (excluding high income)',
    'South Asia (excluding high income)': 'South Asia',
    'Latin America & Caribbean (excluding high income)': 'Latin America & Caribbean (excluding high income)',
}
SHORT = {'High income': 'High income',
         'Sub-Saharan Africa (excluding high income)': 'Sub-Saharan Africa',
         'South Asia (excluding high income)': 'South Asia',
         'Latin America & Caribbean (excluding high income)': 'Latin America & Caribbean'}
S['regional_account'] = {}
for reg in REG:
    s = series(pan_all[pan_all['regionwb24_hi'] == reg], 'account_t_d')
    S['regional_account'][SHORT[reg]] = s.round(1).to_dict()

# mobile money
mm_naive = series(pan_all, 'mobileaccount_t_d', [2014, 2017, 2021, 2024])
mmf = pan_all.copy(); mmf['mm0'] = mmf['mobileaccount_t_d'].fillna(0)
mm_fill = series(mmf, 'mm0', [2014, 2017, 2021, 2024])
mm_off = off_series('world', 'mobileaccount_t_d', [2014, 2017, 2021, 2024])
mm_ssa = series(pan_all[pan_all['regionwb24_hi'] == 'Sub-Saharan Africa (excluding high income)'],
                'mobileaccount_t_d', [2014, 2017, 2021, 2024])
S['mm_naive'] = mm_naive.round(1).to_dict()
S['mm_filled'] = mm_fill.round(1).to_dict()
S['mm_official'] = mm_off.round(1).to_dict()
S['mm_ssa'] = mm_ssa.round(1).to_dict()
ssa24 = pan_all[(pan_all['regionwb24_hi'] == 'Sub-Saharan Africa (excluding high income)')
                & (pan_all['year'] == 2024)]
S['ssa_fiaccount_2024'] = round(float(wmean(ssa24, 'fiaccount_t_d')) * 100, 1)

# usage
dp_dev = series(pan_dev, 'g20_any', [2014, 2017, 2021, 2024])
S['dp_dev'] = dp_dev.round(1).to_dict()
S['dp_dev_official'] = off_series('Developing economies', 'g20_any', [2014, 2017, 2021, 2024]).round(1).to_dict()
S['dp_regional'] = {}
for reg in REG:
    yrs = [2014, 2017, 2021] if reg == 'High income' else [2014, 2017, 2021, 2024]
    S['dp_regional'][SHORT[reg]] = series(pan_all[pan_all['regionwb24_hi'] == reg], 'g20_any', yrs).round(1).to_dict()
hi_pan = pan_all[pan_all['incomegroupwb24'] == 'High income']
S['hi_g20_coverage'] = {int(y): int(n) for y, n in hi_pan.groupby('year')['g20_any'].count().items() if y >= 2014}
S['n_hi_panel'] = int(hi_pan['countrynewwb'].nunique())

sav = series(pan_dev, 'fin17a_17a1_d')
bor = series(pan_dev, 'fin22a_22a1_22g_d', [2014, 2017, 2021, 2024])
S['sav_dev'] = sav.round(1).to_dict()
S['bor_dev'] = bor.round(1).to_dict()
S['sav_dev_official'] = off_series('Developing economies', 'fin17a_17a1_d').round(1).to_dict()
S['bor_dev_official'] = off_series('Developing economies', 'fin22a_22a1_22g_d', [2014, 2017, 2021, 2024]).round(1).to_dict()
S['sav_narrow_dev'] = series(pan_dev, 'fin17a', [2021, 2024]).round(1).to_dict()

inact = series(pan_dev, 'inactive_t_d', [2014, 2017, 2021, 2024])
accd = series(pan_dev, 'account_t_d', [2014, 2017, 2021, 2024])
S['inactivity_ratio'] = (inact / accd * 100).round(1).to_dict()

# resilience
res_p = series(pan_dev, 'fin24aSD_ND', [2021, 2024])
res_o = off_series('Developing economies', 'fin24aSD_ND', [2021, 2024])
S['res_panel'] = res_p.round(1).to_dict()
S['res_official'] = res_o.round(1).to_dict()

# gaps
men = series(pan_grp[pan_grp['group2'] == 'men'], 'account_t_d')
women = series(pan_grp[pan_grp['group2'] == 'women'], 'account_t_d')
rich = series(pan_grp[pan_grp['group2'] == 'richest 60%'], 'account_t_d')
poor = series(pan_grp[pan_grp['group2'] == 'poorest 40%'], 'account_t_d')
S['men'] = men.round(1).to_dict(); S['women'] = women.round(1).to_dict()
S['gender_gap'] = (men - women).round(1).to_dict()
S['rich'] = rich.round(1).to_dict(); S['poor'] = poor.round(1).to_dict()
S['income_gap'] = (rich - poor).round(1).to_dict()

# ---------------------------------------------------------------- pitfalls (Table 3)
# P1 disaggregation-row leakage: resilience, developing panel, all group rows vs group=='all'
pan_grp_dev = pan_grp[pan_grp['incomegroupwb24'] != 'High income']
S['P1_naive'] = {y: round(float(wmean(pan_grp_dev[pan_grp_dev['year'] == y], 'fin24aSD_ND')) * 100, 1)
                 for y in [2021, 2024]}
S['P1_correct'] = S['res_panel']

# P2 unbalanced composition: formal borrowing, developing, all surveyed per wave vs panel
dev_all_unbal = c_all[c_all['incomegroupwb24'] != 'High income']
S['P2_naive'] = {y: round(float(wmean(dev_all_unbal[dev_all_unbal['year'] == y], 'fin22a_22a1_22g_d')) * 100, 1)
                 for y in [2021, 2024]}
S['P2_correct'] = {y: S['bor_dev'][y] for y in [2021, 2024]}

# P3 indicator variant: formal saving, developing panel, narrow vs headline definition
S['P3_naive'] = S['sav_narrow_dev']
S['P3_correct'] = {y: S['sav_dev'][y] for y in [2021, 2024]}

# P4 coverage-driven missingness: global mobile money 2024, naive vs zero-filled vs official
S['P4'] = {'naive_2024': S['mm_naive'][2024], 'filled_2024': S['mm_filled'][2024],
           'official_2024': S['mm_official'][2024]}

# Compound: the original study's recipes, reproduced exactly
d21 = df[df['year'] == 2021]; d24 = df[df['year'] == 2024]
S['orig_resilience'] = {2021: round(float(wmean(d21, 'fin24aSD_ND')) * 100, 1),
                        2024: round(float(wmean(d24, 'fin24aSD_ND')) * 100, 1)}
g_all = df[df['group'] == 'all']
S['orig_borrowing'] = {y: round(float(wmean(g_all[g_all['year'] == y], 'fin22a')) * 100, 1)
                       for y in [2021, 2024]}
S['orig_mm_2024'] = round(float(wmean(d24, 'mobileaccount_t_d')) * 100, 1)
hi_all_rows = df[df['regionwb24_hi'] == 'High income']
S['orig_hi_dp'] = {y: round(float(wmean(hi_all_rows[hi_all_rows['year'] == y], 'g20_any')) * 100, 1)
                   for y in [2021, 2024]}

# ---------------------------------------------------------------- figures
# Print sizing: ~5.2-5.6 in wide, compact heights, direct line-end labels
plt.rcParams.update({'font.size': 9, 'axes.labelsize': 9})

def end_label(ax, x, y, text, color, dy=0):
    ax.annotate(text, (x, y), textcoords='offset points', xytext=(11, dy),
                ha='left', va='center', fontsize=8, color=color)

# Fig 1 account ownership
fig, ax = plt.subplots(figsize=(5.2, 2.7))
ax.plot(acc_p.index, acc_p, marker='o', ms=4, lw=1.8, color='#1f4e79',
        label=f'Balanced panel ({len(panel)} economies)')
ax.plot(acc_o.index, acc_o, ls='none', marker='D', ms=5, mfc='none', color='#c0392b',
        label='WB official world aggregate')
for x, y in acc_p.items():
    ax.annotate(f'{y:.1f}', (x, y), textcoords='offset points', xytext=(0, 6),
                ha='center', fontsize=8)
ax.set_ylabel('% of adults'); ax.set_ylim(42, 88); ax.set_xticks(YEARS)
ax.legend(loc='lower right', frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(f'{FIG}/fig1_account.png'); plt.close(fig)

# Fig 2 regional account: direct end labels, no legend
COLORS = {'High income': '#2c3e50', 'Sub-Saharan Africa': '#e67e22',
          'South Asia': '#27ae60', 'LAC': '#2980b9'}
LBL = {'High income': 'High income',
       'Sub-Saharan Africa (excluding high income)': 'Sub-Saharan Africa',
       'South Asia (excluding high income)': 'South Asia',
       'Latin America & Caribbean (excluding high income)': 'LAC'}
fig, ax = plt.subplots(figsize=(5.4, 2.9))
for reg, agg in REG.items():
    lab = LBL[reg]
    s = series(pan_all[pan_all['regionwb24_hi'] == reg], 'account_t_d')
    o = off_series(agg, 'account_t_d')
    ax.plot(s.index, s, marker='o', ms=3.5, lw=1.8, color=COLORS[lab])
    ax.plot(o.index, o, ls='none', marker='D', ms=4.5, mfc='none', color=COLORS[lab], alpha=0.6)
    end_label(ax, s.index[-1], s.iloc[-1], lab, COLORS[lab])
ax.set_ylabel('% of adults'); ax.set_xticks(YEARS); ax.set_xlim(2010.3, 2029.5)
fig.tight_layout(); fig.savefig(f'{FIG}/fig2_regional.png'); plt.close(fig)

# Fig 3 mobile money
fig, ax = plt.subplots(figsize=(5.2, 2.7))
ax.plot(mm_fill.index, mm_fill, marker='o', ms=4, lw=1.8, color='#8e44ad', label='World')
ax.plot(mm_ssa.index, mm_ssa, marker='s', ms=4, lw=1.8, color='#e67e22', label='Sub-Saharan Africa')
ax.plot(mm_off.index, mm_off, ls='none', marker='D', ms=5, mfc='none', color='#c0392b',
        label='WB official (world)')
for x, y in mm_fill.items():
    if x == 2024:
        ax.annotate(f'{y:.1f}', (x, y), textcoords='offset points', xytext=(9, -3),
                    ha='left', fontsize=8)
    else:
        ax.annotate(f'{y:.1f}', (x, y), textcoords='offset points',
                    xytext=(0, -11 if y > 6 else 6), ha='center', fontsize=8)
for x, y in mm_ssa.items():
    ax.annotate(f'{y:.1f}', (x, y), textcoords='offset points', xytext=(0, 6),
                ha='center', fontsize=8)
ax.set_ylabel('% of adults'); ax.set_xticks([2014, 2017, 2021, 2024]); ax.set_ylim(0, 50)
ax.set_xlim(2013.3, 2025.3)
ax.legend(frameon=False, loc='upper left', fontsize=8)
fig.tight_layout(); fig.savefig(f'{FIG}/fig3_mobile_money.png'); plt.close(fig)

# Fig 4 regional digital payments: direct end labels; HI line ends 2021
fig, ax = plt.subplots(figsize=(5.4, 2.9))
for reg in REG:
    lab = LBL[reg]
    yrs = [2014, 2017, 2021] if reg == 'High income' else [2014, 2017, 2021, 2024]
    s = series(pan_all[pan_all['regionwb24_hi'] == reg], 'g20_any', yrs)
    ax.plot(s.index, s, marker='o', ms=3.5, lw=1.8, color=COLORS[lab])
    end_label(ax, s.index[-1], s.iloc[-1], lab, COLORS[lab])
ax.set_ylabel('% of adults'); ax.set_xticks([2014, 2017, 2021, 2024]); ax.set_xlim(2013.3, 2027.8)
fig.tight_layout(); fig.savefig(f'{FIG}/fig4_dp_regional.png'); plt.close(fig)

# Fig 5 saving & borrowing
sav_o = off_series('Developing economies', 'fin17a_17a1_d')
bor_o = off_series('Developing economies', 'fin22a_22a1_22g_d', [2014, 2017, 2021, 2024])
fig, ax = plt.subplots(figsize=(5.4, 2.8))
ax.plot(sav.index, sav, marker='o', ms=4, lw=1.8, color='#2980b9', label='Saved formally')
ax.plot(bor.index, bor, marker='x', ms=5, lw=1.8, ls='--', color='#c0392b', label='Borrowed formally')
ax.plot(sav_o.index, sav_o, ls='none', marker='D', ms=4.5, mfc='none', color='#2980b9', alpha=0.6)
ax.plot(bor_o.index, bor_o, ls='none', marker='D', ms=4.5, mfc='none', color='#c0392b', alpha=0.6)
for x, y in sav.items():
    ax.annotate(f'{y:.1f}', (x, y), textcoords='offset points', xytext=(0, 7),
                ha='center', fontsize=8, color='#2980b9')
for x, y in bor.items():
    ax.annotate(f'{y:.1f}', (x, y), textcoords='offset points', xytext=(0, -12),
                ha='center', fontsize=8, color='#c0392b')
ax.set_ylabel('% of adults'); ax.set_ylim(0, 45); ax.set_xticks(YEARS)
ax.legend(frameon=False, loc='upper left', fontsize=8)
fig.tight_layout(); fig.savefig(f'{FIG}/fig5_sav_bor.png'); plt.close(fig)

# Fig 6 resilience
fig, ax = plt.subplots(figsize=(3.4, 2.5))
x = np.arange(2)
b1 = ax.bar(x - 0.19, [res_p[2021], res_p[2024]], width=0.38, color='#34495e', label='Balanced panel')
b2 = ax.bar(x + 0.19, [res_o[2021], res_o[2024]], width=0.38, color='#16a085', label='WB official')
for bars in (b1, b2):
    for b in bars:
        ax.annotate(f'{b.get_height():.1f}', (b.get_x() + b.get_width() / 2, b.get_height() + 0.7),
                    ha='center', fontsize=8)
ax.set_xticks(x, ['2021', '2024']); ax.set_ylabel('% of adults'); ax.set_ylim(0, 68)
ax.legend(frameon=False, fontsize=7.5, loc='lower right')
fig.tight_layout(); fig.savefig(f'{FIG}/fig6_resilience.png'); plt.close(fig)

# Fig 7 gender gap (levels + gap)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.6, 2.5), gridspec_kw={'width_ratios': [3, 2]})
a1.plot(men.index, men, marker='s', ms=3.5, lw=1.6, color='#2c3e50', label='Men')
a1.plot(women.index, women, marker='o', ms=3.5, lw=1.6, color='#e74c3c', label='Women')
a1.fill_between(men.index, men, women, color='gray', alpha=0.12)
a1.set_ylabel('% of adults'); a1.set_xticks(YEARS); a1.tick_params(axis='x', labelsize=7)
a1.legend(frameon=False, fontsize=8)
gap = men - women
a2.bar(gap.index.astype(str), gap, color='#c0392b', width=0.55)
for xx, yy in gap.items():
    a2.annotate(f'{yy:.1f}', (str(xx), yy + 0.15), ha='center', fontsize=8)
a2.set_ylabel('gap, pp'); a2.set_ylim(0, 10); a2.tick_params(axis='x', labelsize=7)
fig.tight_layout(); fig.savefig(f'{FIG}/fig7_gender.png'); plt.close(fig)

# Fig 8 income gap
fig, ax = plt.subplots(figsize=(5.2, 2.7))
ax.plot(rich.index, rich, marker='^', ms=4, lw=1.6, color='#27ae60', label='Richest 60% of households')
ax.plot(poor.index, poor, marker='v', ms=4, lw=1.6, color='#f39c12', label='Poorest 40% of households')
ax.fill_between(rich.index, rich, poor, color='#f1c40f', alpha=0.12)
for xx in YEARS:
    ax.annotate(f'{rich[xx] - poor[xx]:.1f} pp', (xx, (rich[xx] + poor[xx]) / 2),
                ha='center', fontsize=7.5, color='#7f6000')
ax.set_ylabel('% of adults'); ax.set_xticks(YEARS)
ax.legend(frameon=False, loc='lower right', fontsize=8)
fig.tight_layout(); fig.savefig(f'{FIG}/fig8_income.png'); plt.close(fig)

# ---------------------------------------------------------------- write stats
with open(os.path.join(os.path.dirname(__file__), 'paper_stats.json'), 'w') as f:
    json.dump(S, f, indent=1, default=str)
print('figures:', sorted(os.listdir(FIG)))
print('stats written')
