def f1():
    n=1
    while n<=10:
        square=n*n
        yield square
        n+=1
ob=f1()
for i in ob:
    print(i)
