import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='root', db='menagerie')

def insert_data_pet():
    c = conn.cursor()
    c.execute('SELECT * FROM pet WHERE species = "dog" AND sex = "f"')
    results = c.fetchall()

    # Print the fetched results
    for row in results:
        print(row)

    conn.commit()
    c.close()

if __name__ == '__main__':
    insert_data_pet()

