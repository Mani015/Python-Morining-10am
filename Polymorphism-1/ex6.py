
class parent:
    def m1(self):
        print('this is parent class')
class child(parent):
    def m1(self):
        print('THis is child class')
    def m2(self):
        super().m1()


ob=child()
ob.m1()
ob.m2()

# THis is child class
# this is parent class
