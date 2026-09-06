# Year 2 — graded round

Working folder for the graded run (simulation `B1SIM2C2`, Company 3, `COMPANY_3`).
**Year 1 results received — 1st of 5 on both rankings. Year 2 decisions entered.**

## Read in this order

| #   | File                                | What it is                                        | When you need it            |
| --- | ----------------------------------- | ------------------------------------------------- | --------------------------- |
| —   | `README.md`                         | this index                                        | start here                  |
| 00  | `00-CALIBRATION-CONSTANTS.md`       | the measured simulator constants, **32/32 exact** | before quoting any figure   |
| 01  | `01-DEMAND-MODEL.md`                | price anchors and elasticities, on graded Y1 data | before setting any price    |
| 02  | `02-YEAR-1-DECISIONS-AS-ENTERED.md` | Year 1 as filed, with the actual outcome          | for the CEO analysis        |
| 03  | `03-YEAR-3-DECISION-PLAYBOOK.md`    | the Year-3 plan and the entry checklist           | on the next decision day    |
| 04  | `04-RESULTS-INTAKE-CHECKLIST.md`    | what to do the hour Year-2 results arrive         | the moment they land        |
| 05  | `05-CEO-MEETING-AND-REPORT-PACK.md` | deck structure, rubric, standing answers          | before every meeting        |
| 06  | `06-OPEN-QUESTIONS.md`              | what is still unknown, and what is now settled    | when planning experiments   |
| 07  | `07-YEAR-2-DECISIONS-AS-ENTERED.md` | **Year 2 as filed** — the record                  | for the CEO analysis        |
| 08  | `08-YEAR-2-DECISION-REVIEW.md`      | **Year 2 graded, decision by decision**           | before the next CEO meeting |

## Where everything else lives

| Thing                                                | Path                                                             |
| ---------------------------------------------------- | ---------------------------------------------------------------- |
| Calibrated engine — **use this, not raw `mmt39.py`** | `model/calibration.py` (32 checks)                               |
| Scenario model, rulebook constants                   | `model/mmt39.py` (100 checks)                                    |
| Table aligner and consistency checker                | `model/align_tables.py`, `model/check_consistency.py`            |
| Year-1 graded result sheets                          | `DIR0114SI02083TE3Y1{DEP,REP,INV,INF}.pdf` and the two XLSX      |
| Full Year-1 analysis, competitor brief, model audit  | `anthony results + review/`                                      |
| Year-2 decision screen captures                      | `year 2 decisions (screenshots)/` — 23 files, 15 unique          |
| Test-round findings, with derivations                | `day 2 - real thing/FINDINGS FROM TEST FOR THE REAL RUN.md`      |
| Test-round result sheets                             | `day 1/year 1/DIR…Y1{DEP,REP,INV,INF}.pdf`                       |
| Skills that load automatically                       | `.claude/skills/mmt39-decisions`, `.claude/skills/mmt39-results` |

## Commands

```bash
python3 model/calibration.py                      # 32 checks vs the actual result sheets
python3 model/mmt39.py --selftest                 # 100 checks vs the rulebook
python3 model/align_tables.py "<file>.md"         # realign tables after editing
```

## The five rules that survived contact with the simulator

1. **Never invent a number.** Every figure traces to a `§` of the scenario, a result sheet, or
   a `model/calibration.py` call.
2. **Price first, plant second.** Capacity was never the binding constraint on moisturiser, and
   is now fixed for sunscreen. Price is the only large lever left.
3. **Two people check the raw-material field.** One mis-key cost second place in test Year 1.
4. **Only make what you can sell.** Year 1 built 32,175,000 units of moisturiser against demand
   of 15,047,394 and turned €41M of cash into stock.
5. **Vary one thing, in one market, at a time** — otherwise the year teaches you nothing.

## Where we are

| Metric                    | Year 1 actual | Year 2 forecast  | Change  |
| ------------------------- | ------------- | ---------------- | ------- |
| Net income                | €67,823,192   | €83,736,075      | +23.5%  |
| Position                  | **1 of 5**    | to defend        | —       |
| Loans outstanding         | €26,000,000   | **€0**           | prepaid |
| Moisturiser stock         | 17,628,699 u  | 6,900,086 u      | −60.9%  |
| Sunscreen demand unserved | 1,827,440 u   | ~608,000 u `[!]` | −67%    |

**Year-2 grade: B+.** Operations and finance excellent; pricing timid for the second year
running. Roughly €11.8M left on the table in two fields that cost nothing to type — see
`08-YEAR-2-DECISION-REVIEW.md`.

## Status

- [x] Year 1 decisions submitted — `02-YEAR-1-DECISIONS-AS-ENTERED.md`
- [x] Year 1 results received and analysed — `anthony results + review/`
- [x] Model recalibrated on graded data — 32/32 exact
- [x] Year 2 decisions entered — `07-YEAR-2-DECISIONS-AS-ENTERED.md`
- [x] Year 2 decisions reviewed and graded — `08-YEAR-2-DECISION-REVIEW.md`
- [ ] Year 2 results received → run `04-RESULTS-INTAKE-CHECKLIST.md`
- [ ] Year 3 decisions entered → `03-YEAR-3-DECISION-PLAYBOOK.md`
- [ ] CEO meeting deck → `05-CEO-MEETING-AND-REPORT-PACK.md`
- [ ] Final report — **due Friday 18 September 2026, 23:00**
