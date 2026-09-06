---
name: mmt39-decisions
description: Build and check a year's MMT39 decision sheet before it is keyed into the simulator. Use whenever the user is preparing, revising or sanity-checking decisions for a virtual year (prices, lines, shifts, logistics, HR, finance, raw material, surveys), or asks "what should we enter for year N".
---

# Entering a year of MMT39 decisions

## Order of work — price first, plant second

The test round proved capacity was never the binding constraint; price was. Set
prices from the demand anchors in `year 2 - real thing/01-DEMAND-MODEL.md`, then
size the plant to the demand that price implies. Never the other way round.

## Always use the calibrated engine

```bash
python3 model/calibration.py     # 15 checks against the actual result sheets
```

Import `model/calibration.py`, not the raw constants in `mmt39.py`. The scenario-derived
figures in `mmt39.py` (78.75% utilisation, uncalibrated standard cost, depreciation on
total fixed assets) are known to be wrong. See
`year 2 - real thing/00-CALIBRATION-CONSTANTS.md`.

## The five fields that silently produce zero sales

A blank or zero here means the simulator assumes you do not want to trade, with no warning:

1. Price (§14) · 2. Retailer margin (§20) · 3. Shelf space (§21) — all three, in every
channel you sell in. 4. **Lines to be activated** (§22) — resets to zero every year.
5. Advertising campaign (§17) — no campaign means neutral positioning.

## Everything resets each year

Sales managers, all six salary fields, factoring, supplier terms, credit line, lines to
activate. Re-enter every one.

## Before submitting

Work through `year 2 - real thing/03-YEAR-2-DECISION-PLAYBOOK.md` section "Pre-submission".
The two that have actually cost money:

- **Raw material = production x 1.02** (exact). Entered by one person, checked by another.
- **OCR must be <= available cash** or the simulator borrows for you at 10%.

## House rules

- Never invent a number. Cite a `§` of the scenario, a result sheet, or a
  `model/calibration.py` call.
- Mark uncertainty `[!]` trap, `[+]` edge, `[~]` judgement call inside tables; emoji in
  prose only, never inside a table cell.
- Run `python3 model/align_tables.py <file>` after editing any document with tables.
