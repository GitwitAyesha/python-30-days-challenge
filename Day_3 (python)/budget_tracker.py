def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, amount is: {amount}")

def get_total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    return total

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"{expense['description']}: {expense['amount']}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")

def main():
    print("Welcome to BudgetApp")
    
    # Convert budget input to float
    budget = float(input("Write your budget: "))
    expenses = []

    while True:
        print("\nWhat do you want to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount of the expense: "))
            add_expense(expenses, description, amount)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            print("Exiting BudgetApp. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
