from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def method(self):
        print('This all are the polygon diagrams')

class Rectangle(Polygon):
    def sides(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return 2*(self.length+self.breadth)

class triangle(Polygon):
    def sides(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return (self.a*self.b)/2

    def perimeter(self):
        return (self.a+self.b+self.c)

ob1=Rectangle()
ob1.sides(10,20)
ob2=triangle()
ob2.sides(12,13,14)
for i in [ob1,ob2]:
    print(i.area())
    print(i.perimeter())
