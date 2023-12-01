from datetime import datetime
import itertools
import tkinter as tk
from tkinter import messagebox
# import ttkbootstrap as tb
import customtkinter as ctk
import Controller
import CTkTable  as ctkTable
from CTkTableRowSelector import *
import os
from fpdf import FPDF
from PIL import Image, ImageTk

class View(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.frame = {}
        self.title("Let's Go Ride with US")
        # self.iconphoto(False, tk.PhotoImdsage(file='images/icon.jpg'))
        self.controller = Controller.Controller()
        self.pull_table_data()
        self.show_welcome()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
        #configure all buttons to Century Gothic
        # ctk.set_default_font("Century Gothic")


    def pull_table_data(self):
        #store all table data into seperate lists
        self.rides_table_data = []
        self.confirmed_rides_table_data = []
        self.users_table_data = []
        self.locations_table_data = []

        self.rides_table_data= self.controller.get_all_rides()
        self.confirmed_rides_table_data = self.controller.get_all_confirmed_rides()
        self.users_table_data = self.controller.get_all_users()
        self.locations_table_data = self.controller.get_all_locations()

        self.display_rides_data = []

        self.temp_rides_data = []
        for ride in self.rides_table_data:
            driver_name = ride[2]
            from_location = self.controller.get_location_by_locationid(ride[3])
            to_location = self.controller.get_location_by_locationid(ride[4])
            date =ride[5]
            #convert date to string
            date = date.strftime("%m/%d/%Y")
            time = self.controller.convert_time(ride[6])
            self.temp_rides_data.append([ride[0],ride[1],driver_name,from_location,to_location,date,time,ride[7]])
        self.display_rides_data = self.temp_rides_data

        try:
            self.temp_confirmed_rides_data = []
            for ride in self.confirmed_rides_table_data:
                if self.current_user_object[0] == ride[2]:
                    ride_details = self.controller.get_ride_by_rideid(ride[1])
                    user_details = self.controller.get_User_by_userid(ride[2])
                    driver_name = ride_details[2]
                    from_location = self.controller.get_location_by_locationid(ride_details[3])
                    to_location = self.controller.get_location_by_locationid(ride_details[4])
                    date =ride_details[5]
                    #convert date to string
                    date = date.strftime("%m/%d/%Y")
                    time = self.controller.convert_time(ride_details[6])
                    self.temp_confirmed_rides_data.append([driver_name,from_location,to_location,date,time,ride[3]])

            
            self.display_confirmed_rides_data = self.temp_confirmed_rides_data 
        except:
            pass





    def show_welcome(self):
        self.clear_content()
        self.geometry("1050x700")


        #display image
        self.image = ctk.CTkImage(light_image=Image.open("images/welcome.jpg"),dark_image=Image.open("images/welcome.jpg"),size=(1050,700))
        self.image_label = ctk.CTkLabel(self, image=self.image,text="")
        self.image_label.place(x=0,y=0)

        
        self.show_welcome_frame = ctk.CTkFrame(self)
        self.show_welcome_frame.pack()

        self.ctk_label = ctk.CTkLabel(self.show_welcome_frame,text="Welcome to the App!",bg_color="transparent", font=("Helvetica", 20, "bold"))
        self.ctk_label.pack(pady=40)

        # self.login_button = ctk.CTkButton(self, text="Login", command=self.show_login)
        self.login_button = ctk.CTkButton(self.show_welcome_frame, text="Login", command=self.show_login)
        self.login_button.pack(pady=20)

        self.register_button = ctk.CTkButton(self.show_welcome_frame, text="Register", command=self.show_register)
        self.register_button.pack(pady=10)


    def show_login(self):
        self.clear_content()
        self.geometry("1050x700")

        #welcome image1
        self.image = ctk.CTkImage(light_image=Image.open("images/welcome2.jpg"),dark_image=Image.open("images/welcome2.jpg"),size=(1050,700))
        self.image_label = ctk.CTkLabel(self, image=self.image,text="")
        self.image_label.place(x=0,y=0)


        #radio button frame
        self.radio_button_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.radio_button_frame.pack(pady=10)

        #login as radio buttons Drivers as Passengers side by side
        self.login_as = tk.StringVar()
        self.login_as.set("Passenger")
        self.driver_radio_button = ctk.CTkRadioButton(self.radio_button_frame, text="Driver", variable=self.login_as, value="Driver")
        self.driver_radio_button.pack(side="left", pady=10)

        self.passenger_radio_button = ctk.CTkRadioButton(self.radio_button_frame, text="Passenger", variable=self.login_as, value="Passenger")
        self.passenger_radio_button.pack(side="left", pady=10)
        

        #login frame
        self.login_frame = ctk.CTkFrame(self, fg_color="red", corner_radius=0)
        self.login_frame.pack(pady=10)


        phone_extensions = ["+1", "+44", "+91", "+33"]
        self.phone_extension_combobox = ctk.CTkComboBox(self.login_frame, values=phone_extensions)
        self.phone_extension_combobox.pack(pady=10)


        self.phone_number_label = ctk.CTkLabel(self.login_frame, text="Phone Number:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.phone_number_label.pack(pady=10)

        self.phone_number_entry = ctk.CTkEntry(self.login_frame, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.phone_number_entry.pack(pady=10)

        self.otp_label = ctk.CTkLabel(self.login_frame, text="OTP:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.otp_label.pack(pady=10)

        self.otp_entry = ctk.CTkEntry(self.login_frame, fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.otp_entry.pack(pady=10)


        self.send_otp_button = ctk.CTkButton(self.login_frame, text="Send OTP", command=self.sendOtpRequest)
        self.send_otp_button.pack(pady=10)

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.verify_login)
        self.login_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self.login_frame, text="Back", command=self.show_welcome)
        self.back_button.pack(pady=10)


    def show_home_page_frame(self,frame_name):

        #hide all frames    
        for frame in self.frame.values():
            frame.grid_forget()

        #show selected frame
        self.dashboard_button.configure(fg_color=("dodger blue") if frame_name == "dashboard" else "transparent")
        self.search_for_ride_button.configure(fg_color=("dodger blue") if frame_name == "search_for_ride" or frame_name=="confirm_ride" else "transparent")
        self.give_ride_button.configure(fg_color=("dodger blue") if frame_name == "give_ride" or frame_name=="passenger_details" else "transparent")
        self.my_rides_button.configure(fg_color=("dodger blue") if frame_name == "my_rides" else "transparent")
        self.feedback_button.configure(fg_color=("dodger blue") if frame_name == "feedback" else "transparent")

        self.frame[frame_name].grid(row=0, column=1, sticky="nsew")

    #admin page
    def admin_page(self):
        self.clear_content()
        self.geometry("1050x700")

        # #set grid layout
        # self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #welcome admin message
        self.welcome_admin_label = ctk.CTkLabel(self, text="Welcome Admin", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.welcome_admin_label.grid(row=0, column=0,columnspan=3, sticky="nsew", padx=10, pady=10)

        #dashboard reports notebook
        self.notebook = ctk.CTkTabview(self)
        self.notebook.grid(row=1, column=0,columnspan=4, sticky="nsew")

        #add tabs
        self.notebook.add("Analytical Reports")
        self.notebook.add("PDF Reports")


        #notebook inside pdf reports tab
        self.pdf_reports_notebook = ctk.CTkTabview(self.notebook.tab("PDF Reports"))  
        self.pdf_reports_notebook.grid(row=0, column=0, sticky="nsew")

        #add tabs   
        self.pdf_reports_notebook.add("Rides Reports")
        self.pdf_reports_notebook.add("Confirmed Rides Reports")
        self.pdf_reports_notebook.add("Users Reports")

        #rides table in rides reports tab
        #rides headers
        rides_headers = [["Ride ID", "Driver Name", "From Location", "To Location", "Date", "Start Time","Available Seats"]]
        #table data
        self.rides_table_data = rides_headers

        #insert rideid, driver name, from location, to location, date, time and available seats in table_data
        for ride in self.rides_table_data:
            driver_name = self.controller.get_User_name_by_userid(ride[2])
            from_location = self.controller.get_location_by_locationid(ride[3])
            to_location = self.controller.get_location_by_locationid(ride[4])
            date =ride[5]
            #convert date to string
            date = date.strftime("%m/%d/%Y")
            time = self.controller.convert_time(ride[6])
            self.rides_table_data.append([ride[1],driver_name,from_location,to_location,date,time,ride[7]])
        #table frame
        self.rides_table_frame = ctk.CTkScrollableFrame(self.pdf_reports_notebook.tab("Rides Reports"), fg_color="transparent", corner_radius=0)
        self.rides_table_frame.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        #table
        self.rides_table= ctkTable.CTkTable(self.rides_table_frame,values=self.rides_table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.rides_table.edit_row(0,text_color="blue",hover_color="light blue")
        self.rides_table.grid(sticky="nsew", padx=10, pady=10)

        #confirmed rides table in confirmed rides reports tab
        #confirmed rides headers
        confirmed_rides_headers = [["Ride ID", "User Name", "From Location", "To Location", "Date", "Start Time","Seats Booked"]]
        #table data
        self.confirmed_rides_table_data = confirmed_rides_headers

        #get all confirmed rides
        #get rideid, userid, seats booked
        #get user name from userid
        #get ride details from rideid

        #insert rideid, user name, from location, to location, date, time and seats booked in table_data
        for ride in self.confirmed_rides_table_data():
            ride_details = self.controller.get_ride_by_rideid(ride[1])
            user_details = self.controller.get_User_by_userid(ride[2])
            from_location = self.controller.get_location_by_locationid(ride_details[3])
            to_location = self.controller.get_location_by_locationid(ride_details[4])
            date =ride_details[5]
            #convert date to string
            date = date.strftime("%m/%d/%Y")
            time = self.controller.convert_time(ride_details[6])
            self.confirmed_rides_table_data.append([ride[1],user_details[1]+" "+user_details[2],from_location,to_location,date,time,ride[3]])            

        #table frame
        self.confirmed_rides_table_frame = ctk.CTkScrollableFrame(self.pdf_reports_notebook.tab("Confirmed Rides Reports"), fg_color="transparent", corner_radius=0)
        self.confirmed_rides_table_frame.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)
        
        #table
        self.confirmed_rides_table= ctkTable.CTkTable(self.confirmed_rides_table_frame,values=self.confirmed_rides_table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.confirmed_rides_table.edit_row(0,text_color="blue",hover_color="light blue")

        self.confirmed_rides_table.grid(sticky="nsew", padx=10, pady=10)

        #users table in users reports tab
        #users headers
        users_headers = [["User ID", "First Name", "Last Name", "Phone Number", "Email"]]
        #table data
        self.users_table_data = users_headers

        #insert userid, first name, last name, phone number and email in table_data
        for user in self.controller.get_all_users():
            self.users_table_data.append([user[0],user[1],user[2],user[3],user[4]])

        #table frame
        self.users_table_frame = ctk.CTkScrollableFrame(self.pdf_reports_notebook.tab("Users Reports"), fg_color="transparent", corner_radius=0)
        self.users_table_frame.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        #table
        self.users_table= ctkTable.CTkTable(self.users_table_frame,values=self.users_table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.users_table.edit_row(0,text_color="blue",hover_color="light blue")
        self.users_table.grid(sticky="nsew", padx=10, pady=10)

        #print as pdf button in all tabs
        self.print_as_pdf_button = ctk.CTkButton(self.pdf_reports_notebook.tab("Rides Reports"), text="Print as PDF",command=self.get_all_rides_reports)
        self.print_as_pdf_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.print_as_pdf_button = ctk.CTkButton(self.pdf_reports_notebook.tab("Confirmed Rides Reports"), text="Print as PDF",command=self.get_all_confirmed_rides_reports)
        self.print_as_pdf_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.print_as_pdf_button = ctk.CTkButton(self.pdf_reports_notebook.tab("Users Reports"), text="Print as PDF",command=self.get_all_users_reports)
        self.print_as_pdf_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)




        #rides reports frame
        #logout button
        self.logout_button = ctk.CTkButton(self, text="Logout",command=self.show_welcome)
        self.logout_button.grid(row=6, column=0, sticky="nsew", padx=10, pady=10)


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
                                            anchor="w",command=lambda : self.show_home_page_frame("search_for_ride"))
        self.search_for_ride_button.grid(row=1, column=0, sticky="ew")

        
        #set create ride button
        self.give_ride_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,border_spacing=10, text="Give Ride",
                                            fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                            anchor="w",command=lambda:self.show_home_page_frame("give_ride")   )
        if self.login_as.get() == "Driver":
            self.give_ride_button.grid(row=2, column=0, sticky="ew")
        
        #set my rides button
        self.my_rides_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,border_spacing=10, text="My Rides",
                                            fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                            anchor="w",command=lambda:self.show_home_page_frame("my_rides"))
        if self.login_as.get() == "Passenger":
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

        
        #3 entries in one row , from ,to, date and time
        self.search_for_ride_search_bar_from_entry = ctk.CTkEntry(self.frame["search_for_ride"],width=150, placeholder_text="from")
        self.search_for_ride_search_bar_from_entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.search_for_ride_search_bar_to_entry = ctk.CTkEntry(self.frame["search_for_ride"],width=150, placeholder_text="to")
        self.search_for_ride_search_bar_to_entry.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.search_for_ride_search_bar_date_entry = ctk.CTkEntry(self.frame["search_for_ride"],width=150, placeholder_text="date")
        self.search_for_ride_search_bar_date_entry.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)


        #search button display corresponding data in the below table
        self.search_for_ride_search_button = ctk.CTkButton(self.frame["search_for_ride"], text="Search",command=self.search_rides)
        self.search_for_ride_search_button.grid(row=1, column=4, sticky="ne", padx=10, pady=10)

        #headers lists
        headers = [["Driver Name", "From Location", "To Location", "Date", "Start Time","Available Seats"]]

        #table data
        self.table_data = headers
        
        #insert rideid, driver name, from location, to location, date, time and available seats in table_data from display_rides
        for ride in self.display_rides_data:
            if ride[7]!=0:
                self.table_data.append([ride[2],ride[3],ride[4],ride[5],ride[6],ride[7]])

    
        #table frame
        self.search_for_ride_table_frame = ctk.CTkScrollableFrame(self.frame["search_for_ride"], fg_color="transparent", corner_radius=0,width=1000,height=400)
        self.search_for_ride_table_frame.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)


        #table 
        self.search_for_ride_table= ctkTable.CTkTable(self.search_for_ride_table_frame,values=self.table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.search_for_ride_table.edit_row(0,text_color="blue",hover_color="light blue")
        self.search_for_ride_table.grid(sticky="nsew", padx=10, pady=10)

        self.search_for_ride_table_selector = CTkTableRowSelector(self.search_for_ride_table)

        #confirm ride button on selected row redirects to new frame within search for ride frame
        #confirm ride frame as frame["confirm_ride"]
        if self.login_as.get() == "Passenger":
            self.search_for_ride_confirm_ride_button = ctk.CTkButton(self.frame["search_for_ride"], text="View Ride Details",command=lambda : self.confirm_ride_page())
            self.search_for_ride_confirm_ride_button.grid(row=3, column=4, sticky="se", padx=10, pady=10)


        #search bar entries
        
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

        #ride details frame as frame["ride_details"]
        self.frame["passenger_details"] = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.frame["passenger_details"].columnconfigure(0, weight=1)
        #create ride details label
        self.ride_details_label = ctk.CTkLabel(self.frame["passenger_details"], text="Ride Details", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.ride_details_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)




        #current ride name and count of active rides
        self.current_user_name = self.current_user_object[1]+" "+self.current_user_object[2]
        self.current_user_id = self.current_user_object[0]

        #get count of rides by current user
        self.current_user_rides_count = self.controller.get_rides_count_by_driverid(self.current_user_id)

        #label to display name and count of rides
        self.current_user_name_and_rides_count_label = ctk.CTkLabel(self.frame["give_ride"], text="Welcome "+self.current_user_name+" ! You have "+str(self.current_user_rides_count[0])+" active rides", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.current_user_name_and_rides_count_label.grid(row=0, column=1, sticky="nesw", padx=10, pady=10)


        #create create ride button top right corner
        self.create_ride_button = ctk.CTkButton(self.frame["give_ride"], text="+ New Ride",command=lambda :  self.show_home_page_frame("new_ride"))
        self.create_ride_button.grid(row=0, column=4, sticky="nw", padx=10, pady=10)

        #3 entries in one row , from ,to, date and time for give ride 
        self.give_ride_search_bar_from_entry = ctk.CTkEntry(self.frame["give_ride"],width=150, placeholder_text="from")
        self.give_ride_search_bar_from_entry.grid(row=1, column=1, sticky="nesw", padx=10, pady=10)

        self.give_ride_search_bar_to_entry = ctk.CTkEntry(self.frame["give_ride"],width=150, placeholder_text="to")
        self.give_ride_search_bar_to_entry.grid(row=1, column=2, sticky="nesw", padx=10, pady=10)

        self.give_ride_search_bar_date_entry = ctk.CTkEntry(self.frame["give_ride"],width=150, placeholder_text="date")
        self.give_ride_search_bar_date_entry.grid(row=1, column=3, sticky="nesw", padx=10, pady=10)

        #search button display corresponding data in the below table
        self.give_ride_search_button = ctk.CTkButton(self.frame["give_ride"], text="Search",command=self.search_give_rides)
        self.give_ride_search_button.grid(row=1, column=4, sticky="ne", padx=10, pady=10)


        #give_ride headers
        give_ride_headers = [["Ride ID",  "From Location", "To Location", "Date", "Start Time","Available Seats"]]

        #table data
        self.give_ride_table_data = give_ride_headers
        
        #insert rider name, from location, to location, date, time in table_data
        for ride in self.display_rides_data:
            print(ride)
            if ride[1]==self.current_user_id:
                self.give_ride_table_data.append([ride[0],ride[3],ride[4],ride[5],ride[6],ride[7]])
        #table frame
        self.give_ride_table_frame = ctk.CTkScrollableFrame(self.frame["give_ride"], fg_color="transparent", corner_radius=0,width=1000,height=350)
        self.give_ride_table_frame.grid(row=3, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)

        #table 
        self.give_ride_table= ctkTable.CTkTable(self.give_ride_table_frame,values=self.give_ride_table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.give_ride_table.edit_row(0,text_color="blue",hover_color="light blue")
        # self.search_for_ride_table.columns[0].width = 100
        self.give_ride_table.grid(sticky="nsew", padx=10, pady=10)

        #create ctkrowselector for give ride table

        self.give_ride_table_selector = CTkTableRowSelector(self.give_ride_table)

        #Passenger Details button
        self.passenger_details_button = ctk.CTkButton(self.frame["give_ride"], text="Passenger Details",command=self.show_passenger_details)
        self.passenger_details_button.grid(row=4, column=2, sticky="w", padx=10, pady=10)

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

        #from locations combobox
        self.from_location_combobox = ctk.CTkComboBox(self.frame["new_ride"], values=[location[1] for location in self.locations_table_data])
        self.from_location_combobox.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        #combobox width
        self.from_location_combobox.configure(width=300)

        # self.from_location_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        # self.from_location_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10,columnspan=2)

        #create to location label and entry side by side
        self.to_location_label = ctk.CTkLabel(self.frame["new_ride"], text="To Location : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.to_location_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

                #to locations combobox
        self.to_location_combobox = ctk.CTkComboBox(self.frame["new_ride"], values=[location[1] for location in self.locations_table_data])
        self.to_location_combobox.grid(row=3, column=1, sticky="w", padx=10, pady=10)
        #combobox width
        self.to_location_combobox.configure(width=300)

        #no of stops
        self.no_of_stops_label = ctk.CTkLabel(self.frame["new_ride"], text="No of Stops : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.no_of_stops_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        #no of stops entry
        self.no_of_stops_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.no_of_stops_entry.grid(row=4, column=1, sticky="w", padx=10, pady=10)

        #keyrelease event on no of stops entry
        self.no_of_stops_entry.bind("<KeyRelease>", self.no_of_stops_entry_keyrelease)




        # self.to_location_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        # self.to_location_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        # #create date label and entry side by side
        self.date_label = ctk.CTkLabel(self.frame["new_ride"], text="Date : ",fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.date_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

        # self.date_entry =DateEntry(self.frame["new_ride"], date_pattern="MM/dd/yyyy", font=("Arial", 15))
        # self.date_entry.grid(row=4, column=1, sticky="w", padx=10, pady=10)

        self.date_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent",placeholder_text="MM/DD/YYYY",  font=("Helvetica", 14, "bold"),width=300)
        self.date_entry.grid(row=5, column=1, sticky="w", padx=10, pady=10)

        #create time label and entry side by side
        self.time_label = ctk.CTkLabel(self.frame["new_ride"], text=" Start Time : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.time_label.grid(row=6, column=0, sticky="e", padx=10, pady=10)

        self.time_entry = ctk.CTkEntry(self.frame["new_ride"],placeholder_text="HH:MM AM/PM", fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.time_entry.grid(row=6, column=1, sticky="w", padx=10, pady=10)

        #crate available seats label and entry side by side
        self.available_seats_label = ctk.CTkLabel(self.frame["new_ride"], text="Available Seats : ", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.available_seats_label.grid(row=7, column=0, sticky="e", padx=10, pady=10)

        self.available_seats_entry = ctk.CTkEntry(self.frame["new_ride"], fg_color="transparent", font=("Helvetica", 14, "bold"),width=300)
        self.available_seats_entry.grid(row=7, column=1, sticky="w", padx=10, pady=10)

        #create submit button
        self.submit_button = ctk.CTkButton(self.frame["new_ride"], text="Submit",command=self.send_ride_data)
        self.submit_button.grid(row=8, column=1, sticky="w", padx=10, pady=10)

        #create back button to create rides frame  
        self.back_button = ctk.CTkButton(self.frame["new_ride"], text="Back",command=lambda :  self.show_home_page_frame("give_ride"))
        self.back_button.grid(row=9, column=1, sticky="w", padx=10, pady=10)

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
        print(self.display_confirmed_rides_data)
        for ride in self.display_confirmed_rides_data:
            self.my_rides_table_data.append([ride[0],ride[1],ride[2],ride[3],ride[4],ride[5]])
        #table frame
        self.my_rides_table_frame = ctk.CTkScrollableFrame(self.frame["my_rides"], fg_color="transparent", corner_radius=0)
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

    #show_passenger_details
    def show_passenger_details(self):

        #now fill give ride frame with passenger details table of selected ride
        #get rideid from selected row
        self.selected_rideid = self.give_ride_table_selector.get()[0][0]

        ride_details = self.controller.get_ride_by_rideid(self.selected_rideid)

        confirmed_rides_data = self.controller.get_all_confirmed_rides_by_rideid(self.selected_rideid)

        self.show_home_page_frame("passenger_details")

        #create passenger details table headers
        passenger_details_headers = [["Passenger Name", "Gmail","Phone Number","Seats Booked"]]

        #create passenger details table data
        passenger_details_table_data = passenger_details_headers

        #insert passenger name, gmail, phone number and seats booked in table_data
        for ride in confirmed_rides_data:
            user_details = self.controller.get_User_by_userid(ride[2])
            passenger_details_table_data.append([user_details[1]+" "+user_details[2],user_details[3],user_details[6],ride[3]])

        #table frame
        self.passenger_details_table_frame = ctk.CTkScrollableFrame(self.frame["passenger_details"], fg_color="transparent", corner_radius=0)
        self.passenger_details_table_frame.grid(row=3, column=0,columnspan=6, sticky="nsew", padx=10, pady=10)

        #table
        self.passenger_details_table= ctkTable.CTkTable(self.passenger_details_table_frame,values=passenger_details_table_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.passenger_details_table.edit_row(0,text_color="blue",hover_color="light blue")

        self.passenger_details_table.grid(sticky="nsew", padx=10, pady=10)

        #create back button to dashboard frame
        self.back_button = ctk.CTkButton(self.frame["passenger_details"], text="Back",command=lambda: self.show_home_page_frame("give_ride"))
        self.back_button.grid(row=4, column=0, sticky="w", padx=10, pady=10)



        

    def confirm_ride_page(self):
        #get index ctktable row selector
        self.current_ride_data = self.search_for_ride_table_selector.get()
        print(self.current_ride_data)
     
        user_details = self.current_user_object

        # print(self.current_ride_data)
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
        
        # print(available_seats)
        available_seats = [str(i) for i in range(1,available_seats+1)]

        self.passenger_seats_combobox = ctk.CTkComboBox(self.frame["confirm_ride"], values=available_seats)
        self.passenger_seats_combobox.grid(row=6, column=1, sticky="w", padx=10, pady=10)

        
        self.current_ride_data = self.convert_ride_data(self.current_ride_data)

        #get ride id from current ride data
        self.current_ride_id = self.controller.get_ride_id_by_drivername_from_location_to_location_date_time_available_seats(self.current_ride_data[0],self.current_ride_data[1],self.current_ride_data[2],self.current_ride_data[3],self.current_ride_data[4],self.current_ride_data[5])
        print(self.current_ride_id)

        #passenger confirm button
        self.passenger_confirm_button = ctk.CTkButton(self.frame["confirm_ride"], text="Confirm",command=self.confirm_ride)
        self.passenger_confirm_button.grid(row=7, column=1, sticky="w", padx=10, pady=10)

        #passenger back button to search for ride frame
        self.passenger_back_button = ctk.CTkButton(self.frame["confirm_ride"], text="Back",command=lambda : self.show_home_page_frame("search_for_ride"))
        self.passenger_back_button.grid(row=8, column=1, sticky="w", padx=10, pady=10)


    #convert_ride_data
    def convert_ride_data(self,ride_data):
        ride_data[1]=self.controller.get_locationid_by_locationname(ride_data[1])
        ride_data[2]=self.controller.get_locationid_by_locationname(ride_data[2])
        #convert string to date
        ride_data[3] = datetime.strptime(ride_data[3], '%m/%d/%Y').date()
        #convert strng to time
        ride_data[4] = datetime.strptime(ride_data[4], '%I:%M %p').time()
        return ride_data

    #no_of_stops_entry_keyrelease
    def no_of_stops_entry_keyrelease(self,event):
        #open a new window to enter stops
        #get no of stops from no_of_stops_entry
        no_of_stops = self.no_of_stops_entry.get()
        print(no_of_stops)
        #check if no of stops is empty
        if int(no_of_stops) == 0:
            return
        #open a new window
        self.new_window = tk.Toplevel(self)
        self.new_window.geometry("1000x700")
        stops_label=["First Stop","Second Stop","Third Stop"]
        self.add_stops_label = ctk.CTkLabel(self.new_window, text="Add Stops in Order", fg_color="transparent", font=("Helvetica", 20, "bold"))
        self.add_stops_label.grid(row=0, column=0,columnspan=2, sticky="w", padx=10, pady=10)
        if int(no_of_stops) >= 1:
            #locations combobox
            self.stop_name_label1 = ctk.CTkLabel(self.new_window, text=stops_label[0], fg_color="transparent", font=("Helvetica", 14, "bold"))
            self.stop_name_label1.grid(row=1, column=0, sticky="e", padx=10, pady=10)

            self.stop_name_combobox1 = ctk.CTkComboBox(self.new_window, values=[location[1] for location in self.locations_table_data])
            self.stop_name_combobox1.grid(row=1, column=1, sticky="w", padx=10, pady=10)
            #combobox width
            self.stop_name_combobox1.configure(width=300)

        if int(no_of_stops) >= 2:
            self.stop_name_label2 = ctk.CTkLabel(self.new_window, text=stops_label[1], fg_color="transparent", font=("Helvetica", 14, "bold"))
            self.stop_name_label2.grid(row=2, column=0, sticky="e", padx=10, pady=10)

            self.stop_name_combobox2 = ctk.CTkComboBox(self.new_window, values=[location[1] for location in self.locations_table_data])
            self.stop_name_combobox2.grid(row=2, column=1, sticky="w", padx=10, pady=10)
            #combobox width
            self.stop_name_combobox2.configure(width=300)

        if int(no_of_stops) == 3:
            self.stop_name_label3 = ctk.CTkLabel(self.new_window, text=stops_label[2], fg_color="transparent", font=("Helvetica", 14, "bold"))
            self.stop_name_label3.grid(row=3, column=0, sticky="e", padx=10, pady=10)

            self.stop_name_combobox3 = ctk.CTkComboBox(self.new_window, values=[location[1] for location in self.locations_table_data])
            self.stop_name_combobox3.grid(row=3, column=1, sticky="w", padx=10, pady=10)
            #combobox width
            self.stop_name_combobox3.configure(width=300)

        
        #Add stops button
        self.add_stops_button = ctk.CTkButton(self.new_window, text="Add Stops",command=self.add_stops)
        self.add_stops_button.grid(row=int(no_of_stops)+2, column=1, sticky="w", padx=10, pady=10)

        #back button
        self.back_button = ctk.CTkButton(self.new_window, text="Back",command=self.new_window.destroy)
        self.back_button.grid(row=int(no_of_stops)+2, column=0, sticky="w", padx=10, pady=10)


    #add_stops
    def add_stops(self):
        #get stops from comboboxs insert into stops list
        stops=[]
        if int(self.no_of_stops_entry.get()) >= 1:
            stops.append(self.stop_name_combobox1.get())
        if int(self.no_of_stops_entry.get()) >= 2:
            stops.append(self.stop_name_combobox2.get())
        if int(self.no_of_stops_entry.get()) == 3:
            stops.append(self.stop_name_combobox3.get())
        #insert stops 
        self.stops= stops

        print(self.stops)
        # print(self.stops)
        #destroy new window
        self.new_window.destroy()



    #send ride data to controller
    def send_ride_data(self):
        #get data from new ride frame
        driverid = self.current_user_object[0]
        driver_name = self.driver_name_entry.get()
        from_location = self.from_location_combobox.get()
        to_location = self.to_location_combobox.get()
        date = self.date_entry.get()
        #convert to date
        date = datetime.strptime(date, '%m/%d/%Y').date()
        time = self.time_entry.get()
        #convert to time format is HH:MM AM/PM
        time = datetime.strptime(time, '%I:%M %p').time()
        available_seats = self.available_seats_entry.get()

        self.date_entry.delete(0, "end")
        self.time_entry.delete(0, "end")
        self.available_seats_entry.delete(0, "end")

        from_location_id = self.controller.get_locationid_by_locationname(from_location)
        to_location_id = self.controller.get_locationid_by_locationname(to_location)
        
        # print(driverid,driver_name, from_location_id, to_location_id, date, time,available_seats)

        try:
            if self.stops:
                self.stops=[self.controller.get_locationid_by_locationname(stop) for stop in self.stops]
        except:
            self.stops=[]
        
        
        #send data to controller
        new_ride=self.controller.add_ride(driverid,driver_name, from_location_id, to_location_id, date, time,available_seats,connecting=False)
        if new_ride:
            print(new_ride)
            from_location = self.controller.get_location_by_locationid(new_ride[3])
            to_location = self.controller.get_location_by_locationid(new_ride[4])
            date =new_ride[5]
            #convert date to string
            date = date.strftime("%m/%d/%Y")
            time=self.controller.convert_time(new_ride[6])
            #insert new ride in give ride table
            self.give_ride_table.add_row([new_ride[1],from_location,to_location,date,time,new_ride[7]])
            #insert new ride in search for ride table
            self.search_for_ride_table.add_row([new_ride[2],from_location,to_location,date,time,new_ride[7]])
            #stop paths
            paths=[from_location_id]+self.stops+[to_location_id]  

            #get all combinations of paths
            paths_combinations=self.path_combinations(paths)



            #add stops in database
            self.controller.add_stops(new_ride[0],paths)
            
            
            for path in paths_combinations:
                if path[0]==new_ride[3] and path[-1]==new_ride[4]:
                    continue
                ride = self.controller.add_ride(new_ride[1],new_ride[2],path[0],path[1],new_ride[5],new_ride[6],new_ride[7],True,new_ride[0])
                
                from_location = self.controller.get_location_by_locationid(ride[3])
                to_location = self.controller.get_location_by_locationid(ride[4])
                date =ride[5]
                #convert date to string
                date = date.strftime("%m/%d/%Y")
                time=self.controller.convert_time(ride[6])
                #insert new ride in give ride table
                self.give_ride_table.add_row([ride[1],from_location,to_location,date,time,ride[7]])
                #insert new ride in search for ride table
                self.search_for_ride_table.add_row([ride[2],from_location,to_location,date,time,ride[7]])
    

        #show my rides frameyYY
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

        self.dob_label = ctk.CTkLabel(self, text="Date of Birth:", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.dob_label.pack(pady=5)

        self.dob_entry = ctk.CTkEntry(self, placeholder_text="mm/dd/yyyy", fg_color="transparent", font=("Helvetica", 14, "bold"))
        self.dob_entry.pack(pady=5)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.sendRegisterUserData)
        self.register_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.show_welcome)
        self.back_button.pack(pady=5)

    #path_combinations
    def path_combinations(self,paths):
        #2 set combinations of paths
        return list(itertools.combinations(paths, 2))
        # print(paths_combinations

    #get_all_confirmed_rides_report
    #get all confirmed rides from database and create a pdf report
    def get_all_confirmed_rides_reports(self):
            
            #get all confirmed rides data
            all_confirmed_rides_data = self.confirmed_rides_table_data()
    
            #create pdf
            pdf = FPDF(orientation='L')
            pdf.add_page()
            pdf.set_font("Arial", size=12)
    
            #add title to page
            pdf.cell(200, 10, txt="All Confirmed Rides Report", ln=1, align="C")
    
            #add header to table
            pdf.cell(30, 10, txt="Ride ID", border=1)
            pdf.cell(50, 10, txt="Driver Name", border=1)
            pdf.cell(50, 10, txt="Passenger Name", border=1)
            pdf.cell(50, 10, txt="From Location", border=1)
            pdf.cell(50, 10, txt="To Location", border=1)
            pdf.cell(30, 10, txt="Date", border=1)
            pdf.cell(30, 10, txt="Time", border=1)
            pdf.cell(30, 10, txt="Seats Booked", border=1)
            pdf.ln()
    
            #add ride data to table
            for ride in all_confirmed_rides_data:
                ride_details = self.controller.get_ride_by_rideid(ride[1])
                ride_id = ride_details[0]
                driver_name = ride_details[2]
                user_details = self.controller.get_user_by_userid(ride[2])
                passenger_name = user_details[1] + " " + user_details[2]
                from_location = ride_details[3]
                to_location = ride_details[4]
                date = ride_details[5]
                time = ride_details[6]
                seats_booked = ride[3]

                pdf.cell(30, 10, txt=str(ride_id), border=1)
                pdf.cell(50, 10, txt=driver_name, border=1)
                pdf.cell(50, 10, txt=passenger_name, border=1)
                pdf.cell(50, 10, txt=from_location, border=1)
                pdf.cell(50, 10, txt=to_location, border=1)
                pdf.cell(30, 10, txt=date, border=1)
                pdf.cell(30, 10, txt=time, border=1)
                pdf.cell(30, 10, txt=str(seats_booked), border=1)

                pdf.ln()

            #save pdf
            pdf.output("all_confirmed_rides_report.pdf")

            #show success message
            messagebox.showinfo("Success", "All Confirmed Rides Report Generated Successfully")

            #show location of pdf
            messagebox.showinfo("Success", "All Confirmed Rides Report Generated Successfully at "+os.getcwd())

    #search_give_rides
    #search rides based on from location, to location and date
    def search_give_rides(self):
        # print("reached")
        #get data from search for ride frame
        try:
            from_location = self.give_ride_search_bar_from_entry.get()
        except:
            from_location = ""
        try: 
            to_location = self.give_ride_search_bar_to_entry.get()
        except:
            to_location = ""
        try:
            date = self.give_ride_search_bar_date_entry.get()
            date = datetime.strptime(date, '%m/%d/%Y').date()
        except:
            date = ""
        rides = []
        #if all fields are not empty

        print(from_location,to_location,date)
        print(self.display_rides_data)
        if from_location != "" and to_location != "" and date != "":
            #get rides by from location, to location and date from display_rides_table_data
            for ride in self.display_rides_data:
                if ride[3] == from_location and ride[4] == to_location and ride[5] == date:
                    rides.append(ride)
        elif from_location != "" and to_location != "":
            for ride in self.display_rides_data:
                if ride[3] == from_location and ride[4] == to_location:
                    rides.append(ride)
        elif from_location != "" and date != "":
            for ride in self.display_rides_data:
                if ride[3] == from_location and ride[5] == date:
                    rides.append(ride)
        elif to_location != "" and date != "":
            for ride in self.display_rides_data:
                if ride[3] == to_location and ride[5] == date:
                    rides.append(ride)
        elif from_location != "":
            for ride in self.display_rides_data:
                if ride[3] == from_location:
                    rides.append(ride)
        elif to_location != "":
            for ride in self.display_rides_data:
                if ride[4] == to_location:
                    rides.append(ride)
        elif date != "":
            for ride in self.display_rides_data:
                if ride[5] == date:
                    rides.append(ride)
        else:
            rides=self.display_rides_data

        # print(rides)

        final_data=[["Ride ID", "From Location", "To Location", "Date", "Start Time","Available Seats"]]
        for ride in rides:
            final_data.append([ride[0],ride[3],ride[4],ride[5],ride[6],ride[7]])

        # #clear give ride table frame
        self.give_ride_table_frame.grid_forget()

        #table frame
        self.give_ride_table_frame = ctk.CTkScrollableFrame(self.frame["give_ride"], fg_color="transparent", corner_radius=0)
        self.give_ride_table_frame.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        #clear the give ride table
        self.give_ride_table= ctkTable.CTkTable(self.give_ride_table_frame,values=final_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.give_ride_table.edit_row(0,text_color="blue",hover_color="light blue")
        self.give_ride_table.grid(sticky="nsew", padx=10, pady=10)

        #add ctktable row selector
        self.give_ride_table_selector = CTkTableRowSelector(self.give_ride_table)





    #search_rides
    #search rides based on from location, to location and date
    def search_rides(self):
        # print("reached")
        #get data from search for ride frame
        try:
            from_location = self.search_for_ride_search_bar_from_entry.get()
        except:
            from_location = ""
        try: 
            to_location = self.search_for_ride_search_bar_to_entry.get()
        except:
            to_location = ""
        try:
            date = self.search_for_ride_search_bar_date_entry.get()
            date = datetime.strptime(date, '%m/%d/%Y').date()
        except:
            date = ""
        rides = []
        #if all fields are not empty

        print(from_location,to_location,date)
        print(self.display_rides_data)
        if from_location != "" and to_location != "" and date != "":
            #get rides by from location, to location and date from display_rides_table_data
            for ride in self.display_rides_data:
                if ride[3] == from_location and ride[4] == to_location and ride[5] == date:
                    rides.append(ride)
        elif from_location != "" and to_location != "":
            for ride in self.display_rides_data:
                if ride[3] == from_location and ride[4] == to_location:
                    print("given","from location",ride[3],"to location",ride[4])
                    rides.append(ride)
        elif from_location != "" and date != "":
            for ride in self.display_rides_data:
                if ride[3] == from_location and ride[5] == date:
                    print("given","from location",ride[3],"date",ride[5])
                    rides.append(ride)
        elif to_location != "" and date != "":
            for ride in self.display_rides_data:
                if ride[4] == to_location and ride[5] == date:
                    print("given","to location",ride[4],"date",ride[5])
                    rides.append(ride)
        elif from_location != "":
            for ride in self.display_rides_data:
                print(from_location,ride[3])
                if ride[3] == from_location:
                    print("given","from location",ride[3])
                    rides.append(ride)
        elif to_location != "":
            for ride in self.display_rides_data:
                if ride[4] == to_location:
                    print("given","to location",ride[4])
                    rides.append(ride)
        elif date != "":
            for ride in self.display_rides_data:
                if ride[5] == date:
                    print("given","date",ride[5])
                    rides.append(ride)
        else:
            rides=self.display_rides_data

        # print(rides)

        final_data=[["Driver Name", "From Location", "To Location", "Date", "Start Time","Available Seats"]]
        for ride in rides:
            final_data+=[[ride[2],ride[3],ride[4],ride[5],ride[6],ride[7]]]

        print(final_data)

        # print(final_data)

        # clear search for ride table frame
        self.search_for_ride_table_frame.grid_forget()

        #table frame
        self.search_for_ride_table_frame = ctk.CTkScrollableFrame(self.frame["search_for_ride"], fg_color="transparent", corner_radius=0)
        self.search_for_ride_table_frame.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        #clear the search for ride table
        self.search_for_ride_table= ctkTable.CTkTable(self.search_for_ride_table_frame,values=final_data,colors=["SkyBlue1","SkyBlue2"],header_color="white")
        self.search_for_ride_table.edit_row(0,text_color="blue",hover_color="light blue")
        self.search_for_ride_table.grid(sticky="nsew", padx=10, pady=10)

        #add ctktable row selector
        self.search_for_ride_table_selector = CTkTableRowSelector(self.search_for_ride_table)





    #get_all_rides_reports
    #get all rides from database and create a pdf report
    def get_all_rides_reports(self):

        #get all rides data
        all_rides_data = self.rides_table_data

        #create pdf
        # pdf = FPDF()
        # pdf.add_page()
        pdf = FPDF(orientation='L')
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        #add title to page
        pdf.cell(200, 10, txt="All Rides Report", ln=1, align="C")

        #add header to table
        pdf.cell(30, 10, txt="Ride ID", border=1)
        pdf.cell(50, 10, txt="Driver Name", border=1)
        pdf.cell(50, 10, txt="From Location", border=1)
        pdf.cell(50, 10, txt="To Location", border=1)
        pdf.cell(30, 10, txt="Date", border=1)
        pdf.cell(30, 10, txt="Time", border=1)
        pdf.cell(30, 10, txt="Available Seats", border=1)
        pdf.ln()

        #add ride data to table
        for ride in all_rides_data:
            ride_id = ride[0]
            driver_name = ride[2]
            from_location = ride[3]
            to_location = ride[4]
            date = ride[5]
            time = ride[6]
            available_seats = ride[7]

            pdf.cell(30, 10, txt=str(ride_id), border=1)
            pdf.cell(50, 10, txt=driver_name, border=1)
            pdf.cell(50, 10, txt=from_location, border=1)
            pdf.cell(50, 10, txt=to_location, border=1)
            pdf.cell(30, 10, txt=date, border=1)
            pdf.cell(30, 10, txt=time, border=1)
            pdf.cell(30, 10, txt=str(available_seats), border=1)
    
            pdf.ln()


        #save pdf
        pdf.output("all_rides_report.pdf")
        
        #show success message
        messagebox.showinfo("Success", "All Rides Report Generated Successfully")
        #show location of pdf
        messagebox.showinfo("Success", "All Rides Report Generated Successfully at "+os.getcwd())

    #create_pairs
    #create pairs of stops
    def create_pairs(self, stops):
        pairs = []
        for i in range(len(stops) - 1):
            pair = [stops[i], stops[i + 1]]
            pairs.append(pair)
        return pairs

    #get_all_users_report
    #get all users from database and create a pdf report
    def get_all_users_reports(self):
        # Get all users data
        all_users_data = self.controller.get_all_users()

        # Create PDF
        pdf = FPDF(orientation='L')
        pdf.add_page()

        # Add a title to the page
        pdf.set_font("Arial", size=20)
        pdf.cell(200, 10, txt="Current Users Report", ln=1, align="C")

        # Add a header to the table
        pdf.set_font("Arial", size=12)
        pdf.cell(30, 10, txt="User ID", border=1)
        pdf.cell(50, 10, txt="Name", border=1)
        pdf.cell(50, 10, txt="Email", border=1)
        pdf.cell(30, 10, txt="Phone", border=1)
        pdf.ln()

        # Add user data to the table
        for user in all_users_data:
            user_id = user[0]
            name = user[1] + " " + user[2]
            email = user[3]
            phone = user[6]

            pdf.cell(30, 10, txt=str(user_id), border=1)
            pdf.cell(50, 10, txt=name, border=1)
            pdf.cell(50, 10, txt=email, border=1)
            pdf.cell(30, 10, txt=phone, border=1)
    
            pdf.ln()

        # Save PDF
        pdf.output("current_users_report.pdf")

        # Show success message
        messagebox.showinfo("Success", "Current Users Report Generated Successfully")

        # Show location of PDF
        messagebox.showinfo("Success", "Current Users Report Generated Successfully at "+os.getcwd())






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
        #get ride details
        ride_details = self.current_ride_data
        rideid=self.current_ride_id

        print("ride details",ride_details)

        total_seats = self.passenger_seats_combobox.get()


        if self.controller.check_if_already_booked_ride(rideid,user_id):
            messagebox.showerror("Error", "You have already booked this ride")
            return
        #insert into confirm ride table
        self.controller.confirm_ride(rideid,user_id,total_seats)
        # #update available seats in rides table
        self.controller.update_available_seats(rideid,total_seats)

        from_location = self.controller.get_location_by_locationid(ride_details[1])
        to_location = self.controller.get_location_by_locationid(ride_details[2])
        date = ride_details[3]
        #convert date to string
        date = date.strftime("%m/%d/%Y")
        time=self.controller.convert_time(ride_details[4])
        #insert new ride in give ride table
        self.give_ride_table.add_row([ride_details[0],from_location,to_location,date,time,ride_details[5]])
        #update my rides table
        self.pull_table_data()
        self.home_page()
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

        if self.phone_number_entry.get() == "admin":
            self.admin_page()
            #welcome admin message
            messagebox.showinfo("Success", "Welcome Admin")
            return
       
        self.current_user_phone_number =  self.phone_extension_combobox.get()+self.phone_number_entry.get()
        #check if number exists in database
        self.current_user_object = self.controller.get_user_by_phone_number(self.current_user_phone_number)
        self.pull_table_data()
        if self.current_user_object:
            #send otp to the user
            if self.current_user_phone_number == "+1989449043":
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
        
  
