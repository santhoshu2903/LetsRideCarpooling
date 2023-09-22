from controller import welcome_controller

if __name__ == "__main__":
    app = welcome_controller.WelcomeController()
    app.view.mainloop()
