# Basically ,abstraction hiding the internal implementation of a process or method from the used
# Class : which have abstract method
# Method:To declare an abstract class, we firstly needed to import the abc module.
from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def camera(self):
        print('this is mobile camere')



ob=Mobile()
ob.camera()
# TypeError: Can't instantiate abstract class Mobile with abstract method camera
