```python
# Student Study Planner

tasks = []

print("===== STUDENT STUDY PLANNER =====")

while True:
    print("\n1. Add a study task")
    print("2. View study tasks")
    print("3. Remove a study task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your study task: ").strip()

        if task:
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No study tasks yet.")
        else:
            print("\nYour Study Tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        if not tasks:
            print("There are no tasks to remove.")
            continue

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

        try:
            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Good luck with your studies!")
        break

    else:
        print("Invalid option. Choose 1, 2, 3, or 4.")
```
