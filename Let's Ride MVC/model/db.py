import sqlite3
import os

# Directory to store database files
DATABASE_DIR = os.path.join(os.getcwd(), "Database")
if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

RIDERS_DB = os.path.join(DATABASE_DIR, "riders.db")
PASSENGERS_DB = os.path.join(DATABASE_DIR, "passengers.db")
ALL_USERS_DB = os.path.join(DATABASE_DIR, "all_users.db")

def init_db(db_path):
    # Initialize the database
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

def init_dbs():
    init_db(RIDERS_DB)
    init_db(PASSENGERS_DB)
    init_db(ALL_USERS_DB)

if __name__ == "__main__":
    init_dbs()
