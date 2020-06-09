import random

x = random.randrange(1,100)
print(x)
age = int(input("Berapa umur adik saya? "))
while True:
    if x == age:
        print("Bener, jago juga lu")
        break
    elif x <= age:
        print("Adik saya gk setua itu")
        age = int(input("coba lagi ya "))
    else:
        print("Kemudaan bro")
        age = int(input("coba lagi ya "))