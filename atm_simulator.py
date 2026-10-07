balance = 5000

print("🏦 Welcome to Simple ATM")

print("\n1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = input("\nEnter your choice: ")

if choice == "1":
    print("Your balance is ₹", balance)

elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("Deposit successful!")
    print("New balance: ₹", balance)

elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance: ₹", balance)
    else:
        print("Insufficient balance!")

else:
    print("Invalid choice!")
