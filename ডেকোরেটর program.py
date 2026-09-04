def halo(fun):
    def wellcome():
        print('before finction')
        fun()
        print('after finction')

    return wellcome

@halo
def say_again():
    print('Hi, Arghyo')

say_again()