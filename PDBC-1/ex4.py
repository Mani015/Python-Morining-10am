import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='dell')

mydb=db.cursor()
mydb.execute("create table student(rollno int, fname varchar(30), lname varchar(30), marks int)")

print(mydb)