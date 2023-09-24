# model.py

import sqlite3
import os

DATABASE_DIR = os.path.join(os.getcwd(), "Database")
RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")

class UserModel:
    def __init__(self, db_path):
        self.db_path = db_path

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone_number TEXT,
                phone_extension TEXT
            );
            ''')

    def register_user(self, username, password, phone_extension, phone_number):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO users (username, password, phone_extension, phone_number) VALUES (?, ?, ?, ?)", 
                               (username, password, phone_extension, phone_number))
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False

    def login_user(self, phone_extension, phone_number, otp_entered):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE phone_extension=? AND phone_number=? AND otp=?", 
                           (phone_extension, phone_number, otp_entered))
            return cursor.fetchone() is not None
