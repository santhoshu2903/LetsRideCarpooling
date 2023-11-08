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


    #check_if_already_booked
    def check_if_already_booked(self,rideid,userid):
        return self.model.check_if_already_booked(rideid,userid)
    #update_available_seats
    def update_available_seats(self,rideid,available_seats):
        return self.model.update_available_seats(rideid,available_seats)
    
    #get_rides_count_by_driverid
    def get_rides_count_by_driverid(self,driverid):
        return self.model.get_rides_count_by_driverid(driverid)
    
    #get_all_rides_count
    def get_all_rides_count(self):
        return self.model.get_all_rides_count()
    
    #get_active_riders_count
    def get_active_riders_count(self):
        return self.model.get_active_riders_count()
    
    #get_active_passengers_count
    def get_active_passengers_count(self):
        return self.model.get_active_passengers_count()


    #.get_ride_by_rideid
    def get_ride_by_rideid(self,rideid):
        return self.model.get_ride_by_rideid(rideid)

    #get_all_confirmed_rides_by_user
    def get_all_confirmed_rides_by_user(self,userid):
        return self.model.get_all_confirmed_rides_by_user(userid)


    #confirm ride
    def confirm_ride(self,rideid,userid,no_of_seats):
        return self.model.confirm_ride( rideid,userid,no_of_seats)
    
    #get_rideid_by_ridedetails

    def get_rideid_by_ridedetails(self,driverid,from_location,to_location,date,time,available_seats):
        return self.model.get_rideid_by_ridedetails(driverid,from_location,to_location,date,time,available_seats)


    def registerUser(self,first_name, last_name,gmail, username, complete_phone_number, dob):
        return self.model.insertUser(first_name, last_name,gmail, username,self.generatePassword(), complete_phone_number, dob)
    

    def add_ride(self, driverid,drivername,from_location, to_location, date, time,available_seats):
        return self.model.add_ride(driverid,drivername,from_location, to_location, date, time,available_seats)
    
    def get_current_user_object(self,phone_number):
        return self.model.get_User_by_phone_number(phone_number)  


    #get_all_users
    def get_all_users(self):
        return self.model.get_all_users()
          
    
    #get rides by riderid
    def get_rides_by_driverid(self, driverid):
        return self.model.get_rides_by_driverid(driverid)
    

    #get user object by phone number
    def get_user_by_phone_number(self,phone_number):
        return self.model.get_User_by_phone_number(phone_number)

    #get rides by that user
    def get_rides_by_user(self, driverid):
        return self.model.get_rides_by_user(driverid)
    

    def sendOtp(self,phoneNumber):
        
        # twillio Details
        print("controller otp",phoneNumber)

        # account 1
        accountSID = "ACd607e2f86a57f692c81867be2f0b351f"
        authToken = "67aade8043b726228d6eea789bb0eb15"
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

    def generateOTP(self):
        self.currentOTP=self.randInt(100000,999999)
        return self.currentOTP
    
    def verifyOTP(self,otp):
        # if self.currentOTP==otp:
        #     return True
        # return False

        #for testing match it with blank
        return True
    

    def get_all_rides(self):
        rides_objects= self.model.get_all_rides()
        rides_data =[]
        for ride in rides_objects:
            rides_data.append([ride[0],ride[1],ride[2],ride[3],ride[4],ride[5],ride[6],ride[7]])
        return rides_data
    

    #random password generator aplhanumeric and special characters
    def generatePassword(self):
        password = ''
        for i in range(0, 8):
            password += chr(random.randint(33, 126))
        return password    
        
    def update_password(self,phone_number,new_password):
        return self.model.update_password(phone_number,new_password)


    # Add similar methods for retrieving users, handling user interactions, etc.
