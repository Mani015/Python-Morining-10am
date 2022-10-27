def fun(n):
    for i in range(1,11):
        yield (n,'x',i,'=',n*i)
ob=fun(8)
# print(ob)
for i in ob:
    print(i)