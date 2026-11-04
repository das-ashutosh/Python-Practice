import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

FILE_NAME = "students.csv"
students = []
selected_reg = None


# Load student records
def load_students():
    global students

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)


# Save student records
def save_students():
    with open(FILE_NAME, "w", newline="") as file:
        fields = ["reg", "name", "department", "year", "marks"]
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(students)


# Refresh student table
def refresh_table(search=""):
    for item in table.get_children():
        table.delete(item)

    for student in students:
        text = " ".join(student.values()).lower()

        if search.lower() in text:
            table.insert(
                "",
                tk.END,
                values=(
                    student["reg"],
                    student["name"],
                    student["department"],
                    student["year"],
                    student["marks"]
                )
            )

    update_statistics()


# Update statistics
def update_statistics():
    total = len(students)

    if total > 0:
        average = sum(
            float(s["marks"]) for s in students
        ) / total
    else:
        average = 0

    stats_label.config(
        text=f"Total Students: {total}   |   Average Marks: {average:.2f}"
    )


# Clear input fields
def clear_fields():
    global selected_reg
    selected_reg = None

    reg_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

    table.selection_remove(table.selection())


# Validate input
def get_student_data():
    reg = reg_entry.get().strip()
    name = name_entry.get().strip()
    department = dept_entry.get().strip()
    year = year_entry.get().strip()
    marks = marks_entry.get().strip()

    if not all([reg, name, department, year, marks]):
        messagebox.showwarning("Warning", "Fill all fields!")
        return None

    try:
        year = int(year)
        marks = float(marks)

        if year < 1 or year > 8:
            raise ValueError

        if marks < 0 or marks > 100:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Year must be 1-8 and marks must be 0-100."
        )
        return None

    return {
        "reg": reg,
        "name": name,
        "department": department,
        "year": str(year),
        "marks": str(marks)
    }


# Add student
def add_student():
    data = get_student_data()

    if data is None:
        return

    if any(s["reg"] == data["reg"] for s in students):
        messagebox.showerror(
            "Error", "Registration number already exists!"
        )
        return

    students.append(data)
    save_students()
    refresh_table()
    clear_fields()

    messagebox.showinfo("Success", "Student added successfully!")


# Select student from table
def select_student(event):
    global selected_reg

    selected = table.selection()

    if not selected:
        return

    values = table.item(selected[0], "values")
    selected_reg = values[0]

    clear_form_only()

    reg_entry.insert(0, values[0])
    name_entry.insert(0, values[1])
    dept_entry.insert(0, values[2])
    year_entry.insert(0, values[3])
    marks_entry.insert(0, values[4])


def clear_form_only():
    for entry in (
        reg_entry, name_entry, dept_entry,
        year_entry, marks_entry
    ):
        entry.delete(0, tk.END)


# Update student
def update_student():
    global selected_reg

    if selected_reg is None:
        messagebox.showwarning(
            "Warning", "Select a student from the table first!"
        )
        return

    data = get_student_data()

    if data is None:
        return

    for student in students:
        if student["reg"] == data["reg"] and student["reg"] != selected_reg:
            messagebox.showerror(
                "Error", "Registration number already exists!"
            )
            return

    for student in students:
        if student["reg"] == selected_reg:
            student.update(data)
            break

    save_students()
    refresh_table()
    clear_fields()

    messagebox.showinfo("Success", "Student updated successfully!")


# Delete student
def delete_student():
    global selected_reg

    if selected_reg is None:
        messagebox.showwarning(
            "Warning", "Select a student to delete!"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )

    if confirm:
        students[:] = [
            s for s in students if s["reg"] != selected_reg
        ]

        save_students()
        refresh_table()
        clear_fields()

        messagebox.showinfo("Success", "Student deleted!")


# Search student
def search_student():
    query = search_entry.get().strip()
    refresh_table(query)


# Reset search
def show_all():
    search_entry.delete(0, tk.END)
    refresh_table()


# Main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("950x650")
root.configure(bg="#eef2f7")

# Heading
heading = tk.Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#eef2f7",
    fg="#17365d"
)
heading.pack(pady=15)

# Input frame
form = tk.LabelFrame(
    root,
    text="Student Details",
    font=("Arial", 12, "bold"),
    bg="white",
    padx=15,
    pady=15
)
form.pack(fill="x", padx=20)

# Input fields
tk.Label(form, text="Registration No.", bg="white").grid(
    row=0, column=0, padx=10, pady=8
)
reg_entry = tk.Entry(form, width=22)
reg_entry.grid(row=0, column=1)

tk.Label(form, text="Student Name", bg="white").grid(
    row=0, column=2, padx=10
)
name_entry = tk.Entry(form, width=22)
name_entry.grid(row=0, column=3)

tk.Label(form, text="Department", bg="white").grid(
    row=1, column=0, padx=10, pady=8
)
dept_entry = tk.Entry(form, width=22)
dept_entry.grid(row=1, column=1)

tk.Label(form, text="Year", bg="white").grid(
    row=1, column=2, padx=10
)
year_entry = tk.Entry(form, width=22)
year_entry.grid(row=1, column=3)

tk.Label(form, text="Marks", bg="white").grid(
    row=2, column=0, padx=10, pady=8
)
marks_entry = tk.Entry(form, width=22)
marks_entry.grid(row=2, column=1)

# Buttons
buttons = tk.Frame(root, bg="#eef2f7")
buttons.pack(pady=12)

tk.Button(
    buttons, text="Add Student", width=14,
    bg="#198754", fg="white", command=add_student
).grid(row=0, column=0, padx=5)

tk.Button(
    buttons, text="Update", width=14,
    bg="#0d6efd", fg="white", command=update_student
).grid(row=0, column=1, padx=5)

tk.Button(
    buttons, text="Delete", width=14,
    bg="#dc3545", fg="white", command=delete_student
).grid(row=0, column=2, padx=5)

tk.Button(
    buttons, text="Clear", width=14,
    command=clear_fields
).grid(row=0, column=3, padx=5)

# Search frame
search_frame = tk.Frame(root, bg="#eef2f7")
search_frame.pack(pady=8)

tk.Label(
    search_frame,
    text="Search Student:",
    bg="#eef2f7",
    font=("Arial", 11)
).pack(side="left", padx=5)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=5)

tk.Button(
    search_frame, text="Search",
    command=search_student
).pack(side="left", padx=5)

tk.Button(
    search_frame, text="Show All",
    command=show_all
).pack(side="left", padx=5)

# Student table
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("reg", "name", "department", "year", "marks")

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

table.heading("reg", text="Registration No.")
table.heading("name", text="Student Name")
table.heading("department", text="Department")
table.heading("year", text="Year")
table.heading("marks", text="Marks")

table.column("reg", width=150)
table.column("name", width=200)
table.column("department", width=180)
table.column("year", width=100)
table.column("marks", width=100)

table.pack(fill="both", expand=True)
table.bind("<<TreeviewSelect>>", select_student)

# Statistics
stats_label = tk.Label(
    root,
    text="Total Students: 0 | Average Marks: 0.00",
    font=("Arial", 12, "bold"),
    bg="#eef2f7",
    fg="#17365d"
)
stats_label.pack(pady=10)

# Load saved records
load_students()
refresh_table()

root.mainloop()
