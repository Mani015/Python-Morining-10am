# Multi level inheritance

class Grandparent:
    def g1(self):
        print('This is grandparent class')
class Parent(Grandparent):
    def p1(self):
        print('This is parent class')
class Child(Parent):
    def c1(self):
        print('This is child class')

ob1=Parent()
# ob1.p1()
# ob1.g1()
# This is parent class
# This is grandparent class

ob2=Child()
# ob2.c1()
# ob2.p1()
# This is child class
# This is parent class


ob3=Child()
ob3.g1()
ob3.p1()
# This is grandparent class
# This is parent class
# This is child class