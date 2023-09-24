# controller.py

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_login(self):
        self.view.show_login()

    def show_register(self):
        self.view.show_register()

    def send_otp(self):
        self.view.send_otp()

    def login_user(self):
        phone_extension = self.view.phone_extension_combobox.get()
        phone_number = self.view.phone_number_entry.get()
        otp_entered = self.view.otp_entry.get()

        if not phone_number or not otp_entered:
            self.view.show_error("Error", "Both fields are required!")
            return

        if self.model.login_user(phone_extension, phone_number, otp_entered):
            self.view.show_success("Success", "Login successful!")
        else:
            self.view.show_error("Error", "Invalid OTP or Phone Number!")

    def register_rider(self):
        username = self.view.rider_username_entry.get()
        password = self.view.rider_password_entry.get()
        phone_extension = self.view.rider_phone_extension_combobox.get()
        phone_number = self.view.rider_phone_number_entry.get()

        if not username or not password:
            self.view.show_error("Error", "Both fields are required!")
            return

        if self.model.register_user(username, password, phone_extension, phone_number):
            self.view.show_success("Success", "Registered Successfully as Rider!")
        else:
            self.view.show_error("Error", "Rider Username already exists!")

    def register_passenger(self):
        username = self.view.passenger_username_entry.get()
        password = self.view.passenger_password_entry.get()
        phone_extension = self.view.passenger_phone_extension_combobox.get()
        phone_number = self.view.passenger_phone_number_entry.get()

        if not username or not password:
            self.view.show_error("Error", "Both fields are required!")
            return

        if self.model.register_user(username, password, phone_extension, phone_number):
            self.view.show_success("Success", "Registered Successfully as Passenger!")
        else:
            self.view.show_error("Error", "Passenger Username already exists!")
