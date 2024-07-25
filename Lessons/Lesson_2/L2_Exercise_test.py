import subprocess
import sys

def test_hello_world():
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'L2_Exercise.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Capture the output
    stdout, stderr = process.communicate()

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Remove any leading/trailing whitespace and newlines
    output = stdout.strip()

    # Check if the output is exactly "Hello World!"
    assert output == "Hello World!", f"Expected 'Hello World!', but got '{output}'"

# To run this test, save it as test_main.py and run: pytest test_main.py