import time

def load():
    for a in range(1,4):
        time.sleep(0.2)
        for b in range(5,0,-1):
            time.sleep(0.2)
            print(f'loading{"."*b}') 

def count(dictionary):
    borun = list(dictionary.keys())
    for x in borun:
        num = borun.count(x)
        print(len(borun),'IDENTIFIED')
    # list1 = [dictionary.values()]
    # print(len(list1))

buronans = {}

def buron():
    while True:
        nama = input('Name: ')
        umur = input('Age: ')
        criminal = input('Criminal: ')
        buronans[nama] = umur,criminal
        add = input('Ada lagi?(Y/N)')
        if add == 'Y':
            continue
        else:
            break

z=input('Password? ')
while True:
    if z == '0211':
        time.sleep(0.2)
        print('-------------------------')
        time.sleep(0.2)
        print('BURONAN UTAMA KEPOLISIAN')
        time.sleep(0.2)
        print('-------------------------')
        print ('   ')
        load()
        print ('   ')
        buron()
        print ('   ')

        break
    else:
        print('Password salah, akses dilarang')
        break
count(buronans)