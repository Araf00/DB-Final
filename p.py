import mysql.connector

# Create a connection to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# Create a cursor object to execute SQL queries
c = cnx.cursor()

# Select the database
c.execute("USE menagerie")

# Execute the SELECT statement
c.execute("SELECT * FROM pet")

# Fetch and print the results
result = c.fetchall()
for row in result:
    print(row)

# Close the cursor and connection
c.close()
cnx.close()
