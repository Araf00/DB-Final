import mysql.connector as mc

conn = mc.connect(user='root', password='root',
                  host='localhost', database='pythonsql',
                  auth_plugin='mysql_native_password')
c = conn.cursor()

def drop_database():
    c.execute('DROP DATABASE IF EXISTS menagerie ')
    c.execute('CREATE DATABASE menagerie ')
    conn.commit()

def main():
    drop_database()

if __name__ == '__main__':
    main()