# Expenses.py
# This file will handle the business logic for the Expenses application.

# Placeholder for business logic functions
def calculate_total_expenses(expenses):
    """Calculate the total expenses from a list of expense amounts."""
    return sum(expenses)

def add_expense(expenses, amount):
    """Add a new expense to the list."""
    expenses.append(amount)
    return expenses

if __name__ == "__main__":
    # Example usage
    expenses = []
    add_expense(expenses, 100)
    add_expense(expenses, 200)
    print("Total Expenses:", calculate_total_expenses(expenses))