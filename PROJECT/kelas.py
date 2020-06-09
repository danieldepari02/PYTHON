class Prisma:
    
    def __init__(self):
        self.alas = float(input('ALAS SEGITIGA   :'))
        self.tinggi = float(input('TINGGI SEGITIGA    :'))

    #methods
    def volume_prisma(self,tprisma):
        volume = 1/2*self.alas * self.tinggi*tprisma
        print(f'Volume prisma segitiga adalah {volume}')
    
    
prisma = Prisma()
tprisma = float(input('TINGGI PRISMA   :'))
prisma.volume_prisma(tprisma)