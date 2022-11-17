# The literal meaning of polymorphism is the condition of occurrence in different forms.

# Polymorphism is a very important concept in programming.
# It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
# One person can do a mulitple task's
# poly=many
# mers=forms

# There are two types here:
# 1)method over loading
# 2)method over riddingf


# method over loading
# method overloading is the ability of have multiple methods with same name but a different of parameters
# if class contains more than one method has same name & the method contains different datatypes
# python doesn't supproot the method overloading

class parent:
    def f1(self,x,y):
        print(x+y)
    def f1(self,x,y,z):
        print(x+y+z)
ob=parent()
ob.f1(10,20,30)
ob.f1(20,30)
# TypeError: f1() missing 1 required positional argument: 'z'
# 60