import random

def awal():
    print('DICE ROLL SIMULATOR')
    print('===================')
    x= input('Ready to start? (y/n)')
    while True:
        if x == 'y':
            z = random.randrange(1,6)
            print('You have rolled:', z)
            print('Bye!')
            print(' ')
            x= input('Try Again? (y/n)')
        else:
            break

awal()