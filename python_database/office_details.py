import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mysql"
)

cursor=db.cursor()
f=open("data1","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into offices values(%s,%s,%s,%s"
    cursor.execute(sql,data)
    db.commit()