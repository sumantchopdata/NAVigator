import requests

def search_scheme(query):
    url = "https://api.mfapi.in/mf/search?q=" + query
    r = requests.get(url, timeout=10)
    r.raise_for_status()

    results = r.json()

    return results[:3]  # top 3