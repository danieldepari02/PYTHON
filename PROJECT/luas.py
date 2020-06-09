def luas_persegi():
    area = p*l
    print("Luas =",area)
def luas_segitiga():
    luas = (a*t)/2
    print("Luas =",luas)
x=input('Mau Hitung luas Persegi atau Segitiga: ')
while True:
    if x == "Persegi":
        p = int(input("panjang: "))
        l = int(input("lebar: "))
        luas_persegi()
        x=input('Mau Hitung luas Persegi atau Segitiga: ')
    elif x == "Segitiga":
        a = int(input("Alas: "))
        t = int(input("Tinggi: "))
        luas_segitiga()
        x=input('Mau Hitung luas Persegi atau Segitiga: ')