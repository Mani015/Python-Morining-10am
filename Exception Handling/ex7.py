
list=[11,22,33,44,55,66]
a=10
b=0

try:
    print(a/b)
except IOError as e:
    print('IO error is oocured')
except ValueError:
    print('this is value error')
except ZeroDivisionError:
    print('Zero division error')

except:
    print('error is occured')

else:
    print('No error it will excute else block of statement')
finally:
    print('i ll call every time')

