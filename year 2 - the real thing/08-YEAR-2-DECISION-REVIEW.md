# 08 · Year 2 decisions — review and grade

Reviewed against `07-YEAR-2-DECISIONS-AS-ENTERED.md`, the graded Year-1 result sheets, and
`model/calibration.py`, which now reproduces **32 of 32** figures from the Year-1 report
exactly. Every euro below is computed, not asserted; the script is
`python3 model/calibration.py`.

## Verdict

> **B+ overall.** The operations and balance-sheet decisions are excellent and repair both
> of Year 1's real errors — 17.6M units of unsellable moisturiser and €26M of unnecessary
> debt. The pricing is the weak half, for the second year running. On the central
> elasticities the plan creates roughly **€12.1M** of value against Year 1 and leaves
> roughly **€11.8M** on the table, all of it in two price fields that cost nothing to type.

The structural read matters more than the score. Year 1 was constrained by capacity and
Year 2 is not; Year 1 was constrained by cash and Year 2 is not. **Price is now the only
large lever left, and it is the one being under-used.**

## Scorecard

| #   | Decision                | Entered                   | Grade | Worth (central)   | One-line reason                                                                    |
| --- | ----------------------- | ------------------------- | ----- | ----------------- | ---------------------------------------------------------------------------------- |
| 1   | Loan prepayment         | €19,500,000               | A+    | +€3,900,000       | A 1% penalty kills three years of 10% coupons `[+]`                                |
| 2   | SMED, 2 modules         | €6,000,000                | A     | +€9,160,000       | Pays back in 0.65 years, on lines already owned `[+]`                              |
| 3   | H lines activated       | 22 → **2**                | A     | +€64,200,000 cash | Stops making a product with 17.6M units already in stock `[+]`                     |
| 4   | Training department     | off                       | A     | +€662,000         | €722,000 bought €60,000 of measured turnover saving `[+]`                          |
| 5   | Research budget         | €166,800 → €680,600       | A     | information       | Buys every survey that explains the market-A moisturiser gap `[+]`                 |
| 6   | Market E block          | left at defaults          | A     | €0                | The simulator's own on-screen instruction; Year 1 proved it costs nothing          |
| 7   | Credit line             | €10,000,000 → €0          | A−    | +€200,000         | Saves the 2% undrawn fee; leaves no backstop but the trough is €32M deep           |
| 8   | H price, market A       | 6.50 → **7.50**           | A−    | +€2,250,000       | Right direction, right size — but see note 12                                      |
| 9   | Advertising, shelf, POP | all held                  | B+    | control           | Correct: net rating is already ~100%, and holding them keeps the price read clean  |
| 10  | Raw material entries    | S 6,578,235 · H 3,446,019 | B+    | −€129,350         | ~1% above the calibrated need — over-buying is the safe error (§28) `[~]`          |
| 11  | Fixed-term deposit      | €10,000,000               | B+    | +€250,000         | Right instrument, undersized against a year that closes near €120M of cash         |
| 12  | Logistics trim          | 50 → 42 last-mile         | B−    | +€170,400         | Load per vehicle rises 20.7% with no measured headroom `[!]`                       |
| 13  | Promotion design        | both markets, channel S   | C+    | −€339,000         | Needs a 13.6% uplift to break even, and running both markets destroyed the control |
| 14  | H price, market B       | **held at 7.50**          | C     | −€5,470,000       | The most-tested inelastic price in the game, left untouched `[!]`                  |
| 15  | S price                 | 14.50 → **15.00**         | C−    | −€5,990,000       | Below the clearing price under *every* elasticity we can defend `[!]`              |

## What the plan gets right

**The plant decision is the best call of the year.** Year 1 activated 22 moisturiser lines
and made 32,175,000 units against demand of 15,047,394. Year 2 activates **2**. That single
field avoids €27,270,000 of crew cost and €36,899,200 of raw material — **€64.2M of cash
that Year 1 converted into stock**. The 17,628,699 units already in the warehouse were paid
for last year; every one sold in Year 2 is contribution against a sunk cost.

**SMED is textbook.** Two modules at €3,000,000 each lift utilisation from 81.25% to 92.9%.
On the sunscreen lines that is 5,850,000 → 6,688,800 units, and because the crew cost is
spread over more units the standard cost falls from €5.5604 to €5.1358. Contribution goes
from €44.11M to €53.27M — **+€9.16M in Year 2 alone against €6.0M of capex.** Payback 0.65
years, comfortably inside the four-year rule.

**The balance sheet is now clean.** Prepaying €19,500,000 costs a 1% penalty of €195,000 and
cancels €1,950,000 + €1,300,000 + €650,000 of interest across Years 2–4. Dropping the
undrawn credit line saves another €200,000. Year 1 paid €3,060,000 in financial expense on
money it never used; Year 2's financial line is **positive**, at roughly +€55,000 after the
deposit interest.

**The research budget is the right kind of brave.** €680,600 for 22 surveys — including 4
(sales by channel), 11 (rival insertions), 13 (rival POP), 14 (rival salesforce) and 15
(shelf space achieved) — buys exactly the variables that could explain why our moisturiser
took 22.6% of market A at the lowest price on the shelf while two rivals sold out. Against a
gap worth roughly €12M a year, €680,600 is not a cost.

## What the plan leaves on the table

### 15.1 · Sunscreen at €15.00 is below the clearing price `[!]`

Year 1 measured brand demand of **7,677,440** units at €14.50 — 5,850,000 sold plus
1,827,440 the report prints as unserved. Capacity with SMED is 6,688,800. The price that
makes demand equal capacity is:

| Elasticity | Clearing price | Contribution at €15.00 | Contribution at clearing | Forgone    |
| ---------- | -------------- | ---------------------- | ------------------------ | ---------- |
| −1.2       | €16.27         | €53.27M                | €61.73M                  | **€8.46M** |
| −1.5       | €15.90         | €53.27M                | €59.26M                  | **€5.99M** |
| −2.0       | €15.53         | €53.27M                | €56.85M                  | **€3.58M** |
| −2.5       | €15.32         | €53.27M                | €55.42M                  | **€2.15M** |

€15.00 sits below the clearing price at **every** elasticity in the defensible range, so
this is not a judgement call that could go either way — it is dominated. The plant sells out
at €15.00, €15.50, €16.00 and €16.50 on the central reading, and each extra euro is
6,688,800 euros of pure contribution.

There is a second cost. At €15.00 roughly **608,000 units of demand go unserved for the
second year running**, and §34 says the brand damage from a stockout outlives the year we
cause it. A higher price would have earned more *and* reduced the damage. That is the rare
decision with no trade-off in it, and it was the one not taken.

### 14.1 · Moisturiser in market B held at €7.50 `[!]`

Market B is the best-measured price point in the game: 55.1% share at €7.75 in test Year 2,
55.8% share at €7.50 in graded Year 1, against Company 2 selling at €10.00–11.00 in the same
market. The elasticity is around −0.9 — **inelastic, so revenue rises with price.**

| B price  | Contribution at e = −0.9 | Contribution at e = −1.6 |
| -------- | ------------------------ | ------------------------ |
| 7.50     | €41.71M (entered)        | €41.71M                  |
| 8.00     | €44.07M                  | €42.12M                  |
| **8.75** | **€47.17M**              | **€42.35M**              |
| 9.50     | €49.86M                  | €42.26M                  |

€8.75 beats €7.50 at **both ends** of the elasticity range — by €5.47M at −0.9 and still by
€0.64M at −1.6. There was no reading of the data under which holding B was the better choice.

Worse, moving market A to €7.50 while holding B at €7.50 makes the two prices identical,
which **throws away the cross-market price experiment** that `01-DEMAND-MODEL.md` calls the
single most valuable thing we can do in a year. Two prices in one year beat any comparison
across years, and it costs nothing to set them.

### 13.1 · The promotion is priced to lose

Three price reductions of €0.50 in channel S, in both markets. Contribution falls from
€4.1748 to €3.6748 per promoted unit, so the promotion must lift channel-S volume by
**13.6%** across the 17.3% of the year it covers just to break even. A €0.50 cut on a €7.50
price is a 6.7% discount, which at e = −0.9 buys about 6.2% more volume — roughly half what
is needed. Expected cost: **−€339,000**.

Two cheaper versions of the same experiment existed:

| Option                               | Cost      | Information | Note                                             |
| ------------------------------------ | --------- | ----------- | ------------------------------------------------ |
| As entered — both markets, channel S | −€339,000 | same        | B/S is 5.86M units, so B carries 81% of the bill |
| **Market A only, channel S**         | −€64,000  | same        | B/S stays a clean untouched control `[+]`        |
| Direct gift (type 5) at €0.40/unit   | lower     | same        | Break-even uplift 10.6% instead of 13.6% (§18)   |

The design is not wasted — channels G and T are unpromoted in both markets, so the promotion
can still be read as A/S versus A/T. But it cost €275,000 more than the same answer needed to.

### 12.1 · The logistics trim is the one uncosted risk `[!]`

Last-mile vehicles go 50 → 42 while volume stays flat, so units per vehicle rise from 407,926
to 492,500 — **+20.7% with no measurement of where the flag threshold sits**. The saving is
€170,400. The test round showed an emergency premium of €1,527,519 on a single flagged
market. This is a 9:1 risk-reward against us, taken to save less than one percent of
operating income. The trunk cut (5 → 4 vehicles) is fine — the 500 × kg rule is known and
predicted all four observed flags, and 4 vehicles at 24,000 kg cover 48M units against ~20.7M
shipped.

## Year-2 forecast at the decisions as entered

| Line                     | Year 1 actual | **Year 2 forecast**  | Δ           |
| ------------------------ | ------------- | -------------------- | ----------- |
| Sales at MSRP            | €189,365,764  | **€205,879,597**     | +8.7%       |
| Net revenue              | €163,704,462  | **€179,097,864**     | +9.4%       |
| Gross profit             | €95,720,201   | **€109,885,934**     | +14.8%      |
| Gross margin on net rev. | 58.5%         | **61.4%**            | +2.9 pp     |
| General expenses         | €24,837,009   | **€26,204,859**      | +5.5%       |
| Operating income         | €70,883,192   | **€83,681,075**      | +18.1%      |
| Financial income/expense | −€3,060,000   | **+€55,000**         | +€3,115,000 |
| **Net income**           | €67,823,192   | **€83,736,075**      | **+23.5%**  |
| S units sold             | 5,850,000     | 6,688,800 (sold out) | +14.3%      |
| H units sold             | 14,546,301    | ~14,073,013          | −3.3%       |
| H stock at 31 December   | 17,628,699    | **6,900,086**        | −60.9%      |

Assumptions: H elasticity −0.90, S elasticity −1.50, 6.2% promotion uplift, no market growth,
no rival capacity change. **The largest unmodelled risk is Company 4 adding a third shift** —
it ran 2 shifts on ~17 lines in Year 1 and sold out; a third shift adds roughly 50% to its
output and it already matches Company 2's share of moisturiser in market A.

## What to carry into Year 3

| #   | Action                                                                 | Why now                                                                 |
| --- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 1   | **Price sunscreen at or above the clearing price**                     | Two stockout years in a row; the plant is fixed at 6,688,800 units      |
| 2   | **Move moisturiser in market B to €8.75–9.50**                         | Inelastic, measured three times, and €1.25–2.25 below the nearest rival |
| 3   | **Always run two different prices for one product in one year**        | The only clean way to recover an elasticity; Year 2 gave that up        |
| 4   | Read surveys 11, 13, 14, 15 before touching market-A moisturiser again | €680,600 has been spent to answer exactly this                          |
| 5   | Restore the last-mile fleet if Year 2 shows a logistic stockout flag   | The premium is ~2× the planned cost                                     |
| 6   | Size the deposit to the actual surplus, not a round €10M               | Year 2 closes near €120M of cash; 2.5% on the idle balance is free      |

## Sources

`07-YEAR-2-DECISIONS-AS-ENTERED.md` · `DIR0114SI02083TE3Y1REP.pdf` p2–p6, p8 ·
`DIR0114SI02083TE3Y1INV.pdf` surveys 3, 20, 22, 23, 28 · `DIR0114SI02083TE3Y1INFen_US.pdf` p2 ·
`anthony results + review/01-results-vs-plan.md` · `anthony results + review/02-competitor-brief.md` ·
`model/calibration.py` (32/32 checks) · `Scenario MMT39 .pdf` §18, §27, §28, §34, §41, §42.
