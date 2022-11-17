
class parent:
    def method1(self,a,b,c):
        print(a+b+c)
class child(parent):
    def method1(self,a,b):
        print(a+b)

object=child()
object.method1(10,20)
object.method1(11,12,13)
# TypeError: method1() takes 3 positional arguments but 4 were given
