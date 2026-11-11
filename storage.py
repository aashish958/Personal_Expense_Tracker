import csv
from pathlib import Path

CSV_FILE = Path(__file__).resolve().parent / "expenses.csv"


def save_expense(expense):

    file_exists = CSV_FILE.exists()

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:

        fieldnames = ["title", "amount", "category", "date"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists or CSV_FILE.stat().st_size == 0:
            writer.writeheader()

        writer.writerow(expense)

    print("Expense saved successfully!")


def view_expenses():

    if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
        print("\nNo expenses found!")
        return

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        print("\n========== ALL EXPENSES ==========")

        for expense in reader:

            print("--------------------------------")
            print("Title    :", expense["title"])
            print("Amount   :", expense["amount"])
            print("Category :", expense["category"])
            print("Date     :", expense["date"])

        print("--------------------------------")


def search_expense():

    print("Search function started")

    search_category = input("Enter the category: ")

    if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
        print("No expenses found")
        return

    found = False

    with open(CSV_FILE,"r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)


        for expense in reader:


            if expense["category"].lower() == search_category.lower():


                print("\n Title     :",expense["title"])
                print("\n Amount     :",expense["amount"])
                print("\n Category     :",expense["category"])
                print("\n Date     :",expense["date"])

                found = True


    if not found:
        print("No expenses found in this category!")



def calculate_total_expense():
    total= 0
    if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
        print("No expenses found")
        return
    
    
    with open(CSV_FILE,"r", newline="", encoding="utf-8") as file:
    
        reader = csv.DictReader(file)
        
        for expense in reader:
            total = total + float(expense["amount"])


    print("===============================")
    print("      TOTAL EXPENSE")
    print("===============================")
                
    print(f"Total Expense: ₹{total:.2f}")
    


        