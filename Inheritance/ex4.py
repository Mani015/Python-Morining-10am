# Multiple inheritance
class Parent1:
    def p1(self):
        print('this is parent class')

class Parent2:
    def p2(self):
        print('THis is parent2 class')

class Child(Parent1,Parent2):
    def c1(self):
        print('This is child class')

ob=Child()
ob.p1()
ob.p2()
ob.c1()

# this is parent class
# THis is parent2 class
# This is child class
