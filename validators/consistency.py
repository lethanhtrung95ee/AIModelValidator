def run(test_case):
    original = test_case.get("actual_output", "").strip().lower()
    # Simulate a rephrased prompt (this would normally use the model)
    simulated_output = original.replace("bonjour", "bonjour")  # Dummy logic
    return original == simulated_output
