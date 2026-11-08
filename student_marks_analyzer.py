students = {
    "Rahul": 85,
    "Amit": 72,
    "Priya": 95,
    "Rohan": 68,
    "Sneha": 90
}

print("===== STUDENT MARKS ANALYZER =====")

for name, marks in students.items():
    print(name, ":", marks)

total = sum(students.values())
average = total / len(students)

topper = max(students, key=students.get)
lowest = min(students, key=students.get)

print("\nTotal Students:", len(students))
print("Average Marks:", average)
print("Highest Scorer:", topper, "-", students[topper])
print("Lowest Scorer:", lowest, "-", students[lowest])
