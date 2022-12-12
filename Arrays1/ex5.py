from array import  array
arr1=array('i', [1, 2, 3, 4, 5, 6])
# print(arr1)
# print(type(arr1))

# print(arr1[2])
# 3
arr1.reverse()
# print(arr1)
# array('i', [7, 6, 5, 4, 3, 2, 1])


# print(arr1.buffer_info())
# (3028448057936, 6)

print(arr1.tolist())
# [6, 5, 4, 3, 2, 1]

print(arr1.count(2))
# 3



