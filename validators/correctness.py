def run(test_case):
    expected = test_case.get("expected_output", "").strip().lower()
    actual = test_case.get("actual_output", "").strip().lower()
    return expected == actual
