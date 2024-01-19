import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        today = datetime.date.today()
        expense = {
            "date": today,
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("\n==== Expenses ====")
            for expense in self.expenses:
                print(f"Date: {expense['date']} | Amount: {expense['amount']} | Category: {expense['category']} | Description: {expense['description']}")

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter a description: ")
            tracker.add_expense(amount, category, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")