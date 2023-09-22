from view import login_view
from model import db
import sqlite3
import random
import tkinter as tk
from tkinter import ttk, messagebox
from twilio.rest import Client

class LoginController:
    def __init__(self):
        self.view = login_view.LoginView(self)

    def show_login(self):
        self.view.clear_content()
        self.view.show_login()
