## Graded Year 1 — model vs actual (Company 3, simulation B1SIM2C2)

Script used: a scratch `check_y1.py` importing `model/mmt39.py` read-only; repo untouched. Sources: `REP` = `DIR0114SI02083TE3Y1REP.md`, `DEP` = `…DEP.md`, `INF` = `…INFen_US.md`, `INV` = `…INV.md`, all under `day 2/year 1 results/`; `§` = `Scenario MMT39 EN v231.pdf`.

Headline: **1st of 5 on both rankings, net income 67,823,192** (REP p6; survey 23: Co2 59,544,072, Co4 5,932,326, Co5 −3,157,092, Co1 −10,887,540). The model, fed the DEP as filed, predicted **127,490,742**. 59,667,549 of the gap is demand (H sold 45.2% of output); the remaining **4,367,763 is model mechanics**, itemised below to the euro.

### (a) Comparison table

Two model runs. **A** = ex-ante, every unit sold (the plan's assumption). **B** = same model with the REP's actual sold units plugged in, so B−Actual isolates the mechanics. Decisions from DEP: 10 S / 22 H lines, 3 shifts, preventive ON, TS ON, salaries 24,000/13,500, office 126k/84k/60k/35k, RM bought S 6,265,350 / H 32,818,500 at 120 days, S 14.50 (margin 1.90), H 6.50 A / 7.50 B (margin 1.00), media 678,000, POP 150,000, research 166,800, 6+6 managers, 8 reps/zone at 27,000 + 0.60%, 3+2 trunk @24,000 kg, 30+20 last-mile @10,000 kg, loan 26,000,000, credit line 10,000,000, 60-day customer terms.

| Line | Model A (ex-ante) | Model B (actual volumes) | Actual (REP) | B − Actual | Err B |
| --- | ---: | ---: | ---: | ---: | ---: |
| Units produced S | 5,808,600 | 5,808,600 | 5,850,000 | −41,400 | −0.7% |
| Units produced H | 31,947,300 | 31,947,300 | 32,175,000 | −227,700 | −0.7% |
| Utilisation, good units / nameplate | 80.675% | 80.675% | 81.250% | −0.575 pp | −0.7% |
| RM used S | 5,846,400 | 5,846,400 | 5,967,000 | −120,600 | **−2.0%** |
| RM used H | 32,155,200 | 32,155,200 | 32,818,500 | −663,300 | **−2.0%** |
| RM closing stock S (units) | 418,950 | 418,950 | 298,350 | +120,600 | **+40.4%** |
| RM closing stock H (units) | 663,300 | 663,300 | 0 | +663,300 | n/a |
| RM unit price S | 1.6500 | 1.6500 | 1.6995 | −0.0495 | −2.9% |
| RM unit price H | 1.0500 | 1.0500 | 1.0815 | −0.0315 | −2.9% |
| Standard cost S | 5.3217 | 5.3217 | 5.5604 | −0.2387 | **−4.3%** |
| Standard cost H | 2.1718 | 2.1718 | 2.3252 | −0.1534 | **−6.6%** |
| Sales at MSRP S | 84,224,700 | 84,825,000 | 84,825,000 | 0 | 0.0% |
| Sales at MSRP H | 221,554,526 | 104,540,764 | 104,540,764 | 0 | 0.0% |
| Retailer margins S / H | 11,036,340 / 31,947,300 | 11,115,000 / 14,546,301 | 11,115,000 / 14,546,301 | 0 | 0.0% |
| Direct production cost S | 30,911,660 | 31,131,979 | 32,528,340 | −1,396,361 | −4.3% |
| Direct production cost H | 69,382,940 | 31,591,563 | 33,823,059 | −2,231,497 | −6.6% |
| Trunk transport (5 vehicles) | 264,000 | 264,000 | 132,000 | +132,000 | **+100%** |
| Last-mile transport (50 vehicles) | 1,800,000 | 1,800,000 | 900,000 | +900,000 | **+100%** |
| Warehouse cost | 875,666 | 494,957 | 600,862 | −105,905 | −17.6% |
| Gross profit S+H (REP basis) | 159,561,320 | 98,421,965 | 95,720,201 | +2,701,763 | +2.8% |
| Depreciation | 7,920,000 | 7,920,000 | 6,480,000 | +1,440,000 | **+22.2%** |
| R&D 4.5% | 13,760,065 | 8,521,459 | 8,521,459 | 0 | 0.0% |
| Sales network A+B (fixed) | 3,192,000 | 3,192,000 | 3,192,000 | 0 | 0.0% |
| Sales force incentives | 1,303,713 | 702,750 | 702,750 | 0 | 0.0% |
| Advertising incl. POP | 828,000 | 828,000 | 828,000 | 0 | 0.0% |
| Office payroll / overhead / research / preventive / TS | 2,818,000 / 600,000 / 166,800 / 500,000 / 722,000 | same | same | 0 | 0.0% |
| Turnover costs (office + sales) | 0 | 0 | 306,000 | −306,000 | **−100%** |
| Total general expenses | 31,810,578 | 25,971,009 | 24,837,009 | +1,134,000 | +4.6% |
| Operating income | 127,750,742 | 72,450,956 | 70,883,192 | +1,567,764 | +2.2% |
| Loan interest | 0 | 0 | 2,600,000 | −2,600,000 | **−100%** |
| Fees + credit line | 260,000 | 260,000 | 460,000 | −200,000 | −43.5% |
| Total financial expense | 260,000 | 260,000 | 3,060,000 | −2,800,000 | **−91.5%** |
| **Net income** | **127,490,742** | **72,190,956** | **67,823,192** | **+4,367,763** | **+6.4%** |
| Cash 31 Dec | 124,917,377 | 51,228,458 | 46,902,208 | +4,326,250 | **+9.2%** |
| Receivables | 50,963,204 | 31,560,961 | 27,284,077 | +4,276,884 | **+15.7%** |
| Inventory FG + RM | 0 | 37,791,377 | 41,497,297 | −3,705,920 | −8.9% |
| Payables | 14,469,840 | 14,469,840 | 15,380,390 | −910,550 | −5.9% |
| Loans outstanding | 26,000,000 | 26,000,000 | 26,000,000 | 0 | 0.0% |
| Loan instalment due 2 Jan | 8,666,667 | 8,666,667 | 6,500,000 | +2,166,667 | **+33.3%** |
| Loan need (OCN test) | 0 (OCN 52,514,576 vs 54,000,000) | 0 | 0 forced; overdraft 0 | 0 | — |

The B net-income error decomposes exactly: SC +3,627,858, loan interest +2,600,000, turnover +306,000, credit line +200,000, warehouse +105,905 (model too cheap) minus depreciation 1,440,000 and transport 1,032,000 (model too dear) = +4,367,763.

Note on A: doc 06's headline of 112,166,213 was for H at 5.25/7.75 and POP 3,000/5,000. The DEP as filed has H 6.50/7.50 and POP 10,000/15,000, hence 127,490,742. That price change is where the H demand went (section d).

### (b) Model fixes, ranked by euro impact on this year

| # | Mechanic | Evidence (REP unless stated) | Impact Y1 | Confidence |
| --- | --- | --- | --- | --- |
| 1 | Loan interest is charged for the full draw year | p5 "Loans 2,600,000" = 10% x 26,000,000; test Y1 382,605 = 10% x 3,826,050 | 2,600,000 | [Certain] |
| 2 | Conversion cost: power comes in at 1.767x the INF rate; RM at 1.02x units and 1.03x price at 120 days | p4 SC S 5.5604 / H 2.3252 (decomposition below) | 3,627,858 on COGS + 2,704,000 on FG inventory value | [Likely] on mechanism, [Certain] on size |
| 3 | Depreciation base excludes land and buildings | p5 6,480,000 = 12% x 54,000,000; p6 lists "Land, buildings 12,000,000" separately; test Y2 7,056,000 = 12% x 58,800,000; §35 table names lines, PY, SMED only | 1,440,000 | [Certain] |
| 4 | Vehicles are charged at exactly 50% of the §10 formula when no stockout flag | p4 trunk 132,000 = 0.5 x 5 x 52,800; last mile 900,000 = 0.5 x 50 x 36,000, both to the euro. Test Y1 48,155 vs half 43,200 and test Y2 187,039 vs half 177,600, each with one stockout flag (emergency premium on top) | 1,032,000 | [Certain] on the number, [Guessing] on why |
| 5 | Receivables are 2/12 of NET revenue (MSRP less retailer margin) | p6 27,284,077 = 2/12 x 163,704,462.5; MSRP basis would be 31,560,961; §38 "retailer margins are paid immediately" | 4,276,884 of cash forecast | [Certain] |
| 6 | Loan maturity is 4, not 3 | p4 "Loans due on Jan. 2: 6,500,000" = 26,000,000 / 4; INF p2 "Loan Maturity 4" | 2,166,667 on the 2-Jan cash call | [Certain] |
| 7 | RM yield: units used = 1.02 x produced, output not reduced by scrap | p4 5,967,000 / 5,850,000 = 1.0200; 32,818,500 / 32,175,000 = 1.0200; test Y1 1.020000 both | RM plan short by 1.3% -> 15% penalty (§28) on ~120,600 S / 663,300 H units | [Certain] |
| 8 | Credit line costs 2% undrawn: 1% upfront in "Fees" + 1% service fee shown as "Credit line" | p5 Credit line 100,000, Fees 360,000 = 260,000 + 100,000; test Y2 300,000 + fees 1,308,577 = 1,008,577 + 300,000 | 200,000 | [Certain] |
| 9 | Turnover cost: office 9,000/leaver with TS on (24,000 off), sales 30,000/leaver | p4-p5: 4 leavers 36,000; 9 leavers 270,000; test Y1 4 x 24,000, 7 x 30,000; test Y2 6 x 30,000 | 306,000 | [Likely] |
| 10 | Payables and RM stock use PURCHASES at the negotiated price | p6 Payables S 3,549,321 = 4/12 x 6,265,350 x 1.6995; H 11,831,069 = 4/12 x 32,818,500 x 1.0815; RM S 507,046 = 298,350 x 1.6995 | 910,550 payables, 507,046 inventory, ~1.4M cash | [Certain] |
| 11 | Warehouse cost | p4 S 168,063 / H 432,799 = 0.0295 per unit sold at 12 platforms per market (test Y1 0.0193 at 6). No charge on the 17.6M H finished-goods stock | 105,905 | [~] basis unclear |
| 12 | Sales-force commission formula | p5 702,750 = 0.006 x (MSRP − margin) x units in channels S and T only (reproduced to 702,749.58) | 0 once fed correctly; `distribution_compare` overstates by using MSRP | [Certain] |

**SC decomposition (per unit, 3 shifts, preventive, 195,000 / 487,500 units per line-shift):**

| Component | S model | S actual | H model | H actual | Rule that reproduces actual |
| --- | ---: | ---: | ---: | ---: | --- |
| Raw material | 1.6607 | 1.7335 | 1.0568 | 1.1031 | list x 1.03 (120 days) x 1.02 (yield) |
| Labour | 3.3468 | 3.3231 | 0.9390 | 0.9323 | crew x salary / 195,000 or 487,500 (model right, units off 0.7%) |
| Repair | 0.0626 | 0.0621 | 0.0250 | 0.0249 | model right |
| Power | 0.2516 | 0.4417 | 0.1510 | 0.2650 | INF rate x **1.767** (S fit 1.7668, H fit 1.7661) |
| Total | 5.3217 | 5.5604 | 2.1718 | 2.3252 | |

The residual is proportional to the power rate, not to labour (residual per line-shift S 36,406 / H 54,555 = 0.667 = 60,000 / 90,000), which rules out absenteeism or wage loading. The same 1.767 reproduces test Y1 S conversion 3.8270 vs 3.8327 and the test Y2 SMED plant 3.4355 vs 3.4276 (S), 1.1128 vs 1.1046 (H) with **no** SMED calibration, so the `conversion_cost_calibration` block (0.9395 / 0.9197) was fitting this effect with the wrong decomposition and should go to 1.0.

**Exact code changes (`model/mmt39.py`):**

1. `LoanBook.year`, line 1669: `interest = opening * self.interest` -> `interest = (opening + draw) * self.interest`. Also the forced-loan branch in `Simulation.run_year` (~line 2027) should add `self.forced_loan * s["loan_interest"]`.
2. `standard_cost`, line 594: `sc.raw_material = rm_cost * started / good` -> `sc.raw_material = rm_cost * (1.0 + s["rm_terms_premium"][rm_terms_months]) * (1.0 + s["rm_yield_loss"])`; add `rm_terms_months: int = 4` to the signature. Line 599: `sc.power = s["power_cost_per_unit"][product] * started / good * cal` -> `sc.power = s["power_cost_per_unit"][product] * s["power_cost_realisation"]`. Drop `cal` (set calibration to 1.0). New SCENARIO keys: `"rm_yield_loss": 0.02`, `"rm_terms_premium": {4: 0.03}` (only 120 days measured; 90 days ~0.0127 from one 795,600-unit test-Y1 order), `"power_cost_realisation": 1.767`.
3. `Simulation.run_year`, the `build_income_statement(... fixed_assets=self.fixed_assets_gross ...)` call (~line 1997): `fixed_assets=self.fixed_assets_gross - s["opening_fixed_assets"]`.
4. `vehicle_annual_cost`, ~line 630: `cost = s["vehicle_fixed_cost"] + s["vehicle_cost_per_kg"] * load_kg` -> multiply by new `s["vehicle_cost_realisation"]` = 0.5, with a comment that this is measured on flag-free years and that stockouts add an unmodelled premium. Keep `--vehicles` sizing logic as is (relative costs unchanged).
5. `Simulation.run_year`, ~line 1990: `recv = receivables(revenue, plan.customer_terms_months)` -> `recv = receivables(revenue - sum(l.retailer_cost for l in plan.sales), plan.customer_terms_months)`. Same basis in `available_cash_jan2()` callers.
6. SCENARIO line 251: `"loan_maturity_years": 3` -> `4`; selftest line 2377 asserts `== 3`, update to 4.
7. `LineHours.good_hours` (line ~409): return `self.operating` (scrap no longer cuts output; model then gives 81.20% vs actual 81.25%). `raw_material_units_needed`, line 615: `return max(0.0, produced * (1.0 + SCENARIO["rm_yield_loss"]) - opening_stock)`; drop the `scrapped` argument at the three call sites (lines 1979-1983 and the `--lines` table).
8. `YearPlan`: add `credit_line: float = 0.0`. `run_year` line 2006: `inc.financial_expenses = fin_exp + loan_row.upfront_fee + plan.credit_line * (s["credit_line_upfront_fee"] + s["credit_line_service_fee"])`.
9. New key `"turnover_cost_per_leaver": {"office_ts_on": 9_000.0, "office_ts_off": 24_000.0, "sales": 30_000.0}` and `"expected_leavers": {"office": 4, "sales": 8}`; add to `inc.other` in `run_year`.
10. `YearPlan`: add `rm_purchase_units: Dict[str, float]`. Line 2017: `payable = rm_cost * ...` -> `payable = sum(plan.rm_purchase_units[p] * s["rm_unit_cost"][p] * (1 + premium) for p) * terms / 12`; set `bs.inventory_raw` (field exists at line 1703, never written) to `(purchased - used) x price`; charge the full purchase to cash.
11. `platform_costs`: average stock assumption `units / 52 / 2` (0.5 weeks) -> a measured `"platform_avg_stock_weeks"`: 0.635 at 12 platforms (solves 600,862 = 2 x avg + 55,070 handling + 46,839 notes + 811 orders), 0.348 at 6 platforms in test Y1. Wire `platform_costs()` into `run_year` (currently only `distribution_compare` uses it).
12. `distribution_compare` line ~735: `ptr = price_to_retailer if ... else retail_price` -> default `retail_price - retailer_margin`; commission only on S and T channel units.

### (c) SCENARIO edits for Year 2 (INF p2 vs dict)

| INF p2 item | INF value | SCENARIO key | Current | Action |
| --- | --- | --- | --- | --- |
| Loan maturity (years) | **4** | `loan_maturity_years` | 3 | **Change to 4** (REP p4 confirms 26M/4 = 6,500,000 due) |
| Per capita income A / B / E | 27,000 / 35,000 / 46,000 | `per_capita_income` | same | none |
| Raw material S / H | 1.6500 / 1.0500 | `rm_unit_cost` | same | none (but add the terms premium, above) |
| Power S / H | 0.2500 / 0.1500 | `power_cost_per_unit` | same | none (add `power_cost_realisation`) |
| EUR per USD | 1.00 | `fx_eur_per_usd` | 1.0 | none |
| Unemployment A+B | 7.00% | `unemployment_rate_AB` | 0.07 | none |
| Overdraft | 20.00% | `overdraft_interest` | 0.20 | none |
| Loan upfront / prepayment / interest | 1 / 1 / 10% | `loan_upfront_fee`, `loan_prepayment_penalty`, `loan_interest` | same | none |
| Credit line interest / upfront / service | 7 / 1 / 1% | `credit_line_*` | same | none |
| Financial investments rate / early fee | 2.5 / 1% | `investment_interest`, `investment_early_withdrawal` | same | none |
| Fixed-term deposits rate / early fee | 2.5 / 1% | `deposit_interest`, `deposit_early_withdrawal` | same | none |
| Factoring | 5.50% | `factoring_rate` | 0.055 | none |

Only one constant moved. Caveat `[!]`: the INF header reads "Year: 1" — it is the sheet issued with the Y1 results. In the test round the Y2 INF cut maturity 4 -> 3 after the Y1 INF said 4. Re-read the platform's Year-2 INF before filing; §42 says a new term "will be applied to the new loans and to the debt that the companies owe at that moment", so a cut to 3 would reschedule the remaining 19,500,000 too.

New measured keys to add alongside: `rm_yield_loss 0.02`, `rm_terms_premium {4: 0.03}`, `power_cost_realisation 1.767`, `vehicle_cost_realisation 0.5`, `turnover_cost_per_leaver`, `platform_avg_stock_weeks`; set `conversion_cost_calibration` to `{"S": 1.0, "H": 1.0}` (superseded).

### (d) What the model does not model at all

| Item | Evidence | Why it matters |
| --- | --- | --- |
| **Demand.** No demand function; the plan assumed 100% sell-through | H sold 14,546,301 of 32,175,000 (REP p3); 17,628,699 in stock worth 40,990,251 (p6); A H sold 4,556,494 at 6.50 vs test Y2 15,684,101 at 5.25. Rivals' H (survey 20): Co1 6.50-7.50, Co4 6.50-7.20, Co2 9.50-11.00; survey 3: A H Co2 7,782,836 and Co4 7,743,383 vs us 4,556,494 | 59.7M of the ex-ante miss. The DEP deviated from doc 06 (5.25/7.75 -> 6.50/7.50) and A collapsed; B at 7.50 still took 9,989,807 of the participants' 17,892,931. Price alone does not explain A (Co2 sold more at 9.50-10.50) |
| S unserved demand | "Units demanded of your brand" S 1,827,440 (p2) at 14.50 with all 5,850,000 sold | S was the binding constraint again; total S demand 7,677,440 |
| H unserved demand while holding stock | H 501,093 unserved (p3) with 17.6M finished goods and no logistic stockout flags (p4) | Mechanism unknown (channel/shelf cap?). Do not build the SMED case on it |
| Workforce turnover (§31) and its cost | 4 office / 9 sales leavers, 306,000 (p4-p5) with TS on | Fix 9 |
| Credit line fees and interest (§43) | 200,000 undrawn | Fix 8 |
| Raw-material price negotiation by volume and terms (§28, §37) | 1.03x at 120 days both products; test Y1 S at 90 days 1.0127x | Fix 2; also feeds OCN item 3 and payables |
| RM inventory on the balance sheet and the cash cost of over-purchase | `inventory_raw` never set; RM S 507,046 held | Fix 10 |
| Warehouse cost in `Simulation` | 600,862 charged; `platform_costs()` exists but is not wired in | Fix 11 |
| Transport cost allocation S vs H | S carries 33.86% of both legs (44,692 / 132,000; 304,718 / 900,000) — matches neither units sold (28.7%), demand (33.78%) nor net revenue (45.0%) | Cosmetic; totals are what matter |
| Emergency-logistics premium on a stockout flag | Test Y1 +4,955 trunk, test Y2 +9,439 trunk and +1,527,519 last mile over the 50% rule | Only the flag is modelled, not the bill |
| E logistics filed with no E price | DEP p2: 60 platforms, 10 trunk @12,000, 30 last-mile @1,500 in E; REP: 0 charged anywhere, "Sales network E 0" | Answers doc 06 open question 1: costs nothing |
| Monthly interest and cash path (§40) | Overdraft 0 on a 26M loan + 10M line; year-end cash 46,902,208 reconciles exactly (54M + 26M − 54M + 67,823,192 + 6,480,000 − 27,284,077 − 41,497,297 + 15,380,390) | Model has only the year-end balancing cash; the intra-year trough is hand-built in doc 06 §4.2 |
| Printed ratios use net revenue as "Total sales" | p8 asset turnover 0.9344 = 163,704,462 / 175,203,582 | Already flagged in doc 05 §1.3; still not in `ratios()` |

Two things confirmed correct and worth keeping: R&D = 4.5% of MSRP sales (8,521,459 to the euro), and office payroll / sales network fixed / research / advertising all reproduce exactly from the DEP.
