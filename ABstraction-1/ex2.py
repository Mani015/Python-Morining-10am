from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def camera(self):
        pass
    @abstractmethod
    def battery(self):
        pass

class Realme(Mobile):
    def camera(self):
        print('THis isexisting camera mathod')
    def battery(self):
        print('realme battery is 5000mah')



class oneplus(Mobile):
    def camera(self):
        print('This is one + camera')
    def battery(self):
        print('one+ battery is 6000mah')

ob=Realme()
ob.camera()
# THis isexisting camera mathod

ob=oneplus()
ob.camera()
ob.battery()