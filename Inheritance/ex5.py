# Hieraricheal inheritance

class Parent:
    def p1(self):
        print('THis is parent class')

class Child1(Parent):
    def c1(self):
        print('THis is child 1 one class')

class Child2(Parent):
    def c2(self):
        print('THis is child2 class')

# ob1=Child1()
# ob1.p1()
# ob1.c1()
# THis is parent class
# THis is child 1 one class

ob2=Child2()
ob2.c2()
ob2.p1()
# THis is child2 class
# THis is parent class