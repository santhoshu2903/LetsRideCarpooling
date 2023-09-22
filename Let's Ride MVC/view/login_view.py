import tkinter as tk
from tkinter import ttk

def show_login(canvas, callbacks):
    username_label = ttk.Label(canvas, text="Username:")
    username_label.pack(padx=20, pady=5)
    username_entry = ttk.Entry(canvas)
    username_entry.pack(padx=20, pady=5)
    password_label = ttk.Label(canvas, text="Password:")
    password_label.pack(padx=20, pady=5)
    password_entry = ttk.Entry(canvas, show="*")
    password_entry.pack(padx=20, pady=5)
    login_button = ttk.Button(canvas, text="Login", command=lambda: callbacks["login"](username_entry.get(), password_entry.get()))
    login_button.pack(pady=20)
    back_button = ttk.Button(canvas, text="Back", command=callbacks["show_welcome"])
    back_button.pack(pady=20)
