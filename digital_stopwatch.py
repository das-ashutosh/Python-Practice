import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Stopwatch")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg="#202124")

running = False
start_time = 0
elapsed_time = 0


def update_timer():
    if running:
        current = elapsed_time + (time.time() - start_time)

        minutes = int(current // 60)
        seconds = int(current % 60)
        milliseconds = int((current % 1) * 100)

        display.config(
            text=f"{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
        )

        root.after(10, update_timer)


def start():
    global running, start_time

    if not running:
        start_time = time.time()
        running = True
        update_timer()


def stop():
    global running, elapsed_time

    if running:
        elapsed_time += time.time() - start_time
        running = False


def reset():
    global running, elapsed_time

    running = False
    elapsed_time = 0
    display.config(text="00:00:00")


title = tk.Label(
    root,
    text="DIGITAL STOPWATCH",
    font=("Arial", 18, "bold"),
    bg="#202124",
    fg="white"
)
title.pack(pady=20)

display = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 35, "bold"),
    bg="#303134",
    fg="#34A853",
    width=12
)
display.pack(pady=15)

button_frame = tk.Frame(root, bg="#202124")
button_frame.pack(pady=20)

tk.Button(
    button_frame, text="START",
    command=start, bg="#34A853",
    fg="white", width=8
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame, text="STOP",
    command=stop, bg="#EA4335",
    fg="white", width=8
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame, text="RESET",
    command=reset, bg="#4285F4",
    fg="white", width=8
).grid(row=0, column=2, padx=5)

root.mainloop()
