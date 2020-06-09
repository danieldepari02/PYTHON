import time

buron = {}
daftar = []

def data():
    name = input('Siapa nama buronan: ')
    age = input('Berapa umur buronan: ')
    criminal = input('Apa kejahatannya:')
    
    return name, age, criminal

def vertikal(daftars):
    for daftar in daftars:
        for key, value in daftar.items():
            print(key, value)
        print(' ')

def load():
    for a in range(1,4):
        time.sleep(0.2)
        for b in range(5,0,-1):
            time.sleep(0.2)
            print(f'loading{"."*b}') 

def awal():
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
        print ('   ')
    else:
        print('Password salah, akses dilarang')           

z=input('Password? ')
awal()



while True:
    buron = {}
    # nama, umur, criminal = daftar()
    name = input('Siapa nama buronan: ')
    age = input('Berapa umur buronan: ')
    criminal = input('Apa kejahatannya:')
    buron['name     :'] = name
    buron['age      :'] = age
    buron['criminal :'] = criminal
    # print(buron)
    daftar.append(buron)
    # print(daftar)

    again = input('Apakah mau menambah lagi(y/n)?  ')
    if again == 'y':
        continue
    else:
        print(len(daftar),'IDENTIFIED')
        break
vertikal(daftar)