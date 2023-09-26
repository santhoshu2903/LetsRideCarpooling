import sqlite3
import os

DATABASE_DIR = os.path.join(os.getcwd(), "Database")
RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")
ALL_USERS_DB =os.path.join(DATABASE_DIR,"all_users.db")

class Model:
    def __init__(self, riders_db_path=RIDERS_DB, passengers_db_path=PASSENGERS_DB):
        self.riders_db_path = riders_db_path
        self.passengers_db_path = passengers_db_path
        self.init_db(self.riders_db_path)
        self.init_db(self.passengers_db_path)

    def init_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
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

    def setRider(self, username, password, phone_number, phone_extension):
        with sqlite3.connect(self.riders_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, password, phone_number, phone_extension)
                VALUES (?, ?, ?, ?)
            ''', (username, password, phone_number, phone_extension))
            return True
    
    def setPassenger(self, username, password, phone_number, phone_extension):
        with sqlite3.connect(self.passengers_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, password, phone_number, phone_extension)
                VALUES (?, ?, ?, ?)
            ''', (username, password, phone_number, phone_extension))
            return True
    
    def get_user_by_username(self, db_path, username):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users
                WHERE username = ?
            ''', (username,))
            user_data = cursor.fetchone()
            return user_data

    # Add more methods for other database operations as needed.
