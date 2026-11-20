# Personal Expense Tracker

A Python-based command-line application that helps users manage their daily expenses, store expense records in a CSV file, and analyze spending through different features.

## 1. Project Overview

The **Personal Expense Tracker** is a console-based application developed using Python. It allows users to record, view, search, calculate, and manage their expenses.

The application uses CSV file handling to store expense records permanently. It also includes a data validation feature to identify missing or incorrect information in the CSV file.

## 2. Project Objectives

- Develop a simple expense management application using Python.
- Store expense records in a CSV file.
- Allow users to view and search their expenses.
- Calculate total expenses and monthly spending.
- Provide functionality to delete expense records.
- Validate CSV data and identify incorrect records.
- Apply Python concepts such as functions, modules, exception handling, and file handling.

## 3. Features

The application provides the following features:

1. **Add Expense:** Add a new expense with title, amount, category, and date.
2. **View All Expenses:** Display all saved expense records.
3. **Search Expense:** Search expenses using their category.
4. **Calculate Total Expense:** Calculate the total amount of recorded expenses.
5. **Monthly Summary:** View expense details for a particular month.
6. **Delete Expense:** Remove an expense record from the CSV file.
7. **Validate Expense Data:** Check the CSV file for missing fields, invalid values, incorrect dates, and unexpected extra values.
8. **Exit:** Close the application.

## 4. Technologies Used

- **Programming Language:** Python
- **Code Editor:** Visual Studio Code
- **Data Storage:** CSV (Comma-Separated Values)
- **Version Control:** Git
- **Repository Hosting:** GitHub

### Python Modules

- `csv` – For reading and writing CSV files.
- `pathlib` – For handling file paths.
- `datetime` – For validating dates and generating monthly summaries.

## 5. Project Structure

```text
Personal_Expense_Tracker/
│
├── main.py
├── expense.py
├── storage.py
├── expenses.csv
├── test_expenses.csv
├── README.md
└── .gitignore
```

**File Description:**

- `main.py` – Contains the main menu and controls the application flow.
- `expense.py` – Handles the process of adding new expenses.
- `storage.py` – Contains functions for saving, viewing, searching, deleting, calculating, and validating expense records.
- `expenses.csv` – Stores actual expense records locally.
- `test_expenses.csv` – Contains sample records used for testing.
- `README.md` – Provides project documentation.
- `.gitignore` – Prevents unnecessary and private files from being committed to GitHub.

## 6. CSV Data Format

Expense records are stored in CSV format with the following columns:

| Column | Description |
|---|---|
| title | Name or description of the expense |
| amount | Expense amount |
| category | Expense category |
| date | Date of the expense |

**Example:**

```csv
title,amount,category,date
Groceries,1200,Food,2026-11-10
Electricity Bill,850,Bills,2026-11-12
Shopping,1500,Personal,2026-11-15
```

**Date Formats:**
- Expense date: `YYYY-MM-DD`
- Monthly summary input: `YYYY-MM`

## 7. Installation and Setup

### Prerequisites

- Python 3 installed on your system.
- Visual Studio Code or any Python-supported code editor.
- Git (optional, for version control).

### Step 1: Clone the Repository

```bash
git clone https://github.com/aashish958/Personal_Expense_Tracker.git
```

### Step 2: Open the Project Folder

```bash
cd Personal_Expense_Tracker
```

### Step 3: Run the Application

```bash
python main.py
```

## 8. Application Menu

When the application starts, the following menu is displayed:

```text
============================================
     Personal_Expense_Tracker
============================================

---------------------------
1. Add Expense
2. View All Expense
3. Search Expense
4. Calculate Total Expense
5. Monthly Summary
6. Delete Expense
7. Validate Expense Data
8. Exit
---------------------------
```

Users can select an option by entering the corresponding number.

## 9. Data Validation

The application includes a CSV data validation feature to identify incorrect or incomplete expense records.

The validation process checks:

- Missing required CSV columns.
- Missing expense title.
- Missing amount.
- Missing category.
- Missing date.
- Invalid date format.
- Non-numeric expense amounts.
- Zero or negative expense amounts.
- Unexpected extra column values.

The application displays validation errors with their corresponding record numbers and provides a summary of the total issues found.

## 10. Error Handling

Exception handling is used to make the application more reliable.

The application handles relevant errors such as:

- File not found.
- Permission denied.
- Invalid input values.
- Incorrect date formats.
- File-related operating system errors.

## 11. Testing

The application has been tested using normal expense records as well as sample records containing invalid data.

Testing includes:

- Adding and saving expenses.
- Viewing saved expense records.
- Searching expenses by category.
- Calculating total expenses.
- Generating monthly summaries.
- Deleting expense records.
- Checking missing and invalid CSV values.
- Checking incorrect CSV headers and unexpected extra values.

A separate `test_expenses.csv` file is used for testing validation scenarios without modifying the actual expense data.

## 12. Future Enhancements

The following features can be added in future versions:

- Graphical User Interface (GUI).
- Expense visualization using charts.
- Category-wise expense reports.
- Budget management and alerts.
- Export reports to Excel or PDF.
- Database integration using SQLite or MySQL.
- User login and authentication.

## 13. Author

**Name:** Aashish Choudhary
**Project:** Personal Expense Tracker
**Programming Language:** Python
**Repository:** [GitHub – Personal Expense Tracker](https://github.com/aashish958/Personal_Expense_Tracker)

---

*Developed as a Python project to practice programming fundamentals, file handling, modular development, data validation, and Git version control.*