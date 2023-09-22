import tkinter as tk
from tkinter import ttk

def show_welcome(canvas, callbacks):
    login_button = ttk.Button(canvas, text="Login", command=callbacks["show_login"])
    login_button.pack(pady=20)
    register_button = ttk.Button(canvas, text="Register", command=callbacks["show_register"])
    register_button.pack(pady=20)
