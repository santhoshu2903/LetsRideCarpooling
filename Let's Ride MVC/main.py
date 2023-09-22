import tkinter as tk
from model import db
from view import main_view, login_view, register_view
from controller import main_controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize DBs
        db.init_dbs()

        # Setup canvas
        self.canvas = tk.Canvas(self, bg="#f4f4f4", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Show initial view
        main_view.show_welcome(self.canvas, {
            "show_login": self.show_login,
            "show_register": self.show_register
        })

    def show_login(self):
        self.clear_canvas()
        login_view.show_login(self.canvas, {
            "login": self.login_user,
            "show_welcome": self.show_welcome
        })

    def show_register(self):
        self.clear_canvas()
        register_view.show_register(self.canvas, {
            "register_rider": main_controller.register_rider,
            "register_passenger": main_controller.register_passenger
        })

    def clear_canvas(self):
        for widget in self.canvas.winfo_children():
            widget.destroy()

    def login_user(self, username, password):
        if main_controller.login(username, password):
            print("Login successful")  # Replace with your logic for a successful login
        else:
            print("Login failed")  # Replace with your logic for a failed login

if __name__ == "__main__":
    app = App()
    app.mainloop()
