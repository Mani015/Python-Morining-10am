import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='dell')

mydb=db.cursor()
# mydb.execute("select * from student")
mydb.execute('select fname, lname,  marks from student pavan')
output=mydb.fetchone()
for i in output:
    print(i)
