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
                connecting boolean DEFAULT false,
                connectingrideid INT DEFAULT NULL,
                FOREIGN KEY (driverid) REFERENCES users(userid),
                FOREIGN KEY (from_location_id) REFERENCES locations(locationid),
                FOREIGN KEY (to_location_id) REFERENCES locations(locationid)
                );
        ''')

        
        #create stops table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stops (
                stopid INT AUTO_INCREMENT PRIMARY KEY,
                rideid INT NOT NULL,
                location1_id INT NOT NULL,
                location2_id INT ,
                location3_id INT,
                FOREIGN KEY (rideid) REFERENCES rides(rideid),
                FOREIGN KEY (location1_id) REFERENCES locations(locationid),
                FOREIGN KEY (location2_id) REFERENCES locations(locationid),
                FOREIGN KEY (location3_id) REFERENCES locations(locationid)
            );
        ''')


                #create stops table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stops (
                stopid INT AUTO_INCREMENT PRIMARY KEY,
                rideid INT NOT NULL,
                location1_id INT NOT NULL,
                location2_id INT ,
                location3_id INT,
                FOREIGN KEY (rideid) REFERENCES rides(rideid),
                FOREIGN KEY (location1_id) REFERENCES locations(locationid),
                FOREIGN KEY (location2_id) REFERENCES locations(locationid),
                FOREIGN KEY (location3_id) REFERENCES locations(locationid)
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
        
        #create feedback table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                feedbackid INT AUTO_INCREMENT PRIMARY KEY,
                userid INT NOT NULL,
                rideid INT NOT NULL,
                rating INT NOT NULL,
                comment VARCHAR(255) NOT NULL,
                FOREIGN KEY (userid) REFERENCES users(userid),
                FOREIGN KEY (rideid) REFERENCES rides(rideid)
            );
        ''')
        
        #add database name to the dictionary
        conn.close()

    #add_available_seats
    def add_available_seats(self,rideid,from_location,to_location,seats):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO availableseats (rideid,from_location_id,to_location_id,seats) VALUES (%s,%s,%s,%s)''',(rideid,from_location,to_location,seats))
        conn.commit()
        cursor.execute("SELECT * FROM availableseats WHERE availableseatid = LAST_INSERT_ID();")
        availableseat = cursor.fetchone()
        conn.close()
        return availableseat

    #get_all_confirmed_rides_by_rideid
    def get_all_confirmed_rides_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM confirmedrides WHERE rideid = %s''',(rideid,))
        rides = cursor.fetchall()
        conn.close()
        return rides
    
    #get_ride_id_by_drivername_from_location_to_location_date_time_available_seats
    def get_ride_id_by_drivername_from_location_to_location_date_time_available_seats(self,drivername,from_location,to_location,date,time,available_seats):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT rideid FROM rides WHERE drivername = %s AND from_location_id = %s AND to_location_id = %s AND date = %s AND time = %s AND available_seats=%s''', (drivername,from_location,to_location,date,time,available_seats))
        rideid = cursor.fetchone()
        conn.close()
        return rideid[0]

    #get_User_by_userid
    def get_User_by_userid(self,userid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM users WHERE userid = %s''',(userid,))
        user = cursor.fetchone()
        conn.close()
        return user
    

    #check_if_already_booked_ride
    def check_if_already_booked_ride(self,rideid,userid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM confirmedrides WHERE rideid = %s AND userid = %s''',(rideid,userid))
        ride = cursor.fetchone()
        conn.close()
        return ride
    
    
        return ride
    
  

    
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
    
 
    #get_all_locations
    def get_all_locations(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM locations')
        locations = cursor.fetchall()
        conn.close()
        return locations


    #update_available_seats
    def update_available_seats(self,rideid,difference):
        print ("reached here",rideid,difference)
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()
        try:
            #check if it is a connecting ride
            connecting=self.check_if_connecting_ride(rideid)
            from_location_id=self.get_from_location_id_by_rideid(rideid)
            to_location_id=self.get_to_location_id_by_rideid(rideid)
            if connecting:
                #get connecting ride id
                connecting_rideid=self.get_connectingrideid_by_rideid(rideid)
                main_from_location_id=self.get_from_location_id_by_rideid(connecting_rideid)
                main_to_location_id=self.get_to_location_id_by_rideid(connecting_rideid)
                stops=self.get_stops_by_rideid(connecting_rideid)
                stops=[main_from_location_id]+stops+[main_to_location_id]
                print ("stops",stops)
                effected_location_ids=self.get_effected_location_ids(stops,from_location_id,to_location_id)
                print("effected_location_ids",effected_location_ids)
                for location in effected_location_ids:
                    #all connecting rides and available seats is negative set it to 0
                    cursor.execute("UPDATE rides SET available_seats = available_seats - %s WHERE from_location_id = %s AND to_location_id = %s AND connectingrideid = %s", (difference, location[0], location[1], connecting_rideid))

                #update the ride itself
                cursor.execute("UPDATE rides SET available_seats = available_seats - %s WHERE rideid = %s", (difference, connecting_rideid))

                conn.commit()
            else:
                stops=self.get_stops_by_rideid(rideid)
                if stops:
                    stops=[from_location_id]+stops+[to_location_id]
                    effected_location_ids=self.get_effected_location_ids(stops,from_location_id,to_location_id)
                    print("effected_location_ids",effected_location_ids)
                    for location in effected_location_ids:
                        print("location",location)
                        #all connecting rides
                        cursor.execute("UPDATE rides SET available_seats = available_seats - %s WHERE from_location_id = %s AND to_location_id = %s AND connectingrideid=%s", (difference, location[0], location[1],rideid))
                #update the ride itself
                cursor.execute("UPDATE rides SET available_seats = available_seats - %s WHERE rideid = %s", (difference, rideid))

            #if available seats is negative set it to 0
            cursor.execute("UPDATE rides SET available_seats = 0 WHERE available_seats < 0")
            conn.commit()

        except mysql.Error as err:
            print(err)
            conn.close()
            return False
        return True
    

    #get_from_location_id_by_rideid
    def get_from_location_id_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT from_location_id FROM rides WHERE rideid = %s''',(rideid,))
        from_location_id = cursor.fetchone()
        conn.close()
        return from_location_id[0]
    
    #get_to_location_id_by_rideid
    def get_to_location_id_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT to_location_id FROM rides WHERE rideid = %s''',(rideid,))
        to_location_id = cursor.fetchone()
        conn.close()
        return to_location_id[0]
    
    #get_available_seats_by_rideid
    def get_available_seats_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT available_seats FROM rides WHERE rideid = %s''',(rideid,))
        available_seats = cursor.fetchone()
        conn.close()
        return available_seats[0]
    
    #update_user_details
    def update_user_details(self,userid,first_name,last_name,email,phone_number,dob):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''UPDATE users SET first_name = %s, last_name = %s, email = %s, phone_number = %s, dob = %s WHERE userid = %s''',(first_name,last_name,email,phone_number,dob,userid))
        conn.commit()
        conn.close()
        return True
    
    
    #update_password
    def update_password(self,userid,password):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''UPDATE users SET password = %s WHERE userid = %s''',(password,userid))
        conn.commit()
        conn.close()
        return True
    
    #get_most_booked_locations
    def get_most_booked_locations(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT l.location, COUNT(*) AS ride_count
                            FROM rides r
                            JOIN locations l ON r.from_location_id = l.locationid
                            GROUP BY r.from_location_id;
                            ''')
        locations = cursor.fetchall()
        conn.close()
        return locations
    
    #get_rides_per_day
    def get_rides_per_day(self):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT date, COUNT(*) FROM rides GROUP BY date''')
        rides_per_day = cursor.fetchall()
        conn.close()
        return rides_per_day
    
    #get_all_rideids_by_userid
    def get_all_rideids_by_userid(self,userid):
        ride_ids=[]
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT rideid FROM rides WHERE driverid = %s''',(userid,))
        rides = cursor.fetchall()
        conn.close()
        for ride in rides:
            ride_ids.append(ride[0])
        return ride_ids
    
    

    #get_effected_location_ids
    def get_effected_location_ids(self,locations,from_location,to_location):
        from_index=locations.index(from_location)
        to_index = locations.index(to_location)
        print(from_index,to_index)
        end_index=len(locations)-1
        effected_locations=[]
        for i in range(0,end_index+1):
            for j in range(from_index,end_index+1):
                if i>to_index or i==to_index or j==from_index :
                    continue
                elif j<i or i==j:
                    continue
                effected_locations.append([locations[i],locations[j]])
                            
        return effected_locations


    #check_if_connecting_ride
    def check_if_connecting_ride(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT connecting FROM rides WHERE rideid = %s''',(rideid,))
        connecting = cursor.fetchone()
        if connecting[0]==1:
            return True
        return False
    #get_connectingrideid_by_rideid
    def get_connectingrideid_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT connectingrideid FROM rides WHERE rideid = %s''',(rideid,))
        ride = cursor.fetchone()
        conn.close()
        return ride[0]
    
    #get_stops_by_rideid
    def get_stops_by_rideid(self,rideid):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM stops WHERE rideid = %s''',(rideid,))
        stops = cursor.fetchone()
        print("stops",stops)
        if stops == None:
            return False

       #convert tuple to list and remove first element
        stops=list(stops)[2:]
        print("stops",stops)
        return stops


    #add_stops
    def add_stops(self,rideid,stops):
        stops=stops[1:4]
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        l=len(stops)

        print("reached here",rideid,stops,l)
        if l == 0:
            return False
        elif l==1:
            #insert into stops table keeping location2_id and location3_id as null
            cursor.execute('''INSERT INTO stops (rideid,location1_id,location2_id,location3_id) VALUES (%s,%s,%s,%s)''',(rideid,stops[0],None,None))
            conn.commit()
        elif l==2:
            #insert into stops table keeping location3_id as null
            cursor.execute('''INSERT INTO stops (rideid,location1_id,location2_id,location3_id) VALUES (%s,%s,%s,%s)''',(rideid,stops[0],stops[1],None))
            conn.commit()
        elif l==3:
            #insert into stops table
            cursor.execute('''INSERT INTO stops (rideid,location1_id,location2_id,location3_id) VALUES (%s,%s,%s,%s)''',(rideid,stops[0],stops[1],stops[2]))
            conn.commit()
        else:
            return False

        cursor.execute("SELECT * FROM stops WHERE stopid = LAST_INSERT_ID();")
        stop = cursor.fetchone()
        conn.close()
        return stop


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

    def add_ride(self, driverid, drivername, from_location, to_location, date, time, available_seats,connecting=False,connecting_rideid=None):
        conn = mysql.connect(**self.letsride_database)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO rides (driverid, drivername, from_location_id, to_location_id, date, time, available_seats, connecting, connectingrideid)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (driverid, drivername, from_location, to_location, date, time, available_seats,connecting,connecting_rideid))
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
