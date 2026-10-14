from datetime import date

print("=== Study Progress Report ===")

student = input("Enter student name: ").strip()
subjects = {}

while True:
    subject = input(
        "\nEnter subject name (or 'done' to finish): "
    ).strip()

    if subject.lower() == "done":
        break

    if not subject:
        print("Subject name cannot be empty.")
        continue

    if subject in subjects:
        print("Subject already entered.")
        continue

    try:
        marks = float(input("Enter marks out of 100: "))

        if 0 <= marks <= 100:
            subjects[subject] = marks
        else:
            print("Marks must be between 0 and 100.")

    except ValueError:
        print("Please enter a valid number.")

if subjects:
    total = sum(subjects.values())
    percentage = total / len(subjects)

    print("\n========== REPORT ==========")
    print("Student:", student)
    print("Date:", date.today())
    print("----------------------------")

    for subject, marks in subjects.items():
        print(f"{subject}: {marks:g}/100")

    print("----------------------------")
    print(f"Total marks: {total:g}/{len(subjects) * 100}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 90:
        print("Grade: Excellent")
    elif percentage >= 75:
        print("Grade: Very Good")
    elif percentage >= 60:
        print("Grade: Good")
    elif percentage >= 40:
        print("Grade: Pass")
    else:
        print("Grade: Needs Improvement")
else:
    print("No subject marks entered.")
