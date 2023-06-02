import mysql.connector

# Create a connection to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="menagerie"
)

# Create a cursor object to execute SQL queries
c = cnx.cursor()

# Define the list of names to delete
names_to_delete = ['Fluffy', 'Claws', 'Buffy', 'Fang', 'Bowser', 'Chirpy', 'Whistler', 'Slim', 'Puffball']

# Create the parameterized query with placeholders
delete_query = "DELETE FROM pet WHERE name IN ({})".format(", ".join(['%s'] * len(names_to_delete)))

# Execute the DELETE statement
c.execute(delete_query, names_to_delete)

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection
c.close()
cnx.close()
