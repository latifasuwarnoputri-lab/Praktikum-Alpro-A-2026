class Baju:
    def __init__(self, merek, bahan, warna):
        self.merek = merek
        self.bahan = bahan 
        self.warna = warna

    def bahan(self):
     return print(f"bahan baju {self.merek} yaitu {self.bahan} ")

    def panjangLengan(self):
       print(f"lengan merek {self.merek} ini pendek")
    
P1 = Baju( "uniqlo", "poliester", "pink")
P2 = Baju( "glamor", "katun", "hitam")
P3 = Baju( "channel", "crinkle", "ungu")

print (P1.merek)
P1.merek = "dior"

print (P1.merek)
print(P1.bahan)
P2.panjangLengan()

