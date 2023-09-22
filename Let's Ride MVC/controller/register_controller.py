from view import register_view
from model import db
import sqlite3

class RegisterController:
    def __init__(self):
        self.view = register_view.RegisterView(self)

    def show_register(self):
        self.view.clear_content()
        self.view.show_register()

if __name__ == "__main__":
    from model import db
    from view import register_view
    db.init_db()
    
    controller = RegisterController()
    controller.view.mainloop()
