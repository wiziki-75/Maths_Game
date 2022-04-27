from random import *

def lvl1():
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    print(str(n1) + ' + ' + str(n2))

    n3 = n1 + n2

    result = input()

    if n3 == int(result):
        print('True \n')
        return True
    else:
        print('False \n')
        return False

def lvl2():
    n1 = randint(4, 10)
    n2 = randint(4, 10)
    print(str(n1) + ' x ' + str(n2))

    n3 = n1 * n2

    result = input()
    if n3 == int(result):
        print('True \n')
        return True
    else:
        print('False \n')
        return False
    
def lvl3():
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    n3 = randint(1, 10)
    print(str(n1) + ' + ' + str(n2) + ' x ' + str(n3))

    n4 = n1 + n2 * n3

    result = input()

    if n4 == int(result):
        print('True \n')
        return True
    else:
        print('False \n')
        return False