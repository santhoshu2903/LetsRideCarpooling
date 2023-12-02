import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import Model
import pandas as pd  # Import Pandas
import customtkinter as ctk

class LetsRideAnalysis:
    def __init__(self, root):
        self.root = root
        self.root.title("Ride-Sharing Analysis")
        self.model = Model.Model()

        # Figure to display the plot
        self.figure = Figure(figsize=(20, 4), dpi=60)
        # Canvas to display the figure
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)

        self.plot_rides_day()
        self.most_booked_locations()

    def plot_rides_day(self):
        try:
            # Get rides data per day from model
            data = self.model.get_rides_per_day()

            if not isinstance(data, pd.DataFrame):
                data = pd.DataFrame(data)

            if data.empty:
                messagebox.showinfo("No Data", "No ride data available for analysis.")
                return None
            
            day, rides = zip(*data.values)
            self.figure = Figure(figsize=(20, 4), dpi=60)
            # Canvas to display the figure
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)

            ax = self.figure.add_subplot(111)
            ax.bar(day, rides)
            ax.set_title('Rides per day')
            ax.set_xlabel('Day')
            ax.set_ylabel('Rides')

            self.canvas.draw()
            self.canvas.get_tk_widget().pack()

            #save as image
            self.figure.savefig('Analytical reports/Rides_per_day.png', bbox_inches='tight')

            # Return the canvas for additional use if needed
            return self.figure

        except Exception as e:
            # Handle exceptions and show an error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return None
        
    def most_booked_locations(self):
        try:
            # Get most booked locations from model
            data = self.model.get_most_booked_locations()

            if not isinstance(data, pd.DataFrame):
                data = pd.DataFrame(data)

            if data.empty:
                messagebox.showinfo("No Data", "No ride data available for analysis.")
                return None
            
            location, rides = zip(*data.values)

            self.figure = Figure(figsize=(20, 4), dpi=60)
            # Canvas to display the figure
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
            ax = self.figure.add_subplot(111)
            ax.bar(location,rides)
            # Set the title
            ax.set_title('Most booked locations')
            ax.set_xlabel('Location')
            for i, v in enumerate(rides):
                ax.text(i, v+0.5, str(v), color='blue', fontweight='bold')

            # Set the y-label
            ax.set_ylabel('Rides')

            self.canvas.draw()
            self.canvas.get_tk_widget().pack()

            #save as image
            self.figure.savefig('Analytical reports/Most_booked_locations.png', bbox_inches='tight')
            return self.figure

        except Exception as e:
            # Handle exceptions and show an error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return None

    def plot_rides_month(self):
        try:
            # Get rides data per month from model
            data = self.model.get_rides_per_month()

            if not isinstance(data, pd.DataFrame):
                data = pd.DataFrame(data)

            if data.empty:
                messagebox.showinfo("No Data", "No ride data available for analysis.")
                return None
            
            month, rides = zip(*data.values)
            self.figure.clear()

            ax = self.figure.add_subplot(111)
            ax.bar(month, rides)
            ax.set_title('Rides per month')
            ax.set_xlabel('Month')
            ax.set_ylabel('Rides')

            self.canvas.draw()
            self.canvas.get_tk_widget().pack()

            #save as image
            self.figure.savefig('Analytical reports/Rides_per_month.png', bbox_inches='tight')

            # Return the canvas for additional use if needed
            return self.figure

        except Exception as e:
            # Handle exceptions and show an error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return None

