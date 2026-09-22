units = float(input("Enter units consumed: "))

if units <= 50:
    bill = units * 2
elif units <= 100:
    bill = (50 * 2) + ((units - 50) * 3)
else:
    bill = (50 * 2) + (50 * 3) + ((units - 100) * 5)

print("Electricity bill: ₹", bill)
