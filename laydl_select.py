import mysql.connector
from mysql.connector import Error
conn=None
try:
    conn=mysql.connector.connect(host='localhost', database='qlbh',user='root',password='')   
    if conn.is_connected():
        print("ket noi voi MySQL thanh cong")
        select_query="select * from tbluser"
        cursor=conn.cursor()
        cursor.execute(select_query)
        records=cursor.fetchall()
        print("Danh sach nguoi dung:")
        for row in records:
            print(row)
except Error as er:
    print("Loi ket noi",er)