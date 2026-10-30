import random

print("===== CLASSROOM SEATING ARRANGEMENT =====")

students = input(
    "Enter student names separated by commas: "
).split(",")

students = [name.strip() for name in students if name.strip()]

try:
    columns = int(input("Enter number of columns: "))

    if not students or columns <= 0:
        print("Please enter valid student names and columns.")

    else:
        random.shuffle(students)

        print("\n===== SEATING PLAN =====")

        for index, student in enumerate(students):
            seat = index + 1
            row = index // columns + 1
            column = index % columns + 1

            print(
                f"Seat {seat}: {student} "
                f"(Row {row}, Column {column})"
            )

        print("\nTotal students:", len(students))
        print("Arrangement completed!")

except ValueError:
    print("Please enter a valid number of columns.")
```
