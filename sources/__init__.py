"""sources — Data-source plug-ins for SSI Canada Digital-Twin.

Each module fetches from a national data source and persists via common.storage.
"""
from sources import d01_cer, d02_statcan, d03_nrcan, d04_eccc, d05_osm, d06_ieso, d07_copernicus
