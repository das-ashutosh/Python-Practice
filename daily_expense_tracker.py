expenses = []

while True:
    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        print("\nYour Expenses:")

        for expense in expenses:
            print(expense["name"], "-", expense["amount"])

    elif choice == "3":
        total = sum(item["amount"] for item in expenses)
        print("Total Spending: ₹", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
