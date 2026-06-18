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
        with open(filename, "w") as file:
            json.load(file)
            for dict in 



tracker = ExpenseTracker()
tracker.add_expense("Food", 250, "2026-06-18", "Lunch")
tracker.add_expense("Transport", 100, "2026-06-18", "Bus")


tracker.view_all_expenses()
tracker.save_to_file("expenses.json")