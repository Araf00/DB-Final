import pymysql
from pymysql import err

try:
    conn = pymysql.connect(host='localhost', user='root', password='root', db='pythonSQL')
    print("Connected")

except err.OperationalError as e:
    if e.args[0] == 1045:
        print("Something is wrong with your username or password")
        print(e)

else:
    print("Connection closed")
    conn.close()