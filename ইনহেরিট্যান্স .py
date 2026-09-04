class animal:
    def what(self):
        print('it is animal')

class cat(animal):
    def sound(self):
        print('cat make sound meww')

d = cat()

d.what()
d.sound()