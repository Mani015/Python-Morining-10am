# m=['mani','nitjin','pandu','agithya']
# n=[1,2,3,4,5]
# for i in m:
#     for k in n:
#         print(i,k)

# postrequest='succes'
# while(postrequest=='succes'):
#     x=input('name')
#     y=input('password')
#     print('Network connected')
# print('helloworld')

# k=[1,2,3,4,3,23,21,2,34,3,2,123,45,6,7,8,9,0,0,11,11,1,1,1,1,]
# l=[1 for i in range(k.count(1))]
# m=[i for i in l if i!=1]
# k.extend(l)
# print(k)
# l=['mani','a','b','v','d']
# data=f'{2}{1}{}'.format(l[1],l[3],l[2])
# print(data)
# c='heavenly father thank you for given this opportunity'
# g=c.split()
# print(g)









import os

# a=os.mkdir("C:\\Users\\DELL\\PycharmProjects\\pythonProject\\FILE")
# print(a)
# b=os.getcwd()
# print(b)
from threading import Thread
from time import  sleep
class math(Thread):
    def run(self):
        for i in range(10):

            print('i am good')
            sleep(1)


class math2(Thread):
    def run(self):
        for i in range(10):
            print('i an not good')
            sleep(1)

t1=math()
t2=math2()

t1.start()
sleep(0.2)
t2.start()





























