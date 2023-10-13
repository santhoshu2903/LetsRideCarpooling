import tkinter as tk
from tkinter import ttk

def submit_phone_number():
    selected_extension = phone_extension_combobox.get()
    phone_number = phone_number_entry.get()
    full_phone_number = f"{selected_extension} {phone_number}"
    result_label.config(text=f"Phone number: {full_phone_number}")

root = tk.Tk()
root.title("Phone Number Entry")

# Create a Combobox for phone extensions
phone_extensions = ["+1", "+44", "+91", "+33"]
phone_extension_combobox = ttk.Combobox(root, values=phone_extensions)
phone_extension_combobox.set("+1")  # Set the default value
phone_extension_combobox.grid(row=0, column=0, padx=5, pady=10)

# Create an Entry for entering the phone number
phone_number_entry = ttk.Entry(root)
phone_number_entry.grid(row=0, column=1, padx=5, pady=10)

# Create a button to submit the phone number
submit_button = ttk.Button(root, text="Submit", command=submit_phone_number)
submit_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

# Create a label to display the result
result_label = ttk.Label(root, text="", font=("Helvetica", 14))
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
