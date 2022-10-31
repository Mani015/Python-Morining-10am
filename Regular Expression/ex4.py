import re

A='Class is blue print of object, object is a instance of class'
# Search:to test the specified pattren is present or not in the given input
r1=re.search(r'instance',A)
# print(r1)
# <re.Match object; span=(43, 51), match='instance'>

B='to test the specified pattren is present or not in the given input'
r2=re.search(r'nagaraju',B)
print('not match:',r2)
# None
