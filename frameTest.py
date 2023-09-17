import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DATABASE_NAME = "users.db"

def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        ''')

class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Let's GO Ride With Us")
        self.geometry("400x300")
        self.configure(bg="#f4f4f4")  # Light grey background

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10, "bold"), borderwidth=0)
        style.configure("TLabel", font=("Segoe UI", 12), background="#f4f4f4")
        style.configure("TEntry", font=("Segoe UI", 10))
        self.show_welcome()

    def show_welcome(self):
        self.clear_content()

        self.label = ttk.Label(self, text="Welcome to the App!")
        self.label.pack(pady=40)

        self.login_button = ttk.Button(self, text="Login", command=self.show_login)
        self.login_button.pack(pady=10)

        self.register_button = ttk.Button(self, text="Register", command=self.show_register)
        self.register_button.pack(pady=10)

    def show_login(self):
        self.clear_content()

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=10)
        self.username_entry.focus_set()

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=10)

        self.login_btn = ttk.Button(self, text="Login", command=self.login_user)
        self.login_btn.pack(pady=10)

        self.back_btn = ttk.Button(self, text="Back", command=self.show_welcome)
        self.back_btn.pack(pady=10)

    def show_register(self):
        self.clear_content()

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=10)
        self.username_entry.focus_set()

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=10)

        self.register_btn = ttk.Button(self, text="Register", command=self.register_user)
        self.register_btn.pack(pady=10)

        self.back_btn = ttk.Button(self, text="Back", command=self.show_welcome)
        self.back_btn.pack(pady=10)

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Login Successful!")
            else:
                messagebox.showerror("Error", "Invalid Username or Password!")

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return

        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                messagebox.showinfo("Success", "Registered Successfully!")
                self.show_login()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists!")

if __name__ == "__main__":
    init_db()
    app = WelcomeWindow()
    app.mainloop()
