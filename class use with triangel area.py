class triangel:
    def __init__(self,a,b,c):
        import math 
        if ((a+b)>c and (c+b)>a and (a+c)>b ):
            s = (a+b+c) / 2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print('area result', area)

        else:
            print('triangle is not possible')
a = float(input('enter  a value'))
b = float(input('enter  b value'))
c = float(input('enter  c value'))

result = triangel(a,b,c)

