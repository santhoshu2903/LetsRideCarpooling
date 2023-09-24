from tkinter import * 
import tkinter.ttk as ttk
import Controller
import Model 

class View:
    def __init__(self, root=None):
        self.root = root
        self.controller = Controller.Controller()
        self.model = Model.Model()
        self.root.title("Let's Go, Ride with US")
        self.root.geometry("500x400")
        self.show_welcome()


    def show_welcome(self):
        self.clear_content()

        self.label = ttk.Label(self.root, text="Welcome to the App!")
        self.label.pack(pady=40)

        self.login_button = ttk.Button(self.root, text="Login", command=self.show_login)
        self.login_button.pack(pady=10)
        
        self.register_button = ttk.Button(self.root, text="Register", command=self.show_register)
        self.register_button.pack(pady=10)


    def show_login(self):
        self.clear_content()
        phone_extensions = ["+1", "+44", "+91", "+33"]
        
        self.phone_extension_combobox = ttk.Combobox(self.root, values=phone_extensions)
        self.phone_extension_combobox.pack(pady=10)
        self.phone_extension_combobox.set(phone_extensions[0])
        
        self.phone_number_label = ttk.Label(self.root, text="Phone Number:")
        self.phone_number_label.pack(pady=10)
        
        self.phone_number_entry = ttk.Entry(self.root)
        self.phone_number_entry.pack(pady=10)
        self.phone_number_entry.focus_set()
        
        self.otp_label = ttk.Label(self.root, text="OTP:")
        self.otp_label.pack(pady=10)
        
        self.otp_entry = ttk.Entry(self.root)
        self.otp_entry.pack(pady=10)
        
        self.send_otp_btn = ttk.Button(self.root, text="Send OTP", command=self.controller.send_otp)
        self.send_otp_btn.pack(pady=10)
        
        self.login_btn = ttk.Button(self.root, text="Login", command=self.controller.login_user)
        self.login_btn.pack(pady=10)
        
        self.back_btn = ttk.Button(self.root, text="Back", command=self.show_welcome)
        self.back_btn.pack(pady=10)
        


    def show_register(self):
        self.clear_content()

        self.notebook = ttk.Notebook(self.root)  # Use self.root as the parent

        # Rider Tab
        self.rider_frame = ttk.Frame(self.notebook)
            # Add this after creating the notebook widget
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


        self.rider_username_label = ttk.Label(self.rider_frame, text="Rider Username:")
        self.rider_username_label.pack(pady=10)

        self.rider_username_entry = ttk.Entry(self.rider_frame)
        self.rider_username_entry.pack(pady=10)

        self.rider_password_label = ttk.Label(self.rider_frame, text="Rider Password:")
        self.rider_password_label.pack(pady=10)

        self.rider_password_entry = ttk.Entry(self.rider_frame, show="*")
        self.rider_password_entry.pack(pady=10)

        phone_extensions = ["+1", "+44", "+91", "+33"]  # Example extensions, you can add more

        self.rider_password_label = ttk.Label(self.rider_frame, text="Rider Phone Number:")
        self.rider_password_label.pack(pady=10)

        self.rider_phone_extension_combobox = ttk.Combobox(self.rider_frame, values=phone_extensions)
        self.rider_phone_extension_combobox.pack(pady=10)
        self.rider_phone_extension_combobox.set(phone_extensions[0])  # Set default value

        self.rider_phone_number_entry = ttk.Entry(self.rider_frame)
        self.rider_phone_number_entry.pack(pady=10)

        self.rider_register_btn = ttk.Button(self.rider_frame, text="Register as Rider", command=self.model.insert_rider)  # You can customize the command for rider-specific registration
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

        self.passenger_register_btn = ttk.Button(self.passenger_frame, text="Register as Passenger", command=self.model.register_user)  # You can customize the command for passenger-specific registration
        self.passenger_register_btn.pack(pady=10)

        self.notebook.add(self.passenger_frame, text="Passenger")

        self.notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.back_btn = ttk.Button(self.root, text="Back", command=self.show_welcome)  # Use self.root as the parent
        self.back_btn.pack(pady=10)

    def clear_content(self):
        # Remove all widgets from the window
        for widget in self.root.winfo_children():
            widget.destroy()