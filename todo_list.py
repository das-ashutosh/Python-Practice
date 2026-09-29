tasks = []
task1 = input("Enter your first task: ")
task2 = input("Enter your second task: ")
task3 = input("Enter your third task: ")
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)

print("\nYour To-Do List:")
for task in tasks:
    print("-", task)
