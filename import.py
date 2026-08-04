import mysql.connector as myconn
mydb= myconn.connect(host="localhost",user="root",password="2809")

print(mydb,"connected")