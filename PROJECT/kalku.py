awal = input("Apakah anda ingin menggunakan kalkualator?(Y/N)")

if awal == "Y":
    print("===========")
    print("Calculator")
    print("===========")
else:
    print("-")
angka1 = int(input("Masukan angka pertama:"))
print(f"angka pertama adalah {angka1}")
print("1 = tambah")
print("2 = kurang")
print("3 = kali")
print("4 = bagi")
operasi = input("Masukan operasi bilangan:")
print(f"operasimu adalah {operasi}")
angka2 = int(input("Masukan angka kedua:"))
print(f"angka kedua adalah {angka2}")
if operasi == "1":
    tambah= angka1+angka2
    print(f"Hasil : {tambah}")
elif operasi == "2":
    kurang= angka1-angka2
    print(f"Hasil : {kurang}")
elif operasi == "3":
    kali= angka1*angka2
    print(f"Hasil : {kali}")
elif operasi =="4":
    bagi= angka1//angka2
    print(f"Hasil : {bagi}")
else:
    print("Operasi tidak valid")




