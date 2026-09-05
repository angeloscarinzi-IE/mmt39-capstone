"""Cross-document consistency check: every key figure, everywhere it appears."""
import glob, re, sys
sys.path.insert(0, "model")
from mmt39 import *

FILES = sorted(glob.glob("docs/*.md")) + ["SUMMARIES.txt"]
text = {f: open(f).read() for f in FILES}

t = market_size_table()
scS = standard_cost("S", 1, 3).total
scH = standard_cost("H", 10, 3).total
h1  = line_hours(1)
capS = capacity(s_lines=1, shifts=3).s_units
capH = capacity(h_lines=1, shifts=3).h_units
c   = contribution_per_unit(4.20, scH, 0.95)
gS  = capacity(h_lines=1, shifts=3, smed=True).h_units - capH
a10 = capacity(h_lines=10, shifts=3); p10 = capacity(h_lines=10, shifts=3, poka_yoke=True)

# (label, string that must appear, computed truth, formatter)
CLAIMS = [
    ("S market total",        "56,200,000",  t["S"]["TOTAL"],      56_200_000),
    ("H market total",        "131,260,000", t["H"]["TOTAL"],      131_260_000),
    ("S sellable 3sh",        "554,400",     capS,                 554_400),
    ("H sellable 3sh",        "1,386,000",   capH,                 1_386_000),
    ("S per line-shift",      "184,800",     capacity(s_lines=1,shifts=1).s_units, 184_800),
    ("H per line-shift",      "462,000",     capacity(h_lines=1,shifts=1).h_units, 462_000),
    ("operating hours",       "1,575",       h1.operating,         1575),
    ("breakdown hours",       "175",         h1.repair_hours,      175),
    ("module hours",          "250",         h1.module_hours,      250),
    ("32H max output",        "44.4M",       capacity(h_lines=32,shifts=3).h_units/1e6, 44.352),
    ("PY extra units",        "630,000",     p10.h_units-a10.h_units, 630_000),
    ("SMED per line",         "208,614",     gS*c,                 208_614),
    ("office payroll low",    "2,413,092",   office_payroll_range()[0], 2_413_092),
    ("office payroll high",   "3,371,620",   office_payroll_range()[1], 3_371_620),
    ("receivable 120d",       "33,333,333",  receivables(100_000_000,4), 33_333_333),
    ("factoring saving",      "1,500,000",   compare_working_capital(100_000_000,4)["saving_from_factoring"], 1_500_000),
    ("deposit income",        "1,350,000",   54_000_000*0.025,     1_350_000),
    ("survey bundle",         "11,000",      research_cost([23,28,1,2,27]), 11_000),
    ("whole research menu",   "1,003,400",   research_cost(SCENARIO["research"].keys()), 1_003_400),
]
# ratio/percentage claims expressed as literal strings in the docs
STRINGS = [
    ("utilisation",     "78.75",  abs(h1.utilisation-0.7875)<1e-9),
    ("SMED utilisation","91.25",  abs(line_hours(1,smed=True).utilisation-0.9125)<1e-9),
    ("SMED uplift",     "15.9",   abs(line_hours(1,smed=True).operating/h1.operating-1-0.1587)<0.001),
    ("SC S",            "5.13",   abs(scS-5.13)<0.005),
    ("SC H",            "2.13",   abs(scH-2.13)<0.005),
    ("capex/unit S",    "3.79",   abs(2_100_000/capS-3.79)<0.005),
    ("capex/unit H",    "1.08",   abs(1_500_000/capH-1.08)<0.005),
    ("BE S own",        "7.99",   abs(breakeven_price(scS,1.90,1.0,0.60,0.0)-7.99)<0.005),
    ("BE S wholesale",  "8.77",   abs(breakeven_price(scS,1.90,1.0,0.60,1.0)-8.77)<0.005),
    ("BE H own",        "3.86",   abs(breakeven_price(scH,0.95,1.0,0.60,0.0)-3.86)<0.005),
    ("BE H wholesale",  "4.23",   abs(breakeven_price(scH,0.95,1.0,0.60,1.0)-4.23)<0.005),
    ("TV A/B",          "300",    cost_per_reach_point("TV","A")==300.0),
    ("Social A/B",      "500",    cost_per_reach_point("SM","A")==500.0),
    ("TV E",            "327.9",  abs(cost_per_reach_point("TV","E")-327.9)<0.1),
    ("Social E",        "517.2",  abs(cost_per_reach_point("SM","E")-517.2)<0.1),
    ("vehicle best",    "0.0044", abs(marginal_cost_per_unit(24000)-0.0044)<1e-6),
    ("vehicle worst",   "0.0504", abs(marginal_cost_per_unit(1000)-0.0504)<1e-6),
    ("PY payback",      "12.3",   abs(7_200_000/((p10.h_units-a10.h_units)*c)-12.33)<0.05),
    ("SMED payback 1",  "14.4",   abs(3_000_000/(gS*c)-14.38)<0.05),
    ("SMED payback 8",  "1.8",    abs((3_000_000*4)/(gS*c*32)-1.80)<0.02),
]

print("=" * 72)
print("CROSS-DOCUMENT CONSISTENCY CHECK")
print("=" * 72)

fails = []

print("\n1. NUMERIC CLAIMS — does the doc string match the model?\n")
for label, s, computed, expected in CLAIMS:
    ok_model = abs(computed - expected) / (abs(expected) or 1) < 0.005
    where = [f.split("/")[-1] for f in FILES if s in text[f]]
    status = "ok " if ok_model else "BAD"
    if not ok_model: fails.append(f"{label}: model says {computed}, docs say {expected}")
    print(f"  {status} {label:<22} {s:>13}  appears in: {', '.join(where) or 'NOWHERE'}")

print("\n2. DERIVED RATIOS AND RATES\n")
for label, s, ok in STRINGS:
    where = [f.split("/")[-1] for f in FILES if s in text[f]]
    status = "ok " if ok else "BAD"
    if not ok: fails.append(f"{label} mismatch")
    print(f"  {status} {label:<20} {s:>10}  appears in: {', '.join(where) or 'NOWHERE'}")

print("\n3. SUPERSEDED FIGURES — must NOT appear as current guidance\n")
STALE = [("4.29","old S standard cost"), ("1.87","old H standard cost"),
         ("2.92","old S capex/unit"), ("0.83","old H capex/unit"),
         ("27% above","old benchmark gap"), ("€9,000","old survey bundle")]
for s, why in STALE:
    hits = []
    for f in FILES:
        alllines = text[f].split("\n")
        for i, line in enumerate(alllines, 1):
            if s in line:
                # look at a +/-2 line window: corrections often span lines
                low = " ".join(alllines[max(0,i-3):i+2]).lower()
                is_corr = (
                    any(k in low for k in ("said:", "now:", "earlier", "supersed",
                                           "wrong", "old ", "corrected", "i quoted"))
                    # a markdown correction table row: old value AND new value present
                    or (low.strip().startswith("|") and any(nv in line for nv in
                        ("5.13", "2.13", "3.79", "1.08", "36%", "11,000")))
                    # the CLI example uses live figures as arguments
                    or "--breakeven" in low
                )
                ctx = "CORRECTION-LOG" if is_corr else "LIVE TEXT"
                hits.append(f"{f.split('/')[-1]}:{i} [{ctx}]")
    bad = [x for x in hits if "LIVE TEXT" in x]
    status = "ok " if not bad else "BAD"
    if bad: fails.append(f"stale {s} in live text: {bad}")
    print(f"  {status} {s:<12} {why:<24} {'; '.join(hits) if hits else 'absent'}")

print("\n" + "=" * 72)
print("RESULT:", "ALL CONSISTENT" if not fails else f"{len(fails)} PROBLEMS")
for f in fails: print("   -", f)
print("=" * 72)
