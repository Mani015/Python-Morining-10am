import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root')

# print(db)

if db:
    print('connceted done')
else:
    print('connection failed')