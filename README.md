# Expense Tracker (Python)

A simple console-based expense tracker written in Python 3. Expenses are saved to a CSV file so your data persists between runs. No external libraries needed.

## Features
- Add expenses with date, category, description and amount
- View all expenses (sorted by date)
- Delete an expense by ID
- Search by keyword (category or description)
- Summary: overall total, current month total, totals by category
- Data stored in `data/expenses.csv`
- Unit tests using `unittest`

## Project Structure
```
expense-tracker-python/
├── main.py                  # entry point
├── requirements.txt
├── data/                    # expenses.csv is created here
├── expense_tracker/
│   ├── models.py            # Expense dataclass
│   ├── storage.py           # CSV read/write
│   ├── service.py           # business logic
│   └── cli.py               # console menu
└── tests/
    └── test_service.py
```

## Requirements
- Python 3.8 or higher

## Run
```bash
python main.py
```

## Run Tests
```bash
python -m unittest discover -s tests -t .
```

## Sample Session
```
=== Expense Tracker ===
1. Add expense
2. View all expenses
...
Choose: 1
Date (YYYY-MM-DD, blank = today):
Category (e.g. Food, Travel): Food
Description: Lunch
Amount: 120.50
Added: 1    2026-01-05   Food           Lunch                         120.50
```

## Future Improvements
- Monthly budgets and alerts
- Export reports to Excel/PDF
- GUI with Tkinter or a web UI with Flask
- SQLite database storage

## License
MIT
