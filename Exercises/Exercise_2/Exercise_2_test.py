import pytest
import subprocess
import sys

@pytest.mark.parametrize("num1,num2,expected_result", [
    ("4", "5", "20"),
    ("10", "3", "30"),
    ("0", "100", "0"),
    ("-2", "7", "-14")
])
def test_multiplication(num1, num2, expected_result):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'Exercise_2.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{num1}\n{num2}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Check if the output format is correct and the calculation is accurate
    expected_output = f"The result of multiplying {num1} and {num2} is {expected_result}."
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"

# To run this test, save it as test_main.py and run: pytest test_main.py