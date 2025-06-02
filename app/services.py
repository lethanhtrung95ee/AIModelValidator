from validators import correctness, consistency, java_integration
from app.models import TestCase, TestResult

validators = {
    "correctness": correctness.run,
    "consistency": consistency.run,
    "java_score": java_integration.run
}

def run_tests(test_cases: list[TestCase]) -> list[TestResult]:
    results = []

    for case in test_cases:
        result = {
            "prompt": case.prompt,
            "expected_output": case.expected_output,
            "actual_output": case.actual_output,
        }
        for name, validator in validators.items():
            result[name] = validator(case.dict())
        results.append(result)

    return results
