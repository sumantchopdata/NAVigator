# NAVigator 📈

**Mutual fund analysis and recommendation engine for Indian investors.**

NAVigator helps investors analyse mutual funds beyond simple returns by combining quantitative performance metrics with an explainable decision engine. Instead of providing a simple "buy" or "sell" recommendation, NAVigator evaluates multiple aspects of a fund and explains *why* it reached its conclusion.

The project is built in Python with an interactive Streamlit interface, making professional-level fund analysis accessible to individual investors.

<img width="300" alt="image" src="https://github.com/user-attachments/assets/f0ce67d8-e5db-45d2-b54f-22775ec086ad" /> <img width="300" alt="image" src="https://github.com/user-attachments/assets/78a2f768-bfda-4dcf-a924-5a162228bcc7" />

---

## ⚠️ Disclaimer

NAVigator is an educational and analytical tool. The recommendations produced by the application should **not** be considered financial advice. Investment decisions should always be made after conducting your own research and considering your financial goals and risk tolerance.

---

## Features

* 📊 Fetch historical NAV data for Indian mutual funds
* 📈 Calculate key performance and risk metrics

  * Annualised Return
  * Volatility
  * Sharpe Ratio
  * Sortino Ratio
  * Alpha
  * Beta
  
* Benchmark comparison
* Explainable rule-based decision engine
* Human-readable investment recommendations
* Interactive Streamlit dashboard

---

## Tech Stack

* Python
* Streamlit
* NumPy
* mfapi.in (NAV data)

---

## Project Structure

```text
NAVigator/
│
├── app.py                  # Streamlit application
├── analyse.py              # Performance and risk metric calculations
├── decision_engine.py      # Recommendation logic
├── fetch_nav.py            # NAV data retrieval
├── utilities.py            # Helper functions
├── requirements.txt
└── README.md
```

---

## Decision Engine

NAVigator evaluates a fund using multiple dimensions instead of relying on a single metric.

The recommendation is based on factors such as:

* Alpha
* Sharpe Ratio
* Sortino Ratio
* Beta
* Volatility
* Annualised Returns
* Benchmark Outperformance

Based on these metrics, the engine generates recommendations such as:

* ✅ Hold
* ⚠️ Watch
* ❗ Review

Each recommendation is accompanied by an explanation highlighting the strengths and weaknesses of the fund.

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/NAVigator.git
```

Move into the project directory

```bash
cd NAVigator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## Roadmap

Planned improvements include:

* Portfolio-level analysis
* Mutual fund comparison
* Automatic portfolio import
* More benchmark options
* Better visualisations
* AI-generated investment insights
* Historical recommendation tracking
* Performance attribution analysis

---

## Contributing

Contributions, feature requests, and suggestions are welcome. Feel free to open an issue or submit a pull request.

---
