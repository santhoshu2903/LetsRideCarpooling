import tkinter as tk
from tkinter import messagebox
from view.register_view import RegisterView
from view.welcome_view import WelcomeView
from controller.welcome_controller import WelcomeController

class RegisterController:
    def __init__(self, root):
        self.root = root
        self.view = RegisterView(self)
        self.view.mainloop()

    def register_rider(self):
        username = self.view.rider_username_entry.get()
        password = self.view.rider_password_entry.get()
        phone_extension = self.view.rider_phone_extension_combobox.get()
        phone_number = self.view.rider_phone_number_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required!")
            return

        # Check if the user exists or register the user in the rider's database
        # Implement your database registration logic here

        # For demonstration purposes, we'll show a messagebox with a successful registration message
        messagebox.showinfo("Success", "Registered as Rider!")

    def register_passenger(self):
        username = self.view.passenger_username_entry.get()
        password = self.view.passenger_password_entry.get()
        phone_extension = self.view.passenger_phone_extension_combobox.get()
        phone_number = self.view.passenger_phone_number_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required!")
            return

        # Check if the user exists or register the user in the passenger's database
        # Implement your database registration logic here

        # For demonstration purposes, we'll show a messagebox with a successful registration message
        messagebox.showinfo("Success", "Registered as Passenger!")

    def show_welcome(self):
        self.view.clear_content()
        welcome_controller = WelcomeController(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterController(root)
    root.mainloop()
