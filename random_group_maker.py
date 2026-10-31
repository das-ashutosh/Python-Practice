import random

print("===== RANDOM GROUP MAKER =====")

names = input(
    "Enter student names separated by commas: "
).split(",")

students = [name.strip() for name in names if name.strip()]

try:
    group_size = int(input("Enter students per group: "))

    if not students:
        print("No student names entered.")

    elif group_size <= 0:
        print("Group size must be greater than zero.")

    else:
        random.shuffle(students)

        groups = [
            students[i:i + group_size]
            for i in range(0, len(students), group_size)
        ]

        print("\n===== GENERATED GROUPS =====")

        for number, group in enumerate(groups, start=1):
            print(f"\nGroup {number}:")
            for student in group:
                print("-", student)

        print("\nTotal students:", len(students))
        print("Total groups:", len(groups))

except ValueError:
    print("Please enter a valid group size.")
```
