print("===== CURRENCY DENOMINATION CALCULATOR =====")

amount = int(input("Enter amount in rupees: "))

if amount <= 0:
    print("Please enter a positive amount.")

else:
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    print("\nCurrency breakdown:")

    remaining = amount

    for note in denominations:
        count = remaining // note
        remaining = remaining % note

        if count > 0:
            print(f"₹{note} x {count}")

    print("\nTotal amount: ₹", amount)
```
