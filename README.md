# Fibonacci Series Generator

A simple Python program that prints the first `n` terms of the Fibonacci series.

## Files

- `fibonacci.py` – the main program
- `test_fibonacci.py` – unit tests for the program

## Requirements

- Python 3.6 or later (no external libraries needed)

## Usage

Run the program:

```bash
python fibonacci.py
```

Enter the number of terms when prompted:

```
Enter the number of terms: 10
0 1 1 2 3 5 8 13 21 34
```

## How It Works

The series starts with 0 and 1. Each next term is the sum of the previous two:

```
0, 1, 1, 2, 3, 5, 8, 13, ...
```

The program keeps two variables, `a` and `b`, and updates them in a loop so that only the last two values are stored at any time.

## Running the Tests

Keep both files in the same folder, then run:

```bash
python test_fibonacci.py
```

The tests cover:

| Case | Input | Expected result |
|------|-------|-----------------|
| Zero terms | `0` | Prints nothing |
| One term | `1` | `0` |
| Five terms | `5` | `0 1 1 2 3` |
| Ten terms | `10` | `0 1 1 2 3 5 8 13 21 34` |
| Twenty terms | `20` | Last term is `4181` |
| Negative number | `-5` | Prints nothing |
| Invalid input | `abc`, `3.5`, empty | Raises `ValueError` |

## Notes

- Entering a non-integer value stops the program with a `ValueError`.
- A negative number or `0` prints nothing.
