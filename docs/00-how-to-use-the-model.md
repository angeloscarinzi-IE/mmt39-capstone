# How to Use `mmt39.py`

**A plain-language guide to the MMT39 decision model**

Version 1.0 · Built from `Scenario MMT39 .pdf` · 89 self-tests passing

---

## 1. Introduction

### What this is

`model/mmt39.py` is a calculator built specifically for your Capstone simulation. You give it
decisions — how many production lines, how many shifts, what price, how much advertising — and it
tells you what will happen: how many units you can actually make, what each one costs, and what your
income statement and balance sheet will look like at the end of the year.

It is one file. It needs nothing installed. It runs on any Mac or PC with Python.

### Why it exists

The MMT39 scenario is 57 pages of rules. Buried in those rules are about sixty numbers that
determine whether you make money or lose it. Most teams will read those pages the way you read a
textbook — they will absorb the *ideas* and skip the *arithmetic*.

That is the opening. Every team gets the identical company: €12,000,000 of fixed assets,
€54,000,000 of cash, €66,000,000 of equity, no debt, no inventory, no products (§1). Nobody starts
with an advantage. The advantage is created entirely by who does the maths.

This model does the maths once, correctly, so you can spend your time on strategy instead of
spreadsheets.

### What it is not

It cannot predict how many units you will **sell**. The simulator's demand engine — how price,
advertising, brand positioning and shelf space combine into customer demand — is hidden, and the
scenario never reveals it. **Nothing in this model invents a demand curve.**

What it does instead is tell you exactly what you can *make*, what it *costs*, and what you *earn*
at any given sales volume. Then, once your first year of real results arrives, it contains a tool
that learns the demand relationship from your own data (see §4.7).

---

## 2. How to use it

### 2.1 Running it

Open Terminal, go to the project folder, and type one of these five commands.

```bash
cd "/Users/angelo/Desktop/Projects & Certificates & Work/Projects/CAPSTONE Project MIM"
```

| Command                                             | What it gives you                                              |
| --------------------------------------------------- | -------------------------------------------------------------- |
| `python3 model/mmt39.py --briefing`                 | Every headline number in one page. **Start here.**             |
| `python3 model/mmt39.py --lines`                    | Production line economics at 1, 2 and 3 shifts                 |
| `python3 model/mmt39.py --media`                    | Which advertising medium is cheapest, ranked                   |
| `python3 model/mmt39.py --promotions 6.00`          | What each promotion type costs at a €6.00 price                |
| `python3 model/mmt39.py --breakeven 2.13 0.95 0.60` | Lowest price you can charge without losing money               |
| `python3 model/mmt39.py --demo`                     | A full worked year: P&L, balance sheet, ratios, stockout check |
| `python3 model/mmt39.py --selftest`                 | Proves the model still matches the rulebook (89 checks)        |

Run `--selftest` after anyone edits the file. If a check fails, a number is wrong somewhere.

### 2.2 Using it for a real management plan

For actual planning you write a few lines of Python. Here is a complete example — copy it, change
the numbers, run it.

```python
import sys; sys.path.insert(0, "model")
from mmt39 import *

# 1. What can the factory physically produce?
cap = capacity(s_lines=2, h_lines=10, shifts=3, preventive=True)
print(cap.summary())

# 2. What does one unit cost to make?
sc_h = standard_cost("H", lines=10, shifts=3, preventive=True)
print(sc_h.summary())

# 3. What is the lowest price that still makes money?
print(breakeven_price(sc_h.total, retailer_margin=0.95,
                      units=13_000_000, allocated_fixed_costs=9_000_000))

# 4. Will your sales forecast actually fit in the factory?
print(capacity_reality_check({"H": 13_000_000, "S": 500_000}, cap))

# 5. What does the whole year look like?
sim = Simulation()
result = sim.run_year(YearPlan(
    year=1, s_lines_new=2, h_lines_new=10, shifts=3, preventive=True,
    sales=[SalesLine("H", "A", "G", units_normal=13_000_000,
                     retail_price=4.20, retailer_margin=0.95)],
    advertising_spend=3_000_000, sales_force_cost=1_500_000,
    logistics_cost=300_000, market_research_spend=100_000))
print(result.income.render())
print(result.balance.render())
print(render_ratios(result.ratios))
```

### 2.3 The one thing you must maintain

Every number the model uses lives in a single block called `SCENARIO` at the top of the file, each
with its rulebook section number beside it.

The simulation Director **changes some of these every year** — the euro/dollar exchange rate, the
raw material cost, the interest rates (§28, §46, §49). When that happens, edit that one block and
everything downstream updates automatically. Do not hunt through the code.

### 2.4 Where the model is honest about not knowing

Three places in the rulebook are genuinely ambiguous. The model does **not** hide this. Each is
marked `ASSUMPTION` in the code, implemented both ways where possible, and defaulted to the
conservative reading.

| Ambiguity                                                                                | What the model does                                                         | What you should do                                                           |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| §18 says "eight types of promotion" then lists six                                       | Models the six that are described                                           | Ask the Director in Session 2                                                |
| §42 says loans repay "a proportion" of the balance but never says what proportion        | Implements both readings; defaults to the one that actually clears the debt | Compare your first balance sheet against both, then set `LoanBook(rule=...)` |
| §24 says the module is serviced "every 40 line operating hours" — two readings, 3% apart | Defaults to the reading that gives *less* capacity                          | Leave as is; under-promising is the safe error                               |

**Why the conservative default matters:** if you forecast production you cannot deliver, §34 says a
stockout does not just cost you the sale — it "damages brand prestige and loyalty as well." That
damage carries into later years. Over-promising is the expensive mistake; under-promising is not.

---

## 3. The main factors the model extracts

Everything below is computed output, not opinion. Run `--briefing` to reproduce any of it.

### 3.1 The market is far bigger than any factory

| Product             | Market A   | Market B   | Market E   | **Total**       |
| ------------------- | ---------- | ---------- | ---------- | --------------- |
| **S** (sunscreen)   | 12,100,000 | 9,000,000  | 35,100,000 | **56,200,000**  |
| **H** (moisturiser) | 29,260,000 | 27,000,000 | 75,000,000 | **131,260,000** |

*Source: §2 population × §3 per-capita consumption.*

Now compare that to the largest factory the rules permit — all 32 lines making H, running three
shifts (§22, §23):

| Configuration                              | Annual sellable units | Share of H demand |
| ------------------------------------------ | --------------------- | ----------------- |
| 32 H lines, 3 shifts                       | 44,352,000            | **33.8%**         |
| Same, plus SMED and preventive maintenance | 53,668,800            | **40.9%**         |

**Conclusion: you physically cannot serve the whole market, even at maximum size.** Capacity is the
binding constraint, not demand. Every plan is therefore a choice about *which* demand to serve — and
teams that plan as though they could sell everywhere will stock out.

Note also that market E alone is **62% of S demand and 57% of H demand**. It is also the only market
with local competition, plus currency risk, 2% customs duty, twelve sales zones instead of six, and a
six-phase logistics chain instead of three (§2, §4, §9). E is where the volume is and where the
difficulty is. That tension is the central strategic question of the game.

### 3.2 Moisturiser is a fundamentally better business than sunscreen

|                                           | S line     | H line     | H advantage      |
| ----------------------------------------- | ---------- | ---------- | ---------------- |
| Cost to install (irreversible)            | €2,100,000 | €1,500,000 | 29% cheaper      |
| Sellable units/year at 3 shifts           | 554,400    | 1,386,000  | 2.5× more        |
| **Capital cost per unit of capacity**     | **€3.79**  | **€1.08**  | **3.5× better**  |
| **Standard cost per unit**                | **€5.13**  | **€2.13**  | **2.4× cheaper** |
| Break-even retail price (own salesforce)  | €7.99      | €3.86      | —                |
| Break-even retail price (via wholesalers) | €8.77      | €4.23      | —                |

*Source: §22, §23, §30, §33, §49. Standard cost includes raw material, power, line labour, scrap and
breakdown repair at minimum legal wages.*

An S line ties up 3.5× more capital per unit of output and costs 2.4× more to run. To make money on
sunscreen you need roughly **double the retail price** of moisturiser.

That may well be achievable — sunscreen is a higher-value product in the real world. But it is a
decision to make with open eyes, not by default. Sunscreen is the more exciting product to build a
marketing campaign around, which is exactly why some rivals will over-invest in it.

### 3.3 A fifth of your factory does not exist

This is the model's most important operational finding.

Per line, per shift, per year (§23, §24):

|                               | Hours     | Share      |
| ----------------------------- | --------- | ---------- |
| Scheduled                     | 2,000     | 100%       |
| Lost to breakdown repair      | −175      | −8.8%      |
| Lost to main-module servicing | −250      | −12.5%     |
| **Actually producing**        | **1,575** | **78.75%** |

The headline capacity figures in §23 — 240,000 units per S line per shift, 600,000 for H — are
**nameplate**, not achievable. Real output is 78.75% of that.

A team that plans production off the headline number will over-commit by about a fifth, stock out,
and take the §34 brand-loyalty damage. This is the single easiest error to avoid and, on the numbers,
the easiest to make.

### 3.4 Television is the cheapest advertising in both markets

Cost per 1% of buyers reached, per insertion (§15 rates ÷ §16 scope):

| Medium                | Markets A & B | Market E   |
| --------------------- | ------------- | ---------- |
| **Television**        | **€300.0**    | **$327.9** |
| Press                 | €312.5        | $516.1     |
| Display / remarketing | €357.1        | $423.1     |
| Radio                 | €400.0        | $400.0     |
| Social media          | €500.0        | $517.2     |

Television is cheapest in both markets. Social media is the most expensive in A/B (+67% versus TV)
and the most expensive in E (+58%).

This matters because "digital-first, social-led" is the instinctive modern answer, and it is the
wrong one here on the scenario's own numbers. Television's €18,000 rate looks expensive next to
display's €10,000 — but TV reaches 60% of buyers per insertion against display's 28%. You are buying
reach, not insertions.

**A useful benchmark the model computes:** one TV insertion in market A reaches 60% of buyers for
€18,000. Reaching 90% costs €57,000 and requires four media (TV + press + display + radio), because
media overlap and each extra medium adds less new audience than the last.

### 3.5 Logistics has an exact answer, and the rulebook's hint is misleading

The vehicle cost formula is `24,000 + 1.2 × load in kg`, one kilogram equals two units, and a vehicle
runs 2,000 hours a year on 8-hour routes (§10).

Per full vehicle, bigger is dramatically cheaper:

| Load capacity | Cost per unit delivered |
| ------------- | ----------------------- |
| 24,000 kg     | €0.0044                 |
| 12,000 kg     | €0.0064                 |
| 6,000 kg      | €0.0104                 |
| 1,000 kg      | €0.0504                 |

That is an **11× spread** on an identical formula.

But the deeper result is this: once your fleet exactly covers your volume, the per-kilogram term
cancels out, and total cost collapses to

> **24,000 × (number of vehicles) + 0.0024 × (units)**

So the real decision is not "how big" but **"how few."** Minimise the vehicle count, then size each
vehicle to fit your volume exactly. Buying 24,000 kg trucks when 20,000 kg would fit costs you 10%
more for nothing. `optimal_vehicle_plan()` does this for you.

**And the trap:** §10 offers €0.006 per unit as a "reasonable" guideline. Any vehicle above roughly
9,000 kg already beats it. A team that hits €0.006 will believe it has optimised, while paying **36%
more than the achievable €0.0044**.

### 3.6 The two irreversible investments have opposite answers

The simulation runs four graded years. Any irreversible investment that does not pay back inside four
years destroys value. Both major options are irreversible (§26, §27).

**SMED (€3,000,000 per module)** eliminates the 250 hours of module downtime, lifting utilisation
from 78.75% to 91.25% — **+15.9% output**, worth €208,614 of extra contribution per line per year at
a €4.20 price.

Whether it is worth buying depends entirely on one question the scenario never answers: **how many
production lines can a single duplicate module serve?**

| Lines served per module | Payback    | Verdict          |
| ----------------------- | ---------- | ---------------- |
| 1 line per module       | 14.4 years | Never worth it   |
| 4 lines per module      | 3.6 years  | Marginal         |
| 8 lines per module      | 1.8 years  | Clearly worth it |

**This is the highest-value question to ask the Director in Session 2.** The answer swings a
multi-million-euro decision from obviously wrong to obviously right. The physics suggests one module
could serve up to eight lines — servicing takes 5 hours and recurs every 40 operating hours — but
this is inference, not a stated rule.

**Poka Yoke (€720,000 per line)** eliminates scrap and cuts breakdown detection time. At ten H lines
running three shifts it adds 630,000 units a year (+4.55%) and saves 315,000 units of scrap — worth
about €584,000 of contribution against €7,200,000 of capital.

> **Payback: 12.3 years, against a four-year game. On these numbers, Poka Yoke destroys value.**

Unless the Director confirms it carries a brand or quality benefit that the scenario does not
document, this is a trap — and an attractive-looking one, because "install quality control" sounds
like unambiguously good management.

**Preventive maintenance (€500,000 per year)** is different: it is not irreversible, it is decided
annually. At ten H lines on three shifts it yields about €613,000 of extra contribution for €500,000
of cost — marginally positive, and it improves as you add lines. Worth taking once the plant is large
enough.

### 3.7 The financing answers are unusually clear-cut

Rates set by §49:

| Instrument                                | Rate                                 |
| ----------------------------------------- | ------------------------------------ |
| Fixed-term deposit / financial investment | 2.5% earned                          |
| **Factoring**                             | **5.5% paid**                        |
| Credit line                               | 7.0% paid (+1% service, +1% upfront) |
| Bank loan                                 | 10.0% paid (+1% upfront)             |
| **Overdraft**                             | **20.0% paid**                       |

Three conclusions follow directly:

1. **Factor your receivables rather than borrowing against them.** Factoring at 5.5% is 4.5
   percentage points cheaper than a 10% loan. On €100,000,000 of revenue at 120-day terms — a
   €33,333,333 receivable — that is **€1,500,000 a year** of pure saving.
2. **Never allow an overdraft.** At 20% it is double the loan rate. And it can happen to you
   passively: §41 states that if your operating cash need exceeds available cash, the simulator takes
   a loan on your behalf. Sloppy cash planning is silently expensive. The model's `ocn()` function
   reproduces the §41 rule exactly so you can check before submitting.
3. **Do not leave €54,000,000 sitting in Cash.** It earns nothing there. At the 2.5% deposit rate
   that is **€1,350,000 a year** you are giving away for free (§44). Your opening balance sheet is
   82% idle cash.

### 3.8 Some costs are simply unavoidable — plan around them, not against them

| Cost                          | Amount                         | Notes                                           |
| ----------------------------- | ------------------------------ | ----------------------------------------------- |
| Office and management payroll | €2,413,092 – €3,371,620        | 56 people at fixed levels (§29)                 |
| General overhead              | €600,000                       | Fixed (§29)                                     |
| **R&D**                       | **4.5% of revenue**            | Automatic, no decision, cannot be avoided (§36) |
| Depreciation                  | 8% / 10% / 12% of fixed assets | Rises with shift count (§35)                    |

The R&D charge deserves attention. It is levied on **revenue, not profit**. It is therefore a direct
tax on a premium-price strategy: every euro of extra price hands 4.5 cents back automatically. Add
the wholesaler's 8.46% of retail (§7) and roughly **13% of any price increase never reaches you**.

This is why the model's break-even calculator shows moving from your own salesforce to wholesalers
pushing the minimum viable H price from €3.86 to €4.23 — a 9.6% jump for the same product.

Depreciation deserves attention too: moving from one shift to three raises it from 8% to 12% of
fixed assets. Running three shifts is usually right — it spreads your irreversible line investment
over three times the output — but it is not free.

### 3.9 Three market research surveys are free, and most teams will not use them

Of the 28 surveys in §50, **surveys 20, 21 and 22 cost nothing**:

- **20** — every competitor's retail prices, by market and channel
- **21** — every competitor's advertising campaign
- **22** — every competitor's promotion type, by channel

That is your rivals' entire commercial strategy, free, every single year.

Beyond those, the cheap intelligence is disproportionately good value: competitor net income costs
€1,000 (survey 23), production shifts €1,000 (28), market sales €3,000 each (1 and 2), platform
counts €3,000 (27). For **€11,000** you can know what every rival earned, how hard their factories
are running, and how big the market actually got.

At the other end, survey 19 — true demand including the units you failed to serve — costs €110,000
and is the only way to see the sales you lost to stockouts. Buying the entire menu would cost
€1,003,400, which is not sensible; targeted buying is.

---

## 4. Conclusions

Five things the arithmetic establishes, in order of how much they should change your plan:

**1. You are constrained by capacity, not demand.** The maximum legal factory serves 33.8% of the
moisturiser market. Every plan is a choice about which demand to serve. Teams that plan for market
coverage instead of profitable coverage will stock out and take permanent brand damage under §34.

**2. Your real capacity is 78.75% of the headline number.** This is the most likely single error any
team will make, and it compounds: it produces an over-optimistic sales forecast, which produces a
stockout, which produces brand damage that persists into later years.

**3. Moisturiser is structurally the stronger business.** 3.5× better on capital per unit, 2.4×
better on running cost. Sunscreen requires roughly double the price to break even. Both can work —
but the product mix is an irreversible decision made in year 1 and carried for all four years (§22),
so it deserves more analysis than any other single choice.

**4. Several "obviously good management" decisions are value-destroying here.** Poka Yoke pays back
in 12.3 years against a 4-year game. Social media costs 67% more per unit of reach than television.
Hitting the rulebook's own €0.006 logistics benchmark costs 36% more than achievable. The
common thread: the intuitive answer and the arithmetic answer point in opposite directions.

**5. The financing decisions are nearly free money, and most teams will not take them.** Factoring
instead of borrowing saves 4.5 points. Depositing idle cash earns €1,350,000 a year. Neither
requires a clever strategy — only that someone does the arithmetic.

---

## 5. Actions to take

### Before Session 2 — this week

| #   | Action                                                                                      | Why                                                                                       |
| --- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1   | Run `--briefing` and read the output once                                                   | It is one page and it is the entire quantitative picture                                  |
| 2   | Bring the SMED question to the Director: **how many lines can one duplicate module serve?** | Swings the decision from 14.4-year payback to 1.8-year. Highest-value unknown in the game |
| 3   | Ask the Director about §18's missing two promotion types                                    | The rulebook says eight and lists six                                                     |
| 4   | Confirm the loan repayment rule in §42                                                      | "A proportion" is undefined; it changes every cash forecast                               |

### During the ungraded test round — two virtual years

The test round is graded zero. Its only value is information. Most teams will treat it as practice
and learn nothing measurable.

| #   | Action                                                             | Why                                                                                                                                  |
| --- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| 5   | **Deliberately vary your prices and advertising across markets**   | You are buying data. `fit_elasticities()` cannot recover a price elasticity if you charged the same price everywhere — no method can |
| 6   | Buy surveys 20, 21, 22 (free) plus 23 and 28 (€2,000) every year   | Rival prices, campaigns, promotions, profits and shifts for €2,000                                                                   |
| 7   | Record every year in an `Observation` and run `fit_elasticities()` | By the graded round you forecast from your own data instead of guessing                                                              |
| 8   | Test one deliberate stockout and one deliberate overstock          | Measure what §34's "brand prestige" damage actually costs. Nobody else will know this number                                         |
| 9   | Check the simulator's actual output against `capacity()`           | Confirms whether the 78.75% or 79.7% reading of §24 is correct, and settles the loan rule                                            |

### Entering the graded round — four years, this is what counts

| #   | Action                                                                                  | Why                                                                |
| --- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 10  | Decide the S/H line mix using §3.2, and commit in year 1                                | Lines are irreversible (§22). This choice is locked for four years |
| 11  | Run `capacity_reality_check()` before every single submission                           | Prevents the most expensive and most common error                  |
| 12  | Lead with television; treat social media as a supplement                                | 67% cheaper per point of reach in A/B (§3.4)                       |
| 13  | Use `optimal_vehicle_plan()` rather than the §10 benchmark                              | The benchmark costs 36% more than achievable                       |
| 14  | Factor receivables; deposit surplus cash; never overdraft                               | €1,500,000 + €1,350,000 a year, on the numbers above               |
| 15  | Buy SMED in year 2 **only if** the Director's answer to action 2 is 4+ lines per module | Otherwise it is a 14-year payback in a 4-year game                 |
| 16  | Treat Poka Yoke as a no unless new information changes the case                         | 12.3-year payback (§3.6)                                           |
| 17  | Run `--selftest` after any edit to the constants                                        | 89 checks; catches a mistyped rate before it reaches a CEO meeting |

### A note on how to use this in the CEO meetings

The evaluation guidelines are explicit: *"IT IS A MUST TO ESTABLISH THE CAUSES FOR THE COMPANY'S
RESULTS."* Analysis that describes what happened scores badly; analysis that explains *why* scores
well. Only 10% of your grade is the actual simulated result — 65% is analysis quality, presentation
and peer assessment.

Every number in this model carries its rulebook section reference (`§22`, `§41`, and so on). When
the CEO challenges a figure, you can point at the rule it comes from. That is the difference between
defending a forecast and defending a guess.

---

## Appendix: correction to earlier figures

Two numbers I quoted before the model was finished have been superseded by fuller calculations:

| Figure                            | Earlier       | Now               | Why it changed                                        |
| --------------------------------- | ------------- | ----------------- | ----------------------------------------------------- |
| Standard cost, S / H              | €4.29 / €1.87 | **€5.13 / €2.13** | Now includes scrap and breakdown repair costs (§24)   |
| Capex per unit of capacity, S / H | €2.92 / €0.83 | **€3.79 / €1.08** | Now measured against *sellable* output, not nameplate |

The conclusions are unchanged — H remains 3.5× better on capital and 2.4× cheaper to run. The
corrected figures are the ones to quote.

Similarly, the earlier guidance "always max out vehicle load capacity" was right per vehicle but
wrong as a fleet plan. The correct rule is in §3.5: **minimise the number of vehicles, then size each
one to fit your volume exactly.**
