from tkinter import * 
from tkinter import messagebox
import tkinter.ttk as ttk
import Controller
from tkinter import PhotoImage
# import Model 

class View:
    def __init__(self, root=None):
        self.messagebox =messagebox
        self.root = root
        self.controller = Controller.Controller()
        # self.model = Model.Model()
        self.root.title("Let's Go, Ride with US")
        self.root.geometry("400x400")
        self.show_welcome()
        style = ttk.Style()
        style.configure("Black.TButton", foreground="black", background="black")
        self.background_image = PhotoImage(file='')

    


    def show_welcome(self):
        self.clear_content()
        

        self.label = ttk.Label(self.root, text="Welcome to the App!")
        self.label.pack(pady=40)

        self.login_button = ttk.Button(self.root, text="Login", command=self.show_login, style="Black.TButton")
        self.login_button.pack(pady=10)
        
        self.register_button = ttk.Button(self.root, text="Register", command=self.show_register, style="Black.TButton")
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
        
        self.send_otp_btn = ttk.Button(self.root, text="Send OTP", command=self.sendOtpRequest, style="Black.TButton")
        self.send_otp_btn.pack(pady=10)
        
        self.login_btn = ttk.Button(self.root, text="Login", command=self.controller.login_user, style="Black.TButton")
        self.login_btn.pack(pady=10)
        
        self.back_btn = ttk.Button(self.root, text="Back", command=self.show_welcome, style="Black.TButton")
        self.back_btn.pack(pady=10)
        


    def show_register(self):
        self.clear_content()

        self.notebook = ttk.Notebook(self.root) 

        # Rider Tab
        self.rider_frame = ttk.Frame(self.notebook)

        self.rider_username_label = ttk.Label(self.rider_frame, text="Rider Username:")
        self.rider_username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.rider_username_entry = ttk.Entry(self.rider_frame)
        self.rider_username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.rider_password_label = ttk.Label(self.rider_frame, text="Rider Password:")
        self.rider_password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.rider_password_entry = ttk.Entry(self.rider_frame, show="*")
        self.rider_password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        phone_extensions = ["+1", "+44", "+91", "+33"]  
        self.rider_phone_label = ttk.Label(self.rider_frame, text="Rider Phone Number:")
        self.rider_phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.rider_phone_extension_combobox = ttk.Combobox(self.rider_frame, values=phone_extensions)
        self.rider_phone_extension_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.rider_phone_extension_combobox.set(phone_extensions[0])  # Set default value

        self.rider_phone_number_entry = ttk.Entry(self.rider_frame)
        self.rider_phone_number_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.rider_register_btn = ttk.Button(self.rider_frame, text="Register as Rider", command=self.sendRegisterRiderData, style="Black.TButton")
        self.rider_register_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.rider_back_btn = ttk.Button(self.rider_frame, text="Back", command=self.show_welcome, style="Black.TButton")
        self.rider_back_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.notebook.add(self.rider_frame, text="Register as a Rider")

        # Passenger Tab
        self.passenger_frame = ttk.Frame(self.notebook)

        self.passenger_username_label = ttk.Label(self.passenger_frame, text="Passenger Username:")
        self.passenger_username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.passenger_username_entry = ttk.Entry(self.passenger_frame)
        self.passenger_username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.passenger_password_label = ttk.Label(self.passenger_frame, text="Passenger Password:")
        self.passenger_password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.passenger_password_entry = ttk.Entry(self.passenger_frame, show="*")
        self.passenger_password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.passenger_phone_label = ttk.Label(self.passenger_frame, text="Passenger Phone Number:")
        self.passenger_phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.passenger_phone_extension_combobox = ttk.Combobox(self.passenger_frame, values=phone_extensions)
        self.passenger_phone_extension_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.passenger_phone_extension_combobox.set(phone_extensions[0])  # Set default value

        self.passenger_phone_number_entry = ttk.Entry(self.passenger_frame)
        self.passenger_phone_number_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.passenger_register_btn = ttk.Button(self.passenger_frame, text="Register as Passenger", command=self.sendRegisterPassengerData, style="Black.TButton")
        self.passenger_register_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.passenger_back_btn = ttk.Button(self.passenger_frame, text="Back", command=self.show_welcome, style="Black.TButton")
        self.passenger_back_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.notebook.add(self.passenger_frame, text="Register as a Passenger")

        self.notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")



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






    def sendRegisterRiderData(self):
        userName = self.rider_username_entry.get()
        password = self.rider_password_entry.get()
        phoneNumber = self.rider_phone_number_entry.get()

        if not userName or not password or not phoneNumber:
            self.messagebox.showerror("Error","All fields are required.")
        else:
            # Combine phone extension and phone number
            phoneExtension = self.rider_phone_extension_combobox.get()
            completePhoneNumber = phoneExtension + phoneNumber

            # Register the rider
            if self.controller.registerRider(userName, password, completePhoneNumber):
                self.messagebox.showinfo("Success","Rider registered successfully.")
            else:
                self.messagebox.showerror("Error","Error registering rider.")

        
    def sendRegisterPassengerData(self):

        userName = self.passenger_username_entry.get()
        password =  self.passenger_password_entry.get()
        phoneNumber = self.passenger_phone_number_entry.get()
        phoneExtension = self.passenger_phone_extension_combobox.get()

        completePhoneNumber = phoneExtension+phoneNumber

        if userName or password or phoneNumber:
            return self.controller.registerPassenger(userName,password,completePhoneNumber )
            
        self.messagebox.showerror("Error","Required needs to filled.")

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