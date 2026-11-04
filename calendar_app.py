import tkinter as tk
import calendar

def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())

        if month < 1 or month > 12:
            raise ValueError

        result.delete("1.0", tk.END)
        result.insert(tk.END, calendar.month(year, month))

    except ValueError:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Enter a valid year and month (1-12).")


root = tk.Tk()
root.title("Calendar Application")
root.geometry("350x400")

tk.Label(root, text="Python Calendar",
         font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Enter Year").pack()
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

tk.Label(root, text="Enter Month (1-12)").pack()
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

tk.Button(root, text="Show Calendar",
          command=show_calendar).pack(pady=10)

result = tk.Text(root, height=10, width=30,
                 font=("Courier", 12))
result.pack(pady=10)

root.mainloop()
