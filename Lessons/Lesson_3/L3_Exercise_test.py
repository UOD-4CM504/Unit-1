import pytest
import subprocess
import sys


def run_script():
    process = subprocess.Popen(
        [sys.executable, 'L3_Exercise.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    return stdout.strip(), stderr.strip()


def test_script_execution():
    stdout, stderr = run_script()

    assert not stderr, f"Script produced errors: {stderr}"

    output_lines = stdout.split('\n')

    # Check each expected output separately
    hello_world_line = None
    division_result = None

    for line in output_lines:
        if line == "Hello World!":
            hello_world_line = line
        elif line.replace('.', '').isdigit():  # Check if the line is a number
            division_result = float(line)

    # Check for "Hello World!" output (fixed NameError)
    assert hello_world_line == "Hello World!", "Expected 'Hello World!' in the output"

    # Check for the division result (fixed TypeError)
    assert division_result is not None, "Expected a numeric result from division"
    assert abs(division_result - 10.0) < 0.001, f"Expected division result close to 10.0, but got {division_result}"

    # Optionally check for "hello world" (fixed SyntaxError)
    if "hello world" in stdout:
        print("Note: 'hello world' is present in the output (SyntaxError fix)")
    else:
        print("Note: 'hello world' is not present in the output (potential missing SyntaxError fix)")

# To run this test, save it as L3_Exercise_test.py and run: pytest L3_Exercise_test.py