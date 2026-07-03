# streamlit app 

import streamlit as st
from analyse import analyze_fund
from decision_engine import count_results, determine_recommendation, determine_risk
from utilities import fetch_nav_history
from parse_amfi_list import load_scheme_list

st.title("NAVigator")
st.write("Mutual Fund Analysis and Recommendation Tool")

schemes_df = load_scheme_list()

selected_scheme = st.selectbox(
    "Select Mutual Fund",
    schemes_df["scheme_name"]
)

scheme_code = schemes_df.loc[
    schemes_df["scheme_name"] == selected_scheme,
    "scheme_code"
].iloc[0]

df = fetch_nav_history(scheme_code)

# print that df is fetched and show the date range
st.write(f"Fetched NAV history for {selected_scheme} from {df['date'].min()} to {df['date'].max()}")
st.write(f"Total records: {len(df)}")

if st.button("Analyze Fund"):
    metrics = analyze_fund(df, selected_scheme)

    st.header(f"Fund Metrics obtained for {selected_scheme}:")
    
    col1, col2 = st.columns(2)

    with col1:
        st.header("Performance Metrics")
        st.write('Alpha: {:.2%}'.format(metrics['alpha']))
        st.write('Return: {:.2%}'.format(metrics['return_pct']))
        st.write('Total Returns: {:.2%}'.format(metrics['total_return']))
        st.write('Annualized Return: {:.2%}'.format(metrics['annualized_return']))

    with col2:
        st.header("Risk Metrics")
        st.write('Beta: {:.2f}'.format(metrics['beta']))
        st.write('Volatility: {:.2%}'.format(metrics['volatility']))
        st.write('Sharpe Ratio: {:.2f}'.format(metrics['sharpe']))
        st.write('Sortino Ratio: {:.2f}'.format(metrics['sortino']))        

    results = count_results(metrics)
    results = determine_recommendation(results)
    final_results = determine_risk(results)

    st.header("Recommendation")

    if final_results["recommendation"] == "HOLD":
        st.success("Recommendation: HOLD")
    elif final_results["recommendation"] == "WATCH":
        st.warning("Recommendation: WATCH")
    elif final_results["recommendation"] == "REVIEW":
        st.error("Recommendation: REVIEW")
    
    st.write("Recommendation based on the following results:")
    st.write("Passed Rules:")
    for rule in final_results["passed"]:
        st.write(f"- {rule}")

    st.write("Failed Rules:")
    for rule in final_results["failed"]:
        st.write(f"- {rule}")

    st.header("Risk Assessment")

    if final_results['risk'] == 'LOW':
        st.success('Risk Level: LOW')
    elif final_results['risk'] == 'MEDIUM':
        st.warning('Risk Level: MEDIUM')
    elif final_results['risk'] == 'HIGH':
        st.error('Risk Level: HIGH')

    st.write("Risk assessment based on the following warnings:")
    for rule in final_results["warnings"]:
        st.write(f"- {rule}")