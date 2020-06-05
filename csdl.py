import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(host='localhost',database='qlbh',user='root',password='')
    if conn.is_connected():
        print("Ket noi voi MySQL thanh cong")
except Error as e:
    print("Loi ket noi",e)