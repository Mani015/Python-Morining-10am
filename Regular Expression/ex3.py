# match():It is used to test ,the  input string start with the specified pattren (or) not

# On success: it returns the match object
# on failure: it returns the None

import re

x='Python is general-purpose programming language and also object oriented language'
y=re.match(r'Python',x)
# print('on success:',y)
# on success: <re.Match object; span=(0, 6), match='Python'>

# ON FAILURE-CASE
z=re.match(r'is',x)
# print('on failure:',z)
# NOne

# Using with.... out of senctence
r1=re.match(r'bharath',x)
print(r1)
# None
