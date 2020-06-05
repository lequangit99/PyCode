import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(host='localhost',database='qlbh',user='root',password='')
    if conn.is_connected():
        insert_query= "insert into tbluser (tendangnhap,matkhau,hoten,dienthoai,email,diachi) values('ha133','12345','Nguyen van a','019738934','han@gmail.com','CNTT3-k58')"
        cursor = conn.cursor()
        cursor.execute(insert_query)
        conn.commit()
        print("So ban ghi duoc them vao bang thanh cong: ", cursor.rowcount)
        cursor.close()
        conn.close()
except Error as e:
    print("Loi ket noi",e)