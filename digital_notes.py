import tkinter as tk
from tkinter import messagebox

def save_note():
    note = text_area.get("1.0", tk.END).strip()

    if note:
        with open("my_notes.txt", "a") as file:
            file.write(note + "\n\n")

        messagebox.showinfo("Success", "Note saved successfully!")
    else:
        messagebox.showwarning("Warning", "Please write something!")

def clear_note():
    text_area.delete("1.0", tk.END)


root = tk.Tk()
root.title("Digital Notes App")
root.geometry("450x400")

title = tk.Label(
    root,
    text="My Digital Notes",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

text_area = tk.Text(
    root,
    height=12,
    width=45,
    font=("Arial", 12)
)
text_area.pack(pady=10)

save_button = tk.Button(
    root,
    text="Save Note",
    command=save_note
)
save_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_note
)
clear_button.pack(pady=5)

root.mainloop()
