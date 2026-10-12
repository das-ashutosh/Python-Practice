import csv
from datetime import date
from pathlib import Path

FILE_NAME = "attendance.csv"

file_exists = Path(FILE_NAME).exists()

with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["Date", "Student Name", "Status"])

    print("=== Student Attendance Tracker ===")

    while True:
        name = input("\nEnter student name (or 'done'): ").strip()

        if name.lower() == "done":
            break

        if not name:
            print("Name cannot be empty.")
            continue

        status = input("Present or Absent? ").strip().title()

        if status not in ["Present", "Absent"]:
            print("Please enter Present or Absent.")
            continue

        writer.writerow([date.today(), name, status])
        print("Attendance recorded!")

print("\nAttendance saved to", FILE_NAME)
