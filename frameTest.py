import random
import tkinter as tk
from tkinter import ttk, messagebox
from twilio.rest import Client
import sqlite3
import os


#DATABASE_DB = "/Database/passengers.db"

DATABASE_DIR = os.path.join(os.getcwd(), "Database")
RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")
ALL_USERS_DB = os.path.join(DATABASE_DIR,"all_users.db")

def init_db():
    # Initialize the riders database
    with sqlite3.connect(RIDERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS riders (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone_number TEXT,
        phone_extension TEXT
    );
    ''')

    # Initialize the passengers database
    with sqlite3.connect(PASSENGERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS passengers (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone_number TEXT,
        phone_extension TEXT
    );
    ''')
    
    #Initialize the all users database( contains userid, phone number and name)
    with sqlite3.connect(ALL_USERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS riders (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        phone_number TEXT,
        phone_extension TEXT
    );
    ''')

class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Let's GO Ride With Us")
        self.geometry("500x400")
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

        phone_extensions = ["+1", "+44", "+91", "+33"]  # Example extensions, add as needed

        self.phone_extension_combobox = ttk.Combobox(self, values=phone_extensions)
        self.phone_extension_combobox.pack(pady=10)
        self.phone_extension_combobox.set(phone_extensions[0])  # Set default value

        self.phone_number_label = ttk.Label(self, text="Phone Number:")
        self.phone_number_label.pack(pady=10)

        self.phone_number_entry = ttk.Entry(self)
        self.phone_number_entry.pack(pady=10)
        self.phone_number_entry.focus_set()

        self.otp_label = ttk.Label(self, text="OTP:")
        self.otp_label.pack(pady=10)

        self.otp_entry = ttk.Entry(self)
        self.otp_entry.pack(pady=10)

        self.send_otp_btn = ttk.Button(self, text="Send OTP", command=self.send_otp)
        self.send_otp_btn.pack(pady=10)

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



        phone_extensions = ["+1", "+44", "+91", "+33"]  # Example extensions, you can add more

        self.passenger_password_label = ttk.Label(self.rider_frame, text="Rider Phone Number:")
        self.passenger_password_label.pack(pady=10)

        self.rider_phone_extension_combobox = ttk.Combobox(self.rider_frame, values=phone_extensions)
        self.rider_phone_extension_combobox.pack(pady=10)
        self.rider_phone_extension_combobox.set(phone_extensions[0])  # Set default value

        self.rider_phone_number_entry = ttk.Entry(self.rider_frame)
        self.rider_phone_number_entry.pack(pady=10)

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

        self.passenger_password_label = ttk.Label(self.passenger_frame, text="Passenger Phone Number:")
        self.passenger_password_label.pack(pady=10)
        
        self.passenger_phone_extension_combobox = ttk.Combobox(self.passenger_frame, values=phone_extensions)
        self.passenger_phone_extension_combobox.pack(pady=10)
        self.passenger_phone_extension_combobox.set(phone_extensions[0])  # Set default value

        self.passenger_phone_number_entry = ttk.Entry(self.passenger_frame)
        self.passenger_phone_number_entry.pack(pady=10)

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
        phone_extension = self.phone_extension_combobox.get()
        phone_number = self.phone_number_entry.get()
        otp_entered = self.otp_entry.get()

        if not phone_number or not otp_entered:
            messagebox.showerror("Error", "Both fields are required!")
            return

        # Check OTP in the RIDERS_DB first
        with sqlite3.connect(RIDERS_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM riders WHERE phone_extension=? AND phone_number=? AND otp=?", (phone_extension, phone_number, otp_entered))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Rider login successful!")
                return  # Exit the method if OTP matches in RIDERS_DB

        # Check OTP in the PASSENGERS_DB next
        with sqlite3.connect(PASSENGERS_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM passengers WHERE phone_extension=? AND phone_number=? AND otp=?", (phone_extension, phone_number, otp_entered))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Passenger login successful!")
                return  # Exit the method if OTP matches in PASSENGERS_DB

        # If neither database has a match, display an error
        messagebox.showerror("Error", "Invalid OTP or Phone Number!")


    def register_user(self):
        current_tab = self.notebook.tab(self.notebook.select(), "text")

        if current_tab == "Rider":
            username = self.rider_username_entry.get()
            password = self.rider_password_entry.get()
            phone_extension = self.rider_phone_extension_combobox.get()
            phone_number = self.rider_phone_number_entry.get()
            db_path = RIDERS_DB
            table_name = "riders"
        elif current_tab == "Passenger":
            username = self.passenger_username_entry.get()
            password = self.passenger_password_entry.get()
            phone_extension = self.passenger_phone_extension_combobox.get()
            phone_number = self.passenger_phone_number_entry.get()
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
                cursor.execute(f"INSERT INTO {table_name} (username, password, phone_extension, phone_number) VALUES (?, ?, ?, ?)", 
                            (username, password, phone_extension, phone_number))
                messagebox.showinfo("Success", f"Registered Successfully as {current_tab}!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", f"{current_tab} Username already exists!")

    def send_otp(self):
        phone_extension = self.phone_extension_combobox.get()
        phone_number = phone_extension + self.phone_number_entry.get()

        # Generate a random 6-digit OTP
        self.otp_generated = str(random.randint(100000, 999999))

        try:
            # Send the OTP to the user's phone number using the send_sms function
            send_sms(phone_number, f"Your OTP is: {self.otp_generated}")
            messagebox.showinfo("Success", f"OTP sent to {phone_number}")
        except Exception as e:
            messagebox.showerror("Error", f"Error sending OTP: {str(e)}")

def send_sms(phone_number, message):
    # My Twilio account SID and Auth Token
    account_sid = 'ACd607e2f86a57f692c81867be2f0b351f'
    auth_token = 'acda06ff971cc152136b2355c24b9a11'
    client = Client(account_sid, auth_token)

    # My Twilio phone number
    twilio_phone_number = '+18449584452'
    message = client.messages.create(
        to=phone_number,
        from_=twilio_phone_number,
        body=message
    )
    return message.sid



if __name__ == "__main__":
    init_db()
    app = WelcomeWindow()
    app.mainloop()
