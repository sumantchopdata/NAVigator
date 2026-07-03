# parse amfi_nav.txt and return a dataframe with scheme_code and scheme_name
#%%
import pandas as pd

def load_scheme_list(path="data/amfi_nav.txt"):

    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) >= 5 and parts[0].isdigit():
                rows.append({
                    "scheme_code": parts[0],
                    "scheme_name": parts[3]
                })

    return pd.DataFrame(rows)