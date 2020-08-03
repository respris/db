# Create a database and table

# import sqlite3 library
import sqlite3

# create a new database
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""create table population (city text, state text, population int)""")

# close db connection

conn.close()