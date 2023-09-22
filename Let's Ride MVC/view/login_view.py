import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Login")
        self.geometry("500x400")
        self.configure(bg="#f4f4f4")

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10, "bold"), borderwidth=0)
        style.configure("TLabel", font=("Segoe UI", 12), background="#f4f4f4")
        style.configure("TEntry", font=("Segoe UI", 10))

        self.phone_extensions = ["+1", "+44", "+91", "+33"]

        self.phone_extension_combobox = ttk.Combobox(self, values=self.phone_extensions)
        self.phone_extension_combobox.pack(pady=10)
        self.phone_extension_combobox.set(self.phone_extensions[0])

        self.phone_number_label = ttk.Label(self, text="Phone Number:")
        self.phone_number_label.pack(pady=10)

        self.phone_number_entry = ttk.Entry(self)
        self.phone_number_entry.pack(pady=10)
        self.phone_number_entry.focus_set()

        self.otp_label = ttk.Label(self, text="OTP:")
        self.otp_label.pack(pady=10)

        self.otp_entry = ttk.Entry(self)
        self.otp_entry.pack(pady=10)

        self.send_otp_btn = ttk.Button(self, text="Send OTP", command=self.controller.send_otp)
        self.send_otp_btn.pack(pady=10)

        self.login_btn = ttk.Button(self, text="Login", command=self.controller.login_user)
        self.login_btn.pack(pady=10)

        self.back_btn = ttk.Button(self, text="Back", command=self.controller.show_welcome)
        self.back_btn.pack(pady=10)

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = LoginView(None)
    app.mainloop()
