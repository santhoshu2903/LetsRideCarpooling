import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random

class LoginView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Login")
        self.geometry("500x400")
        self.configure(bg="#f4f4f4")

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10, "bold"), borderwidth=0)
        style.configure("TLabel", font=("Segoe UI", 12), background="#f4f4f4")
        style.configure("TEntry", font=("Segoe UI", 10))
        self.show_login()

    def show_login(self):
        self.clear_content()

        self.phone_extensions = ["+1", "+44", "+91", "+33"]
        
        self.phone_extension_combobox = ttk.Combobox(self, values=self.phone_extensions)
        self.phone_extension_combobox.pack(pady=10)
        self.phone_extension_combobox.set(self.phone_extensions[0])

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

        self.back_btn = ttk.Button(self, text="Back", command=self.controller.show_welcome)
        self.back_btn.pack(pady=10)

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

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

    def login_user(self):
        phone_extension = self.phone_extension_combobox.get()
        phone_number = self.phone_number_entry.get()
        otp_entered = self.otp_entry.get()

        if not phone_number or not otp_entered:
            messagebox.showerror("Error", "Both fields are required!")
            return

        # Check OTP entered by the user with the OTP generated earlier
        if otp_entered == self.otp_generated:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid OTP!")

def send_sms(phone_number, message):
    # Implement Twilio SMS sending logic here
