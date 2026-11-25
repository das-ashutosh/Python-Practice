queue = []

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value: ")
        queue.append(value)
        print("Value added")

    elif choice == "2":
        if queue:
            print("Removed:", queue.pop(0))
        else:
            print("Queue is empty")

    elif choice == "3":
        print("Queue:", queue)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
