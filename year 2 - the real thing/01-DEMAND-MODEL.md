# 01 · Demand model — the anchors and how to forecast from them

The simulator's demand engine is hidden. What follows is fitted to the **graded Year-1**
result sheet, which supersedes the test-round anchors entirely: the test round ran a different
simulation instance (`B1SIM2C1`) with different Director factors, and its share figures mixed
two incompatible bases. This is still the most valuable and least certain thing in the
repository.

## The anchors — units of our own brand demand

📌 **Anchor on units, not share.** "Units demanded of your brand" (REP p2/p3) is the only
**uncensored** demand figure the simulator prints: it is reported even when we stock out and
sell less. Share figures depend on what rivals happened to supply, which is not a property of
our demand curve.

| Product | Market | Price | Media       | Units sold | Unserved  | **Brand demand** | Source    |
| ------- | ------ | ----- | ----------- | ---------- | --------- | ---------------- | --------- |
| S       | A+B    | 14.50 | 4 PR + 8 TV | 5,850,000  | 1,827,440 | **7,677,440**    | graded Y1 |
| H       | A      | 6.50  | 3 PR + 5 TV | 4,556,494  | —         | **4,556,494**    | graded Y1 |
| H       | B      | 7.50  | 3 PR + 5 TV | 9,989,807  | —         | **9,989,807**    | graded Y1 |
| H       | A+B    | —     | —           | 14,546,301 | 501,093   | 15,047,394       | graded Y1 |

Conditions held constant across all four rows: campaign 18 / 19, positioning S (1,8) and
H (9,1), retailer margin S 1.90 / H 1.00, shelf-space objective S 18% / H 22%, POP €10,000 /
€15,000 per channel, no promotions, 6 sales managers and 8 reps per zone in each market.
**The forecast is conditional on all of it.** Change one and the anchors stop being anchors.

`[~]` Sunscreen demand is **not split by market**. Year 1 stocked out, so the simulator's A/B
allocation of a short supply says nothing about where the demand sat — market B took 90,504
units at the same price that sold 5,759,496 in A. Treat S as one A+B pool until supply exceeds
A's demand.

`[~]` The 501,093 units of unserved moisturiser sit alongside 17.6M units of stock and no
logistic stockout flag. The report does not explain it. Treat it as upside, not as a plan line.

## Implied elasticities

| Product | Central   | Range           | Why the uncertainty                                                                                        |
| ------- | --------- | --------------- | ---------------------------------------------------------------------------------------------------------- |
| H       | **−0.90** | −0.563 to −1.60 | The two same-year price points give −0.563, but B is the richer market so the true figure is more negative |
| S       | **−1.50** | −1.20 to −2.50  | No within-year price variation exists for S — both markets were priced flat at 14.50 in Year 1             |

📌 **Moisturiser is inelastic.** With |e| < 1, revenue *rises* with price. That single fact is
worth more than every cost decision in the model combined — and it is why holding market B at
€7.50 in Year 2 was the most expensive field on the sheet (`08-YEAR-2-DECISION-REVIEW.md` §14.1).

## Price is not the driver of moisturiser in market A `[!]`

The clearest finding of Year 1, and the one that should govern Year 3:

| Company | H price in A  | Units sold in A | Promotion            | Positioning   |
| ------- | ------------- | --------------- | -------------------- | ------------- |
| 2       | 9.50 – 10.50  | 7,782,836       | price reduction, all | (9,1) natural |
| 4       | 6.50 – 7.20   | 7,743,383       | 3×2 in supermarkets  | (1,8) tech    |
| **3**   | **6.50 flat** | **4,556,494**   | **none**             | (9,1) natural |

We were the cheapest and finished third. A rival at €3.00–4.00 above us, running **our
campaign and our positioning**, sold 71% more. Whatever decides moisturiser in market A, it is
not price. Surveys 11, 13, 14 and 15 — all bought for Year 2 — are the instruments that can
identify it.

The channel data sharpens it further: in market A our hypermarket channel sold **63,960**
units across 35 stores, while in market B it sold 2,057,439 across 30. The same 35 A
hypermarkets took 2,587,071 units of our sunscreen. Channel G behaves as winner-take-most, and
in A our moisturiser is not the winner.

## Advertising: a saturation curve, not a straight line

| Insertions per market | Observed effect                                             |
| --------------------- | ----------------------------------------------------------- |
| 3                     | `[!]` share collapsed to ~2% (test Y2, market B, sunscreen) |
| 7 vs 14               | `[+]` no measurable difference (test Y1, A vs B)            |
| 8 to 12               | the safe operating band; net rating already ~99.9%          |

⚖️ Reaching ~99% net rating is necessary but not sufficient, and beyond it extra insertions buy
frequency, not reach. Television is the cheapest reach at €300 per point of buyers, social
media the dearest at €500. **Never starve a market. Do not gold-plate one either.**

## How to forecast a year

```python
from model.calibration import demand_H, demand_S, clearing_price, output, standard_cost

demand_S(15.50)                        # units of S demanded across A+B
demand_H("B", 8.75)                    # units of H demanded in market B
output("S", 10, 3, smed=True)          # 6,688,800 units the plant can make
clearing_price(6_688_800)              # the S price at which demand == capacity
standard_cost("S", smed=True)          # 5.1358
```

Sold = `min(demand, available)`. Unsold units become finished goods: they never deteriorate and
are sold first next year (§3), so over-producing costs working capital, not profit. **Unserved
demand is the asymmetric risk** — §34 says a stockout damages brand prestige into later years,
and Year 1 left 1,827,440 units of sunscreen unserved.

## The one experiment that matters most

Every year, price the two markets **differently** for at least one product. Two prices in one
year give a clean elasticity with the year's conditions held constant; comparing across years
never will.

`[!]` **Year 2 gave this up.** Sunscreen is €15.00 in both markets and moisturiser €7.50 in
both. The only reads available from Year 2 are time-series: S 14.50 → 15.00 with everything
else held, and H in market A 6.50 → 7.50 with market B as a same-price control. That control is
genuinely useful — B/T and B/G are untouched on every dimension — but it is second best, and it
was avoidable at zero cost.

## Update log

| Date       | Change                                                                                                                              |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 2026-09-06 | Anchors established from test Y1 and Y2                                                                                             |
| 2026-09-06 | **Rebuilt on graded Year 1.** Test-round share anchors retired; replaced with unit-demand anchors. Added the market-A price finding |
