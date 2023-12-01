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

# Method to fetch data and plot rides per day
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

    # Draw the plot on Tkinter canvas
    canvas.draw()

# Method to fetch data and plot active users
def plot_active_users():
    cursor.execute('''
        SELECT date, COUNT(userid) as num_active_users
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

    # Draw the plot on Tkinter canvas
    canvas.draw()

# Method to fetch data and plot most booked ride locations
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

    # Draw the plot on Tkinter canvas
    canvas.draw()

# Add buttons to each tab to trigger the corresponding plot
rides_button = tk.Button(tab1, text="Plot Rides per Day", command=plot_rides_per_day)
rides_button.pack()

users_button = tk.Button(tab2, text="Plot Active Users", command=plot_active_users)
users_button.pack()

locations_button = tk.Button(tab3, text="Plot Most Booked Locations", command=plot_most_booked_locations)
locations_button.pack()

# Create Matplotlib canvas
canvas = FigureCanvasTkAgg(figure, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the Tkinter main loop
app.mainloop()

# Close the database connection after the application is closed
connection.close()
