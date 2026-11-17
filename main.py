from expense import add_expense
from storage import (
    view_expenses,
    search_expense,
    calculate_total_expense,
    monthly_summary,
    delete_expense,
    validate_expense_data
)

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
    print("7. Validate Expense Data")
    print("8. Exit")
    print("---------------------------")

    
    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 8.")
        continue

    if choice == 1:
        add_expense()
    
    elif choice == 2:
        view_expenses()
    
    elif choice == 3:
        print("Step 1: Search option selected")
        search_expense()
        print("Step 2: Search function completed")

    elif choice == 4:
        calculate_total_expense()

    elif choice== 5:
        monthly_summary()

    elif choice == 6:
        delete_expense()

    elif choice== 7:
        validate_expense_data()

    elif choice == 8:
        print("Thank you!!")
        break
    