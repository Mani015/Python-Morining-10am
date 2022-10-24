# Decorator is higer order function, A function returns a another function
def outer(func):
    def inner():
        a=func()
        return a + '--->with decorator'
    return inner
@outer
def another():
    return 'using'
# ob=outer(another)
# print(ob())

print(another())
