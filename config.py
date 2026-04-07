# config.py
# configuration file for the mutual fund analyzer project.
# It contains constants and settings

TELEGRAM_BOT_TOKEN = "1234567890:AAHkLz8qP4xyzABCDE_FakeTokenExample"
TELEGRAM_CHAT_ID = "1234567890"

MFAPI_BASE = "https://api.mfapi.in/mf"

LOOKBACK_MONTHS = 12  # analyze performance over the last 12 months
GOOD_RETURN = 0.10     # +10%
BAD_RETURN = 0.00      # <0%
RISK_FREE_RATE = 0.06  # 6% annual

# These are the codes for index funds that we will use as benchmarks for
# different categories of mutual funds.

BENCHMARK_MAP = {
    "large cap": "147794",         # Motilal Oswal Nifty 50 Index Fund - Direct plan - Growth
    "mid cap": "147622",           # Motilal Oswal Nifty Midcap 150 Index Fund
    "small cap": "147623",         # Motilal Oswal Nifty smallcap 250 index fund direct
    "flexi cap": "147794",         # fallback to Nifty 50
    "multi cap": "147794",         # fallback to Nifty 50
    "large and mid cap": "147704", # Motilal Oswal Large and Midcap Fund Direct Growth 
    "index": "147794",             # fallback to Nifty 50
    "elss": "147725",              # motilal oswal nifty 500 index fund - direct plan growth
    "debt": "120608",              # ICICI Prudential short term gilt fund - direct plan - growth
    "gilt": "120608",              # ICICI Prudential short term gilt fund - direct plan - growth
}
