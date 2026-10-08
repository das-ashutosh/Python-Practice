cart = []
print("🛒 Simple Shopping Cart")
while True:
    item = input("\nEnter an item (or type 'done'): ")
    if item.lower() == "done":
        break
    cart.append(item)
    print(item, "added to cart!")
print("\n=== Your Shopping Cart ===")
for i, item in enumerate(cart, start=1):
    print(i, ".", item)
print("\nTotal items:", len(cart))
