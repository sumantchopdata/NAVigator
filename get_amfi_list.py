# get AMFI list of mutual funds
#%%
import requests

url = "https://www.amfiindia.com/spages/NAVAll.txt"

response = requests.get(url)
response.raise_for_status()

with open("data/amfi_nav.txt", "w", encoding="utf-8") as f:
    f.write(response.text)