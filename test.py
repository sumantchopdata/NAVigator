#%%
# test
from analyse import analyze_fund
from decision_engine import count_results, determine_recommendation, determine_risk
from utilities import search_scheme, fetch_nav_history

mf = 'Parag Parikh Flexi Cap Fund - Direct Plan - Growth'
scheme_code = search_scheme(mf)
scheme_code = scheme_code[0]['schemeCode']
df = fetch_nav_history(scheme_code)
df.head()
# %%
metrics = analyze_fund(df, mf)
print(metrics)
# %%
results = count_results(metrics)
print(results)
# %%
results = determine_recommendation(results)
print(results)
# %%
final_results = determine_risk(results)
print(final_results)
# %%
from parse_amfi_list import load_scheme_list
df = load_scheme_list()
df.head()
# %%
