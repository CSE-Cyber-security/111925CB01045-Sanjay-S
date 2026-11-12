from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Dict, List

from .models import Expense
from .storage import CsvExpenseRepository


class ExpenseService:
    """Business logic for managing expenses."""

    def __init__(self, repository: CsvExpenseRepository):
        self.repository = repository
        self.expenses: List[Expense] = repository.load()

    def add(self, when: date, category: str, description: str, amount: Decimal) -> Expense:
        next_id = max((e.id for e in self.expenses), default=0) + 1
        expense = Expense(next_id, when, category.strip(), description.strip(), Decimal(amount))
        self.expenses.append(expense)
        self.repository.save(self.expenses)
        return expense

    def delete(self, expense_id: int) -> bool:
        remaining = [e for e in self.expenses if e.id != expense_id]
        if len(remaining) == len(self.expenses):
            return False
        self.expenses = remaining
        self.repository.save(self.expenses)
        return True

    def list_all(self) -> List[Expense]:
        return sorted(self.expenses, key=lambda e: (e.date, e.id))

    def search(self, keyword: str) -> List[Expense]:
        k = keyword.lower()
        return [e for e in self.list_all()
                if k in e.description.lower() or k in e.category.lower()]

    def total(self) -> Decimal:
        return sum((e.amount for e in self.expenses), Decimal("0"))

    def total_for_month(self, year: int, month: int) -> Decimal:
        return sum((e.amount for e in self.expenses
                    if e.date.year == year and e.date.month == month), Decimal("0"))

    def totals_by_category(self) -> Dict[str, Decimal]:
        totals = defaultdict(Decimal)
        for e in self.expenses:
            totals[e.category] += e.amount
        return dict(sorted(totals.items()))
