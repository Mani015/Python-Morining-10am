import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root')

mydb=db.cursor()

mydb.execute('create database dell')
print(mydb)