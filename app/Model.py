import mysql.connector as mysql

class Model:
    def __init__(self):
        
        self.letsride_database = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': 3306,
            'database': 'letsride'
        }

        self.init_db()



    def init_db(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        # Create the 'users' table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userid INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                phone_number VARCHAR(255) NOT NULL UNIQUE,
                dob VARCHAR(255) NOT NULL
            );
        ''')

        # Create the 'rides' table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rides (
                rideid INT AUTO_INCREMENT PRIMARY KEY,
                driverid INT NOT NULL,
                drivername VARCHAR(255) NOT NULL,
                from_location VARCHAR(255) NOT NULL,
                to_location VARCHAR(255) NOT NULL,
                date VARCHAR(255) NOT NULL,
                time VARCHAR(255) NOT NULL,
                available_seats INT NOT NULL,
                FOREIGN KEY (driverid) REFERENCES users(userid)
            );
        ''')

        #create a table for confirmedrides
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS confirmedrides (
                confirmedrideid INT AUTO_INCREMENT PRIMARY KEY,
                rideid INT NOT NULL,
                userid INT NOT NULL,
                no_of_seats INT NOT NULL,
                FOREIGN KEY (rideid) REFERENCES rides(rideid),
                FOREIGN KEY (userid) REFERENCES users(userid)
            );
        ''')

        conn.close()

    #get_all_confirmed_rides_by_rideid
    def get_all_confirmed_rides_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM confirmedrides WHERE rideid = %s''',(rideid,))
        rides = cursor.fetchall()
        conn.close()
        return rides

    #get_User_by_userid
    def get_User_by_userid(self,userid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM users WHERE userid = %s''',(userid,))
        user = cursor.fetchone()
        conn.close()
        return user
    #get_all_confirmed_rides
    def get_all_confirmed_rides(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM confirmedrides''')
        rides = cursor.fetchall()
        conn.close()
        return rides

    #check_if_already_booked
    def check_if_already_booked(self,rideid,userid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM confirmedrides WHERE rideid = %s AND userid = %s''',(rideid,userid))
        ride = cursor.fetchone()
        conn.close()
        return ride


    #update_available_seats
    def update_available_seats(self,rideid,available_seats):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''UPDATE rides SET available_seats = %s WHERE rideid = %s''',(available_seats,rideid))
        conn.commit()

        cursor.execute("SELECT * FROM rides WHERE rideid = %s",(rideid,))
        ride = cursor.fetchone()
        conn.close()
        return ride


    #get_all_confirmed_rides_by_user
    def get_all_confirmed_rides_by_user(self,userid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM confirmedrides WHERE userid = %s''',(userid,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #.get_ride_by_rideid
    def get_ride_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE rideid = %s''',(rideid,))
        ride = cursor.fetchone()
        conn.close()
        return ride


    #confirm ride
    def confirm_ride(self,rideid,userid,no_of_seats):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO confirmedrides (rideid,userid,no_of_seats) VALUES (%s,%s,%s)''',(rideid,userid,no_of_seats))
        conn.commit()

        cursor.execute("SELECT * FROM confirmedrides WHERE confirmedrideid = LAST_INSERT_ID();")
        ride = cursor.fetchone()
        conn.close()
        return ride


    #get_rideid_by_ridedetails
    def get_rideid_by_ridedetails(self,drivername,from_location,to_location,date,time,available_seats):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT rideid FROM rides WHERE drivername = %s AND from_location = %s AND to_location = %s AND date = %s AND time = %s AND available_seats=%s''', (drivername,from_location,to_location,date,time,available_seats))
        rideid = cursor.fetchone()
        conn.close()
        return rideid

    def add_ride(self, driverid, drivername, from_location, to_location, date, time, available_seats):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO rides (driverid, drivername, from_location, to_location, date, time, available_seats)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (driverid, drivername, from_location, to_location, date, time, available_seats))
        conn.commit()

        cursor.execute("SELECT * FROM rides WHERE rideid = LAST_INSERT_ID();")
        ride = cursor.fetchone()
        conn.close()
        return ride

    #get_all_users
    def get_all_users(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        return users

    def get_rides_by_driverid(self, driverid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM rides
            WHERE driverid = %s
        ''', (driverid,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    

    def get_rides_by_user(self, userid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM confirmedrides
            WHERE userid = %s
        ''', (userid,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_all_rides_count
    def get_all_rides_count(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT COUNT(*) FROM rides''')
        rides_count = cursor.fetchone()
        conn.close()
        return rides_count
    
    #get_active_passengers_count from confirmedrides table seats booked column  
    def get_active_passengers_count(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT SUM(no_of_seats) FROM confirmedrides''')
        passengers_count = cursor.fetchone()
        conn.close()
        return passengers_count

    
    #get_active_rides_count  from rides table with date greater than yesterday
    def get_active_rides_count(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT COUNT(*) FROM rides WHERE date > CURDATE()''')
        rides_count = cursor.fetchone()
        conn.close()
        return rides_count

    

    #get_rides_count_by_driverid
    def get_rides_count_by_driverid(self,driverid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT COUNT(*) FROM rides WHERE driverid = %s''',(driverid,))
        rides_count = cursor.fetchone()
        conn.close()
        return rides_count

    def get_all_rides(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM rides')
        rides = cursor.fetchall()
        conn.close()
        return rides

    def get_user_by_username(self, username):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM users
            WHERE username = %s
        ''', (username,))
        user_data = cursor.fetchone()
        conn.close()
        return user_data

    # Add more methods for other database operations as needed

    def get_User_by_phone_number(self, phone_number):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM users
            WHERE phone_number = %s
        ''', (phone_number,))
        user_data = cursor.fetchone()
        conn.close()
        return user_data


    def insertUser(self, first_name, last_name, email, username, password, phone_number, dob):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO users (first_name, last_name, email, username, password, phone_number, dob)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (first_name, last_name, email, username, password, phone_number, dob))
            conn.commit()
            conn.close()
            return True  # Insertion successful
        except mysql.IntegrityError:
            # Handle duplicate username or phone_number error
            conn.close()
            return False  # Insertion failed due to a duplicate


    def update_password(self, username, password):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE users
            SET password = %s
            WHERE username = %s
        ''', (password, username))
        conn.commit()
        conn.close()
        return True  # Update successful
