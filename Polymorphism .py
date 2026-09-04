class cat:
    def sound(self):
        print('cat make sound mewww !')

class cow:
    def sound(self):
        print('cow sound hamba hamba !')

for i in [cat(), cow()]:
    i.sound()