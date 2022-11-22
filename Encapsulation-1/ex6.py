# Name mangling:declare data or method with atleast two leading underscores and atmost one trailing underscrore.
# Then it will be replace to class name name by the interpreter

class parent:
    _a=10
    # private data
    __b=20
    #
    ___c_=30
    ____d=50
    __f__=60
    ____s___=80

print(dir(parent))


#  '__str__', '__subclasshook__', '__weakref__', '_a', '_parent____d', '_parent___c_', '_parent__b']
# ____s___', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__f__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__'