# There are 3 types of varaibles
# 1.Instance varaible
# 2.Static variable
# 3.local variable [or] class variable

# 1.Instace variable:instance variable is a varaible method of object
# to use of object creation of instance method create /access/modify/data

class Car:
    # Instance method
    def method1(self):
        # instance variable
        # [object.attribute=value]
        self.dogname='rocky'
        # instance variable
        self.age='10'
        # instance of variable
        self.colour='brown'
        print(self.dogname,self.colour,self.age)
# Object creation
ob=Car()
ob.method1()
# Instance method can be accessed using object creation (or)instance
