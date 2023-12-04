import tkinter as tk
from tkinter import ttk
import mysql.connector
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Database credentials
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'letsride',
    'port': 3306
}

# Create a connection to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create the Tkinter app
app = tk.Tk()
app.title("Ride Data Analysis")

# Matplotlib figure for plotting
figure = Figure(figsize=(5, 4), dpi=100)

# Create tabs
tab_control = ttk.Notebook(app)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Rides per Day')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Active Users')

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Most Booked Locations')

tab_control.pack(expand=1, fill='both')

# Method to fetch data and return rides per day plot
def plot_rides_per_day():
    cursor.execute('''
        SELECT date, COUNT(rideid) as num_rides
        FROM rides
        GROUP BY date;
    ''')
    data = cursor.fetchall()

    dates, num_rides = zip(*data)

    # Clear previous plot
    figure.clear()

    # Create a new subplot
    ax = figure.add_subplot(111)

    # Plot the data
    ax.bar(dates, num_rides)

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Rides')
    ax.set_title('Number of Rides Per Day')

    return figure

# Method to fetch data and return active users plot
def plot_active_users():
    cursor.execute('''
        SELECT date, COUNT(driverid) as num_active_users
        FROM rides
        GROUP BY date;
    ''')
    data = cursor.fetchall()

    dates, num_active_users = zip(*data)

    # Clear previous plot
    figure.clear()

    # Create a new subplot
    ax = figure.add_subplot(111)

    # Plot the data
    ax.bar(dates, num_active_users)

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Active Users')
    ax.set_title('Number of Active Users Per Day')

    return figure

# Method to fetch data and return most booked ride locations plot
def plot_most_booked_locations():
    cursor.execute('''
        SELECT location, COUNT(rideid) as num_bookings
        FROM locations
        JOIN stops ON locations.locationid = stops.location1_id
        GROUP BY location
        ORDER BY num_bookings DESC
        LIMIT 5;
    ''')
    data = cursor.fetchall()

    locations, num_bookings = zip(*data)

    # Clear previous plot
    figure.clear()

    # Create a new subplot
    ax = figure.add_subplot(111)

    # Plot the data
    ax.bar(locations, num_bookings)

    # Set labels and title
    ax.set_xlabel('Location')
    ax.set_ylabel('Number of Bookings')
    ax.set_title('Most Booked Ride Locations')

    return figure

# Add buttons to each tab to trigger the corresponding plot
def display_plot(plot_function):
    global canvas  # Declare canvas as global
    # Get the plot from the function
    plot = plot_function()

    # Clear previous plot on Tkinter canvas
    if 'canvas' in globals():
        canvas.get_tk_widget().destroy()

    # Create Matplotlib canvas with the new plot
    canvas = FigureCanvasTkAgg(plot, master=app)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

rides_button = tk.Button(tab1, text="Plot Rides per Day", command=lambda: display_plot(plot_rides_per_day))
rides_button.pack()

users_button = tk.Button(tab2, text="Plot Active Users", command=lambda: display_plot(plot_active_users))
users_button.pack()

locations_button = tk.Button(tab3, text="Plot Most Booked Locations", command=lambda: display_plot(plot_most_booked_locations))
locations_button.pack()

# Run the Tkinter main loop
app.mainloop()

# Close the database connection after the application is closed
connection.close()
