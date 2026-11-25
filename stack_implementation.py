stack = []

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value: ")
        stack.append(value)
        print("Value pushed successfully")

    elif choice == "2":
        if stack:
            print("Removed:", stack.pop())
        else:
            print("Stack is empty")

    elif choice == "3":
        print("Stack:", stack)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
