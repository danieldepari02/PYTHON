import time
z=input('Password? ')
def load():
    for a in range(1,4):
        time.sleep(0.2)
        for b in range(5,0,-1):
            time.sleep(0.2)
            print(f'loading{"."*b}') 
def buron():
    dic = {"nama": "Cei", "umur": 20, "crime":"Nyolong pisang"}
    dic2 = {"nama": "Pang", "umur": 19, "crime":"Perdagangan Manusia"}
    dic3 = {"nama": "Pao", "umur": 30, "crime":"Penculikan anak"}
    list1 = [dic,dic2,dic3]
    print(len(list1),"Ditemukan")

    for x in list1:
        time.sleep(0.5)
        print(f'Name        : {x["nama"]}')
        time.sleep(0.5)
        print(f'Age         : {x["umur"]}')
        time.sleep(0.5)
        print(f'Crime       : {x["crime"]}')
        print ('   ')
while True:
    if z == '02112002':
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