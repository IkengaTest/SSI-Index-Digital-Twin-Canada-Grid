"""D03-NRCan: Natural Resources Canada — Energy Production and Grid Assets.

Electricity generation mix, renewable capacity, grid infrastructure age.
Source: https://www.nrcan.gc.ca/energy
Variables: #16 DER_ratio, #17 renewable_penetration, #30 capacity_factor
"""
import logging
import pandas as pd
from common.storage import save_source
import config

log = logging.getLogger(__name__)

NRCAN_GENERATION_MIX = {
    "hydro": {"capacity_gw": 82.5, "generation_twh": 380.2, "share_pct": 59.3},
    "nuclear": {"capacity_gw": 13.6, "generation_twh": 92.4, "share_pct": 14.4},
    "natural_gas": {"capacity_gw": 22.8, "generation_twh": 68.5, "share_pct": 10.7},
    "wind": {"capacity_gw": 17.2, "generation_twh": 42.8, "share_pct": 6.7},
    "coal": {"capacity_gw": 4.8, "generation_twh": 24.1, "share_pct": 3.8},
    "solar": {"capacity_gw": 5.8, "generation_twh": 7.2, "share_pct": 1.1},
    "biomass": {"capacity_gw": 3.2, "generation_twh": 11.5, "share_pct": 1.8},
    "oil": {"capacity_gw": 5.1, "generation_twh": 6.8, "share_pct": 1.1},
    "other": {"capacity_gw": 2.4, "generation_twh": 7.8, "share_pct": 1.2},
}

def fetch():
    rows = []
    total_re = sum(v["share_pct"] for k, v in NRCAN_GENERATION_MIX.items()
                    if k in ("hydro", "wind", "solar", "biomass"))
    for fuel, d in NRCAN_GENERATION_MIX.items():
        rows.append({"fuel_type": fuel, **d, "ssi_var": "#16 DER_ratio, #17 renewable"})
    df = pd.DataFrame(rows)
    df.attrs["renewable_share_pct"] = total_re
    save_source(df, "d03_nrcan")
    log.info("NRCan: %d fuel types, RE share=%.1f%%", len(df), total_re)
    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch()
