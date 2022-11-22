# protected data, protected access specifier,protectd member
# put [_] 'single underscore' before data & method to declared protected data or member

class parent:
    _protectedmember=10
    def protectedmethod1(self):
        print(self._protectedmember)
class child(parent):
    def protectedmethod2(self):
        print(self._protectedmember)


ob1=parent()
ob1.protectedmethod1()
print(ob1._protectedmember)

ob2=child()
ob2.protectedmethod2()
print(ob2._protectedmember)
