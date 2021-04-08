#instal my-connector
#step 1 import package

import mysql.connector

# step2 establish connection

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mysql"
)
cursor=db.cursor()
sql="insert into college values(100,'aravind','mech',1000)"
cursor.execute(sql)
db.commit()
db.close()
print("values inserted")