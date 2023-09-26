from tkinter import *
import Model
import View


class Controller:
    def __init__(self):
        self.model = Model.Model()
        # self.view= View.View()


    def registerRider(self,username, password, phonenumber, extension):
        # print(username, password, phonenumber, extension)
        if not username or not password or not phonenumber:
            self.view.show_error_message("Both fields are required!")
            return
    
        return self.model.setRider(username,password, phonenumber, extension)
        
    


    def registerPassenger(self,username, password, phonenumber, extension):
        if not username or not password or not phonenumber:
            self.view.show_error_message("Both fields are required!")
            return
    
        return self.model.setPassenger(username,password, phonenumber, extension)


    def register_user(self):
        current_tab = self.view.get_current_tab()  
        if current_tab == "Rider":
            username = self.view.get_rider_username()
            password = self.view.get_rider_password()

            phone_extension = self.view.get_rider_phone_extension()
            phone_number = self.view.get_rider_phone_number()
            table_name = "riders"
        elif current_tab == "Passenger":
            username = self.view.get_passenger_username()
            password = self.view.get_passenger_password()
            phone_extension = self.view.get_passenger_phone_extension()
            phone_number = self.view.get_passenger_phone_number()
            table_name = "passengers"
        else:
            return

        if not username or not password:
            # self.view.show_error_message("Both fields are required!")
            return

        # Call the appropriate method in the Model to insert the user
        if current_tab == "Rider":
            self.model.insert_rider(username, password, phone_number, phone_extension)
        elif current_tab == "Passenger":
            self.model.insert_passenger(username, password, phone_number, phone_extension)

        # self.view.show_success_message(f"Registered Successfully as {current_tab}!")


    def send_otp(self):
        pass

    def login_user(self):
        pass

    # Add similar methods for retrieving users, handling user interactions, etc.
