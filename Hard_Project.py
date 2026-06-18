import json
class Expense:
    def __init__(self, category, amount, date, note):
        self.category = category
        self.amount = amount
        self.date = date
        self.note = note

    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
            "note": self.note
        }

    def __str__(self):
        return f"Category: {self.category}, Amount: {self.amount}, Date: {self.date}, Note: {self.note}"

    

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, date, note):
        new_expense = Expense(category, amount, date, note)
        self.expenses.append(new_expense)
    def view_all_expenses(self):
        for exp in self.expenses:
            print(exp)
    def view_all_Expenses(self):
        for index, exp in enumerate(self.expenses, start=1):
            print(f"{index}. {exp}")
    
    def save_to_file(self, filename):
        expense_list = []
        for exp in self.expenses:
            expense_list.append(exp.to_dict())
        with open(filename, "w") as file:
            json.dump(expense_list, file)
        print(f"saved to {filename}")

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            for d in data:
                self.add_expense(d["category"], d["amount"], d["date"], d["note"]) 
    def view_by_category(self, category):
        for exp in self.expenses:
            if exp.category == category:
                print(exp)
    def total_by_category(self):
        totals = {}
        for exp in self.expenses:
            if exp.category in totals:
                totals[exp.category] += exp.amount
            else:
                totals[exp.category] = exp.amount
        return totals
    def delete_expense(self, index):
        if index > 0 and index <= len(self.expenses):
            del self.expenses[index - 1]
            print("Expense deleted successfully.")
        else:
            print("Invalid expense index.")
    def monthly_summary(self, month):
        matching_expenses = []
        for exp in self.expenses:
            if exp.date.startswith(month):
                matching_expenses.append(exp)
        total = 0

        for exp in matching_expenses:
            total = total + exp.amount
        print(f"Total spent: {total}")  

        biggest = max(matching_expenses, key=lambda exp: exp.amount)
        print(f"Biggest expense: {biggest}")

        unique_days = set()
        for exp in matching_expenses:
            unique_days.add(exp.date)
            average_daily = total / len(unique_days)
            print(f"Average daily expense: {average_daily}")
    
def main():
    tracker = ExpenseTracker()
    tracker.load_from_file("expenses.json")
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View by category")
        print("4. Total by category")
        print("5. Monthly summary")
        print("6. Delete expense")
        print("7. Save and Exit")
        
        choice = input("\nEnter choice (1-7): ")
        
        if choice == "1":
            category = input("Enter category (Food/Transport/Rent/Entertainment/Other): ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            note = input("Enter note: ")
            tracker.add_expense(category, amount, date, note)
            print("Expense added successfully.")
        
        elif choice == "2":
            tracker.view_all_Expenses()
        
        elif choice == "3":
            category = input("Enter category to filter by: ")
            tracker.view_by_category(category)
        
        elif choice == "4":
            print(tracker.total_by_category())
        
        elif choice == "5":
            month = input("Enter month (YYYY-MM): ")
            tracker.monthly_summary(month)
        
        elif choice == "6":
            tracker.view_all_Expenses()
            index = int(input("Enter expense number to delete: "))
            tracker.delete_expense(index)
        
        elif choice == "7":
            tracker.save_to_file("expenses.json")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


