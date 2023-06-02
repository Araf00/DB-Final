import mysql.connector as mc

conn = mc.connect(user='root', password='root',
                  host='localhost', database='pythonsql',
                  auth_plugin='mysql_native_password')
c = conn.cursor()

def read_data():
    c.execute('SHOW DATABASES;')
    databases = c.fetchall()
    for show in databases:
        print(show)

def main():
    read_data()

if __name__ == '__main__':
    main()