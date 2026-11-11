from storage import save_expense
from datetime import datetime   
def add_expense():

    print("\n--- Add New Expense ---")


    while True:
        title = input("Enter expense title: ").strip()

        if title:
            break

        print("Title cannot be empty! Please Enter a Title.")

    while True:
        try:
            amount = float(input("Enter the Amount: "))

            if amount <=0:
                print("Amount must be greater than zero.")
                continue
            break

        except ValueError:
            print("Invalid amount! Please Enter the Valid amount.")


    while True:
        category = input("Enter expense category: ").strip()
        
        if category:
            break
        
        print("Category cannot be empty! Please Enter a category.")
    while True:
        date = input("Enter the date(YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date ! Please Enter the Date in YYYY-MM-DD format.")
            
    
    expense = {
            "title": title,
            "amount": amount,
            "category": category,
            "date": date
        }
    
    # Save expense in CSV file
    save_expense(expense)
    
    print("\nExpense added successfully!")
    print(expense)