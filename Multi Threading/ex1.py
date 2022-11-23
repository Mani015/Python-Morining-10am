import threading

t=threading.main_thread().getName()
# print(t)
# <_MainThread(MainThread, started 4208)>
# main thread

t1=threading.currentThread().getName()
# print(t1)
# MainThread


if t==t1:
    print('This is main thread')
else:
    print('This is not main thread')
# This is main thread
