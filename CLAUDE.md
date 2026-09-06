# CLAUDE.md — MMT39 Capstone

Project-specific conventions. Global preferences live in `~/.claude/CLAUDE.md`.

## What this project is

IE MIM Dual Degrees Capstone: a business simulation (Praxis MMT 39) where student teams each run a
skincare company selling sunscreen (**S**) and moisturiser (**H**) across three markets (**A**, **B**
domestic in euros; **E** export in dollars).

**Critical framing:** MMT39 is *not* a real company. Every team starts from an identical balance
sheet (§1: €12M fixed assets + €54M cash = €66M equity, no debt, no products). There is no incumbent
advantage to research. Analysis must therefore target **traps in the rules** and **arithmetic other
teams skip**, never a fictional company history.

**Structure:** ungraded test round (2 virtual years), then a graded round (4 virtual years) with 3
CEO meetings and a final report.

## Repository layout

```
README.md                  Index — start here
SUMMARIES.txt              Plain-text digest, corrections, Director questions, number sheet
docs/00-…-model.md         How to run the model
docs/01-…-dossier.md       Master reference: every scenario fact + verdict
docs/02-…-battle-plan.md   Blind spots, counters, 4-year plan, team split
docs/03-…-playbook.md      Decision checklist + CEO deck skeleton
model/mmt39.py             The decision model (89 self-tests)
*.pdf                      Source material — never edit
```

## Non-negotiable rules for this project

**1. Never invent a number.** Every quantitative claim must trace to a numbered section of
`Scenario MMT39 .pdf` (cited as `§22`, `§41`…) or be computed by `model/mmt39.py`. This is a graded
academic deliverable; a fabricated figure is worse than a missing one.

**2. Verify before writing.** Run figures through the model *before* putting them in a document, then
re-verify after. Two arithmetic errors were caught this way that would otherwise have shipped.

**3. Name ambiguity, never paper over it.** Where the scenario is silent or contradictory, mark it
`ASSUMPTION` in code with the reasoning, implement both readings where possible, and default to the
**conservative** one. Over-promising production causes stockouts, and §34 says the brand damage
outlives the year.

**4. Superseded figures are never deleted.** They move to `SUMMARIES.txt` Appendix A with old and new
side by side, so nobody quotes a stale number in a CEO meeting. Appendix A now carries 16 entries;
items 6-16 are the graded-round recalibration.

**5. All scenario constants live in one place** — the `SCENARIO` dict at the top of `mmt39.py`, each
with its `§` reference. The Director changes FX, raw material costs and interest rates during the
course; edit that block only.

## Working conventions learned on this repo

- **Decisions arrive as WhatsApp screenshot dumps** (`*/decisions taken/`,
  `*/year N decisions (screenshots)/`) with heavy duplication — 23 files, 15 unique in Year 2.
  Deduplicate by hash before reading, then transcribe every form into a numbered
  `NN-YEAR-N-DECISIONS-AS-ENTERED.md` so results can be traced to a specific field.
- **This repo is public on GitHub.** Never commit Praxis course PDFs, simulator report sheets
  (`DIR*.pdf`, `DIR*.XLSX`) or decision-screen captures — `.gitignore` covers them, and commit
  514d353 exists because they were published once by accident. Team-authored PDFs are fine.
- **Each virtual year gets two documents**, not one: the record of what was entered, and a
  graded review of whether it was right, with the euro value behind every grade.

## Document conventions

- Verdict markers: `[!]` trap · `[+]` edge · `[~]` judgement call. Use `[!]`/`[+]`/`[~]` **inside
  tables** (emoji break pipe alignment) and ⚠️/✅/⚖️ in prose.
- **Tables over prose.** These are working references consulted under time pressure, not essays.
- Keep documents short. Convert complex rules into a table plus a verdict line.
- Every document ends with its sources.

## Verification commands

```bash
python3 model/calibration.py          # 32 checks against the ACTUAL result sheets
python3 model/mmt39.py --selftest     # 100 checks against the rulebook
python3 model/mmt39.py --briefing     # regenerate every headline figure
```

**`model/calibration.py` outranks `model/mmt39.py`.** Its constants were fitted to real
result sheets; `mmt39.py`'s were inferred from the scenario and several are wrong
(utilisation, scrap, standard cost, depreciation base). Where they disagree, calibration
wins. Since 6 September 2026 it is fitted to the **graded** Year-1 sheet (`B1SIM2C2`) and
reproduces that report to the euro. Provenance:
`day 2 - real thing/FINDINGS FROM TEST FOR THE REAL RUN.md` and
`year 2 - the real thing/00-CALIBRATION-CONSTANTS.md`.

After editing any document, re-run the table aligner and the consistency checker (both padding by
**character count**, not display width — table cells must contain no emoji or wide characters).

## Key figures (recompute rather than trust this list)

|                            |                                                                    |
| -------------------------- | ------------------------------------------------------------------ |
| Market size, units/yr      | S 56,200,000 · H 131,260,000                                       |
| Real line utilisation      | **81.25%** measured (92.9% with SMED) — see `model/calibration.py` |
| Sellable, per line-shift   | S 195,000 · H 487,500                                              |
| Standard cost              | S €5.5604 · H €2.3252 at 120-day supplier terms — **exact**        |
| Capex per unit of capacity | S €3.59 · H €1.03 at 3 shifts                                      |
| Raw material to purchase   | production × **1.02** exactly, less opening stock                  |
| Cheapest advertising       | Television, in both markets                                        |
| Cheapest logistics         | €0.0044/unit (benchmark €0.006 is a decoy)                         |
| Grading                    | 40% individual · 25% team · 15% peer · 10% report · 10% results    |

## Academic integrity

The syllabus permits GenAI for research and for structuring presentations, but discourages it for
analysis and drafting, and requires acknowledgement. `README.md` carries that acknowledgement.
Everything here is computed and traceable — the team must understand and be able to defend each
figure independently, since the CEO grades on the defence, not the deck.
