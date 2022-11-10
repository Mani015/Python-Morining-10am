# Static varaible or class varaible:
# the static variable we  declared out side of the method and inside of the class then it is called c.v and static varaible
class Tv:
    # static varaible
    color='black'
    price=50000
    width='300cm'
    Brand='samsung'
    def m1(self):
        print('This is instance method')

# ob1=Tv()
# print(ob1.price)
# print(ob1.Brand)
# print(ob1.width)
# print(ob1.color)
# ob1.m1()

# # syntax:print(class name.attribute)
print(Tv.price)
print(Tv.color)
print(Tv.Brand)