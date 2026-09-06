---
name: mmt39-results
description: Process an MMT39 results sheet the moment it arrives — extract the actuals, compare against forecast, recalibrate the model, and prepare the CEO analysis. Use when the user uploads or mentions new simulation results, DEP/REP/INV/INF reports, or asks what the results mean.
---

# Processing an MMT39 results sheet

## 1. Extract

```bash
pdftotext -layout "<file>.pdf" out.txt
```

Four reports per year: **DEP** decisions as submitted · **REP** results, P&L, balance
sheet, ratios · **INV** surveys · **INF** the Director's factor values.

Read INF first. Per-capita income, raw material and power costs, exchange rate, interest
rates and loan maturity all change between years, and every forecast depends on them.

## 2. Record actual vs forecast

Fill the table in `year 2 - real thing/04-RESULTS-INTAKE-CHECKLIST.md`. The gap between
what was predicted and what happened is what the rubric grades — the guidelines say in
capitals that it is a must to establish the causes.

## 3. Recalibrate

Re-run `python3 model/calibration.py`. Then check, in this order:

| Read | Against | Tells you |
| ---- | ------- | --------- |
| units produced / (nameplate x shifts) | 0.8125, or 0.929 with SMED | is the utilisation constant still right |
| RM used / units produced | 1.02 | is the scrap rate still 2% |
| reported standard cost | `standard_cost()` | is the 1.70 power multiplier still right |
| units demanded of your brand | the forecast demand | **the elasticity — the most valuable line on the sheet** |
| transport cost and stockout flags | `trunk_capacity()` and the planned fleet | is the fleet right-sized |
| financial expenses | the plan | did the simulator borrow on your behalf |

Update the anchors in `01-DEMAND-MODEL.md` with the new price/demand point. Two points
per market make a curve; three make a forecast.

## 4. Never delete a superseded figure

Move it to `SUMMARIES.txt` Appendix A with old and new side by side, so nobody quotes a
stale number in a CEO meeting.
