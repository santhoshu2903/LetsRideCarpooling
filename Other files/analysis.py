import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

class RideSharingAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ride-Sharing Analysis")

        self.create_widgets()

    def create_widgets(self):
        # Button to show the number of rides over time
        button_rides_over_time = ttk.Button(self.root, text="Rides Over Time", command=self.show_rides_over_time)
        button_rides_over_time.pack(pady=10)

        # Button to show popular routes
        button_popular_routes = ttk.Button(self.root, text="Popular Routes", command=self.show_popular_routes)
        button_popular_routes.pack(pady=10)

    def show_rides_over_time(self):
        # Simulate data retrieval from the database
        dates = ["2023-01-01", "2023-01-02", "2023-01-03"]
        ride_counts = [random.randint(10, 30) for _ in range(len(dates))]

        self.show_bar_chart(dates, ride_counts, 'Number of Rides Over Time', 'Date', 'Number of Rides')

    def show_popular_routes(self):
        # Simulate data retrieval from the database
        routes = ["Route A", "Route B", "Route C"]
        ride_counts = [random.randint(5, 20) for _ in range(len(routes))]

        self.show_bar_chart(routes, ride_counts, 'Popular Routes', 'Route', 'Number of Rides')

    def show_bar_chart(self, x_data, y_data, title, x_label, y_label):
        fig, ax = plt.subplots()
        ax.bar(x_data, y_data)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = RideSharingAnalysisApp(root)
    root.mainloop()
