
# we are using single inheritance

class parent:
    __privatedata=20
    def m1(self):
        print(self.__privatedata)
class child(parent):
    def m2(self):
        print(self.__privatedata)


ob2=child()
ob2.m2()
# AttributeError: 'child' object has no attribute '_child__privatedata'
# print(ob2.__privatedata)
# AttributeError: 'child' object has no attribute '_child__privatedata'