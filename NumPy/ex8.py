import numpy as np

np1=np.array([(1,2,3,4),(2,3,4,5),(1,2,3,5)])

# Slicing

# print(np1[(0)])
# [1 2 3 4]

# print(np1[0,2])
# 3


# print(np1[0,-1])
print(np1[1,2:])
# [4 5]
print(np1[-1])
# [1 2 3 5]