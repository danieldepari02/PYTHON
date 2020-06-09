from datetime import date

def umur():
    age = (y-list2[0]+ extra)
    print('Umur anda adalah', age)

y = date.today().year
m = date.today().month
d = date.today().day

print('====================')
print('MENGHITUNG UMUR ANDA')
print('====================')
z = input ('Ingin tahun umur anda sekarang?(y/n) ')


while True:
    if z == 'y':
        x = input('Tuliskan tanggal lahir anda (yyyy mm dd)  ')
        list1 = x.split(' ')
        list2 = [int(list1[0]),int(list1[1]),int(list1[2])]
        if list2[1] < m:
            extra = 0
            umur()
            x = input('Tuliskan tanggal lahir anda (yyyy mm dd)  ')
        elif list2[1] > m:
            extra = -1
            umur()
            x = input('Tuliskan tanggal lahir anda (yyyy mm dd)  ')
        elif list2[1] == m and list2[2] > d:
            extra = -1
            umur()
            x = input('Tuliskan tanggal lahir anda (yyyy mm dd)  ')
        elif list2[1] == m and list2[2] <= d:
            extra = 0
            umur()
            x = input('Tuliskan tanggal lahir anda (yyyy mm dd)  ')
    else:
        break