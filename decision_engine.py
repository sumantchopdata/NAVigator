# Decision Engine for the NAVigator

'''
The input looks like a dictionary of the form:
metrics = {
    "alpha": 2.8,
    "sharpe": 1.24,
    "sortino": 1.72,
    "beta": 0.95,
    "volatility": 15.3,
    "benchmark_return": 14.2,
    "annualized_return": 16.8
}

It is based on six explainable rules:

Rule 1: alpha > 0 => passed, else failed
Rule 2: sharpe > 1 => passed, else failed
Rule 3: sortino > 1 => passed, else failed
Rule 4: Annualized Return > Benchmark Return
Rule 5: 0.8 <= beta <= 1.2, Outside this range: Warning (not failure)
Rule 6: volatility < 15% => passed, else warning
'''

RULES = [
    {
        "name": "alpha",
        "check": lambda m: m["alpha"] > 0,
        "pass": "alpha is positive.",
        "fail": "alpha is not positive.",
        "type": "failure"
    },
    {
        "name": "sharpe",
        "check": lambda m: m["sharpe"] > 1,
        "pass": "sharpe is positive.",
        "fail": "sharpe is not positive.",
        "type": "failure"
    },
    {
        "name": "sortino",
        "check": lambda m: m["sortino"] > 1,
        "pass": "sortino is positive.",
        "fail": "sortino is not positive.",
        "type": "failure"
    },
    {
        "name": "benchmark",
        "check": lambda m: m["annualized_return"] >= m["benchmark_return"],
        "pass": "annualized_return >= benchmark_return",
        "fail": "annualized_return < benchmark_return",
        "type": "failure"
    },
    {
        "name": "beta",
        "check": lambda m: 0.8 <= m["beta"] <= 1.2,
        "pass": "beta within preferred range (0.8 - 1.2).",
        "fail": "beta outside preferred range (0.8 - 1.2).",
        "type": "warning"
    },
    {
        "name": "volatility",
        "check": lambda m: m["volatility"] < 15,
        "pass": "volatility less than 15%",
        "fail": "volatility greater than or equal to 15%",
        "type": "warning"
    }
]


def evaluate_rules(metrics):
    results = {
        "passed": [],
        "failed": [],
        "warnings": [],
    }

    for rule in RULES:
        if rule["check"](metrics):
            results["passed"].append(rule["pass"])
        else:
            if rule["type"] == "failure":
                results["failed"].append(rule["fail"])
            else:
                results["warnings"].append(rule["fail"])

    # Recommendation
    failures = len(results["failed"])
    if failures == 0:
        results["recommendation"] = "HOLD"
    elif failures == 1:
        results["recommendation"] = "WATCH"
    else:
        results["recommendation"] = "REVIEW"

    # Risk
    warnings = len(results["warnings"])
    if warnings == 0:
        results["risk"] = "LOW"
    elif warnings == 1:
        results["risk"] = "MEDIUM"
    else:
        results["risk"] = "HIGH"

    return results