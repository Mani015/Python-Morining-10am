# With out using decorator
def outer(func):
    def inner():
        a=func()
        return a + 'with out decorator'
    return inner

def another():
    return 'using'
ob=outer(another)
print(ob())