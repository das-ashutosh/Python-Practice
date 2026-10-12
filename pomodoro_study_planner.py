import time

study_minutes = 25
break_minutes = 5

print("=== Pomodoro Study Planner ===")

while True:
    choice = input(
        "\nStart a study session? (yes/no): "
    ).lower()

    if choice != "yes":
        print("Good luck with your studies!")
        break

    print("\n📚 Focus time! Avoid distractions.")

    for remaining in range(study_minutes * 60, 0, -1):
        if remaining % 60 == 0:
            print(f"{remaining // 60} minute(s) remaining")
        time.sleep(1)

    print("\n✅ Study session complete!")
    print(f"☕ Take a {break_minutes}-minute break.")

    for remaining in range(break_minutes * 60, 0, -1):
        if remaining % 60 == 0:
            print(f"{remaining // 60} minute(s) of break remaining")
        time.sleep(1)

    print("\nBreak finished. Ready to study again!")
