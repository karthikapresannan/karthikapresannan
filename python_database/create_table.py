#instal my-connector
#step 1 import package

import mysql.connector
db=mysql.connector.connect(                   # step2 estabalish connection
    host="localhost",
    user="root",
    password="kathu1997zz",
    auth_plugin="mysql_native_password",
    database="mysql"
)
cursor=db.cursor()
sql="create table student(roll int,name varchar(50),course varchar(50),total int)"
cursor.execute(sql)
print("table created")
