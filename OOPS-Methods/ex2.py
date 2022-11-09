# Init is a constructor or method

class Student:
    def __init__(self,Fname,Lname,age,standard,rollno,pockemoney,):
        self.Fn=Fname
        self.Ln=Lname
        self.sta=standard
        self.no=rollno
        self.money=pockemoney
        self.age=age
        # object.attribute=value
        print(self.no,self.money,self.Ln,self.Fn,self.sta,self.age)

Student('pavan','kalyan',12,'8th',101020,100)
