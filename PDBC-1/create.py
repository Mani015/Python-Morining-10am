import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='dell')

mydb=db.cursor()
data="Insert into student(rollno, fname, lname, marks) values (%s, %s,%s,%s)"
stu=[(101,'pavan', 'kumar',92),(102,'rajesh','reddy',93),(103, 'thushara','thushara',94),(104,'vamsi', 'krish',92)]

mydb.executemany(data,stu )



db.commit()
