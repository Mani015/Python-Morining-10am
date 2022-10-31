import sys
def fun(n):
    list=[]
    for i in range(1,11):
         list.append(f'{n}x{i}={n*i}')
    yield list

ob=fun(5)
s=sys.getsizeof(ob)
print('yield taken size:',s)
for i in ob:
    print(i)

