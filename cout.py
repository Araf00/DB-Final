import mysql.connector as mc

def show_owned(c):
    c.execute('SELECT owner, COUNT(*) FROM pet GROUP BY owner')
    owned = c.fetchall()
    for own in owned:
        owner, count = own
        print(f'Owner: {owner}, Count: {count}')

def main():
    conn = mc.connect(
        host='localhost',
        user='root',
        password='root',
        db='menagerie'
    )
    cursor = conn.cursor()
    show_owned(cursor)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
