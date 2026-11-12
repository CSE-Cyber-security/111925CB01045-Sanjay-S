import csv
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import List

from .models import Expense

FIELDS = ["id", "date", "category", "description", "amount"]


class CsvExpenseRepository:
    """Loads and saves expenses to a CSV file."""

    def __init__(self, path):
        self.path = Path(path)

    def load(self) -> List[Expense]:
        if not self.path.exists():
            return []
        with self.path.open(newline="", encoding="utf-8") as f:
            return [
                Expense(
                    id=int(row["id"]),
                    date=date.fromisoformat(row["date"]),
                    category=row["category"],
                    description=row["description"],
                    amount=Decimal(row["amount"]),
                )
                for row in csv.DictReader(f)
            ]

    def save(self, expenses: List[Expense]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)
            for e in expenses:
                writer.writerow([e.id, e.date.isoformat(), e.category, e.description, e.amount])
