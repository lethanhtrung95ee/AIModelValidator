import json
import csv
from validators import correctness, consistency, java_integration

# List of enabled validators
validators = {
    "correctness": correctness.run,
    "consistency": consistency.run,
    "java_score": java_integration.run
}
# Load test cases
with open("data/test_cases.json", encoding="utf-8") as f:
    test_cases = json.load(f)

results = []

# Run all validators on each test case
for case in test_cases:
    result = {
        "Prompt": case.get("prompt"),
        "Expected": case.get("expected_output"),
        "Actual": case.get("actual_output")
    }
    for name, validator_fn in validators.items():
        result[name] = validator_fn(case)
    results.append(result)

# Save report
with open("reports/report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print("✅ Report generated: reports/report.csv")
