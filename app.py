import tkinter as tk
from tkinter import messagebox

expenses = []

def setup_window():
    root = tk.Tk()
    root.title("Expense Splitter")
    root.geometry("400x400")
    return root

def create_input_fields(root):
    tk.Label(root, text="Participant Name:").pack(pady=5)
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=5)

    tk.Label(root, text="Expense Description:").pack(pady=5)
    description_entry = tk.Entry(root, width=30)
    description_entry.pack(pady=5)

    tk.Label(root, text="Amount:").pack(pady=5)
    amount_entry = tk.Entry(root, width=30)
    amount_entry.pack(pady=5)

    return name_entry, description_entry, amount_entry

def create_buttons(root, name_entry, description_entry, amount_entry, expense_list):
    add_button = tk.Button(root, text="Add Expense", command=lambda: add_expense(name_entry, description_entry, amount_entry, expense_list))
    add_button.pack(pady=5)

    split_button = tk.Button(root, text="Split Expenses", command=lambda: split_expenses(expense_list))
    split_button.pack(pady=5)

def create_expense_list(root):
    expense_list = tk.Listbox(root, width=50, height=10)
    expense_list.pack(pady=10)
    return expense_list

def add_expense(name_entry, description_entry, amount_entry, expense_list):
    name = name_entry.get().strip()
    description = description_entry.get().strip()
    amount = amount_entry.get().strip()
    
    if name and description and amount:
        try:
            amount = float(amount)
            expenses.append((name, description, amount))
            expense_list.insert(tk.END, f"{name}: {description} - ${amount:.2f}")
            name_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid amount.")
    else:
        messagebox.showwarning("Warning", "All fields are required.")

def split_expenses(expense_list):
    if not expenses:
        messagebox.showwarning("Warning", "No expenses to split.")
        return
    
    total_amount = sum(expense[2] for expense in expenses)
    num_participants = len(set(expense[0] for expense in expenses))
    split_amount = total_amount / num_participants
    
    result_window = tk.Toplevel()
    result_window.title("Split Expenses")
    result_window.geometry("300x200")
    
    result_text = f"Total Amount: ${total_amount:.2f}\nNumber of Participants: {num_participants}\nEach Participant Owes: ${split_amount:.2f}"
    tk.Label(result_window, text=result_text, justify="left").pack(pady=10)
    
    for participant in set(expense[0] for expense in expenses):
        participant_expenses = sum(expense[2] for expense in expenses if expense[0] == participant)
        amount_owed = split_amount - participant_expenses
        tk.Label(result_window, text=f"{participant} owes: ${amount_owed:.2f}").pack(pady=2)

def main():
    root = setup_window()
    
    name_entry, description_entry, amount_entry = create_input_fields(root)
    expense_list = create_expense_list(root)
    create_buttons(root, name_entry, description_entry, amount_entry, expense_list)
    
    root.mainloop()

if __name__ == "__main__":
    main()
