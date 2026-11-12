package com.expensetracker.storage;

import com.expensetracker.model.Expense;

import java.io.IOException;
import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/** Saves and loads expenses from a simple CSV file. */
public class CsvExpenseRepository {

    private static final String HEADER = "id,date,category,description,amount";
    private final Path file;

    public CsvExpenseRepository(Path file) {
        this.file = file;
    }

    public List<Expense> load() {
        List<Expense> list = new ArrayList<>();
        if (!Files.exists(file)) return list;
        try {
            List<String> lines = Files.readAllLines(file);
            for (int i = 1; i < lines.size(); i++) { // skip header
                String line = lines.get(i).trim();
                if (line.isEmpty()) continue;
                List<String> f = parseLine(line);
                list.add(new Expense(Integer.parseInt(f.get(0)), LocalDate.parse(f.get(1)),
                        f.get(2), f.get(3), new BigDecimal(f.get(4))));
            }
        } catch (IOException | RuntimeException e) {
            throw new IllegalStateException("Could not read " + file + ": " + e.getMessage(), e);
        }
        return list;
    }

    public void save(List<Expense> expenses) {
        List<String> lines = new ArrayList<>();
        lines.add(HEADER);
        for (Expense e : expenses) {
            lines.add(e.id() + "," + e.date() + "," + escape(e.category()) + ","
                    + escape(e.description()) + "," + e.amount().toPlainString());
        }
        try {
            if (file.getParent() != null) Files.createDirectories(file.getParent());
            Files.write(file, lines);
        } catch (IOException e) {
            throw new IllegalStateException("Could not write " + file + ": " + e.getMessage(), e);
        }
    }

    private static String escape(String s) {
        if (s.contains(",") || s.contains("\"")) {
            return "\"" + s.replace("\"", "\"\"") + "\"";
        }
        return s;
    }

    private static List<String> parseLine(String line) {
        List<String> out = new ArrayList<>();
        StringBuilder cur = new StringBuilder();
        boolean inQuotes = false;
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (inQuotes) {
                if (c == '"' && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                    cur.append('"');
                    i++;
                } else if (c == '"') {
                    inQuotes = false;
                } else {
                    cur.append(c);
                }
            } else if (c == '"') {
                inQuotes = true;
            } else if (c == ',') {
                out.add(cur.toString());
                cur.setLength(0);
            } else {
                cur.append(c);
            }
        }
        out.add(cur.toString());
        return out;
    }
}
