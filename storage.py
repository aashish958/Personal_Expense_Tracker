import csv
from pathlib import Path
from datetime import datetime

CSV_FILE = Path(__file__).resolve().parent / "expenses.csv"



def save_expense(expense):

    try:
        file_exists = CSV_FILE.exists()

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:

            fieldnames = ["title", "amount", "category", "date"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists or CSV_FILE.stat().st_size == 0:
                writer.writeheader()

            writer.writerow(expense)

        print("Expense saved successfully!")

        
    except FileNotFoundError:
        print("Error:Expense file or Directory not found.")
    except PermissionError:
        print("Error: Permission Denied! Cannot access the file.")
    except OSError as e:
        print(f"File operation failed{e}")

    


def view_expenses():

    try:
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

    except FileNotFoundError:
        print("Error:Expense file or Directory not found.")
    except PermissionError:
        print("Error: Permission Denied! cannot access the file.")
    except OSError as e:
        print(f"File operation failed:{e}")


def search_expense():

    print("Search function started")

    search_category = input("Enter the category: ").strip()

    try:
        if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
            print("No expenses found!")
            return

        found = False

        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for expense in reader:

                if expense["category"].lower() == search_category.lower():

                    print("\nTitle    :", expense["title"])
                    print("Amount   :", expense["amount"])
                    print("Category :", expense["category"])
                    print("Date     :", expense["date"])

                    found = True

        if not found:
            print("No expenses found in this category!")

    except FileNotFoundError:
        print("Error: Expense file or directory not found!")

    except PermissionError:
        print("Error: Permission denied! Cannot access the expense file.")

    except OSError as e:
        print(f"File operation failed: {e}")





def calculate_total_expense():
    total= 0
    try:
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

    except FileNotFoundError:
        print("Error:Expense file or Directory not found.")
    except PermissionError:
        print("Error:Permission Denied! cannot access the file")
    except ValueError:
        print("Error:Invalid amount found in the Expense file!")
    except KeyError as e:
        print(f"Error: Missing column in expense file:{e}")
    except OSError as e:
        print(f"file operation failed:{e}")


def monthly_summary():

    while True:
        month = input("Enter the Month(YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
            break

        except ValueError:
            print("Invalid month! Please enter in YYYY-MM format.")
            
    total = 0
    found = False

    try:
        if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
            print("No expense Found")
            return

        with open(CSV_FILE,"r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for expense in reader :

                if expense["date"][:7] == month:

                    print(expense["title"],expense["amount"])

                    total = total + float(expense["amount"])
                    found = True


        if not found:
            print("No expenses found in this month!")

        else:
            print("-----------------------")
            print(f"Total Monthly Expense: ₹{total:.2f}")

    except FileNotFoundError:
        print("Error: Expense File or Directory not found.")
    except PermissionError:
        print("Error: Permission Denied! Cannot access this file.")
    except ValueError:
        print("Error: Invalid amount found in the expense file!")
    except KeyError:
        print("Error: Missing Column in Expense file!")
    except OSError as e:
        print(f"File Operation failed:{e}")


   
def delete_expense():

    try:
        if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
            print("No expenses found!")
            return

        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)
            expenses = list(reader)

        if not expenses:
            print("No expenses Found!")
            return

        print("\n=========Select Expense to Delete============")

        for index ,  expense in enumerate(expenses, start= 1):


            print("----------------------------------")
            print("NO.     :", index)
            print("Title      :",expense["title"])
            print("Amount      :",expense["amount"])
            print("Category      :",expense["category"])
            print("Date      :",expense["date"])

        while True:

            try:

                choice = int(input("\n Enter the expense number to delete: "))

                if choice < 1 or choice >len(expenses):
                    print("Invalid selection!  Please enter valid expense number.")
                    continue

                break 
            except ValueError:
                print("Invalid number! Please enter a number.")

        selection_expense = expenses[choice - 1]


        print("\n========Selected Expense========")
        print("Title     :",selection_expense["title"])
        print("Amount     :",selection_expense["amount"])
        print("Category     :",selection_expense["category"])
        print("Date     :",selection_expense["date"])


        confirm = input("\n Are you sure you want to delete this expense?(y/n): ").strip().lower()

        if confirm == "y":
            delete_expense = expenses.pop(choice - 1)
            print("\nExpense removed from the list successfully!")
            print("Delete Expense:",delete_expense["title"])

            with open(CSV_FILE, "w", newline="", encoding="utf- 8 ") as file:

                fieldnames = ["title", "amount", "category", "date"]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()

                writer.writerows(expenses)

            print("Expense deleted successfully from CSV file!")

        elif confirm == "n":
            print("Deletion cancelled!")
            return

        else:
            print("Invalid confirmation!")
            return
        

    except FileNotFoundError:
        print("Error: Expense file or directory not found!")

    except PermissionError:
        print("Error: Permission denied! Cannot access the expense file.")

    except OSError as e:
        print(f"File operation failed: {e}")



def validate_expense_data():

    error_count = 0 

    try:
        if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
            print("No expense Found")
            return

        with open(CSV_FILE,"r", newline="", encoding="utf-8")as file:

            reader = csv.DictReader(file)

            required_fields = ["title", "amount", "category", "date"]

            if reader.fieldnames is None:
                print("Error: CSV file has no header row!")
                return

            missing_column = [
                column for column in required_fields
                if column not in reader.fieldnames
            ]

            if missing_column:
                print("CSV  is missing required columns: ", ",".join(missing_column))
                return


            for index, expense in enumerate(reader, start=1):

                if None in expense:
                    print(f"Record {index}: Extra unexpected column values!")
                    error_count += 1

                
                title = expense.get("title") or ""
                if not title.strip():
                    print(f"Record {index}: Title is missing!")
                    error_count += 1                    
                    
                category = expense.get("category") or ""
                if not category.strip():
                    print(f"Record {index}: Category is missing!")
                    error_count += 1

                amount = expense.get("amount") or ""

                if not amount.strip():
                    print(f"Record {index}: Amount is missing!")
                    error_count += 1

                date = expense.get("date") or ""

                if not date.strip():
                    print(f"Record {index}: Date is missing!")
                    error_count += 1
                    
                
                if date.strip():

                    try:
                        datetime.strptime(expense["date"], "%Y-%m-%d")

                    except ValueError:
                        print(f"Record {index}: Invalid date format!")
                        error_count += 1

                if amount.strip():

                    try:
                        amount = float(expense["amount"])

                        if amount <= 0:
                            print(f"Record {index}: Amount must be greater than zero!")
                            error_count+=1

                    except ValueError:
                        print(f"Record {index}: Invalid amount!")
                        error_count += 1

            print("\n=========== VALIDATION SUMMARY =============")
            
            if error_count == 0:
                print("All expense records are valid!")
            else:
                print(f"Total issues found: {error_count}")

    except FileNotFoundError:
        print("Error: Expense file not found!")

    except PermissionError:
        print("Error: Permission denied")

    except OSError as e:
        print(f"File operation Failed:{e}")


        