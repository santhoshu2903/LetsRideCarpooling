# main.py

import os
import tkinter as tk
from tkinter import ttk
from MVC.controller import UserController
from MVC.model import UserModel
from MVC.view import WelcomeWindow

DATABASE_DIR = os.path.join(os.getcwd(), "Database")
RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")

def main():
    model = UserModel(RIDERS_DB)  # You can choose RIDERS_DB or PASSENGERS_DB
    model.init_db()

    root = tk.Tk()
    app = WelcomeWindow(controller=UserController(model, app))  # Pass the controller to the view
    app.controller = UserController(model, app)  # Set the controller for the view

    app.mainloop()

if __name__ == "__main__":
    main()
