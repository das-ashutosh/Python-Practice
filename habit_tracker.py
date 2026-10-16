```python
# Personal Habit Tracker

habits = {}

print("===== PERSONAL HABIT TRACKER =====")

while True:
    print("\n1. Add a habit")
    print("2. View habits")
    print("3. Mark a habit as completed")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        habit = input("Enter habit name: ").strip()

        if habit:
            if habit in habits:
                print("This habit already exists!")
            else:
                habits[habit] = False
                print("Habit added successfully!")
        else:
            print("Habit name cannot be empty.")

    elif choice == "2":
        if not habits:
            print("No habits added yet.")
        else:
            print("\nYour Habits:")
            for habit, completed in habits.items():
                status = "Completed" if completed else "Pending"
                print(f"- {habit}: {status}")

    elif choice == "3":
        habit = input("Enter habit to complete: ").strip()

        if habit in habits:
            habits[habit] = True
            print(f"Great! '{habit}' completed!")
        else:
            print("Habit not found.")

    elif choice == "4":
        print("Keep building good habits. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
```
