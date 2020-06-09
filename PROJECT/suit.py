import random

def com():
    x = random.randrange(1,3)
    if x == 1:
        x = 'Rock'
    elif x == 2:
        x = 'Paper'
    else:
        x = 'Scissors'
    # print(x)
    y = input('Rock/Paper/Scissors?  ')
    while True:
        if x == 'Rock' and y == 'Paper': 
            print('You win!!!')
            break
        elif x == 'Rock' and y == 'Scissors':
            print('You lose...')
            y = input('Rock/Paper/Scissors?  ')
        elif x == 'Rock' and y == 'Rock':
            print('You Tie')
            y = input('Rock/Paper/Scissors?  ')
        elif x == 'Paper' and y == 'Rock':
            print('You lose...')
            y = input('Rock/Paper/Scissors?  ')
        elif x == 'Paper' and y == 'Scissors':
            print('You Win !!!')
            break
        elif x == 'Paper' and y == 'Paper':
            print('You Tie')
            y = input('Rock/Paper/Scissors?  ')
        elif x == 'Scissors' and y == 'Scissors':
            print('You Tie')
            y = input('Rock/Paper/Scissors?  ')
        elif x == 'Scissors' and y == 'Paper':
            print('You lose...')
            y = input('Rock/Paper/Scissors?  ')
        elif x == 'Scissors' and y == 'Rock':
            print('You Win !!!')
            break

com()