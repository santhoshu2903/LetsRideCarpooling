import tkinter as tk
from controller.welcome_controller import WelcomeController

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeController(root)
    root.mainloop()
