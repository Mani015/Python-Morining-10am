class Fruits:
    def __init__(self,price,color,quantity,weight,taste,damagedpart):
        # Instance method or constructor

        self.mrp=price
        # instance variable
        self.co=color
        self.qua=quantity
        self.kg=weight
        self.ta=taste
        self.fault=damagedpart
    def display(self):
        print(self.mrp)
        print(self.co,self.qua,self.kg,self.ta,self.fault)

ob=Fruits(120,'green','5*','2kg','spicy',0.0)
ob.display()
ob1=Fruits(130,'yellow',2,'10kg','sweet',0)
ob1.display()


