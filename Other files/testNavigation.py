import tkinter as tk

class YourApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        
        # Create a dictionary to store references to your frames
        self.frames = {}

        # Create the navigation frame
        self.navigation_frame = tk.Frame(self.root, bg="blue")
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        
        # Create buttons in the navigation frame to switch between frames
        self.dashboard_button = tk.Button(self.navigation_frame, text="Dashboard", command=lambda: self.show_frame("dashboard"))
        self.dashboard_button.grid(row=0, column=0)

        self.search_for_ride_button = tk.Button(self.navigation_frame, text="Search for Ride", command=lambda: self.show_frame("search_for_ride"))
        self.search_for_ride_button.grid(row=1, column=0)

        self.give_ride_button = tk.Button(self.navigation_frame, text="Give Ride", command=lambda: self.show_frame("give_ride"))
        self.give_ride_button.grid(row=2, column=0)

        # Create frames for different sections
        self.frames["dashboard"] = tk.Frame(self.root)
        self.frames["search_for_ride"] = tk.Frame(self.root)
        self.frames["give_ride"] = tk.Frame(self.root)

        # Add widgets to your frames
        self.dashboard_label = tk.Label(self.frames["dashboard"], text="Dashboard")
        self.dashboard_label.pack()

        self.search_for_ride_label = tk.Label(self.frames["search_for_ride"], text="Search for Ride")
        self.search_for_ride_label.pack()

        self.give_ride_label = tk.Label(self.frames["give_ride"], text="Give Ride")
        self.give_ride_label.pack()

        # Show the default frame
        self.show_frame("dashboard")

    def show_frame(self, frame_name):
        # Hide all frames
        for frame in self.frames.values():
            frame.grid_forget()
        
        # Show the selected frame
        self.frames[frame_name].grid(row=0, column=1, sticky="nsew")

    def run(self):
        self.root.mainloop()

app = YourApp()
app.run()
