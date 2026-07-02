# Decision Engine for the MF Analyzer

'''
The input looks like a dictionary of the form:
metrics = {
    "alpha": 2.8,
    "sharpe": 1.24,
    "sortino": 1.72,
    "beta": 0.95,
    "volatility": 15.3,
    "benchmark_return": 14.2,
    "fund_return": 16.8
}

The output looks like a dictionary of the form:
{
    "recommendation": "HOLD",

    "passed": [
        "Positive alpha",
        "Sharpe ratio above 1",
        "Outperformed benchmark"
    ],

    "warnings": [
        "Slightly high volatility"
    ],

    "failed": [
        "Beta above preferred range"
    ]
}

It is based on six explainable rules:

Rule 1: alpha > 0 => passed, else failed
Rule 2: sharpe > 1 => passed, else failed
Rule 3: sortino > 1 => passed, else failed
Rule 4: Fund Return > Benchmark Return
Rule 5: 0.8 <= beta <= 1.2, Outside this range: Warning (not failure)
Rule 6: volatility < 15% => passed, else warning
'''

def alpha_rule(alpha):
    if alpha > 0:
        return "passed"
    else:
        return "failed"
    

def sharpe_rule(sharpe):
    if sharpe > 1:
        return "passed"
    else:
        return "failed"
    

def sortino_rule(sortino):
    if sortino > 1:
        return "passed"
    else:
        return "failed"


def benchmark_rule(fund_return, benchmark_return):
    if fund_return >= benchmark_return:
        return "passed"
    else:
        return "failed"


def beta_rule(beta):
    if 0.8 <= beta <= 1.2:
        return "passed"
    else:
        return "warning"


def volatility_rule(volatility):
    if volatility < 15:
        return "passed"
    else:
        return "warning"


def count_results(metrics):
    results = {
        "risk": None,
        "recommendation": None,
        "passed": [],
        "warnings": [],
        "failed": []
    }

    # Evaluate each rule
    rules = {
        "alpha": alpha_rule(metrics["alpha"]),
        "sharpe": sharpe_rule(metrics["sharpe"]),
        "sortino": sortino_rule(metrics["sortino"]),
        "benchmark": benchmark_rule(metrics["fund_return"],
                                    metrics["benchmark_return"]),
        "beta": beta_rule(metrics["beta"]),
        "volatility": volatility_rule(metrics["volatility"])
    }

    # Populate results based on rule evaluations
    for rule, result in rules.items():
        if result == "passed":
            results["passed"].append(f"{rule} passed")
        elif result == "failed":
            results["failed"].append(f"{rule} failed")
        elif result == "warning":
            results["warnings"].append(f"{rule} warning")

    return results

def determine_recommendation(results):

    # Determine overall recommendation
    if len(results["failed"]) == 0:
        results["recommendation"] = "HOLD"
    elif len(results["failed"]) == 1:
        results["recommendation"] = "WATCH"
    elif len(results["failed"]) >= 1:
        results["recommendation"] = "REVIEW"

    return results

def determine_risk(results):

    # Determine risk level based on warnings
    if len(results["warnings"]) == 0:
        results["risk"] = "LOW"

    elif len(results["warnings"]) == 1:
        results["risk"] = "MEDIUM"

    else:
        results["risk"] = "HIGH"

    return results