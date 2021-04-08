#install my-connector
#step 1 import package

import mysql.connector
db=mysql.connector.connect(                   #step2 estabalish connection
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
#cursor object
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)