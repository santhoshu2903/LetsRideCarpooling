import tkinter as tk

root = tk.Tk()

root.overrideredirect(True)
root.geometry("120x30+1000+550")

label = tk.Label(root, text='Python', bg='white', fg='red', font=('Courier', 25))
label.pack()

root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", '#fc0000')

root.mainloop()