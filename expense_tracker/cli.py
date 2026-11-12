from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

from .service import ExpenseService
from .storage import CsvExpenseRepository

DATA_FILE = Path("data") / "expenses.csv"

MENU = """
1. Add expense
2. View all expenses
3. Delete expense
4. Search expenses
5. Summary
0. Exit"""


def add_expense(service: ExpenseService) -> None:
    try:
        raw = input("Date (YYYY-MM-DD, blank = today): ").strip()
        when = date.fromisoformat(raw) if raw else date.today()
        category = input("Category (e.g. Food, Travel): ")
        description = input("Description: ")
        amount = Decimal(input("Amount: ").strip())
        expense = service.add(when, category, description, amount)
        print("Added:", expense)
    except ValueError as err:
        print(f"Error: {err}")
    except InvalidOperation:
        print("Invalid amount.")


def delete_expense(service: ExpenseService) -> None:
    try:
        expense_id = int(input("Expense ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    print("Deleted." if service.delete(expense_id) else "No expense with that ID.")


def print_list(expenses) -> None:
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<4} {'Date':<12} {'Category':<14} {'Description':<25} {'Amount':>10}")
    print("-" * 70)
    for e in expenses:
        print(e)


def print_summary(service: ExpenseService) -> None:
    today = date.today()
    print("\n--- Summary ---")
    print(f"Total spent:  {service.total():>10.2f}")
    print(f"This month:   {service.total_for_month(today.year, today.month):>10.2f}")
    print("By category:")
    for category, amount in service.totals_by_category().items():
        print(f"  {category:<18} {amount:>10.2f}")


def main() -> None:
    service = ExpenseService(CsvExpenseRepository(DATA_FILE))
    print("=== Expense Tracker ===")
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense(service)
        elif choice == "2":
            print_list(service.list_all())
        elif choice == "3":
            delete_expense(service)
        elif choice == "4":
            print_list(service.search(input("Keyword: ").strip()))
        elif choice == "5":
            print_summary(service)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
