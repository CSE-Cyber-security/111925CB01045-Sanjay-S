package com.expensetracker.service;

import com.expensetracker.storage.CsvExpenseRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;

import java.math.BigDecimal;
import java.nio.file.Path;
import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

class ExpenseServiceTest {

    @TempDir
    Path tempDir;

    private ExpenseService newService() {
        return new ExpenseService(new CsvExpenseRepository(tempDir.resolve("expenses.csv")));
    }

    @Test
    void addAndTotal() {
        ExpenseService s = newService();
        s.add(LocalDate.of(2026, 1, 5), "Food", "Lunch", new BigDecimal("120.50"));
        s.add(LocalDate.of(2026, 1, 6), "Travel", "Bus", new BigDecimal("30"));
        assertEquals(new BigDecimal("150.50"), s.total());
        assertEquals(2, s.totalsByCategory().size());
    }

    @Test
    void dataPersistsWithCommasInDescription() {
        newService().add(LocalDate.of(2026, 2, 1), "Food", "Rice, dal, \"veg\"", new BigDecimal("80"));
        ExpenseService reloaded = newService();
        assertEquals(1, reloaded.listAll().size());
        assertEquals("Rice, dal, \"veg\"", reloaded.listAll().get(0).description());
    }

    @Test
    void deleteWorks() {
        ExpenseService s = newService();
        s.add(LocalDate.now(), "Food", "Tea", new BigDecimal("10"));
        assertTrue(s.delete(1));
        assertFalse(s.delete(1));
        assertTrue(s.listAll().isEmpty());
    }

    @Test
    void rejectsNegativeAmount() {
        assertThrows(IllegalArgumentException.class,
                () -> newService().add(LocalDate.now(), "Food", "Bad", new BigDecimal("-5")));
    }
}
