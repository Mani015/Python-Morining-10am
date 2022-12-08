import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='dell')

mydb=db.cursor()
my='delete from student where marks=92'
mydb.execute(my)

db.commit()