def f1():
    yield 10
    yield 20
    yield 30
    yield 40

ob=f1()
# print(ob)
print(ob.__next__())
# print(next(ob))
# print(next(ob))
# print(next(ob))

# for i in ob:
#     print(i)