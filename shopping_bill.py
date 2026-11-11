items = {
    "Shirt": 500,
    "Jeans": 1200,
    "Shoes": 2000,
    "Watch": 800
}

print("===== SHOPPING BILL =====")

total = 0

for item, price in items.items():
    print(item, ":", "₹", price)
    total += price

if total >= 3000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("------------------------")
print("Total Amount: ₹", total)
print("Discount: ₹", discount)
print("Final Bill: ₹", final_amount)
