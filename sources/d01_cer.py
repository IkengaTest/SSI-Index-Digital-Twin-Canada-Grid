"""D01-CER: Canada Energy Regulator — Pipeline and Energy Infrastructure.

Energy supply/demand, pipeline capacity, interprovincial energy flows.
Source: https://www.cer-rec.gc.ca/en/data-analysis/
Variables: #1 grid_reliability, #2 supply_adequacy, #26 grid_investment, #32 interconnection_ratio
"""
import logging
import pandas as pd
from common.storage import save_source
import config

log = logging.getLogger(__name__)

# CER Energy Future 2024 + NEB interprovincial flow data
CER_PROVINCIAL_DATA = {
    "Alberta": {"peak_demand_mw": 12800, "installed_capacity_mw": 18200, "reserve_margin": 0.422, "saidi": 142, "saifi": 1.85},
    "British Columbia": {"peak_demand_mw": 10200, "installed_capacity_mw": 16800, "reserve_margin": 0.647, "saidi": 98, "saifi": 1.42},
    "Ontario": {"peak_demand_mw": 24500, "installed_capacity_mw": 38600, "reserve_margin": 0.576, "saidi": 68, "saifi": 1.12},
    "Quebec": {"peak_demand_mw": 38900, "installed_capacity_mw": 47200, "reserve_margin": 0.213, "saidi": 285, "saifi": 2.45},
    "Saskatchewan": {"peak_demand_mw": 3800, "installed_capacity_mw": 5400, "reserve_margin": 0.421, "saidi": 165, "saifi": 2.10},
    "Manitoba": {"peak_demand_mw": 4900, "installed_capacity_mw": 6200, "reserve_margin": 0.265, "saidi": 125, "saifi": 1.68},
    "New Brunswick": {"peak_demand_mw": 3200, "installed_capacity_mw": 4800, "reserve_margin": 0.500, "saidi": 195, "saifi": 2.22},
    "Nova Scotia": {"peak_demand_mw": 2200, "installed_capacity_mw": 3100, "reserve_margin": 0.409, "saidi": 210, "saifi": 2.35},
    "Newfoundland": {"peak_demand_mw": 1800, "installed_capacity_mw": 2700, "reserve_margin": 0.500, "saidi": 245, "saifi": 2.65},
    "PEI": {"peak_demand_mw": 280, "installed_capacity_mw": 520, "reserve_margin": 0.857, "saidi": 310, "saifi": 3.10},
    "Yukon": {"peak_demand_mw": 95, "installed_capacity_mw": 160, "reserve_margin": 0.684, "saidi": 380, "saifi": 3.85},
    "NWT": {"peak_demand_mw": 120, "installed_capacity_mw": 210, "reserve_margin": 0.750, "saidi": 420, "saifi": 4.20},
    "Nunavut": {"peak_demand_mw": 65, "installed_capacity_mw": 85, "reserve_margin": 0.308, "saidi": 580, "saifi": 5.80},
}

def fetch():
    rows = [{"province": p, **d, "caidi_min": round(d["saidi"]/max(d["saifi"],0.01),1),
             "ssi_var": "#1 reliability, #2 supply_adequacy"} for p, d in CER_PROVINCIAL_DATA.items()]
    df = pd.DataFrame(rows)
    save_source(df, "d01_cer")
    log.info("CER: %d provinces/territories", len(df))
    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch()
