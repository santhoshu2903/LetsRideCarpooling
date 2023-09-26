from tkinter import *
import Model
import View
from twilio.rest import Client 
import random


class Controller:
    def __init__(self):
        self.model = Model.Model()
        self.twilioClient = Client
        self.randInt = random.randint
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


    def sendOtp(self,phoneNumber):
        
        #twillio Details

        accountSID = "ACd607e2f86a57f692c81867be2f0b351f"
        authToken = "96b7f2afb95fe95ebdda6d837187d123"
        twillioPhoneNumber = "+18449584452"

        smsClient =  self.twilioClient( accountSID,authToken)


        otpMessage = f"Your Let's Go, OTP is  {self.generateOTP()}"

        try:
            otpMessage = smsClient.messages.create(
                to = phoneNumber,
                from_= twillioPhoneNumber,
                body = otpMessage
            )
        except Exception as e:
            print(e)
            return False

        




    def generateOTP(self):
        return self.randInt(100000,999999)
    

    def login_user(self):
        pass

    # Add similar methods for retrieving users, handling user interactions, etc.
