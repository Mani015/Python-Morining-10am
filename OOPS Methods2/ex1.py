# the init method or constructor in python.this mehtod is automatically called to allocate memory when anew objecy
# instance of a class is created.
class Fruits:
    def __init__(self,price,color,quantity,weight,taste,damagedpart):
        self.mrp=price
        self.co=color
        self.qua=quantity
        self.kg=weight
        self.ta=taste
        self.fault=damagedpart

# syntazx:print(object.attribute)

ob=Fruits(100,'red','5*','120grms','good',-0.2)
print(ob.qua)
print(ob.fault)
print(ob.ta)
print(ob.kg)
print(ob.co)

# 5*
# -0.2
# good
# 120grms
# red
