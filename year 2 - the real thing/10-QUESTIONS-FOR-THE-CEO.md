# 10 · Questions for the CEO — Meeting 1

Company 3 · simulation `B1SIM2C2` · CEO Meeting 1, Year 1 results and the Year-2 plan.
The five in section 1 go on **slide 36**. Sections 2 to 4 are the briefing behind them.

## The admission test

A question earns a place here only if **the answer changes a decision we have not yet made**.
Anything we can settle by reading our own report, running `python3 model/calibration.py`, or
waiting for a survey we have already bought is rejected — it is in section 3 instead, or in the
reserve with the reason it was demoted. Every euro figure traces to the fact pack, to
`08-YEAR-2-DECISION-REVIEW.md`, or to `06-OPEN-QUESTIONS.md`, and each is cited.

---

## 1 · The five to ask out loud

| #   | Question, in one line                                                         | Worth                    | Asks | Mark  |
| --- | ----------------------------------------------------------------------------- | ------------------------ | ---- | ----- |
| 1   | What determines the shelf space a brand actually gets in a channel?           | ~€12,000,000 a year      | CMO  | `[!]` |
| 2   | Does a prepayment on 2 January stop that year's interest?                     | €1,950,000               | CFO  | `[!]` |
| 3   | What does it take to open market E, and what does 98,165 units actually mean? | 20 idle lines · 110.1M   | MD   | `[~]` |
| 4   | How large is the §34 stockout penalty, and how many years does it run?        | €2,150,000 to €8,460,000 | COO  | `[!]` |
| 5   | Does the retailer margin buy us anything, or is it purely a deduction?        | €25,661,301 paid in Y1   | CMO  | `[~]` |

`[~]` The CMO asks two. If the board expects every director to take a turn, the CHRO opens
reserve question **R1** as a sixth — it is the only HR item with a decision attached.

---

### Q1 — CMO · What determines the shelf space a brand actually gets in a channel?

> **Spoken:** "In market A, thirty-five hypermarkets took 63,960 units of our moisturiser while
> thirty hypermarkets in market B took 2,057,439 of the same product — and those same thirty-five
> A stores took 2,587,071 units of our sunscreen. What decides how much shelf a brand actually
> gets, as against the shelf-space objective we type in?"

|                             |                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Why it matters**          | Moisturiser in market A took **22.60% share at the lowest price on the shelf** and finished third. Company 2 sold 7,782,836 at €9.50–10.50 with **our** campaign 19 and **our** (9,1) positioning; Company 4 sold 7,743,383 at €6.50–7.20. We sold 4,556,494. The gap is sized at **~€12,000,000 a year** and it is the single largest unexplained number in the company |
| **Corroborating fact**      | 501,093 units of moisturiser went unserved while **17,628,699 units sat in stock** and every logistic stockout flag read "No". Demand was censored by something that is not supply and not the fleet                                                                                                                                                                     |
| **What we assume now**      | That the 22% shelf-space objective was granted, and the gap is an awareness or in-store effect that surveys 11, 13, 14 and 15 will identify from rival behaviour                                                                                                                                                                                                         |
| **If shelf is rationed**    | — i.e. achieved shelf is allocated on retailer margin, price-to-retailer or POP: **Year 3 raises the moisturiser margin in market A above €1.00 and re-weights the €150,000 of POP toward channel G, and leaves price alone.** Cutting price further would be the exactly wrong move                                                                                     |
| **If shelf is granted**     | — i.e. the objective is always met and demand is allocated on share of voice and positioning: **Year 3 moves the €678,000 media budget into market-A moisturiser and does not touch the margin.** Media is currently split evenly A/B with no market-A weighting                                                                                                         |
| **Why we cannot settle it** | Survey 15 prices the *outcome* (shelf achieved by company and channel). No survey in the §50 menu names the *driver*. Buying the outcome twice does not identify the mechanism                                                                                                                                                                                           |

---

### Q2 — CFO · Does a prepayment on 2 January stop that year's interest?

> **Spoken:** "We have prepaid the €19,500,000 loan balance on 2 January. Is Year-2 interest
> charged on the balance outstanding after that payment, or on the 1 January opening balance
> regardless? It is €1,950,000 either way."

|                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Why it matters**                              | Our Year-2 financial line is forecast at **+€55,000** — a €195,000 prepayment penalty against €250,000 of deposit interest — and that assumes **no Year-2 coupon at all**. If interest is charged on the opening balance, the line is **-€1,895,000** and central net income falls from **€84,074,528 to €82,124,528**                                                                                                  |
| **The worse branch**                            | `[~]` Year 1 charged interest on **opening plus draw**: €2,600,000 = 10% × €26,000,000. That fixes the base at the start of the year but is silent on whether a 2-January payment reduces it. If the base is the full €26,000,000 opening — the €6,500,000 scheduled instalment included — Year-2 interest is €2,600,000 and net income is €81,474,528. Exposure is therefore €0 to €2,600,000, headline **€1,950,000** |
| **Where we are split**                          | `model/mmt39.py:1652` computes `interest = opening * rate` — the pessimistic reading. `model/calibration.py` and the Year-2 forecast use the optimistic one. Two of our own tools disagree, which is why it is a question and not an assumption                                                                                                                                                                         |
| **What we assume now**                          | The optimistic reading: prepay on 2 January, pay no Year-2 coupon. It is the reading behind the +24.0% headline on slide 33                                                                                                                                                                                                                                                                                             |
| **If interest follows the outstanding balance** | Nothing restates. **Year-3 policy: sweep every euro of surplus cash against debt on 2 January, every year.**                                                                                                                                                                                                                                                                                                            |
| **If interest follows the opening balance**     | We restate the forecast band at this meeting rather than at Meeting 2, and **Year-3 financing policy inverts: never prepay, draw as late in the year as possible, repay on the contractual schedule, and put the surplus in the 2.5% deposit instead.** A prepayment would then buy nothing in the year it is made                                                                                                      |
| **Why we cannot settle it**                     | It is unobservable until the Year-2 report, and it is the one number on our own forecast that we cannot verify before presenting it                                                                                                                                                                                                                                                                                     |

---

### Q3 — MD · What does it take to open market E?

> **Spoken:** "Market E has 110,100,000 units of potential and the whole industry sold 98,165
> units into it last year. Is that because nobody tried, or because there is a barrier for
> companies based in A and B — and if we wanted to open it in Year 3, what does it take?"

|                                       |                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Why it matters**                    | We hold **32 installed lines and activated 12**. Twenty moisturiser lines are idle, paid for, and depreciating. E is 110,100,000 units of potential — of which moisturiser is 75,000,000 (`SUMMARIES.txt` Appendix C). Only Companies 1 and 2 entered, and between them they moved **98,165 units, 0.09% of potential**                             |
| **What we assume now**                | That E is not worth entering: the observed uptake is near zero and the E logistics defaults cost us €0, so staying out is free                                                                                                                                                                                                                      |
| **If E is open on the same terms**    | — media, platforms, a dollar price, no lag: **Year 3 activates idle moisturiser lines against E rather than leaving them dark.** The capex is already sunk; the marginal cost is crew plus raw material at €2.1730 a unit                                                                                                                           |
| **If E carries a structural barrier** | — domestic incumbents, an entry lag, or a tariff we have not read: **we stay out permanently, the 20 idle lines are written off as a Year-1 sizing error, and Year 4 becomes a harvest year with no further capex.** That is a materially different four-year story and the board should hear which one we are telling                              |
| **Why we cannot settle it**           | We bought surveys 17, 18 and 19 (overseas prices, overseas sales, demand by company and market) but **not 9 or 12** — foreign advertising by A/B companies and by E domestic companies. So we will see *that* E sold nothing and never *whether Companies 1 and 2 actually advertised there*. Effort and demand are not separable from what we hold |

---

### Q4 — COO · How large is the §34 stockout penalty, and how long does it run?

> **Spoken:** "We left 1,827,440 units of sunscreen demand unserved in Year 1 and our Year-2
> plan leaves roughly 608,000 more. Section 34 says brand prestige is damaged — how large is
> that penalty, and does it decay after one year or accumulate?"

|                                   |                                                                                                                                                                                                                                                                                                                      |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Why it matters**                | Year 1 forwent **€26,497,880 of revenue and €12,702,797 of contribution** on the unserved sunscreen. The plant is now fixed at **6,688,800 units** — 32 of 32 line slots are used, so there is no capacity answer left. Price is the only instrument, and its correct setting depends on how expensive a stockout is |
| **What we assume now**            | That the penalty is real but unquantified, so we treat unserved demand as an asymmetric risk and nothing more                                                                                                                                                                                                        |
| **If the penalty is persistent**  | **Year 3 prices sunscreen at the top of the clearing band, €16.27 (e = -1.2), to drive unserved demand to zero**, accepting the volume loss as the price of stopping the damage                                                                                                                                      |
| **If it is one year or cosmetic** | **Year 3 prices at the central clearing price of €15.90 and tolerates the residual unserved demand**, which is the higher-contribution choice on the modelled band                                                                                                                                                   |
| **The spread**                    | The two answers are **€2,150,000 to €8,460,000 apart** across the defensible elasticity range (€15.32 at e = -2.5 to €16.27 at e = -1.2, central €15.90). We should say plainly that €15.00 is below the clearing price at *every* one of them — that is on slide 35, not here                                       |
| **Why we cannot settle it**       | `06-OPEN-QUESTIONS.md` #10 rules out testing it: deliberately stocking out to measure the penalty costs more than the answer. It can only be asked or inferred, and inference needs a year we do not have                                                                                                            |

---

### Q5 — CMO · Does the retailer margin buy us anything?

> **Spoken:** "We paid €25,661,301 in retailer margins last year — our second-largest line after
> cost of goods. Does the margin influence shelf space, listing or retailer push, or is it purely
> a deduction from our revenue?"

|                               |                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Why it matters**            | €25,661,301 on €189,365,764 of sales at MSRP. `model/calibration.py` has settled the accounting half — it is a straight euro-per-unit deduction, every euro of margin costs a euro. The **demand** half is untested and no line of our model contains a margin effect                    |
| **What we assume now**        | That the margin does nothing but cost money, and that €1.90 on sunscreen and €1.00 on moisturiser are conventional rather than chosen                                                                                                                                                    |
| **If it is a pure deduction** | **Year 3 cuts the sunscreen margin toward the legal floor.** Sunscreen sells out at every price we can defend, so margin on that product is contribution we hand away for nothing: €1.90 × 6,688,800 units = **€12,708,720** sits in that one field (derived from two fact-pack figures) |
| **If it buys shelf or push**  | It becomes the **cheapest instrument we own against the market-A moisturiser gap** — we raise the moisturiser margin in A instead of cutting price, which is the move Q1 also points at                                                                                                  |
| **Relationship to Q1**        | `[~]` Q1 and Q5 are two halves of one coin. If the CEO answers Q1 fully, Q5 may resolve with it — ask it anyway, because the sunscreen half of the answer stands on its own                                                                                                              |
| **Why we cannot settle it**   | Survey 20 gives rivals' **retail prices** by market and channel. Nothing in the §50 menu prices a rival's retailer margin, so we cannot infer it from what the field pays elsewhere                                                                                                      |

---

## 2 · Reserve bank — only if time allows, otherwise in writing

| #   | Question                                                                                             | Worth                  | Asks | If the answer is X we...                                                                           | Why demoted                                                          |
| --- | ---------------------------------------------------------------------------------------------------- | ---------------------- | ---- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| R1  | What reduces sales-rep turnover — the €27,000 base, the 0.60% incentive, or headcount?               | €270,000 a year        | CHRO | ...raise the self-funding incentive rather than the base in Year 3; if neither, stop paying for it | Smaller than any of the five; but it is the CHRO's only live lever   |
| R2  | Is the promotion field a per-unit reduction on promoted units, or a total budget?                    | €662,279               | CMO  | ...restate slide 32 at this meeting instead of Meeting 2                                           | The Year-2 report settles it before any Year-3 promotion is designed |
| R3  | If cash goes negative mid-year, is the deposit broken at the 1% fee or is the 20% overdraft charged? | €1M to €2M of deposit  | CFO  | ...size the Year-3 deposit to the whole surplus instead of holding a round €10,000,000             | We can size conservatively and lose only the yield                   |
| R4  | Is the SMED figure of 92.9% a constant, or does it depend on modules per line?                       | €6,000,000 of capex    | COO  | ...buy a third module in Year 3, or stop at two                                                    | The Year-2 report measures it directly `[!]` once, elsewhere         |
| R5  | Will loan maturity move again for Year 3, and does a change reschedule debt already owed (§42)?      | timing only            | CFO  | ...borrow early or late in the year we next need money                                             | Moot at zero debt; live the moment we borrow again                   |
| R6  | Where is the last-mile flag threshold, in units per vehicle?                                         | €170,400 vs €1,527,519 | COO  | ...cut the fleet again in Year 3, or restore it                                                    | Year 2 runs 42 vehicles on Year-1 volume and answers it for free     |
| R7  | Is the power realisation of 1.764582 structural, or refitted every year?                             | ~€3,500,000 on COGS    | CFO  | ...stop refitting it and treat standard cost as forecastable                                       | Re-solvable from the Year-2 printed standard costs                   |
| R8  | Is channel G allocated winner-take-most, or was our market-A moisturiser simply not listed?          | several million        | CMO  | ...decide whether channel G is contestable at all in market A                                      | Overlaps Q1; ask only if Q1 gets a partial answer                    |
| R9  | Does storage cost scale with platform count — €0.0295/unit at 12 platforms against €0.0193 at 6?     | up to €1,000,000       | COO  | ...run 6 platforms in one market in Year 3 as a paired test                                        | Testable ourselves at bounded cost                                   |

---

## 3 · Do not ask — already settled

Burning a turn on any of these tells the board we have not read our own report.

| Question                                                           | The answer, and where it came from                                                                                                                                                                                                |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How many lines can one SMED module serve?                          | Several. Test Y2 ran 2 modules across 32 lines at 92.9%. **This is question 2 on the current slide 30 — remove it**                                                                                                               |
| Is loan interest charged in the draw year?                         | Yes, on the full drawn balance: €2,600,000 = 10% × €26,000,000. Note this does **not** answer Q2, which is about a prepayment                                                                                                     |
| What proportion of a loan repays each year?                        | One quarter at a 4-year maturity — €6,500,000 on €26,000,000. Re-read INF each year; the test round ran 3                                                                                                                         |
| Which reading of §24 does the simulator use?                       | Neither. A flat **81.25%** with preventive maintenance, and raw material at a flat 2%                                                                                                                                             |
| Does preventive maintenance pay?                                   | Yes, twice. 81.25% against 78.75% for €500,000, and it cuts repairs from €16,829 to €12,224 per line-shift                                                                                                                        |
| Does the training department pay?                                  | **No.** €24,000 -> €9,000 an office leaver, 4 leavers, €60,000 of saving against €722,000 of cost. Switched off for Year 2                                                                                                        |
| Does the undrawn credit line cost anything?                        | 2% — 1% upfront plus 1% service. €200,000 on €10,000,000, drawn nothing. Set to zero for Year 2                                                                                                                                   |
| Do 120-day supplier terms cost anything?                           | **3% of raw material.** €1,343,918 in Year 1 to buy float worth €384,510                                                                                                                                                          |
| Is the depreciation base gross or net, land included?              | Gross, lines and SMED only. Land and buildings are never depreciated. €6,480,000 = 12% × €54,000,000                                                                                                                              |
| Are receivables on MSRP or on net revenue?                         | Net revenue. €27,284,077 = 2/12 × €163,704,462. Retailer margins are paid immediately (§38)                                                                                                                                       |
| Do the market-E logistics defaults cost anything?                  | **No.** 60 platforms and 40 vehicles in E with no E price were charged €0, and the simulator's own screen says to leave them                                                                                                      |
| Is the last mile drop-driven or tonnage-driven?                    | Drop-driven. 50 vehicles cleared 20,396,301 units with no flags                                                                                                                                                                   |
| Do the eight promotion types map to the survey codes?              | Survey 22's legend is offset by one — code 1 is *no promotion*. The decision sheet uses the scenario's numbering                                                                                                                  |
| Does "units demanded of your brand" mean total or unserved demand? | **Unserved only.** Moisturiser prints 501,093 against 14,546,301 units sold; a total-demand reading would put demand below sales, which is impossible. Our whole clearing-price method rests on this and it is settled internally |
| Is finished-goods stock charged a warehouse cost?                  | **No.** 17,628,699 units were held all year with no charge in the report                                                                                                                                                          |
| Why is our inventory turnover 1.62?                                | It is not. The printed figure reproduces from no combination of the statements — a known artefact. **Do not quote it, and do not ask about it**                                                                                   |

---

## 4 · What the CEO will ask us — the standing answers

Rows marked **NEW** extend `05-CEO-MEETING-AND-REPORT-PACK.md` to cover the Year-2 decisions.
Every answer carries its number because the number is the answer.

### 4a · Year 1 — carried forward from doc 05

| Question                                     | Our answer                                                                                                                                                                                                                       |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why three shifts?                            | Labour is charged per line-shift inside standard cost, so cost per unit is identical at 1, 2 or 3 shifts. The only cost is 2 points of depreciation; matching the output at two shifts would need 33 lines against a 32-line cap |
| Why did net income miss your plan by €44.3M? | We built 32,175,000 units of moisturiser against demand of 15,047,394. It is a planning error, not an execution one — output landed at exactly 195,000 and 487,500 units per line-shift, to the unit                             |
| Why did moisturiser lose market A?           | We were the **cheapest** and finished third at 22.60%. Company 2 sold 71% more at €3.00–4.00 above us using our campaign and our positioning. Price is not the driver. Surveys 11, 13, 14 and 15 are bought to find what is      |
| Why is your debt ratio 3.3× the industry?    | It was, on a €26,000,000 loan we did not need. It is **zero** after the Year-2 prepayment                                                                                                                                        |
| Why is inventory so high?                    | Unsold units never deteriorate and sell first next year (§3). €40,990,251 of it is production cost already paid; Year 2 converts 61% of it back into cash                                                                        |
| Why own the sales network?                   | Wholesalers take 8.46% of retail price — €16.0M on Year-1 sales, against €3.9M for our own managers and reps, and the gap widens with every price rise                                                                           |
| Why no factoring?                            | §41 adds receivables back to available cash on 2 January, so declining it costs only intra-year timing. We closed Year 1 with no overdraft and an untouched credit line                                                          |
| Why no Poka Yoke?                            | €720,000 per line, applied to every line ever installed. Payback runs past the end of the game                                                                                                                                   |
| Why is transport 530% over the reference?    | 50 last-mile vehicles were sized for 37.8M units and moved 20,396,301 — €0.0441 a unit against the §12 reference of €0.007. The trunk leg ran €0.0065 against €0.006 and is right-sized                                          |

### 4b · Year 2 decisions — NEW

| Question                                                            | Our answer                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why activate only 2 of 22 moisturiser lines?                        | 17,628,699 units are already in the warehouse against Year-1 demand of 15,047,394. Running the other 20 spends €27,270,000 of crew and €36,899,200 of raw material to make stock we cannot sell — **€64,200,000 of cash**                                                        |
| Why buy SMED?                                                       | 81.25% -> 92.9% on lines we already own. Sunscreen goes 5,850,000 -> **6,688,800** units and standard cost falls €5.5604 -> €5.0853 at cash terms. **+€9,160,000 in Year 2 on €6,000,000 of capex, payback 0.65 years**                                                          |
| Why prepay the loan?                                                | A 1% penalty of €195,000 cancels €1,950,000 + €1,300,000 + €650,000 of 10% coupons across Years 2–4. Year 1 paid €3,060,000 of financial expense on money that closed the year unused `[~]` subject to Q2                                                                        |
| Why drop the credit line?                                           | 2% of the facility is charged whether or not it is drawn. We paid €200,000 in Year 1 and drew nothing, against a cash trough €32M deep                                                                                                                                           |
| Why drop the training department?                                   | €722,000 bought €60,000 of measured saving, and it does nothing for sales-rep turnover, which is 4.5× larger                                                                                                                                                                     |
| Why move supplier terms to cash?                                    | 120 days cost 3% of raw material — €1,343,918 in Year 1 — to buy float worth €384,510 at the deposit rate. Cash terms save **€434,174** and cut standard cost to €5.0853 and €2.1730                                                                                             |
| Why is your forecast +24.0% when you cut moisturiser output by 90%? | Because we are selling stock, not output. 17,628,699 units carried at €2.3252 sell first under FIFO (§3), so **20,973,099 units are available** against a forecast 14,073,013 sold                                                                                               |
| Why raise sunscreen only to €15.00?                                 | **We should not have.** €15.00 is below the clearing price at every defensible elasticity — €15.32 to €16.27, central €15.90. Central forgone **€5,990,000**, and ~608,000 units go unserved a second year. Year 3 prices at the clearing price                                  |
| Why hold moisturiser in market B at €7.50?                          | **The weakest field on the sheet.** €8.75 beats €7.50 at both ends of the range — by €5,470,000 at e = -0.9 and €640,000 at e = -1.6. B is our best-measured price point and the nearest rival sells at €10.00–11.00                                                             |
| Why are both products priced the same in A and B?                   | An avoidable error. It gives up the within-year cross-market elasticity read, which is the most valuable experiment available and costs nothing to run. Year 3 differs at least one product by €1.00 across markets                                                              |
| Why run the promotion in both markets?                              | Also avoidable. Market A alone costs **€64,000** and answers the same question; both markets cost **€662,279** and weakened the control. The design still reads as A/S against A/T                                                                                               |
| Will the promotion pay?                                             | On the modelled elasticity, no — it needs a **13.6%** uplift on channel S to break even and a 6.7% discount at e = -0.9 buys about 6.2%. We are buying the **first measurement of a promotion in this simulation**, and stating that openly                                      |
| Why cut the last-mile fleet to 42 vehicles?                         | It recovers €170,400 of a €0.0441-per-unit overspend. `[!]` It is the one uncosted risk in the plan: load per vehicle rises 20.7% with no measured headroom, and a single flagged market cost €1,527,519 in the test round                                                       |
| Why deposit only €10,000,000?                                       | Right instrument, undersized — the year closes near €120M of cash. It earns €250,000 at 2.5%. Year 3 sizes the deposit to the actual surplus, worth €1–2M `[~]` subject to reserve question R3                                                                                   |
| Why spend €680,600 on 22 surveys, up from €166,800?                 | Against a market-A moisturiser gap sized at ~€12,000,000 a year, €680,600 is not a cost. It buys surveys 4, 11, 13, 14 and 15 — precisely the variables that could explain it                                                                                                    |
| Why leave market E blank again?                                     | 98,165 participant units against 110,100,000 of potential, and the defaults cost €0. `[~]` We are asking the board directly whether that number is a demand fact or an effort fact — see Q3                                                                                      |
| How confident are you in 92.9% for SMED?                            | `[!]` It is measured **once**, in a different simulation instance. €6,000,000 of capex and €9,160,000 of Year-2 contribution ride on it. At 81.25% the SMED case collapses to zero and the forecast loses that €9,160,000                                                        |
| What is the biggest risk to your forecast?                          | Company 4 adding a third shift. It ran 2 shifts on ~17 lines in Year 1, sold out, and already matches Company 2's moisturiser share in market A. A third shift adds roughly 50% to its output and none of it is in our band                                                      |
| What would you do differently in Year 1?                            | Two things, both priced: build for demand of 15,047,394 rather than 32,175,000, and take €26,000,000 less debt. Together **€40,990,251 of trapped cash and €3,060,000 of financial expense**. Both are already fixed in Year 2                                                   |
| What are you committing to for Year 2?                              | Central net income **€84,074,528** (+24.0%), band **€82,511,510 to €86,202,865**; sunscreen sold out at 6,688,800 units; moisturiser stock down from 17,628,699 to **6,900,086**; zero debt at 31 December; first on accumulated profit held `[!]` see the correction note below |

`[!]` **Correction to carry into the deck.** The existing slide 30 commits to "87.5 M € of net
income — up 29%", "42% unit share" and "5.9 M units of H stock". None of the three reproduces
from the fact pack. The defensible figures are **€84,074,528 (+24.0%)** central, a band of
**€82,511,510 to €86,202,865**, and **6,900,086** units of closing moisturiser stock. Slide 36
must carry those. A commitment the CEO can falsify with our own model is worse than a modest one.

---

## Sources

`06-OPEN-QUESTIONS.md` (both tables) · `00-CALIBRATION-CONSTANTS.md` (every `[~]` reading) ·
`08-YEAR-2-DECISION-REVIEW.md` §12.1, §13.1, §14.1, §15.1 and the scorecard ·
`07-YEAR-2-DECISIONS-AS-ENTERED.md` · `05-CEO-MEETING-AND-REPORT-PACK.md` (standing answers) ·
`01-DEMAND-MODEL.md` (anchors and elasticities) · `03-YEAR-3-DECISION-PLAYBOOK.md` ·
`anthony results + review/01-results-vs-plan.md` §2, §3b, §5, §6, §8 ·
`anthony results + review/03-model-vs-actual.md` §b, §d ·
`CEO_Meeting_1_Company3.pptx` slide 30 (superseded by section 1) ·
`SUMMARIES.txt` Appendix B (superseded) and Appendix C (market-E sizing) ·
`DIR0114SI02083TE3Y1REP.pdf` p2–p6, p8 · `DIR0114SI02083TE3Y1INV.pdf` surveys 1, 3, 20, 21, 22, 23, 27, 28 ·
`DIR0114SI02083TE3Y1INFen_US.pdf` p2 · `model/calibration.py` (32/32) · `model/mmt39.py:1652` ·
`Scenario MMT39 .pdf` §3, §18, §20, §24, §27, §28, §34, §38, §41, §42, §50.
