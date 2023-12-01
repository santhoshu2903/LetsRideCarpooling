import mysql.connector
from datetime import date, timedelta
import random

def insert_sample_rides(cursor):
    # User IDs corresponding to the provided usernames
    user_ids = [ 2, 3, 4, 5, 6, 7, 8, 9]

    # Location names
    locations = [
        'Detroit', 'Ann Arbor', 'Lansing', 'Grand Rapids', 'Flint', 'Kalamazoo', 'Traverse City',
        'Saginaw', 'Muskegon', 'Holland', 'Mount Pleasant', 'Battle Creek', 'Livonia', 'Dearborn',
        'Sterling Heights', 'Warren', 'Troy', 'Farmington Hills', 'Jackson', 'Midland'
    ]

    #converts locations into id of index of list
    locations = [i+1 for i in range(len(locations))]
    print(locations)

    # Inserting rides for the next 60 days
    current_date = date.today()
    end_date = current_date + timedelta(days=60)

    #date list of 60 days date from today
    dates = [current_date + timedelta(days=i) for i in range(60)]


    for i in range(60):
        for user_id in user_ids:
            from_location_id = random.choice(range(1, len(locations) + 1))
            to_location_id = random.choice([i for i in range(1, len(locations) + 1) if i != from_location_id])

            #get First name and last name of user
            cursor.execute(f"""
                SELECT first_name, last_name
                FROM users
                WHERE userid = {user_id}
            """)
            user_name = cursor.fetchone()
            user_name = user_name[0] + ' ' + user_name[1]
            driver_name = user_name
            date1=random.choice(dates)
            #random time
            time = random.choice(['01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00','07:00:00','08:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00'])

            cursor.execute("""
                INSERT INTO rides (driverid, drivername, from_location_id, to_location_id, date, time, available_seats)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (user_id, driver_name, from_location_id, to_location_id, date1, time, 3))



if __name__ == "__main__":
    # Replace these with your actual database connection details
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="letsride",
        port=3306
    )

    cursor = db_connection.cursor()

    # Assuming you've already created the rides table
    insert_sample_rides(cursor)

    db_connection.commit()
    cursor.close()
    db_connection.close()
