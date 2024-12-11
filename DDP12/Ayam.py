from Animal import *

class Ayam(Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak,
    jenis, suara):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.suara = suara
    def cetak_ayam(self):
        super().cetak()
        print("jenis \t\t\t:", self.jenis,
        "\nSuara \t\t\t:", self.suara)
    
siam = Ayam("Siam", "Dedak, padi", "Darat", "Bertelur", "Ayam Petarung",
"Kukuruyukk")
polandia = Ayam("Polandia", "Jagung, beras merah", "Darat", "Bertelur", "Ayam Hias", "Kukuruyuuk")
polandia.cetak_ayam()
siam.cetak_ayam()

    