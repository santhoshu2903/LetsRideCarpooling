import tkinter as tk
from tkinter import messagebox
# import ttkbootstrap as tb
import customtkinter as ctk
import Controller
import tkinter.ttk as ttk
from tkinter import font
from tkcalendar import Calendar, DateEntry
import CTkTable  as ctkTable
from CTkTableRowSelector import *

class View(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.frame = {}
        self.title("Let's Go Ride with US")
        # self.iconphoto(False, tk.PhotoImdsage(file='images/icon.jpg'))
        self.controller = Controller.Controller()
        self.show_welcome()
        ctk.set_appearance_mode("light")

    def show_welcome(self):
        self.clear_content()
        self.geometry("600x400")

        self.show_welcome_frame = ctk.CTkFrame(self)

        self.ctk_label = ctk.CTkLabel(self,text="Welcome to the App!", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.ctk_label.pack(pady=40)

        # self.login_button = ctk.CTkButton(self, text="Login", command=self.show_login)
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

        # self.login_button = ctk.CTkButton(self, text="Login", command=self.controller.verify_login)
        # self.login_button = ctk.CTkButton(self, text="Login", command=self.home_page)
        self.login_button = ctk.CTkButton(self, text="Login", command=self.verify_login)
        self.login_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.show_welcome)
        self.back_button.pack(pady=10)


    def show_home_page_frame(self,frame_name):

        #hide all frames    
        for frame in self.frame.values():
            frame.grid_forget()

        # #update table data if frame_name is search_for_ride
        # if frame_name == "search_for_ride":
        #     self.table_data = [["Ride ID", "Rider Name", "From Location", "To Location", "Date", "Start Time"]] 
        #     for ride in self.controller.get_all_rides():
        #         self.table_data.append([ride[0],ride[2],ride[3],ride[4],ride[5],ride[6]])
        #     self.search_for_ride_table.update_values(self.table_data)

        #show selected frame
        self.dashboard_button.configure(fg_color=("dodger blue") if frame_name == "dashboard" else "transparent")
        self.search_for_ride_button.configure(fg_color=("dodger blue") if frame_name == "search_for_ride" or frame_name=="confirm_ride" else "transparent")
        self.give_ride_button.configure(fg_color=("dodger blue") if frame_name == "give_ride" else "transparent")
        self.my_rides_button.configure(fg_color=("dodger blue") if frame_name == "my_rides" else "transparent")
        self.feedback_button.configure(fg_color=("dodger blue") if frame_name == "feedback" else "transparent")

        self.frame[frame_name].grid(row=0, column=1, sticky="nsew")

    def home_page(self):
        self.clear_content()
        self.geometry("1050x600")


        #store current user name
        # self.current_user_object = self.controller.get_current_user_object()


        #set grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        #set navigation frame

        self.navigation_frame = ctk.CTkFrame(self, bg_color="blue", corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)



        #set navigation buttons

        #set dashboard button
        self.dashboard_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,border_spacing=10, text="DashBoard",
                                         fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                         anchor="w",command=lambda : self.show_home_page_frame("dashboard"))
        self.dashboard_button.grid(row=0, column=0, sticky="ew")
        
        #set serch for ride button
        self.search_for_ride_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,border_spacing=10, text="Search for Ride",
                                            fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                            anchor="w",command=self.search_for_ride_page)
        self.search_for_ride_button.grid(row=1, column=0, sticky="ew")
        
        #set create ride button
        self.give_ride_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,border_spacing=10, text="Give Ride",
                                            fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                            anchor="w",command=lambda:self.show_home_page_frame("give_ride")   )
        self.give_ride_button.grid(row=2, column=0, sticky="ew")
        
        #set my rides button
        self.my_rides_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,border_spacing=10, text="My Rides",
                                            fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                            anchor="w",command=lambda:self.show_home_page_frame("my_rides"))
        self.my_rides_button.grid(row=3, column=0, sticky="ew")


        #set feedback button
        self.feedback_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,border_spacing=10, text="Feedback",
                                            fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                            anchor="w",command=lambda:self.show_home_page_frame("feedback"))
        self.feedback_button.grid(row=4, column=0, sticky="ew")
        

        #set logout button at bottom of frame
        self.logout_button = ctk.CTkButton(self.navigation_frame,  text="Logout", command=self.show_welcome)
        self.logout_button.grid(row=5, column=0, sticky="sew", padx=10, pady=10)


        #create dashboard frame as frame["dashboard"]
        self.frame["dashboard"] = ctk.CTkFrame(self,fg_color="transparent", corner_radius=0)
        self.frame["dashboard"].columnconfigure(0, weight=1)

        #create dashboard label
        self.dashboard_label = ctk.CTkLabel(self.frame["dashboard"], text="Dashboard", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.dashboard_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #create search for ride frame as frame["search_for_ride"]
        self.frame["search_for_ride"] = ctk.CTkFrame(self,fg_color="transparent" ,corner_radius=0)
        self.frame["search_for_ride"].columnconfigure(0, weight=1)

        #create search for ride label
        self.search_for_ride_label = ctk.CTkLabel(self.frame["search_for_ride"], text="Search for Ride", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.search_for_ride_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #search bar entry directly in search for ride frame

        #confirm ride button on selected row redirects to new frame within search for ride frame 
        #confirm ride frame as frame["confirm_ride"]
        #it consists of details to insert of the passengers and how many seats he wants to book
        self.frame["confirm_ride"] = ctk.CTkFrame(self,fg_color="transparent", corner_radius=0)
        self.frame["confirm_ride"].columnconfigure(1, weight=1)

        #create confirm ride label
        self.confirm_ride_label = ctk.CTkLabel(self.frame["confirm_ride"], text="Confirm Ride", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.confirm_ride_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        #create give ride frame as frame["give_ride"]
        self.frame["give_ride"] = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.frame["give_ride"].columnconfigure(0, weight=1)

        #create create ride button top right corner
        self.create_ride_button = ctk.CTkButton(self.frame["give_ride"], text="+ New Ride",command=lambda :  self.show_home_page_frame("new_ride"))
        self.create_ride_button.grid(row=0, column=5, sticky="nw", padx=30, pady=30)

        #give_ride headers
        give_ride_headers = [["Ride ID",  "From Location", "To Location", "Date", "Start Time","Available Seats"]]

        #table data
        self.give_ride_table_data = give_ride_headers
        
        #insert rider name, from location, to location, date, time in table_data
        for ride in self.controller.get_rides_by_driverid(self.current_user_object[0]):
            self.give_ride_table_data.append([ride[0],ride[3],ride[4],ride[5],ride[6],ride[7]])

        #table frame
        self.give_ride_table_frame = ctk.CTkFrame(self.frame["give_ride"], fg_color="transparent", corner_radius=0)
        self.give_ride_table_frame.grid(row=3, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)

        #table 
        self.give_ride_table= ctkTable.CTkTable(self.give_ride_table_frame,values=self.give_ride_table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.give_ride_table.edit_row(0,text_color="blue",hover_color="light blue")
        # self.search_for_ride_table.columns[0].width = 100
        self.give_ride_table.grid(sticky="nsew", padx=10, pady=10)

        #create new ride frame as frame["new_ride"]
        self.frame["new_ride"] = ctk.CTkFrame(self,fg_color="transparent", corner_radius=0)
        self.frame["new_ride"].columnconfigure(1, weight=1)

        #Insert new ride frame elements
        #create Add new ride heading
        self.new_ride_label = ctk.CTkLabel(self.frame["new_ride"], text="Add New Ride", fg_color="transparent", font=("Helvetica", 25, "bold"))
        self.new_ride_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        #rider name label
        self.driver_name_label = ctk.CTkLabel(self.frame["new_ride"], text="Driver Name : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.driver_name_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        #rider name entry display current signed in username
        self.driver_name_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.driver_name_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        #set rider name entry to current signed in username from current_user_object
        self.current_user_name = self.current_user_object[1]+" "+self.current_user_object[2]
        self.driver_name_entry.insert(0,self.current_user_name)   

        #create from location label and entry side by side
        self.from_location_label = ctk.CTkLabel(self.frame["new_ride"], text="From Location : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.from_location_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        self.from_location_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.from_location_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10,columnspan=2)

        #create to location label and entry side by side
        self.to_location_label = ctk.CTkLabel(self.frame["new_ride"], text="To Location : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.to_location_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        self.to_location_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.to_location_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        # #create date label and entry side by side
        self.date_label = ctk.CTkLabel(self.frame["new_ride"], text="Date : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.date_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        # self.date_entry =DateEntry(self.frame["new_ride"], date_pattern="MM/dd/yyyy", font=("Arial", 15))
        # self.date_entry.grid(row=4, column=1, sticky="w", padx=10, pady=10)

        self.date_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.date_entry.grid(row=4, column=1, sticky="w", padx=10, pady=10)

        #create time label and entry side by side
        self.time_label = ctk.CTkLabel(self.frame["new_ride"], text="Time : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.time_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

        self.time_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.time_entry.grid(row=5, column=1, sticky="w", padx=10, pady=10)

        #crate available seats label and entry side by side
        self.available_seats_label = ctk.CTkLabel(self.frame["new_ride"], text="Available Seats : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.available_seats_label.grid(row=6, column=0, sticky="e", padx=10, pady=10)

        self.available_seats_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.available_seats_entry.grid(row=6, column=1, sticky="w", padx=10, pady=10)

        #create submit button
        self.submit_button = ctk.CTkButton(self.frame["new_ride"], text="Submit",command=self.send_ride_data)
        self.submit_button.grid(row=7, column=1, sticky="w", padx=10, pady=10)

        #create back button to create rides frame  
        self.back_button = ctk.CTkButton(self.frame["new_ride"], text="Back",command=lambda :  self.show_home_page_frame("give_ride"))
        self.back_button.grid(row=8, column=1, sticky="w", padx=10, pady=10)

        #create my rides frame as frame["my_rides"]
        self.frame["my_rides"] = ctk.CTkFrame(self,fg_color="transparent", corner_radius=0)
        self.frame["my_rides"].columnconfigure(0, weight=1)

        #create my rides label
        self.my_rides_label = ctk.CTkLabel(self.frame["my_rides"], text="My Rides", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.my_rides_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #my rides headers
        my_rides_headers = [["Driver Name", "From Location", "To Location", "Date", "Start Time","Seats Booked"]]
        #table data
        self.my_rides_table_data = my_rides_headers

        #insert rider name, from location, to location, date, time and seats booked in table_data
        #get all confride rides by userid
        rideids=[]
        seats_booked=[]
        ride_details=[]
        for ride in self.controller.get_all_confirmed_rides_by_user(self.current_user_object[0]):
            rideids.append(ride[1])
            seats_booked.append(ride[3])
            ride_details.append(self.controller.get_ride_by_rideid(ride[1]))
        
        #create my rides table data
        for i in range(len(rideids)):
            self.my_rides_table_data.append([ride_details[i][2],ride_details[i][3],ride_details[i][4],ride_details[i][5],ride_details[i][6],seats_booked[i]])

        #table frame
        self.my_rides_table_frame = ctk.CTkFrame(self.frame["my_rides"], fg_color="transparent", corner_radius=0)
        self.my_rides_table_frame.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        #table
        self.my_rides_table= ctkTable.CTkTable(self.my_rides_table_frame,values=self.my_rides_table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.my_rides_table.edit_row(0,text_color="blue",hover_color="light blue")
        self.my_rides_table.grid(sticky="nsew", padx=10, pady=10)

        #create feedback frame as frame["feedback"]
        self.frame["feedback"] = ctk.CTkFrame(self,fg_color="transparent", corner_radius=0)
        self.frame["feedback"].columnconfigure(0, weight=1)

        #create feedback label
        self.feedback_label = ctk.CTkLabel(self.frame["feedback"], text="Feedback", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.feedback_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #show dashboard frame as default frame
        self.show_home_page_frame("dashboard")


    def search_for_ride_page(self):

        self.show_home_page_frame("search_for_ride")

        
        #3 entries in one row , from ,to, date and time
        self.search_for_ride_search_bar_entry = ctk.CTkEntry(self.frame["search_for_ride"],width=150, placeholder_text="from ").grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.search_for_ride_search_bar_entry = ctk.CTkEntry(self.frame["search_for_ride"],width=150, placeholder_text="to").grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.search_for_ride_search_bar_entry = ctk.CTkEntry(self.frame["search_for_ride"],width=150, placeholder_text="date").grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
        self.search_for_ride_search_bar_entry = ctk.CTkEntry(self.frame["search_for_ride"],width=150, placeholder_text="time").grid(row=1, column=3, sticky="nsew", padx=10, pady=10)


        #search button display corresponding data in the below table
        self.search_for_ride_search_button = ctk.CTkButton(self.frame["search_for_ride"], text="Search",command=lambda : self.show_home_page_frame("search_for_ride"))
        self.search_for_ride_search_button.grid(row=1, column=4, sticky="ne", padx=10, pady=10)

        #headers lists
        headers = [["Driver Name", "From Location", "To Location", "Date", "Start Time","Available Seats"]]

        #table data
        self.table_data = headers
        
        #insert rider name, from location, to location, date, time in table_data
        for ride in self.controller.get_all_rides():
            self.table_data.append([ride[2],ride[3],ride[4],ride[5],ride[6],ride[7]])

        #table frame
        self.search_for_ride_table_frame = ctk.CTkFrame(self.frame["search_for_ride"], fg_color="transparent", corner_radius=0)
        self.search_for_ride_table_frame.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        #table 
        self.search_for_ride_table= ctkTable.CTkTable(self.search_for_ride_table_frame,values=self.table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.search_for_ride_table.edit_row(0,text_color="blue",hover_color="light blue")
        self.search_for_ride_table.grid(sticky="nsew", padx=10, pady=10)

        self.search_for_ride_table_selector = CTkTableRowSelector(self.search_for_ride_table)
        #confirm ride button on selected row redirects to new frame within search for ride frame
        #confirm ride frame as frame["confirm_ride"]
        self.search_for_ride_confirm_ride_button = ctk.CTkButton(self.frame["search_for_ride"], text="Confirm Ride",command=lambda : self.confirm_ride_page())
        self.search_for_ride_confirm_ride_button.grid(row=3, column=4, sticky="se", padx=10, pady=10)


    def confirm_ride_page(self):
        self.current_ride_data = self.search_for_ride_table_selector.get()
        user_details = self.current_user_object


        #check if current ride data is empty
        if self.current_ride_data == []:
            messagebox.showerror("Error", "Please select a ride")
            return
        #check if current user is same as driver name
        if self.current_ride_data[0][0] == user_details[1]+" "+user_details[2]:
            messagebox.showerror("Error", "You cannot book your own ride")
            return
        self.show_home_page_frame("confirm_ride")
        self.current_ride_data = self.current_ride_data[0]

        #get number of seats available
        available_seats = self.current_ride_data[5]


        #print(self.current_ride_data)
        #get rideid by drivername, from location, to location, date, time, available seats
           
        #current user details
       
        #create label and entry for passengers details and seats
        #for each seat new details of passengers should be created
        #passenger name label and entry

        #from and to location label and entry combined in one entry box
        #from location label and entry combined in one entry box
        #ride path label
        self.from_to_location_label = ctk.CTkLabel(self.frame["confirm_ride"], text="Ride Path : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.from_to_location_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)


        self.from_to_location_entry = ctk.CTkEntry(self.frame["confirm_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.from_to_location_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        self.from_to_location_entry.insert(0,self.current_ride_data[1]+" to "+self.current_ride_data[2])

        #driver name
        self.driver_name_label = ctk.CTkLabel(self.frame["confirm_ride"], text="Driver Name : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.driver_name_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.driver_name_entry = ctk.CTkEntry(self.frame["confirm_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.driver_name_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.driver_name_entry.insert(0,self.current_ride_data[0])



        #passenger name label and entry
        self.passenger_name_label = ctk.CTkLabel(self.frame["confirm_ride"], text="Passenger Name : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.passenger_name_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        self.passenger_name_entry = ctk.CTkEntry(self.frame["confirm_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.passenger_name_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        #passenger phone number label and entry
        self.passenger_phone_number_label = ctk.CTkLabel(self.frame["confirm_ride"], text="Passenger Phone Number : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.passenger_phone_number_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)

        self.passenger_phone_number_entry = ctk.CTkEntry(self.frame["confirm_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.passenger_phone_number_entry.grid(row=4, column=1, sticky="w", padx=10, pady=10)

        #passenger email label and entry
        self.passenger_email_label = ctk.CTkLabel(self.frame["confirm_ride"], text="Passenger Email : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.passenger_email_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)

        self.passenger_email_entry = ctk.CTkEntry(self.frame["confirm_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.passenger_email_entry.grid(row=5, column=1, sticky="w", padx=10, pady=10)

        #set driver name entry to current signed in username from current_user_object
        self.passenger_name_entry.insert(0,user_details[1]+" "+user_details[2])
        self.passenger_phone_number_entry.insert(0,user_details[6])
        self.passenger_email_entry.insert(0,user_details[3])

        #passenger seats label and entry
        #no of seats comboxbox to select and based on count of seats available
        self.passenger_seats_label = ctk.CTkLabel(self.frame["confirm_ride"], text="Passenger Seats : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.passenger_seats_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)

        available_seats = [str(i) for i in range(1,available_seats+1)]

        self.passenger_seats_combobox = ctk.CTkComboBox(self.frame["confirm_ride"], values=available_seats)
        self.passenger_seats_combobox.grid(row=6, column=1, sticky="w", padx=10, pady=10)

        #passenger confirm button
        self.passenger_confirm_button = ctk.CTkButton(self.frame["confirm_ride"], text="Confirm",command=self.confirm_ride)
        self.passenger_confirm_button.grid(row=7, column=1, sticky="w", padx=10, pady=10)

        #passenger back button to search for ride frame
        self.passenger_back_button = ctk.CTkButton(self.frame["confirm_ride"], text="Back",command=lambda : self.show_home_page_frame("search_for_ride"))
        self.passenger_back_button.grid(row=8, column=1, sticky="w", padx=10, pady=10)

    #send ride data to controller
    def send_ride_data(self):
        #get data from new ride frame
        driverid = self.current_user_object[0]
        driver_name = self.driver_name_entry.get()
        from_location = self.from_location_entry.get()
        to_location = self.to_location_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        available_seats = self.available_seats_entry.get()

        #clear all entries
        self.from_location_entry.delete(0, "end")
        self.to_location_entry.delete(0, "end")
        self.date_entry.delete(0, "end")
        self.time_entry.delete(0, "end")
        self.available_seats_entry.delete(0, "end")
        

        #send data to controller
        new_ride=self.controller.add_ride(driverid,driver_name, from_location, to_location, date, time,available_seats)
        if new_ride:
            self.search_for_ride_table.add_row([new_ride[2],new_ride[3],new_ride[4],new_ride[5],new_ride[6],new_ride[7]])
            self.give_ride_table.add_row([new_ride[0],new_ride[3],new_ride[4],new_ride[5],new_ride[6],new_ride[7]])
        
        #show my rides frame
        self.show_home_page_frame("give_ride")

    def clear_frame(self, frame):
        if frame.winfo_children():
            frame.grid_forget()


    def show_register(self):
        self.clear_content()
        self.geometry("600x750")
        self.use_gmail_var = tk.BooleanVar()

        self.progress_bar = ctk.CTkProgressBar(self, orientation="horizontal",progress_color="light blue")   # Use default style for input fields
        self.progress_bar.step()
        self.progress_bar.pack(pady=5)

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

        self.phone_extensions=["+1", "+44", "+91", "+33"]
        self.phone_extension_combobox = ctk.CTkComboBox(self, values=self.phone_extensions)
        self.phone_extension_combobox.pack(pady=5)
        

        self.phone_number_entry = ctk.CTkEntry(self, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.phone_number_entry.pack(pady=5)

        self.user_type_label = ctk.CTkLabel(self, text="User Type:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.user_type_label.pack(pady=5)

        user_type_values = ["Driver", "Passenger"]
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
            self.username_entry.insert(0, self.gmail_entry.get().split("@")[0])  # Set username to Gmail address
        else:
            self.username_entry.delete(0, "end")  # Clear the current username


    
    #confirm ride
    def confirm_ride(self):
        #current user details
        user_details = self.current_user_object
        user_id=user_details[0]
        total_seats = int(self.passenger_seats_combobox.get())

        #get riderid from ride details ridernam, from location, to location, date, time, available seats
        ride_details = self.current_ride_data
        riderid=list(self.controller.get_rideid_by_ridedetails(ride_details[0],ride_details[1],ride_details[2],ride_details[3],ride_details[4],ride_details[5]))[0]

        #check if user has already booked the ride

        if self.controller.check_if_already_booked(riderid,user_id):
            messagebox.showerror("Error", "You have already booked this ride")
            return

        #insert into confirm ride table
        self.controller.confirm_ride(riderid,user_id,total_seats)

        #substract seats booked from available seats
        available_seats = int(ride_details[5])
        available_seats = available_seats - total_seats

        #update available seats in rides table
        self.controller.update_available_seats(riderid,available_seats)

        #update my rides table
        self.my_rides_table.add_row([ride_details[0],ride_details[1],ride_details[2],ride_details[3],ride_details[4],total_seats])

        self.show_home_page_frame("my_rides")


        

    def sendRegisterUserData(self):
        # Get values from the user input fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gmail = self.gmail_entry.get()
        username = self.username_entry.get()
        phone_extension = self.phone_extension_combobox.get()
        phone_number = self.phone_number_entry.get()
        dob = self.dob_entry.get()

        # Check if required fields are empty
        if not first_name or not last_name or not dob:
            messagebox.showerror("Error", "First Name, Last Name, and Date of Birth are required.")
            return

        # Combine phone extension and phone number
        complete_phone_number = phone_extension +phone_number

        # Register the user (you may call your registration function here)
        # Example: self.controller.registerUser(first_name, last_name, username, complete_phone_number, dob)

        # Display a success message or handle registration result
        registration_result = self.controller.registerUser(first_name, last_name, gmail, username,complete_phone_number, dob)
        if registration_result:
            messagebox.showinfo("Success", "User registered successfully.")
        else:
            messagebox.showerror("Error", "Error registering user.")

        self.show_welcome()

    def sendOtpRequest(self):
       
        self.current_user_phone_number =  self.phone_extension_combobox.get()+self.phone_number_entry.get()
        #check if number exists in database
        self.current_user_object = self.controller.get_user_by_phone_number(self.current_user_phone_number)
        if self.current_user_object:
            #send otp to the user
            if self.current_user_phone_number == "+19803224017":
                self.controller.sendOtp(self.current_user_phone_number)
                messagebox.showinfo("Success", "OTP sent successfully.")
                return
            
            #show otp sent message
            messagebox.showinfo("Success", "OTP sent successfully.")
        else:
            messagebox.showerror("Error", "User does not exist.")
        


    def verify_login(self):
        #check if otp matches   
        self.enteredOTP=self.otp_entry.get()

        if self.controller.verifyOTP(self.enteredOTP):
            #show home page
            self.home_page()
        else:
            messagebox.showerror("Error", "OTP does not match.")
        
  
