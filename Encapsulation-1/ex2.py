# Public value, public access specifier

class parent:
    publicdata=100
    def publicmethod(self):
        print(self.publicdata)
class child(parent):
    def childmethod(self):
        print(self.publicdata)


ob=parent()
ob.publicmethod()

print('public data using out side of the function:',ob.publicdata)
# 100
# public data using out side of the function: 100

ob2=child()
ob2.childmethod()
print(ob2.publicdata)