class Human:                         # Super Class
    def __init__(self, name):
        self.__name = name             # Encapsulation

    def get_name(self):
        return self.__name


class Arghyo(Human):                 # Inheritance + Sub Class
    def run(self):                     # Polymorphism
        print(self.get_name(), "is running slowly!")


class Tanzim(Human):                 # Inheritance + Sub Class
    def run(self):                     # Polymorphism
        print(self.get_name(), "is running fast!")


arghyo = Arghyo("Arghyo")
Tanzim = Tanzim("Tanzim")

arghyo.run()
Tanzim.run()

