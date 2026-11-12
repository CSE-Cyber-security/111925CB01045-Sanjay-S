import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from expense_tracker.service import ExpenseService
from expense_tracker.storage import CsvExpenseRepository


class ExpenseServiceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "expenses.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def new_service(self):
        return ExpenseService(CsvExpenseRepository(self.path))

    def test_add_and_total(self):
        s = self.new_service()
        s.add(date(2026, 1, 5), "Food", "Lunch", Decimal("120.50"))
        s.add(date(2026, 1, 6), "Travel", "Bus", Decimal("30"))
        self.assertEqual(s.total(), Decimal("150.50"))
        self.assertEqual(len(s.totals_by_category()), 2)

    def test_persists_with_commas_and_quotes(self):
        self.new_service().add(date(2026, 2, 1), "Food", 'Rice, dal, "veg"', Decimal("80"))
        reloaded = self.new_service()
        self.assertEqual(len(reloaded.list_all()), 1)
        self.assertEqual(reloaded.list_all()[0].description, 'Rice, dal, "veg"')

    def test_delete(self):
        s = self.new_service()
        s.add(date.today(), "Food", "Tea", Decimal("10"))
        self.assertTrue(s.delete(1))
        self.assertFalse(s.delete(1))
        self.assertEqual(s.list_all(), [])

    def test_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            self.new_service().add(date.today(), "Food", "Bad", Decimal("-5"))

    def test_monthly_total_and_search(self):
        s = self.new_service()
        s.add(date(2026, 3, 1), "Food", "Pizza", Decimal("200"))
        s.add(date(2026, 4, 1), "Food", "Burger", Decimal("100"))
        self.assertEqual(s.total_for_month(2026, 3), Decimal("200"))
        self.assertEqual(len(s.search("pizza")), 1)


if __name__ == "__main__":
    unittest.main()
