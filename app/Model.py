import mysql.connector as mysql

class Model:
    def __init__(self):
        try:
            self.letsride_database = {
                'user': 'root',
                'password': 'root',
                'host': 'localhost',
                'port': 3306,
                'database': 'letsride'
                }

            self.init_db()
        #database accessing error
        except mysql.Error as err:
            print(err)
            print("Error connecting to database. Please check your connection settings and try again.")
            exit(1)
        
    def init_db(self):


        #connect again to the database
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

        #create table locations if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS locations (
                locationid INT AUTO_INCREMENT PRIMARY KEY,
                location VARCHAR(255) NOT NULL
            );
        ''')


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS routes (
                routeid INT AUTO_INCREMENT PRIMARY KEY,
                routesid INT ,
                order_number INT,
                locationid INT,
                foreign key (locationid) references locations(locationid)
            );
        ''')

        # Create the 'rides' table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rides (
                rideid INT AUTO_INCREMENT PRIMARY KEY,
                driverid INT NOT NULL,
                drivername VARCHAR(255) NOT NULL,
                from_location_id INT NOT NULL,
                to_location_id INT NOT NULL,
                date date NOT NULL,
                time TIME NOT NULL,
                available_seats INT NOT NULL,
                routesid INT NOT NULL,
                FOREIGN KEY (driverid) REFERENCES users(userid),
                FOREIGN KEY (from_location_id) REFERENCES locations(locationid),
                FOREIGN KEY (to_location_id) REFERENCES locations(locationid)
                );
        ''')
                #create index for locations table on locationid
        # cursor.execute('''CREATE INDEX locationid_index ON locations (locationid)''')
        # Create the routes table if it doesn't exist

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

        #add database name to the dictionary
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
    
    #get_all_rides_by_from_location
    def get_all_rides_by_from_location(self,from_location):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE from_location_id = %s''',(from_location,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_rides_by_from_location
    def get_rides_by_from_location(self,from_location):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE from_location_id = %s''',(from_location,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_rides_by_date
    def get_rides_by_date(self,date):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE date = %s''',(date,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_rides_by_to_location
    def get_rides_by_to_location(self,to_location):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE to_location_id = %s''',(to_location,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_rides_by_from_location_and_date
    def get_rides_by_from_location_and_date(self,from_location,date):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE from_location_id = %s AND date = %s''',(from_location,date))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_rides_by_from_location_and_to_location
    def get_rides_by_from_location_and_to_location(self,from_location,to_location):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE from_location_id = %s AND to_location_id = %s''',(from_location,to_location))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_rides_by_from_location_to_location_and_date
    def get_rides_by_from_location_to_location_and_date(self,from_location,to_location,date):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM rides WHERE from_location_id = %s AND to_location_id = %s AND date = %s''',(from_location,to_location,date))
        rides = cursor.fetchall()
        conn.close()
        return rides
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
    
    #add_route
    def add_route(self,stops):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()
        #get last routesid
        cursor.execute('''SELECT routesid FROM routes ORDER BY routesid DESC LIMIT 1''')
        routesid = cursor.fetchone()
        if routesid is None:
            routesid = 1
        else:
            routesid = routesid[0] + 1
        for i,stop in enumerate(stops):
            cursor.execute('''INSERT INTO routes (routesid,order_number,locationid) VALUES (%s,%s,%s)''',(routesid,i+1,stop))
            conn.commit()
        return routesid
    
    #get_all_locations
    def get_all_locations(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM locations')
        locations = cursor.fetchall()
        conn.close()
        return locations


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

    # #add_route
    # def add_route(self,stops):
    #     conn = mysql.connect(**self.letsride_database)
    #     cursor = conn.cursor()
    #     cursor.execute('''INSERT INTO routes (order_number,locationid) VALUES (%s,%s)''',(stops[0],stops[1]))
    #     conn.commit()
    #     conn.close()
    #     return True
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

    #get_User_name_by_userid
    def get_User_name_by_userid(self,userid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT first_name FROM users WHERE userid = %s''',(userid,))
        first_name = cursor.fetchone()
        conn.close()
        return first_name[0]
    
    #get_rideid_by_ridedetails
    def get_rideid_by_ridedetails(self,drivername,from_location,to_location,date,time,available_seats):
        print(drivername,from_location,to_location,date,time,available_seats)
        print(type(drivername),type(from_location),type(to_location),type(date),type(time),type(available_seats))
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT rideid FROM rides WHERE drivername = %s AND from_location_id = %s AND to_location_id = %s AND date = %s AND time = %s AND available_seats=%s''', (drivername,from_location,to_location,date,time,available_seats))
        rideid = cursor.fetchone()
        conn.close()
        return rideid

    def add_ride(self, driverid, drivername, from_location, to_location, date, time, available_seats,routeid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO rides (driverid, drivername, from_location_id, to_location_id, date, time, available_seats,routesid)
            VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
        ''', (driverid, drivername, from_location, to_location, date, time, available_seats,routeid))
        conn.commit()

        cursor.execute("SELECT * FROM rides WHERE rideid = LAST_INSERT_ID();")
        ride = cursor.fetchone()
        conn.close()
        return ride
    #get_location_by_locationid
    def get_location_by_locationid(self,locationid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM locations WHERE locationid = %s''',(locationid,))
        location = cursor.fetchone()

        conn.close()
        return location[1]
    
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
    

    #get_locationid_by_locationname
    def get_locationid_by_locationname(self,locationname):
        print(locationname)
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT locationid FROM locations WHERE location = %s''',(locationname,))
        locationid = cursor.fetchone()
        conn.close()
        return locationid[0]
    
    #get_routes_by_routesid
    def get_routes_by_routesid(self,routesid):
        routes_name = []
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT order_number,locationid FROM routes WHERE routesid = %s''',(routesid,))
        routes = cursor.fetchall()
        for route in routes:
            routes=[route[0],self.get_location_by_locationid(route[1])]
            routes_name.append(routes)
        conn.close()
        return routes_name

    
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
