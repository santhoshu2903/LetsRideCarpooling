import sqlite3
import os

DATABASE_DIR = os.path.join(os.getcwd(), "Database")
USERS_DB =os.path.join(DATABASE_DIR,"users.db")

class Model:
    def __init__(self,users_db_path =USERS_DB):

        self.users_db_path = users_db_path

        self.init_users_db()



    def init_users_db(self):
        with sqlite3.connect(self.users_db_path) as conn:
            cursor = conn.cursor()
        
            # Drop the existing users table if it exists
            cursor.execute('DROP TABLE IF EXISTS users')
        
            # Create a new table with the desired structure
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone_number TEXT NOT NULL UNIQUE,
                dob TEXT NOT NULL
            );
            ''')


    def get_user_by_username(self, username):
        with sqlite3.connect(self.users_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users
                WHERE username = ?
            ''', (username,))
            user_data = cursor.fetchone()
            return user_data
        
    def login(self, username, password):
        user_data = self.get_user_by_username(username)
        if user_data:
            if user_data[4] == password:
                return True
        return False

    def insertUser(self, first_name, last_name, username, password, phone_number, dob):
        with sqlite3.connect(self.users_db_path) as conn:
            cursor = conn.cursor()

            try:
                cursor.execute('''
                    INSERT INTO users (first_name, last_name, username, password, phone_number, dob)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (first_name, last_name, username, password, phone_number, dob))
                
                conn.commit()
                return True  # Insertion successful
            except sqlite3.IntegrityError:
                # Handle duplicate username or phone_number error
                return False  # Insertion failed due to a duplicate



    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rides (
                    id INTEGER PRIMARY KEY,
                    from_location TEXT,
                    to_location TEXT,
                    date TEXT,
                    time TEXT
                );
            ''')

    def add_ride(self, from_location, to_location, date, time):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO rides (from_location, to_location, date, time)
                VALUES (?, ?, ?, ?)
            ''', (from_location, to_location, date, time))
            ride_id = cursor.lastrowid
        return ride_id
    
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
