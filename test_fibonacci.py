import subprocess
import sys
import unittest

SCRIPT = "fibonacci.py"


def run_program(user_input):
    """Run fibonacci.py, feed it user_input on stdin, return the CompletedProcess."""
    return subprocess.run(
        [sys.executable, SCRIPT],
        input=user_input,
        capture_output=True,
        text=True,
    )


def series_from_output(stdout):
    """Strip the prompt text and return the printed numbers as a list of ints."""
    prompt = "Enter the number of terms: "
    text = stdout.replace(prompt, "")
    return [int(x) for x in text.split()]


class TestFibonacci(unittest.TestCase):

    def test_zero_terms(self):
        result = run_program("0\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(series_from_output(result.stdout), [])

    def test_one_term(self):
        result = run_program("1\n")
        self.assertEqual(series_from_output(result.stdout), [0])

    def test_two_terms(self):
        result = run_program("2\n")
        self.assertEqual(series_from_output(result.stdout), [0, 1])

    def test_five_terms(self):
        result = run_program("5\n")
        self.assertEqual(series_from_output(result.stdout), [0, 1, 1, 2, 3])

    def test_ten_terms(self):
        result = run_program("10\n")
        self.assertEqual(
            series_from_output(result.stdout),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
        )

    def test_twenty_terms_last_value(self):
        result = run_program("20\n")
        series = series_from_output(result.stdout)
        self.assertEqual(len(series), 20)
        self.assertEqual(series[-1], 4181)

    def test_each_term_is_sum_of_previous_two(self):
        result = run_program("15\n")
        series = series_from_output(result.stdout)
        for i in range(2, len(series)):
            self.assertEqual(series[i], series[i - 1] + series[i - 2])

    def test_negative_input_prints_nothing(self):
        result = run_program("-5\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(series_from_output(result.stdout), [])

    def test_non_integer_input_raises_error(self):
        result = run_program("abc\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ValueError", result.stderr)

    def test_decimal_input_raises_error(self):
        result = run_program("3.5\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ValueError", result.stderr)

    def test_empty_input_raises_error(self):
        result = run_program("\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ValueError", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
