# Expense Tracker (Java)

A simple console-based expense tracker built with Java 17 and Maven. Expenses are saved to a CSV file so your data persists between runs.

## Features
- Add expenses with date, category, description and amount
- View all expenses (sorted by date)
- Delete an expense by ID
- Search by keyword (category or description)
- Summary: overall total, current month total, totals by category
- Data stored in `data/expenses.csv`
- Unit tests with JUnit 5

## Project Structure
```
expense-tracker/
├── pom.xml
├── data/                      # expenses.csv is created here
└── src/
    ├── main/java/com/expensetracker/
    │   ├── Main.java              # console menu
    │   ├── model/Expense.java
    │   ├── service/ExpenseService.java
    │   └── storage/CsvExpenseRepository.java
    └── test/java/com/expensetracker/service/ExpenseServiceTest.java
```

## Requirements
- JDK 17 or higher
- Maven 3.6+ (optional if you compile with `javac`)

## Build & Run
```bash
mvn clean package
java -jar target/expense-tracker-1.0.0.jar
```

Run tests:
```bash
mvn test
```

Without Maven:
```bash
mkdir out
javac -d out $(find src/main -name "*.java")
java -cp out com.expensetracker.Main
```

## Sample Session
```
=== Expense Tracker ===
1. Add expense
2. View all expenses
...
Choose: 1
Date (yyyy-MM-dd, blank = today):
Category (e.g. Food, Travel): Food
Description: Lunch
Amount: 120.50
```

## Future Improvements
- Monthly budgets and alerts
- Export reports to PDF/Excel
- JavaFX or Spring Boot web UI
- Database (SQLite/MySQL) storage

## License
MIT
