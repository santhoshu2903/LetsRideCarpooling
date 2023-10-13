from tkinter import *
import Model
import View
from twilio.rest import Client 
import random
# from vonage import Client


class Controller:
    def __init__(self):
        self.model = Model.Model()
        self.twilioClient = Client
        self.randInt = random.randint
        # self.view= View.View()


    def registerUser(self,first_name, last_name,gmail, username, complete_phone_number, dob):
        return self.model.insertUser(first_name, last_name,gmail, username, complete_phone_number, dob)


    def sendOtp(self,phoneNumber):
        
        # twillio Details
        print("controller otp",phoneNumber)

        # account 1
        accountSID = "ACd607e2f86a57f692c81867be2f0b351f"
        authToken = "28000cefd2c2ff8f4c7ebb8b73d500ea"
        twillioPhoneNumber = "+18449584452"


        # account 2
        # accountSID = "AC0ced1832758903e7cc0d69bff6b1d26f"
        # authToken = "be2b35e7801d348501b8cb80ae5532d3"
        # twillioPhoneNumber = "+18447342183"


        smsClient =  self.twilioClient( accountSID,authToken)


        otpMessage = f"Your Let's Go, OTP is  {self.generateOTP()}"

        try:
            print("otp sent")
            otpMessage = smsClient.messages.create(
                to = phoneNumber,
                from_= twillioPhoneNumber,
                body = otpMessage
            )
            print(otpMessage.sid)
            return otpMessage.sid
        except Exception as e:
            print(e)
            return False

    def verify_login(self,phoneNumber):
        if self.model.get_loginUser_by_phone_number(phoneNumber):
            return True
            self.sendOtp(phoneNumber)
        return False

    def generateOTP(self):
        return self.randInt(100000,999999)
    

    def get_all_rides(self):
        return self.model.get_all_rides()


    # Add similar methods for retrieving users, handling user interactions, etc.
