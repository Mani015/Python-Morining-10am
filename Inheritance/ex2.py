class Parent:
    def parent1(self):
        print('This is parent property')

class Child (Parent):
    def child1(self):
        print('This is child class')
#  who is getting parent property ,It should create an a object(Inherit)
ob1=Child()
ob1.child1()
ob1.parent1()

# This is child class
# This is parent property
