# import threading
import time
from time import *


def f1(n):
    for i in range(10):
        time.sleep(0.1)
        print('square of n value:',n**2)


def f2(x):
    for i in range(10):
        time.sleep(0.2)
        print('cube of x value:',x**3)


# timetaken=time.time()
intial=time.time()
list=[1,2,3,4,5,6]
f1(10)
f2(5)
print('time taken with out threading:',time.time()-intial())
