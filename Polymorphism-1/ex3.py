# Pip install mutlipledispatch
# pip : pacakage install for python
import multipledispatch as multipledispatch
import multipledispatch as dispatch


class parent:
    @multipledispatch.dispatch(int,int)
    def f1(self,x,y):
        print(x+y)
    @multipledispatch.dispatch(int,int,int)
    def f1(self,x,y,z):
        print(x+y+z)
    @multipledispatch.dispatch(str,str,str,str)
    def f1(self,x,y,z,a):
        print(x+y+z+a)



ob=parent()
# ob.f1(10,20)
ob.f1(10,20,50)
ob.f1(10,20)
ob.f1('pavan','kalyan','rajesh','python')