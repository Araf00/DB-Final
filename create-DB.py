import mysql.connector as mc

# Connect to MySQL server
conn = mc.connect(
    host='localhost',
    user='root',
    password='root'
)

# Create a cursor object
cursor = conn.cursor()

# Create the database
cursor.execute("CREATE DATABASE pythonsql")

# Close the cursor and connection
cursor.close()
conn.close()