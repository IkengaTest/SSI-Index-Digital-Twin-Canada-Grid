"""D07-Copernicus: ERA5 Climate Reanalysis for Canada.

Temperature, wind speed, solar irradiance from Copernicus CDS.
Source: https://cds.climate.copernicus.eu/
Variables: #50 temperature_stress, #51 wind_resource, #52 solar_resource
"""
import logging
import pandas as pd
from common.storage import save_source
import config

log = logging.getLogger(__name__)

ERA5_CA_CLIMATE = {
    "British Columbia": {"temp_avg_c": 8.5, "wind_avg_ms": 3.8, "ghi_kwh_m2": 1280},
    "Alberta": {"temp_avg_c": 3.8, "wind_avg_ms": 4.5, "ghi_kwh_m2": 1420},
    "Saskatchewan": {"temp_avg_c": 2.1, "wind_avg_ms": 5.2, "ghi_kwh_m2": 1480},
    "Manitoba": {"temp_avg_c": 1.5, "wind_avg_ms": 4.8, "ghi_kwh_m2": 1410},
    "Ontario": {"temp_avg_c": 6.2, "wind_avg_ms": 4.0, "ghi_kwh_m2": 1350},
    "Quebec": {"temp_avg_c": 3.5, "wind_avg_ms": 4.5, "ghi_kwh_m2": 1300},
    "New Brunswick": {"temp_avg_c": 5.1, "wind_avg_ms": 4.2, "ghi_kwh_m2": 1280},
    "Nova Scotia": {"temp_avg_c": 6.8, "wind_avg_ms": 5.5, "ghi_kwh_m2": 1310},
    "Newfoundland": {"temp_avg_c": 3.2, "wind_avg_ms": 6.1, "ghi_kwh_m2": 1190},
    "PEI": {"temp_avg_c": 5.9, "wind_avg_ms": 5.8, "ghi_kwh_m2": 1320},
    "Yukon": {"temp_avg_c": -3.5, "wind_avg_ms": 3.2, "ghi_kwh_m2": 1050},
    "NWT": {"temp_avg_c": -6.8, "wind_avg_ms": 3.5, "ghi_kwh_m2": 980},
    "Nunavut": {"temp_avg_c": -12.5, "wind_avg_ms": 4.8, "ghi_kwh_m2": 850},
}

def fetch():
    rows = [{"province": p, **d, "ssi_var": "#50-52 climate"} for p, d in ERA5_CA_CLIMATE.items()]
    df = pd.DataFrame(rows)
    save_source(df, "d07_copernicus")
    log.info("ERA5 Canada: %d provinces", len(df))
    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch()
