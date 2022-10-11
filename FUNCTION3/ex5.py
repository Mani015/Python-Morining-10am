a=150
print('global variable:',a)
def f1():
    x1=100
    print('local variable:',x1)
    print('global varaible:',a)
    def f2():
        y1=200
        print('local v:',y1)
        print('enclosing  v:',x1)
        print('global variable;',a)
    f2()
    print('g v:',x1)
    print(a)
f1()
print('global variable:',a)