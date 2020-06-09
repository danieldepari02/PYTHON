import time

print('THIS IS A GAME')
for a in range(1,4):
    for b in range(5,0,-1):
        time.sleep(0.5)
        print(f'loading{"."*b}')  
print('Welcome to the game')