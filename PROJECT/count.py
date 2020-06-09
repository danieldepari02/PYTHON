import time

print('COUNTDOWN')
print('^^^^^^^^^^')

a = int(input('How long:'))
read = input('Ready to start?(Y/N)')
if read == 'Y':
    while a >0:
        time.sleep(0.5)
        print(a)
        a -= 1
    time.sleep(0.5)
    print('YOUR TIME IS DONE')

    