import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='root', db='menagerie')

def insert_data_pet():
    c = conn.cursor()
    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', NULL)")

    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', NULL)")

    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Buffy', 'Harold', 'dog', 'f', '1989-05-13', NULL)")

    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Fang', 'Benny', 'dog', 'm', '1990-08-27', NULL)")

    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29')")

    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', NULL)")

    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Whistler', 'Gwen', 'bird',NULL , '1997-12-09', NULL)")

    c.execute("INSERT INTO pet (name, owner, species, sex, birth, death) "
                   "VALUES ('Slim', 'Benny', 'snake', 'm', '1996-04-29', NULL)")

    c.execute("INSERT INTO pet(name, owner, species, sex, birth, death)"
                    "VALUES ('Puffball','Diane','hamster','f','1993-03-30',NULL)")

    conn.commit()
    c.close()

def show_data_pet():
    c = conn.cursor()
    c.execute("SELECT * FROM pet")

    result = c.fetchall()
    for row in result:
        print(row)

    c.close()

if __name__ == '__main__':
    insert_data_pet()
    show_data_pet()
