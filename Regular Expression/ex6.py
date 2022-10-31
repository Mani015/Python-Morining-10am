print('WELCOME TO CANDY CRUSH')
n=str(input('Enter your name'))
if n=='pavan':
    print('log in success')
    l1=int(input('Enter your number:'))
    if l1==1:
        print('first level completed')
        l2=int(input('Ennter tour number:'))
        if l2==2:
            print('second level complted')
            l3=int(input('Ennter tour number:'))
            if l3==3:
                print('third level successfully compltedede')
            else:
                print('third level unsuccessfully')
        else:
            print('second level in complteded')
    else:
        print('incompleted 2nd level')
else:
    print('you have enter wrong name')

