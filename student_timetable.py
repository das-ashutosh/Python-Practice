```python
# Student Timetable Generator

timetable = {
    "Monday": ["Mathematics", "Physics", "Programming"],
    "Tuesday": ["Chemistry", "English", "Programming"],
    "Wednesday": ["Physics", "Mathematics", "Lab"],
    "Thursday": ["Programming", "Chemistry", "English"],
    "Friday": ["Mathematics", "Physics", "Lab"],
    "Saturday": ["Revision", "Project Work"]
}

print("===== STUDENT TIMETABLE =====")

for day, subjects in timetable.items():
    print(f"\n{day}:")
    for period, subject in enumerate(subjects, start=1):
        print(f"  Period {period}: {subject}")

day = input("\nEnter a day to check your classes: ").strip().title()

if day in timetable:
    print(f"\nYour classes on {day}:")
    for subject in timetable[day]:
        print(f"- {subject}")
else:
    print("Invalid day. Please enter a valid weekday.")
```
