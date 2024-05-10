import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        messagebox.showinfo("Expense Tracker", "Expense added successfully.")

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        return total

    def show_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Expense Tracker", "No expenses to show.")
            return
        expenses_text = "Expenses:\n"
        for expense in self.expenses:
            expenses_text += f"Category: {expense['category']}, Amount: {expense['amount']}\n"
        messagebox.showinfo("Expense Tracker", expenses_text)

def add_expense_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Expense")

    tk.Label(add_window, text="Category:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(add_window, text="Amount:").grid(row=1, column=0, padx=5, pady=5)

    category_entry = tk.Entry(add_window)
    category_entry.grid(row=0, column=1, padx=5, pady=5)
    amount_entry = tk.Entry(add_window)
    amount_entry.grid(row=1, column=1, padx=5, pady=5)

    def add():
        category = category_entry.get()
        amount = float(amount_entry.get())
        expense_tracker.add_expense(category, amount)
        add_window.destroy()

    tk.Button(add_window, text="Add", command=add).grid(row=2, column=0, columnspan=2, pady=10)

def main():
    global root
    global expense_tracker
    root = tk.Tk()
    root.title("Expense Tracker")

    expense_tracker = ExpenseTracker()

    tk.Button(root, text="Add Expense", command=add_expense_window).pack(pady=10)
    tk.Button(root, text="Show Expenses", command=expense_tracker.show_expenses).pack(pady=10)
    tk.Button(root, text="Total Expenses", command=lambda: messagebox.showinfo("Expense Tracker", f"Total expenses: {expense_tracker.total_expenses()}")).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
