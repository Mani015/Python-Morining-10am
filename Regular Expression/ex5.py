# Find all
import re

C='list is a coolection of data '
r1=re.findall(r'is',C)
# print('It find:',r1)
# [is, is]

D='prevention is better than cure'
r2=re.findall(r'cool',D)
print(r2)
# []

