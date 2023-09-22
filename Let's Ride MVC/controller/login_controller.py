import tkinter as tk
import random
from tkinter import messagebox
from view.login_view import LoginView
from view.welcome_view import WelcomeView

class LoginController:
    def __init__(self, root):
        self.root = root
        self.view = LoginView(self)
        self.view.mainloop()

    def send_otp(self):
        # Implement sending OTP logic here (e.g., using Twilio)
        # Generate OTP (for example, a random 6-digit number)
        otp_generated = str(random.randint(100000, 999999))
        # Send the OTP to the user's phone number

        # For demonstration purposes, we'll show a messagebox with the generated OTP
        messagebox.showinfo("OTP Sent", f"OTP sent to your phone: {otp_generated}")

    def login_user(self):
        phone_extension = self.view.phone_extension_combobox.get()
        phone_number = self.view.phone_number_entry.get()
        otp_entered = self.view.otp_entry.get()

        if not phone_number or not otp_entered:
            messagebox.showerror("Error", "Both fields are required!")
            return

        # Check OTP validity (you can implement this logic)

        # For demonstration purposes, we'll show a messagebox with a successful login message
        messagebox.showinfo("Success", "Login successful!")

    def show_welcome(self):
        self.view.clear_content()
        welcome_controller = WelcomeController(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginController(root)
    root.mainloop()
