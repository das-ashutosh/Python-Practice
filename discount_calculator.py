price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (price * discount) / 100
final_price = price - discount_amount
print("Discount amount:", discount_amount)
print("Final price:", final_price)
