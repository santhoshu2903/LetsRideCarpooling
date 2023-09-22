import sqlite3

RIDERS_DB = "riders.db"
PASSENGERS_DB = "passengers.db"

def init_dbs():
    init_db(RIDERS_DB, "rider")
    init_db(PASSENGERS_DB, "passenger")

def init_db(db_name, role):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        ''', (role,))


def add_user_to_db(db_name, username, password):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

def add_rider(username, password):
    add_user_to_db(RIDERS_DB, username, password)

def add_passenger(username, password):
    add_user_to_db(PASSENGERS_DB, username, password)

def get_user(db_name, username):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()
