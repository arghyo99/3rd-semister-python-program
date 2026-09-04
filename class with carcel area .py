import math
class circelarea:
    def __init__(self,a):
        area = math.pi*a**2
        print('circelarea is ', area)
a = float(input('enter value '))
result = circelarea(a)