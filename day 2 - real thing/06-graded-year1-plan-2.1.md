# 06 — Graded Year 1 entry sheet (Plan 2.1)

**Status:** graded run, Year 1 of 4. Fresh §1 balance sheet: €12,000,000 fixed assets, €54,000,000
cash, €66,000,000 equity, no lines, no stock, no debt. Written 2026-09-06 for a ~60-minute entry
session. Every figure traces to a `§` of `Scenario MMT39 EN v231.pdf`, a test-round result document,
or a `model/mmt39.py` call (the script that produced every model figure below is reproducible from
the calls named in the Source column).

Markers: `[!]` trap · `[+]` edge · `[~]` judgement call. No emoji inside tables.

Decisions taken by the team before this sheet was written (stated, not relitigated): all 32 lines
installed **and activated** in Year 1, sunscreen-heavy mix; fleet sized by tonnage so both legs
clear in A and B; loan sized to the real cash trough, not €100M; no factoring; S raw material at
production x 1.02 x 1.05, H at production x 1.02 only; **exit E** for Year 1; surveys 20/21/22 + the
€11,000 bundle + 3/7/8; selection and training ON; promotions in A and B; TV-led media with B matched
to A; no SMED in Year 1; no Poka Yoke.

---

## The sheet in ten lines

| #   | Item                        | Value                                                                                                        | Source                                                                       |
| --- | --------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| 1   | Lines                       | **12 S + 20 H = 32**, all installed and activated this year. Capex €55,200,000                               | §22; 12 x 2,100,000 + 20 x 1,500,000                                         |
| 2   | Shifts / maintenance        | **3 shifts**, preventive maintenance ON, Poka Yoke OFF, SMED 0 (not purchasable in Y1)                       | §23, §25, §26, §27                                                           |
| 3   | Planned output              | **S 6,970,320 · H 29,043,000** sellable (81.20% of nameplate)                                                | `capacity(12, 20, 3, preventive=True)`                                       |
| 4   | Raw material to buy         | **S 7,518,420 · H 29,835,000** units, 120-day terms on both                                                  | S = 12x3x195,000 x1.02x1.05; H = 20x3x487,500 x1.02 (test-Y1 per line-shift) |
| 5   | Prices (MSRP), all channels | **S 14.50** in A and B · **H 5.25 in A, 7.75 in B** · margins S 1.90 / H 0.95 · shelf S 18% / H 20%          | Test Y2 DEP p4-p5 (only price points with demand evidence)                   |
| 6   | Sales network               | 6 managers A, 6 B, **0 E**. Reps per zone A: S 4 / T 4; B: S 5 / T 3. Fixed 27,000, variable 0.60%           | §6, §13; Doc 04 Part 4 #6                                                    |
| 7   | Fleet                       | Platforms 12 A / 12 B. Trunk **3 veh A, 2 veh B @ 24,000 kg**. Last mile **30 A, 20 B @ 10,000 kg**          | §10, §12; `plan_platform_to_retailer()`; stockout-flag arithmetic (2.3)      |
| 8   | Media                       | Campaign 18 (S) / 19 (H). S: PR 4 + TV 8 per market; H: PR 3 + TV 5 per market. Total €678,000 + POP €48,000 | Test Y2 DEP p5-p6, B matched to A                                            |
| 9   | Finance                     | **Loan €25,000,000** + **credit line €10,000,000**, deposits 0, factoring NO, customer terms 60 days         | §41-§44; cash trough -21,737,713 in month 2 (section 4)                      |
| 10  | Expected Year-1 net income  | **€110,187,386** from the model; ~€109,000,000 after three known model corrections (section 4.3)             | `Simulation.run_year()`; test Y2 actual for scale: 87,103,307                |

`[!]` Line 10 assumes 100% sell-through of planned output at the Year-2 test prices. The test-Y2
demand readings that support it: S 5,536,395 at 14.50 with B starved of media (3 insertions vs 12 in
A); H 35,881,291 at 5.25/7.75. Planned S output 6.97M sits between that and the test-Y1 demand of
9,199,028 at ~11.00; planned H output 29.04M is **below** both H readings, so H should sell out.

---

## 4-year trajectory (model, base case)

Flat volumes, flat prices, no E, no SMED, loan repaid one third per year. `Simulation` run with the
Year-1 plan below repeated in Years 2-4, surplus cash moved to fixed-term deposits each year keeping a
€10,000,000 cash buffer.

| Year | Lines (S/H) | Units S   | Units H    | Revenue (MSRP) | Net income  | Cash + deposits (31 Dec) | Loan balance | Repaid 2 Jan |
| ---- | ----------- | --------- | ---------- | -------------- | ----------- | ------------------------ | ------------ | ------------ |
| 1    | 12 / 20     | 6,970,320 | 29,043,000 | 285,160,336    | 110,187,386 | 108,614,487              | 25,000,000   | 0            |
| 2    | 12 / 20     | 6,970,320 | 29,043,000 | 285,160,336    | 112,694,415 | 221,039,569              | 16,666,667   | 8,333,333    |
| 3    | 12 / 20     | 6,970,320 | 29,043,000 | 285,160,336    | 113,005,042 | 333,775,277              | 8,333,333    | 8,333,333    |
| 4    | 12 / 20     | 6,970,320 | 29,043,000 | 285,160,336    | 116,656,768 | 450,162,712              | 0            | 8,333,333    |

Accumulated profit, 4 years: **452,543,610**. Financial expense peaks at 2,500,000 (Year 2 interest on
the full €25M); financial income reaches 7,886,049 by Year 4 on deposits. Debt never exceeds 25M
against a Year-1 closing cash of 108.6M, so Year-1 borrowing cannot choke Years 3-4.

**Build path and decision points**

| Year | Capex                                    | Decision gate                                                                                                                                                                                          | Marker |
| ---- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| 1    | 32 lines, €55,200,000 (this sheet)       | None left: the §22 cap is reached. Mix 12/20 is locked for four years                                                                                                                                  | `[!]`  |
| 2    | 2 SMED modules, €6,000,000, if justified | Buy only if the Year-1 REP "Units demanded of your brand" line is > 0 for S or H (unserved demand exists). Model: +14.5% output, +38,977,888 accumulated profit over Years 2-4 if the extra units sell | `[~]`  |
| 2    | Poka Yoke: no                            | 12.3-year payback (Doc 00 §3.6); never inside a 4-year game                                                                                                                                            | `[+]`  |
| 3    | E: last sensible entry year              | Enter only if Year-2 surveys 17/18 show a price point below the local brands and A+B demand is below capacity. A Year-4 entry cannot pay back the 720,000 sales network                                | `[~]`  |
| 2-4  | None otherwise                           | Everything else on this sheet is a yearly lever (next table)                                                                                                                                           |        |

**Irreversible over four years vs adjustable every plan**

| Irreversible                                                         | §        | Adjustable each year                                            | §        |
| -------------------------------------------------------------------- | -------- | --------------------------------------------------------------- | -------- |
| Lines installed: cannot be removed, 32 total cap, 12/20 mix fixed    | §22      | Shifts (1-3), lines activated                                   | §22, §23 |
| Poka Yoke (once, all lines)                                          | §26      | Preventive maintenance, training department                     | §25, §32 |
| SMED modules once bought                                             | §27      | Prices, margins, shelf, campaign, media, promotions, POP        | §14-§21  |
| Brand damage from a finished-goods stockout carries into later years | §34      | Platforms (rented), vehicles, managers, reps, salaries          | §10-§13  |
| Loan: 3-year commitment, one third leaves cash every 2 January       | §42, §47 | Credit line (1 year), deposits (1 year), surveys, payment terms | §43, §44 |

`[!]` Sales managers reset to zero every year (Doc 04 Part 6). Re-enter 6/6/0 in every plan.

---

## Form 1 — Commercial distribution

| Field          | A | B | E | Source                                                                       |
| -------------- | - | - | - | ---------------------------------------------------------------------------- |
| Sales managers | 6 | 6 | 0 | §6 (50,000 each in A/B). E exit: 0 managers, no E price, no E media (below) |

`[~]` **To enter E instead** (team can overrule): 12 managers $720,000 + test-Y2 E media $236,000 +
POP 60,000 + 3 trunk vehicles $158,400 + 12 last-mile vehicles $432,000 = **$1,606,400** for
the 112,814 units E produced in test Y2 (**$14.24 per unit**), against three local brands spending
$8,000,000 each on media (survey 12). Source: Doc 05 §6.3 and §7.2; `vehicle_annual_cost()`.

## Form 2 — Logistics

| Field                                      | A      | B      | E                    | Source                                                                                                    |
| ------------------------------------------ | ------ | ------ | -------------------- | --------------------------------------------------------------------------------------------------------- |
| Platforms                                  | 12     | 12     | 12 (form minimum)    | §10 allowed values. 12 is the tested configuration; §11 platform cost is per order/unit, not per platform |
| Transport to platforms: number of vehicles | **3**  | **2**  | 1 (form minimum)     | Section 2.3 below                                                                                         |
| Transport to platforms: load capacity (kg) | 24,000 | 24,000 | 1,000 (form minimum) | §10 max; cheapest per unit at full load, 0.0044 (`--vehicles`)                                            |
| Transport to retailers: number of vehicles | **30** | **20** | 1 (form minimum)     | `plan_platform_to_retailer(20,374,889, "A", 12, 3815)` = 30; `(15,895,111, "B", 12, 2190)` = 20           |
| Transport to retailers: load capacity (kg) | 10,000 | 10,000 | 500 (form minimum)   | §12 max                                                                                                   |

`[!]` §13: "Values of zero may not be entered in logistics decisions." E is exited by leaving the
E **price** blank (§15: no price = not commercialising), not by zeroing logistics. Test Y1 provisioned
60 platforms and 40 vehicles in E with no E price and no E vehicle cost appeared in the P&L (trunk cost
48,155 total against 86,400 of A+B planned rentals), so the minimum entries above should cost nothing;
if charged, 1 x (24,000 + 1,200) + 1 x (24,000 + 600) = $49,800. Open question 1.

### 2.3 Why these vehicle counts — the trunk leg is pure arithmetic

One vehicle at load L kg moves 2L units per route, 2,000 / 8 = 250 routes a year (§10). Four test
flags confirm it exactly:

| Test year / market | Trunk fleet | Capacity units | Units shipped | Flag (REP p4) | Check |
| ------------------ | ----------- | -------------- | ------------- | ------------- | ----- |
| Y1 A               | 1 @ 17,000  | 8,500,000      | 6,340,088     | No            | `[+]` |
| Y1 B               | 1 @ 15,000  | 7,500,000      | 8,089,912     | **Yes**       | `[+]` |
| Y2 A               | 2 @ 20,000  | 20,000,000     | 20,934,924    | **Yes**       | `[+]` |
| Y2 B               | 2 @ 22,000  | 22,000,000     | 12,178,692    | No            | `[+]` |

Planned volume by market (S split 55/45 after matching B media; H split by the test-Y2 sold shares
56.5/43.5): **A 20,374,889 · B 15,895,111**.

| Market | Vehicles @ 24,000 kg | Capacity   | Headroom over plan | Annual cost | Source                      |
| ------ | -------------------- | ---------- | ------------------ | ----------- | --------------------------- |
| A      | 3                    | 36,000,000 | +77%               | 158,400     | 3 x (24,000 + 1.2 x 24,000) |
| B      | 2                    | 24,000,000 | +51%               | 105,600     | 2 x 52,800                  |

`[+]` Two vehicles would cover A on paper (24.0M vs 20.4M), but test Y2 stocked out at 20.93M on
20.0M of capacity with an identical S/H pattern. The third vehicle is €52,800 against the €27,206,904 of
gross profit Doc 05 attributes to the fleet failure.

**Last mile** has no closed-form rule in §12 (route time "can be any"). Evidence bounds it: test Y2
B stocked out with 10 vehicles @ 10,000 kg on 12,178,692 units, so one vehicle moves **fewer than
1,217,870 units a year**. The model's §8 geometry at 12 platforms gives 679,163 (A) and 794,756 (B)
units per vehicle, hence 30 and 20. Never plan below the evidence floor: A 17, B 14. Cost of 50
vehicles: 50 x 36,000 = **1,800,000**, against the test-Y2 last-mile bill of 2,103,519 that still
stocked out in both markets.

## Form 3 — Human resources

| Field                               | Value   | Source                                                                 |
| ----------------------------------- | ------- | ---------------------------------------------------------------------- |
| Level I                             | 126,000 | §29 range 108,000-150,000; test Y1/Y2 value                            |
| Level II                            | 84,000  | §29 range 72,124-99,170; test value                                    |
| Level III                           | 60,000  | §29 range 51,100-72,124; test value                                    |
| Level IV                            | 35,000  | §29 range 30,050-42,075; test value                                    |
| Operator                            | 13,500  | §30 range 12,000-16,830; test value                                    |
| Specialist                          | 24,000  | §30 range 21,000-29,450; test value                                    |
| Recruitment and training department | **Yes** | §32, €722,000. Turnover cost 306,000 (Y1) and 276,000 (Y2) with it off |

Office payroll at these levels: **2,818,000** (test Y2 REP p5, reproduced by `office_payroll()`).
Production headcount at 32 lines x 3 shifts: 684 specialists + 2,532 operators = **3,216**, payroll
50,598,000 (`production_headcount()`, §30).

| Sales reps per zone | Channel S | Channel T | Source                                                                     |
| ------------------- | --------- | --------- | -------------------------------------------------------------------------- |
| A                   | 4         | 4         | Test Y2 (A took 51.9% S / 68.6% H share)                                   |
| B                   | **5**     | **3**     | Doc 04 Part 4 #6: B supermarkets are 36-38% of volume, staffed 2/2 in test |

| Sales force salary | Fixed (€) | Variable (%) | Source                                     |
| ------------------ | --------- | ------------ | ------------------------------------------ |
| A                  | 27,000    | 0.60         | §13 range 21,000-42,000 / 0.6-1.2; test Y2 |
| B                  | 27,000    | 0.60         | same                                       |

Sales network cost: managers 600,000 + reps 2 x 6 zones x 8 reps x 27,000 = **3,192,000** fixed;
variable 0.60% of price-to-retailer on normal units in S and T, model estimate 1,191,006.

## Form 4 — Market research surveys

| Survey     | Content                                | Cost        | Select | Source                                               |
| ---------- | -------------------------------------- | ----------- | ------ | ---------------------------------------------------- |
| 1          | Sales of S by market                   | 3,000       | Yes    | €11,000 bundle (Doc 00 §3.9)                         |
| 2          | Sales of H by market                   | 3,000       | Yes    | bundle                                               |
| 3          | Sales of S and H by company and market | 36,000      | Yes    | Doc 05 §6.4: only way to compute a rival's share     |
| 7          | Positioning of S brands                | 59,900      | Yes    | Doc 05 §6.4: campaign IDs are meaningless without it |
| 8          | Positioning of H brands                | 59,900      | Yes    | same                                                 |
| 20         | Rivals' retail prices                  | 0           | Yes    | free                                                 |
| 21         | Rivals' campaigns                      | 0           | Yes    | free                                                 |
| 22         | Rivals' promotion types                | 0           | Yes    | free                                                 |
| 23         | Net income by company                  | 1,000       | Yes    | bundle                                               |
| 27         | Platforms by company and market        | 3,000       | Yes    | bundle                                               |
| 28         | Shifts by company                      | 1,000       | Yes    | bundle                                               |
| 19         | Demand for normal units                | 110,000     | **No** | REP prints unserved demand free (Doc 05 §5.2)        |
| all others | —                                      | —           | No     |                                                      |
| **Total**  |                                        | **166,800** |        | `research_cost([1,2,3,7,8,23,27,28])`                |

## Form 5 — Product S: price, margin, shelf, promotions

| Market | Channel | M.S.R.P. (€) | Margin (€) | Shelf space (%) | Promotion                | Number | Detail | Source                                  |
| ------ | ------- | ------------ | ---------- | --------------- | ------------------------ | ------ | ------ | --------------------------------------- |
| A      | G       | 14.50        | 1.90       | 18              | Direct promotional bonus | 1      | 2      | Price/margin/shelf: test Y2 DEP p4      |
| A      | S       | 14.50        | 1.90       | 18              | Direct promotional bonus | 1      | 2      | Promotion: only tested setting (Y2 H/E) |
| A      | T       | 14.50        | 1.90       | 18              | Direct promotional bonus | 1      | 2      |                                         |
| B      | G       | 14.50        | 1.90       | 18              | Direct promotional bonus | 1      | 2      |                                         |
| B      | S       | 14.50        | 1.90       | 18              | Direct promotional bonus | 1      | 2      |                                         |
| B      | T       | 14.50        | 1.90       | 18              | Direct promotional bonus | 1      | 2      |                                         |
| E      | G       | **blank**    | blank      | blank           | No promotion             | 0      | 0      | §15: no price = not commercialising     |

`[+]` Direct bonus is the cheapest promotion at 14.50: 0.40/unit, 2.8% of price (`--promotions 14.50`);
the one run in test Y2 cost 0.60/unit and moved 85,714 units, 81% of that market's H volume. One
promotion per channel (not three) keeps the §48 supply test easy: S has 1.4M units of headroom over
the test-Y2 demand reading.

| POP advertising (€) | A G   | A S   | A T   | B G   | B S   | B T   | E G | Source                                  |
| ------------------- | ----- | ----- | ----- | ----- | ----- | ----- | --- | --------------------------------------- |
| S                   | 3,000 | 3,000 | 3,000 | 3,000 | 3,000 | 3,000 | 0   | Test Y2 DEP p5; §19 cap 500,000/channel |

| Advertising campaign S | A  | B  | E | Source                                       |
| ---------------------- | -- | -- | - | -------------------------------------------- |
| Campaign               | 18 | 18 | 0 | Test Y2 DEP p5; A took 51.9% S share with it |

| Advertising repetitions S | A: No. | A: Cost (€) | B: No. | B: Cost (€) | E: No. | Source                                             |
| ------------------------- | ------ | ----------- | ------ | ----------- | ------ | -------------------------------------------------- |
| DR Display                | 0      | 0           | 0      | 0           | 0      |                                                    |
| PR Press                  | 4      | 60,000      | 4      | 60,000      | 0      | §15 rate 15,000; B matched to A (Doc 05 §6.3)      |
| RA Radio                  | 0      | 0           | 0      | 0           | 0      |                                                    |
| SM Social media           | 0      | 0           | 0      | 0           | 0      | Dearest per reach point, 500 vs TV 300 (`--media`) |
| TV Television             | 8      | 144,000     | 8      | 144,000     | 0      | §15 rate 18,000; cheapest reach (`--media`)        |
| **Total**                 | 12     | **204,000** | 12     | **204,000** | 0      |                                                    |

## Form 6 — Product H: price, margin, shelf, promotions

| Market | Channel | M.S.R.P. (€) | Margin (€) | Shelf space (%) | Promotion    | Number | Detail | Source                            |
| ------ | ------- | ------------ | ---------- | --------------- | ------------ | ------ | ------ | --------------------------------- |
| A      | G       | 5.25         | 0.95       | 20              | No promotion | 0      | 0      | Test Y2 DEP p5 (68.6% share in A) |
| A      | S       | 5.25         | 0.95       | 20              | No promotion | 0      | 0      |                                   |
| A      | T       | 5.25         | 0.95       | 20              | No promotion | 0      | 0      |                                   |
| B      | G       | 7.75         | 0.95       | 20              | No promotion | 0      | 0      | Test Y2 DEP p5 (55.1% share in B) |
| B      | S       | 7.75         | 0.95       | 20              | No promotion | 0      | 0      |                                   |
| B      | T       | 7.75         | 0.95       | 20              | No promotion | 0      | 0      |                                   |
| E      | G       | **blank**    | blank      | blank           | No promotion | 0      | 0      | §15                               |

`[~]` No H promotion: planned H output 29,043,000 is already below the test-Y2 demand reading of
35,881,291, and §48 rejects a promotion whose demand cannot be supplied. The H price in A is open
question 3.

| POP advertising (€) | A G   | A S   | A T   | B G   | B S   | B T   | E G | Source         |
| ------------------- | ----- | ----- | ----- | ----- | ----- | ----- | --- | -------------- |
| H                   | 5,000 | 5,000 | 5,000 | 5,000 | 5,000 | 5,000 | 0   | Test Y2 DEP p6 |

| Advertising campaign H | A  | B  | E | Source          |
| ---------------------- | -- | -- | - | --------------- |
| Campaign               | 19 | 19 | 0 | Test Y2 DEP p6  |

| Advertising repetitions H | A: No. | A: Cost (€) | B: No. | B: Cost (€) | E: No. | Source                          |
| ------------------------- | ------ | ----------- | ------ | ----------- | ------ | ------------------------------- |
| DR Display                | 0      | 0           | 0      | 0           | 0      |                                 |
| PR Press                  | 3      | 45,000      | 3      | 45,000      | 0      | §15; test Y2 A and B were equal |
| RA Radio                  | 0      | 0           | 0      | 0           | 0      |                                 |
| SM Social media           | 0      | 0           | 0      | 0           | 0      |                                 |
| TV Television             | 5      | 90,000      | 5      | 90,000      | 0      | §15                             |
| **Total**                 | 8      | **135,000** | 8      | **135,000** | 0      |                                 |

Media total S + H: **678,000**. POP total: **48,000**.

## Form 7 — Production

| Field                      | H              | S             | Source                                                                    |
| -------------------------- | -------------- | ------------- | ------------------------------------------------------------------------- |
| Lines previously installed | 0              | 0             | §1 fresh start                                                            |
| Lines installed this year  | **20**         | **12**        | §22, 32-line cap; sunscreen-heavy vs test 24/8                            |
| Total lines                | 20             | 12            |                                                                           |
| Active lines               | **20**         | **12**        | §22: new lines run at full capacity in their first year; A0 silent killer |
| Stock in units of RM       | 0              | 0             | §1                                                                        |
| Stock in units of FP       | 0              | 0             | §1                                                                        |
| Units purchased of RM      | **29,835,000** | **7,518,420** | H = 20 x 3 x 487,500 x 1.02; S = 12 x 3 x 195,000 x 1.02 x 1.05           |

`[!]` Raw material arithmetic. Test Y1 with preventive maintenance and no SMED produced exactly
195,000 S and 487,500 H per line-shift (REP p4: 780,000 / 4 and 13,650,000 / 28), 1.055x the bare
184,800 / 462,000 plan-on figures; the model's `capacity()` gives 193,620 / 484,050 (81.20%). Scrap
consumed material at exactly 1.020000 in Y1 (§34). S carries a further 5% because the test-Y2 S
shortfall of 442,600 units was sourced at a premium (Doc 05 §7.1); H carries none because the test-Y1
over-order locked €109,431,358 (Doc 04 §1.5). Raw material cost at list: S 12,405,393 + H 31,326,750
= **43,732,143** (§49 rates 1.65 / 1.05).

| Production options      | Value  | Source                                                    |
| ----------------------- | ------ | --------------------------------------------------------- |
| Number of shifts        | **3**  | §23; depreciation 12% (§35)                               |
| Preventive maintenance  | Yes    | §25, 500,000; +3.1% output on 32 lines (81.20% vs 78.75%) |
| Pokayoke previous years | No     |                                                           |
| Pokayoke                | **No** | §26; 12.3-year payback (Doc 00 §3.6)                      |

| SMED                             | Value | Source                           |
| -------------------------------- | ----- | -------------------------------- |
| SMEDs previous years             | 0     |                                  |
| To acquire                       | **0** | §27: not available before year 2 |
| Total SMED                       | 0     |                                  |
| Active                           | 0     |                                  |
| Teams assigned to SMED per shift | 0     |                                  |

Standard cost the model expects at these settings: **S 5.3217 · H 2.1718** (`standard_cost()` with
preventive, salaries 24,000 / 13,500). Test Y1 actuals on the same configuration at two shifts:
S 5.5371 / H 2.1788.

## Form 8 — Finance

| Field                        | Value          | Source                                                                                |
| ---------------------------- | -------------- | ------------------------------------------------------------------------------------- |
| Loan requested               | **25,000,000** | Section 4: month-2 trough -21,737,713 + 3,262,287 buffer (15.0%)                      |
| Loan prepayment              | 0              |                                                                                       |
| Financial investment         | 0              | §44: 1-year lock, cashed 2 Jan next year; every euro is needed by February            |
| Fixed-term deposits          | **0**          | same; the deposit lever starts in Plan 2.2 with the Year-1 closing cash               |
| Line of credit requested     | **10,000,000** | §43: 1% fee = 100,000 as insurance against the 20% overdraft (§42) if sales slip      |
| Customer payment terms       | 60 Days        | §38 shortest option; receivable 47,526,723 at year end (2/12 of revenue)              |
| Factoring                    | **No**         | Team decision; test Y2 paid 1,995,715 to factor receivables that closed at zero       |
| Max. amount to be discounted | --             |                                                                                       |
| Payment term for suppliers S | **120 Days**   | §28; test Y2 S raw material at 120 days came in at list 1.65 (Doc 05 §7.1 arithmetic) |
| Payment term for suppliers H | **120 Days**   | §28; payable at year end 4/12 x 43,732,143 = 14,577,381 of free financing             |
| Investment in securities 1-3 | 0 / 0 / 0      | §45                                                                                   |
| Sale of shares 1-3           | No / No / No   |                                                                                       |

---

## 4. Cash check

### 4.1 The §41 test the simulator runs

| Component                                                                                                         | €              | Source                                                       |
| ----------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------ |
| 80% x new fixed assets 55,200,000                                                                                 | 44,160,000     | §41 item 1                                                   |
| 50% x (media 678,000 + POP 48,000 + managers 600,000 + rep fixed 2,592,000 + overhead 600,000 + research 166,800) | 2,342,400      | §41 item 2                                                   |
| 15% x raw material 43,732,143                                                                                     | 6,559,821      | §41 item 3                                                   |
| **OCN**                                                                                                           | **53,062,221** | `operating_cash_needed()`                                    |
| Available cash 2 January                                                                                          | 54,000,000     | `available_cash_jan2(54,000,000)`: no payables, no loans due |
| Headroom                                                                                                          | +937,779       | `financing_gap()` -> loan_needed 0                           |

`[!]` The OCN test passes, so the simulator will **not** borrow for us. That is not the same as having
enough cash: §37 says lines are paid in cash, so on 2 January cash is 54,000,000 - 55,200,000 =
**-1,200,000** before a single salary is paid, and the first 60-day receipts arrive in March.

### 4.2 The real trough (monthly, before financing)

Outflows spread evenly: production payroll 50,598,000, power 6,138,720, fixed opex 8,724,800
(office 2,818,000, overhead 600,000, preventive 500,000, training 722,000, sales network 3,192,000,
media 678,000, POP 48,000, research 166,800), logistics 2,907,079, R&D 12,832,215, rep variable
1,191,006, retailer margins 40,834,458 paid at sale (§38). Raw material 43,732,143 paid from month 5
(120 days). Revenue 285,160,336 received from month 3 (60 days).

| Month-end | Jan         | Feb             | Mar        | Apr       | May        | Dec        |
| --------- | ----------- | --------------- | ---------- | --------- | ---------- | ---------- |
| Cash      | -11,468,856 | **-21,737,713** | -8,243,208 | 5,251,297 | 15,101,456 | 84,052,573 |

| Financing          | €                        | Cost in Year 1                                             |
| ------------------ | ------------------------ | ---------------------------------------------------------- |
| Loan               | 25,000,000               | 2,500,000 interest + 250,000 fee (§49: 10% + 1%)           |
| Credit line        | 10,000,000               | 100,000 fee; 7% only on any draw (§43)                     |
| Facility vs trough | 35,000,000 vs 21,737,713 | 1.6x cover; a 30% shortfall in March receipts still clears |
| Deposit            | 0                        | nothing to park until the Year-1 close                     |

Test comparison: test Y1 with no planned loan cost 1,892,199 of overdraft on ~9.46M average; test Y2
with a 100,857,687 loan cost 13,977,015 of financial expense while closing with 107,327,322 of cash.

### 4.3 Year-1 result from the model and the year-end position

`Simulation.run_year()` with this sheet: revenue 285,160,336; net sales 244,325,878; gross margin
144,156,486; operating income 110,437,386; **net income 110,187,386**. Year-end: cash 108,614,487,
receivables 47,526,723, payables 14,089,824, loan 25,000,000, inventory 0. Available cash for the
Year-2 OCN test: **133,718,053**, after the 8,333,333 repayment.

Two model behaviours the test round has already measured, applied by hand rather than by editing the
model:

| Correction                                | Evidence                                                                                        | Effect on Y1 net income |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------- |
| Loan interest is charged in the draw year | Test Y1: "Loans 382,605" = 10% x 3,826,050 drawn that year; model charges 0                     | -2,500,000              |
| Credit-line fee                           | Test Y2: 300,000 = 1% x 30,000,000, undrawn                                                     | -100,000                |
| Land and buildings are not depreciated    | Test Y2: 7,056,000 = 12% x (52,800,000 lines + 6,000,000 SMED); model applies 12% to 67,200,000 | +1,440,000              |
| **Adjusted Year-1 net income**            |                                                                                                 | **~109,027,000**        |

`[~]` For scale: test Y2 earned 87,103,307 on 254,505,471 of revenue with 12,253,570 H units unsold
and 13,977,015 of financial expense. This plan has 12% more revenue, one fifth of the financial
expense, and no unsold stock **if the fleet clears** - which is the whole bet.

---

## 5. A6 pre-submission checklist, ticked against this sheet

| Check                                                           | Status | Where                                                                  |
| --------------------------------------------------------------- | ------ | ---------------------------------------------------------------------- |
| Price, retailer margin and shelf space in every cell we sell in | Yes    | Forms 5-6: 12 A/B cells; E deliberately blank                          |
| Advertising campaign selected                                   | Yes    | 18 S / 19 H in A and B                                                 |
| Lines activated, not just installed                             | Yes    | Form 7: 20 H + 12 S active                                             |
| Production forecast <= capacity at the plan-on rate             | Yes    | `capacity_reality_check`: S 6,970,320 / H 29,043,000, no STOCKOUT flag |
| Raw material covers production plus scrap                       | Yes    | H x1.02; S x1.02 x1.05                                                 |
| No logistics field blank or zero                                | Yes    | Form 2, E at form minimums (open question 1)                           |
| Every zone covered by a manager or wholesaler                   | Yes    | 6/6 managers in A/B; E not operated                                    |
| Promotion volumes within supply                                 | Yes    | S only, 1 per channel; H none                                          |
| OCN <= available cash, or loan deliberately requested           | Yes    | 53,062,221 <= 54,000,000 and 25M loan for the trough                   |
| Surplus cash on deposit                                         | n/a    | No surplus until 31 Dec; deposit in Plan 2.2                           |
| Surveys 20, 21, 22 + the 11,000 bundle ordered                  | Yes    | Form 4, total 166,800                                                  |
| SMED not requested in year 1; Poka Yoke not requested           | Yes    | Form 7                                                                 |
| Sales managers entered (they reset every year)                  | Yes    | Form 1                                                                 |

---

## 6. Open questions to confirm on the interface (max 5)

| # | Question                                                                                                                                                                                           | If the answer is bad                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1 | Does the E logistics block accept the form minimums (12 / 1 @ 1,000 / 1 @ 500) with **no E price**, and does the DEP mirror show E as not commercialised? §13 forbids zero; §15 says no price = not selling | If the form forces a price, enter one above the E average (test Y2: 19.50 S / 9.00 H) and 0 shelf space so no E sales occur   |
| 2 | Graded-run INF: loan maturity and rate. Test went 4 -> 3 years; §49 says it keeps falling                                                                                                          | At 2 years the repayment is 12,500,000 on 2 Jan Y2 and Y3, against 108.6M closing cash: still fine, update `SCENARIO`         |
| 3 | H price in market A: hold 5.25 (68.6% share evidence) or lift toward B's 7.75 (55.1% share evidence)? Planned H output 29.0M is 6.8M below the test-Y2 demand reading, so some H demand goes unserved either way (§34) | Doc 05 §7.3 says re-read price only once the fleet is proven; if the team lifts A, do it in steps that keep the B-market evidence as the ceiling |
| 4 | Promotion form semantics: is "Detail" the gift value and "Number" the count of promotions (test Y2 E entry 2 / 2 cost 0.60 per promo unit, 51,428 total)?                                          | If "Detail" is a euro budget, set it to 0.40 x expected promo units per channel (`--promotions 14.50`)                        |
| 5 | Last-mile count: the interface may show a per-vehicle capacity or route time. If it does, resize: units per vehicle must stay above 20,374,889 / A-count and 15,895,111 / B-count                  | Never below A 17 / B 14 (the test-Y2 evidence floor of 1,217,870 units per vehicle)                                           |

---

## 7. Where Doc 05's plan did not translate to a fresh start

| Doc 05 item                                                           | Fresh-start translation                                                                                                                                                    |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #3 "Sell the H you already made, buy no H raw material, idle H lines" | No stock exists. H raw material **must** be bought (29,835,000) and every line activated; the 0.9379 cheap-material block is gone, so H standard cost is 2.17, not 2.06    |
| #2 "Right-size the debt vs 100M, deploy the cash"                     | There is no 100M loan to right-size and no payables or loans due on 2 January; the loan is a fresh 2-month trough loan, and there is no surplus to deposit until the close |
| Part 4 calibrations (SMED 92.9%, conversion cost -6%/-8%)             | Both are SMED-plant measurements; Year 1 has no SMED, so the model correctly runs the bare-line 81.20% and uncalibrated costs                                              |
| #1 "Fix the fleet" from stockout flags                                | Translated into tonnage arithmetic (2.3) because there are no Year-0 flags to react to                                                                                     |
| #4 "Rebalance toward S"                                               | Done at install time (12/20 vs 8/24), the only moment it can be done without stranding H lines                                                                             |
| §7.2 "Decide E explicitly"                                            | Decided: out. Entry cost stated on Form 1 for the overrule                                                                                                                 |
| 4-year horizon (new requirement)                                      | All capex lands in Year 1 by team decision; Years 2-4 have one gated capex (SMED) and no line additions possible                                                           |

Figures that could **not** be sourced and are therefore judgement calls: the 55/45 S market split
(interpolated between test Y1 48/52 and test Y2 98/2), the 15% loan buffer, the €10,000,000
credit-line size, and the last-mile vehicle counts beyond the evidence floor.

---

## Sources

- `Scenario MMT39 EN v231.pdf` — §1, §6, §8, §10-§15, §18-§23, §25-§30, §32, §34, §35, §37, §38, §41-§45, §47-§49
- `day 1/year 2/DIR0114SI02082TE3Y1REP.pdf` — units by channel p2-p3, production and stockout flags p4, P&L p5, balance sheet p6
- `day 1/year 2/DIR0114SI02082TE3Y1DEP.pdf` — Year-1 form layout and values, logistics p2, HR p3, production p6, finance p7
- `day 2/year 2 results/DIR0114SI02082TE3Y2DEP.md` — form order and field names used above
- `day 2/year 2 results/DIR0114SI02082TE3Y2REP.md` — units by channel p2-p3, production and flags p4, P&L p4-p5, balance sheet p6
- `day 2/year 2 results/DIR0114SI02082TE3Y2INFen_US.md` — loan maturity 3 years, rates
- `docs/03-decision-checklist-and-grading-playbook.md` — A0-A6
- `docs/04-test-year1-postmortem-and-year2-audit.md` — Part 1 failures, Part 3 form template, Part 4 gap list
- `docs/05-test-year2-postmortem-and-graded-run-plan.md` — Parts 1, 2, 4, 6, 7
- `model/mmt39.py` — `capacity()`, `standard_cost()`, `production_headcount()`, `office_payroll()`, `plan_platform_to_retailer()`, `vehicle_annual_cost()`, `platform_costs()`, `operating_cash_needed()`, `available_cash_jan2()`, `financing_gap()`, `research_cost()`, `promotion_menu()`, `Simulation.run_year()`, `LoanBook`
