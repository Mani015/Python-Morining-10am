def fun(n):
    list=[]
    for i in range(1,11):
         list.append(f'{n}x{i}={n*i}')
    return list

ob=fun(5)
for i in ob:
    print(i)




# s='python'
# print('class is',f'{s}')