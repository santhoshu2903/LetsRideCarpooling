import sqlite3
import os

DATABASE_DIR = os.path.join(os.getcwd(), "Database")
RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")
ALL_USERS_DB = os.path.join(DATABASE_DIR, "all_users.db")

def init_db():
    # Initialize the riders database
    with sqlite3.connect(RIDERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS riders (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone_number TEXT,
        phone_extension TEXT
    );
    ''')

    # Initialize the passengers database
    with sqlite3.connect(PASSENGERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS passengers (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone_number TEXT,
        phone_extension TEXT
    );
    ''')
    
    # Initialize the all users database
    with sqlite3.connect(ALL_USERS_DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS all_users (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        phone_number TEXT,
        phone_extension TEXT
    );
    ''')

if __name__ == "__main__":
    init_db()
