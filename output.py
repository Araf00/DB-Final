import mysql.connector as mc

# Connect to MySQL server
conn = mc.connect(
    host='localhost',
    user='root',
    password='root',
    database='menagerie'
)

# Create a cursor object
c = conn.cursor()

# Create the database
c.execute("SELECT name, birth, MONTH(birth) FROM pet")

rows = c.fetchall()
for row in rows:
    name, birth, month = row
    print(f"Name: {name,}, Birth: {birth}, Month: {month}")

# Close the cursor and connection
c.close()
conn.close()