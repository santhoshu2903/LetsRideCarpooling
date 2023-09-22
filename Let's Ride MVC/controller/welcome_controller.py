import tkinter as tk
from view.welcome_view import WelcomeView
from controller.register_controller import RegisterController
from controller.login_controller import LoginController
from view.login_view import LoginView
from view.register_view import RegisterView

class WelcomeController:
    def __init__(self, root):
        self.root = root
        self.view = WelcomeView(self)
        self.view.mainloop()

    def show_login(self):
        self.view.clear_content()
        login_controller = LoginController(self.root)

    def show_register(self):
        self.view.clear_content()
        register_controller = RegisterController(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeController(root)
    root.mainloop()
