"""
MMT39 decision model — IE MIM Dual Degrees Capstone (Praxis MMT 39 simulator).

Every constant below is lifted from `Scenario MMT39 .pdf` and carries its section
reference. Nothing here is invented. Where the scenario is ambiguous the ambiguity
is named explicitly in an ASSUMPTION comment and exposed as a parameter, so you can
recalibrate against real results instead of arguing with the rulebook.

Usage
-----
    python3 mmt39.py --selftest      # verify constants against the scenario
    python3 mmt39.py --briefing      # the headline numbers, ready to paste into a deck
    python3 mmt39.py --media         # media efficiency ranking
    python3 mmt39.py --vehicles      # vehicle sizing table
    python3 mmt39.py --lines         # line economics table

    >>> from mmt39 import *
    >>> cap = capacity(s_lines=4, h_lines=10, shifts=2)
    >>> sc  = standard_cost("H", shifts=2, lines=10, produced=cap.h_units)

No third-party dependencies. Python 3.9+.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Tuple

# ---------------------------------------------------------------------------
# SCENARIO CONSTANTS
# Edit only this block when the simulation Director changes a figure. This block has to include all of the updated values. 
# ---------------------------------------------------------------------------

SCENARIO: Dict[str, object] = {
    # -- §1 Companies: identical opening balance sheet for every team -------
    "opening_fixed_assets": 12_000_000.0,
    "opening_cash": 54_000_000.0,
    "opening_equity": 66_000_000.0,
    "opening_inventory": 0.0,

    # -- §2 Environment ----------------------------------------------------
    "population": {"A": 22_000_000, "B": 18_000_000, "E": 30_000_000},
    "surface_km2": {"A": 100_000, "B": 95_000, "E": 210_000},

    # -- §3 Products: per-capita consumption at t0 (units/person/year) ------
    # NOTE: applied to TOTAL population, not to the 25% buyer base — §3 says
    # "approximate per capita consumption", §5 separately defines buyers as the
    # advertising target. Keep the two apart when sizing vs. planning reach.
    "per_capita": {
        "S": {"A": 0.55, "B": 0.50, "E": 1.17},
        "H": {"A": 1.33, "B": 1.50, "E": 2.50},
    },

    # -- §4 Markets: points of sale by channel -----------------------------
    "outlets": {
        "A": {"T": 2_160, "S": 1_620, "G": 35},
        "B": {"T": 1_080, "S": 1_080, "G": 30},
        "E": {"G": 200},
    },
    "zones": {"A": 6, "B": 6, "E": 12},

    # -- §5 Demographic profile -------------------------------------------
    "buyer_share_of_population": 0.25,   # 50/50 male/female

    # -- §6 Commercial distribution ---------------------------------------
    "sales_manager_cost": {"A": 50_000.0, "B": 50_000.0, "E": 60_000.0},  # E in dollars

    # -- §7 Wholesalers: commission on RETAIL price ------------------------
    "wholesaler_pct_normal": 0.0846,
    "wholesaler_pct_promo": 0.065,

    # -- §9 Export chain to E ---------------------------------------------
    "export_fixed_per_unit": 0.024,      # freight + insurance + clearance + main platform
    "customs_duty_pct": 0.02,            # ad valorem on (standard cost + 0.024)

    # -- §10 / §12 Logistics ----------------------------------------------
    "vehicle_fixed_cost": 24_000.0,
    "vehicle_cost_per_kg": 1.2,
    "units_per_kg": 2,
    "vehicle_uptime_hours": 2_000.0,
    "f2p_route_hours": 8.0,              # §10: "The average time of a route is 8 hours"
    "f2p_kg_min": 1_000,
    "f2p_kg_max": 24_000,
    "p2r_kg_min": 500,
    "p2r_kg_max": 10_000,
    "f2p_benchmark_per_unit": 0.006,     # §10 "reasonable" guideline — see docs/03
    "p2r_benchmark_per_unit": 0.007,     # §12 guideline
    "platforms_allowed": {               # §10
        "A": [6, 12, 18, 24, 30, 36],
        "B": [6, 12, 18, 24, 30, 36],
        "E": [12, 24, 36, 48, 60, 72],
    },
    "speed_kmh": {                       # §10 / §12
        "factory_platform": {"A": 90, "B": 90},
        "platform_platform": {"A": 90, "B": 90, "E": 100},
        "mainplatform_platform": {"E": 110},
        "platform_retailer": {"A": 60, "B": 60, "E": 80},
        "retailer_retailer": {"A": 40, "B": 40, "E": 60},
    },
    "load_unload_hours": {
        "load_origin": 0.5,
        "unload_platform": 0.25,
        "unload_retailer": 0.16,
    },

    # -- §11 Platform costs (borne only in own-sales-manager zones) --------
    "platform_order_cost": 0.65,         # per order platform -> factory
    "platform_deliverynote_cost": 0.15,  # per order delivered to a retailer
    "platform_storage_per_unit": 2.0,    # per unit of AVERAGE annual stock
    "platform_handling_per_unit": 0.0027,

    # -- §13 Sales force (channels S and T, markets A and B only) ---------
    "rep_fixed_min": 21_000.0,
    "rep_fixed_max": 42_000.0,
    "rep_variable_min": 0.006,
    "rep_variable_max": 0.012,           # % of PRICE TO RETAILER, normal units only

    # -- §15 Advertising rate card (per insertion) ------------------------
    "media_rate": {  # medium: (A/B in EUR, E in USD)
        "DR": (10_000.0, 11_000.0),
        "PR": (15_000.0, 16_000.0),
        "RA": (14_000.0, 16_000.0),
        "SM": (15_000.0, 15_000.0),
        "TV": (18_000.0, 20_000.0),
    },
    # -- §16 Scope: % of buyers reached by ONE insertion -------------------
    "media_scope": {  # medium: (A/B %, E %)
        "DR": (28.0, 26.0),
        "PR": (48.0, 31.0),
        "RA": (35.0, 40.0),
        "SM": (30.0, 29.0),
        "TV": (60.0, 61.0),
    },
    "media_names": {
        "DR": "Display network & remarketing",
        "PR": "Press (newspapers/magazines, print & online)",
        "RA": "Radio (conventional & online)",
        "SM": "Social media",
        "TV": "Television (conventional & online)",
    },

    # -- §17 Brand positioning --------------------------------------------
    "segment_weights": (0.40, 0.40, 0.20),
    "e_local_brands": ("J", "K", "L"),   # sit on E's three biggest segments, act as one

    # -- §18 Sales promotion ----------------------------------------------
    "max_promotions_per_channel_per_year": 3,
    "promotion_effect_weeks": 3,
    "weeks_per_year": 52,
    "promo_direct_gift_cost": 1.20,
    "promo_indirect_gift_cost": 3.60,

    # -- Synoptic Overview additions (not stated in the main scenario) -----
    "pop_max_per_channel": 500_000.0,      # PoS advertising cap, per channel per year
    "dumping_banned": True,                # cannot sell below production cost + retailer margin
    "smed_serves_multiple_lines": True,    # "One SMED unit can be used for several lines"
    "loan_term_decreases_each_year": True, # "term for new loans decreases each simulation year"
    "positioning_axis_x": "Natural",       # horizontal axis of the positioning map
    "positioning_axis_y": "Technological", # vertical axis
    "segment_x_share": 0.40,               # 40% seek Natural
    "segment_y_share": 0.40,               # 40% seek Technological
    "segment_neither_share": 0.20,         # 20% seek neither

    # -- §22 Production facilities ----------------------------------------
    "line_capex": {"S": 2_100_000.0, "H": 1_500_000.0},
    "max_total_lines": 32,               # any S/H combination
    # Lines are IRREVERSIBLE once installed (§22).

    # -- §23 Production capacity ------------------------------------------
    "line_capacity_per_shift": {"S": 240_000, "H": 600_000},
    "working_hours_per_shift_year": 2_000.0,
    "max_shifts": 3,

    # -- §24 Maintenance ---------------------------------------------------
    "breakdowns_per_2000h": 70,
    "repair_detect_hours": 0.5,          # detection & localization
    "repair_prep_hours": 0.5,            # preparation
    "repair_work_hours": 1.5,            # the actual repair
    "repair_crew": 4,                    # outside technicians per breakdown
    "repair_hourly_rate": 24.041,
    "module_interval_hours": 40.0,       # main module serviced every 40 operating hours
    "module_stop_hours": 5.0,            # 4 specialists x 5 hours, line halted
    "module_specialists": 4,

    # -- §25 Preventive maintenance ---------------------------------------
    "preventive_maintenance_cost": 500_000.0,
    "preventive_foresight": 0.70,        # 70% of breakdowns foreseen

    # -- §26 Quality control (Poka Yoke) — IRREVERSIBLE, once only --------
    "poka_yoke_capex_per_line": 720_000.0,

    # -- §27 SMED — IRREVERSIBLE, not available before year 2 -------------
    "smed_capex_per_module": 3_000_000.0,
    "smed_first_available_year": 2,

    # -- §28 Purchasing ----------------------------------------------------
    "rm_payment_terms_months": (0, 2, 3, 4),
    "rm_stockout_penalty": 0.15,         # +15% on units bought outside the plan

    # -- §29 Office & management staff (fixed expense) --------------------
    "office_headcount": {"I": 1, "II": 8, "III": 15, "IV": 32},
    "office_salary_range": {
        "I": (108_000.0, 150_000.0),
        "II": (72_124.0, 99_170.0),
        "III": (51_100.0, 72_124.0),
        "IV": (30_050.0, 42_075.0),
    },
    "general_overhead": 600_000.0,

    # -- §30 Direct production personnel ----------------------------------
    "specialist_salary_range": (21_000.0, 29_450.0),
    "operator_salary_range": (12_000.0, 16_830.0),
    "line_crew_per_shift": {             # per line, per shift
        "S": {"specialists": 9, "operators": 32},
        "H": {"specialists": 6, "operators": 23},
    },

    # -- §32 Selection & training (TS department) -------------------------
    "training_department_cost": 722_000.0,

    # -- §35 Depreciation on total fixed assets, by shift count -----------
    "depreciation_by_shifts": {1: 0.08, 2: 0.10, 3: 0.12},

    # -- §36 R&D: automatic, unavoidable ----------------------------------
    "rd_pct_of_revenue": 0.045,

    # -- §38 Customer payment terms ---------------------------------------
    "customer_terms_months": (2, 3, 4),

    # -- §49 Macro / financial / production factors (Director may change) --
    "per_capita_income": {"A": 27_000.0, "B": 35_000.0, "E": 46_000.0},  # E in USD
    "fx_eur_per_usd": 1.0,
    "unemployment_rate_AB": 0.07,
    "rm_unit_cost": {"S": 1.65, "H": 1.05},
    "power_cost_per_unit": {"S": 0.25, "H": 0.15},
    "loan_maturity_years": 4,
    "loan_interest": 0.10,
    "loan_upfront_fee": 0.01,
    "loan_prepayment_penalty": 0.01,
    "credit_line_interest": 0.07,
    "credit_line_service_fee": 0.01,
    "credit_line_upfront_fee": 0.01,
    "deposit_interest": 0.025,
    "deposit_early_withdrawal": 0.01,
    "investment_interest": 0.025,
    "investment_early_withdrawal": 0.01,
    "factoring_rate": 0.055,
    "overdraft_interest": 0.20,

    # -- §41 Operating cash needed ----------------------------------------
    "ocn_capex_pct": 0.80,
    "ocn_opex_pct": 0.50,
    "ocn_rm_pct": 0.15,

    # -- §50 Market research menu (EUR) -----------------------------------
    "research": {
        1:  ("Sales of S by market", 3_000.0),
        2:  ("Sales of H by market", 3_000.0),
        3:  ("Sales of S and H by company and market", 36_000.0),
        4:  ("Sales of S and H by company, market and channel", 72_000.0),
        5:  ("Promotional sales of S and H by company and market", 89_800.0),
        6:  ("Promotional sales of S and H by company, market and channel", 107_000.0),
        7:  ("Positioning of S brands by market", 59_900.0),
        8:  ("Positioning of H brands by market", 59_900.0),
        9:  ("Overseas advertising for S and H by companies from A and B", 36_000.0),
        10: ("Coverage of S and H advertising by company and market", 59_900.0),
        11: ("Number of advertising insertions for S and H by company", 36_000.0),
        12: ("Advertising for S and H by E domestic companies", 36_000.0),
        13: ("Investment in PoP advertising by company, market and channel", 59_900.0),
        14: ("Number of sales managers and sales reps by company and market", 24_000.0),
        15: ("Percentage of shelf space achieved for S and H by company and channel", 72_000.0),
        16: ("Accumulated investment in fixed assets by company", 49_000.0),
        17: ("Average overseas prices of S and H", 24_000.0),
        18: ("Total overseas sales of S and H by companies from A, B and E", 36_000.0),
        19: ("Demand for normal units of S and H by company and market", 110_000.0),
        20: ("Companies' S and H retail prices by market and channel", 0.0),
        21: ("Companies' advertising campaigns for S and H by market", 0.0),
        22: ("Type of promotion, for S and H, by company and channel", 0.0),
        23: ("Companies' end of year net income", 1_000.0),
        24: ("Industry's average production cost", 10_000.0),
        25: ("Industry's average salary cost", 5_000.0),
        26: ("Industry's end of year balance sheets", 10_000.0),
        27: ("Number of logistics platforms by company and market", 3_000.0),
        28: ("Companies' production shifts", 1_000.0),
    },

    # -- §51 Appendix: campaign counts ------------------------------------
    "campaigns": {"S": 20, "H": 20},
}

MARKETS = ("A", "B", "E")
PRODUCTS = ("S", "H")


# ---------------------------------------------------------------------------
# MARKET SIZING  (§3, §5)
# ---------------------------------------------------------------------------

def market_size(product: str, market: str) -> float:
    """Annual units demanded in a market at t0 (§3 per-capita x §2 population)."""
    return SCENARIO["population"][market] * SCENARIO["per_capita"][product][market]


def market_size_table() -> Dict[str, Dict[str, float]]:
    out: Dict[str, Dict[str, float]] = {}
    for p in PRODUCTS:
        row = {m: market_size(p, m) for m in MARKETS}
        row["TOTAL"] = sum(row.values())
        out[p] = row
    return out


def buyers(market: str) -> float:
    """Advertising target population: 25% of inhabitants (§5)."""
    return SCENARIO["population"][market] * SCENARIO["buyer_share_of_population"]


# ---------------------------------------------------------------------------
# CAPACITY  (§23, §24, §25, §26, §27)
# ---------------------------------------------------------------------------

@dataclass
class LineHours:
    """Hour budget for ONE line running `shifts` shifts for one year."""
    scheduled: float          # shifts x 2,000
    repair_hours: float       # time lost to breakdown repair
    module_hours: float       # time lost to main-module servicing (0 with SMED)
    operating: float          # hours actually producing
    breakdowns: float         # count
    scrap_hours: float        # production discarded (quality loss around breakdowns)

    @property
    def utilisation(self) -> float:
        return self.operating / self.scheduled

    @property
    def good_hours(self) -> float:
        """Operating hours whose output is sellable."""
        return self.operating - self.scrap_hours


def repair_hours_each(preventive: bool = False, poka_yoke: bool = False) -> float:
    """
    Average hours to clear one breakdown.

    §24 states 2.5 h = 0.5 detect + 0.5 prepare + 1.5 repair.
    §26 states Poka Yoke saves the detection/localisation time.
    §25 states preventive maintenance foresees ~70% of breakdowns, letting you
        "anticipate their detection and localization".
    §30 states the observed range is 1.5 - 2.5 h.

    ASSUMPTION (not stated in the scenario, and the reason the range exists):
    Poka Yoke removes detection on every breakdown; preventive maintenance
    additionally lets preparation be done in advance on the 70% it foresees.
    Both systems together approach the 1.5 h floor §30 quotes, which is the
    consistency check for this reading. Recalibrate from actual results.
    """
    s = SCENARIO
    detect = s["repair_detect_hours"]
    prep = s["repair_prep_hours"]
    work = s["repair_work_hours"]
    if poka_yoke:
        detect = 0.0
    elif preventive:
        detect *= (1.0 - s["preventive_foresight"])
    if preventive:
        prep *= (1.0 - s["preventive_foresight"])
    return detect + prep + work


def scrap_hours_each(preventive: bool = False, poka_yoke: bool = False) -> float:
    """
    Production discarded per breakdown, expressed in line-hours.

    §24: "These lost units usually match the ones produced during the time
    required to detect and locate the breakdown."  §26: Poka Yoke stops the line
    on anomaly, so the loss of quality "is avoided".
    """
    s = SCENARIO
    if poka_yoke:
        return 0.0
    h = s["repair_detect_hours"]
    if preventive:
        h *= (1.0 - s["preventive_foresight"])
    return h


def line_hours(
    shifts: int,
    preventive: bool = False,
    poka_yoke: bool = False,
    smed: bool = False,
    strict_module_counter: bool = False,
) -> LineHours:
    """
    Hour budget for one line.

    Module servicing (§24): "must be carried out every 40 line operating hours",
    4 specialists x 5 h with the whole process halted.

    Two defensible readings, 3% apart:
      * default (conservative): 2,000 / 40 = 50 stops per shift-year -> 250 h lost.
      * strict_module_counter=True: the 40 h counter advances only while the line
        actually operates, which solves to operating = (scheduled - repair)/1.125.
    The default is the conservative one on purpose: under-promising production is
    the safe direction of error in a CEO forecast.

    SMED (§27) performs the servicing outside the process, so module_hours -> 0.
    """
    s = SCENARIO
    scheduled = s["working_hours_per_shift_year"] * shifts
    n_breakdowns = s["breakdowns_per_2000h"] * shifts
    repair = n_breakdowns * repair_hours_each(preventive, poka_yoke)

    if smed:
        module = 0.0
        operating = scheduled - repair
    elif strict_module_counter:
        ratio = s["module_stop_hours"] / s["module_interval_hours"]  # 0.125
        operating = (scheduled - repair) / (1.0 + ratio)
        module = operating * ratio
    else:
        module = (scheduled / s["module_interval_hours"]) * s["module_stop_hours"]
        operating = scheduled - repair - module

    scrap = n_breakdowns * scrap_hours_each(preventive, poka_yoke)
    return LineHours(scheduled, repair, module, operating, n_breakdowns, scrap)


def units_per_hour(product: str) -> float:
    """Nameplate line speed (§23): capacity per shift / 2,000 h."""
    return (SCENARIO["line_capacity_per_shift"][product]
            / SCENARIO["working_hours_per_shift_year"])


@dataclass
class Capacity:
    s_lines: int
    h_lines: int
    shifts: int
    hours: LineHours
    s_units: float = 0.0        # sellable units of S
    h_units: float = 0.0        # sellable units of H
    s_scrapped: float = 0.0     # units started and discarded
    h_scrapped: float = 0.0
    s_nameplate: float = 0.0
    h_nameplate: float = 0.0

    @property
    def utilisation(self) -> float:
        return self.hours.utilisation

    def summary(self) -> str:
        lines = [
            f"Capacity: {self.s_lines} S line(s) + {self.h_lines} H line(s) x {self.shifts} shift(s)",
            f"  hours/line: scheduled {self.hours.scheduled:,.0f}"
            f" | repair {self.hours.repair_hours:,.1f}"
            f" | module stops {self.hours.module_hours:,.1f}"
            f" | operating {self.hours.operating:,.1f}"
            f" ({self.hours.utilisation:.2%} of nameplate)",
            f"  S: {self.s_units:,.0f} sellable of {self.s_nameplate:,.0f} nameplate"
            f"  (scrap {self.s_scrapped:,.0f})",
            f"  H: {self.h_units:,.0f} sellable of {self.h_nameplate:,.0f} nameplate"
            f"  (scrap {self.h_scrapped:,.0f})",
        ]
        return "\n".join(lines)


def capacity(
    s_lines: int = 0,
    h_lines: int = 0,
    shifts: int = 1,
    preventive: bool = False,
    poka_yoke: bool = False,
    smed: bool = False,
    strict_module_counter: bool = False,
) -> Capacity:
    """Sellable annual output given the plant configuration."""
    s = SCENARIO
    total = s_lines + h_lines
    if total > s["max_total_lines"]:
        raise ValueError(
            f"{total} lines exceeds the {s['max_total_lines']}-line factory limit (§22)")
    if not 1 <= shifts <= s["max_shifts"]:
        raise ValueError(f"shifts must be 1..{s['max_shifts']} (§23)")

    h = line_hours(shifts, preventive, poka_yoke, smed, strict_module_counter)
    cap = Capacity(s_lines, h_lines, shifts, h)
    cap.s_units = h.good_hours * units_per_hour("S") * s_lines
    cap.h_units = h.good_hours * units_per_hour("H") * h_lines
    cap.s_scrapped = h.scrap_hours * units_per_hour("S") * s_lines
    cap.h_scrapped = h.scrap_hours * units_per_hour("H") * h_lines
    cap.s_nameplate = s["line_capacity_per_shift"]["S"] * shifts * s_lines
    cap.h_nameplate = s["line_capacity_per_shift"]["H"] * shifts * h_lines
    return cap


def capex_per_annual_unit(product: str, shifts: int = 3, **kw) -> float:
    """
    Euros of irreversible line investment per unit of SELLABLE annual capacity.
    The cleanest single comparison between an S line and an H line (§22, §23).
    """
    cap = capacity(**{f"{product.lower()}_lines": 1}, shifts=shifts, **kw)
    units = cap.s_units if product == "S" else cap.h_units
    return SCENARIO["line_capex"][product] / units


# ---------------------------------------------------------------------------
# STANDARD COST  (§33, §24, §30, §49)
# ---------------------------------------------------------------------------

@dataclass
class StandardCost:
    product: str
    raw_material: float = 0.0
    power: float = 0.0
    labour: float = 0.0
    breakdown_repair: float = 0.0

    @property
    def total(self) -> float:
        return self.raw_material + self.power + self.labour + self.breakdown_repair

    def summary(self) -> str:
        return (f"SC({self.product}) = RM {self.raw_material:.4f}"
                f" + power {self.power:.4f}"
                f" + labour {self.labour:.4f}"
                f" + repairs {self.breakdown_repair:.4f}"
                f" = EUR {self.total:.4f}/unit")


def standard_cost(
    product: str,
    lines: int,
    shifts: int,
    specialist_salary: Optional[float] = None,
    operator_salary: Optional[float] = None,
    preventive: bool = False,
    poka_yoke: bool = False,
    smed: bool = False,
    smed_teams_per_shift: int = 0,
    rm_unit_cost: Optional[float] = None,
    strict_module_counter: bool = False,
) -> StandardCost:
    """
    Standard cost of ONE sellable unit (§33: raw materials + power + personnel),
    plus the breakdown-repair charge §24 says is "added to the standard
    production cost".

    Salaries default to the legal minimum of each range (§30) — that is the cost
    floor, not a recommendation; see docs/02 on turnover and absenteeism.
    """
    s = SCENARIO
    if product not in PRODUCTS:
        raise ValueError(f"product must be one of {PRODUCTS}")
    spec_pay = specialist_salary if specialist_salary is not None else s["specialist_salary_range"][0]
    oper_pay = operator_salary if operator_salary is not None else s["operator_salary_range"][0]
    rm_cost = rm_unit_cost if rm_unit_cost is not None else s["rm_unit_cost"][product]

    h = line_hours(shifts, preventive, poka_yoke, smed, strict_module_counter)
    rate = units_per_hour(product)
    good = h.good_hours * rate * lines
    started = h.operating * rate * lines
    if good <= 0:
        raise ValueError("configuration produces no sellable units")

    crew = s["line_crew_per_shift"][product]
    crew_cost = (crew["specialists"] * spec_pay + crew["operators"] * oper_pay) * shifts * lines
    if smed and smed_teams_per_shift:
        # §27: SMED teams are 4 specialists per team, paid as production specialists.
        crew_cost += (s["module_specialists"] * spec_pay
                      * smed_teams_per_shift * shifts * lines)

    repair_cost = (h.breakdowns * repair_hours_each(preventive, poka_yoke)
                   * s["repair_crew"] * s["repair_hourly_rate"] * lines)

    sc = StandardCost(product)
    # §34: raw material is consumed by every unit STARTED, including scrap.
    sc.raw_material = rm_cost * started / good
    sc.power = s["power_cost_per_unit"][product] * started / good
    sc.labour = crew_cost / good
    sc.breakdown_repair = repair_cost / good
    return sc


def weighted_average_sc(
    opening_units: float, opening_sc: float, produced_units: float, current_sc: float
) -> float:
    """SCM — the weighted average of opening inventory and current production (§33, §34)."""
    total = opening_units + produced_units
    if total <= 0:
        return current_sc
    return (opening_units * opening_sc + produced_units * current_sc) / total


def raw_material_units_needed(produced: float, scrapped: float, opening_stock: float = 0.0) -> float:
    """
    §34: subtract the units USED, not the units produced. Scrap consumes raw
    material. Under-ordering costs +15% on the shortfall (§28).
    """
    return max(0.0, produced + scrapped - opening_stock)


# ---------------------------------------------------------------------------
# LOGISTICS  (§10, §11, §12)
# ---------------------------------------------------------------------------

def vehicle_annual_cost(load_kg: float, fx_eur_per_usd: Optional[float] = None,
                        market: str = "A") -> float:
    """§10: 24,000 + 1.2 x load capacity in kg. In E, apply the exchange rate."""
    s = SCENARIO
    cost = s["vehicle_fixed_cost"] + s["vehicle_cost_per_kg"] * load_kg
    if market == "E":
        fx = fx_eur_per_usd if fx_eur_per_usd is not None else s["fx_eur_per_usd"]
        cost *= fx
    return cost


def units_per_vehicle_year(load_kg: float, route_hours: float) -> float:
    """A vehicle runs 2,000 h/yr; each route moves load_kg x 2 units (§10)."""
    s = SCENARIO
    routes = s["vehicle_uptime_hours"] / route_hours
    return load_kg * s["units_per_kg"] * routes


def marginal_cost_per_unit(load_kg: float, route_hours: Optional[float] = None,
                           market: str = "A") -> float:
    """
    Transport cost per unit for a FULLY LOADED vehicle of this size — the clean
    economic comparison between load capacities, before whole-vehicle rounding.

    Your realised cost is this figure divided by the fleet's fill rate, so a
    volume that leaves the last vehicle half empty pays roughly double on that
    vehicle. Size the fleet, then check the realised figure with
    plan_factory_to_platform().
    """
    rh = route_hours if route_hours is not None else SCENARIO["f2p_route_hours"]
    return vehicle_annual_cost(load_kg, market=market) / units_per_vehicle_year(load_kg, rh)


@dataclass
class LogisticsLeg:
    leg: str
    market: str
    load_kg: float
    route_hours: float
    vehicles: int
    units: float
    total_cost: float

    @property
    def cost_per_unit(self) -> float:
        return self.total_cost / self.units if self.units else float("nan")


def plan_factory_to_platform(units: float, market: str = "A",
                             load_kg: Optional[float] = None,
                             fx_eur_per_usd: Optional[float] = None) -> LogisticsLeg:
    """
    Vehicles needed to move `units` from the factory to every platform (§10).
    Cost is borne by the manufacturer in ALL zones, wholesaler zones included.
    """
    s = SCENARIO
    load_kg = float(load_kg if load_kg is not None else s["f2p_kg_max"])
    if not s["f2p_kg_min"] <= load_kg <= s["f2p_kg_max"]:
        raise ValueError(f"load must be {s['f2p_kg_min']}-{s['f2p_kg_max']} kg (§10)")
    per_vehicle = units_per_vehicle_year(load_kg, s["f2p_route_hours"])
    n = max(1, math.ceil(units / per_vehicle))   # §12: zero is not a legal entry
    cost = n * vehicle_annual_cost(load_kg, fx_eur_per_usd, market)
    return LogisticsLeg("factory->platform", market, load_kg,
                        s["f2p_route_hours"], n, units, cost)


def estimate_p2r_route_hours(market: str, platforms: int, retailers_served: int,
                             drops_per_route: int) -> float:
    """
    Estimate one platform->retailer route in hours from the scenario's geometry.

    §8 says the territory is homogeneous with retailers uniformly distributed and
    that "certain large companies apply geometric operational research methods"
    rather than trial and error. This is that calculation.

      time = load 0.5 h
           + travel platform -> first retailer   (at platform_retailer speed)
           + per drop: unload 0.16 h + hop to the next retailer
                                                 (at retailer_retailer speed)
           + return leg to the platform

    ASSUMPTION: a platform serves an equal share of the territory, so its service
    area is surface/platforms; mean platform-to-area distance is taken as
    0.5*sqrt(area) and retailer spacing as sqrt(area/retailers_in_area). These are
    standard uniform-density approximations, NOT scenario constants.

    *** DO NOT TRUST THIS FOR PLANNING. *** At realistic volumes it returns route
    times above 100 hours and an implied cost roughly 20x the EUR 0.007/unit that
    §12 calls reasonable, because the scenario never fixes retailer spacing or
    drop density. Use size_from_benchmark() instead and calibrate from actuals.
    It is kept only to show the geometric method §8 alludes to.
    """
    s = SCENARIO
    area = s["surface_km2"][market] / max(1, platforms)
    side = math.sqrt(area)
    approach_km = 0.5 * side
    spacing_km = math.sqrt(area / max(1, retailers_served)) if retailers_served else 0.0

    v_out = s["speed_kmh"]["platform_retailer"][market]
    v_hop = s["speed_kmh"]["retailer_retailer"][market]

    t = s["load_unload_hours"]["load_origin"]
    t += approach_km / v_out                                   # out
    t += drops_per_route * s["load_unload_hours"]["unload_retailer"]
    t += max(0, drops_per_route - 1) * spacing_km / v_hop      # between drops
    t += approach_km / v_out                                   # back
    return t


def plan_platform_to_retailer(units: float, market: str, platforms: int,
                              retailers: int, load_kg: Optional[float] = None,
                              route_hours: Optional[float] = None,
                              fx_eur_per_usd: Optional[float] = None) -> LogisticsLeg:
    """
    Last-mile vehicles, needed ONLY in zones run by your own sales managers (§12).
    Retailers order weekly, 52 weeks a year (§12).
    """
    s = SCENARIO
    load_kg = float(load_kg if load_kg is not None else s["p2r_kg_max"])
    if not s["p2r_kg_min"] <= load_kg <= s["p2r_kg_max"]:
        raise ValueError(f"load must be {s['p2r_kg_min']}-{s['p2r_kg_max']} kg (§12)")

    weekly_units_per_retailer = units / max(1, retailers) / s["weeks_per_year"]
    capacity_units = load_kg * s["units_per_kg"]
    drops = max(1, int(capacity_units // max(1.0, weekly_units_per_retailer)))
    drops = min(drops, max(1, retailers // max(1, platforms)))

    if route_hours is None:
        route_hours = estimate_p2r_route_hours(
            market, platforms, max(1, retailers // max(1, platforms)), drops)

    per_vehicle = units_per_vehicle_year(load_kg, route_hours)
    n = max(1, math.ceil(units / per_vehicle))
    cost = n * vehicle_annual_cost(load_kg, fx_eur_per_usd, market)
    return LogisticsLeg("platform->retailer", market, load_kg, route_hours, n, units, cost)


def optimal_vehicle_plan(units: float, leg: str = "f2p", market: str = "A",
                         route_hours: Optional[float] = None) -> LogisticsLeg:
    """
    The cheapest legal fleet for a known volume — and the reason the naive
    "always buy the biggest vehicle" rule is only half right.

    Substituting the smallest capacity that still covers the volume with n
    vehicles, kg = units / (units_per_kg x routes x n), into the §10 cost
    formula collapses it to:

        total cost = 24,000 x n  +  0.0024 x units        (factory->platform)

    The per-kilogram term is INVARIANT once the fleet exactly covers the volume.
    So the decision is not "how big" but "how few": minimise the vehicle COUNT,
    then size each vehicle exactly to the volume it must carry. Buying maximum
    capacity is right only when it also minimises the count — otherwise you pay
    1.2 EUR/kg for load you never fill.

    Returns the cheapest plan; `.cost_per_unit` is the realised figure to compare
    against the §10/§12 benchmark.
    """
    s = SCENARIO
    if leg == "f2p":
        lo, hi, rh = s["f2p_kg_min"], s["f2p_kg_max"], s["f2p_route_hours"]
    else:
        lo, hi = s["p2r_kg_min"], s["p2r_kg_max"]
        rh = route_hours if route_hours is not None else 4.0

    per_kg_year = s["units_per_kg"] * (s["vehicle_uptime_hours"] / rh)
    n_min = max(1, math.ceil(units / (per_kg_year * hi)))

    best: Optional[LogisticsLeg] = None
    for n in range(n_min, n_min + 4):          # a couple of extra vehicles, just in case
        kg = max(lo, math.ceil(units / (per_kg_year * n)))
        if kg > hi:
            continue
        cost = n * vehicle_annual_cost(kg, market=market)
        cand = LogisticsLeg(
            "factory->platform" if leg == "f2p" else "platform->retailer",
            market, float(kg), rh, n, units, cost)
        if best is None or cand.total_cost < best.total_cost:
            best = cand
    assert best is not None
    return best


def size_from_benchmark(units: float, leg: str = "p2r", market: str = "A",
                        target_per_unit: Optional[float] = None) -> Dict[str, object]:
    """
    Size a fleet by working BACKWARDS from the scenario's own cost benchmark.

    WHY THIS EXISTS. estimate_p2r_route_hours() applies textbook uniform-density
    geometry to the platform->retailer leg and produces route times of 100+ hours
    for realistic volumes — implying a cost around 20x the EUR 0.007/unit that
    §12 itself calls reasonable. The geometry is therefore NOT trustworthy for
    this leg: the scenario never states the retailer spacing or the drop density,
    so the approximation has nothing solid under it.

    Rather than present a confident wrong number, this function inverts the
    problem: §12 says roughly EUR 0.007 per unit is achievable, so the fleet that
    achieves it is the sensible opening bid. Submit it, read your ACTUAL transport
    cost and any logistic-stockout flag from the results, then correct.

    §8 explicitly endorses this: a theoretical logistic stockout means you were
    short of vehicles (the logistics company covers it at a higher price, so you
    lose money but never a sale); an actual cost BELOW the benchmark with no
    stockout means you are over-provisioned and should cut back.
    """
    s = SCENARIO
    if leg == "f2p":
        lo, hi = s["f2p_kg_min"], s["f2p_kg_max"]
        target = target_per_unit or s["f2p_benchmark_per_unit"]
    else:
        lo, hi = s["p2r_kg_min"], s["p2r_kg_max"]
        target = target_per_unit or s["p2r_benchmark_per_unit"]

    budget = target * units
    options = []
    for kg in range(lo, hi + 1, 500 if lo < 1000 else 1000):
        per_vehicle = vehicle_annual_cost(kg, market=market)
        n = max(1, int(budget // per_vehicle))
        cost = n * per_vehicle
        options.append({"load_kg": kg, "vehicles": n, "total_cost": cost,
                        "cost_per_unit": cost / units,
                        "gap_to_benchmark": cost / units - target})
    # closest to the benchmark without going under it by much
    best = min(options, key=lambda o: abs(o["gap_to_benchmark"]))
    return {"benchmark_per_unit": target, "budget": budget, "recommended": best,
            "note": "OPENING BID ONLY — correct from year-1 actual cost and "
                    "logistic-stockout flags (§8, §12)."}


def vehicle_size_scan(units: float, leg: str = "f2p", market: str = "A",
                      route_hours: Optional[float] = None,
                      steps: Iterable[int] = ()) -> List[Tuple[int, int, float, float]]:
    """
    Cost per unit across the legal load-capacity range. Returns
    (load_kg, vehicles, total_cost, cost_per_unit) sorted cheapest first.
    """
    s = SCENARIO
    if leg == "f2p":
        lo, hi = s["f2p_kg_min"], s["f2p_kg_max"]
        rh = s["f2p_route_hours"]
    else:
        lo, hi = s["p2r_kg_min"], s["p2r_kg_max"]
        rh = route_hours if route_hours is not None else 4.0
    if not steps:
        steps = [lo] + list(range(int(math.ceil(lo / 1000.0) * 1000), hi + 1, 1000))
        steps = sorted(set(k for k in steps if lo <= k <= hi))

    rows = []
    for kg in steps:
        per_vehicle = units_per_vehicle_year(kg, rh)
        n = max(1, math.ceil(units / per_vehicle))
        cost = n * vehicle_annual_cost(kg, market=market)
        rows.append((kg, n, cost, cost / units))
    return sorted(rows, key=lambda r: r[3])


def platform_costs(units_in_own_zones: float, platforms_in_own_zones: int,
                   retailers_in_own_zones: int, orders_to_factory_per_platform: int = 52,
                   average_stock_units: Optional[float] = None,
                   fx_eur_per_usd: Optional[float] = None, market: str = "A") -> Dict[str, float]:
    """
    Platform running costs (§11). Borne ONLY where you have your own sales
    manager; in wholesaler zones these sit inside the 8.46% commission (§7).
    """
    s = SCENARIO
    fx = fx_eur_per_usd if fx_eur_per_usd is not None else s["fx_eur_per_usd"]
    mult = fx if market == "E" else 1.0

    if average_stock_units is None:
        # ASSUMPTION: weekly replenishment -> average stock is half a week of sales.
        average_stock_units = units_in_own_zones / s["weeks_per_year"] / 2.0

    admin = platforms_in_own_zones * orders_to_factory_per_platform * s["platform_order_cost"]
    notes = retailers_in_own_zones * s["weeks_per_year"] * s["platform_deliverynote_cost"]
    storage = average_stock_units * s["platform_storage_per_unit"]
    handling = units_in_own_zones * s["platform_handling_per_unit"]
    out = {"orders": admin * mult, "delivery_notes": notes * mult,
           "storage": storage * mult, "handling": handling * mult}
    out["total"] = sum(out.values())
    return out


def export_cost_per_unit(standard_cost_unit: float) -> Dict[str, float]:
    """
    §9: the fixed export chain is 0.024 EUR/unit; the 2% ad valorem duty applies
    ONLY to cargo bound for platforms run by your own sales managers — in
    wholesaler zones it is already inside the 8.46%.
    """
    s = SCENARIO
    fixed = s["export_fixed_per_unit"]
    duty = (standard_cost_unit + fixed) * s["customs_duty_pct"]
    return {"fixed": fixed, "duty_own_zones": duty, "total_own_zones": fixed + duty,
            "total_wholesaler_zones": fixed}


# ---------------------------------------------------------------------------
# DISTRIBUTION: own sales managers vs. wholesalers  (§6, §7, §11, §13)
# ---------------------------------------------------------------------------

@dataclass
class DistributionComparison:
    market: str
    zones_owned: int
    units: float
    retail_price: float
    wholesaler_cost: float
    own_cost: float

    @property
    def advantage(self) -> float:
        """Positive = owning the zone is cheaper."""
        return self.wholesaler_cost - self.own_cost

    def summary(self) -> str:
        verdict = "OWN SALES MANAGERS" if self.advantage > 0 else "WHOLESALERS"
        return (f"{self.market}: {self.units:,.0f} units @ EUR {self.retail_price:.2f}"
                f" | wholesaler EUR {self.wholesaler_cost:,.0f}"
                f" vs own EUR {self.own_cost:,.0f}"
                f" -> {verdict} by EUR {abs(self.advantage):,.0f}")


def distribution_compare(market: str, units: float, retail_price: float,
                         zones_owned: int, platforms: int, retailers: int,
                         reps_per_zone: int = 0,
                         rep_fixed: Optional[float] = None,
                         rep_variable: float = 0.0,
                         price_to_retailer: Optional[float] = None,
                         fx_eur_per_usd: Optional[float] = None) -> DistributionComparison:
    """
    Full cost of serving `units` in `zones_owned` zones yourself, against the
    wholesaler commission you would otherwise pay on the same units.

    Own cost = sales managers (§6) + reps fixed & variable (§13)
             + platform running costs (§11) + last-mile vehicles (§12).
    Factory->platform transport is EXCLUDED from both sides: §8 says the
    manufacturer pays it either way, so it does not affect the choice.
    """
    s = SCENARIO
    fx = fx_eur_per_usd if fx_eur_per_usd is not None else s["fx_eur_per_usd"]
    rep_fixed = rep_fixed if rep_fixed is not None else s["rep_fixed_min"]
    ptr = price_to_retailer if price_to_retailer is not None else retail_price

    wholesaler = units * retail_price * s["wholesaler_pct_normal"]

    mgr_unit = s["sales_manager_cost"][market] * (fx if market == "E" else 1.0)
    own = zones_owned * mgr_unit
    if market in ("A", "B") and reps_per_zone:
        # §13: reps exist only for channels S and T, i.e. only in A and B.
        own += zones_owned * reps_per_zone * rep_fixed
        own += units * ptr * rep_variable
    own += platform_costs(units, platforms, retailers, market=market,
                          fx_eur_per_usd=fx)["total"]
    own += plan_platform_to_retailer(units, market, platforms, retailers,
                                     fx_eur_per_usd=fx).total_cost

    return DistributionComparison(market, zones_owned, units, retail_price,
                                  wholesaler, own)


def wholesaler_breakeven_units(market: str, retail_price: float, zones_owned: int,
                               platforms: int, retailers: int, reps_per_zone: int = 0,
                               rep_fixed: Optional[float] = None,
                               lo: float = 1_000.0, hi: float = 200_000_000.0) -> float:
    """Units at which owning the zones stops costing more than the 8.46% commission."""
    def delta(u: float) -> float:
        c = distribution_compare(market, u, retail_price, zones_owned, platforms,
                                 retailers, reps_per_zone, rep_fixed)
        return c.advantage
    if delta(hi) < 0:
        return float("inf")          # wholesalers win at every legal volume
    if delta(lo) > 0:
        return lo                    # own network wins from the first unit
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if delta(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


# ---------------------------------------------------------------------------
# ADVERTISING  (§15, §16)
# ---------------------------------------------------------------------------

def media_rate(medium: str, market: str) -> float:
    ab, e = SCENARIO["media_rate"][medium]
    return e if market == "E" else ab


def media_scope(medium: str, market: str) -> float:
    """Percent of buyers reached by ONE insertion (§16)."""
    ab, e = SCENARIO["media_scope"][medium]
    return e if market == "E" else ab


def cost_per_reach_point(medium: str, market: str) -> float:
    """Currency per 1% of the buyer base reached, per insertion. Lower is better."""
    return media_rate(medium, market) / media_scope(medium, market)


def media_efficiency(market: str) -> List[Tuple[str, float, float, float]]:
    """(medium, rate, scope %, cost per reach point) sorted cheapest first."""
    rows = [(m, media_rate(m, market), media_scope(m, market),
             cost_per_reach_point(m, market)) for m in SCENARIO["media_rate"]]
    return sorted(rows, key=lambda r: r[3])


@dataclass
class AdPlan:
    market: str
    insertions: Dict[str, int]
    cost: float
    grps: float
    net_reach_pct: float
    average_frequency: float

    def summary(self) -> str:
        mix = ", ".join(f"{m}x{n}" for m, n in self.insertions.items() if n)
        return (f"{self.market}: {mix or 'no advertising'}"
                f" | cost {self.cost:,.0f}"
                f" | GRPs {self.grps:,.0f}"
                f" | net reach {self.net_reach_pct:.1f}% of buyers"
                f" | avg frequency {self.average_frequency:.1f}")


def advertising(market: str, insertions: Dict[str, int]) -> AdPlan:
    """
    Cost, GRPs and net reach for a media mix.

    §16 defines scope as the share of buyers reached by one insertion, and
    insertions as frequency on that audience. Media overlap, so net reach across
    media is taken as 1 - PROD(1 - scope_i) over the media actually used — the
    standard random-duplication model. GRPs = sum(scope x insertions).
    """
    cost = 0.0
    grps = 0.0
    unreached = 1.0
    for medium, n in insertions.items():
        if medium not in SCENARIO["media_rate"]:
            raise ValueError(f"unknown medium {medium!r}")
        if not n:
            continue
        cost += n * media_rate(medium, market)
        scope = media_scope(medium, market) / 100.0
        grps += scope * 100.0 * n
        unreached *= (1.0 - scope)
    reach = (1.0 - unreached) * 100.0
    freq = grps / reach if reach else 0.0
    return AdPlan(market, dict(insertions), cost, grps, reach, freq)


def cheapest_mix_for_reach(market: str, target_reach_pct: float) -> Dict[str, int]:
    """
    Greedy: add the medium with the lowest cost per incremental reach point until
    the net-reach target is met. One insertion per medium buys the reach; extra
    insertions buy frequency, not reach (§16).
    """
    chosen: Dict[str, int] = {}
    unreached = 1.0
    while (1.0 - unreached) * 100.0 < target_reach_pct:
        best, best_cost = None, float("inf")
        for m in SCENARIO["media_rate"]:
            if m in chosen:
                continue
            scope = media_scope(m, market) / 100.0
            gain = unreached * scope * 100.0
            if gain <= 0:
                continue
            c = media_rate(m, market) / gain
            if c < best_cost:
                best, best_cost = m, c
        if best is None:
            break
        chosen[best] = 1
        unreached *= (1.0 - media_scope(best, market) / 100.0)
    return chosen


# ---------------------------------------------------------------------------
# HUMAN RESOURCES  (§29, §30, §32)
# ---------------------------------------------------------------------------

def office_payroll(salaries: Optional[Dict[str, float]] = None) -> float:
    """Annual fixed office and management payroll (§29)."""
    s = SCENARIO
    total = 0.0
    for level, headcount in s["office_headcount"].items():
        lo, hi = s["office_salary_range"][level]
        pay = salaries.get(level, lo) if salaries else lo
        if not lo <= pay <= hi:
            raise ValueError(f"level {level} salary must be {lo:,.0f}-{hi:,.0f} (§29)")
        total += headcount * pay
    return total


def office_payroll_range() -> Tuple[float, float]:
    s = SCENARIO
    lo = sum(n * s["office_salary_range"][lv][0] for lv, n in s["office_headcount"].items())
    hi = sum(n * s["office_salary_range"][lv][1] for lv, n in s["office_headcount"].items())
    return lo, hi


def production_headcount(s_lines: int, h_lines: int, shifts: int,
                         smed_teams_per_shift: int = 0) -> Dict[str, int]:
    """Direct production personnel on the payroll (§30). One shift each, no overtime."""
    s = SCENARIO
    spec = (s["line_crew_per_shift"]["S"]["specialists"] * s_lines
            + s["line_crew_per_shift"]["H"]["specialists"] * h_lines) * shifts
    oper = (s["line_crew_per_shift"]["S"]["operators"] * s_lines
            + s["line_crew_per_shift"]["H"]["operators"] * h_lines) * shifts
    smed = s["module_specialists"] * smed_teams_per_shift * shifts
    return {"specialists": spec, "operators": oper, "smed_specialists": smed,
            "total": spec + oper + smed}


# ---------------------------------------------------------------------------
# FINANCE: P&L, balance sheet, OCN  (§35, §36, §37, §41, §47, §49)
# ---------------------------------------------------------------------------

@dataclass
class SalesLine:
    """One product x market x channel row of the commercial plan."""
    product: str
    market: str
    channel: str
    units_normal: float = 0.0
    units_promo: float = 0.0
    retail_price: float = 0.0        # MSRP — §14, revenue is booked at this price
    retailer_margin: float = 0.0     # EUR per unit, §20
    wholesaler_share: float = 0.0    # 0..1 of units flowing through wholesaler zones
    promo_cost: float = 0.0          # direct promotional spend, §18

    @property
    def units(self) -> float:
        return self.units_normal + self.units_promo

    @property
    def revenue(self) -> float:
        return self.units * self.retail_price

    @property
    def retailer_cost(self) -> float:
        return self.units * self.retailer_margin

    @property
    def wholesaler_cost(self) -> float:
        s = SCENARIO
        return (self.units_normal * self.wholesaler_share
                * self.retail_price * s["wholesaler_pct_normal"]
                + self.units_promo * self.wholesaler_share
                * self.retail_price * s["wholesaler_pct_promo"])


@dataclass
class IncomeStatement:
    revenue: float = 0.0
    retailer_margins: float = 0.0
    wholesaler_margins: float = 0.0
    promotions: float = 0.0
    cogs: float = 0.0
    advertising: float = 0.0
    pop: float = 0.0
    sales_force: float = 0.0
    logistics: float = 0.0
    office_payroll: float = 0.0
    overhead: float = 0.0
    market_research: float = 0.0
    preventive_maintenance: float = 0.0
    training_department: float = 0.0
    rd: float = 0.0
    depreciation: float = 0.0
    financial_expenses: float = 0.0
    financial_income: float = 0.0
    other: float = 0.0

    @property
    def net_sales(self) -> float:
        """§47: retail invoicing less retailer and wholesaler margins and promotions."""
        return (self.revenue - self.retailer_margins
                - self.wholesaler_margins - self.promotions)

    @property
    def gross_margin(self) -> float:
        return self.net_sales - self.cogs

    @property
    def operating_expenses(self) -> float:
        return (self.advertising + self.pop + self.sales_force + self.logistics
                + self.office_payroll + self.overhead + self.market_research
                + self.preventive_maintenance + self.training_department
                + self.rd + self.depreciation + self.other)

    @property
    def operating_income(self) -> float:
        return self.gross_margin - self.operating_expenses

    @property
    def net_income(self) -> float:
        # No corporate income tax is specified anywhere in the scenario.
        return self.operating_income - self.financial_expenses + self.financial_income

    @property
    def operating_margin(self) -> float:
        return self.operating_income / self.revenue if self.revenue else 0.0

    @property
    def net_margin(self) -> float:
        return self.net_income / self.revenue if self.revenue else 0.0

    def render(self) -> str:
        w = 34
        rows = [
            ("Revenue (at retail price)", self.revenue),
            ("  less retailer margins", -self.retailer_margins),
            ("  less wholesaler margins", -self.wholesaler_margins),
            ("  less promotions", -self.promotions),
            ("NET SALES", self.net_sales),
            ("  less cost of goods sold", -self.cogs),
            ("GROSS MARGIN", self.gross_margin),
            ("  advertising", -self.advertising),
            ("  point-of-purchase", -self.pop),
            ("  sales force & managers", -self.sales_force),
            ("  logistics", -self.logistics),
            ("  office payroll", -self.office_payroll),
            ("  general overhead", -self.overhead),
            ("  market research", -self.market_research),
            ("  preventive maintenance", -self.preventive_maintenance),
            ("  training department", -self.training_department),
            ("  R&D (4.5% of revenue)", -self.rd),
            ("  depreciation", -self.depreciation),
            ("  other", -self.other),
            ("OPERATING INCOME", self.operating_income),
            ("  financial expenses", -self.financial_expenses),
            ("  financial income", self.financial_income),
            ("NET INCOME", self.net_income),
        ]
        out = [f"{'':<{w}}{'EUR':>16}"]
        for label, value in rows:
            out.append(f"{label:<{w}}{value:>16,.0f}")
        out.append("")
        out.append(f"{'Operating margin':<{w}}{self.operating_margin:>15.2%}")
        out.append(f"{'Net margin':<{w}}{self.net_margin:>15.2%}")
        return "\n".join(out)


def build_income_statement(
    sales: Iterable[SalesLine],
    sc_by_product: Dict[str, float],
    advertising_spend: float = 0.0,
    pop_spend: float = 0.0,
    sales_force_cost: float = 0.0,
    logistics_cost: float = 0.0,
    office_salaries: Optional[Dict[str, float]] = None,
    market_research_spend: float = 0.0,
    preventive: bool = False,
    training_dept: bool = False,
    fixed_assets: float = 0.0,
    shifts: int = 1,
    financial_expenses: float = 0.0,
    financial_income: float = 0.0,
    other: float = 0.0,
) -> IncomeStatement:
    """Projected income statement for one simulated year (§47)."""
    s = SCENARIO
    inc = IncomeStatement()
    for line in sales:
        inc.revenue += line.revenue
        inc.retailer_margins += line.retailer_cost
        inc.wholesaler_margins += line.wholesaler_cost
        inc.promotions += line.promo_cost
        inc.cogs += line.units * sc_by_product.get(line.product, 0.0)

    inc.advertising = advertising_spend
    inc.pop = pop_spend
    inc.sales_force = sales_force_cost
    inc.logistics = logistics_cost
    inc.office_payroll = office_payroll(office_salaries)
    inc.overhead = s["general_overhead"]
    inc.market_research = market_research_spend
    inc.preventive_maintenance = s["preventive_maintenance_cost"] if preventive else 0.0
    inc.training_department = s["training_department_cost"] if training_dept else 0.0
    inc.rd = inc.revenue * s["rd_pct_of_revenue"]
    inc.depreciation = fixed_assets * s["depreciation_by_shifts"][shifts]
    inc.financial_expenses = financial_expenses
    inc.financial_income = financial_income
    inc.other = other
    return inc


def roe(net_income: float, opening_equity: Optional[float] = None) -> float:
    """Return on equity. Equity cannot be increased (§37); it grows only by retained profit."""
    eq = opening_equity if opening_equity is not None else SCENARIO["opening_equity"]
    return net_income / eq if eq else 0.0


def operating_cash_needed(new_capex: float = 0.0, advertising_spend: float = 0.0,
                          pop_spend: float = 0.0, sales_manager_spend: float = 0.0,
                          rep_fixed_salaries: float = 0.0,
                          market_research_spend: float = 0.0,
                          overhead: Optional[float] = None,
                          raw_material_cost: float = 0.0) -> Dict[str, float]:
    """
    §41: OCN = 80% of new fixed-asset investment
             + 50% of (advertising + POP + sales managers + rep fixed salaries
                       + general overhead + market research)
             + 15% of raw material cost.
    """
    s = SCENARIO
    overhead = s["general_overhead"] if overhead is None else overhead
    capex_part = s["ocn_capex_pct"] * new_capex
    opex_base = (advertising_spend + pop_spend + sales_manager_spend
                 + rep_fixed_salaries + overhead + market_research_spend)
    opex_part = s["ocn_opex_pct"] * opex_base
    rm_part = s["ocn_rm_pct"] * raw_material_cost
    return {"capex_component": capex_part, "opex_component": opex_part,
            "raw_material_component": rm_part,
            "total": capex_part + opex_part + rm_part}


def available_cash_jan2(cash_dec31: float, loan_amortisation_due: float = 0.0,
                        credit_lines_due: float = 0.0, accounts_payable: float = 0.0,
                        financial_investments: float = 0.0,
                        fixed_term_deposits: float = 0.0,
                        accounts_receivable: float = 0.0) -> float:
    """§41: the cash figure the OCN test is actually run against."""
    return (cash_dec31 - loan_amortisation_due - credit_lines_due - accounts_payable
            + financial_investments + fixed_term_deposits + accounts_receivable)


def financing_gap(ocn_total: float, available_cash: float) -> Dict[str, float]:
    """
    §41/§42: if OCN exceeds available cash the simulator takes a loan for you at
    the loan rate. If it is lower you are sitting on a cash surplus that earns
    nothing unless you deposit or invest it (§44).
    """
    s = SCENARIO
    gap = ocn_total - available_cash
    if gap > 0:
        return {"loan_needed": gap, "surplus": 0.0,
                "first_year_interest": gap * s["loan_interest"],
                "upfront_fee": gap * s["loan_upfront_fee"]}
    surplus = -gap
    return {"loan_needed": 0.0, "surplus": surplus,
            "deposit_income": surplus * s["deposit_interest"],
            "first_year_interest": 0.0, "upfront_fee": 0.0}


def factoring_cost(receivables: float) -> float:
    """§39: the bank discounts invoices at the factoring rate."""
    return receivables * SCENARIO["factoring_rate"]


def receivables(annual_revenue: float, terms_months: int) -> float:
    """
    §38: monthly invoicing of 1/12 of annual sales at retail price, collected
    after `terms_months`. Year-end receivables = terms/12 of annual revenue.
    """
    if terms_months not in SCENARIO["customer_terms_months"]:
        raise ValueError(f"terms must be one of {SCENARIO['customer_terms_months']} (§38)")
    return annual_revenue * terms_months / 12.0


def compare_working_capital(annual_revenue: float, terms_months: int) -> Dict[str, float]:
    """Factor the receivable at 5.5%, or fund it with a 10% loan (§39, §49)."""
    s = SCENARIO
    r = receivables(annual_revenue, terms_months)
    return {"receivable": r,
            "factoring_cost": r * s["factoring_rate"],
            "loan_cost_same_amount": r * s["loan_interest"],
            "saving_from_factoring": r * (s["loan_interest"] - s["factoring_rate"])}


# ---------------------------------------------------------------------------
# MARKET RESEARCH  (§50)
# ---------------------------------------------------------------------------

FREE_SURVEYS = (20, 21, 22)


def research_cost(survey_ids: Iterable[int]) -> float:
    return sum(SCENARIO["research"][i][1] for i in survey_ids)


def research_menu(max_cost: Optional[float] = None) -> List[Tuple[int, str, float]]:
    rows = [(i, name, cost) for i, (name, cost) in sorted(SCENARIO["research"].items())]
    if max_cost is not None:
        rows = [r for r in rows if r[2] <= max_cost]
    return rows


# ---------------------------------------------------------------------------
# PROMOTIONS  (§18)
# ---------------------------------------------------------------------------
#
# NOTE ON A DISCREPANCY IN THE SOURCE: §18 opens with "There are eight different
# types of promotions" and then enumerates six (price reduction, 3x2, drawing,
# discount on next purchase, direct bonus, indirect bonus). The six described are
# modelled here. Confirm the remaining two with the simulation Director in
# Session 2 rather than guessing at them.

PROMOTION_TYPES = {
    1: "Price reduction",
    2: "3x2",
    3: "Drawing",
    4: "Discount on next purchase",
    5: "Direct promotional bonus (instant gift)",
    6: "Indirect promotional bonus (points-based gift)",
}


def promotion_cost_per_unit(kind: int, retail_price: float,
                            discount: float = 0.0,
                            units_to_qualify: int = 1,
                            drawing_budget: float = 0.0,
                            promo_units: float = 0.0,
                            redemption_rate: float = 1.0) -> float:
    """
    Cost to the company of ONE unit sold on promotion (§18).

    kind 1  price reduction        -> `discount` euros off the retail price
    kind 2  3x2                    -> one free unit in every three: retail/3
    kind 3  drawing                -> `drawing_budget` spread over `promo_units`
    kind 4  discount next purchase -> `discount` x `redemption_rate`
    kind 5  direct bonus           -> 1.20 EUR per `units_to_qualify` units
    kind 6  indirect bonus         -> 3.60 EUR per `units_to_qualify` units

    `redemption_rate` applies to kind 4 only: not every coupon comes back.
    Rejected promotions cost nothing except drawings (§18).
    """
    s = SCENARIO
    if kind == 1:
        return discount
    if kind == 2:
        return retail_price / 3.0
    if kind == 3:
        return drawing_budget / promo_units if promo_units else float("inf")
    if kind == 4:
        return discount * redemption_rate
    if kind == 5:
        return s["promo_direct_gift_cost"] / max(1, units_to_qualify)
    if kind == 6:
        return s["promo_indirect_gift_cost"] / max(1, units_to_qualify)
    raise ValueError(f"unknown promotion type {kind}; see §18")


def promotion_menu(retail_price: float, discount: float = 0.50,
                   units_to_qualify: int = 3) -> List[Tuple[int, str, float, float]]:
    """(type, name, cost/unit, cost as % of retail price) ranked cheapest first."""
    rows = []
    for k, name in PROMOTION_TYPES.items():
        if k == 3:
            continue  # a drawing has no per-unit cost without a volume assumption
        c = promotion_cost_per_unit(k, retail_price, discount=discount,
                                    units_to_qualify=units_to_qualify)
        rows.append((k, name, c, c / retail_price if retail_price else float("nan")))
    return sorted(rows, key=lambda r: r[2])


def promotion_capacity_check(promo_units: float, available_units: float) -> Dict[str, float]:
    """
    §48: if you cannot supply the demand your promotions create, the market
    REJECTS the promotions it cannot serve. Promoting beyond your capacity does
    not merely stock you out — it wastes the promotion entirely.
    """
    served = min(promo_units, available_units)
    return {"promo_units_planned": promo_units, "units_available": available_units,
            "units_served": served, "units_rejected": max(0.0, promo_units - served),
            "fully_supplied": promo_units <= available_units}


# ---------------------------------------------------------------------------
# PRICING: break-even  (§14, §20, §7, §36)
# ---------------------------------------------------------------------------

def breakeven_price(standard_cost_unit: float, retailer_margin: float,
                    units: float, allocated_fixed_costs: float = 0.0,
                    wholesaler_share: float = 0.0,
                    promo_cost_per_unit: float = 0.0) -> float:
    """
    Lowest retail price (MSRP) at which a unit still covers its own costs.

    Three of the deductions scale WITH the retail price, not against it:
      * the wholesaler takes 8.46% of retail on the units it moves (§7),
      * R&D takes 4.5% of revenue automatically (§36).
    The retailer margin (§20) and the standard cost (§33) are flat euros per unit.
    Solving  P x (1 - w x share - rd) - retailer_margin - SC - promo = fixed/units:

        P = (fixed/units + retailer_margin + SC + promo) / (1 - w x share - rd)

    The denominator is why a high wholesaler share raises your break-even price:
    every euro of price you add hands 8.46 cents straight back.
    """
    s = SCENARIO
    denom = 1.0 - s["wholesaler_pct_normal"] * wholesaler_share - s["rd_pct_of_revenue"]
    if denom <= 0:
        raise ValueError("price-linked deductions exceed 100% of revenue")
    per_unit_fixed = allocated_fixed_costs / units if units else 0.0
    return (per_unit_fixed + retailer_margin + standard_cost_unit
            + promo_cost_per_unit) / denom


def minimum_legal_price(standard_cost_unit: float, retailer_margin: float) -> float:
    """
    The DUMPING FLOOR. Synoptic Overview: "Dumping is not allowed; you cannot
    sell below production cost plus the retailer margin."

    This is a hard legality limit, NOT a profitability limit. It ignores fixed
    costs, the wholesaler commission and the automatic 4.5% R&D charge — so a
    price that is legal can still lose money on every unit. Always check it
    against breakeven_price() as well; the higher of the two is your real floor.
    """
    return standard_cost_unit + retailer_margin


def price_floor(standard_cost_unit: float, retailer_margin: float, units: float,
                allocated_fixed_costs: float = 0.0, wholesaler_share: float = 0.0,
                promo_cost_per_unit: float = 0.0) -> Dict[str, float]:
    """The binding price floor: the higher of the dumping limit and break-even."""
    legal = minimum_legal_price(standard_cost_unit, retailer_margin)
    economic = breakeven_price(standard_cost_unit, retailer_margin, units,
                               allocated_fixed_costs, wholesaler_share,
                               promo_cost_per_unit)
    return {"legal_minimum": legal, "breakeven": economic,
            "binding_floor": max(legal, economic),
            "binding_constraint": "dumping ban" if legal > economic else "break-even"}


def pop_budget_check(budget: float) -> Dict[str, object]:
    """Point-of-sale advertising is capped at EUR 500,000 per channel per year."""
    cap = SCENARIO["pop_max_per_channel"]
    return {"budget": budget, "cap": cap, "legal": budget <= cap,
            "excess": max(0.0, budget - cap)}


def contribution_per_unit(retail_price: float, standard_cost_unit: float,
                          retailer_margin: float, wholesaler_share: float = 0.0,
                          promo_cost_per_unit: float = 0.0) -> float:
    """Euros left per unit to cover fixed costs and profit, after every variable deduction."""
    s = SCENARIO
    return (retail_price * (1.0 - s["wholesaler_pct_normal"] * wholesaler_share
                            - s["rd_pct_of_revenue"])
            - retailer_margin - standard_cost_unit - promo_cost_per_unit)


# ---------------------------------------------------------------------------
# CAPACITY REALITY CHECK  (§34, §48)
# ---------------------------------------------------------------------------

def capacity_reality_check(forecast: Dict[str, float], cap: "Capacity",
                           opening_inventory: Optional[Dict[str, float]] = None
                           ) -> Dict[str, Dict[str, float]]:
    """
    Compare a sales forecast against what the plant can physically deliver.

    §34: a finished-goods stockout "not only results in lower sales, but damages
    brand prestige and loyalty as well" — the damage outlives the year. §48: units
    SOLD need not equal units DEMANDED, and the gap is exactly this.

    Run this before every plan. It is the cheapest error to avoid in the game.
    """
    opening_inventory = opening_inventory or {}
    out: Dict[str, Dict[str, float]] = {}
    for product in PRODUCTS:
        want = forecast.get(product, 0.0)
        made = cap.s_units if product == "S" else cap.h_units
        have = made + opening_inventory.get(product, 0.0)
        total_mkt = market_size_table()[product]["TOTAL"]
        out[product] = {
            "forecast_units": want,
            "producible_units": made,
            "available_units": have,
            "shortfall": max(0.0, want - have),
            "surplus_to_inventory": max(0.0, have - want),
            "utilisation_of_capacity": want / made if made else 0.0,
            "implied_market_share": want / total_mkt if total_mkt else 0.0,
            "capacity_as_share_of_market": have / total_mkt if total_mkt else 0.0,
            "STOCKOUT": want > have,
        }
    return out


# ---------------------------------------------------------------------------
# DEBT: loan amortisation  (§42, §49)
# ---------------------------------------------------------------------------

@dataclass
class LoanYear:
    year: int
    opening_balance: float
    drawn: float
    repayment: float
    interest: float
    upfront_fee: float
    closing_balance: float


class LoanBook:
    """
    Tracks outstanding bank debt across the simulated years.

    §42: "Loan amortization will always be carried out so that each year, except
    the year in which the loan is requested, the company returns a proportion of
    the total amount owed at the beginning of the year." Maturity and rate are set
    by the Director (§49 defaults: 4 years, 10%, 1% upfront fee).

    AMBIGUITY, stated plainly: "a proportion" is not defined. Two readings —
      * `straight_line` (default): opening balance / remaining years, so the debt
        is genuinely cleared by maturity.
      * `declining`: a flat 1/maturity of the opening balance every year, which
        never fully clears.
    The default is the one that actually retires the debt. Check your first-year
    balance sheet against both and set `rule` to whichever the simulator used.
    """

    def __init__(self, rule: str = "straight_line",
                 maturity_years: Optional[int] = None,
                 interest: Optional[float] = None,
                 upfront_fee: Optional[float] = None):
        s = SCENARIO
        self.rule = rule
        self.maturity = maturity_years or s["loan_maturity_years"]
        self.interest = interest if interest is not None else s["loan_interest"]
        self.fee = upfront_fee if upfront_fee is not None else s["loan_upfront_fee"]
        self.balance = 0.0
        self.age = 0                # years since the outstanding debt was drawn
        self.history: List[LoanYear] = []

    def year(self, year: int, draw: float = 0.0, prepay: float = 0.0) -> LoanYear:
        """Advance one simulated year. Repayment is skipped in a year money is drawn (§42)."""
        opening = self.balance
        repayment = 0.0
        if opening > 0 and draw == 0:
            if self.rule == "declining":
                repayment = opening / self.maturity
            else:
                remaining = max(1, self.maturity - self.age)
                repayment = opening / remaining
            repayment = min(repayment, opening)

        prepay = min(prepay, max(0.0, opening - repayment))
        penalty = prepay * SCENARIO["loan_prepayment_penalty"]
        interest = opening * self.interest
        fee = draw * self.fee

        self.balance = opening - repayment - prepay + draw
        self.age = 0 if draw else self.age + 1
        row = LoanYear(year, opening, draw, repayment + prepay,
                       interest + penalty, fee, self.balance)
        self.history.append(row)
        return row

    def schedule(self) -> str:
        w = "{:>5}{:>16}{:>14}{:>14}{:>14}{:>14}{:>16}"
        out = [w.format("year", "opening", "drawn", "repaid", "interest",
                        "fee", "closing")]
        for r in self.history:
            out.append(w.format(r.year, f"{r.opening_balance:,.0f}", f"{r.drawn:,.0f}",
                                f"{r.repayment:,.0f}", f"{r.interest:,.0f}",
                                f"{r.upfront_fee:,.0f}", f"{r.closing_balance:,.0f}"))
        return "\n".join(out)


# ---------------------------------------------------------------------------
# BALANCE SHEET AND RATIOS  (§47, and the rubric's explicit demand for ratios)
# ---------------------------------------------------------------------------

@dataclass
class BalanceSheet:
    """
    Year-end position (31 December, §40). Note §47: a loan drawn this year is
    NOT repaid this year — the money leaves your cash on 2 January.
    """
    fixed_assets_gross: float = 0.0
    accumulated_depreciation: float = 0.0
    inventory_finished: float = 0.0
    inventory_raw: float = 0.0
    receivables: float = 0.0
    financial_investments: float = 0.0
    fixed_term_deposits: float = 0.0
    cash: float = 0.0
    shares_held: float = 0.0

    loans: float = 0.0
    credit_lines_drawn: float = 0.0
    accounts_payable: float = 0.0
    equity: float = 0.0
    retained_earnings: float = 0.0

    @property
    def fixed_assets_net(self) -> float:
        return self.fixed_assets_gross - self.accumulated_depreciation

    @property
    def inventory(self) -> float:
        return self.inventory_finished + self.inventory_raw

    @property
    def current_assets(self) -> float:
        return (self.inventory + self.receivables + self.financial_investments
                + self.fixed_term_deposits + self.cash + self.shares_held)

    @property
    def total_assets(self) -> float:
        return self.fixed_assets_net + self.current_assets

    @property
    def current_liabilities(self) -> float:
        return self.credit_lines_drawn + self.accounts_payable

    @property
    def total_liabilities(self) -> float:
        return self.loans + self.current_liabilities

    @property
    def total_equity(self) -> float:
        return self.equity + self.retained_earnings

    @property
    def balances(self) -> bool:
        return abs(self.total_assets - (self.total_liabilities + self.total_equity)) < 1.0

    def render(self) -> str:
        w = 32
        rows = [
            ("ASSETS", None),
            ("  Fixed assets (gross)", self.fixed_assets_gross),
            ("  Accumulated depreciation", -self.accumulated_depreciation),
            ("  Fixed assets (net)", self.fixed_assets_net),
            ("  Inventory - finished goods", self.inventory_finished),
            ("  Inventory - raw materials", self.inventory_raw),
            ("  Receivables (clients)", self.receivables),
            ("  Financial investments", self.financial_investments),
            ("  Fixed term deposits", self.fixed_term_deposits),
            ("  Shares held", self.shares_held),
            ("  Cash & equivalents", self.cash),
            ("TOTAL ASSETS", self.total_assets),
            ("", None),
            ("LIABILITIES & EQUITY", None),
            ("  Bank loans", self.loans),
            ("  Credit lines drawn", self.credit_lines_drawn),
            ("  Accounts payable", self.accounts_payable),
            ("  Equity", self.equity),
            ("  Retained earnings", self.retained_earnings),
            ("TOTAL LIABILITIES & EQUITY", self.total_liabilities + self.total_equity),
        ]
        out = []
        for label, value in rows:
            out.append(label if value is None else f"{label:<{w}}{value:>16,.0f}")
        out.append("")
        out.append(f"{'Balances?':<{w}}{'YES' if self.balances else 'NO — CHECK':>16}")
        return "\n".join(out)


def ratios(bs: BalanceSheet, inc: IncomeStatement,
           opening_equity: Optional[float] = None,
           opening_assets: Optional[float] = None) -> Dict[str, float]:
    """
    The ratio set the evaluation guidelines ask for in every CEO meeting and in
    the final report ("financial statement analysis ... including financial ratios").

    Returns are computed on OPENING equity and assets where those are supplied,
    which is the defensible convention: you earned the year's profit on the
    capital you started it with.
    """
    eq = opening_equity if opening_equity is not None else bs.total_equity
    assets = opening_assets if opening_assets is not None else bs.total_assets
    cl = bs.current_liabilities

    def safe(n: float, d: float) -> float:
        return n / d if d else float("nan")

    return {
        # Profitability
        "gross_margin_pct": safe(inc.gross_margin, inc.revenue),
        "operating_margin_pct": inc.operating_margin,
        "net_margin_pct": inc.net_margin,
        "ROE": safe(inc.net_income, eq),
        "ROA": safe(inc.net_income, assets),
        "ROCE": safe(inc.operating_income, eq + bs.loans),
        # Efficiency
        "asset_turnover": safe(inc.revenue, assets),
        "days_sales_outstanding": safe(bs.receivables * 365.0, inc.revenue),
        "days_inventory": safe(bs.inventory_finished * 365.0, inc.cogs),
        "days_payable": safe(bs.accounts_payable * 365.0, inc.cogs),
        # Liquidity
        "current_ratio": safe(bs.current_assets, cl),
        "quick_ratio": safe(bs.current_assets - bs.inventory, cl),
        "working_capital": bs.current_assets - cl,
        # Leverage and cover
        "debt_to_equity": safe(bs.total_liabilities, bs.total_equity),
        "equity_ratio": safe(bs.total_equity, bs.total_assets),
        "interest_cover": safe(inc.operating_income, inc.financial_expenses),
    }


def render_ratios(r: Dict[str, float]) -> str:
    groups = [
        ("Profitability", ["gross_margin_pct", "operating_margin_pct", "net_margin_pct",
                           "ROE", "ROA", "ROCE"]),
        ("Efficiency", ["asset_turnover", "days_sales_outstanding", "days_inventory",
                        "days_payable"]),
        ("Liquidity", ["current_ratio", "quick_ratio", "working_capital"]),
        ("Leverage", ["debt_to_equity", "equity_ratio", "interest_cover"]),
    ]
    pct = {"gross_margin_pct", "operating_margin_pct", "net_margin_pct",
           "ROE", "ROA", "ROCE", "equity_ratio"}
    out = []
    for title, keys in groups:
        out.append(title)
        for k in keys:
            v = r[k]
            if k in pct:
                out.append(f"  {k:<26}{v:>14.2%}")
            elif k == "working_capital":
                out.append(f"  {k:<26}{v:>14,.0f}")
            else:
                out.append(f"  {k:<26}{v:>14.2f}")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# MULTI-YEAR RUNNER  (chains the 4 graded years)
# ---------------------------------------------------------------------------

@dataclass
class YearPlan:
    """One year of decisions. Only what the model needs; the full decision list is docs/04."""
    year: int
    s_lines_new: int = 0
    h_lines_new: int = 0
    shifts: int = 1
    preventive: bool = False
    poka_yoke_install: bool = False
    smed_modules_new: int = 0
    smed_active: bool = False
    smed_teams_per_shift: int = 0
    training_dept: bool = False

    sales: List[SalesLine] = field(default_factory=list)
    advertising_spend: float = 0.0
    pop_spend: float = 0.0
    sales_force_cost: float = 0.0
    logistics_cost: float = 0.0
    market_research_spend: float = 0.0
    office_salaries: Optional[Dict[str, float]] = None
    specialist_salary: Optional[float] = None
    operator_salary: Optional[float] = None

    customer_terms_months: int = 2
    use_factoring: bool = False
    rm_payment_terms_months: int = 0
    loan_draw: float = 0.0
    loan_prepay: float = 0.0
    deposit: float = 0.0


@dataclass
class YearResult:
    year: int
    capacity: "Capacity"
    standard_cost: Dict[str, float]
    income: IncomeStatement
    balance: BalanceSheet
    ratios: Dict[str, float]
    stockout: Dict[str, Dict[str, float]]
    ocn: Dict[str, float]


class Simulation:
    """
    Chains YearPlans, carrying forward everything that persists: installed lines
    (irreversible, §22), finished-goods inventory and its weighted-average
    standard cost (§33, §34), equity and retained earnings (§37), and debt (§42).

    This is the difference between a calculator and a plan. Run all four graded
    years, look at accumulated profit — which is what the ranking is decided on
    (§47) and what "company results" is graded on.
    """

    def __init__(self, poka_yoke: bool = False):
        s = SCENARIO
        self.s_lines = 0
        self.h_lines = 0
        self.smed_modules = 0
        self.poka_yoke = poka_yoke
        self.fixed_assets_gross = s["opening_fixed_assets"]
        self.accumulated_depreciation = 0.0
        self.cash = s["opening_cash"]
        self.equity = s["opening_equity"]
        self.retained = 0.0
        self.inventory_units: Dict[str, float] = {p: 0.0 for p in PRODUCTS}
        self.inventory_sc: Dict[str, float] = {p: 0.0 for p in PRODUCTS}
        self.loans = LoanBook()
        self.results: List[YearResult] = []

    def run_year(self, plan: YearPlan) -> YearResult:
        s = SCENARIO

        # --- irreversible investment decisions (§22, §26, §27) --------------
        if plan.smed_modules_new and plan.year < s["smed_first_available_year"]:
            raise ValueError(
                f"SMED cannot be acquired before year {s['smed_first_available_year']} (§27)")
        self.s_lines += plan.s_lines_new
        self.h_lines += plan.h_lines_new
        if self.s_lines + self.h_lines > s["max_total_lines"]:
            raise ValueError(f"factory limit is {s['max_total_lines']} lines (§22)")
        self.smed_modules += plan.smed_modules_new
        if plan.poka_yoke_install:
            if self.poka_yoke:
                raise ValueError("Poka Yoke can only be installed once (§26)")
            self.poka_yoke = True

        capex = (plan.s_lines_new * s["line_capex"]["S"]
                 + plan.h_lines_new * s["line_capex"]["H"]
                 + plan.smed_modules_new * s["smed_capex_per_module"])
        if plan.poka_yoke_install:
            # §26: every line already installed is affected, plus all future ones.
            capex += (self.s_lines + self.h_lines) * s["poka_yoke_capex_per_line"]
        self.fixed_assets_gross += capex

        smed_on = plan.smed_active and self.smed_modules > 0

        # --- production ----------------------------------------------------
        cap = capacity(self.s_lines, self.h_lines, plan.shifts,
                       preventive=plan.preventive, poka_yoke=self.poka_yoke,
                       smed=smed_on)

        sc_now: Dict[str, float] = {}
        sc_used: Dict[str, float] = {}
        for p in PRODUCTS:
            lines = self.s_lines if p == "S" else self.h_lines
            if lines == 0:
                sc_now[p] = 0.0
                sc_used[p] = self.inventory_sc[p]
                continue
            sc = standard_cost(p, lines=lines, shifts=plan.shifts,
                               specialist_salary=plan.specialist_salary,
                               operator_salary=plan.operator_salary,
                               preventive=plan.preventive, poka_yoke=self.poka_yoke,
                               smed=smed_on,
                               smed_teams_per_shift=plan.smed_teams_per_shift)
            sc_now[p] = sc.total
            produced = cap.s_units if p == "S" else cap.h_units
            sc_used[p] = weighted_average_sc(self.inventory_units[p],
                                             self.inventory_sc[p], produced, sc.total)

        stockout = capacity_reality_check(
            {p: sum(l.units for l in plan.sales if l.product == p) for p in PRODUCTS},
            cap, self.inventory_units)

        # --- income statement ----------------------------------------------
        rm_cost = sum(
            raw_material_units_needed(
                cap.s_units if p == "S" else cap.h_units,
                cap.s_scrapped if p == "S" else cap.h_scrapped)
            * s["rm_unit_cost"][p] for p in PRODUCTS)

        revenue = sum(l.revenue for l in plan.sales)
        recv = receivables(revenue, plan.customer_terms_months)
        fin_exp = self.loans.history[-1].interest if self.loans.history else 0.0
        fin_inc = 0.0
        if plan.use_factoring:
            fin_exp += factoring_cost(recv)
            recv = 0.0                      # §39: the Clients account goes to zero
        if plan.deposit:
            fin_inc += plan.deposit * s["deposit_interest"]

        inc = build_income_statement(
            plan.sales, sc_used,
            advertising_spend=plan.advertising_spend, pop_spend=plan.pop_spend,
            sales_force_cost=plan.sales_force_cost, logistics_cost=plan.logistics_cost,
            office_salaries=plan.office_salaries,
            market_research_spend=plan.market_research_spend,
            preventive=plan.preventive, training_dept=plan.training_dept,
            fixed_assets=self.fixed_assets_gross, shifts=plan.shifts,
            financial_expenses=0.0, financial_income=fin_inc)

        loan_row = self.loans.year(plan.year, draw=plan.loan_draw, prepay=plan.loan_prepay)
        inc.financial_expenses = fin_exp + loan_row.upfront_fee

        # --- roll the balance sheet forward ---------------------------------
        self.accumulated_depreciation += inc.depreciation
        for p in PRODUCTS:
            produced = cap.s_units if p == "S" else cap.h_units
            sold = sum(l.units for l in plan.sales if l.product == p)
            closing = max(0.0, self.inventory_units[p] + produced - sold)
            self.inventory_sc[p] = sc_used[p]
            self.inventory_units[p] = closing

        payable = rm_cost * plan.rm_payment_terms_months / 12.0
        self.retained += inc.net_income

        bs = BalanceSheet(
            fixed_assets_gross=self.fixed_assets_gross,
            accumulated_depreciation=self.accumulated_depreciation,
            inventory_finished=sum(self.inventory_units[p] * self.inventory_sc[p]
                                   for p in PRODUCTS),
            receivables=recv,
            fixed_term_deposits=plan.deposit,
            cash=self.cash,
            loans=self.loans.balance,
            accounts_payable=payable,
            equity=self.equity,
            retained_earnings=self.retained)
        # Cash is the balancing figure: everything else is determined above.
        bs.cash = (bs.total_liabilities + bs.total_equity
                   - bs.fixed_assets_net - bs.inventory - bs.receivables
                   - bs.financial_investments - bs.fixed_term_deposits - bs.shares_held)

        # §42: "The Cash and Equivalents account can be negative, in which case it
        # is obligatory to request a bank loan for that negative amount." The
        # simulator will do this for you if you do not — at 10%. Model it, so the
        # forecast you show the CEO is the one the simulator will produce.
        self.forced_loan = 0.0
        if bs.cash < 0:
            self.forced_loan = -bs.cash
            self.loans.balance += self.forced_loan
            loan_row.drawn += self.forced_loan
            loan_row.closing_balance = self.loans.balance
            inc.financial_expenses += self.forced_loan * s["loan_upfront_fee"]
            bs.loans = self.loans.balance
            bs.cash = 0.0
        self.cash = bs.cash

        ocn = operating_cash_needed(
            new_capex=capex, advertising_spend=plan.advertising_spend,
            pop_spend=plan.pop_spend, sales_manager_spend=plan.sales_force_cost,
            market_research_spend=plan.market_research_spend, raw_material_cost=rm_cost)

        opening_eq = self.equity + self.retained - inc.net_income
        res = YearResult(plan.year, cap, sc_now, inc, bs,
                         ratios(bs, inc, opening_equity=opening_eq),
                         stockout, ocn)
        self.results.append(res)
        return res

    @property
    def accumulated_profit(self) -> float:
        """§47: the ranking against competitors is decided on accumulated profit."""
        return sum(r.income.net_income for r in self.results)

    def summary(self) -> str:
        w = "{:>6}{:>16}{:>16}{:>14}{:>9}{:>9}{:>10}{:>14}"
        out = [w.format("year", "revenue", "net income", "cum. profit",
                        "op.mgn", "ROE", "stockout", "debt")]
        cum = 0.0
        for r in self.results:
            cum += r.income.net_income
            so = ",".join(p for p in PRODUCTS if r.stockout[p]["STOCKOUT"]) or "-"
            out.append(w.format(r.year, f"{r.income.revenue:,.0f}",
                                f"{r.income.net_income:,.0f}", f"{cum:,.0f}",
                                f"{r.income.operating_margin:.1%}",
                                f"{r.ratios['ROE']:.1%}", so,
                                f"{r.balance.loans:,.0f}"))
        return "\n".join(out)


# ---------------------------------------------------------------------------
# DEMAND CALIBRATION SCAFFOLD
# ---------------------------------------------------------------------------
#
# The simulator's demand function is HIDDEN. Nothing in the scenario states how
# price, advertising, positioning and shelf space combine into units demanded, so
# no coefficient is asserted here. What this does instead is FIT the relationship
# from your own results once you have them.
#
# Use it from the test round onwards: every year you play is one observation per
# product-market. By the time the graded round starts you should have enough to
# forecast instead of guess — which is the whole point of the ungraded round and
# the part most teams waste.
#
# Model: log(demand) = b0 + b1*log(price) + b2*log(GRPs+1) + b3*log(shelf%)
#                         + b4*log(PoP+1) + b5*reach_share ...
# i.e. constant-elasticity. b1 is your price elasticity, b2 your advertising
# elasticity. Both are directly quotable in a CEO meeting.


@dataclass
class Observation:
    """One product x market outcome from one played year."""
    year: int
    product: str
    market: str
    price: float
    demand_units: float
    grps: float = 0.0
    reach_pct: float = 0.0
    shelf_pct: float = 0.0
    pop_spend: float = 0.0
    retailer_margin: float = 0.0
    promo_units: float = 0.0
    notes: str = ""


def _solve(a: List[List[float]], b: List[float]) -> List[float]:
    """Gaussian elimination with partial pivoting. Keeps the module dependency-free."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[piv][col]) < 1e-12:
            raise ValueError("singular system — add more varied observations")
        m[col], m[piv] = m[piv], m[col]
        pv = m[col][col]
        for r in range(n):
            if r == col:
                continue
            f = m[r][col] / pv
            for c in range(col, n + 1):
                m[r][c] -= f * m[col][c]
    return [m[i][n] / m[i][i] for i in range(n)]


@dataclass
class Elasticities:
    intercept: float
    price: float
    advertising: float
    shelf: float
    r_squared: float
    n_observations: int
    drivers: List[str]

    def summary(self) -> str:
        return (f"n={self.n_observations}  R^2={self.r_squared:.3f}\n"
                f"  price elasticity        {self.price:>8.3f}"
                f"   (a 10% price cut moves demand {abs(self.price)*10:.1f}%)\n"
                f"  advertising elasticity  {self.advertising:>8.3f}\n"
                f"  shelf-space elasticity  {self.shelf:>8.3f}")


def fit_elasticities(observations: List[Observation],
                     use_shelf: bool = True) -> Elasticities:
    """
    Fit constant-elasticity demand from played results. Needs at least one more
    observation than parameters, and genuine VARIATION in the drivers — if you
    charged the same price everywhere, no method can recover a price elasticity.

    This is why docs/05 tells you to deliberately vary price and advertising
    across markets during the ungraded round: you are buying information.
    """
    drivers = ["const", "log_price", "log_grps"]
    if use_shelf:
        drivers.append("log_shelf")
    k = len(drivers)
    usable = [o for o in observations if o.demand_units > 0 and o.price > 0]
    if len(usable) < k + 1:
        raise ValueError(
            f"need at least {k+1} observations with positive price and demand, "
            f"got {len(usable)}. Play more years, or drop a driver.")

    rows, y = [], []
    for o in usable:
        r = [1.0, math.log(o.price), math.log(o.grps + 1.0)]
        if use_shelf:
            r.append(math.log(max(o.shelf_pct, 0.01)))
        rows.append(r)
        y.append(math.log(o.demand_units))

    xtx = [[sum(rows[i][a] * rows[i][b] for i in range(len(rows))) for b in range(k)]
           for a in range(k)]
    xty = [sum(rows[i][a] * y[i] for i in range(len(rows))) for a in range(k)]
    beta = _solve(xtx, xty)

    ybar = sum(y) / len(y)
    ss_tot = sum((v - ybar) ** 2 for v in y)
    ss_res = sum((y[i] - sum(beta[j] * rows[i][j] for j in range(k))) ** 2
                 for i in range(len(rows)))
    r2 = 1.0 - ss_res / ss_tot if ss_tot else float("nan")

    return Elasticities(beta[0], beta[1], beta[2],
                        beta[3] if use_shelf else float("nan"),
                        r2, len(usable), drivers)


def predict_demand(e: Elasticities, price: float, grps: float,
                   shelf_pct: float = 1.0) -> float:
    """Forecast units from fitted elasticities. Only as good as the fit — check R^2 first."""
    v = e.intercept + e.price * math.log(price) + e.advertising * math.log(grps + 1.0)
    if not math.isnan(e.shelf):
        v += e.shelf * math.log(max(shelf_pct, 0.01))
    return math.exp(v)


# ---------------------------------------------------------------------------
# REPORTING HELPERS
# ---------------------------------------------------------------------------

def briefing() -> str:
    s = SCENARIO
    out: List[str] = []
    add = out.append

    add("=" * 74)
    add("MMT39 BRIEFING — every figure below is computed from the scenario PDF")
    add("=" * 74)

    add("\nOPENING POSITION (§1)")
    add(f"  Fixed assets            EUR {s['opening_fixed_assets']:>14,.0f}")
    add(f"  Cash & equivalents      EUR {s['opening_cash']:>14,.0f}"
        f"   ({s['opening_cash']/s['opening_equity']:.0%} of the balance sheet, idle)")
    add(f"  Equity                  EUR {s['opening_equity']:>14,.0f}   (cannot be increased, §37)")
    add(f"  Forgone deposit income  EUR {s['opening_cash']*s['deposit_interest']:>14,.0f}"
        f"   /yr if cash is left in Cash (§44)")

    add("\nMARKET SIZE AT t0 (§2, §3) — annual units")
    tbl = market_size_table()
    add(f"  {'':<4}{'A':>14}{'B':>14}{'E':>14}{'TOTAL':>16}")
    for p in PRODUCTS:
        r = tbl[p]
        add(f"  {p:<4}{r['A']:>14,.0f}{r['B']:>14,.0f}{r['E']:>14,.0f}{r['TOTAL']:>16,.0f}")
    for p in PRODUCTS:
        add(f"  E is {tbl[p]['E']/tbl[p]['TOTAL']:.0%} of {p} demand"
            f" — and the only market with local competition (§2)")

    add("\nLINE ECONOMICS (§22, §23) — 3 shifts, no productivity systems")
    add(f"  {'':<3}{'capex':>12}{'nameplate':>14}{'sellable':>14}"
        f"{'capex/unit':>13}{'SC floor':>11}")
    for p in PRODUCTS:
        cap = capacity(**{f"{p.lower()}_lines": 1}, shifts=3)
        units = cap.s_units if p == "S" else cap.h_units
        nameplate = cap.s_nameplate if p == "S" else cap.h_nameplate
        sc = standard_cost(p, lines=1, shifts=3)
        add(f"  {p:<3}{s['line_capex'][p]:>12,.0f}{nameplate:>14,.0f}{units:>14,.0f}"
            f"{s['line_capex'][p]/units:>13,.2f}{sc.total:>11,.2f}")
    ratio = capex_per_annual_unit("S") / capex_per_annual_unit("H")
    add(f"  -> an S line costs {ratio:.1f}x more capex per unit of annual capacity than an H line")

    add("\nTHE CAPACITY THAT ISN'T THERE (§23, §24)")
    h = line_hours(shifts=1)
    add(f"  Scheduled per line-shift-year  {h.scheduled:>8,.0f} h")
    add(f"  Lost to breakdown repair       {h.repair_hours:>8,.0f} h  ({h.repair_hours/h.scheduled:.1%})")
    add(f"  Lost to main-module servicing  {h.module_hours:>8,.0f} h  ({h.module_hours/h.scheduled:.1%})"
        f"  <- SMED removes this (§27)")
    add(f"  Actually producing             {h.operating:>8,.0f} h  ({h.utilisation:.2%} of nameplate)")
    hs = line_hours(shifts=1, smed=True)
    add(f"  With SMED                      {hs.operating:>8,.0f} h  ({hs.utilisation:.2%})"
        f"  = +{hs.operating/h.operating-1:.1%} output, and SMED cannot be bought before year"
        f" {s['smed_first_available_year']}")

    add("\nMEDIA EFFICIENCY (§15, §16) — currency per 1% of buyers reached, per insertion")
    for mk in ("A", "E"):
        label = "A / B (EUR)" if mk == "A" else "E (USD)"
        rows = media_efficiency(mk)
        add(f"  {label}")
        for m, rate, scope, cpp in rows:
            add(f"    {m}  {s['media_names'][m]:<44} rate {rate:>7,.0f}"
                f"  scope {scope:>4.0f}%  ->{cpp:>8,.1f}")
        add(f"    cheapest {rows[0][0]} at {rows[0][3]:,.0f};"
            f" dearest {rows[-1][0]} at {rows[-1][3]:,.0f}"
            f"  (+{rows[-1][3]/rows[0][3]-1:.0%})")

    add("\nVEHICLE SIZING (§10) — factory to platform")
    add("  Per FULL vehicle, bigger is always cheaper:")
    for kg in (s["f2p_kg_max"], 12_000, 6_000, s["f2p_kg_min"]):
        add(f"    {kg:>7,} kg -> EUR {marginal_cost_per_unit(kg):.5f}/unit")
    add(f"  -> {marginal_cost_per_unit(s['f2p_kg_min'])/marginal_cost_per_unit(s['f2p_kg_max']):.0f}x"
        f" spread on an identical cost formula; the §10 benchmark of"
        f" {s['f2p_benchmark_per_unit']} is beaten by every size above ~9,000 kg")
    add("  But for a REAL volume the optimum is fewest vehicles sized to fit exactly,")
    add("  because cost collapses to 24,000 x vehicles + 0.0024 x units:")
    for vol in (10_000_000, 20_000_000, 40_000_000):
        opt = optimal_vehicle_plan(vol)
        naive = plan_factory_to_platform(vol, load_kg=s["f2p_kg_max"])
        add(f"    {vol/1e6:>4.0f}M units -> {opt.vehicles} veh @ {opt.load_kg:,.0f} kg"
            f" = EUR {opt.cost_per_unit:.5f}/unit"
            f"   (naive max-capacity buy: EUR {naive.cost_per_unit:.5f},"
            f" +{naive.total_cost/opt.total_cost-1:.0%})")

    add("\nFINANCING (§39, §49)")
    add(f"  Factoring {s['factoring_rate']:.1%} vs loan {s['loan_interest']:.1%}"
        f" vs credit line {s['credit_line_interest']:.1%}"
        f" vs OVERDRAFT {s['overdraft_interest']:.0%}")
    wc = compare_working_capital(100_000_000, 4)
    add(f"  On EUR 100M revenue at 120-day terms: receivable EUR {wc['receivable']:,.0f};"
        f" factoring saves EUR {wc['saving_from_factoring']:,.0f}/yr vs funding it with a loan")

    add("\nFIXED COSTS YOU CANNOT AVOID")
    lo, hi = office_payroll_range()
    add(f"  Office payroll (§29)      EUR {lo:>11,.0f} .. {hi:>11,.0f}  (spread {hi-lo:,.0f})")
    add(f"  General overhead (§29)    EUR {s['general_overhead']:>11,.0f}")
    add(f"  R&D (§36)                 4.5% of REVENUE, automatic, not optional")
    add(f"  Preventive maint. (§25)   EUR {s['preventive_maintenance_cost']:>11,.0f}  optional, annual")
    add(f"  Training dept TS (§32)    EUR {s['training_department_cost']:>11,.0f}  optional, annual")

    add("\nMARKET RESEARCH (§50)")
    free = [i for i in FREE_SURVEYS]
    add(f"  FREE and most teams will not harvest them systematically: {free}")
    for i in free:
        add(f"    {i:>2}. {s['research'][i][0]}")
    add(f"  Cheapest paid intelligence: 23 net income EUR 1,000;"
        f" 28 shifts EUR 1,000; 1/2 market sales EUR 3,000 each;"
        f" 27 platforms EUR 3,000")
    add(f"  Whole menu if you bought everything: EUR {research_cost(s['research'].keys()):,.0f}")
    add("")
    return "\n".join(out)


def _selftest() -> None:
    s = SCENARIO
    ok = 0

    def check(label: str, cond: bool) -> None:
        nonlocal ok
        assert cond, f"FAILED: {label}"
        ok += 1
        print(f"  ok  {label}")

    print("Self-test against figures stated directly in Scenario MMT39:")

    # §1
    check("opening balance sheet balances at EUR 66,000,000",
          abs(s["opening_fixed_assets"] + s["opening_cash"] + s["opening_inventory"]
              - s["opening_equity"]) < 1e-6)

    # §3 x §2
    t = market_size_table()
    check("S market totals 56,200,000 units", abs(t["S"]["TOTAL"] - 56_200_000) < 1)
    check("H market totals 131,260,000 units", abs(t["H"]["TOTAL"] - 131_260_000) < 1)
    check("E is the largest single market for both products",
          t["S"]["E"] > t["S"]["A"] + t["S"]["B"] and t["H"]["E"] > t["H"]["A"])

    # §23
    check("S line nameplate is 240,000 units/shift/year",
          capacity(s_lines=1, shifts=1).s_nameplate == 240_000)
    check("H line nameplate is 600,000 units/shift/year",
          capacity(h_lines=1, shifts=1).h_nameplate == 600_000)
    check("3 shifts triple nameplate output",
          capacity(h_lines=1, shifts=3).h_nameplate == 3 * capacity(h_lines=1, shifts=1).h_nameplate)
    check("factory cannot exceed 32 lines (§22)",
          _raises(lambda: capacity(s_lines=20, h_lines=20, shifts=1)))

    # §24
    h1 = line_hours(shifts=1)
    check("breakdowns are 70 per 2,000 line-hours", h1.breakdowns == 70)
    check("breakdown repair consumes 175 h per line-shift-year",
          abs(h1.repair_hours - 175.0) < 1e-9)
    check("main-module servicing consumes 250 h per line-shift-year",
          abs(h1.module_hours - 250.0) < 1e-9)
    check("hours reconcile: operating + repair + module = scheduled",
          abs(h1.operating + h1.repair_hours + h1.module_hours - h1.scheduled) < 1e-9)
    check("effective utilisation is 78.75% of nameplate",
          abs(h1.utilisation - 0.7875) < 1e-9)
    check("strict module-counter reading lands within 3% of the default",
          abs(line_hours(1, strict_module_counter=True).operating / h1.operating - 1) < 0.03)

    # §27
    check("SMED removes main-module downtime entirely",
          line_hours(shifts=1, smed=True).module_hours == 0.0)
    check("SMED lifts operating hours above the no-SMED case",
          line_hours(shifts=1, smed=True).operating > h1.operating)

    # §26 / §25
    check("Poka Yoke eliminates breakdown scrap", scrap_hours_each(poka_yoke=True) == 0.0)
    check("preventive maintenance cuts but does not eliminate scrap",
          0 < scrap_hours_each(preventive=True) < scrap_hours_each())
    check("repair time stays inside the 1.5-2.5 h range §30 quotes",
          all(1.5 <= repair_hours_each(p, q) <= 2.5
              for p in (False, True) for q in (False, True)))

    # §33 / §49 / §30
    sc_s = standard_cost("S", lines=1, shifts=1)
    sc_h = standard_cost("H", lines=1, shifts=1)
    check("S standard cost exceeds H standard cost", sc_s.total > sc_h.total)
    check("S raw material component reflects the 1.65 EUR unit cost plus scrap",
          sc_s.raw_material >= s["rm_unit_cost"]["S"])
    check("H is cheaper than S per unit of capex too",
          capex_per_annual_unit("H") < capex_per_annual_unit("S"))

    # §10 — the scenario's own guideline must be reachable
    f2p = plan_factory_to_platform(20_000_000, load_kg=s["f2p_kg_max"])
    check("factory->platform beats the 0.006 EUR/unit guideline at max load",
          f2p.cost_per_unit < s["f2p_benchmark_per_unit"])
    check("a full max-load vehicle carries at EUR 0.0044/unit",
          abs(marginal_cost_per_unit(s["f2p_kg_max"]) - 0.0044) < 1e-6)
    check("a full min-load vehicle carries at EUR 0.0504/unit",
          abs(marginal_cost_per_unit(s["f2p_kg_min"]) - 0.0504) < 1e-6)
    check("the smallest vehicle is >10x worse per unit than the largest",
          marginal_cost_per_unit(s["f2p_kg_min"])
          > 10 * marginal_cost_per_unit(s["f2p_kg_max"]))
    check("marginal cost falls monotonically as load capacity rises",
          all(marginal_cost_per_unit(k) > marginal_cost_per_unit(k + 1000)
              for k in range(1_000, 24_000, 1_000)))
    check("per FULL vehicle, the largest legal size is always the cheapest",
          vehicle_size_scan(24_000_000, leg="f2p")[0][0] == s["f2p_kg_max"])
    plan = optimal_vehicle_plan(20_000_000, leg="f2p")
    check("for a real volume the optimum is fewest vehicles sized to fit, "
          "not always max capacity",
          plan.load_kg == 20_000 and plan.vehicles == 2)
    check("the optimal plan beats naive max-capacity buying",
          plan.total_cost < plan_factory_to_platform(20_000_000,
                                                     load_kg=s["f2p_kg_max"]).total_cost)
    check("fleet cost collapses to 24,000 x vehicles + 0.0024 x units",
          abs(plan.total_cost - (24_000 * plan.vehicles + 0.0024 * 20_000_000)) < 1.0)
    check("vehicle cost formula reproduces 24,000 + 1.2 x kg",
          abs(vehicle_annual_cost(24_000) - 52_800) < 1e-9)

    # §16
    for mk in ("A", "E"):
        check(f"television is the cheapest reach in market {mk}",
              media_efficiency(mk)[0][0] == "TV")
    ad = advertising("A", {"TV": 3})
    check("insertions buy frequency, not extra reach, within one medium",
          abs(ad.net_reach_pct - media_scope("TV", "A")) < 1e-9 and ad.average_frequency == 3)
    check("adding a second medium raises net reach",
          advertising("A", {"TV": 1, "PR": 1}).net_reach_pct > ad.net_reach_pct)

    # §29
    lo, hi = office_payroll_range()
    check("office payroll floor is EUR 2,413,092", abs(lo - 2_413_092) < 1)
    check("office payroll ceiling is EUR 3,371,620", abs(hi - 3_371_620) < 1)
    check("office salary outside the legal band is rejected",
          _raises(lambda: office_payroll({"I": 200_000})))

    # §30
    hc = production_headcount(s_lines=1, h_lines=0, shifts=1)
    check("an S line needs 9 specialists and 32 operators per shift",
          hc["specialists"] == 9 and hc["operators"] == 32)

    # §41 — reproduce the rule verbatim
    o = operating_cash_needed(new_capex=1_000_000, advertising_spend=1_000_000,
                              pop_spend=0, sales_manager_spend=0, rep_fixed_salaries=0,
                              market_research_spend=0, overhead=0, raw_material_cost=1_000_000)
    check("OCN = 80% capex + 50% opex + 15% raw materials",
          abs(o["total"] - (800_000 + 500_000 + 150_000)) < 1e-6)
    check("OCN above available cash triggers a loan for the difference",
          abs(financing_gap(5_000_000, 3_000_000)["loan_needed"] - 2_000_000) < 1e-6)
    check("OCN below available cash leaves an investable surplus",
          financing_gap(3_000_000, 5_000_000)["surplus"] == 2_000_000)

    # §38 / §39
    check("120-day terms tie up one third of annual revenue in receivables",
          abs(receivables(120_000_000, 4) - 40_000_000) < 1e-6)
    check("factoring at 5.5% is cheaper than a 10% loan on the same receivable",
          compare_working_capital(100_000_000, 4)["saving_from_factoring"] > 0)
    check("customer terms outside 60/90/120 days are rejected",
          _raises(lambda: receivables(1_000_000, 1)))

    # §35 / §36
    inc = build_income_statement(
        [SalesLine("H", "A", "G", units_normal=1_000_000, retail_price=5.0,
                   retailer_margin=1.0)],
        {"H": 2.0}, fixed_assets=12_000_000, shifts=1)
    check("R&D is booked at 4.5% of revenue", abs(inc.rd - 0.045 * inc.revenue) < 1e-6)
    check("depreciation at 1 shift is 8% of fixed assets",
          abs(inc.depreciation - 0.08 * 12_000_000) < 1e-6)
    check("depreciation rises with shift count",
          s["depreciation_by_shifts"][3] > s["depreciation_by_shifts"][1])
    check("net sales deduct retailer and wholesaler margins from retail invoicing",
          abs(inc.net_sales - (5_000_000 - 1_000_000)) < 1e-6)

    # §50
    check("surveys 20, 21 and 22 are free", research_cost(FREE_SURVEYS) == 0.0)
    check("survey 19 (true demand) is the most expensive single survey",
          max(s["research"].items(), key=lambda kv: kv[1][1])[0] == 19)

    # -- §18 promotions ----------------------------------------------------
    check("a 3x2 promotion costs one third of the retail price per unit",
          abs(promotion_cost_per_unit(2, 6.0) - 2.0) < 1e-9)
    check("a direct gift over 3 units costs 0.40 EUR/unit",
          abs(promotion_cost_per_unit(5, 6.0, units_to_qualify=3) - 0.40) < 1e-9)
    check("an indirect gift is 3x the cost of a direct gift for the same threshold",
          abs(promotion_cost_per_unit(6, 6.0, units_to_qualify=3)
              / promotion_cost_per_unit(5, 6.0, units_to_qualify=3) - 3.0) < 1e-9)
    check("3x2 is the most expensive promotion type at a 6 EUR price point",
          promotion_menu(6.0)[-1][0] == 2)
    check("an unknown promotion type is rejected",
          _raises(lambda: promotion_cost_per_unit(9, 6.0)))
    pc = promotion_capacity_check(1_000_000, 600_000)
    check("promotions beyond available stock are rejected by the market (§48)",
          pc["units_rejected"] == 400_000 and not pc["fully_supplied"])

    # -- break-even pricing ------------------------------------------------
    bp = breakeven_price(standard_cost_unit=2.0, retailer_margin=1.0,
                         units=1_000_000, allocated_fixed_costs=1_000_000)
    check("break-even price covers SC, retailer margin, fixed costs and the 4.5% R&D",
          abs(contribution_per_unit(bp, 2.0, 1.0) * 1_000_000 - 1_000_000) < 1.0)
    check("a wholesaler share raises the break-even price",
          breakeven_price(2.0, 1.0, 1_000_000, 1_000_000, wholesaler_share=1.0) > bp)
    check("contribution turns negative below the break-even price",
          contribution_per_unit(bp - 0.5, 2.0, 1.0) * 1_000_000 < 1_000_000)

    # -- capacity reality check --------------------------------------------
    cap3 = capacity(h_lines=10, shifts=3)
    rc = capacity_reality_check({"H": 50_000_000}, cap3)
    check("a forecast above producible units is flagged as a stockout",
          rc["H"]["STOCKOUT"] and rc["H"]["shortfall"] > 0)
    rc2 = capacity_reality_check({"H": 1_000_000}, cap3)
    check("a forecast within capacity is not flagged, and the rest goes to inventory",
          not rc2["H"]["STOCKOUT"] and rc2["H"]["surplus_to_inventory"] > 0)
    check("no single company can supply the whole H market",
          capacity(h_lines=32, shifts=3).h_units < market_size_table()["H"]["TOTAL"])

    # -- §42 loan amortisation ---------------------------------------------
    lb = LoanBook()
    lb.year(1, draw=10_000_000)
    check("no repayment is made in the year a loan is drawn (§42)",
          lb.history[-1].repayment == 0.0 and lb.balance == 10_000_000)
    check("the upfront fee is 1% of the amount drawn",
          abs(lb.history[-1].upfront_fee - 100_000) < 1e-6)
    for y in (2, 3, 4, 5):
        lb.year(y)
    check("straight-line amortisation clears the debt by maturity",
          abs(lb.balance) < 1.0)
    lb2 = LoanBook(rule="declining")
    lb2.year(1, draw=10_000_000)
    for y in (2, 3, 4, 5):
        lb2.year(y)
    check("the declining reading leaves debt outstanding at maturity",
          lb2.balance > 0)
    check("interest is charged on the opening balance at 10%",
          abs(lb.history[1].interest - 1_000_000) < 1.0)

    # -- balance sheet and ratios ------------------------------------------
    bs = BalanceSheet(fixed_assets_gross=12_000_000, cash=54_000_000,
                      equity=66_000_000)
    check("the opening balance sheet balances", bs.balances)
    inc2 = build_income_statement(
        [SalesLine("H", "A", "G", units_normal=10_000_000, retail_price=5.0,
                   retailer_margin=1.0)],
        {"H": 2.0}, fixed_assets=12_000_000, shifts=1)
    r = ratios(bs, inc2, opening_equity=66_000_000)
    check("ROE is net income over opening equity",
          abs(r["ROE"] - inc2.net_income / 66_000_000) < 1e-12)
    check("the ratio set covers profitability, efficiency, liquidity and leverage",
          {"ROE", "ROA", "current_ratio", "debt_to_equity", "asset_turnover",
           "days_sales_outstanding"} <= set(r))
    check("120-day terms produce a DSO near 120 days",
          abs(ratios(BalanceSheet(receivables=receivables(120_000_000, 4),
                                  equity=66_000_000, cash=66_000_000),
                     build_income_statement(
                         [SalesLine("H", "A", "G", units_normal=24_000_000,
                                    retail_price=5.0)], {"H": 2.0}))
              ["days_sales_outstanding"] - 121.7) < 1.0)

    # -- multi-year runner --------------------------------------------------
    sim = Simulation()
    sim.run_year(YearPlan(
        year=1, h_lines_new=6, shifts=2,
        sales=[SalesLine("H", "A", "G", units_normal=5_000_000, retail_price=4.0,
                         retailer_margin=0.9)],
        advertising_spend=2_000_000, sales_force_cost=1_000_000,
        logistics_cost=200_000))
    check("year 1 balance sheet balances after a full run", sim.results[0].balance.balances)
    check("installed lines persist into the next year",
          sim.s_lines == 0 and sim.h_lines == 6)
    check("unsold production carries forward as finished-goods inventory",
          sim.inventory_units["H"] > 0)
    sim.run_year(YearPlan(
        year=2, h_lines_new=2, shifts=2, smed_modules_new=1, smed_active=True,
        sales=[SalesLine("H", "A", "G", units_normal=8_000_000, retail_price=4.0,
                         retailer_margin=0.9)],
        advertising_spend=2_000_000, sales_force_cost=1_000_000,
        logistics_cost=300_000))
    check("year 2 balance sheet balances", sim.results[1].balance.balances)
    check("SMED raises output per line versus year 1",
          sim.results[1].capacity.utilisation > sim.results[0].capacity.utilisation)
    check("accumulated profit is the sum of the years played",
          abs(sim.accumulated_profit
              - sum(r.income.net_income for r in sim.results)) < 1e-6)
    check("SMED cannot be bought in year 1 (§27)",
          _raises(lambda: Simulation().run_year(YearPlan(year=1, smed_modules_new=1))))
    check("Poka Yoke cannot be installed twice (§26)",
          _raises(lambda: (lambda s2: (s2.run_year(YearPlan(year=1, h_lines_new=1,
                                                            poka_yoke_install=True)),
                                       s2.run_year(YearPlan(year=2, h_lines_new=1,
                                                            poka_yoke_install=True))))
                  (Simulation())))

    # -- §42 mandatory loan on negative cash --------------------------------
    sim3 = Simulation()
    sim3.run_year(YearPlan(
        year=1, h_lines_new=30, shifts=3,      # deliberately over-invest
        sales=[SalesLine("H", "A", "G", units_normal=1_000_000, retail_price=4.0,
                         retailer_margin=0.9)],
        advertising_spend=5_000_000, sales_force_cost=2_000_000))
    check("negative cash triggers the mandatory bank loan (§42)",
          sim3.results[0].balance.loans > 0 and sim3.results[0].balance.cash >= 0)
    check("the balance sheet still balances after the forced loan",
          sim3.results[0].balance.balances)

    # -- demand calibration scaffold ---------------------------------------
    truth = dict(intercept=15.0, price=-1.8, adv=0.35)
    obs = []
    for i, (pr, g) in enumerate([(3.0, 400), (3.5, 600), (4.0, 500), (4.5, 900),
                                 (5.0, 300), (5.5, 800), (6.0, 700)]):
        d = math.exp(truth["intercept"] + truth["price"] * math.log(pr)
                     + truth["adv"] * math.log(g + 1.0))
        obs.append(Observation(year=1, product="H", market="A", price=pr,
                               demand_units=d, grps=g))
    fit = fit_elasticities(obs, use_shelf=False)
    check("the demand fitter recovers a known price elasticity",
          abs(fit.price - truth["price"]) < 0.01)
    check("the demand fitter recovers a known advertising elasticity",
          abs(fit.advertising - truth["adv"]) < 0.01)
    check("a perfect fit reports R^2 of 1", abs(fit.r_squared - 1.0) < 1e-6)
    check("predictions round-trip back to the observed demand",
          abs(predict_demand(fit, 4.0, 500) / obs[2].demand_units - 1.0) < 1e-6)
    check("too few observations are refused rather than silently fitted",
          _raises(lambda: fit_elasticities(obs[:2], use_shelf=False)))
    check("no variation in the drivers is refused rather than silently fitted",
          _raises(lambda: fit_elasticities(
              [Observation(1, "H", "A", 4.0, 1_000_000, grps=500) for _ in range(8)],
              use_shelf=False)))

    # -- Synoptic Overview rules -------------------------------------------
    check("dumping floor = production cost + retailer margin",
          abs(minimum_legal_price(2.13, 0.95) - 3.08) < 1e-9)
    pf = price_floor(2.13, 0.95, units=1.0, allocated_fixed_costs=0.776)
    check("break-even normally binds above the dumping floor",
          pf["binding_constraint"] == "break-even" and pf["binding_floor"] > pf["legal_minimum"])
    pf2 = price_floor(2.13, 0.95, units=1.0, allocated_fixed_costs=0.0)
    check("with no fixed costs to cover the dumping ban can be the binding limit",
          pf2["binding_floor"] >= pf2["legal_minimum"])
    check("PoS advertising is capped at EUR 500,000 per channel",
          pop_budget_check(500_000)["legal"] and not pop_budget_check(500_001)["legal"])
    check("PoS overspend is reported",
          pop_budget_check(600_000)["excess"] == 100_000)
    check("the synoptic confirms one SMED unit serves several lines",
          SCENARIO["smed_serves_multiple_lines"] is True)
    check("positioning axes are Natural (X) and Technological (Y)",
          SCENARIO["positioning_axis_x"] == "Natural"
          and SCENARIO["positioning_axis_y"] == "Technological")
    check("consumer segments weight 40/40/20",
          abs(SCENARIO["segment_x_share"] + SCENARIO["segment_y_share"]
              + SCENARIO["segment_neither_share"] - 1.0) < 1e-9)

    check("benchmark sizing lands near the EUR 0.007 platform->retailer guideline",
          abs(size_from_benchmark(6_837_600, leg="p2r")["recommended"]["cost_per_unit"]
              - 0.007) < 0.002)
    check("benchmark sizing lands near the EUR 0.006 factory->platform guideline",
          abs(size_from_benchmark(6_837_600, leg="f2p")["recommended"]["cost_per_unit"]
              - 0.006) < 0.002)
    check("the geometric estimator is the one that disagrees with the benchmark",
          plan_platform_to_retailer(6_837_600, "A", 6, 3815).cost_per_unit > 0.05)

    print(f"\n{ok} checks passed.")


def _raises(fn) -> bool:
    try:
        fn()
    except Exception:
        return True
    return False


def main() -> None:
    p = argparse.ArgumentParser(description="MMT39 decision model")
    p.add_argument("--selftest", action="store_true",
                   help="verify constants and formulas against the scenario")
    p.add_argument("--briefing", action="store_true", help="headline numbers")
    p.add_argument("--media", action="store_true", help="media efficiency ranking")
    p.add_argument("--vehicles", type=float, metavar="UNITS",
                   help="vehicle sizing table for a units volume")
    p.add_argument("--lines", action="store_true", help="line economics by shift count")
    p.add_argument("--promotions", type=float, metavar="PRICE",
                   help="promotion cost ranking at a given retail price")
    p.add_argument("--breakeven", nargs=3, type=float,
                   metavar=("SC", "RETAILER_MARGIN", "FIXED_PER_UNIT"),
                   help="minimum viable retail price")
    p.add_argument("--demo", action="store_true",
                   help="worked 4-year run: P&L, balance sheet, ratios, stockout check")
    args = p.parse_args()

    if args.selftest:
        _selftest()
        return
    if args.media:
        for mk in ("A", "E"):
            print(f"\nMarket {mk} — cost per 1% of buyers reached, per insertion")
            for m, rate, scope, cpp in media_efficiency(mk):
                print(f"  {m}  rate {rate:>7,.0f}  scope {scope:>4.0f}%  -> {cpp:>8,.1f}")
        return
    if args.vehicles:
        print(f"\nFactory -> platform, {args.vehicles:,.0f} units (§10)")
        for kg, n, cost, per in vehicle_size_scan(args.vehicles, leg="f2p")[:5]:
            print(f"  {kg:>7,} kg  {n:>4} veh  EUR {cost:>12,.0f}  EUR {per:.5f}/unit")
        print("  ...")
        for kg, n, cost, per in vehicle_size_scan(args.vehicles, leg="f2p")[-3:]:
            print(f"  {kg:>7,} kg  {n:>4} veh  EUR {cost:>12,.0f}  EUR {per:.5f}/unit")
        return
    if args.lines:
        print(f"\n{'prod':<5}{'shifts':>7}{'nameplate':>14}{'sellable':>14}"
              f"{'util':>8}{'capex/unit':>12}{'SC':>9}")
        for prod in PRODUCTS:
            for sh in (1, 2, 3):
                cap = capacity(**{f"{prod.lower()}_lines": 1}, shifts=sh)
                units = cap.s_units if prod == "S" else cap.h_units
                nameplate = cap.s_nameplate if prod == "S" else cap.h_nameplate
                sc = standard_cost(prod, lines=1, shifts=sh)
                print(f"{prod:<5}{sh:>7}{nameplate:>14,.0f}{units:>14,.0f}"
                      f"{cap.utilisation:>8.2%}"
                      f"{SCENARIO['line_capex'][prod]/units:>12,.2f}{sc.total:>9,.2f}")
        return

    if args.promotions:
        price = args.promotions
        print(f"\nPromotion cost per unit at a EUR {price:.2f} retail price (§18)")
        print(f"  {'#':<3}{'type':<44}{'EUR/unit':>10}{'% of price':>12}")
        for k, name, c, pct in promotion_menu(price):
            print(f"  {k:<3}{name:<44}{c:>10.2f}{pct:>11.1%}")
        print("  (3 Drawing is excluded: its cost per unit depends on the volume it draws)")
        print("  Max 3 promotions per channel per product per year; effect lasts 3 of 52 weeks (§18)")
        return
    if args.breakeven:
        sc, margin, fixed = args.breakeven
        print(f"\nBreak-even retail price (§7, §14, §20, §36)")
        print(f"  standard cost {sc:.2f} + retailer margin {margin:.2f}"
              f" + fixed {fixed:.2f}/unit")
        for share, label in ((0.0, "all own sales managers"),
                             (0.5, "half wholesalers"),
                             (1.0, "all wholesalers")):
            bp = breakeven_price(sc, margin, units=1.0, allocated_fixed_costs=fixed,
                                 wholesaler_share=share)
            print(f"  {label:<26} EUR {bp:>7.2f}")
        return
    if args.demo:
        sim = Simulation()
        plans = [
            YearPlan(year=1, h_lines_new=8, s_lines_new=2, shifts=2,
                     sales=[SalesLine("H", "A", "G", units_normal=6_000_000,
                                      retail_price=4.20, retailer_margin=0.95),
                            SalesLine("S", "A", "G", units_normal=1_500_000,
                                      retail_price=8.50, retailer_margin=1.90)],
                     advertising_spend=2_500_000, pop_spend=400_000,
                     sales_force_cost=1_200_000, logistics_cost=250_000,
                     market_research_spend=50_000, customer_terms_months=2),
            YearPlan(year=2, h_lines_new=4, shifts=3, preventive=True,
                     smed_modules_new=2, smed_active=True, smed_teams_per_shift=1,
                     sales=[SalesLine("H", "A", "G", units_normal=11_000_000,
                                      retail_price=4.20, retailer_margin=0.95),
                            SalesLine("S", "A", "G", units_normal=2_000_000,
                                      retail_price=8.50, retailer_margin=1.90)],
                     advertising_spend=3_200_000, pop_spend=500_000,
                     sales_force_cost=1_600_000, logistics_cost=350_000,
                     market_research_spend=120_000, customer_terms_months=2),
        ]
        for pl in plans:
            sim.run_year(pl)
        print("\nWORKED EXAMPLE — illustrative decisions, not a recommendation\n")
        print(sim.summary())
        last = sim.results[-1]
        print("\n" + "=" * 52 + "\nYEAR 2 INCOME STATEMENT\n" + "=" * 52)
        print(last.income.render())
        print("\n" + "=" * 52 + "\nYEAR 2 BALANCE SHEET\n" + "=" * 52)
        print(last.balance.render())
        print("\n" + "=" * 52 + "\nYEAR 2 RATIOS\n" + "=" * 52)
        print(render_ratios(last.ratios))
        print("\n" + "=" * 52 + "\nCAPACITY CHECK\n" + "=" * 52)
        for prod, d in last.stockout.items():
            if d["forecast_units"] == 0:
                continue
            flag = "STOCKOUT" if d["STOCKOUT"] else "ok"
            print(f"  {prod}: forecast {d['forecast_units']:>12,.0f}"
                  f" | available {d['available_units']:>12,.0f}"
                  f" | {d['implied_market_share']:>6.2%} of market  [{flag}]")
        print("\n" + "=" * 52 + "\nLOAN SCHEDULE\n" + "=" * 52)
        print(sim.loans.schedule() if sim.loans.history else "  no debt drawn")
        return

    print(briefing())


if __name__ == "__main__":
    main()
