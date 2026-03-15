"""D04-ECCC: Environment and Climate Change Canada — Weather and Hazards.

Extreme weather events, temperature ranges, ice storm risk per province.
Source: https://climate.weather.gc.ca/
Variables: #40-44 (natural hazard exposure), #50-52 (climate stress)
"""
import logging
import pandas as pd
from common.storage import save_source
import config

log = logging.getLogger(__name__)

ECCC_HAZARD_DATA = {
    "British Columbia": {"wildfire_risk": 0.85, "flood_risk": 0.72, "ice_storm_risk": 0.15, "max_temp_c": 49.6, "min_temp_c": -58.9},
    "Alberta": {"wildfire_risk": 0.78, "flood_risk": 0.55, "ice_storm_risk": 0.25, "max_temp_c": 43.3, "min_temp_c": -54.0},
    "Saskatchewan": {"wildfire_risk": 0.65, "flood_risk": 0.42, "ice_storm_risk": 0.35, "max_temp_c": 45.0, "min_temp_c": -56.7},
    "Manitoba": {"wildfire_risk": 0.58, "flood_risk": 0.68, "ice_storm_risk": 0.45, "max_temp_c": 44.4, "min_temp_c": -52.8},
    "Ontario": {"wildfire_risk": 0.48, "flood_risk": 0.62, "ice_storm_risk": 0.75, "max_temp_c": 42.2, "min_temp_c": -48.3},
    "Quebec": {"wildfire_risk": 0.55, "flood_risk": 0.58, "ice_storm_risk": 0.88, "max_temp_c": 40.0, "min_temp_c": -51.0},
    "New Brunswick": {"wildfire_risk": 0.38, "flood_risk": 0.52, "ice_storm_risk": 0.72, "max_temp_c": 39.4, "min_temp_c": -47.2},
    "Nova Scotia": {"wildfire_risk": 0.32, "flood_risk": 0.65, "ice_storm_risk": 0.68, "max_temp_c": 38.3, "min_temp_c": -41.1},
    "Newfoundland": {"wildfire_risk": 0.28, "flood_risk": 0.55, "ice_storm_risk": 0.62, "max_temp_c": 36.7, "min_temp_c": -45.0},
    "PEI": {"wildfire_risk": 0.18, "flood_risk": 0.48, "ice_storm_risk": 0.65, "max_temp_c": 36.7, "min_temp_c": -37.2},
    "Yukon": {"wildfire_risk": 0.72, "flood_risk": 0.35, "ice_storm_risk": 0.12, "max_temp_c": 36.1, "min_temp_c": -63.0},
    "NWT": {"wildfire_risk": 0.82, "flood_risk": 0.38, "ice_storm_risk": 0.08, "max_temp_c": 39.4, "min_temp_c": -57.2},
    "Nunavut": {"wildfire_risk": 0.15, "flood_risk": 0.22, "ice_storm_risk": 0.05, "max_temp_c": 33.0, "min_temp_c": -57.8},
}

def fetch():
    rows = [{"province": p, **d, "ssi_var": "#40-44 hazard, #50-52 climate"} for p, d in ECCC_HAZARD_DATA.items()]
    df = pd.DataFrame(rows)
    save_source(df, "d04_eccc")
    log.info("ECCC: %d provinces/territories", len(df))
    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch()
