class BigNumber:
    def __init__(self,a,b,c):
        if ((a>b) and (a>c)):
            print('a is a biggest number',a)
        elif ((b>a) and (b>c)):
            print('b is a biggest number',b)
        else:
            print('c is a biggest number',c)
a= int(input('enter numer a '))
b= int(input('enter numer b '))
c= int(input('enter numer c '))
result = BigNumber(a,b,c)
