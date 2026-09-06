# 04 · Results intake — the first hour

Run this the moment the Year-1 reports arrive. Invoking the **`mmt39-results`** skill
walks the same path.

## 1 · Extract

```bash
cd "year 2 - the real thing"
for f in *.pdf; do pdftotext -layout "$f" "${f%.pdf}.txt"; done
```

Four reports: **DEP** what we submitted · **REP** results and statements · **INV** surveys
· **INF** the Director's factors. **Read INF first** — every forecast depends on it.

## 2 · Fill this table before discussing anything

Forecast column is the Year-2 central case from `07-YEAR-2-DECISIONS-AS-ENTERED.md`.

| Line                              | Forecast                  | Actual | Gap | Cause |
| --------------------------------- | ------------------------- | ------ | --- | ----- |
| S units produced                  | 6,688,800                 |        |     |       |
| S units sold                      | 6,688,800                 |        |     |       |
| **S units demanded of our brand** | **~7,296,800**            |        |     |       |
| H units produced                  | 3,344,400                 |        |     |       |
| H units sold                      | ~14,073,013               |        |     |       |
| **H units demanded, market A**    | **~4,005,762**            |        |     |       |
| **H units demanded, market B**    | **~9,989,807**            |        |     |       |
| H units sold on promotion         | ~1,247,000                |        |     |       |
| H finished goods, 31 December     | 6,900,086                 |        |     |       |
| Standard cost S / H               | 5.1358 / 2.2051           |        |     |       |
| Sales at MSRP                     | €205,879,597              |        |     |       |
| Net revenue                       | €179,097,864              |        |     |       |
| Gross profit                      | €109,885,934              |        |     |       |
| General expenses                  | €26,204,859               |        |     |       |
| Operating income                  | €83,681,075               |        |     |       |
| Financial income/expense          | **+€55,000**              |        |     |       |
| **Net income**                    | **€83,736,075**           |        |     |       |
| Depreciation                      | €7,200,000                |        |     |       |
| Loans outstanding, 31 December    | **€0**                    |        |     |       |
| Logistic stockout flags           | none expected `[!]`       |        |     |       |
| Transport cost per unit           | ~€0.042                   |        |     |       |
| Office / sales turnover           | 4 × €24,000 + 9 × €30,000 |        |     |       |
| Position on net income            | 1st, to defend            |        |     |       |

## 3 · Recalibrate, in this order

| Read                                  | Against                           | Tells you                                                         |
| ------------------------------------- | --------------------------------- | ----------------------------------------------------------------- |
| units produced / (nameplate × shifts) | **0.929**                         | **is SMED really worth 92.9%?** The one unverified constant `[!]` |
| RM used / units produced              | 1.02                              | is scrap still 2%                                                 |
| reported standard cost                | 5.1358 / 2.2051                   | do the power and repair constants hold at SMED utilisation        |
| **units demanded of your brand**      | 7,296,800 · 4,005,762 · 9,989,807 | **the elasticities — the most valuable lines on the sheet**       |
| units sold on promotion               | ~1,247,000                        | **what a promotion actually does** — first ever measurement       |
| A/S vs A/T channel volumes            | each other                        | the promotion effect, market A, with T as the control             |
| B/T and B/G channel volumes           | Year 1                            | market drift at an unchanged price — the clean control cell       |
| transport cost and flags              | `trunk_capacity()`                | did cutting to 42 last-mile vehicles flag `[!]`                   |
| surveys 11, 13, 14, 15                | our own settings                  | **why market A's moisturiser resists us** — the €12M/yr question  |
| survey 4                              | our channel mix                   | is channel G really winner-take-most                              |
| financial expenses                    | +€55,000                          | did the prepayment land as expected                               |

Then update the anchor table in `01-DEMAND-MODEL.md` and re-run
`python3 model/calibration.py`.

## 4 · The five questions Year 2 was designed to answer

| Question                                                  | Where the answer is                                                                  |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Does SMED really deliver 92.9%?**                       | units produced ÷ (nameplate × 3 shifts × lines). €6M of capex rests on it            |
| **What does a promotion actually do?**                    | "units sold on promotion", channel A/S and B/S, against A/T and B/T as controls      |
| **Why does market A's moisturiser resist us?**            | surveys 11 (insertions), 13 (POP), 14 (salesforce), 15 (shelf space achieved)        |
| How elastic is sunscreen?                                 | units demanded of our brand at 15.00 vs 7,677,440 at 14.50 — media and all else held |
| Did cutting the last mile to 42 vehicles flag a stockout? | the logistic stockout flags on REP p4                                                |

## 5 · Housekeeping

- Superseded figures go to `SUMMARIES.txt` Appendix A, never deleted (project rule 4).
- Re-run `python3 model/align_tables.py` on any document edited.
- Record what changed and when — the record of the change *is* part of the CEO analysis.
