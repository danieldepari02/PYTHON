class Flower:
    
    def __init__(self):
        self.nama = input('JENIS BUNGA        :')
        self.kelopak = int(input('JUMLAH KELOPAK     :'))
        self.price = int(input('HARGA SATUAN       :'))
        # print(f'Jenis Bunga     :{self.nama}')
        # print(f'Jumlah Kelopak  :{self.kelopak}')
        # print(f'Harga saturan   :{self.price}')
    #methods
    def harga_bunga(self):
        total = self.kelopak * self.price
        print(f'Harga bunga jenis {self.nama} dengan jumlah kelopak {self.kelopak} adalah {total}')
        
bunga = Flower()
bunga.harga_bunga()
