# Tracker

# Personal Expense Tracker

A Python-based command-line application that helps users record, manage, search, and track their daily expenses using CSV file storage.

## Features

- **Add Expense:** Record expenses with title, amount, category, and date.
- **View Expenses:** Display all recorded expenses.
- **Search Expenses:** Find expenses by category.
- **Calculate Total Expense:** Calculate the total amount spent across all recorded expenses.
- **Monthly Summary:** Planned feature.
- **Delete Expense:** Planned feature.

## Technologies Used

- Python
- CSV (Comma-Separated Values)
- Python `csv` module
- `pathlib` module
- Git and GitHub

## Project Structure

```text
Personal_Expense_Tracker/
│
├── main.py
├── expense.py
├── storage.py
├── expenses.csv
├── README.md
└── .gitignore
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/aashish958/Personal_Expense_Tracker.git
   ```

2. Open the project folder:

   ```bash
   cd Personal_Expense_Tracker
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Data Storage

Expense records are stored locally in `expenses.csv`.

The CSV file is excluded from Git tracking to protect personal financial information.

## Future Improvements

- Monthly expense summaries
- Delete expense functionality
- Input validation and error handling
- Expense visualization and reporting

## Author

**Aashish Chaudhary**

GitHub: [aashish958]
GitHub URL: (https://github.com/aashish958)