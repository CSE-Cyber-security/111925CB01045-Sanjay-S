package com.expensetracker.service;

import com.expensetracker.model.Expense;
import com.expensetracker.storage.CsvExpenseRepository;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.YearMonth;
import java.util.*;
import java.util.stream.Collectors;

/** Business logic for managing expenses. */
public class ExpenseService {

    private final CsvExpenseRepository repository;
    private final List<Expense> expenses;

    public ExpenseService(CsvExpenseRepository repository) {
        this.repository = repository;
        this.expenses = new ArrayList<>(repository.load());
    }

    public Expense add(LocalDate date, String category, String description, BigDecimal amount) {
        int nextId = expenses.stream().mapToInt(Expense::id).max().orElse(0) + 1;
        Expense e = new Expense(nextId, date, category, description, amount);
        expenses.add(e);
        repository.save(expenses);
        return e;
    }

    public boolean delete(int id) {
        boolean removed = expenses.removeIf(e -> e.id() == id);
        if (removed) repository.save(expenses);
        return removed;
    }

    public List<Expense> listAll() {
        return expenses.stream()
                .sorted(Comparator.comparing(Expense::date).thenComparingInt(Expense::id))
                .collect(Collectors.toList());
    }

    public List<Expense> search(String keyword) {
        String k = keyword.toLowerCase();
        return listAll().stream()
                .filter(e -> e.description().toLowerCase().contains(k)
                        || e.category().toLowerCase().contains(k))
                .collect(Collectors.toList());
    }

    public BigDecimal total() {
        return expenses.stream().map(Expense::amount).reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public BigDecimal totalForMonth(YearMonth month) {
        return expenses.stream()
                .filter(e -> YearMonth.from(e.date()).equals(month))
                .map(Expense::amount)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public Map<String, BigDecimal> totalsByCategory() {
        Map<String, BigDecimal> map = new TreeMap<>();
        for (Expense e : expenses) {
            map.merge(e.category(), e.amount(), BigDecimal::add);
        }
        return map;
    }
}
