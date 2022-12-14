# Give a line space

import numpy as np

# a=np.linspace(2,2, num=100)
# print(a)

# Sum of values
n=np.array([(1,2,3,4),(2,3,4,5)])
# axis=1 means adding rows
print(n.sum(axis=1))


print(n.sum(axis=0))
# axis=0 adding columns
