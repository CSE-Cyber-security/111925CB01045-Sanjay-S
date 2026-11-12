package com.expensetracker;

import com.expensetracker.model.Expense;
import com.expensetracker.service.ExpenseService;
import com.expensetracker.storage.CsvExpenseRepository;

import java.math.BigDecimal;
import java.nio.file.Path;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.DateTimeParseException;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/** Console entry point for the Expense Tracker. */
public class Main {

    private static final Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        ExpenseService service = new ExpenseService(new CsvExpenseRepository(Path.of("data", "expenses.csv")));
        System.out.println("=== Expense Tracker ===");

        boolean running = true;
        while (running) {
            printMenu();
            switch (in.nextLine().trim()) {
                case "1" -> addExpense(service);
                case "2" -> printList(service.listAll());
                case "3" -> deleteExpense(service);
                case "4" -> searchExpenses(service);
                case "5" -> printSummary(service);
                case "0" -> running = false;
                default -> System.out.println("Invalid choice, try again.");
            }
        }
        System.out.println("Goodbye!");
    }

    private static void printMenu() {
        System.out.println("""

                1. Add expense
                2. View all expenses
                3. Delete expense
                4. Search expenses
                5. Summary
                0. Exit""");
        System.out.print("Choose: ");
    }

    private static void addExpense(ExpenseService service) {
        try {
            System.out.print("Date (yyyy-MM-dd, blank = today): ");
            String d = in.nextLine().trim();
            LocalDate date = d.isEmpty() ? LocalDate.now() : LocalDate.parse(d);
            System.out.print("Category (e.g. Food, Travel): ");
            String category = in.nextLine();
            System.out.print("Description: ");
            String desc = in.nextLine();
            System.out.print("Amount: ");
            BigDecimal amount = new BigDecimal(in.nextLine().trim());
            Expense e = service.add(date, category, desc, amount);
            System.out.println("Added: " + e);
        } catch (DateTimeParseException ex) {
            System.out.println("Invalid date format. Use yyyy-MM-dd.");
        } catch (NumberFormatException ex) {
            System.out.println("Invalid amount.");
        } catch (IllegalArgumentException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }

    private static void deleteExpense(ExpenseService service) {
        System.out.print("Expense ID to delete: ");
        try {
            int id = Integer.parseInt(in.nextLine().trim());
            System.out.println(service.delete(id) ? "Deleted." : "No expense with that ID.");
        } catch (NumberFormatException ex) {
            System.out.println("Invalid ID.");
        }
    }

    private static void searchExpenses(ExpenseService service) {
        System.out.print("Keyword: ");
        printList(service.search(in.nextLine().trim()));
    }

    private static void printList(List<Expense> list) {
        if (list.isEmpty()) {
            System.out.println("No expenses found.");
            return;
        }
        System.out.printf("%-4s %-12s %-14s %-25s %10s%n", "ID", "Date", "Category", "Description", "Amount");
        System.out.println("-".repeat(70));
        list.forEach(System.out::println);
    }

    private static void printSummary(ExpenseService service) {
        System.out.println("\n--- Summary ---");
        System.out.printf("Total spent:        %10.2f%n", service.total());
        System.out.printf("This month:         %10.2f%n", service.totalForMonth(YearMonth.now()));
        System.out.println("By category:");
        for (Map.Entry<String, BigDecimal> en : service.totalsByCategory().entrySet()) {
            System.out.printf("  %-18s %10.2f%n", en.getKey(), en.getValue());
        }
    }
}
