
class parent:
    _a=10
    __b=20
    # '_parent__b'
    ___c_=30
    ____d=40
    # '_parent____d'
    __e__=50
    ____f___=60
    ______g=70
#     # '_parent______g'


# name mangling= atleast two underscore__(class name)_atmost one trailing underscore
# syntax:_classname__b_


# print(dir(parent))
# '_parent______g', '_parent____d', '_parent___c_', '_parent__b'
ob=parent()
print(ob.__e__)
print(ob.____f___)
# print(ob.__b)
# AttributeError: 'parent' object has no attribute '__b'
print(ob._parent__b)
print(ob._parent___c_)