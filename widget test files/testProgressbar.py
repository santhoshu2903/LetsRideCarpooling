import tkinter as tk
from tkinter import ttk

def update_progress():
    global progress_position
    if progress_position == 0:
        progress_bar.step(33)  # Move to the second position
        progress_position = 1
    elif progress_position == 1:
        progress_bar.step(33)  # Move to the third position
        progress_position = 2
    else:
        progress_bar.stop()  # Stop when it reaches the third position

root = tk.Tk()
root.title("Custom Progress Bar")

progress_bar = ttk.Progressbar(root, mode="determinate", maximum=99, length=300)
progress_bar.grid(row=0, column=0, padx=10, pady=10)

progress_position = 0  # Tracks the current position of the progress bar

update_button = ttk.Button(root, text="Update Progress", command=update_progress)
update_button.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
import tkinter as tk
from tkinter import ttk

def update_progress():
    global progress_position
    if progress_position == 0:
        progress_bar.step(33)  # Move to the second position
        progress_position = 1
    elif progress_position == 1:
        progress_bar.step(33)  # Move to the third position
        progress_position = 2
    else:
        progress_bar.stop()  # Stop when it reaches the third position

root = tk.Tk()
root.title("Custom Progress Bar")

progress_bar = ttk.Progressbar(root, mode="determinate", maximum=99, length=300)
progress_bar.grid(row=0, column=0, padx=10, pady=10)

progress_position = 0  # Tracks the current position of the progress bar

update_button = ttk.Button(root, text="Update Progress", command=update_progress)
update_button.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
