# Graded Year 1 — Competitor and Market Intelligence Brief (Company 3, "COMPANY_3" / ANGELO TEAM)

**Sources** (all in `day 2/year 1 results/`): `…Y1INV.md` (surveys, PDF conversion), `…Y1EXCINV.md` (same surveys, Excel conversion — used wherever the PDF table is garbled), `…Y1REP.md` (our results), `…Y1INFen_US.md` (macro bulletin), `…Y1DEP.md` (our filed decisions). Survey names from `model/mmt39.py` `SCENARIO["research"]`; market potentials from `docs/01-company-and-market-dossier.md` "Market size" table; positioning-axis labels from `SUMMARIES.txt` (synoptic: X = Natural, Y = Technological). Every figure not marked **[derived]** is copied verbatim.

**Identity check.** Graded files carry `Simulation: B1SIM2C2`, `Trade name: COMPANY_3`, `C: 3`, `Year: 1`. Test-round files carried `B1SIM2C1` — a different simulation instance, same company numbering 1–5. [Likely] the same teams are behind the same numbers: the behavioural fingerprints match the test round exactly (Co 1 runs campaign 1 everywhere at S 8.00–9.00; Co 2 is highest-priced with promotions in every channel; Co 4 is cheapest-S with 3x2 on H; Co 5 files 0.00 everywhere). Not provable from the files.

---

## 1. Surveys bought and not bought (DEP p4 "MARKET RESEARCH SURVEYS")

| ID | Name (model `research` dict) | Cost € | Bought |
|---|---|---|---|
| 1 | Sales of S by market | 3,000 | **Yes** |
| 2 | Sales of H by market | 3,000 | **Yes** |
| 3 | Sales of S and H by company and market | 36,000 | **Yes** |
| 4 | Sales of S and H by company, market and channel | 72,000 | No |
| 5 | Promotional sales by company and market | 89,800 | No |
| 6 | Promotional sales by company, market and channel | 107,000 | No |
| 7 | Positioning of S brands by market | 59,900 | **Yes** |
| 8 | Positioning of H brands by market | 59,900 | **Yes** |
| 9 | Overseas advertising by A/B companies | 36,000 | No |
| 10 | Coverage of advertising by company and market | 59,900 | No |
| 11 | Number of advertising insertions by company | 36,000 | No |
| 12 | Advertising by E domestic companies | 36,000 | No |
| 13 | PoP advertising by company, market, channel | 59,900 | No |
| 14 | Sales managers and reps by company and market | 24,000 | No |
| 15 | Shelf space achieved by company and channel | 72,000 | No |
| 16 | Accumulated fixed-asset investment by company | 49,000 | No |
| 17 | Average overseas prices | 24,000 | No |
| 18 | Total overseas sales by A/B/E companies | 36,000 | No |
| 19 | Demand for normal units by company and market | 110,000 | No |
| 20 | Retail prices by market and channel | 0 | **Yes** |
| 21 | Advertising campaigns by market | 0 | **Yes** |
| 22 | Promotion type by company and channel | 0 | **Yes** |
| 23 | End-of-year net income | 1,000 | **Yes** |
| 24 | Industry average production cost | 10,000 | No |
| 25 | Industry average salary cost | 5,000 | No |
| 26 | Industry balance sheets | 10,000 | No |
| 27 | Logistics platforms by company and market | 3,000 | **Yes** |
| 28 | Production shifts | 1,000 | **Yes** |
| | **Total** (DEP p4 "Total"; REP p5 "Market research expense") | **166,800** | 11 surveys |

Consequence of what was **not** bought: no rival ad budgets/insertions (10, 11, 13), no rival salesforce (14), no shelf space (15), no rival balance sheets or asset base (16, 26), no channel split of rival sales (4). Those rows are marked "not purchased" below rather than guessed.

---

## 2. Per-company tables

### 2.1 Units sold by company, product, market — Survey 3 (EXCINV p3) with **[derived]** shares

| Product | Market | Co 1 | Co 2 | **Co 3 (us)** | Co 4 | Co 5 | Participants' total (Survey 1/2) |
|---|---|---|---|---|---|---|---|
| S | A | 731,930 (6.69%) | 1,355,660 (12.40%) | **5,759,496 (52.67%)** | 3,088,590 (28.24%) | 0 | 10,935,676 |
| S | B | 49,135 (2.15%) | 2,119,478 (**92.53%**) | **90,504 (3.95%)** | 31,410 (1.37%) | 0 | 2,290,527 |
| S | E | 3,735 (9.68%) | 34,862 (90.32%) | **0** | 0 | 0 | 38,597 |
| H | A | 80,098 (0.40%) | 7,782,836 (38.60%) | **4,556,494 (22.60%)** | 7,743,383 (38.40%) | 0 | 20,162,811 |
| H | B | 86,810 (0.49%) | 6,784,697 (37.92%) | **9,989,807 (55.83%)** | 1,031,617 (5.77%) | 0 | 17,892,931 |
| H | E | 2,101 (3.53%) | 57,467 (96.47%) | **0** | 0 | 0 | 59,568 |
| **S all markets [derived]** | | 784,800 | 3,510,000 | **5,850,000** | 3,120,000 | 0 | 13,264,800 |
| **H all markets [derived]** | | 169,009 | 14,625,000 | **14,546,301** | 8,775,000 | 0 | 38,115,310 |

Checks: every Survey 3 row sums exactly to its Survey 1/2 total; our rows equal REP p2–p3 channel sums (A: 2,587,071 + 2,459,621 + 712,804 = 5,759,496; B: 20,421 + 50,922 + 19,161 = 90,504; H A: 63,960 + 1,534,920 + 2,957,614 = 4,556,494; H B: 2,057,439 + 5,856,779 + 2,075,589 = 9,989,807). Value shares are not computable — no channel split of rival units (survey 4 not bought).

### 2.2 Prices (MSRP, €; E in $ at FX 1.00) — Survey 20 (INV p7)

| Product | Market | Ch | Co 1 | Co 2 | **Co 3 (us)** | Co 4 | Co 5 |
|---|---|---|---|---|---|---|---|
| S | A | G | 8.50 | 11.50 | **14.50** | 8.50 | 0.00 |
| S | A | S | 8.50 | 12.00 | **14.50** | 9.10 | 0.00 |
| S | A | T | 8.00 | 12.50 | **14.50** | 9.40 | 0.00 |
| S | B | G | 9.00 | 12.00 | **14.50** | 8.50 | 0.00 |
| S | B | S | 9.00 | 12.50 | **14.50** | 9.10 | 0.00 |
| S | B | T | 8.50 | 13.00 | **14.50** | 9.40 | 0.00 |
| S | E | G | 10.00 | 13.00 | **0.00** | 0.00 | 0.00 |
| H | A | G | 7.00 | 9.50 | **6.50** | 6.50 | 0.00 |
| H | A | S | 7.00 | 10.00 | **6.50** | 6.80 | 0.00 |
| H | A | T | 6.50 | 10.50 | **6.50** | 7.20 | 0.00 |
| H | B | G | 7.50 | 10.00 | **7.50** | 6.50 | 0.00 |
| H | B | S | 7.50 | 10.50 | **7.50** | 6.80 | 0.00 |
| H | B | T | 7.00 | 11.00 | **7.50** | 7.20 | 0.00 |
| H | E | G | 8.50 | 12.00 | **0.00** | 0.00 | 0.00 |

Our retailer margin S 1.90 / H 1.00, shelf space S 18% / H 22% (DEP p4–p5). Rival margins and shelf space: not in any purchased survey. Co 2 and Co 4 ladder G < S < T; Co 1 ladders the other way (T cheapest); we are flat.

### 2.3 Advertising campaign IDs — Survey 21 (INV p8); spend only known for us

| Product | Market | Co 1 | Co 2 | **Co 3 (us)** | Co 4 | Co 5 |
|---|---|---|---|---|---|---|
| S | A | 1 | 17 | **18** | 6 | 0 |
| S | B | 1 | 17 | **18** | 6 | 0 |
| S | E | 1 | 17 | **0** | 0 | 0 |
| H | A | 1 | 19 | **19** | 14 | 0 |
| H | B | 1 | 19 | **19** | 14 | 0 |
| H | E | 1 | 19 | **0** | 0 | 0 |

Our media (DEP p5–p6): S per market 8 TV (144,000) + 4 press (60,000) = 12 insertions / 204,000, POP 10,000 per channel; H per market 5 TV (90,000) + 3 press (45,000) = 8 / 135,000, POP 15,000 per channel. REP p5: "Advertising (including POP) S 468,000, H 360,000" (= 2 × 204,000 + 6 × 10,000; 2 × 135,000 + 6 × 15,000 [derived]). Rival media weight, vehicle mix and POP: **not purchased** (surveys 10, 11, 13). Campaign names for IDs 1, 6, 14, 17 are not in any repo file; 18 = "Technology for your skin", 19 = aloe vera "most natural of creams" (SUMMARIES.txt). **Co 2 runs our exact H campaign (19).**

### 2.4 Promotions — Survey 22 (INV p9); legend 1 = none, 2 = price reduction, 3 = 3x2, 5 = discount on next purchase

| Product | Market/Ch | Co 1 | Co 2 | **Co 3** | Co 4 | Co 5 |
|---|---|---|---|---|---|---|
| S | all 7 cells | 1 | **2** | **1** | 1 | 1 |
| H | A/G, A/T, B/G, B/T, E/G | 1 | **2** | **1** | 1 | 1 |
| H | A/S | 2 | **2** | **1** | **3** | 1 |
| H | B/S | **5** | **2** | **1** | **3** | 1 |

Co 2 runs a price reduction in every cell of both products. Co 4 runs 3x2 on H in supermarkets only. We ran nothing (REP p2–p3: "Units sold on promotion" 0 everywhere).

### 2.5 Brand positioning — Surveys 7 and 8 (INV p5–p6). X = Natural, Y = Technological (SUMMARIES.txt synoptic; §17 leaves axes unlabelled)

| Product | Co 1 | Co 2 | **Co 3** | Co 4 | Co 5 | E locals J / K / L |
|---|---|---|---|---|---|---|
| S (A, B identical) | (8, 2) natural | (3, 8) tech | **(1, 8) tech** | (2, 8) tech | (0, 0) | J (3, 8) · K (6, 6) · L (8, 3) |
| H (A, B identical) | (5, 5) neutral | (9, 1) natural | **(9, 1) natural** | (1, 8) tech | (0, 0) | J (3, 8) · K (6, 6) · L (8, 3) |

Three of four live companies crowd the technological S corner; on H, Co 2 sits on top of us at (9, 1). In E only Co 1 and Co 2 have coordinates. Quality / product characteristics: no survey covers these; none bought.

### 2.6 Logistics platforms — Survey 27 (INV p11)

| Market | Co 1 | Co 2 | **Co 3** | Co 4 | Co 5 |
|---|---|---|---|---|---|
| A | 30 | 12 | **12** | 6 | 30 |
| B | 30 | 12 | **12** | 6 | 30 |
| E | 48 | 12 | **60** | 60 | 60 |

Our DEP p2 shows E: 60 platforms, 10 vehicles × 12,000, 30 × 1,500 with **no E price** — the worksheet template defaults (SUMMARIES.txt "trap hiding in the worksheet template"). Co 4 and Co 5 show the same 60. REP p5 "Sales network – Market E 0" and no import duties, so [Likely] no E cost hit us, but the form was not blanked as Doc 06 planned. Co 4 serves A and B on 6 platforms each — the leanest footprint.

### 2.7 Shifts (Survey 28, INV p12), net income (Survey 23, INV p10; REP p6), and **[derived]** line counts

| Co | Shifts | Net income € | Rank | S units ÷ 195,000 per line-shift | H units ÷ 487,500 per line-shift | Implied lines |
|---|---|---|---|---|---|---|
| 1 | 1 | **-10,887,540** | 4 | 784,800 / 195,000 = 4.02 (not integer → did not sell out, or different yield) | 0.35 | not inferable |
| 2 | 3 | 59,544,072 | 2 | 3,510,000 / 195,000 = **18.0** → 6 S lines | 14,625,000 / 487,500 = **30.0** → 10 H lines | 16 |
| **3** | 3 | **67,823,192** | **1** | 5,850,000 / 195,000 = 30 → 10 S lines (DEP p6: 10) | 32,175,000 / 487,500 = 66 → 22 H lines (DEP p6: 22) | 32 |
| 4 | 2 | 5,932,326 | 3 | 3,120,000 / 195,000 = **16.0** → 8 S lines | 8,775,000 / 487,500 = **18.0** → 9 H lines | 17 |
| 5 | 1 | -3,157,092 | 5 | 0 | 0 | inactive |

Basis: REP p4 shows our plant delivered 5,850,000 / (10 lines × 3 shifts) = **195,000** per S line-shift and 32,175,000 / 66 = **487,500** per H line-shift, i.e. 240,000 × 0.8125 and 600,000 × 0.8125 — **81.25%**, not the 78.75% in CLAUDE.md (we ran preventive maintenance, DEP p7). Co 2's and Co 4's totals divide to exact integers at that yield, so [Likely] both ran preventive maintenance and **sold every unit they made** (Co 2 in 3 shifts, Co 4 in 2). Their shares are therefore capacity, not demand. Our plan-on figure of 184,800/462,000 undershot the real yield by 5.5% — worth a model fix.

Salesforce: Survey 14 not bought. Ours (DEP p2–p3): 6 sales managers in A, 6 in B, 0 in E; reps A: S 4, T 4; B: S 5, T 3; salary 27,000 fixed + 0.60% variable.

---

## 3. Market actually sold vs theoretical potential

| Product | Market | Participants sold (Survey 1/2) | Potential (dossier §3×§2) | Penetration **[derived]** | Unsold potential **[derived]** |
|---|---|---|---|---|---|
| S | A | 10,935,676 | 12,100,000 | 90.38% | 1,164,324 |
| S | B | 2,290,527 | 9,000,000 | 25.45% | 6,709,473 |
| S | E | 38,597 | 35,100,000 | 0.11% | 35,061,403 |
| S | **all** | 13,264,800 | 56,200,000 | 23.60% | 42,935,200 |
| H | A | 20,162,811 | 29,260,000 | 68.91% | 9,097,189 |
| H | B | 17,892,931 | 27,000,000 | 66.27% | 9,107,069 |
| H | E | 59,568 | 75,000,000 | 0.08% | 74,940,432 |
| H | **all** | 38,115,310 | 131,260,000 | 29.04% | 93,144,690 |

Where the unmet demand went, with evidence:

| Pocket | Evidence | Reading |
|---|---|---|
| S, A+B: 7,873,797 unsold | We stocked out: REP p2 "Units demanded of your brand **1,827,440**" (unserved, per Doc 05 §5.1), inventory 0. Co 2 and Co 4 sold out [Likely, §2.7]. | **Supply-constrained.** The S market had buyers nobody could serve. Total demand for our S alone = 5,850,000 + 1,827,440 = **7,677,440** [derived]. |
| S, B specifically: 25% penetration | Our B media equalled A this year (12 insertions / 204,000 each, DEP p5) yet B sold 90,504 vs A 5,759,496. | [Likely] the simulator filled A first from a sold-out pool; the test-Y2 "B is media-starved" reading (Doc 05 §6.3) is not what happened here. B S demand is unobserved, not absent — Co 2 pulled 2,119,478 there at 12.00–13.00. |
| H, A+B: 18,204,258 unsold | We sat on **17,628,699** finished H (REP p3) with only 501,093 unserved, while Co 2 and Co 4 sold out [Likely]. | **Demand-constrained for our brand, not for theirs.** Buyers chose Co 2 at 9.50–11.00 and Co 4 at 6.50–7.20 over us at 6.50/7.50. Whatever drives H choice, it is not price (§5). |
| E: 109,999,835 unsold across both products | Only Co 1 and Co 2 present; combined 98,165 units. Local brands J/K/L not counted in participants' totals. | Unchanged from the test round: E is not buyable with marginal money. |
| The 501,093 unserved H | Printed alongside 17.6M inventory and "Logistic stockout No / No" for all markets. | `[~]` Unexplained by the files — possibly channel/shelf-level demand we could not place. Flag to the Director; do not build on it. |

---

## 4. Rival profiles

| Co | Strategy they seem to run | Where they beat us | Where they are weak |
|---|---|---|---|
| **2** | Premium price (S 11.50–13.00, H 9.50–12.00), price-reduction promo in every cell, 3 shifts on ~16 lines, present in all three markets on 12 platforms each, our H campaign and our H positioning. | Sold out both products (14,625,000 H at ~10 € vs our 14.5M at 6.50–7.50); owns S in B (92.53%); only real E participant (90–96% of participant E units); net income 59.5M only 8.28M behind us [derived: 67,823,192 − 59,544,072]. | Capacity-capped — could not serve more of B or E; E volumes are trivial (34,862 S / 57,467 H) for 12 platforms and a 3-market footprint. |
| **4** | Volume-price play: cheapest S (8.50–9.40), cheap H (6.50–7.20) with 3x2 in supermarkets, tech-positioned H, 2 shifts on ~17 lines, 6 platforms per market, zero E. | 38.40% of H in A (7,743,383) at a price near ours; leanest logistics; 28.24% of S in A on cheap price. | Net income only 5,932,326 — low prices ate the margin; near-absent in B (S 1.37%, H 5.77%); a third shift would add ~50% output and is the obvious Year-2 move. |
| **1** | Minimum effort: campaign 1 everywhere, one shift, 30 platforms in A and B (5× ours per unit sold), token E entry (48 platforms for 5,836 units). | Nothing. | Loss of 10,887,540; H 0.4–0.5% share; fixed-cost overhang from platforms. Irrelevant unless they pivot. |
| **5** | Inactive (0.00 prices, campaign 0, 30/30/60 platforms). Loss 3,157,092 = fixed costs. | Nothing. | Not a competitor. Watch only for a sudden entry. |

**Strongest rival: Co 2** — second on net income, sold out everything, the only one with a price umbrella above ours on H and the only one growing E. **Most likely to collide with us in Year 2: Co 2 on H** — identical campaign (19), identical positioning (9, 1), 3 shifts, and 17.6M of our unsold H means we will be pushing volume into the segment they already win at higher prices. Second collision risk: **Co 4 on H in A** if they add a shift — they already match Co 2's A share at a lower price than ours.

---

## 5. Price map and price sensitivity

| Product | Market | Our price vs rivals | Our share | What the data supports |
|---|---|---|---|---|
| S | A | Highest by 2.00–6.50 (14.50 vs C2 11.50–12.50, C4 8.50–9.40, C1 8.00–8.50) | 52.67%, stocked out with 1,827,440 unserved | Share rank is the **inverse** of price rank, but every seller with a round-number total sold out, so shares measure capacity. **No evidence** on S price elasticity; strong evidence that 14.50 did not cap demand below our capacity. |
| S | B | Highest (14.50 vs C2 12.00–13.00) | 3.95% | Allocation artefact of the stockout (§3). **No evidence.** |
| H | A | Lowest-or-equal (6.50 vs C4 6.50–7.20, C1 6.50–7.00, C2 9.50–10.50) | 22.60% | Cheapest price, third share, 17.6M unsold — **price is not the H driver**. Co 2 at +3.00–4.00 sold out with the same campaign and positioning; the difference sits in something we did not buy visibility on: promotions (Co 2 price reduction everywhere; Co 4 3x2), media weight (survey 11), salesforce (14), shelf (15), POP (13). |
| H | B | Middle (7.50 vs C4 6.50–7.20, C1 7.00–7.50, C2 10.00–11.00) | 55.83% | We won B at a *higher* price than in A. Consistent with the A reading: non-price factors dominate. |
| S/H | E | Not present; C1 10.00/8.50, C2 13.00/12.00 | 0 | No evidence. |

Bottom line: [Certain] at Year-1 settings S demand for our brand exceeded our supply at 14.50; [Certain] our H did not clear at the lowest price in A; [Guessing] which non-price lever explains Co 2's H sell-through — the 36,000 (survey 11) + 24,000 (14) + 59,900 (13) needed to know is cheap against 40,990,251 of H stock on the balance sheet (REP p6).

---

## 6. Market E entrants

| Co | E prices ($) | E units S / H (Survey 3) | E platforms | E campaign | E positioning S / H |
|---|---|---|---|---|---|
| 1 | S 10.00, H 8.50 | 3,735 / 2,101 | 48 | 1 / 1 | (8, 2) / (5, 5) |
| 2 | S 13.00, H 12.00 | 34,862 / 57,467 | 12 | 17 / 19 | (3, 8) / (9, 1) |
| 3, 4, 5 | none | 0 / 0 | 60 / 60 / 60 (template default) | 0 | (0, 0) |

Result: 98,165 participant units against 110,100,000 of E potential (0.09% [derived]). Co 2's S positioning (3, 8) is identical to local brand J's; Co 2's 12 platforms are the E form minimum. E remains a money sink for entrants; Co 1's 48 platforms for 5,836 units is the worst ratio in the industry.

---

## 7. INF bulletin for Year 2 — quoted exactly (`…Y1INFen_US.md` p2)

| Item | Value | Change vs test-round bulletin |
|---|---|---|
| Per capita income | A "27,000 €", B "35,000 €", E "46,000 $" | unchanged |
| Standard cost, raw material | H "1.0500", S "1.6500" | unchanged |
| Standard cost, power | H "0.1500", S "0.2500" | unchanged |
| Exchange rate, "Euros per 1 Dolar" | "1.00" | unchanged |
| Unemployment rate | "7.00" % | unchanged |
| Overdraft interest | "20.00" % | unchanged |
| Loans | upfront fee "1.00" %, prepayment penalty "1.00" %, maturity "4" years, interest "10.00" % | unchanged |
| Lines of credit | interest "7.00" %, upfront "1.00" %, service "1.00" % | unchanged |
| Financial investments / fixed-term deposits | interest "2.50" %, early withdrawal "1.00" % | unchanged |
| Factoring | "5.50" % | unchanged |

Nothing in INF changes the competitive picture: no FX move, no cost shock, no rate change. Note REP p4 actual "S.C. per unit of raw materials" H 1.0815 / S 1.6995 versus INF standard 1.05 / 1.65 — the 3% gap is our purchasing, not the market. The competitive change comes entirely from the surveys, not the bulletin.

---

## 8. Year-2 implications (max six, each tied to a row)

| # | Implication | Row |
|---|---|---|
| 1 | **Do not add H capacity; sell the 17,628,699 units first.** Total H demand for our brand was 15,047,394 [derived: 14,546,301 + 501,093] against 32,175,000 produced. Even a repeat of Year-1 sell-through leaves ~3M unsold at year-end 2. Cut H to the shifts needed to top up, and re-deploy the freed cash. | §3 H A+B row; §2.1 H totals |
| 2 | **Add S capacity or a shift-equivalent; S is the product with proven unserved demand.** 1,827,440 unserved at 14.50, and Co 2 + Co 4 also sold out, so Year-2 S demand is at least Year-1 sales plus that. New S lines are irreversible, so size to 7,677,440 [derived] before any growth assumption, at the measured 195,000 per line-shift, not 184,800. | §3 S A+B row; §2.7 our row |
| 3 | **Buy surveys 11, 13, 14 (119,900 total) before touching the H price.** Co 2 out-sold us on H at +3.00–4.00 with the same campaign and positioning; the levers that differ are media weight, POP, salesforce, and promotions, and we bought none of the surveys that reveal them. Cutting the H price would be guessing against Co 4's 6.50 without knowing why 6.50 lost in A. | §5 H A row; §2.3, §2.4 |
| 4 | **Run an H promotion in supermarkets in both markets.** The two H sell-outs both promoted (Co 2 price reduction everywhere, Co 4 3x2 in channel S); we ran none and have the stock to fund it. Channel S is our largest H channel (A 1,534,920; B 5,856,779, REP p3). | §2.4 H A/S and B/S rows |
| 5 | **Hold S at 14.50 and keep campaign 18 + the 12-insertion weight in both markets; move nothing on S price.** The market took everything we made at the highest price in the industry, and B's 3.95% is a stockout artefact, not a price signal. Re-read B only after S supply exceeds A demand. | §5 S A and S B rows |
| 6 | **Blank the E logistics block properly, and expect Co 2 — not us — to keep bleeding in E.** Our DEP shows 60 platforms / 40 vehicles in E with no price (template defaults); rivals can see the 60 in survey 27. Co 2's 12-platform E presence yielded 92,329 units; no reason to follow. | §2.6 E row; §6 |

**Open items for the Director:** (a) the 501,093 unserved H alongside 17.6M inventory and no logistic stockout; (b) whether 81.25% yield is the preventive-maintenance figure (§25) so the model's 78.75% plan-on constant can be corrected; (c) whether the E platforms on the DEP incurred any cost (REP shows none identifiable).
