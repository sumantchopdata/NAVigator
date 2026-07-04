# analyzer.py
# This module contains the core logic for analyzing mutual fund performance based on historical NAV data.

import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import LOOKBACK_MONTHS, RISK_FREE_RATE
from utilities import fetch_nav_history, compute_returns, get_benchmark_code
import streamlit as st

@st.cache_data
def analyse_fund(df, fund_name):
    '''
    Analyze a mutual fund's performance based on its NAV history
    and compare it to its benchmark. REturn its metrics.
    '''
    cutoff = datetime.now() - relativedelta(months=LOOKBACK_MONTHS)

    df = df[df["date"] >= cutoff]

    if len(df) < 10:
        return None

    # Fund returns
    df = compute_returns(df)

    # Benchmark
    benchmark_code = get_benchmark_code(fund_name)
    bench_df = fetch_nav_history(benchmark_code)
    bench_df = bench_df[bench_df["date"] >= cutoff]
    bench_df = compute_returns(bench_df)

    # Align dates
    merged = df.merge(bench_df, on="date", suffixes=("_fund", "_bench"))

    if len(merged) < 10:
        return None

    fund_returns = merged["returns_fund"]
    bench_returns = merged["returns_bench"]

    # ---- Basic return ----
    total_return = (df["nav"].iloc[-1] / df["nav"].iloc[0]) - 1

    # ---- Volatility ----
    vol = fund_returns.std() * np.sqrt(252) # 252 trading days in a year

    # ---- Sharpe ----
    excess_return = fund_returns.mean() * 252 - RISK_FREE_RATE
    sharpe = excess_return / vol if vol != 0 else 0

    # ---- Sortino ----
    downside = fund_returns[fund_returns < 0]
    downside_std = downside.std() * np.sqrt(252)

    sortino = excess_return / downside_std if downside_std != 0 else 0

    # ---- Beta ----
    covariance = np.cov(fund_returns, bench_returns)[0][1]
    variance = np.var(bench_returns)

    beta = covariance / variance if variance != 0 else 0

    # ---- Alpha (CAPM) ----
    bench_return_annual = bench_returns.mean() * 252
    alpha = (
        (fund_returns.mean() * 252)
        - (RISK_FREE_RATE + beta * (bench_return_annual - RISK_FREE_RATE))
    )
    annualized_return = (
        (df["nav"].iloc[-1] / df["nav"].iloc[0]) ** (252 / len(df))
        ) - 1

    return {
        "return_pct": round(total_return * 100, 2),                     # return from beginning to end in percentage
        "volatility": round(vol * 100, 2),                              # annualized standard deviation of returns
        "sharpe": round(sharpe, 2),                                     # risk-adjusted return metric (Sharpe Ratio)
        "sortino": round(sortino, 2),                                   # risk-adjusted return metric focusing on downside risk (Sortino Ratio)
        "beta": round(beta, 2),                                         # measure of the fund's volatility relative to its benchmark
        "alpha": round(alpha * 100, 2),                                 # measure of the fund's performance relative to its expected return based on its beta
        "annualized_return": round(annualized_return * 100, 2),         # annualized return of the fund
        "benchmark_return": round(bench_returns.mean() * 252 * 100, 2)  # average annual return of the benchmark
    }