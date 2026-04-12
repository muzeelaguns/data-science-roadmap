def main():
    print("Welcome to the Budget Planner!")
    monthly_income = float(input("Enter your monthly income: "))
    expense_list = []
    while True:
        expense_name = input("Enter an expense name (or 'done' to finish): ")
        if expense_name.lower() == "done":
            break
        else:
            expense_amount = float(input(f"Amount: "))
            expense_list.append(expense_amount)
    total_expenditure = sum(expense_list)
    for expense_amount in expense_list:
        percentage = (expense_amount / monthly_income) * 100
        print(f"{expense_name}: ${expense_amount} ({percentage:.2f}%)")

    balance = monthly_income - total_expenditure
    print(f'''Your total income : ${monthly_income} \n 
              total expenditure: ${total_expenditure} \n
              remaining balance: ${balance}''')


main()
