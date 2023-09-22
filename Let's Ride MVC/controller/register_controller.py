from view import register_view
from model import db

class RegisterController:
    def __init__(self):
        self.view = register_view.RegisterView(self)

    def show_register(self):
        self.view.clear_content()
        self.view.show_register()

    def register_user(self):
        # Implement user registration logic here
