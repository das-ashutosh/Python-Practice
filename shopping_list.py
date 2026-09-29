items = []
item1 = input("Enter item 1: ")
item2 = input("Enter item 2: ")
item3 = input("Enter item 3: ")
items.append(item1)
items.append(item2)
items.append(item3)

print("\nShopping List:")
for item in items:
    print("-", item)
