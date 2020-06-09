import time
def gaji():
    jam = int(input("Berapa jam kamu kerja: "))
    gj = int(input("Berapa gajimu per jam : "))
    if jam > 10:
        y= jam*gj+1000
        time.sleep(0.5)
        print(f'Gajimu adalah:\n {y}')  
    elif jam <=10:
        y= jam*gj
        time.sleep(0.5)
        print(f'Gajimu adalah:\n {y}')

x=input('Anda ingin menghitung gaji(Y/N): ')
while True:
    if x == "Y":
        gaji()
        time.sleep(0.5)
        x=input('Anda ingin menghitung gaji(Y/N): ')
    elif x == "N":
        break