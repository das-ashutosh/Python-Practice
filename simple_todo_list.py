tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(i, task["task"], "-", status)

    elif choice == "3":
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print("Task completed!")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
