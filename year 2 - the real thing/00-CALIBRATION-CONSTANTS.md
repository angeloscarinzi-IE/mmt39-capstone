# 00 · Calibrated constants — the single source of truth

Every constant below was fitted to an actual result sheet and reproduces the simulator's own
figure. `python3 model/calibration.py` re-verifies all **32** of them in one second.

⚠️ These **supersede** the scenario-derived assumptions in `model/mmt39.py`. Where the two
disagree, this file wins. As of the graded Year-1 sheet (`B1SIM2C2`) the calibration
reproduces the income statement, the balance sheet and both standard costs **to the euro** —
no residual, no fudge factor.

## Production

| Constant                         | Value                                     | Evidence                                          |
| -------------------------------- | ----------------------------------------- | ------------------------------------------------- |
| Line utilisation, no SMED        | **81.25% exactly**                        | test Y1 and graded Y1, both products              |
| Line utilisation, with SMED      | **92.9%**                                 | test Y2, 2 modules — the one unverified input     |
| Raw material per finished unit   | **1.02 exactly**                          | 5,967,000 / 5,850,000 and 32,818,500 / 32,175,000 |
| Preventive maintenance           | **+2.5 points of nameplate** for €500,000 | 81.25% observed vs 78.75% without                 |
| Nameplate per line-shift         | S 240,000 · H 600,000                     | §23                                               |
| Sellable per line-year, 3 shifts | S 585,000 · H 1,462,500                   | 81.25%                                            |
| Sellable per line-year with SMED | S 668,880 · H 1,672,200                   | 92.9%                                             |
| Crew per line-shift              | S 9 spec + 32 op · H 6 spec + 23 op       | §30                                               |
| Absenteeism at €13,500 / €24,000 | **none measurable**                       | output hit the theoretical maximum in both years  |
| SMED module cost                 | €3,000,000, irreversible, from year 2     | §27                                               |

## Standard cost — now exact

```
SC = 1.02 x RM_list x (1 + terms_premium)
   + 1.764582 x power_rate
   + (spec x spec_wage + oper x oper_wage) / (nameplate_per_shift x utilisation)
   + 12,224.10 / (nameplate_per_shift x utilisation)
```

| Product | Model      | Reported (REP p4) | Error |
| ------- | ---------- | ----------------- | ----- |
| S       | **5.5604** | 5.5604            | 0     |
| H       | **2.3252** | 2.3252            | 0     |

The two conversion constants were **solved jointly** from the two printed standard costs —
two equations, two unknowns — and then reproduced COGS, finished-goods inventory value and
raw-material inventory value to the euro without further adjustment.

| Constant                   | Value          | Reading                                                                                                                                                                                            |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power realisation          | **1.764582**   | `[~]` appears nowhere in §33 or §49. Purely empirical. Re-fit every year                                                                                                                           |
| Repair cost per line-shift | **€12,224.10** | = 127.12 h × 4 technicians × €24.041                                                                                                                                                               |
| Repair hours, mechanism    | 127.12 h       | `[~]` within 0.9% of 70 × (0.7 × 1.5 h + 0.3 × 2.5 h) = 126 h — preventive maintenance appears to remove the 0.5 h detection and 0.5 h preparation on the 70% of breakdowns it foresees (§24, §25) |

⚠️ Superseded: the previous power multiplier of **1.70** and the previous repair assumption of
the full 2.5 h on all 70 breakdowns (€16,828.70 per line-shift). Both are kept in
`SUMMARIES.txt` Appendix A. The old pair fitted the test round to 0.03%; the new pair fits the
graded round to zero.

## Purchasing — 120-day terms are not free `[!]`

| Supplier term | Premium on list   | Status                                            |
| ------------- | ----------------- | ------------------------------------------------- |
| 0 days (cash) | 0%                | `[~]` interpolated, never observed                |
| 60 days       | ~0.85%            | `[~]` interpolated                                |
| 90 days       | **1.27%**         | measured, test Y1                                 |
| 120 days      | **3.00% exactly** | measured, graded Y1: 1.65 → 1.6995, 1.05 → 1.0815 |

Year 1 paid **€1,343,918** for 120-day terms and got €15,380,390 of supplier float in return,
worth €384,510 at the 2.5% deposit rate. The terms cost 3.5× what the float is worth. Shorten
them.

## Money

| Rule                 | Value                                                | Evidence                                      |
| -------------------- | ---------------------------------------------------- | --------------------------------------------- |
| R&D                  | 4.5% of **MSRP** sales, not net revenue              | €8,521,459 on €189,365,764                    |
| Sales commission     | 0.6% of price-to-retailer, **channels S and T only** | €702,750 on €117,124,930; channel G is free   |
| Depreciation         | 8/10/12% by shift count, on **lines and SMED only**  | €6,480,000 = 12% × €54,000,000; land excluded |
| Depreciation base    | **gross**, not net of prior depreciation             | graded Y1                                     |
| Loan interest        | charged on the **full draw year**, opening + draw    | €2,600,000 = 10% × €26,000,000                |
| Loan amortisation    | 1/4 of principal per year at a 4-year maturity       | €6,500,000 on €26,000,000                     |
| Loan maturity        | **4 years** in the graded round                      | INF p2; re-read INF every year `[!]`          |
| Credit line, undrawn | **2%** — 1% upfront plus 1% service                  | €200,000 on €10,000,000                       |
| Receivables          | 2/12 of **net** revenue, not MSRP sales              | €27,284,077 on €163,704,462                   |
| Payables             | 4/12 of **purchases at the price paid**              | €15,380,390                                   |
| Turnover, office     | €9,000/leaver with TS on · €24,000 with TS off       | 4 leavers, both years                         |
| Turnover, sales reps | €30,000/leaver, unaffected by TS                     | 9 leavers × €30,000 = €270,000                |
| Corporate tax        | **none**                                             | operating − financial = net, exactly          |
| Retailer margin      | a straight €/unit deduction                          | every euro of margin costs a euro             |
| Factoring            | 5.5% × (collection months / 12) × net revenue        | test Y1                                       |

📌 **The training department does not pay.** It cuts the office rate from €24,000 to €9,000 a
leaver — 4 leavers, so €60,000 — and costs €722,000. It does nothing for sales-rep turnover,
which is 4.5× larger.

## Logistics

| Rule                            | Value                                  | Evidence                                          |
| ------------------------------- | -------------------------------------- | ------------------------------------------------- |
| Trunk capacity per vehicle-year | **500 × load capacity in kg**          | predicted 4 of 4 stockout flags across both years |
| Vehicle billing                 | **exactly 50% of the §10/§12 formula** | €132,000 on 5 trunk, €900,000 on 50 last-mile     |
| Last mile                       | drop-driven, not tonnage-driven        | 30 in A and 20 in B cleared 20.4M units, no flags |
| Last-mile emergency premium     | about 2× the planned cost              | test Y2: +€1,527,519 on one flagged market        |
| Warehouse cost                  | €0.0295/unit sold at 12 platforms      | €600,862; €0.0193 at 6 platforms in test Y1       |
| Finished-goods stock            | **not charged** warehouse cost         | 17.6M units held, no charge in REP                |
| Unused market                   | costs nothing at the form defaults     | E at 60 platforms / 40 vehicles, charged €0       |

⚠️ Against the §12 reference of €0.007/unit the last mile actually cost **€0.044/unit** — 6.3×
the benchmark. That deviation is exactly what the rubric asks Operations to explain.

## Ratios, as the simulator computes them

| Ratio         | Numerator  | Denominator            |
| ------------- | ---------- | ---------------------- |
| Profit margin | net income | **net** revenue        |
| ROE           | net income | **closing** equity     |
| ROA           | net income | closing total assets   |
| ROI           | net income | **gross** fixed assets |

`[!]` The printed inventory turnover does not reproduce from any combination of the statements.
Do not quote it.

## What resets every year

Sales managers · all six salary fields · **lines to be activated** · SMED to be activated ·
factoring · supplier terms · credit line · surveys · logistics (to 30/30/60 platforms and
10 + 30 vehicles). Lines and SMED modules installed carry over; their **activation does not**.

## Update log

| Date       | Change                                                                                                                                                                                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-09-06 | Rebuilt on the graded Year-1 sheet. Power realisation 1.70 → 1.764582; repair €16,828.70 → €12,224.10 per line-shift; added the supplier-terms premium table, the 50% vehicle realisation, turnover costs, and the gross depreciation base. 15 checks → **32**, all exact |
