import customtkinter
from CTkTable import *
from CTkTableRowSelector import *

root = customtkinter.CTk()

value = [
    ["Header" + letter for letter in "ABCDE"],
    *[[i, i+1, i+2, i+3, i+4] for i in range(0, 25, 5)]
]
table = CTkTable(master=root, row=5, column=5, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)

# Add the selector
row_selector = CTkTableRowSelector(table)

# Get the value
button = customtkinter.CTkButton(
    root, text="Print selected rows", command=lambda: print(row_selector.get())
)
button.pack(pady=(0, 20))

root.mainloop()