import numpy as np

n1=np.array([1,2,3,4])
# print(n1)
# [1 2 3 4]
# To find number of dimensions
# print(np.ndim(n1))
# 1





n2=np.array([(1,2,3,4),('a','b','c','d')])
print(n2)
# [['1' '2' '3' '4']
#  ['a' 'b' 'c' 'd']]

print(np.ndim(n2))
# 2
