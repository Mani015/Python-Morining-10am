import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root')

mydb=db.cursor()
mydb.execute('show databases')
for i in mydb:
    print(i)