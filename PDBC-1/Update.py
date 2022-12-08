import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='dell')

mydb=db.cursor()
mydb1='update student set fname="pandu" where  lname="reddy"'
mydb.execute(mydb1)
db.commit()