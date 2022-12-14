import numpy as np
import time
list_size=10000

l1=range(list_size)
l2=range(list_size)
# print(l1+l2)
# TypeError: unsupported operand type(s) for +: 'range' and 'range'

start=time.time()

r1=[(x,y) for x,y in zip(l1,l2)]
print(r1)

print((time.time()-start)*1000)






















# d1={1:'a',2:'b'}
# d2={'a':11,'b':22}
# x={**d1,**d2}
# print(x)

n1=np.arange(list_size)
n2=np.arange(list_size)
print(n1+n2)
print((time.time()-start)*1000)