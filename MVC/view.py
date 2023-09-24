# view.py

import tkinter as tk
from tkinter import ttk, messagebox

class WelcomeWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Let's GO Ride With Us")
        self.geometry("500x400")
        self.configure(bg="#f4f4f4")

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
        phone_extensions = ["+1", "+44", "+91", "+33"]
        self.phone_extension_combobox = ttk.Combobox(self, values=phone_extensions)
        self.phone_extension_combobox.pack(pady=10)
        self.phone_extension_combobox.set(phone_extensions[0])
        self.phone_number_label = ttk.Label(self, text="Phone Number:")
        self.phone_number_label.pack(pady=10)
        self.phone_number_entry = ttk.Entry(self)
        self.phone_number_entry.pack(pady=10)
        self.phone_number_entry.focus_set()
        self.otp_label = ttk.Label(self, text="OTP:")
        self.otp_label.pack(pady=10)
        self.otp_entry = ttk.Entry(self)
        self.otp_entry.pack(pady=10)
        self.send_otp_btn = ttk.Button(self, text="Send OTP", command=self.controller.send_otp)
        self.send_otp_btn.pack(pady=10)
        self.login_btn = ttk.Button(self, text="Login", command=self.controller.login_user)
        self.login_btn.pack(pady=10)
        self.back_btn = ttk.Button(self, text="Back", command=self.show_welcome)
        self.back_btn.pack(pady=10)
        self.back_btn = ttk.Button(self, text="Back", command=self.show_welcome)
        self.back_btn.pack(pady=10)

    def show_register(self):
        self.clear_content()
        self.notebook = ttk.Notebook(self)
        self.rider_frame = ttk.Frame(self.notebook)
        self.rider_username_label = ttk.Label(self.rider_frame, text="Rider Username:")
        self.rider_username_label.pack(pady=10)
        self.rider_username_entry = ttk.Entry(self.rider_frame)
        self.rider_username_entry.pack(pady=10)
        self.rider_password_label = ttk.Label(self.rider_frame, text="Rider Password:")
        self.rider_password_label.pack(pady=10)
        self.rider_password_entry = ttk.Entry(self.rider_frame, show="*")
        self.rider_password_entry.pack(pady=10)
        phone_extensions = ["+1", "+44", "+91", "+33"]
        self.passenger_password_label = ttk.Label(self.rider_frame, text="Rider Phone Number:")
        self.passenger_password_label.pack(pady=10)
        self.rider_phone_extension_combobox = ttk.Combobox(self.rider_frame, values=phone_extensions)
        self.rider_phone_extension_combobox.pack(pady=10)
        self.rider_phone_extension_combobox.set(phone_extensions[0])
        self.rider_phone_number_entry = ttk.Entry(self.rider_frame)
        self.rider_phone_number_entry.pack(pady=10)
        self.rider_register_btn = ttk.Button(self.rider_frame, text="Register as Rider", command=self.controller.register_rider)
        self.rider_register_btn.pack(pady=10)
        self.notebook.add(self.rider_frame, text="Rider")
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
        self.passenger_phone_extension_combobox.set(phone_extensions[0])
        self.passenger_phone_number_entry = ttk.Entry(self.passenger_frame)
        self.passenger_phone_number_entry.pack(pady=10)
        self.passenger_register_btn = ttk.Button(self.passenger_frame, text="Register as Passenger", command=self.controller.register_passenger)
        self.passenger_register_btn.pack(pady=10)
        self.notebook.add(self.passenger_frame, text="Passenger")
        self.notebook.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)
        self.back_btn = ttk.Button(self, text="Back", command=self.show_welcome)
        self.back_btn.pack(pady=10)

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_success(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

# Other methods for displaying UI components
