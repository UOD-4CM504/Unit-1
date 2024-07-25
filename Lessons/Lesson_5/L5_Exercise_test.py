import pytest
import subprocess
import sys
import re

@pytest.mark.parametrize("input_number,expected_output", [
    ("3", "3x10 = 30"),
    ("10", "10x10 = 100"),
    ("0", "0x10 = 0"),
    ("-5", "-5x10 = -50")
])
def test_multiplication_io(input_number, expected_output):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'L5_Exercise.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{input_number}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Remove any leading/trailing whitespace and split into lines
    output_lines = stdout.strip().split('\n')

    # Check if we have at least one line of output
    assert output_lines, "No output was produced"

    # Check the multiplication result (should be in the last line of output)
    result_line = output_lines[-1]
    assert result_line == expected_output, \
        f"Expected '{expected_output}', but got '{result_line}'"

    # Optional: Check if the input prompt is present (but don't fail if it's not)
    if len(output_lines) > 1 and "enter a whole number" in output_lines[0].lower():
        print("Input prompt is present.")
    else:
        print("Note: Input prompt is not present or not in the expected format.")

# To run this test, save it as test_main.py and run: pytest test_main.py