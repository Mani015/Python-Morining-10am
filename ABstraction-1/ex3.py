
from abc import ABC ,abstractmethod

class Car(ABC):
    @abstractmethod
    def speed(self):
        pass
    @abstractmethod
    def series(self):
        pass
    # concrete method
    def concrete(self):
        print('This is concrete method')
    def con1(self):
        print('this car is amazing')
class BMW(Car):
    def speed(self):
        print('speed of car is 1200/hr')
    def series(self):
        print('BMW is the 7th series of model')
ob=BMW()
ob.speed()
ob.series()
ob.concrete()
# speed of car is 1200/hr
# BMW is the 7th series of model
# This is concrete method
ob.con1()
# this car is amazing