# Doc 03 — Decision Checklist & Grading Playbook

**Two things you run before every submission.** Part A: every field the simulator accepts.
Part B: the deck the rubric actually rewards. Markers: `[!]` trap · `[+]` edge.

---

# PART A — THE DECISION CHECKLIST

## A0. The five silent killers

Read these before anything else. Each produces **zero sales with no warning message**.

| If you leave this blank         | The simulator assumes                   | §   |
| ------------------------------- | --------------------------------------- | --- |
| **Price** for a product/channel | You are not selling there               | §14 |
| **Retailer margin**             | You do not want that channel — no sales | §20 |
| **Shelf space**                 | You do not want that channel — no sales | §21 |
| **Line activation**             | You do not want to produce — no output  | §22 |
| **Advertising campaign**        | Neutral, undefined brand positioning    | §17 |

`[!]` **Zero is not a legal entry in any logistics field** (§12). A blank or a zero breaks the plan.

---

## A1. Marketing

| Decision               | Range / options                            | Per                        | §        |
| ---------------------- | ------------------------------------------ | -------------------------- | -------- |
| Retail price (MSRP)    | Any, 2 decimals                            | Product × market × channel | §14      |
| Retailer margin        | In **euros per unit**, not a percentage    | Product × market × channel | §20      |
| Shelf space objective  | % — negotiated down by the simulator       | Product × market × channel | §21      |
| Advertising campaign   | 1 of 20 (S) or 1 of 20 (H)                 | Product × market           | §17, §51 |
| Advertising insertions | Count, per medium: DR / PR / RA / SM / TV  | Market                     | §15      |
| POP advertising budget | Euros, separate for S and H                | Product                    | §19      |
| Promotion type         | 1 type only per channel per year           | Product × market × channel | §18      |
| Number of promotions   | Max **3** per channel per product per year | Product × market × channel | §18      |

**Reminders that cost money if forgotten:**

- `[+]` Positioning can change **every year at zero cost** (§17). Cheap experiment, not a commitment.
- `[!]` Shelf space is an *objective*. Over-asking makes the retailer "react negatively" (§21).
- `[!]` Promotions last **3 of 52 weeks** (§18), and if you cannot supply the demand they create, the
  market **rejects the promotion entirely** (§48).
- `[!]` A 3×2 promotion is a **33% discount**. Cheapest is a direct gift at ~6.7% of price.
- Prices in market E are entered **in euros**; the simulator applies the FX rate (§2, §46).

---

## A2. Operations

| Decision                | Range                                                  | §        |
| ----------------------- | ------------------------------------------------------ | -------- |
| New S lines to install  | Any, total ≤ **32** lines. **IRREVERSIBLE**            | §22      |
| New H lines to install  | Any, total ≤ **32** lines. **IRREVERSIBLE**            | §22      |
| Lines to activate       | ≤ lines installed                                      | §22      |
| Production shifts       | 1, 2 or 3 — applies to **all** lines equally           | §23      |
| Preventive maintenance  | Yes / no — decided **annually**, €500,000              | §25      |
| Poka Yoke               | Once only, ever. €720,000 **per line**. IRREVERSIBLE   | §26      |
| SMED modules to buy     | **Year 2 onwards only**. €3,000,000 each. IRREVERSIBLE | §27      |
| SMED modules to operate | ≤ modules owned                                        | §27      |
| SMED teams per shift    | Teams of 4 specialists, paid as production specialists | §27, §30 |
| Raw material units, S   | Cover production **+ scrap**                           | §28, §34 |
| Raw material units, H   | Cover production **+ scrap**                           | §28, §34 |
| RM payment terms, S     | 0 / 60 / 90 / 120 days                                 | §28      |
| RM payment terms, H     | 0 / 60 / 90 / 120 days                                 | §28      |

**Reminders:**

- `[!]` **Plan production at 78.75% of nameplate** — 184,800 per S line-shift, 462,000 per H
  line-shift (§23, §24).
- `[!]` Under-ordering raw material costs **+15%** on the shortfall (§28).
- `[!]` Order for units **used**, not units produced — scrap consumes raw material (§34).
- `[!]` New lines run at full capacity in their first year (§22), but SMED cannot be bought in year 1.
- Depreciation rises with shifts: 8% / 10% / 12% (§35).

---

## A3. Logistics

| Decision                           | Range                                     | §        |
| ---------------------------------- | ----------------------------------------- | -------- |
| Platforms in A / B                 | 6, 12, 18, 24, 30 or 36                   | §10      |
| Platforms in E                     | 12, 24, 36, 48, 60 or 72                  | §10      |
| Sales managers in A / B            | 0 to 6 (one per zone)                     | §10      |
| Sales managers in E                | 0 to 12                                   | §10      |
| Vehicles, factory → platform       | Count, per market. **Never zero**         | §10, §12 |
| Load capacity, factory → platform  | 1,000 – 24,000 kg                         | §10      |
| Vehicles, platform → retailer      | Count, per market. Own-managed zones only | §12      |
| Load capacity, platform → retailer | 500 – 10,000 kg                           | §12      |

**Reminders:**

- `[+]` **Minimise vehicle count, then size each to fit exactly.** Fleet cost is
  `24,000 × vehicles + 0.0024 × units`. Use `optimal_vehicle_plan()`.
- `[!]` The §10 benchmark of €0.006/unit **costs 36% more** than the achievable €0.0044.
- `[!]` You pay factory→platform transport in **every** zone, wholesaler zones included (§8).
- Last-mile vehicles are needed **only** in zones you manage yourself (§12).
- Every zone must be covered — by your manager or a wholesaler (§8).

---

## A4. Human resources

| Decision                 | Range                                 | §       |
| ------------------------ | ------------------------------------- | ------- |
| Level I salary           | €108,000 – €150,000 (1 person)        | §29     |
| Level II salary          | €72,124 – €99,170 (8 people)          | §29     |
| Level III salary         | €51,100 – €72,124 (15 people)         | §29     |
| Level IV salary          | €30,050 – €42,075 (32 people)         | §29     |
| Specialist salary        | €21,000 – €29,450                     | §30     |
| Operator salary          | €12,000 – €16,830                     | §30     |
| Sales reps per zone      | Your choice — A and B only            | §6, §13 |
| Rep fixed salary         | €21,000 – €42,000 per year            | §13     |
| Rep variable salary      | 0%, or 0.6% – 1.2% (optional)         | §13     |
| Training department (TS) | Yes / no — €722,000, decided annually | §32     |

**Reminders:**

- `[!]` Minimum wages are **not free**: low pay drives office turnover and production absenteeism
  (§31). Turnover also depends on the 7% unemployment rate in A+B (§49).
- Rep commission is on the **price to the retailer**, not retail price, and only on **normal** units.
  Wholesaler sales pay no commission (§13).
- Reps exist only for channels S and T — so **market E needs no reps**, only managers (§6).
- Headcount recorded is **per zone**, multiplied by the number of zones you staff (§6).

---

## A5. Finance

| Decision                | Range / options                           | §        |
| ----------------------- | ----------------------------------------- | -------- |
| Customer payment terms  | 60 / 90 / 120 days — same for all markets | §38      |
| Factoring               | Yes / no, with an optional limit          | §39      |
| Loan request            | Any amount; 10%, 4-year maturity, 1% fee  | §42, §49 |
| Loan prepayment         | Requires cash surplus; 1% penalty         | §42, §49 |
| Credit line             | 7% + 1% service + 1% upfront; 1 year      | §43      |
| Fixed-term deposit      | 2.5%; 1% early-withdrawal penalty         | §44      |
| Financial investment    | 2.5%; 1% early-withdrawal penalty         | §44      |
| Share purchases         | 3 listed securities; specify cash amount  | §45      |
| Market research surveys | Pick from the 28-item menu                | §50      |

**Reminders:**

- `[+]` Factor rather than borrow: 5.5% vs 10% (§39, §49).
- `[+]` Deposit surplus cash — €54M idle earns **€1,350,000** a year (§44).
- `[!]` Never overdraft at 20% (§42).
- `[!]` A loan drawn this year is **not repaid this year** — it leaves your cash on 2 January (§47).
- `[!]` To buy more of a security you already hold, you must **sell it all first** (§45).

### The OCN check — run this before every submission (§41)

> **OCN = 80% × new capex + 50% × (advertising + POP + sales managers + rep fixed salaries +
> overhead + market research) + 15% × raw material cost**

Compare against cash available on 2 January:

> cash on 31 Dec − loan repayments due − credit lines due − payables
> **+** investments **+** deposits **+** receivables

`[!]` **If OCN exceeds available cash, the simulator takes a loan for you at 10%** (§41). Use
`ocn()` and `financing_gap()` in the model.

---

## A6. Pre-submission checklist

Run this every single time. Assign it to one named person.

- [ ] Every product/market/channel you intend to sell in has a **price**, a **retailer margin** and a
      **shelf-space** figure
- [ ] Every advertising campaign selected (or you accept neutral positioning)
- [ ] Lines **activated**, not just installed
- [ ] Production forecast ≤ capacity at **78.75%** — run `capacity_reality_check()`
- [ ] Raw material covers production **plus scrap**
- [ ] No logistics field is blank or zero
- [ ] Every sales zone covered by a manager or a wholesaler
- [ ] Promotion volumes are within what you can actually supply
- [ ] **OCN ≤ available cash** — or you have deliberately requested the loan
- [ ] Surplus cash is on deposit, not sitting idle
- [ ] Surveys 20, 21, 22 (free) plus the €11,000 bundle ordered
- [ ] SMED not requested in year 1; Poka Yoke not requested twice

---

# PART B — THE GRADING PLAYBOOK

## B1. Where the marks actually are

| Component                       | Weight  | What moves it                                      |
| ------------------------------- | ------- | -------------------------------------------------- |
| Individual work & presentations | **40%** | Your own department, defended in front of the CEO  |
| Teamwork                        | **25%** | Coordination, roles, response to market and rivals |
| Peer feedback                   | **15%** | How your teammates rate your contribution          |
| Final report                    | **10%** | Statements, ratios, SWOT, forecasts                |
| Company results                 | **10%** | Accumulated profit and net income evolution        |

**Only 10% is the simulated result.** 65% is analysis quality, presentation and peer assessment.
Winning the market is neither sufficient nor the main lever.

`[!]` **Missing one CEO meeting = zero for that meeting. Missing two = automatic fail.**

---

## B2. The two rules that silently cost marks

**1. Analysis must establish CAUSES, not describe outcomes.**
The guidelines state it in capitals: *"IT IS A MUST TO ESTABLISH THE CAUSES FOR THE COMPANY'S
RESULTS."*

| Scores badly                | Scores well                                                                                                     |
| --------------------------- | --------------------------------------------------------------------------------------------------------------- |
| "Market share fell to 12%." | "Share fell 4 pts because our GRPs dropped 30% while Company B raised theirs 50% — survey 11 confirms."         |
| "Production cost rose."     | "Unit cost rose €0.18 because scrap consumed raw material we had not ordered, triggering the §28 +15% penalty." |

**2. Each member's role must be clearly identified in the deck handed in.**
Stated explicitly in the evaluation guidelines. Put the owner's name on every section slide.

---

## B3. The CEO deck skeleton

Same structure for all three meetings. Section 1 appears in meeting 1 only.

| # | Section | Content | Owner |
| - | ---------------------- | ------------------------------------------------------------ | ------- |
| 1 | Introduction *(1st only)* | Market size by product and market; what kind of company we are; brand-perception and share goals | Team |
| 2 | Summary of results | Revenue, operating income, net profit, margins, ROE; sales and share by product and market; revenue by product and market | Finance |
| 3 | Analysis of results | Marketing, operations, HR, finance — **with causes** | All four |
| 4 | Objectives | Sales and share by product/market; operating margin, net margin, ROE | Team |
| 5 | Actions | Decisions by department | All four |
| 6 | Financial forecast | Projected income statement | Finance |

**45 minutes maximum** — the CEO needs time to challenge you.

### Section 3 in detail — the 18 items the rubric lists

| #   | Item                                  | Show this                                      | Model call                   |
| --- | ------------------------------------- | ---------------------------------------------- | ---------------------------- |
| 4   | Product portfolio by market & channel | Table: units and revenue per cell              | —                            |
| 5   | Brand positioning                     | Positioning map, ours vs rivals                | Survey 7 / 8                 |
| 6   | Distribution                          | Managers vs wholesalers, POP, shelf space      | `distribution_compare()`     |
| 7   | Advertising                           | Budget, share of voice, share of spend, GRPs   | `advertising()`              |
| 8   | Prices and promotions                 | Ours vs rivals; promotion effectiveness        | Survey 20, 22                |
| 9   | Expected vs actual production         | Variance chart **with the cause**              | `capacity()`                 |
| 10  | Productivity policies                 | SMED / Poka Yoke / preventive effect           | `line_hours()`               |
| 11  | Actual vs forecast production cost    | Bridge chart, component by component           | `standard_cost()`            |
| 12  | Supply chain                          | Raw material inventory, stockouts, cost        | —                            |
| 13  | Transport cost vs the reference       | €/unit vs €0.006 and €0.007                    | `plan_factory_to_platform()` |
| 14  | HR turnover and salaries vs rivals    | Ours vs industry average                       | Survey 25                    |
| 15  | Salesforce optimisation               | Cost per unit sold, by zone                    | `distribution_compare()`     |
| 16  | Financial statements **incl. ratios** | Balance sheet, P&L, full ratio set             | `ratios()`                   |
| 17  | Cash management                       | Working capital; collection, payment, leverage | `ocn()`                      |
| 18  | Other — e.g. inventory effect         | Inventory value and its cash impact            | `Simulation`                 |

Items 1–3 are the summary figures in Section 2.

### Sections 4–6 — the 8 planning items

| # | Item | Owner |
| - | ------------------------------------------------------------------- | --------- |
| 1 | Sales and market share objectives, by product and market | Team |
| 2 | Operating margin, net margin, ROE targets | Finance |
| 3 | Any other objective the CEO asks for | Team |
| 4 | Marketing: positioning, portfolio, distribution, advertising, prices, promotions, shelf | Marketing |
| 5 | Operations: capex, production schedule, productivity systems, inventory, supply chain | Operations |
| 6 | HR: salaries and sales incentives | HR |
| 7 | Finance: OCN, loans, credit lines, receivables/payables, factoring | Finance |
| 8 | Projected income statement | Finance |

`[!]` Objectives must be **specific, measurable and coherent**, and must follow from your analysis.
"Grow market share" is not an objective. "Raise H share in market A from 8.4% to 11% by lifting GRPs
from 171 to 240" is.

---

## B4. The final report

Same shape as a presentation, plus multi-year history.

| Section            | Content                                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Summary of results | **Horizontal (year-on-year) analysis** of P&L, balance sheet and ratios, years 1–4; sales, revenue and share by product and market, years 1–4 |
| Analysis           | Every department's performance in **year 4**                                                                                                  |
| SWOT               | Strengths, weaknesses, opportunities, threats at the end of year 4                                                                            |
| Objectives         | For **year 5**                                                                                                                                |
| Action plan        | Year-5 decisions across marketing, operations, HR, finance                                                                                    |
| Forecast           | Projected year-5 income statement                                                                                                             |

`Simulation.summary()` produces the year-by-year table this needs.

---

## B5. Meeting-day routine

| When              | Do                                                                                        |
| ----------------- | ----------------------------------------------------------------------------------------- |
| Results released  | Buy surveys 20, 21, 22 + the €11,000 bundle. Update the rival table                       |
| Same day          | Each owner writes their causes — not their numbers, their **causes**                      |
| Before drafting   | Run `--demo`-style projection; confirm the forecast is achievable                         |
| Draft deck        | One owner per section; name on every slide                                                |
| Rehearse          | Time it to **45 minutes**. Everyone speaks for a similar length                           |
| Prepare defence   | List the three numbers the CEO is most likely to challenge, with the § reference for each |
| After the meeting | You may make slight plan changes — hand in the deck first                                 |

`[+]` Every figure in the model carries its § reference. When challenged, point at the rule.

---

*Sources: `Scenario MMT39 .pdf`, `capstone evaluaion guidelines.pdf`, `overview capstone.md`.
Facts: `docs/01`. Strategy: `docs/02`. Model: `docs/00`.*
