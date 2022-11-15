class parent:
    myproperty=100000

class child(parent):
    def f1(self):
        self.b=200
        print('child total property:',self.b + self.myproperty)

ob=child()
ob.f1()

