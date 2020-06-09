nama = input('masukkan nama anda ...')
nilai = int(input('masukkan nilai kalian:'))

if nilai >= 90:
    grade = "A"
    print(f'Nilai kamu {nilai} dengan peringkat {grade}.Luar biasa,{nama}!!!')
if nilai >= 80:
    grade = "B"
    print(f'Nilai kamu {nilai} dengan peringkat {grade}.Tingkatkan terus ya,{nama}!!!')
if nilai >= 70:
    grade = "C"
    print(f'Nilai kamu {nilai} dengan peringkat {grade},Tetap semangat ya,{nama}!!!')
else:
    grade="D"
    print(f'Nilai kamu {nilai} dengan peringkat {grade}, Kurang beruntung,{nama}')