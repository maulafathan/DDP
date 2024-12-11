from Animal import *

class Burung(Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak,
    jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_burung(self):
        super().cetak()
        print("jenis \t\t\t:", self.jenis,
        "\nBunyi \t\t\t:", self.bunyi)
    
gereja = Burung("Gereja", "Biji bijian", "Udara", "Bertelur", "Sparrow Weaver",
"NGAKNGAKKKK")
elang = Burung("Elang", "Daging Hewan Mamalia", "Pohon tinggi", "Bertelur", "Elang laut steller",
"Bernada tinggi")
gereja.cetak_burung() 
elang.cetak_burung()
    