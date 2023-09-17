import tkinter as tk

# Create a window.
window = tk.Tk()

# Create a label for the username.
username_label = tk.Label(text="Username")

# Create a label for the password.
password_label = tk.Label(text="Password")

# Create a button for logging in.
login_button = tk.Button(text="Login")

# Create a function for logging in.
def login():
  # Get the username and password from the user.
  username = input("Username: ")
  password = input("Password: ")

  # Check if the username and password are correct.
  if username == "admin" and password == "password":
    print("Login successful!")
  else:
    print("Login failed!")

# Bind the button to the function.
login_button.config(command=login)

# Show the window.
window.mainloop()
