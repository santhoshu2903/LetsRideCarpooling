import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
import customtkinter as ctk
import Controller
import tkinter.ttk as ttk
from tkinter import font
from tkcalendar import DateEntry


class View(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Let's Go Ride with US")
        # self.iconphoto(False, tk.PhotoImdsage(file='images/icon.jpg'))
        self.controller = Controller.Controller()
        self.show_welcome()

    def show_welcome(self):
        self.clear_content()
        self.geometry("600x400")

        self.ctk_label = ctk.CTkLabel(self,text="Welcome to the App!", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.ctk_label.pack(pady=40)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.show_login)
        self.login_button.pack(pady=20)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.show_register)
        self.register_button.pack(pady=10)


    def show_login(self):
        self.clear_content()
        self.geometry("600x500")
        phone_extensions = ["+1", "+44", "+91", "+33"]
        self.phone_extension_combobox = ctk.CTkComboBox(self, values=phone_extensions)
        self.phone_extension_combobox.pack(pady=10)

        self.phone_number_label = ctk.CTkLabel(self, text="Phone Number:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.phone_number_label.pack(pady=10)

        self.phone_number_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.phone_number_entry.pack(pady=10)

        self.otp_label = ctk.CTkLabel(self, text="OTP:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.otp_label.pack(pady=10)

        self.otp_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.otp_entry.pack(pady=10)

        self.send_otp_button = ctk.CTkButton(self, text="Send OTP", command=self.sendOtpRequest)
        self.send_otp_button.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.controller.verify_login)
        self.login_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.show_welcome)
        self.back_button.pack(pady=10)



    def show_register(self):
        self.clear_content()
        self.geometry("600x750")
        self.use_gmail_var = tk.BooleanVar()



        #create labels and entry fields and place them side by side using grid
        self.first_name_label = ctk.CTkLabel(self, text="First Name:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.first_name_label.pack(pady=5)

        self.first_name_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.first_name_entry.pack(pady=5)

        self.last_name_label = ctk.CTkLabel(self, text="Last Name:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.last_name_label.pack(pady=5)

        self.last_name_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.last_name_entry.pack(pady=5)

        self.gmail_label = ctk.CTkLabel(self, text="Gmail:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.gmail_label.pack(pady=5)

        self.gmail_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.gmail_entry.pack(pady=5)

        self.use_gmail_checkbox = ctk.CTkCheckBox(self, text="Use Gmail as Username", variable=self.use_gmail_var, command=self.update_username_entry)
        self.use_gmail_checkbox.pack(pady=5)
        
        self.username_label = ctk.CTkLabel(self, text="Username:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.username_label.pack(pady=5)

        self.username_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.username_entry.pack(pady=5)

        self.phone_label = ctk.CTkLabel(self, text="Phone Number:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.phone_label.pack(pady=5)

        self.phone_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.phone_entry.pack(pady=5)

        self.user_type_label = ctk.CTkLabel(self, text="User Type:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.user_type_label.pack(pady=5)

        user_type_values = ["Rider", "Passenger"]
        self.user_type_combobox = ctk.CTkComboBox(self, values=user_type_values)
        self.user_type_combobox.pack(pady=5)

        self.dob_label = ctk.CTkLabel(self, text="Date of Birth:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.dob_label.pack(pady=5)

        self.dob_entry = ctk.CTkEntry(self, placeholder_text="mm/dd/yyyy", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.dob_entry.pack(pady=5)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.sendRegisterUserData)
        self.register_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.show_welcome)
        self.back_button.pack(pady=5)





    def clear_content(self):
        # Remove all widgets from the window
        for widget in self.winfo_children():
            widget.destroy()

    def update_username_entry(self):
        if self.use_gmail_var.get():
            self.username_entry.delete(0, "end")  # Clear the current username
            self.username_entry.insert(0, self.gmail_entry.get())  # Set username to Gmail address
        else:
            self.username_entry.delete(0, "end")  # Clear the current username

        

    def sendRegisterUserData(self):
        # Get values from the user input fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        use_gmail = self.use_gmail_var.get()
        username = self.username_entry.get()
        phone_number = self.phone_number_entry.get()
        dob = self.dob_entry.get()

        # Check if required fields are empty
        if not first_name or not last_name or not dob:
            messagebox.showerror("Error", "First Name, Last Name, and Date of Birth are required.")
            return

        # If the user chose to use Gmail as username, set the username accordingly
        if use_gmail:
            username = username + "@gmail.com"

        # Combine phone extension and phone number
        complete_phone_number =phone_number

        # Register the user (you may call your registration function here)
        # Example: self.controller.registerUser(first_name, last_name, username, complete_phone_number, dob)

        # Display a success message or handle registration result
        registration_result = self.controller.registerUser(first_name, last_name, username, complete_phone_number, dob)
        if registration_result:
            messagebox.showinfo("Success", "User registered successfully.")
        else:
            messagebox.showerror("Error", "Error registering user.")

    def sendOtpRequest(self):
        pass

# class View:
#     def __init__(self, root=None):
#         self.tb=tb
#         self.tk = tk
#         self.messagebox = messagebox
#         self.font = font
#         #iconphoto not working
#         self.root = root
#         self.root.geometry("1380x1020")
#         self.controller = Controller.Controller()

#         # #stlying the buttons
#         # self.button_style = self.tb.Style()
#         # self.button_style.configure('Custom.TButton', font=('Helvetica', 14, 'bold'), bordercolor='green', borderless=1, background='green', foreground='white')
#         # self.rounded_button_style = self.tb.Style()
#         # self.rounded_button_style.configure('Rounded.TButton', font=('Helvetica', 14, 'bold'), relief='raised', borderwidth=5,padding=(10,5))
#         self.show_welcome()

#     def show_welcome(self):

#         self.clear_content()
#         self.root.geometry("600x500")
#         self.label = tb.Label(self.root,text="Welcome to the App!", bootstyle="primary")
#         self.label.pack(pady=40)

#         self.login_btn = tb.Button(self.root,text="Login",bootstyle="success")
#         self.login_btn.config(command=self.user_page)
#         self.login_btn.pack(pady=20)

#         self.register_btn = tb.Button(self.root,text="Register", bootstyle="info")
#         self.register_btn.config(command=self.show_register)
#         self.register_btn.pack(pady=10)

#     def show_login(self):

#         self.clear_content()
#         self.root.geometry("600x600")
#         phone_extensions = ["+1", "+44", "+91", "+33"]

#         self.phone_extension_combobox = tb.Combobox(self.root, values=phone_extensions)
#         self.phone_extension_combobox.pack(pady=10)

#         self.phone_number_label = tb.Label(self.root, text="Phone Number:", bootstyle="primary")
#         self.phone_number_label.pack(pady=10)

#         self.phone_number_entry = tb.Entry(self.root, style="default.TEntry")   # Use default style for input fields
#         self.phone_number_entry.pack(pady=10)
#         self.phone_number_entry.focus_set()

#         self.otp_label = tb.Label(self.root, text="OTP:", bootstyle="primary")
#         self.otp_label.pack(pady=10)

#         self.otp_entry = tb.Entry(self.root, style="default.TEntry")
#         self.otp_entry.pack(pady=10)

#         self.send_otp_btn = tb.Button(self.root, text="Send OTP", command=self.sendOtpRequest, bootstyle="success")  # Apply "success" style
#         self.send_otp_btn.pack(pady=10)

#         self.login_btn = tb.Button(self.root, text="Login", command=self.controller.verify_login, bootstyle="success")
#         self.login_btn.pack(pady=10)

#         self.back_btn = tb.Button(self.root, text="Back", command=self.show_welcome, bootstyle="danger")  # Apply "danger" style
#         self.back_btn.pack(pady=10)

#     def show_register(self):
        
#         self.clear_content()
#         # self.root.geometry("600x650")
#         use_gmail_var = self.tkinter.BooleanVar()

#         self.first_name_label = ttk.Label(self.root, text="First Name:")
#         self.first_name_label.pack(pady=10)

#         self.first_name_entry = ttk.Entry(self.root, style="default.TEntry")  # Use default style for input fields
#         self.first_name_entry.pack(pady=10)

#         self.last_name_label = ttk.Label(self.root, text="Last Name:")
#         self.last_name_label.pack(pady=10)

#         self.last_name_entry = ttk.Entry(self.root, style="default.TEntry")
#         self.last_name_entry.pack(pady=10)

#         self.gmail_label = ttk.Label(self.root, text="Gmail:")
#         self.gmail_label.pack(pady=10)

#         self.gmail_entry = ttk.Entry(self.root, style="default.TEntry")
#         self.gmail_entry.pack(pady=10)

#         self.use_gmail_checkbox = ttk.Checkbutton(self.root, text="Use Gmail as Username", variable=use_gmail_var, command=self.update_username_entry, style="default.TCheckbutton")
#         self.use_gmail_checkbox.pack(pady=10)

#         self.username_label = ttk.Label(self.root, text="Username:")
#         self.username_label.pack(pady=10)

#         self.username_entry = ttk.Entry(self.root, style="default.TEntry")
#         self.username_entry.pack(pady=10)

#         self.phone_label = ttk.Label(self.root, text="Phone Number:")
#         self.phone_label.pack(pady=10)

#         self.phone_entry = ttk.Entry(self.root, style="default.TEntry")
#         self.phone_entry.pack(pady=10)

#         self.user_type_label = ttk.Label(self.root, text="User Type:")
#         self.user_type_label.pack(pady=10)

#         user_type_values = ["Rider", "Passenger"]
#         self.user_type_combobox = ttk.Combobox(self.root, values=user_type_values, style="default.TCombobox")
#         self.user_type_combobox.pack(pady=10)

#         #self.dob_label = ttk.Label(self.root, text="Date of Birth:")
#         #self.dob_label.pack(pady=10)

#         #self.dob_entry = DateEntry(self.root, date_pattern="dd/mm/yyyy", style="default.TEntry")
#         #self.dob_entry.pack(pady=10)

#         self.register_btn = ttk.Button(self.root, text="Register", command=self.sendRegisterUserData, style="success.TButton")  # Apply "success" style
#         self.register_btn.pack(pady=10)

#         self.back_btn = ttk.Button(self.root, text="Back", command=self.show_welcome, style="danger.TButton")  # Apply "danger" style
#         self.back_btn.pack(pady=10)

#     # def clear_content(self):
#     #     for widget in self.root.winfo_children():
#     #         widget.destroy()


#     def clear_content(self):
#         # Remove all widgets from the window
#         for widget in self.root.winfo_children():
#             widget.destroy()


# # Function to update the username entry based on the checkbox state
#     def update_username_entry(self):
#         if self.use_gmail_var.get():
#             self.username_entry.delete(0, "end")  # Clear the current username
#             self.username_entry.insert(0, self.gmail_entry.get())  # Set username to Gmail address
#         else:
#             self.username_entry.delete(0, "end")  # Clear the current username


#     def sendOtpRequest(self):

#         phoneExtension = self.phone_extension_combobox.get()
#         phoneNumber = self.phone_number_entry.get()

#         if not phoneNumber:
#             messagebox.showerror("Error", "Phone number is required!")
#             return
        
#         completePhoneNumber= phoneExtension+phoneNumber

#         if self.controller.sendOtp(completePhoneNumber):
#             return self.messagebox.showinfo("Success","OTP Sent Succesfully")
#         return self.messagebox.showinfo("Error","Error Sending OTP")




#     def sendRegisterUserData(self):
#         # Get values from the user input fields
#         first_name = self.first_name_entry.get()
#         last_name = self.last_name_entry.get()
#         use_gmail = self.use_gmail_var.get()
#         username = self.username_entry.get()
#         phone_extension = self.phone_extension_combobox.get()
#         phone_number = self.phone_number_entry.get()
#         dob = self.dob_entry.get()

#         # Check if required fields are empty
#         if not first_name or not last_name or not dob:
#             self.messagebox.showerror("Error", "First Name, Last Name, and Date of Birth are required.")
#             return

#         # If the user chose to use Gmail as username, set the username accordingly
#         if use_gmail:
#             username = username + "@gmail.com"

#         # Combine phone extension and phone number
#         complete_phone_number = phone_extension + phone_number

#         # Register the user (you may call your registration function here)
#         # Example: self.controller.registerUser(first_name, last_name, username, complete_phone_number, dob)

#         # Display a success message or handle registration result
#         registration_result = self.controller.registerUser(first_name, last_name, username, complete_phone_number, dob)
#         if registration_result:
#             self.messagebox.showinfo("Success", "User registered successfully.")
#         else:
#             self.messagebox.showerror("Error", "Error registering user.")


#     def show_create_ride(self):
#         # Clear the login screen widgets
#         self.view.clear_content()

#         # Add labels and text boxes for "To," "From," "Date," and "Time"
#         ttk.Label(self.root, text="To:").pack(pady=5)
#         self.to_entry_create = ttk.Entry(self.root)
#         self.to_entry_create.pack(pady=5)

#         ttk.Label(self.root, text="From:").pack(pady=5)
#         self.from_entry_create = ttk.Entry(self.root)
#         self.from_entry_create.pack(pady=5)

#         ttk.Label(self.root, text="Date:").pack(pady=5)
#         self.date_entry_create = ttk.Entry(self.root)
#         self.date_entry_create.pack(pady=5)

#         ttk.Label(self.root, text="Time:").pack(pady=5)
#         self.time_entry_create = ttk.Entry(self.root)
#         self.time_entry_create.pack(pady=5)

#         # Create Ride button
#         self.create_ride_button = ttk.Button(self.root, text="Create Ride", command=self.create_ride, style="Black.TButton")
#         self.create_ride_button.pack(pady=10)

#     def user_page(self):
#         self.clear_content()
#         self.user_page=ttk.Frame(self.root)
#         self.user_page.pack()
#         self.user_page.config(height=1000,width=1000)
#         # self.user_page.config(bg="blue")
#         self.user_page.config(relief="sunken")
#         self.user_page.config(padding=(30,15))
#         self.user_page.config(borderwidth=5)


#         self.user_page_label=ttk.Label(self.user_page,text="User Page")
#         self.user_page_label.pack(pady=10)

#         self.rides_listbox = tk.Listbox(self.user_page, height=20, width=50)
#         self.rides_listbox.pack(pady=10)

#         self.rides_button = ttk.Button(self.user_page, text="Rides", command=self.show_rides, style="Black.TButton")
#         self.rides_button.pack(pady=10)

    
#     def show_rides(self):

#         #clear the listbox
#         self.rides_listbox.delete(0,ttk.END)

#         #get the rides from the controller
#         rides = self.controller.get_all_rides()

#         #display the rides in the listbox
#         for ride in rides:
#             self.ride_listbox.insert(ttk.END, f"From: {ride['from_location']}, To: {ride['to_location']}, Date: {ride['date']}, Time: {ride['time']}")
        

#     def clear_content(self):
#         # Remove all widgets from the window
#         for widget in self.root.winfo_children():
#             widget.destroy()