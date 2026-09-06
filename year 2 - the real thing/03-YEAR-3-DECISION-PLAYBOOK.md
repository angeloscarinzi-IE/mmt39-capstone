# 03 · Year 3 playbook

⚠️ **Nothing here is final until the Year-2 results land.** Run
`04-RESULTS-INTAKE-CHECKLIST.md` first, then come back and fill the "actual" column.

## Audit trail — what the provisional Year-2 playbook proposed vs what was entered

Kept in full per project rule 4. The provisional plan was written before the Year-1 results
arrived; six of its ten items survived contact with the data.

| #   | Provisional Year-2 proposal    | Entered                    | Verdict                                                                                                                         |
| --- | ------------------------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1   | S price 18.00 A / 18.50 B      | **15.00 flat**             | Both wrong: 18.00 was built on a pre-result demand guess; 15.00 is below the clearing price. The defensible band is 15.32–16.27 |
| 2   | H price 8.00 A / 8.75 B        | **7.50 flat**              | A moved the right way but short; B should have moved and did not `[!]`                                                          |
| 3   | Training department off        | **off**                    | Correct, +€662,000 `[+]`                                                                                                        |
| 4   | SMED, 2 modules                | **2 modules**              | Correct, +€9.16M `[+]`                                                                                                          |
| 5   | Add surveys 19, 15, 11, 4      | **all four, plus 7 more**  | Correct and then some `[+]`                                                                                                     |
| 6   | Deposit the surplus            | **€10,000,000**            | Right instrument, undersized                                                                                                    |
| 7   | Prepay the loan if cash allows | **€19,500,000 prepaid**    | Correct, +€3.9M of coupons killed `[+]`                                                                                         |
| 8   | Decide market E explicitly     | **left at defaults**       | Correct — the simulator's own instruction; costs nothing                                                                        |
| 9   | One promotion as a test        | **two markets, channel S** | Right idea, twice the necessary cost, control weakened                                                                          |
| 10  | Hold everything else           | **held**                   | Correct `[+]`                                                                                                                   |

The provisional plan also assumed all 32 line slots would stay activated. They did not, and
should not have: only 12 lines ran. That was the single best decision of Year 2.

## The Year-3 thesis in one line

Year 1 built the plant, Year 2 fixed the balance sheet and the plant utilisation. **Year 3 is
the pricing year** — it is the only large lever still under-used, and Year 2's surveys are
about to say why market A's moisturiser resists us.

## The Year-3 plan

| #   | Decision             | Year 2       | Year-3 proposal                              | Worth         | Why                                                                                         |
| --- | -------------------- | ------------ | -------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------- |
| 1   | S price              | 15.00 flat   | **at or above the clearing price**           | +€2.2–8.5M    | Below it at every defensible elasticity; recompute with `clearing_price()` on Year-2 demand |
| 2   | H price, market B    | 7.50         | **8.75, or 9.50 if Year 2 confirms**         | +€5.5M        | Inelastic and measured three times; nearest rival sells at 10.00–11.00                      |
| 3   | S price, split A / B | flat         | **differ by €1.00**                          | information   | The one experiment that recovers an elasticity within a year; costs nothing                 |
| 4   | H in market A        | 7.50 + promo | **act on surveys 11, 13, 14, 15**            | up to €12M/yr | 16-point share gap at the lowest price in the market — the cause is now buyable             |
| 5   | H lines activated    | 2            | **size to demand + one line of cover**       | cash          | 6,900,086 units carry in; do not rebuild the 17.6M pile                                     |
| 6   | Supplier terms       | 120 days?    | **60 days or cash**                          | +€250–350k    | 120 days cost 3% of raw material to buy float worth 0.83% `[!]`                             |
| 7   | Last-mile fleet      | 42 vehicles  | **restore if Year 2 flags**                  | −€1.5M risk   | The emergency premium is ~2× the planned cost                                               |
| 8   | Fixed-term deposit   | €10,000,000  | **size to the actual surplus**               | +€1–2M        | Year 2 closes near €120M of cash; 2.5% on idle balances is free                             |
| 9   | Promotion            | both markets | **one market only, type 5**                  | −€275k saved  | Direct gift breaks even at 10.6% uplift, price reduction at 13.6%                           |
| 10  | Market E             | out          | **stay out unless survey 19 says otherwise** | —             | 98,165 participant units against 110,100,000 of potential                                   |

`[!]` Items 1 and 2 are worth €8–14M together and cost nothing to type. If time is short, do
those two and item 3.

## Sizing the sunscreen price

```python
from model.calibration import clearing_price, demand_S, output, standard_cost
cap = output("S", 10, 3, smed=True)          # 6,688,800
clearing_price(cap)                           # central elasticity
[clearing_price(cap, e) for e in (-1.2, -1.5, -2.0, -2.5)]
```

Re-anchor `S_ANCHOR` on the Year-2 report's "units demanded of your brand" **before** running
this. The plant is fixed at 6,688,800 units for the rest of the game, so the whole sunscreen
decision reduces to one number: the price at which demand equals that.

## Cash sequence for Year 3

Read in this order, from the Year-2 balance sheet:

1. Cash and equivalents at 31 December
2. minus the loan instalment due 2 January — **should now be zero**, the balance was prepaid
3. minus credit line outstanding · minus accounts payable
4. plus receivables — we do not factor, so these come back in full
5. plus the fixed-term deposit and its interest
6. = available cash. Then run the §41 operating-cash test and confirm it clears.

## Pre-submission checklist

- [ ] **Information screen read first.** Income, raw material and power costs, exchange rate,
      interest rates, **loan maturity**. If anything moved, re-run the plan
- [ ] Sales managers re-entered 6 / 6 / 0 — resets to zero
- [ ] All six salary fields re-entered — reset to the legal minimum
- [ ] Training department **unchecked**
- [ ] Price, retailer margin **and** shelf space in every channel we sell in
- [ ] Campaign 18 for S and 19 for H, in **both** markets; media identical in A and B
- [ ] **Lines to be activated** — resets to zero. So does **SMED to be activated**
- [ ] Shifts 3 · preventive maintenance checked · Poka Yoke unchecked
- [ ] **Raw material = production × 1.02, less opening stock.** Typed by one person, read back
      by another. At 92.9% utilisation, not 93.6%
- [ ] Supplier terms shortened · factoring unchecked · customer terms 60 days
- [ ] Credit line: leave at zero unless the §41 test is tight
- [ ] Surplus cash into a fixed-term deposit, sized to the surplus
- [ ] §41 operating cash needed ≤ available cash
- [ ] Surveys re-selected — they reset too
- [ ] **Two different prices for at least one product**
