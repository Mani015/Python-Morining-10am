# The process of acquiring properties from one class to another class is called Inheritance
# The class which is giving properties to another class is called Parentclass/superclass
# the class which is getting properties from another class is called childclass/ subclass
# TYPES OF INHERITANCE
# 1)single level inheritance
# 2) multi level inheritance
# 3)multiple inheritance
# 4)hirarchical inheritance
# 5)hybrid inheritance



# Single inheritance
class Parent:
    def parent1(self):
        print('This is parent property')

class Child:
    def child1(self):
        print('This is child class')

# ob1=Parent()
# ob1.parent1()
# This is parent property

ob2=Child()
ob2.child1()
# This is child class