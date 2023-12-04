import sqlite3

# connect to the database
conn = sqlite3.connect('passenger.sqlite')

# create a cursor
c = conn.cursor()

# execute a query
c.execute('create table mytable (id integer primary key, name text)')

# commit the changes
conn.commit()

# close the connection
conn.close()
