# Private member,private access specifier,private access modifier

# put [__] 'double underscore' before data & method to declared protected data or member

class parent:
    __privatedata=500
    def m1(self):
        print(self.__privatedata)

ob1=parent()
ob1.m1()

# We are trying to get out side of the class ,in a private data

print(ob1.__privatedata)
# AttributeError: 'parent' object has no attribute '__privatedata'