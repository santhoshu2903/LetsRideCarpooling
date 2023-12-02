import tkinter as tk

def button_click(button_number):
    print(f"Button {button_number} Clicked!")

# Create the main window
root = tk.Tk()
root.title("Left, Center, Right Buttons Example")

# Create three buttons
button_left = tk.Button(root, text="Left", command=lambda: button_click(1))
button_center = tk.Button(root, text="Center", command=lambda: button_click(2))
button_right = tk.Button(root, text="Right", command=lambda: button_click(3))

# Pack the buttons at left, center, and right positions
button_left.pack(side="left", padx=10, pady=10)
button_center.pack(anchor="center", pady=10)
button_right.pack(side="right", padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
