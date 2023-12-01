import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import Model
import pandas as pd  # Import Pandas
import customtkinter as ctk

class RideSharingAnalysis:
    def __init__(self, root):
        self.root = root
        self.root.title("Ride-Sharing Analysis")
        self.model = Model.Model()

        # Figure to display the plot
        self.figure = Figure(figsize=(20, 4), dpi=60)

        # Canvas to display the figure
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)

    def plot_rides_day(self):
        try:
            # Get rides data per day from model
            data = self.model.get_rides_per_day()

            if not isinstance(data, pd.DataFrame):
                # If data is not a DataFrame, attempt to convert it
                data = pd.DataFrame(data)

            if data.empty:
                # No data to plot, show a message box
                messagebox.showinfo("No Data", "No ride data available for analysis.")
                return None
            
            day, rides = zip(*data.values)

            # Clear the figure
            self.figure.clear()

            # Add subplot to the figure
            ax = self.figure.add_subplot(111)

            # Plot the data
            ax.bar(day, rides)
            # Set the title
            ax.set_title('Rides per day')

            # Set the x-label
            ax.set_xlabel('Day')

            # Set the y-label
            ax.set_ylabel('Rides')


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
                # If data is not a DataFrame, attempt to convert it
                data = pd.DataFrame(data)

            if data.empty:
                # No data to plot, show a message box
                messagebox.showinfo("No Data", "No ride data available for analysis.")
                return None
            
            location, rides = zip(*data.values)

            # Clear the figure
            self.figure.clear()

            # Add subplot to the figure
            ax = self.figure.add_subplot(111)

            # Plot the data
            ax.bar(location,rides)
            # Set the title
            ax.set_title('Most booked locations')

            # Set the x-label
            ax.set_xlabel('Location')

            # Set the y-label
            ax.set_ylabel('Rides')

            
            return self.figure

        except Exception as e:
            # Handle exceptions and show an error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return None
        
if __name__ == '__main__':
    root = ctk.CTk()
    app = RideSharingAnalysis(root)
    
    # # Attempt to plot rides per day
    # canvas = app.plot_rides_day()
    # if canvas:
    #     # If canvas is not None, pack it
    #     canvas.get_tk_widget().pack()

    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    Figure = app.most_booked_locations()
    if Figure:
        # If canvas is not None, pack it
        canvas=FigureCanvasTkAgg(Figure, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    

    root.mainloop()
