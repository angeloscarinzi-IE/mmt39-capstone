# 06 · Open questions and the experiments that settle them

## Still unknown, ranked by how much money the answer moves

| #   | Question                                                                 | Size             | How to settle it                                                                                          |
| --- | ------------------------------------------------------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------- |
| 1   | **Why does market A's moisturiser resist us?**                           | ~€12M a year     | Surveys 11, 13, 14, 15 — **all four bought for Year 2**. We were cheapest and finished third of three     |
| 2   | How far can the sunscreen price rise before demand falls below capacity? | €2–8M a year     | `clearing_price()` on the Year-2 demand line. Then price two markets differently in Year 3                |
| 3   | **Does SMED really deliver 92.9%?**                                      | €6M of capex     | Year-2 units produced ÷ (nameplate × 3 × lines). Measured once, in a different simulation instance `[!]`  |
| 4   | What does a promotion actually do?                                       | unknown          | Year-2 "units sold on promotion", A/S and B/S against A/T and B/T as controls. **First ever measurement** |
| 5   | Is channel G winner-take-most?                                           | several million  | Survey 4, bought for Year 2. A/G took 63,960 H units across 35 stores; B/G took 2,057,439 across 30       |
| 6   | Where is the last-mile stockout threshold?                               | €1.5M a year     | Year 2 runs 42 vehicles against Year 1's 50 on the same volume. If no flag, cut again `[!]`               |
| 7   | Does a cash or 60-day supplier term price at list?                       | €250–350k a year | 90 and 120 days are measured at 1.27% and 3.00%; 0 and 60 days are interpolated                           |
| 8   | Is the power realisation of 1.7646 stable, or a per-year fit?            | ~€3.5M on COGS   | Re-solve it from the Year-2 printed standard costs. Two years of stability would make it structural       |
| 9   | Is storage cost proportional to platform count?                          | up to €1M        | €0.0295/unit at 12 platforms vs €0.0193 at 6. Try 6 platforms in one market in Year 3                     |
| 10  | What does a finished-goods stockout cost in later years?                 | §34, unbounded   | Never worth testing deliberately. Infer it from the Year-2 sunscreen share after 1,827,440 went unserved  |

## Answered — do not spend a question or a survey on these

| Question                                              | Answer                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| How many lines can one SMED module serve?             | Several. Test Y2 ran 2 modules across 32 lines at 92.9%                                                                       |
| What proportion of a loan repays each year?           | One quarter at a 4-year maturity. The graded round reset to 4 years after the test round showed 3 — **re-read INF**           |
| Is loan interest charged in the draw year?            | Yes, on the full drawn balance: €2,600,000 = 10% × €26,000,000                                                                |
| Which reading of §24 does the simulator use?          | Neither — a flat 81.25% with preventive maintenance, and raw material at a flat 2%                                            |
| Does preventive maintenance pay?                      | Yes, twice: 81.25% against 78.75% for €500,000, **and** it cuts the repair bill from €16,829 to €12,224 per line-shift        |
| Does the training department pay?                     | **No.** It cuts the office rate from €24,000 to €9,000 a leaver — 4 leavers, €60,000 — and costs €722,000                     |
| Does the undrawn credit line cost anything?           | 2%: 1% upfront plus 1% service. €200,000 on €10,000,000                                                                       |
| Do 120-day supplier terms cost anything?              | **3% of raw material.** €1,343,918 in Year 1, to buy float worth €384,510                                                     |
| Is the depreciation base gross or net, land included? | Gross, lines and SMED only. Land and buildings are not depreciated                                                            |
| Are receivables on MSRP or net revenue?               | Net revenue. Retailer margins are paid immediately (§38)                                                                      |
| Do the E logistics defaults cost anything?            | **No.** 60 platforms and 40 vehicles in E with no E price were charged €0 — and the simulator's own screen says to leave them |
| Is the last mile drop-driven or tonnage-driven?       | Drop-driven. 50 vehicles cleared 20.4M units with no flags                                                                    |
| Do the eight promotion types map to the survey codes? | Survey 22's legend is offset by one: code 1 is *no promotion*. The decision sheet uses the scenario's numbering               |

## Experiment discipline for a graded year

Bound the downside every time: **one channel, one market, never a whole product line.** Hold
everything else at the level that produced the current demand anchors — media, margins, shelf
space, POP — because the forecast is conditional on them. Changing two things at once means
learning neither.

`[!]` **Year 2 broke this twice.** The promotion ran in both markets rather than one, costing
€275,000 more than the same answer required and weakening the cross-market control. And both
products were priced flat across A and B, which gave up the within-year elasticity read
entirely. Neither error was expensive on its own; together they cost a year of measurement in a
four-year game.

`[+]` **Year 2 also got the discipline right where it counted.** Media, campaigns, positioning,
shelf space, POP, salesforce and salaries were all held at Year-1 levels, so the price and
promotion effects will be readable against a clean background. That restraint is what makes the
€680,600 of surveys worth buying.
