import tkinter as tk

root = tk.Tk()

# Configure the number of rows in the grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=2)

# Create a label in the first row
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

# Create a label in the second row
label2 = tk.Label(root, text="Label 2")
label2.grid(row=1, column=0)

root.mainloop()
