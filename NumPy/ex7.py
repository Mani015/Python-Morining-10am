import numpy as np

np1=np.array([(1,2,3,4),(2,3,4,5),(1,2,3,5)])

# print('shape of np1:',np1.shape)
# shape of np1: (3, 4)
# shape of np1: (rows, colums)

print('reshape of np1:',np1.reshape(4,3))

# reshape of np1: [[1 2 3]
#  [4 2 3]
#  [4 5 1]
#  [2 3 5]]
