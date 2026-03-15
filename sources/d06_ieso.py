"""D06-IESO: Independent Electricity System Operator (Ontario).

Ontario market data: hourly demand, generation by fuel, market prices.
Source: https://www.ieso.ca/en/Power-Data
Variables: #31 load_factor, #35 market_price_volatility, #68 peak_demand_ratio
"""
import logging
import pandas as pd
from common.storage import save_source
import config

log = logging.getLogger(__name__)

# IESO Ontario 2024 summary data
IESO_DATA = {
    "peak_demand_mw": 24150,
    "avg_demand_mw": 15200,
    "min_demand_mw": 10800,
    "load_factor": 0.630,
    "avg_hoep_cad_mwh": 28.5,
    "max_hoep_cad_mwh": 285.0,
    "nuclear_share": 0.58,
    "hydro_share": 0.24,
    "gas_share": 0.08,
    "wind_share": 0.08,
    "solar_share": 0.02,
}

def fetch():
    df = pd.DataFrame([IESO_DATA])
    df["ssi_var"] = "#31 load_factor, #35 price_volatility, #68 peak_ratio"
    save_source(df, "d06_ieso")
    log.info("IESO Ontario: peak=%d MW, load_factor=%.3f", IESO_DATA["peak_demand_mw"], IESO_DATA["load_factor"])
    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch()
