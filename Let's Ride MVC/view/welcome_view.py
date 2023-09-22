import tkinter as tk
from tkinter import ttk

class WelcomeView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Welcome to Our App")
        self.geometry("500x400")
        self.configure(bg="#f4f4f4")  # Light grey background

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10, "bold"), borderwidth=0)
        style.configure("TLabel", font=("Segoe UI", 12), background="#f4f4f4")
        style.configure("TEntry", font=("Segoe UI", 10))

        self.label = ttk.Label(self, text="Welcome to Our App!")
        self.label.pack(pady=40)

        self.login_button = ttk.Button(self, text="Login", command=self.controller.show_login)
        self.login_button.pack(pady=10)

        self.register_button = ttk.Button(self, text="Register", command=self.controller.show_register)
        self.register_button.pack(pady=10)

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = WelcomeView(None)
    app.mainloop()
