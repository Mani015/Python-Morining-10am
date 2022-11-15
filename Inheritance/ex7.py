class Gparent:
    a=100
class parent(Gparent):
    b=100


class child(parent):
    def f1(self):
        self.c=200
        print(self.a +self.b+self.c)

ob1=child()
ob1.f1()
