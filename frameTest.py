import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os


DATABASE_DIR = os.path.join(os.getcwd(), "Database")
RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")

def init_db():
    # Initialize the riders database
    with sqlite3.connect(RIDERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS riders (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        ''')

    # Initialize the passengers database
    with sqlite3.connect(PASSENGERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS passengers (
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

        self.notebook = ttk.Notebook(self)
        
        # Rider Tab
        self.rider_frame = ttk.Frame(self.notebook)
        
        self.rider_username_label = ttk.Label(self.rider_frame, text="Rider Username:")
        self.rider_username_label.pack(pady=10)

        self.rider_username_entry = ttk.Entry(self.rider_frame)
        self.rider_username_entry.pack(pady=10)

        self.rider_password_label = ttk.Label(self.rider_frame, text="Rider Password:")
        self.rider_password_label.pack(pady=10)

        self.rider_password_entry = ttk.Entry(self.rider_frame, show="*")
        self.rider_password_entry.pack(pady=10)

        self.rider_register_btn = ttk.Button(self.rider_frame, text="Register as Rider", command=self.register_user)  # You can customize the command for rider-specific registration
        self.rider_register_btn.pack(pady=10)

        self.notebook.add(self.rider_frame, text="Rider")

        # Passenger Tab
        self.passenger_frame = ttk.Frame(self.notebook)

        self.passenger_username_label = ttk.Label(self.passenger_frame, text="Passenger Username:")
        self.passenger_username_label.pack(pady=10)

        self.passenger_username_entry = ttk.Entry(self.passenger_frame)
        self.passenger_username_entry.pack(pady=10)

        self.passenger_password_label = ttk.Label(self.passenger_frame, text="Passenger Password:")
        self.passenger_password_label.pack(pady=10)

        self.passenger_password_entry = ttk.Entry(self.passenger_frame, show="*")
        self.passenger_password_entry.pack(pady=10)

        self.passenger_register_btn = ttk.Button(self.passenger_frame, text="Register as Passenger", command=self.register_user)  # You can customize the command for passenger-specific registration
        self.passenger_register_btn.pack(pady=10)

        self.notebook.add(self.passenger_frame, text="Passenger")

        self.notebook.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        self.back_btn = ttk.Button(self, text="Back", command=self.show_welcome)
        self.back_btn.pack(pady=10)


    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return

        # Check credentials in the RIDERS_DB first
        with sqlite3.connect(RIDERS_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM riders WHERE username=? AND password=?", (username, password))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Rider login successful!")
                return  # Exit the method if found in RIDERS_DB

        # Check credentials in the PASSENGERS_DB next
        with sqlite3.connect(PASSENGERS_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM passengers WHERE username=? AND password=?", (username, password))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Passenger login successful!")
                return  # Exit the method if found in PASSENGERS_DB

        # If neither database has a match, display an error
        messagebox.showerror("Error", "Invalid Username or Password!")


    def register_user(self):
        current_tab = self.notebook.tab(self.notebook.select(), "text")

        if current_tab == "Rider":
            username = self.rider_username_entry.get()
            password = self.rider_password_entry.get()
            db_path = RIDERS_DB
            table_name = "riders"
        elif current_tab == "Passenger":
            username = self.passenger_username_entry.get()
            password = self.passenger_password_entry.get()
            db_path = PASSENGERS_DB
            table_name = "passengers"
        else:
            return

        if not username or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"INSERT INTO {table_name} (username, password) VALUES (?, ?)", (username, password))
                messagebox.showinfo("Success", f"Registered Successfully as {current_tab}!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", f"{current_tab} Username already exists!")


if __name__ == "__main__":
    init_db()
    app = WelcomeWindow()
    app.mainloop()
