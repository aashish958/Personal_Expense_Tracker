from storage import save_expense

def add_expense():

    print("\n--- Add New Expense ---")

    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

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