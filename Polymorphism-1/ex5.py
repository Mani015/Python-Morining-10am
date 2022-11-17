
class parent:
    def method1(self):
        print('THis is parent class')

class child(parent):
    def method1(self):
        print('This is child class')


ob=child()
ob.method1()
ob.method1()