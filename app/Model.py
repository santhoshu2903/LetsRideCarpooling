import sqlite3
import os

DATABASE_DIR = os.path.join(os.getcwd(), "Database")
RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")
ALL_USERS_DB =os.path.join(DATABASE_DIR,"all_users.db")

class Model:
    def __init__(self,all_users_db_path =ALL_USERS_DB, riders_db_path=RIDERS_DB, passengers_db_path=PASSENGERS_DB):
        self.riders_db_path = riders_db_path
        self.passengers_db_path = passengers_db_path
        self.all_users_db_path = all_users_db_path

        self.init_db(self.riders_db_path)
        self.init_db(self.passengers_db_path)
        self.init_all_users_db()



    def init_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone_number TEXT
            );
            ''')


    def init_all_users_db(self):
        with sqlite3.connect(self.all_users_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT NOT NULL UNIQUE,
                role TEXT NOT NULL
            );
            ''')

    def setRider(self, username, password, phone_number):
        with sqlite3.connect(self.all_users_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (phone_number, role)
                VALUES (?, ?)
            ''', (phone_number, "rider"))
            conn.commit()  # Commit the changes
            generated_userid = cursor.lastrowid

        # Now, insert rider-specific data into the 'riders' table
        with sqlite3.connect(self.riders_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (userid, username, password, phone_number)
                VALUES (?, ?, ?, ?)
            ''', (generated_userid, username, password, phone_number))
            conn.commit()

    
    def setPassenger(self, username, password, phone_number):
        with sqlite3.connect(self.all_users_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (phone_number,role)
                VALUES (?,?)
            ''', (phone_number,"passenger"))
            conn.commit()  # Commit the changes
            generated_userid = cursor.lastrowid

        with sqlite3.connect(self.passengers_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (userid, username, password, phone_number)
                VALUES (?, ?, ?, ?, ?)
            ''', (generated_userid, username, password,phone_number))
            conn.commit()  # Commit the changes

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
