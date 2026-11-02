import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x480")
root.resizable(False, False)
root.configure(bg="#202124")

# Calculator display
expression = ""

display = tk.Entry(
    root,
    font=("Arial", 25),
    bg="#303134",
    fg="white",
    justify="right",
    bd=0
)
display.pack(fill="both", padx=15, pady=20, ipady=15)


def click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def calculate():
    global expression

    try:
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

        expression = str(result)

    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""


# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Create button frame
frame = tk.Frame(root, bg="#202124")
frame.pack(expand=True, fill="both", padx=10, pady=10)

for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):

        if value == "=":
            command = calculate
            color = "#34A853"
        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: click(v)
            color = "#4285F4"
        else:
            command = lambda v=value: click(v)
            color = "#3C4043"

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            activebackground="#5F6368",
            activeforeground="white",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=5,
            pady=5
        )

# Clear button
clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 14, "bold"),
    bg="#EA4335",
    fg="white",
    bd=0,
    command=clear
)
clear_button.pack(fill="x", padx=15, pady=10, ipady=8)

# Equal button and grid resizing
for i in range(4):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

# Start application
root.mainloop()
``` id="calculator"
