# mf_data.py
# This module contains functions to fetch and process mutual fund data from the MFAPI.

import requests
import pandas as pd

def fetch_nav_history(scheme_code):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()

    data = r.json()["data"]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["nav"] = df["nav"].astype(float)

    return df.sort_values("date")