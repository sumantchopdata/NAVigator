# mf_data.py
# This module contains functions to fetch and process mutual fund data from the MFAPI.

import time
import requests
import pandas as pd

def search_scheme(query):
    '''
    Search for mutual fund schemes based on a query string.
    '''
    url = "https://api.mfapi.in/mf/search?q=" + query
    r = requests.get(url, timeout=10)
    r.raise_for_status()

    results = r.json()

    return results[:3]  # top 3

def fetch_nav_history(scheme_code, max_retries=3):
    """
    Fetch NAV history for a given mutual fund scheme code.
    Retries automatically if the API is temporarily slow.
    """

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            data = response.json()["data"]

            df = pd.DataFrame(data)
            df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
            df["nav"] = df["nav"].astype(float)

            return df.sort_values("date")

        except requests.exceptions.ReadTimeout:
            print(f"Attempt {attempt+1}/{max_retries} timed out.")
            time.sleep(2)

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching NAV history: {e}")

    raise Exception("MFAPI is currently unavailable. Please try again later.")