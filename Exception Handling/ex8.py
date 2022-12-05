
l1=[1,2,3,4,5,6,7,8,9]

try:
    print(l1[10])
except IOError as e:
    print('IO error is oocured')
except ValueError:
    print('this is value error')
except ZeroDivisionError:
    print('Zero division error')

except IndexError:
    print('index error is here')
except:
    print('error occured')

else:
    print('No error it will excute else block of statement')
finally:
    print('i ll call every time')

