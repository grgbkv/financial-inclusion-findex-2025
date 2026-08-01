"""Coverage ledger for the Findex autoresearch loop — read-only instrument, not a data path.

Answers one question at the start of a cycle: WHICH PARTS OF THE DATASET HAS THE LOOP NEVER
TOUCHED? After 50 experiments the ledger covered ~15 of 437 country columns, ~25 of 199 micro
columns, one of four wave transitions and one of seven country frames. This module measures that
so the frame-rotation rules in program_findex.md ("Breadth discipline") can be applied mechanically
instead of by memory.

Data access still goes exclusively through the fixed modules: harness.Findex for the country file,
micro.Micro for the individual file. Nothing here computes an outcome, a rate or a correlation —
it counts availability and usage only, so running it is never a peek under the pre-registration
rule.

Usage:
    python3 coverage.py              # full report
    python3 coverage.py --module con # drill into one column family
"""
import os
import re
import sys
from collections import defaultdict

import pandas as pd

from harness import Findex, YEARS

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER_FILES = ["findings.tsv", "RESEARCH_LOG.md", "results_prediction.tsv"]

TRANSITIONS = [(a, b) for a, b in zip(YEARS, YEARS[1:])]

# Country-file demographic slices (the `group` column). The 13-year within-country inequality
# panel lives here and is nearly untouched.
GROUP_SLICES = ["all", "gender", "income", "education", "age_cat", "laborforce", "urbanicity"]

# Module prefixes worth reporting separately in the country file.
MODULE_LABELS = {
    "con": "consumer protection / fraud / trust / digital risk",
    "fh": "financial health",
    "fin11": "barriers to account ownership (unbanked)",
    "fin13": "mobile-money usage",
    "fin14": "mobile-money usage detail",
    "fin17": "saving modes",
    "fin22": "borrowing sources",
    "fin24": "emergency funds / resilience",
    "fin25": "emergency-fund detail",
    "fin31": "digital payment detail",
    "fin32": "wage payments",
    "fin33": "wage payment detail",
    "fin34": "wage payment modes",
    "fin39": "utility payments",
    "fin43": "agricultural payments",
    "fin48": "digital-risk exposure",
    "fin49": "digital-risk exposure detail",
    "fing2p": "government-to-person payments",
    "g20": "digital payment headline",
}


def _ledger_text():
    parts = []
    for f in LEDGER_FILES:
        p = os.path.join(HERE, f)
        if os.path.exists(p):
            parts.append(open(p, encoding="utf-8", errors="ignore").read())
    return "\n".join(parts)


def _used_columns(text, columns):
    """A column counts as USED if its name appears in the ledger with word boundaries
    (so fin17a does not match inside fin17a_17a1_d, and con1 does not match con10)."""
    used = set()
    for c in columns:
        if re.search(r"(?<![A-Za-z0-9_])" + re.escape(c) + r"(?![A-Za-z0-9_])", text):
            used.add(c)
    return used


def _module_of(col):
    for pref in sorted(MODULE_LABELS, key=len, reverse=True):
        if col.startswith(pref):
            return pref
    m = re.match(r"([a-z_]+)", col)
    return m.group(1) if m else col


def _wave_coverage(frame, col):
    """Countries reporting `col` in each wave (availability only, never a value)."""
    out = {}
    for y in YEARS:
        d = frame[(frame["year"] == y) & frame[col].notna()]
        out[y] = int(d["countrynewwb"].nunique())
    return out


def country_report(fx: Findex, text, module_filter=None):
    frame = fx.pan_dev
    skip = {"year", "pop_adult", "group", "group2", "countrynewwb", "codewb",
            "regionwb24_hi", "incomegroupwb24"}
    cols = [c for c in fx.raw.columns if c not in skip]
    used = _used_columns(text, cols)

    by_mod = defaultdict(list)
    for c in cols:
        by_mod[_module_of(c)].append(c)

    print("=" * 90)
    print(f"COUNTRY FILE — {len(cols)} indicator columns, {len(used)} touched by the ledger "
          f"({len(used) / len(cols):.0%})")
    print("=" * 90)
    rows = []
    for mod, members in sorted(by_mod.items(), key=lambda kv: -len(kv[1])):
        if module_filter and mod != module_filter:
            continue
        u = [c for c in members if c in used]
        # wave availability of the module's best-covered member, developing panel
        best, best_cov = None, -1
        for c in members:
            try:
                cov = int(frame[(frame["year"] == 2024) & frame[c].notna()]["countrynewwb"].nunique())
            except (TypeError, KeyError):
                continue
            if cov > best_cov:
                best, best_cov = c, cov
        waves = _wave_coverage(frame, best) if best else {}
        n_waves = sum(1 for y, n in waves.items() if n >= 30)
        rows.append({"module": mod, "label": MODULE_LABELS.get(mod, ""), "cols": len(members),
                     "used": len(u), "n2024_dev": best_cov, "waves>=30c": n_waves,
                     "waves": "/".join(str(waves.get(y, 0)) for y in YEARS)})
    t = pd.DataFrame(rows)
    if module_filter:
        members = sorted(by_mod.get(module_filter, []))
        print(f"module {module_filter}: {MODULE_LABELS.get(module_filter, '')}")
        for c in members:
            mark = "used" if c in used else "  . "
            print(f"  [{mark}] {c:22s} waves(dev, countries) = "
                  f"{'/'.join(str(_wave_coverage(frame, c).get(y, 0)) for y in YEARS)}")
        return
    t = t.sort_values(["used", "cols"], ascending=[True, False])
    print(t.to_string(index=False))
    print("\nwaves column = countries reporting in 2011/2014/2017/2021/2024 (developing panel, "
          "best-covered member of the module)")
    untouched = t[t["used"] == 0]
    print(f"\nUNTOUCHED MODULES: {len(untouched)} families, "
          f"{int(untouched['cols'].sum())} columns — "
          f"{', '.join(untouched.head(12)['module'])}")


def wave_report(text):
    print("\n" + "=" * 90)
    print("WAVE TRANSITIONS")
    print("=" * 90)
    for a, b in TRANSITIONS:
        pats = [f"{a}-{str(b)[-2:]}", f"{a}->{b}", f"{a}-{b}", f"{a}→{b}"]
        hits = sum(text.count(p) for p in pats)
        flag = "USED" if hits >= 3 else ("thin" if hits else "UNTOUCHED")
        print(f"  {a}->{b}: {hits:4d} ledger mentions   [{flag}]")
    print("  (rule: a kept 2021->2024 association is not a general claim until replicated on "
          "at least one earlier transition — see program_findex.md 'Breadth discipline')")


def frame_report(fx: Findex, text):
    print("\n" + "=" * 90)
    print("FRAMES (country file)")
    print("=" * 90)
    grp = fx.countries[fx.countries["countrynewwb"].isin(fx.panel_names)]
    for g in GROUP_SLICES:
        d = grp[grp["group"] == g]
        n_c = d["countrynewwb"].nunique()
        n_w = d["year"].nunique()
        subs = sorted(str(x) for x in d["group2"].dropna().unique())[:6] if "group2" in d else []
        # Usage detector: the slice's own group2 LABELS (e.g. "out of laborforce") appear in the
        # ledger only when the slice was actually pulled. Bare words like "income" or "education"
        # are prose and would over-count wildly, so they are deliberately not matched.
        # Only distinctive labels (>= 8 chars) are reliable detectors; "men"/"rural" and friends
        # collide with ordinary prose, so those slices report n/a rather than a wrong number.
        probes = [s for s in subs if len(s) >= 8]
        if probes:
            hits = sum(text.count(s) for s in probes)
            flag = "USED" if hits >= 8 else ("thin" if hits else "UNTOUCHED")
        else:
            hits, flag = -1, "detector n/a (labels too generic)"
        print(f"  group={g:11s} {n_c:3d} panel economies x {n_w} waves   "
              f"subgroups: {', '.join(subs) if subs else '-':38s} "
              f"[{flag}{'' if hits < 0 else f': {hits} mentions'}]")
    print("  (the non-'all' slices are a 13-year within-country inequality panel; as of the "
          "2026-08-01 audit only two experiments, E20/E21, had used it)")


def micro_report(text):
    try:
        from micro import Micro
    except Exception as e:                                    # microdata is optional/licensed
        print(f"\n(micro file unavailable: {e})")
        return
    mi = Micro()
    skip = {"economy", "economycode", "wgt", "year", "wpid_random", "pop_adult", "regionwb"}
    cols = [c for c in mi.df.columns if c not in skip]
    used = _used_columns(text, cols)
    print("\n" + "=" * 90)
    print(f"MICRO FILE (2024) — {len(cols)} columns, {len(used)} touched by the ledger "
          f"({len(used) / len(cols):.0%})")
    print("=" * 90)
    by_mod = defaultdict(list)
    for c in cols:
        by_mod[_module_of(c)].append(c)
    rows = []
    for mod, members in by_mod.items():
        u = [c for c in members if c in used]
        rows.append({"module": mod, "label": MODULE_LABELS.get(mod, ""),
                     "cols": len(members), "used": len(u)})
    t = pd.DataFrame(rows).sort_values(["used", "cols"], ascending=[True, False])
    print(t.head(30).to_string(index=False))
    untouched = t[t["used"] == 0]
    print(f"\nUNTOUCHED MICRO MODULES: {len(untouched)} families, "
          f"{int(untouched['cols'].sum())} columns")


def main():
    module_filter = None
    if "--module" in sys.argv:
        module_filter = sys.argv[sys.argv.index("--module") + 1]
    text = _ledger_text()
    fx = Findex()
    country_report(fx, text, module_filter)
    if module_filter:
        return
    wave_report(text)
    frame_report(fx, text)
    micro_report(text)
    print("\n" + "=" * 90)
    print("Pick the cycle's experiments so that at least one lands on an UNTOUCHED module, "
          "wave transition or frame (program_findex.md, Breadth discipline rule B1).")
    print("=" * 90)


if __name__ == "__main__":
    main()
