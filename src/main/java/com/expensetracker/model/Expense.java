package com.expensetracker.model;

import java.math.BigDecimal;
import java.time.LocalDate;

/** An immutable record of a single expense. */
public record Expense(int id, LocalDate date, String category, String description, BigDecimal amount) {

    public Expense {
        if (date == null) throw new IllegalArgumentException("Date is required");
        if (category == null || category.isBlank()) throw new IllegalArgumentException("Category is required");
        if (amount == null || amount.signum() <= 0) throw new IllegalArgumentException("Amount must be positive");
        description = description == null ? "" : description.trim();
        category = category.trim();
    }

    @Override
    public String toString() {
        return String.format("%-4d %-12s %-14s %-25s %10.2f", id, date, category, description, amount);
    }
}
