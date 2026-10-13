print("=== Expense Splitter ===")
people = input(
    "Enter names separated by commas: "
).split(",")
people = [name.strip() for name in people if name.strip()]
if not people:
    print("Please enter at least one name.")
else:
    total_bill = float(input("Enter total bill amount (₹): "))
    tip_percent = float(input("Enter tip percentage: "))

    if total_bill < 0 or tip_percent < 0:
        print("Amounts and tip percentage cannot be negative.")
    else:
        tip = total_bill * tip_percent / 100
        final_bill = total_bill + tip
        share = final_bill / len(people)

        print("\n=== Bill Summary ===")
        print(f"Number of people: {len(people)}")
        print(f"Original bill: ₹{total_bill:.2f}")
        print(f"Tip: ₹{tip:.2f}")
        print(f"Total bill: ₹{final_bill:.2f}")
        print(f"Each person pays: ₹{share:.2f}")
        for person in people:
            print(f"{person}: ₹{share:.2f}")
