import tkinter
from tkinter import messagebox
import ttkbootstrap as tb
import Controller
import tkinter.ttk as ttk
from tkinter import font
from tkcalendar import DateEntry

class View:
    def __init__(self, root=None):
        self.tb=tb
        self.tkinter = tkinter
        self.messagebox = messagebox
        self.font = font
        #iconphoto not working
        self.root = root
        self.controller = Controller.Controller()
        self.show_welcome()

    

    def show_welcome(self):

        self.clear_content()
        self.root.geometry("600x400")
        self.label = tb.Label(self.root,text="Welcome to the App!", bootstyle="primary")
        self.label.pack(pady=40)

        self.login_btn = tb.Button(self.root,text="Login",bootstyle="success")
        self.login_btn.config(command=self.show_login)
        self.login_btn.pack(pady=20)

        self.register_btn = tb.Button(self.root,text="Register", bootstyle="info")
        self.register_btn.config(command=self.show_register)
        self.register_btn.pack(pady=10)

    def show_login(self):

        self.clear_content()
        self.root.geometry("600x400")
        phone_extensions = ["+1", "+44", "+91", "+33"]

        self.phone_extension_combobox = tb.Combobox(self.root, values=phone_extensions)
        self.phone_extension_combobox.pack(pady=10)

        self.phone_number_label = tb.Label(self.root, text="Phone Number:", bootstyle="primary")
        self.phone_number_label.pack(pady=10)

        self.phone_number_entry = tb.Entry(self.root, style="default.TEntry")   # Use default style for input fields
        self.phone_number_entry.pack(pady=10)
        self.phone_number_entry.focus_set()

        self.otp_label = tb.Label(self.root, text="OTP:", bootstyle="primary")
        self.otp_label.pack(pady=10)

        self.otp_entry = tb.Entry(self.root, style="default.TEntry")
        self.otp_entry.pack(pady=10)

        self.send_otp_btn = tb.Button(self.root, text="Send OTP", command=self.sendOtpRequest, bootstyle="success")  # Apply "success" style
        self.send_otp_btn.pack(pady=10)

        # self.login_btn = tb.Button(self.root, text="Login", command=self.controller.login_user, bootstyle="success")
        # self.login_btn.pack(pady=10)

        self.back_btn = tb.Button(self.root, text="Back", command=self.show_welcome, bootstyle="danger")  # Apply "danger" style
        self.back_btn.pack(pady=10)

    def show_register(self):
        
        self.clear_content()
        self.root.geometry("600x650")
        use_gmail_var = self.tkinter.BooleanVar()

        self.first_name_label = ttk.Label(self.root, text="First Name:")
        self.first_name_label.pack(pady=10)

        self.first_name_entry = ttk.Entry(self.root, style="default.TEntry")  # Use default style for input fields
        self.first_name_entry.pack(pady=10)

        self.last_name_label = ttk.Label(self.root, text="Last Name:")
        self.last_name_label.pack(pady=10)

        self.last_name_entry = ttk.Entry(self.root, style="default.TEntry")
        self.last_name_entry.pack(pady=10)

        self.gmail_label = ttk.Label(self.root, text="Gmail:")
        self.gmail_label.pack(pady=10)

        self.gmail_entry = ttk.Entry(self.root, style="default.TEntry")
        self.gmail_entry.pack(pady=10)

        self.use_gmail_checkbox = ttk.Checkbutton(self.root, text="Use Gmail as Username", variable=use_gmail_var, command=self.update_username_entry, style="default.TCheckbutton")
        self.use_gmail_checkbox.pack(pady=10)

        self.username_label = ttk.Label(self.root, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = ttk.Entry(self.root, style="default.TEntry")
        self.username_entry.pack(pady=10)

        self.phone_label = ttk.Label(self.root, text="Phone Number:")
        self.phone_label.pack(pady=10)

        self.phone_entry = ttk.Entry(self.root, style="default.TEntry")
        self.phone_entry.pack(pady=10)

        #self.dob_label = ttk.Label(self.root, text="Date of Birth:")
        #self.dob_label.pack(pady=10)

        #self.dob_entry = DateEntry(self.root, date_pattern="dd/mm/yyyy", style="default.TEntry")
        #self.dob_entry.pack(pady=10)

        self.register_btn = ttk.Button(self.root, text="Register", command=self.sendRegisterUserData, style="success.TButton")  # Apply "success" style
        self.register_btn.pack(pady=10)

        self.back_btn = ttk.Button(self.root, text="Back", command=self.show_welcome, style="danger.TButton")  # Apply "danger" style
        self.back_btn.pack(pady=10)

    def clear_content(self):
        for widget in self.root.winfo_children():
            widget.destroy()




# Function to update the username entry based on the checkbox state
    def update_username_entry(self):
        if self.use_gmail_var.get():
            self.username_entry.delete(0, "end")  # Clear the current username
            self.username_entry.insert(0, self.gmail_entry.get())  # Set username to Gmail address
        else:
            self.username_entry.delete(0, "end")  # Clear the current username


    def sendOtpRequest(self):

        phoneExtension = self.phone_extension_combobox.get()
        phoneNumber = self.phone_number_entry.get()

        if not phoneNumber:
            messagebox.showerror("Error", "Phone number is required!")
            return
        
        completePhoneNumber= phoneExtension+phoneNumber

        if self.controller.sendOtp(completePhoneNumber):
            return self.messagebox.showinfo("Success","OTP Sent Succesfully")
        return self.messagebox.showinfo("Error","Error Sending OTP")




    def sendRegisterUserData(self):
        # Get values from the user input fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        use_gmail = self.use_gmail_var.get()
        username = self.username_entry.get()
        phone_extension = self.phone_extension_combobox.get()
        phone_number = self.phone_number_entry.get()
        dob = self.dob_entry.get()

        # Check if required fields are empty
        if not first_name or not last_name or not dob:
            self.messagebox.showerror("Error", "First Name, Last Name, and Date of Birth are required.")
            return

        # If the user chose to use Gmail as username, set the username accordingly
        if use_gmail:
            username = username + "@gmail.com"

        # Combine phone extension and phone number
        complete_phone_number = phone_extension + phone_number

        # Register the user (you may call your registration function here)
        # Example: self.controller.registerUser(first_name, last_name, username, complete_phone_number, dob)

        # Display a success message or handle registration result
        registration_result = self.controller.registerUser(first_name, last_name, username, complete_phone_number, dob)
        if registration_result:
            self.messagebox.showinfo("Success", "User registered successfully.")
        else:
            self.messagebox.showerror("Error", "Error registering user.")

#=======================================================================================================================================================================

    def show_create_ride(self):
        # Clear the login screen widgets
        self.view.clear_content()

        # Add labels and text boxes for "To," "From," "Date," and "Time"
        ttk.Label(self.root, text="To:").pack(pady=5)
        self.to_entry_create = ttk.Entry(self.root)
        self.to_entry_create.pack(pady=5)

        ttk.Label(self.root, text="From:").pack(pady=5)
        self.from_entry_create = ttk.Entry(self.root)
        self.from_entry_create.pack(pady=5)

        ttk.Label(self.root, text="Date:").pack(pady=5)
        self.date_entry_create = ttk.Entry(self.root)
        self.date_entry_create.pack(pady=5)

        ttk.Label(self.root, text="Time:").pack(pady=5)
        self.time_entry_create = ttk.Entry(self.root)
        self.time_entry_create.pack(pady=5)

        # Create Ride button
        self.create_ride_button = ttk.Button(self.root, text="Create Ride", command=self.create_ride, style="Black.TButton")
        self.create_ride_button.pack(pady=10)


    def clear_content(self):
        # Remove all widgets from the window
        for widget in self.root.winfo_children():
            widget.destroy()