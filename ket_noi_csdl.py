import mysql.connector
from mysql.connector import Error
def CheckLogin(username, password):
    try:
        conn=mysql.connector.connect(host='localhost', database='qlbh', user='root', password='')
        if conn.is_connected():
            select_query = "Select * from tbluser where tendangnhap='{}' and matkhau='{}'".format(username,password)
            cursor = conn.cursor()
            cursor.execute(select_query)
            records=cursor.fetchall()
            if len(records)>0:
                return True
            else:
                return False
    except Error as e:
        print("Loi ket noi",e)