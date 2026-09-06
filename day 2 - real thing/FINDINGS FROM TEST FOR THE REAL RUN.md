# FINDINGS FROM TEST FOR THE REAL RUN

**MMT39 · Company 3 · Simulation B1SIM2C1 (test round) → graded round, 4 virtual years**
**Written 6 September 2026, before Year 1 of the graded round is entered.**

The test round was worth exactly one thing: it turned the scenario PDF from a document we
*interpreted* into a machine we have now *measured*. This file records what the machine actually
does, what it cost us to find out, and what each finding changes about the Year-1 decision.

Every number below is either quoted from the Year-1 result reports or recomputed from them. A
verification script reproduces all 34 of the checks in this document from the reported actuals; the
standard-cost formula in §3 reproduces the simulator's own figure to within 0.03%.

---

## 0 · What this is based on, and what is missing

| Evidence                                     | Status                                                                                                                |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Year-1 decisions as submitted (`…Y1DEP.pdf`) | [+] complete — the authoritative record                                                                               |
| Year-1 results (`…Y1REP.pdf`)                | [+] complete — P&L, balance sheet, ratios                                                                             |
| Year-1 surveys 20-24 (`…Y1INV.pdf`)          | [+] complete — every rival's prices and profit                                                                        |
| Year-1 general information (`…Y1INF.pdf`)    | [+] complete — Director's factor values                                                                               |
| `day 1/DECISIONS-EXPLAINED_year1.txt`        | [+] our plan, and where it diverged from entry                                                                        |
| `day 1/DECISIONS-EXPLAINED_year2.txt`        | [~] a plan only — never validated by results                                                                          |
| Year-2 test **results**                      | [!] NOT IN THIS REPO. `06-graded-year1-plan-2.1.md` quotes them, but every file it cites for them is absent — see §14 |
| `day 2 - real thing/`                        | [!] empty at the time of writing                                                                                      |

⚠️ Two consequences. First, everything below is calibrated on **one** observed year, so a rule that
fits one data point is labelled as such. Second, the Year-2 test plan (enter market E, 32 lines,
€104M loan) was never confirmed by a results sheet — **do not carry its numbers into the graded run
as if they were tested.** Several of them are now known to be wrong; see §9.

⚖️ The graded round is a **new simulation**. Mechanical findings (§3) carry over exactly. Behavioural
findings (§4, §8 — what rivals did, what share we won) are priors, not facts: the other four teams
also spent Saturday learning.

---

## 1 · The scoreboard: 2nd of 5, and why that flatters us

| Metric                            | Company 3 (us) | Industry average | Rank            |
| --------------------------------- | -------------- | ---------------- | --------------- |
| Net income                        | €4,919,135     | €1,014,914       | 2 of 5          |
| Accumulated profit                | €4,919,135     | —                | 2 of 5          |
| Profit margin (income / net rev.) | 8.39%          | 2.37%            | —               |
| ROE (income / closing equity)     | 6.94%          | 0.91%            | —               |
| ROA                               | 4.44%          | 0.41%            | —               |
| Debt ratio (debt / assets)        | 35.94%         | 7.19%            | [!] worst by 5x |
| Total asset turnover              | 0.53           | 0.37             | —               |

Rival net income (survey 23): Company 2 **+€7,366,632** · Company 3 (us) +€4,919,135 · Company 4
+€2,609,602 · Company 5 −€3,157,092 · Company 1 −€6,663,707.

✅ We were profitable while two of five teams were not, and our operating income (€8,214,100) was
*higher* than the winner's net income. ⚠️ But we lost first place below the operating line, to
mistakes that were entirely self-inflicted. The debt ratio tells the story: five times the industry's
leverage, in a year in which no team needed to borrow at all.

**There is no corporate tax in this simulation.** Operating income €8,214,100 − financial expenses
€3,294,965 = net income €4,919,135, exactly. Every euro saved below the operating line is a euro of
net income and a euro of accumulated profit — which is 10% of the course grade.

---

## 2 · The three errors, and the counterfactual

### 2.1 The raw-material order — one field, €1.58M net

We bought **130,600,000** units of H raw material. Production needed **13,923,000**. A 10x
mis-keying.

| Consequence                             | Amount       |
| --------------------------------------- | ------------ |
| Raw material left on the balance sheet  | €109,431,358 |
| Cash and equivalents at 31 December     | −€33,411,377 |
| Overdraft interest (20%)                | €1,892,199   |
| Credit-line interest (line fully drawn) | €244,193     |
| Loan interest                           | €382,605     |
| Fees (see §3.6)                         | €238,260     |
| Fixed-term deposit income earned        | €0           |

[+] The one thing it bought: the enormous order earned a **10.7% volume discount**, H raw material
at €0.9379 against the €1.05 list price — worth €1,560,570. Netting that against the financing
damage, the error cost about **€1,576,157**. It also left us starting Year 2 with negative cash and
€30.6M of payables, which is what forced the €104M loan in the (untested) Year-2 plan.

### 2.2 The last mile — €1.19M avoidable

One vehicle per market on the platforms→retailers leg. Result: logistic stockouts in **three of the
four domestic legs**, and a charge of €2,506,409 — €0.1737 per unit against the scenario's €0.007
guideline, **25 times over**. Full analysis in §5.

### 2.3 Market E — €184,000 for nothing

We set prices and retailer margins for E, and we bought and paid for E advertising, but we left
**shelf space at 0** and **campaign at 0**. §21 is explicit: no shelf space means the simulator
assumes you do not want the channel. We sold zero units in E and paid for the privilege:

| Item                           | Cost         |
| ------------------------------ | ------------ |
| S insertions in E (1 PR, 2 TV) | $56,000      |
| H insertions in E (3 PR, 4 TV) | $128,000     |
| **Total burned in market E**   | **$184,000** |

### 2.4 What Year 1 should have been

| Line                                                             | Amount         |
| ---------------------------------------------------------------- | -------------- |
| Net income as reported                                           | €4,919,135     |
| + financing damage removed (no overdraft, no loan, deposit kept) | +€3,132,257    |
| − raw material at list price instead of the volume discount      | −€1,556,100    |
| + last mile planned properly (§5) instead of emergency rates     | +€1,190,609    |
| **Counterfactual net income**                                    | **€7,685,901** |
| Company 2's actual net income (the winner)                       | €7,366,632     |

📌 **Two fields and one fleet decision cost us first place.** Nothing about the strategy did.

---

## 3 · What the simulator actually does — the calibrated constants

This is the most valuable section in the file. These are no longer readings of the scenario; they are
measurements. Unless the Director changes a factor, they hold in the graded round.

### 3.1 Line utilisation is exactly 81.25% ✅

| Product | Nameplate (§23)                            | Actual output | Ratio        |
| ------- | ------------------------------------------ | ------------- | ------------ |
| S       | 240,000 x 2 lines x 2 shifts = 960,000     | 780,000       | **0.812500** |
| H       | 600,000 x 14 lines x 2 shifts = 16,800,000 | 13,650,000    | **0.812500** |

Identical to six decimal places for both products. In hours: 4,000 scheduled − 750 lost = 3,250
operating. Our model used 80.675% and therefore **understated every capacity number by 0.71%**.

| Configuration (2 or 3 shifts, PM on) | Sellable units per line-year |
| ------------------------------------ | ---------------------------- |
| S line, 2 shifts                     | 390,000                      |
| S line, 3 shifts                     | 585,000                      |
| H line, 2 shifts                     | 975,000                      |
| H line, 3 shifts                     | 1,462,500                    |

⚖️ Preventive maintenance is confirmed as worth buying. The no-PM arithmetic (140 breakdowns x 2.5 h
+ 100 module stops x 5 h = 850 hours lost) gives 78.75%; we observed 81.25%. PM buys **+2.5 points of
nameplate for €500,000** — marginal at 16 lines, clearly positive at 3 shifts or 24+ lines.

### 3.2 Raw material = production x 1.02, exactly ✅

| Product | Units produced | RM units used | Ratio      |
| ------- | -------------- | ------------- | ---------- |
| H       | 13,650,000     | 13,923,000    | **1.0200** |
| S       | 780,000        | 795,600       | **1.0200** |

📌 **Raw materials to purchase = planned production x 1.02 − opening RM stock.** Not a derivation from
breakdown hours; a flat 2%. This one line replaces a whole page of our old scrap model.

### 3.3 Standard cost — a formula that reproduces the simulator to 0.03%

```
SC = 1.02 x RM_negotiated_price
   + 1.70 x power_rate
   + (specialists x spec_wage + operators x op_wage) / (nameplate_per_shift x 0.8125)
   + 70 x 2.5 x 4 x 24.041 / (nameplate_per_shift x 0.8125)
```

| Product | RM     | Power  | Labour | Repairs | Model SC | Reported SC | Error  |
| ------- | ------ | ------ | ------ | ------- | -------- | ----------- | ------ |
| S       | 1.7044 | 0.4250 | 3.3231 | 0.0863  | 5.5388   | 5.5371      | +0.03% |
| H       | 0.9567 | 0.2550 | 0.9323 | 0.0345  | 2.1785   | 2.1788      | −0.01% |

[~] The **1.70 multiplier on power is empirical**, not stated anywhere in §33 or §49. It was fitted to
one product and then reproduced the other to within 0.03%, which is strong evidence but not proof.
[~] The repair term uses the **full 2.5 h**, i.e. preventive maintenance does *not* reduce the
technicians' bill even though it does raise utilisation. Re-fit both in Year 1 of the graded run.

Crew per line-shift (§30): S = 9 specialists + 32 operators · H = 6 specialists + 23 operators.

### 3.4 Raw material price moves with order size — two data points

| Product | Units ordered | Terms   | Price paid | vs list | Note                                                      |
| ------- | ------------- | ------- | ---------- | ------- | --------------------------------------------------------- |
| H       | 130,600,000   | 90 days | €0.9379    | −10.68% | [+] the accidental mega-order                             |
| S       | 780,000       | 90 days | €1.6710    | +1.27%  | [!] of which +0.29% is the §28 penalty for under-ordering |

Stripping the penalty, a small order at 90 days costs **+0.98% over list**; a very large one at the
same terms costs **−10.7%**. ⚖️ The discount is real and worth planning for — order the whole year in
one purchase — but the shape of the curve between 1M and 130M units is unknown. Do not "buy the
discount" with cash you need.

📌 Survey 24 put the industry's average production cost at S €5.47 / H €2.30 against our €5.5371 /
€2.1788. **Our only production-cost advantage in Year 1 was an accident of the mis-keyed order.**

### 3.5 Revenue, commission and R&D mechanics ✅

| Rule                                                                      | Verified against         |
| ------------------------------------------------------------------------- | ------------------------ |
| Total sales = MSRP x units (retail value)                                 | €8,586,286 / €64,522,316 |
| Retailer margin is a straight €/unit deduction                            | €1,482,000 / €12,967,500 |
| Net revenue = (MSRP − margin) x units                                     | €7,104,286 / €51,554,816 |
| R&D = **4.5% of RETAIL sales**, not of net revenue                        | €3,289,887               |
| Rep commission = 0.6% of net revenue in **channels S and T only**         | €310,685                 |
| Depreciation = 10% of **production lines only** (land is not depreciated) | €2,520,000               |
| Factoring = 5.5% annual x (collection months / 12) x net revenue          | €537,708                 |
| Sales network A = 6 x €50,000 + 48 reps x €26,000                         | €1,548,000               |

📌 Channel G carries **no** sales commission — 0.6% of *all* net revenue would have been €351,955, and
the simulator charged €310,685. Hypermarket volume is commission-free.

📌 Every €1.00 added to an MSRP costs €0.045 of extra R&D and nothing else. **We keep €0.955 of every
price increase**, versus the 13% our Year-1 notes assumed.

### 3.6 Finance mechanics ✅

| Component                                   | Amount       | Rule                         |
| ------------------------------------------- | ------------ | ---------------------------- |
| Loan interest                               | €382,605     | 10% x €3,826,050             |
| Loan amortisation due 2 January             | €956,512     | 1/4 of principal (4-yr term) |
| Loan upfront fee                            | €38,260      | 1% of principal              |
| Credit-line upfront fee                     | €50,000      | 1% of the €5,000,000 line    |
| Fixed-term deposit early-withdrawal penalty | €150,000     | 1% of €15,000,000            |
| **Total "Fees" line**                       | **€238,260** | sums exactly                 |

[!] **The €15,000,000 fixed-term deposit earned zero interest and cost €150,000.** When cash went
negative the simulator cancelled it to plug the hole, exactly as §40 says it will. Never hold a 2.5%
asset while running any risk of a 20% overdraft.

[!] The credit line appears on the balance sheet at its full €5,000,000 — **it was drawn, not merely
held**. A credit line is not a free safety net; it is a facility the simulator will use on your behalf.

### 3.7 How the reported ratios are computed (needed for the CEO deck)

| Ratio          | Numerator   | Denominator                        | Our Year 1 |
| -------------- | ----------- | ---------------------------------- | ---------- |
| Profit margin  | Net income  | **Net** revenue €58,659,102        | 8.386%     |
| ROE            | Net income  | **Closing** equity €70,919,135     | 6.936%     |
| ROA            | Net income  | Closing total assets               | 4.444%     |
| ROI            | Net income  | **Gross** fixed assets €37,200,000 | 13.224%    |
| Asset turnover | Net revenue | Closing total assets               | 0.530      |

### 3.8 Everything resets to a template every year [!]

The Year-2 decision screens (screenshots, `day 1/year 2/`) open with: sales managers **0 / 0 / 0**;
platforms **30 / 30 / 60**; transport to platforms **10 vehicles x 12,000 kg** in every market;
transport to retailers **30 vehicles x 1,500 kg** in every market; all finance fields **0**; factoring
**unchecked**; supplier terms back to **Cash**; and all salaries back to the legal minimum.

⚠️ Lines installed carry over, but **"lines to be activated" resets to zero.** An installed,
unactivated line produces nothing.

📌 The logistics screen carries an on-screen note our documents never recorded: *"If your company is
not operating in a market or is using wholesalers for transport to retailers, no cost will be
allocated for this concept. Leave the default decisions as they are."* This is confirmed by the
result: we left E at its 60-platform / 10-vehicle / 30-vehicle default and were charged nothing for
it. **The logistics template default in an unused market is harmless — the trap is elsewhere.**

### 3.9 Depreciation is charged on the lines, not on the land [+]

Reported depreciation was €2,520,000 = **10% of the €25,200,000 of production lines**. The
€12,000,000 of land, buildings and facilities we start with is **not** depreciated; 10% of the full
€37,200,000 asset base would have been €3,720,000. So the cost of a third shift is two percentage
points on the **line** value only — on a €36.6M plant, €732,000.

### 3.10 Three shifts dominate two, and it is not close

Production labour is charged **per line-shift** and sits inside the standard cost, so the standard
cost per unit is **identical at 1, 2 or 3 shifts**. The only cost of adding a shift is the
depreciation step (8% → 10% → 12% of line value).

| Route to 26,910,000 units | Lines needed | Capex       | Depreciation | Slots used   |
| ------------------------- | ------------ | ----------- | ------------ | ------------ |
| 3 shifts                  | 6 S + 16 H   | €36,600,000 | €4,392,000   | 22 of 32     |
| 2 shifts                  | 9 S + 24 H   | €54,900,000 | €5,490,000   | 33 — ILLEGAL |

[!] Reaching the same output at 2 shifts costs **€18,300,000 more of irreversible capex** and needs
33 lines, which breaches the 32-line ceiling outright. The Year-1 pack's "2 shifts, not 3, because
depreciation rises from 10% to 12%" priced the depreciation step without pricing the lines that step
forces you to buy.

### 3.11 The two HR remedies we were about to buy do not pay

| Remedy                          | Annual cost | Measured problem it addresses               | Verdict                         |
| ------------------------------- | ----------- | ------------------------------------------- | ------------------------------- |
| Selection & training department | €722,000    | €336,000 of total turnover cost, 11 leavers | [!] never pays                  |
| Raising office pay ~5%          | ~€147,000   | €96,000 — 4 office leavers at €24,000 each  | [!] costs more than the disease |
| Raising rep pay €26k to €28k    | €168,000    | €210,000 — 7 sales leavers at €30,000 each  | [~] marginal at best            |

📌 **Absenteeism did not bite at operator €13,500 / specialist €24,000.** Output landed on exactly
81.25% — the theoretical maximum for that plant. §31 warns that low pay lowers productivity; at these
wages it measurably did not. Production wages sit inside the standard cost and there are 2,130 of
them at 22 lines on three shifts, so **holding them at the tested level is worth about €729,000 a
year** and costs nothing we can measure.

### 3.12 Factoring is optional, and expensive when cash is positive

Factoring cost €537,708 = 5.5% x (2 months / 12) x net revenue, exactly. §41's available-cash formula
**adds accounts receivable back** on 2 January, so declining to factor does not reduce the cash next
year's plan can draw on — it only delays collection inside the year by the payment term.

⚖️ In the test round we needed the liquidity because of the raw-material error. On a cash-positive
plan factoring is a pure cost: at €184M of net revenue on 60-day terms it would be **€1,688,875**,
against about €100,000 for a €5,000,000 credit line covering the same two-month gap.

### 3.13 Market size is a baseline, not a ceiling

§3 gives per-capita consumption "at the beginning of the simulation" and then says plainly:
*"demand will change according to the marketing strategy employed by each company."* Our brand alone
generated demand equal to **52% of the entire A+B baseline** in Year 1. Treat the 21.1M and 56.26M
unit figures as the market's starting scale, not as a share cap.


---

## 4 · Pricing: the finding that matters most

### 4.1 We were not demand-constrained. We were capacity-constrained, twice over

| Product | A+B market size | Demand for our brand | Share of market | Units we could supply | Demand served |
| ------- | --------------- | -------------------- | --------------- | --------------------- | ------------- |
| S       | 21,100,000      | 8,419,028            | 39.9%           | 780,000               | **9.3%**      |
| H       | 56,260,000      | 31,966,201           | **56.8%**       | 13,650,000            | **42.7%**     |
| Total   | 77,360,000      | 40,385,229           | 52.2%           | 14,430,000            | 35.7%         |

Closing finished-goods inventory: **zero** for both products. We sold every unit we made.

### 4.2 Our moisturiser was the cheapest in the market by a third

Survey 20, market A, channel G — every company's retail price:

| Company | S price | H price   | Net income      |
| ------- | ------- | --------- | --------------- |
| 1       | €8.50   | €7.00     | −€6,663,707     |
| 2       | €9.50   | €8.50     | **+€7,366,632** |
| 3 (us)  | €10.40  | **€4.45** | +€4,919,135     |
| 4       | €7.20   | €6.50     | +€2,609,602     |
| 5       | —       | —         | −€3,157,092     |

📌 **Company 2 charged 1.9x our moisturiser price and out-earned us by 50%.** Even Company 4, the
cheapest rival, was 46% above us on H. We generated 56.8% of the entire A+B moisturiser demand — the
market was telling us, in the loudest possible way, that the price was wrong.

### 4.3 The size of the prize

At Company 4's H prices (€6.50 / €6.80 / €7.20 by channel, still the cheapest branded option), on the
same 13,650,000 units we actually sold:

| Line                                          | Amount          |
| --------------------------------------------- | --------------- |
| Additional price per unit (vs our €4.45-5.00) | €2.1335         |
| Additional retail revenue                     | €29,121,867     |
| Less additional R&D at 4.5%                   | −€1,310,484     |
| **Additional net income**                     | **€27,811,383** |

Demand would have fallen — but it would have had to fall by **more than 57.3%** before it stopped
exceeding our production capacity. ⚠️ This is the single largest number in this document and the
first thing to fix in the graded run.

[~] The honest caveat: the graded round is a fresh simulation and rival prices will differ. What
carries over is the *structure* — a mature market where our capacity is a fraction of the demand our
brand can generate, so **capacity, not price, is what limits revenue.** Price to the market, then
build lines to serve it.

### 4.4 The channel mix we assumed was wrong

| Channel | Share of S sold | Share of H sold |
| ------- | --------------- | --------------- |
| AG      | 7.4%            | 7.3%            |
| AS      | 28.0%           | 25.0%           |
| AT      | 12.6%           | 11.5%           |
| BG      | 3.7%            | 5.3%            |
| BS      | **36.2%**       | **37.9%**       |
| BT      | 12.0%           | 13.1%           |

We assumed sunscreen would lean to pharmacies as a premium product. It did not. **Supermarkets are
64% of both products**, and market B's supermarkets alone are over a third. Hypermarkets are 11%
despite carrying no sales commission.

📌 Market B outsold market A on both products — S +8.1%, H +28.8% — despite being the *smaller*
market on paper (S 9.0M vs 12.1M units; H 27.0M vs 29.26M). Higher per-capita income (€35,000 vs
€27,000) appears to dominate raw population.

---

## 5 · Logistics: the leg we planned and the leg we guessed

### 5.1 Factory → platforms: the capacity rule is confirmed ✅

| Market | Fleet planned        | Capacity = 500 x kg | Units shipped | Predicted   | Actual      |
| ------ | -------------------- | ------------------- | ------------- | ----------- | ----------- |
| A      | 1 vehicle, 17,000 kg | 8,500,000           | 6,340,088     | no stockout | no stockout |
| B      | 1 vehicle, 15,000 kg | 7,500,000           | 8,089,912     | STOCKOUT    | STOCKOUT    |

📌 **Annual capacity per vehicle = 500 x load capacity in kg** (250 routes of 8 h x 2 units per kg).
The rule predicted both outcomes correctly. Size this leg with 25-30% headroom and it is solved.

[!] We sized market A larger than market B. B sold 28% more. **Size the fleet to the market's income,
not its population** — see §4.4.

[~] The *cost* of this leg is not yet understood. The §10 formula applied to our own fleet gives
€86,400; the simulator charged **€48,155** (€0.00334/unit, well *under* the €0.006 guideline, and
that despite an emergency in B). Until this is explained, treat factory→platform capacity as cheap
and buy headroom generously.

### 5.2 Platform → retailers: this is a €1.3M fixed cost, not a €72,000 one

We planned one 10,000 kg vehicle per market and were charged **€2,506,409**.

Why one vehicle could never have worked — the leg is governed by **drops, not tonnage**:

| Market | Retailers | Weekly orders/yr (§12) | Spacing (§4 map) | Hours per drop | Vehicle-hours | Vehicles needed |
| ------ | --------- | ---------------------- | ---------------- | -------------- | ------------- | --------------- |
| A      | 3,815     | 198,380                | 5.12 km          | 0.288 h        | 57,132        | **28.6**        |
| B      | 2,190     | 113,880                | 6.59 km          | 0.325 h        | 36,972        | **18.5**        |

A planned fleet of ~31 + ~20 vehicles at 1,500 kg would cost **€1,315,800**. We were charged
€2,506,409 — **1.90x**, which is exactly the shape of the "higher cost than those previously rented"
premium §12 warns about. ✅ Two independent routes to the same number is the strongest evidence in
this document that the drop-density model is the right one.

[!] **The template default was 30 vehicles x 1,500 kg per market — approximately the correct answer.**
Our Year-1 pack called the template defaults "the most expensive trap in the pack" and overrode them.
On this leg, the override cost €1.19M. The template was right and we were wrong.

⚖️ The €0.007/unit guideline in §12 is unreachable at our Year-1 volume: €1.3M over 14.4M units is
€0.091. It only approaches €0.007 at 10x the volume, because the cost is driven by the retailer count
and barely at all by units. **This makes the last mile a scale argument for filling the factory.**

### 5.3 Own sales network vs wholesalers — right answer, wrong arithmetic

| Option                                                                             | Cost on Year-1 actuals |
| ---------------------------------------------------------------------------------- | ---------------------- |
| Own network: managers + reps + commission + platforms + last mile properly planned | €4,377,791             |
| Wholesalers at 8.46% of retail sales                                               | €6,184,988             |
| **Advantage of owning**                                                            | **€1,807,197**         |

Our Year-1 pack claimed €2,517,165 because it costed the last mile at €6,000 per zone instead of
~€110,000. ✅ The conclusion survives — and it *strengthens* as prices rise, because the wholesaler
takes a percentage of retail while our network is almost entirely fixed. At €150M of revenue,
wholesalers would cost €12.7M against roughly €6M for our own network.

---

## 6 · Advertising: buy the net rating, then stop

The Round-2 briefing (`3 2026 MIM DD C2 EN MMT39.pdf`, slide "Net rating") states the target
explicitly: **"1.00 (100%) is a must. It means you're reaching all potential buyers."**

Net rating achieved in Year 1, computed as 1 − Π(1 − scope)^insertions:

| Product | Market | Insertions  | Spend    | Net rating |
| ------- | ------ | ----------- | -------- | ---------- |
| S       | A      | 3 TV + 2 PR | €84,000  | 98.27%     |
| S       | B      | 2 TV + 1 PR | €51,000  | 91.68%     |
| H       | A      | 8 TV + 6 PR | €234,000 | 100.00%    |
| H       | B      | 4 TV + 3 PR | €117,000 | 99.64%     |

📌 **Market B ran half of A's insertions, half of A's sales reps and higher prices, in a smaller
market — and generated more demand than A** (S +8.1%, H +28.8%). For H the two markets were 100.00%
and 99.64% reached: the extra €117,000 spent in A bought 0.36 points of reach and no measurable
demand.

⚠️ **CORRECTED 6 September, after the Year-2 readings arrived.** The conclusion above holds only
at the *top* of the curve. In test Year 2, market B's sunscreen media was cut to three insertions
while market A ran twelve, and **B's share collapsed from 48.6% to roughly 2%**. So the response is a
saturation curve: flat above roughly seven insertions, cliff-edged below four. Reaching ~99% net
rating is necessary but the floor is nearer 7-8 insertions than 5. **Never starve a market, and keep
A and B identical** — see §14.

⚖️ Cheapest route to ≥99%: television is the most efficient medium in every market
(€18,000 per insertion for 60% scope). **5 TV insertions ≈ 98.98% for €90,000; 6 TV ≈ 99.59% for
€108,000.** Roughly €90-110k per product per market is the whole requirement.

[~] Caveat before cutting to the bone: the same briefing lists *"comparative active advertising (over
the years)"* as a share-of-demand driver, so relative spend may matter beyond reach. **Rule for the
graded run: ≥99% net rating in every product-market as a hard floor; spend above that only if survey
10 or 11 shows a rival materially outspending us.** Social media stays at zero — dearest per point of
reach in both territories.

---

## 7 · Market E: what actually happened, and what it is worth

We did not fail in E. **We never entered it.** Prices and margins were set; shelf space and campaign
were left at zero; §21 and §17 did the rest.

| Company | S price in E | H price in E | Campaign in E |
| ------- | ------------ | ------------ | ------------- |
| 1       | €10.00       | €8.50        | 15            |
| 2       | €10.50       | €9.50        | none          |
| 3 (us)  | €11.99       | €6.49        | **none**      |
| 4       | —            | —            | none          |
| 5       | —            | —            | none          |

⚖️ E is the largest single prize on the board — 35.1M units of S and 75.0M of H, at $46,000 per capita
income — and only one team advertised there in the test round, and it finished last. But entering E
costs a full commercial set-up (12 managers at $60,000, an export chain at €0.024/unit plus 2%
customs, its own logistics and its own advertising) and it competes for the same factory output as A
and B, where we already cannot serve half the demand.

**Position for the graded run: E is a Year-2 or Year-3 decision, taken only alongside the capacity to
serve it.** Entering E with no spare capacity moves units between markets and pays for the privilege.
If it is entered, all six fields must be filled: price, retailer margin, **shelf space**, campaign,
insertions, and POP.

---

## 8 · The competitors, from the free surveys

| Company | S price band | H price band | Campaign S / H | Promotions run                     | Net income      |
| ------- | ------------ | ------------ | -------------- | ---------------------------------- | --------------- |
| 1       | 8.00-9.00    | 6.50-7.50    | 15 / 13        | price reduction in G and S         | −€6,663,707     |
| 2       | 9.50-11.50   | 8.50-10.50   | none / none    | price reduction everywhere         | **+€7,366,632** |
| 3 (us)  | 10.40-11.70  | 4.45-5.00    | 18 / 19        | none                               | +€4,919,135     |
| 4       | 7.20-7.90    | 6.50-7.20    | none / none    | 3x2, discount-next-purchase, gifts | +€2,609,602     |
| 5       | none         | none         | none / none    | none                               | −€3,157,092     |

📌 Company 5 set no prices at all and lost €3,157,092. **That is the annual fixed-cost floor of doing
nothing** — a useful denominator for any "is this decision worth it" argument in a CEO meeting.

📌 The winner ran the **highest prices** and **no advertising campaign at all**. Two of five teams ran
no campaign; three ran promotions. Nobody else chose a positioning.

⚠️ Reading survey 22 correctly: its legend is offset by one from the scenario's own list. Survey code
1 = *no promotion*, 2 = price reduction, 3 = 3x2, 4 = drawing, 5 = discount on next purchase, 6 =
direct promotional bonus. On the **decision sheet** the numbering is the scenario's: type 5 = direct
promotional bonus (€1.20 per gift, detail = units required to qualify).

### 8.1 The eight experiments the master plan designed — what we actually ran

| # | Experiment (MASTER-PLAN Part 8)           | Ran? | What it returned                                    |
| - | ----------------------------------------- | ---- | --------------------------------------------------- |
| 1 | Different prices in A and B                | part | B priced ~3% above A; B outsold A anyway             |
| 2 | Sharply different advertising, A vs B      | YES  | [+] B at half the spend outsold A — no measurable return above ~99% net rating |
| 3 | Deliberately stock out in one market       | no   | [!] we stocked out everywhere by accident; the brand cost is still unmeasured |
| 4 | One zone own-managed, one via wholesalers  | no   | [~] still theoretical; the own-network case is €1.81M, not €2.52M |
| 5 | 2 shifts in Y1, 3 shifts in Y2             | no   | superseded — 3.10 settles it arithmetically          |
| 6 | One promotion type per channel             | no   | [!] we ran zero promotions; three of four rivals ran some |
| 7 | Buy the €11,000 survey bundle both years   | YES  | delivered the competitor table in section 8          |
| 8 | Compare actual output against capacity()   | YES  | [+] the most valuable result in the round: 81.25%    |

📌 Four of eight were run. The two run properly — 2 and 8 — produced the findings that move the most
money. **Experiments 3, 4 and 6 are still open and now have to be run inside a graded year, which
makes them expensive.** Design them with bounded downside: one channel, one market, never a whole
product line.


---

## 9 · Corrections to our own model and documents

| Where                                     | What it says                                    | What is now known                                                                       | Impact                           |
| ----------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------- |
| `model/mmt39.py` utilisation              | 78.75% headline / 80.675% with PM               | **81.25% exactly**                                                                      | [!] every capacity and RM figure |
| `model/mmt39.py` scrap model              | derived from breakdown hours (~0.65%)           | **flat 2.00% of production**                                                            | [!] RM order size                |
| `model/mmt39.py` standard cost            | no power multiplier                             | **power x 1.70**, repairs at the full 2.5 h                                             | [!] understated SC by 5-7%       |
| Y1 pack §2 "template defaults are a trap" | 30 platforms / 30 last-mile vehicles is ruinous | **the last-mile default was roughly right**                                             | [!] cost €1.19M                  |
| Y1 pack §2 last mile                      | one 10,000 kg vehicle, €36,000/market           | **~30 (A) and ~20 (B) vehicles, ~€1.3M total**                                          | [!]                              |
| Y1 pack §1 own-vs-wholesaler              | owning wins by €2,517,165                       | owning wins by **€1,807,197**                                                           | [+] conclusion holds             |
| Y1 pack §8 finance                        | deposit €15,000,000 at 2.5%                     | **cancelled, €0 earned, €150,000 penalty**                                              | [!]                              |
| Y1 pack §5 pricing                        | prices set 18-30% above break-even              | **underpriced H by ~45% against the market**                                            | [!] the largest number here      |
| Y1 pack §5 "13% of a price rise is lost"  | wholesaler 8.46% + R&D 4.5%                     | with an own network, **only 4.5%** is lost                                              | [+]                              |
| Y1 pack §9 channel split                  | S leans to pharmacies                           | **supermarkets are 64% of both products**                                               | [!]                              |
| Y2 plan (never run) finance               | €104,000,000 loan is mandatory                  | premised on the RM error; **do not reuse**                                              | [!]                              |
| Y2 plan (never run) logistics             | 10 last-mile vehicles per market                | closer, still likely short of ~30 / ~20                                                 | [~]                              |
| MASTER-PLAN Part 0 point 3                | "plan on 184,800 S / 462,000 H per line-shift"  | 195,000 S / 487,500 H at 81.25%                                                         | [!]                              |
| MASTER-PLAN Part 4                        | 2 shifts, not 3, in Year 1                      | 3 shifts dominates — see 3.10                                                           | [!] €18.3M of capex              |
| MASTER-PLAN Part 6 free win 1             | deposit the idle cash at 2.5%                   | the deposit is cancelled at a 1% penalty the moment cash dips                           | [~]                              |
| MASTER-PLAN Part 6 free win 2             | factor, do not borrow                           | factor only when cash is short — see 3.12                                               | [~]                              |
| MASTER-PLAN Part 2 R&D note               | ~13% of a price rise never reaches you          | 4.5% with an own network; 13% only via wholesalers                                      | [+]                              |
| MASTER-PLAN Part 5 trap 5                 | the EUR 0.006 logistics benchmark is a decoy    | true on the factory leg; the last-mile EUR 0.007 guideline is unreachable at our volume | [~]                              |
| MASTER-PLAN Part 7                        | Year 1 = "commit and learn", plan at 78.75%     | Year 1 = commit hard; the learning is already done                                      | [!]                              |
| `model/mmt39.py` depreciation             | applied to total fixed assets                   | production lines only — land is not depreciated                                         | [!]                              |

⚠️ `model/mmt39.py` has **not** been changed yet — the four corrections in the first three rows are
still outstanding and should be applied and re-self-tested before any Year-1 figure is quoted to the
CEO.

---

## 10 · What this implies for Year 1 of the graded round

Order of operations, most valuable first.

| # | Decision                | Position                                                                                     | Evidence |
| - | ----------------------- | -------------------------------------------------------------------------------------------- | -------- |
| 1 | **Price**               | Price H into the rivals' band, not below it. Break-even is not the reference point; the market is. | §4.2-4.3 |
| 2 | **Capacity**            | Buy lines aggressively in Year 1 — they are irreversible, they pay back inside a year, and demand is ~3x anything we can build. Weight toward H (€1.03 vs €3.59 of capex per unit of sellable capacity at 3 shifts) but do not starve S: we served 9.3% of its demand. | §4.1, §3.1 |
| 3 | **Last mile**           | ~30 vehicles in A and ~20 in B, load sized to units-per-drop with headroom. Budget €1.3-1.8M and treat it as a fixed cost of owning the network. | §5.2 |
| 4 | **Raw material**        | Production x 1.02, entered twice by two people, read back aloud. One field. | §3.2, §2.1 |
| 5 | **Factory→platform**    | Capacity = 500 x kg per vehicle, +25-30% headroom, sized per market on *income*-weighted demand. | §5.1 |
| 6 | **Finance**             | No fixed-term deposit unless cash is unambiguously surplus after the OCR test. Run the §41 OCR test before submitting. Factoring on. | §3.6 |
| 7 | **Advertising**         | ≥99% net rating per product-market (≈5-6 TV insertions), then stop. Zero social media. | §6 |
| 8 | **Shelf space + margin** | Every channel we price must also carry a margin **and** a shelf-space percentage, or it sells nothing. | §7, §2.3 |
| 9 | **Market E**            | Not in Year 1. Revisit in Year 2 with capacity to serve it. | §7 |
| 10 | **Preventive maintenance** | On. Poka Yoke off. SMED not available until Year 2. | §3.1 |

⚖️ On capacity in Year 1 specifically: 32 lines is the lifetime ceiling and lines cannot be removed,
but they can be installed in any year and are assumed to run at full capacity in the year they are
installed. The binding constraint in Year 1 is **cash** — capex is paid in cash (§37) and the §41 OCR
test must clear €54,000,000. Work the exact line count against the OCR test on the day, once the
Director's Year-1 factor values are on screen.

---

## 11 · Before entering anything on Day 2

| # | Check                                                                                 |
| - | ------------------------------------------------------------------------------------- |
| 1 | Open **Information** and copy the Director's actual values. Per-capita income, raw material costs, power costs, FX, unemployment, and every interest rate can differ from the test round. Nothing in this file survives a changed factor unexamined. |
| 2 | Confirm the number of sales zones, outlets and channels is unchanged from the test scenario. |
| 3 | Re-enter **every** field: managers, logistics, all salaries, factoring, supplier terms, lines to activate. Everything resets. |
| 4 | Apply the four `model/mmt39.py` corrections in §9 and re-run `--selftest` before quoting a figure. |
| 5 | Decide the price *before* the capacity plan, then size the plant to the demand that price implies — not the other way round. |
| 6 | Whoever enters raw materials is not the person who checks it.                          |

---

## 12 · Open questions the graded Year 1 should answer

| Question                                                                      | How Year 1 answers it                                                                                               |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Why is the factory→platform charge 56% of the §10 formula?                    | Plan a known fleet, read the reported cost, divide.                                                                 |
| Is the last mile drop-driven (~30 vehicles) or tonnage-driven (~2)?           | Plan ~30/~20, read the cost per unit and the stockout flags. Cost near €1.3M with no stockout confirms drop-driven. |
| Is the 1.70x power multiplier real, or a proxy for something else?            | Re-fit the §3.3 formula against the new standard cost.                                                              |
| Does preventive maintenance cut the repair bill as well as raise utilisation? | Compare the fitted repair term against 2.5 h and 1.8 h.                                                             |
| What does shelf space actually achieve versus what we ask for?                | Buy survey 15 (€72,000) in Year 1 — we have never seen this number.                                                 |
| How much demand are we still failing to serve?                                | Buy survey 19 (€110,000). It sizes the Year-2 capex directly.                                                       |

**Already answered by the Year-1 results — do not spend a Director question on these:**

| MASTER-PLAN Part 12 question                            | Answer from the Year-1 reports                                                                |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Section 42: what proportion of a loan repays each year? | **One quarter.** EUR 956,512 due on a EUR 3,826,050 loan at a 4-year maturity.                |
| Which reading of section 24 does the simulator use?     | Neither exactly — it lands on a flat **81.25%**, and raw material on a flat **2%**.           |
| Does preventive maintenance pay?                        | Yes: 81.25% observed against 78.75% without it — +2.5 points of nameplate for EUR 500,000.    |
| Section 11 storage "per unit" or "per litre"?           | Still open, but bounded: total warehouse cost was EUR 279,306 on 14.43M units at 6 platforms. |

---

## 13 · What the CEO is graded on (from the 2026 evaluation guidelines)

| Component                                                         | Weight |
| ----------------------------------------------------------------- | ------ |
| Individual work and presentations                                 | 40%    |
| Teamwork                                                          | 25%    |
| Peer feedback                                                     | 15%    |
| Final report                                                      | 10%    |
| **Company results** (accumulated profit and net income evolution) | 10%    |

Every CEO meeting is two parts: **previous year — analysis of results establishing the causes**, then
**following year — plan with specific, measurable objectives, decisions and forecasts.** The first
meeting also opens with an introduction: market size by product and market, the company's strategy,
and goals for brand perception and market share.

📌 The guidelines name, as required content, several things this document now supplies with hard
numbers: *"actual production cost vs forecast, industry average or previous years"*, *"transport cost
deviations vs the reference given"*, *"raw material inventory, stockouts and cost analysis"*,
*"effectiveness of productivity policies"*, and *"the inventory effect on the financial situation"*.
The test round's failures are, conveniently, exactly the material the rubric asks us to analyse.

⚠️ Missing one CEO meeting is a zero for that meeting; missing two fails the course. **Final report
due Friday 18 September 2026, 23:00.**

---

## 14 · A second plan document that cites evidence this repo does not hold

`day 2 - real thing/06-graded-year1-plan-2.1.md` (44 KB) builds a Year-1 plan on **test-round Year-2
results**. Those results would be more valuable than anything in this file — a second price point is
what turns a single observation into a demand curve. But none of the sources it names exist here:
`day 2/year 2 results/…Y2REP.md`, `…Y2DEP.md`, `…Y2INFen_US.md`, `docs/04-…`, `docs/05-…`, and
`Scenario MMT39 EN v231.pdf`. This repo has no `day 2` folder, `docs/` holds only 00-03, and the
scenario file is `Scenario MMT39 .pdf`.

[!] One of its **Year-1** figures is checkable and wrong: it quotes sunscreen demand of 9,199,028;
page 2 of the Year-1 results reports **8,419,028**.

✅ **RESOLVED 6 September.** A second file, `MMT39 - Graded Year 1 Plan 2.1 (8S-24H).pdf`, carries the
same Year-2 readings, and they were tested against four rules verified independently from the Year-1
result sheets: the 500 x load-kg trunk capacity rule predicts all four stockout flags across both test
years; the Year-2 depreciation of €7,056,000 matches 12% of lines and SMED with land excluded; the
€52,800,000 of lines reconstructs exactly to 8 S + 24 H; and the unit accounting closes at the 92.9%
SMED utilisation. **The readings are treated as sound and the final plan is built on them.** The
source files are still worth having. If they exist, the price readings alone (S at 14.50, H at 5.25 in A against 7.75
in B) would let us fit a real elasticity instead of reasoning from rival prices. Section 17 of
`YEAR 1 - OPTIMAL STRATEGY.txt` compares the two plans decision by decision.

---

## Sources

- `day 1/year 1/DIR0114SI02082TE3Y1DEP.pdf` — decisions as submitted, Year 1 (test)
- `day 1/year 1/DIR0114SI02082TE3Y1REP.pdf` — results, Year 1 (test)
- `day 1/year 1/DIR0114SI02082TE3Y1INV.pdf` — surveys 20, 21, 22, 23, 24
- `day 1/year 1/DIR0114SI02082TE3Y1INFen_US.pdf` — Director's factor values, Year 1
- `day 1/year 2/Screenshot 2026-09-05 at 1.49-1.52 PM.png` — Year-2 decision screens at reset
- `Scenario MMT39 .pdf` — §4, §9, §10, §11, §12, §17, §18, §21, §22, §23, §24, §25, §28, §30, §33, §36, §37, §40, §41, §42, §43, §48, §49
- `3 2026 MIM DD C2 EN MMT39.pdf` — Round 2 briefing: net rating, demand drivers, logistics method
- `4 2026 MIM evaluation guidelines.pdf` — grading weights, CEO meeting structure, report deadline
- `day 1/DECISIONS-EXPLAINED_year1.txt`, `day 1/DECISIONS-EXPLAINED_year2.txt` — our own plans
- Verification: all quantitative claims recomputed from the reported actuals; the standard-cost
  formula in §3.3 reproduces the simulator's figure for both products to within 0.03%.
