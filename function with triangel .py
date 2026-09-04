import math
def triangel():
    a = int(input('enter the value of a '))
    b = int(input('enter the value of b '))
    c = int(input('enter the value of c '))
    
    if ((a+b)>c and (c+b)>a and (a+c)>b ):
        s = (a+b+c) / 2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('the area of ', area)
    else:
        print('triangel is not possible ')



triangel()