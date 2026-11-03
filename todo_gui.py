import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x450")
root.configure(bg="#202124")
root.resizable(False, False)

# Add task
def add_task():
    task = entry.get().strip()

    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Delete selected task
def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showwarning(
            "Warning", "Select a task first!"
        )

# Clear all tasks
def clear_tasks():
    task_list.delete(0, tk.END)

# Heading
title = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="#202124",
    fg="white"
)
title.pack(pady=20)

# Task input
entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
entry.pack(pady=10)

# Add button
tk.Button(
    root,
    text="ADD TASK",
    command=add_task,
    bg="#34A853",
    fg="white",
    width=15
).pack(pady=5)

# Task list
task_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=32,
    height=10,
    bg="#303134",
    fg="white",
    selectbackground="#4285F4"
)
task_list.pack(pady=15)

# Delete button
tk.Button(
    root,
    text="DELETE SELECTED",
    command=delete_task,
    bg="#EA4335",
    fg="white",
    width=18
).pack(pady=5)

# Clear button
tk.Button(
    root,
    text="CLEAR ALL",
    command=clear_tasks,
    bg="#4285F4",
    fg="white",
    width=15
).pack(pady=5)

root.mainloop()
