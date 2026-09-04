import math 

class Eq:
    def __init__(self,a,b,c):
        d = ((b**2 )- (4*a*c))
        if (d < 0):
            print('roots are imaginary')
        elif d == 0:
            x = (-d/(2*a))
            print('one value', x)
        else:
            x1 = (- b + math.sqrt(d))/(2*a)
            x2 = (- b - math.sqrt(d))/(2*a)
            print('value x1', x1 , 'vlaue x2',x2)

a = int(input('enter value a '))
b = int(input('enter value b '))
c = int(input('enter value c '))
result = Eq(a,b,c)