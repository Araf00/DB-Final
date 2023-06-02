import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='root', db='menagerie')

def show_name_name_birth(conn):
    c = conn.cursor()
    c.execute('SELECT name, birth FROM pet')
    fields = c.fetchall()
    for field in fields:
        print(field)
    c.close()

def main():
    show_name_name_birth(conn)
    conn.close()

if __name__ == '__main__':
    main()
