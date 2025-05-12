# Get user input for income and fixed expenses
Total_income = float(input("How much do you MAKE monthly? "))
Fixed_expenses = float(input("How much do you SPEND monthly? "))


def get_variable_expenses():
    all_expenses = []
    while len(all_expenses) < 5:  # Limit to 5 expenses
        user_input = input("List a variable expense (or press Enter to finish): ")
        
        if user_input.strip():
            all_expenses.append(user_input.strip())
        
        if len(all_expenses) < 5:
            more = input("Do you want to add more variable expenses? (yes/no): ").strip().lower()
            if more != "yes":
                break
        else:
            print("You have reached the maximum of 5 variable expenses.")
            break

    return all_expenses

# Get all variable expenses
variable_expenses = get_variable_expenses()

# Show all expenses
print("\nYour Variable Expenses:")
for i, expense in enumerate(variable_expenses, start=1):
    print(f"{i}. {expense}")


