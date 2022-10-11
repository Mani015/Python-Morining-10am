x=10
def f1():
    global x
    x=20
    print(x)
    print(x)
f1()
print(x)