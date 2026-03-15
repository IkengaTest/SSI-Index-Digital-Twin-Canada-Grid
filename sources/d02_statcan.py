"""D02-StatsCan: Statistics Canada — Demographics and Economics.

Population, GDP, industrial output per province/territory.
Source: https://www.statcan.gc.ca/
Variables: #55-60 (socioeconomic), #61-65 (demographic)
"""
import logging
import pandas as pd
from common.storage import save_source
import config

log = logging.getLogger(__name__)

STATCAN_DATA = {
    "Ontario": {"pop_million": 15.8, "gdp_billion_cad": 936, "pop_density": 15.2, "median_age": 41.1},
    "Quebec": {"pop_million": 8.8, "gdp_billion_cad": 487, "pop_density": 6.4, "median_age": 43.2},
    "British Columbia": {"pop_million": 5.5, "gdp_billion_cad": 356, "pop_density": 5.5, "median_age": 42.3},
    "Alberta": {"pop_million": 4.8, "gdp_billion_cad": 388, "pop_density": 7.2, "median_age": 37.8},
    "Manitoba": {"pop_million": 1.4, "gdp_billion_cad": 79, "pop_density": 2.3, "median_age": 37.5},
    "Saskatchewan": {"pop_million": 1.2, "gdp_billion_cad": 82, "pop_density": 2.0, "median_age": 37.2},
    "Nova Scotia": {"pop_million": 1.1, "gdp_billion_cad": 52, "pop_density": 19.4, "median_age": 45.1},
    "New Brunswick": {"pop_million": 0.83, "gdp_billion_cad": 42, "pop_density": 11.7, "median_age": 46.2},
    "Newfoundland": {"pop_million": 0.53, "gdp_billion_cad": 38, "pop_density": 1.4, "median_age": 47.8},
    "PEI": {"pop_million": 0.17, "gdp_billion_cad": 8.2, "pop_density": 29.4, "median_age": 43.5},
    "Yukon": {"pop_million": 0.044, "gdp_billion_cad": 3.5, "pop_density": 0.09, "median_age": 39.1},
    "NWT": {"pop_million": 0.045, "gdp_billion_cad": 5.1, "pop_density": 0.04, "median_age": 35.2},
    "Nunavut": {"pop_million": 0.040, "gdp_billion_cad": 3.8, "pop_density": 0.02, "median_age": 27.7},
}

def fetch():
    rows = [{"province": p, **d, "ssi_var": "#55-60 socioeconomic"} for p, d in STATCAN_DATA.items()]
    df = pd.DataFrame(rows)
    save_source(df, "d02_statcan")
    log.info("StatsCan: %d provinces/territories", len(df))
    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch()
