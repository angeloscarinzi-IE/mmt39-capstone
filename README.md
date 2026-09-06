# MMT39 Capstone — Team Intelligence Pack

**IE MIM Dual Degrees Capstone · Scenario MMT39 · Praxis MMT simulator**

Everything here is derived from `Scenario MMT39 .pdf` and the evaluation guidelines.
Every figure carries its rulebook section (`§`) and reproduces from the model. Nothing is invented.

---

## Start here

| If you have…              | Read                                               |
| ------------------------- | -------------------------------------------------- |
| **5 minutes**             | `MASTER-PLAN.txt` → Part 0 (the 90-second version) |
| **20 minutes**            | `MASTER-PLAN.txt` Parts 0-3                        |
| **Before a team meeting** | `MASTER-PLAN.txt` end to end                       |
| **An hour**               | Doc 01 §§3, 4, 8 → then Doc 02                     |
| **A decision to make**    | Doc 03 Part A, then run the model                  |
| **A CEO meeting**         | Doc 03 Part B + `SUMMARIES.txt` Appendix C         |

---

## What's in here

| File                                                 | What it is                                                                                                         | Lines |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----- |
| `MASTER-PLAN.txt`                                    | **THE ONE TO READ.** Everything united: strategy, numbers, traps, Year-1 plan, meeting agenda                      | 881   |
| `RUN-ME.command`                                     | Double-click in Finder to see the briefing — no Terminal needed                                                    | 17    |
| `SUMMARIES.txt`                                      | **Plain-text digest.** Every finding, all corrections, the questions for the Director, and a one-page number sheet | 552   |
| `docs/00-how-to-use-the-model.md`                    | How to run the model, what it produces, 17 actions                                                                 | 451   |
| `docs/01-company-and-market-dossier.md`              | **The master reference.** Every scenario fact, in decision order, with a verdict on each                           | 440   |
| `docs/02-edge-and-battle-plan.md`                    | 8 blind spots rivals will have, the counter to each, the 4-year plan, team split                                   | 240   |
| `docs/03-decision-checklist-and-grading-playbook.md` | Every simulator field + the CEO deck the rubric rewards                                                            | 311   |
| `model/mmt39.py`                                     | The decision model. 89 self-tests                                                                                  | 2,650 |
| `model/align_tables.py`                              | Re-aligns markdown tables after any edit                                                                           | 90    |
| `model/check_consistency.py`                         | Checks every figure agrees with the model and with itself across all documents                                     | 110   |

Source PDFs stay in the root folder.

---

## Running the model

```bash
cd "/Users/angelo/Desktop/Projects & Certificates & Work/Projects/CAPSTONE Project MIM"

python3 model/mmt39.py --briefing      # every headline number, one page
python3 model/mmt39.py --demo          # worked year: P&L, balance sheet, ratios
python3 model/mmt39.py --lines         # line economics at 1, 2, 3 shifts
python3 model/mmt39.py --media         # advertising cost per point of reach
python3 model/mmt39.py --promotions 6  # promotion costs at a €6.00 price
python3 model/mmt39.py --breakeven 2.13 0.95 0.60
python3 model/mmt39.py --selftest      # 89 checks against the rulebook
```

No installation needed. Python 3.9+, zero dependencies.

**When the Director changes a rate** (FX, raw material cost, interest rates — §28, §46, §49), edit
the `SCENARIO` block at the top of `mmt39.py` and re-run. Nothing else needs touching.

---

## The five things that matter most

1. **Capacity is the constraint, not demand.** The maximum legal factory serves ~34% of the
   moisturiser market. Every plan is a choice about *which* demand to serve.
2. **Real capacity is 78.75% of the headline figure** (§23, §24). Plan on 184,800 per S line-shift
   and 462,000 per H line-shift, never 240,000 / 600,000.
3. **Moisturiser is 3.5× more capital-efficient and 2.4× cheaper than sunscreen** — and the choice is
   irreversible, made in year 1, carried for four years (§22).
4. **Only 10% of your grade is the simulated result.** 65% is analysis quality, presentation and peer
   feedback. Demonstrably knowing *why* the market moved beats winning it.
5. **Several "obviously good" decisions destroy value here.** Poka Yoke pays back in 12.3 years.
   Social media costs 67% more per point of reach than TV. The rulebook's own logistics benchmark
   costs 36% more than achievable.

---

## Before Session 2 — four questions for the Director

Ranked by how much money the answer moves. Full context in `SUMMARIES.txt` Appendix B.

1. **How many production lines can one SMED duplicate module serve?**
   Swings SMED between a 14.4-year and a 1.8-year payback.
2. **Does Poka Yoke carry any benefit beyond scrap and repair time?**
   On the documented effects alone it should be skipped.
3. **§18 says eight promotion types but lists six — what are the other two?**
4. **§42: what proportion of the loan balance repays each year?**
   Undefined in the scenario; it changes every cash forecast.

---

## Verification

All figures are checked automatically, not by eye:

| Check                                                     | Result                      |
| --------------------------------------------------------- | --------------------------- |
| Calibration against the actual result sheets              | **32 of 32, exact**         |
| Model self-tests against the rulebook                     | **100 passing**             |
| Figures in docs matching the model                        | **all verified**            |
| Same figure agreeing across every document                | **all consistent**          |
| Superseded figures appearing only in labelled corrections | **confirmed**               |
| Markdown table alignment                                  | **58 tables, 0 misaligned** |

Re-run any time with `python3 model/calibration.py` and `python3 model/mmt39.py --selftest`.

---

## Conventions

- Verdict markers: `[!]` trap · `[+]` edge · `[~]` judgement call
- `§` refers to a numbered section of `Scenario MMT39 .pdf`
- Superseded figures are never deleted — they're kept in `SUMMARIES.txt` Appendix A so nobody quotes
  an old number in a CEO meeting

---

*Built from the source PDFs before Session 2. AI assistance was used to compute and structure this
material; every figure traces to a numbered section of the scenario and is reproducible from
`model/mmt39.py`.*

---

## Current state — 6 September 2026

Test round complete (2 virtual years). Graded round **Year 1 results received — 1st of 5 on
both rankings, net income €67,823,192.** Year 2 decisions entered; results pending.

| Start here                                                  | For                                                        |
| ----------------------------------------------------------- | ---------------------------------------------------------- |
| `year 2 - the real thing/README.md`                         | everything from Year 2 onward — the working index          |
| `year 2 - the real thing/08-YEAR-2-DECISION-REVIEW.md`      | the Year-2 decisions, graded, with the money behind each   |
| `year 2 - the real thing/00-CALIBRATION-CONSTANTS.md`       | the measured constants, now exact against the real report  |
| `year 2 - the real thing/anthony results + review/`         | the full Year-1 results analysis and competitor brief      |
| `day 2 - real thing/FINDINGS FROM TEST FOR THE REAL RUN.md` | what the test round measured (superseded where they clash) |
| `model/calibration.py`                                      | the calibrated engine. **Outranks `model/mmt39.py`**       |

Two Claude Code skills load automatically: `mmt39-decisions` for building a year's sheet,
`mmt39-results` for processing a results sheet.
