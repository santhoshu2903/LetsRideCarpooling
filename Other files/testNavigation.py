import tkinter as tk
import customtkinter as ctk

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Let's Go Ride With Us")
        self.geometry("800x600")

        self.home_page()

    def home_page(self):

        self.clear_content()
        #set test label
        self.test_label = ctk.CTkLabel(self, text="Test", fg_color="transparent")   
        self.test_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


        self.home_page_frame = ctk.CTkFrame(self, corner_radius=0)

        # Set grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #set test label
        self.test_label = ctk.CTkLabel(self, text="Test", fg_color="transparent")
        self.test_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Set navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        #set navigation frame label
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Let's Go Ride With Us", fg_color="transparent",
                                                font=("Helvetica", 20, "bold"))
        self.navigation_frame_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Set navigation buttons
        #testlabel
        self.test_label = ctk.CTkLabel(self.navigation_frame, text="Test", fg_color="transparent")
        self.test_label.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)

        # Set dashboard button
        self.dashboard_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                              text="DashBoard",anchor="w",
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"),
                                                command=self.show_dashboard)
        self.dashboard_button.grid(row=0, column=0, sticky="ew")

        # Set search for ride button
        self.search_for_ride_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Search for Ride",anchor="w",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   command=self.show_search_for_ride)
        self.search_for_ride_button.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Set create ride button
        self.create_ride_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                text="Create Ride",
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"),
                                                anchor="w", command=self.show_create_ride)
        self.create_ride_button.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        # Set my rides button
        self.my_rides_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                             text="My Rides",anchor="w",
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             hover_color=("gray70", "gray30"),
                                             command=self.show_my_rides)
        self.my_rides_button.grid(row=3, column=0, sticky="ew", padx=10, pady=10)

        # Set feedback button
        self.feedback_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                             text="Feedback",anchor="w",
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             hover_color=("gray70", "gray30"),
                                             command=self.show_feedback)
        self.feedback_button.grid(row=4, column=0, sticky="ew", padx=10, pady=10)

        # Set dashboard frame
        self.dashboard_frame = ctk.CTkFrame(self.home_page_frame, bg_color="red", corner_radius=0)
        self.dashboard_frame.columnconfigure(0, weight=1)

        # Set dashboard label
        # self.dashboard_label = ctk.CTkLabel(self.dashboard_frame, text="Dashboard", fg_color="transparent",
        #                                      font=("Helvetica", 20, "bold"))
        # self.dashboard_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Set search for ride frame
        self.search_for_ride_frame = ctk.CTkFrame(self.home_page_frame, bg_color="green", corner_radius=0)

        # Set search for ride label
        # self.search_for_ride_label = ctk.CTkLabel(self.search_for_ride_frame, text="Search for Ride",
        #                                          fg_color="transparent", font=("Helvetica", 20, "bold"))
        # self.search_for_ride_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Set create ride frame
        self.create_ride_frame = ctk.CTkFrame(self.home_page_frame, bg_color="yellow", corner_radius=0)

        # Set create ride label
        # self.create_ride_label = ctk.CTkLabel(self.create_ride_frame, text="Create Ride", fg_color="transparent",
        #                                      font=("Helvetica", 20, "bold"))
        # self.create_ride_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Set my rides frame
        self.my_rides_frame = ctk.CTkFrame(self.home_page_frame, bg_color="purple", corner_radius=0)

        # Set my rides label
        # self.my_rides_label = ctk.CTkLabel(self.my_rides_frame, text="My Rides", fg_color="transparent",
        #                                    font=("Helvetica", 20, "bold"))
        # self.my_rides_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Set feedback frame
        self.feedback_frame = ctk.CTkFrame(self.home_page_frame, bg_color="orange", corner_radius=0)

        # Set feedback label
        # self.feedback_label = ctk.CTkLabel(self.feedback_frame, text="Feedback", fg_color="transparent",
        #                                    font=("Helvetica", 20, "bold"))
        # self.feedback_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)



        # Select default frame
        self.select_home_page_frame("dashboard")

    def show_dashboard(self):
        self.select_home_page_frame("dashboard")

    def show_search_for_ride(self):
        self.select_home_page_frame("search_for_ride")

    def show_create_ride(self):
        self.select_home_page_frame("create_ride")

    def show_my_rides(self):
        self.select_home_page_frame("my_rides")

    def show_feedback(self):
        self.select_home_page_frame("feedback")

    def select_home_page_frame(self, frame_name):
        pass
    #     self.dashboard_button.configure(fg_color=("gray75", "gray25") if frame_name == "dashboard" else "transparent")
    #     self.search_for_ride_button.configure(fg_color=("gray75", "gray25") if frame_name == "search_for_ride" else "transparent")
    #     self.create_ride_button.configure(fg_color=("gray75", "gray25") if frame_name == "create_ride" else "transparent")
    #     self.my_rides_button.configure(fg_color=("gray75", "gray25") if frame_name == "my_rides" else "transparent")
    #     self.feedback_button.configure(fg_color=("gray75", "gray25") if frame_name == "feedback" else "transparent")

    #     if frame_name == "dashboard":
    #         self.dashboard_frame.grid(row=0, column=1, sticky="nsew")
    #     else:
    #         self.dashboard_frame.grid_forget()

    #     if frame_name == "search_for_ride":
    #         self.search_for_ride_frame.grid(row=0, column=1, sticky="nsew")
    #     else:
    #         self.search_for_ride_frame.grid_forget()

    #     if frame_name == "create_ride":
    #         self.create_ride_frame.grid(row=0, column=1, sticky="nsew")
    #     else:
    #         self.create_ride_frame.grid_forget()

    #     if frame_name == "my_rides":
    #         self.my_rides_frame.grid(row=0, column=1, sticky="nsew")
    #     else:
    #         self.my_rides_frame.grid_forget()

    #     if frame_name == "feedback":
    #         self.feedback_frame.grid(row=0, column=1, sticky="nsew")
    #     else:
    #         self.feedback_frame.grid_forget()

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
