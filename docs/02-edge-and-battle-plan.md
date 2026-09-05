# Doc 02 — Edge & Battle Plan

**What the other teams will miss, and what to do about it.**
Markers: `[!]` trap · `[+]` edge · `[~]` judgement call. Figures verified against `mmt39.py`.

---

## 1. Where the edge actually comes from

Everyone starts identical (§1). So an advantage can only come from three places:

| Source                   | Why it exists                                          | How long it lasts        |
| ------------------------ | ------------------------------------------------------ | ------------------------ |
| **Doing the arithmetic** | 57 pages of rules; most teams read the ideas, not sums | All four years           |
| **Rival predictability** | Students default to instinct in year 1                 | Years 1–2, then it fades |
| **Free information**     | Three surveys cost nothing and reveal rival strategy   | All four years           |

Only the first is durable. The other two are worth most early — which is why the year-1 plan matters
more than its share of the timeline suggests.

---

## 2. The eight blind spots

Each is a real number, a predicted rival behaviour, and your counter.

### 2.1 `[!]` Nameplate capacity is 21% fiction

**Fact:** real output is **78.75%** of the §23 headline — 175 h of breakdowns and 250 h of module
servicing out of 2,000 (§24).

**What rivals do:** forecast off 240,000 / 600,000 per line-shift, promise the volume to their CEO,
then stock out. §34 says a stockout damages "brand prestige and loyalty," which carries into later
years.

**Your counter:** plan off 184,800 (S) and 462,000 (H) per line-shift. Run
`capacity_reality_check()` before every submission. When a rival stocks out in year 1, their
year-2 demand is already impaired — take that share.

### 2.2 `[!]` Sunscreen is the glamour trap

**Fact:** an S line costs **3.5× more capital per unit** (€3.79 vs €1.08) and **2.4× more to run**
(€5.13 vs €2.13). S needs roughly double the price to break even: €7.99 vs €3.86.

**What rivals do:** over-weight S. It is the more exciting product to build a campaign around, and
the higher price looks like higher margin.

**Your counter:** weight toward H unless you have a genuine premium positioning for S. And remember
H is a **2.3× larger market** (131.3M vs 56.2M units). If rivals crowd into S, the H market gets
less contested — the opposite of what they expect.

`[!]` **Lines are irreversible (§22).** This choice is locked for all four years.

### 2.3 `[+]` Television beats social media everywhere

**Fact:** cost per 1% of buyers reached — **TV €300 vs social €500 in A/B** (+67%), **TV $328 vs
social $517 in E** (+58%).

**What rivals do:** build a "digital-first, social-led" plan because that is the modern instinct.
They pay up to 67% more per point of reach.

**Your counter:** lead with TV. Use survey 21 (**free**) to see exactly which campaigns rivals ran,
and survey 11 (€36,000) for their insertion counts if you need share-of-voice.

`[+]` **Positioning is free to change every year** (§17) — no extra marketing spend required. Most
teams will treat year-1 positioning as a commitment. Treat it as an experiment.

### 2.4 `[!]` The logistics benchmark is a decoy

**Fact:** §10 calls €0.006/unit "reasonable." A full 24,000 kg vehicle achieves **€0.0044** — the
benchmark costs **36% more**.

**What rivals do:** hit €0.006, see it matches the rulebook, and believe they optimised.

**Your counter:** cost collapses to `24,000 × vehicles + 0.0024 × units`, so **minimise vehicle
count, then size each to fit exactly.** Use `optimal_vehicle_plan()`. Buying max-capacity trucks when
smaller ones fit your volume wastes ~10%.

### 2.5 `[!]` Poka Yoke destroys value

**Fact:** €720,000 **per line**. At 10 H lines / 3 shifts it adds 630,000 units (+4.55%) worth about
€584,000 a year, against €7,200,000 of capital. **Payback 12.3 years, in a four-year game.**

**What rivals do:** buy it. "Install quality control" reads as unambiguously good management, and it
is irreversible so they cannot undo it.

**Your counter:** don't — unless the Director confirms a brand or quality benefit the scenario does
not document. Ask directly in Session 2.

### 2.6 `[~]` SMED depends on one unasked question

**Fact:** SMED removes all 250 h of module downtime → **+15.9% output**, worth €208,614 per line per
year. But payback depends entirely on how many lines one duplicate module serves:

| Lines per module | Payback    | Verdict          |
| ---------------- | ---------- | ---------------- |
| 1                | 14.4 years | Never            |
| 4                | 3.6 years  | Marginal         |
| 8                | 1.8 years  | Clearly worth it |

**Your counter:** **ask the Director in Session 2.** Physics hints at up to 8 — servicing takes 5 h
and recurs every 40 operating hours — but that is inference. This single answer swings a
multi-million-euro decision. `[!]` Unavailable in year 1 (§27), so the year-1 plan must live at
78.75%.

### 2.7 `[+]` The financing answers are nearly free

| Fact                                              | Worth                |
| ------------------------------------------------- | -------------------- |
| Factoring 5.5% vs loan 10% on a €33.3M receivable | **€1,500,000 / yr**  |
| Depositing €54M idle cash at 2.5% (§44)           | **€1,350,000 / yr**  |
| Avoiding the 20% overdraft (§42)                  | Double the loan rate |

**What rivals do:** leave cash in the Cash account and borrow when they need working capital — the
exact wrong way round.

**Your counter:** factor receivables, deposit surplus, and check `ocn()` before every submission.
`[!]` §41 means the simulator takes a loan **for you** if OCN exceeds available cash. Sloppy cash
planning is silently expensive.

### 2.8 `[+]` Three surveys are free and nobody harvests them

| Survey | Cost | What it reveals                                |
| ------ | ---- | ---------------------------------------------- |
| 20     | Free | Every rival's retail prices, by market/channel |
| 21     | Free | Every rival's advertising campaign             |
| 22     | Free | Every rival's promotion type, by channel       |

Add **23** (net income, €1,000), **28** (shifts, €1,000), **1 & 2** (market sales, €3,000 each) and
**27** (platforms, €3,000) — **€11,000 total** tells you what every rival earned, how hard their
factories run, and how big the market actually got.

**Your counter:** buy all seven every single year and keep a running comparison table. That table is
also your CEO-meeting evidence: the rubric demands analysis "compared to other companies."

---

## 3. Predicted rival behaviour in year 1

Not certainties — working hypotheses to verify with the free surveys, then exploit.

| Likely rival move               | Why                           | Your counter                                    |
| ------------------------------- | ----------------------------- | ----------------------------------------------- |
| Over-weight S lines             | Glamour product, higher price | Weight H; take the less contested larger market |
| Plan off nameplate capacity     | Skipped §24                   | Plan at 78.75%; take share when they stock out  |
| Digital/social-led advertising  | Modern instinct               | Lead TV at 40% lower cost per reach point       |
| Hit the €0.006 logistics mark   | Rulebook says "reasonable"    | Reach €0.0044                                   |
| Enter all three markets at once | Maximise coverage             | Concentrate; capacity caps you at ~34% anyway   |
| Buy Poka Yoke early             | Sounds like good management   | Skip it; 12.3-year payback                      |
| Leave €54M in Cash              | Nobody told them not to       | Deposit it: €1.35M/yr                           |
| Skip the free surveys           | Assume free means worthless   | Harvest all three, every year                   |

`[~]` **If most rivals crowd into S**, the H market gets *less* competitive, not more. Verify with
survey 3 (€36,000) after year 1 before committing further capital.

---

## 4. The ungraded test round — 2 years

It is graded zero. Its **only** value is information. Most teams will treat it as practice and learn
nothing measurable. This is the largest single edge available, and it costs nothing.

| # | Experiment | What it buys you |
| - | -------------------------------------------------- | ---------------------------------------------------------- |
| 1 | **Charge different prices in A, B and E** | Price elasticity. `fit_elasticities()` cannot recover it if you charged the same price everywhere |
| 2 | **Vary advertising spend sharply between markets** | Advertising elasticity — how much reach actually converts |
| 3 | **Deliberately stock out in one market** | The real cost of §34's "brand prestige" damage. Nobody else will know this number |
| 4 | **Run one zone own-managed, one via wholesalers** | The true breakeven, not the theoretical one |
| 5 | **Try 2 shifts in year 1, 3 in year 2** | Whether depreciation (10%→12%) outweighs the extra output |
| 6 | **Test one promotion type per channel** | Which promotions the simulator actually accepts |
| 7 | **Buy the €11,000 survey bundle both years** | A rival baseline before it counts |
| 8 | **Check actual output against `capacity()`** | Settles the §24 reading and the §42 loan rule |

Record every year as an `Observation` and run `fit_elasticities()`. By the graded round you forecast
from **your own data** instead of guessing — which is exactly what the rubric rewards.

---

## 5. The four graded years

| Year  | Theme                | Key commitments                                                                                                                                              |
| ----- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1** | **Commit and learn** | S/H line mix (irreversible), markets entered, positioning. Plan at 78.75%. Deposit surplus cash. No SMED available                                           |
| **2** | **Fix and scale**    | SMED if the Director's answer justifies it. Preventive maintenance once the plant is large. Add lines where year 1 proved demand. Respond to rival stockouts |
| **3** | **Consolidate**      | Push share in markets that worked. Third shift if depreciation is covered. Prune losing channels — but lines stay installed                                  |
| **4** | **Harvest**          | Maximise accumulated profit — the ranking basis (§47). No new irreversible capex that cannot pay back inside one year                                        |

### The rule that governs every irreversible decision

> **Four years. Any irreversible investment with a payback beyond four years destroys value.**

| Investment             | Payback               | Verdict                      |
| ---------------------- | --------------------- | ---------------------------- |
| SMED (8 lines/module)  | 1.8 yrs               | Yes, from year 2             |
| SMED (4 lines/module)  | 3.6 yrs               | Marginal — year 2 only       |
| Preventive maintenance | Positive at 10+ lines | Yes, and reversible annually |
| SMED (1 line/module)   | 14.4 yrs              | No                           |
| Poka Yoke              | 12.3 yrs              | No                           |

---

## 6. Splitting the team

40% of your grade is **your individual area**, and the rubric requires each member's role to be
clearly identified in every deck. So the split must be real, not cosmetic.

| Role           | Owns                                                | Must be able to defend                                |
| -------------- | --------------------------------------------------- | ----------------------------------------------------- |
| **Marketing**  | Price, positioning, advertising, promotions, shelf  | Why TV over social; the segment map; price elasticity |
| **Operations** | Lines, shifts, SMED/PY/PM, raw materials, logistics | The 78.75% number; vehicle sizing; stockout risk      |
| **HR**         | Salaries at all levels, salesforce size, training   | Turnover vs. wage trade-off; salesforce breakeven     |
| **Finance**    | Financing, factoring, terms, OCN, forecasts         | Factoring vs loan; the OCN rule; every ratio          |

**Two cross-cutting jobs to assign explicitly**, because they fall between departments and get
dropped:

- **Competitive intelligence** — buy the survey bundle every year, maintain the rival comparison
  table. Feeds everyone's analysis and the rubric's "compared to other companies" requirement.
- **Submission check** — run through doc 03's checklist before every submit. A blank price, margin
  or shelf-space field means **zero sales** in that channel with no warning (§14, §20, §21).

---

## 7. Do this now

| # | Action | When |
| - | ------------------------------------------------------------------- | ------------------ |
| 1 | Ask the Director: **how many lines can one SMED module serve?** | Session 2 |
| 2 | Ask: does Poka Yoke carry any benefit beyond scrap and repair time? | Session 2 |
| 3 | Ask: §18 says eight promotion types but lists six — what are they? | Session 2 |
| 4 | Ask: what proportion do loans repay each year (§42)? | Session 2 |
| 5 | Assign the four departments plus the two cross-cutting jobs | Before Plan 1.1 |
| 6 | Decide the S/H mix from doc 01 §3 — it is locked for four years | Before Plan 1.1 |
| 7 | Design the test-round experiments from §4 above | Before Plan 1.1 |
| 8 | Buy surveys 20, 21, 22 (free) + 23, 28, 1, 2, 27 (€11,000) | Every year |

---

*Sources: `Scenario MMT39 .pdf`. Figures reproduce via `python3 model/mmt39.py --briefing`.
Facts and rules: `docs/01-company-and-market-dossier.md`. Submission checklist: `docs/03`.*
