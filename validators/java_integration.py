import subprocess

def run(test_case):
    output = test_case.get("actual_output", "")
    try:
        result = subprocess.run(
            ["java", "-cp", "java_engine", "RuleChecker", output],
            capture_output=True,
            text=True,
            timeout=5
        )
        return int(result.stdout.strip())
    except Exception as e:
        print(f"Java integration error: {e}")
        return -1
