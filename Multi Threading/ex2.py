from time import *
from threading import *


# class threading

class whatsapp(Thread):
    def run(self):
        for i in range(100):
            print('using whatsapp')
            sleep(2)


class telegram(Thread):
    def run(self):
        for i in range(100):
            print('using telegram')
            sleep(1)



t1=whatsapp()
t2=telegram()

t1.start()
sleep(0.1)
t2.start()
