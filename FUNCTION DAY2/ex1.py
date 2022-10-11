# Scope of variables
# Global variable
x=10
# print('Global variable:',x)
def fun():
    print('this is function')
    print("Global variable :",x)
    y=20
    print('Local varaible:',y)

fun()
print('Local variable',y)
