from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Expense:
    """A single expense record."""

    id: int
    date: date
    category: str
    description: str
    amount: Decimal

    def __post_init__(self):
        if not self.category or not self.category.strip():
            raise ValueError("Category is required")
        if self.amount <= 0:
            raise ValueError("Amount must be positive")

    def __str__(self) -> str:
        return (f"{self.id:<4} {self.date.isoformat():<12} {self.category:<14} "
                f"{self.description:<25} {self.amount:>10.2f}")
