from expense import add_expense
from storage import view_expenses, search_expense, calculate_total_expense

while True:

    print("============================================")
    print("     Personal_Expense_Tracker")
    print("============================================\n")

    print("---------------------------")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. Search Expense")
    print("4. Calculate Total Expense")
    print("5. Monthly Summary")
    print("6. Delete Expense")
    print("7. Exit")
    print("---------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    
    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        print("Step 1: Search option selected")
        search_expense()
        print("Step 2: Search function completed")

    elif choice == "4":
        calculate_total_expense()

    elif choice== "5":
        print("Monthly Summary")

    elif choice == "6":
        print("Delete Expense")

    elif choice== "7":
        print("Thank you!!")
        break
    else:
        print("Invalid choice!!")