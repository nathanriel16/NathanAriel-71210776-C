class Mobil:
    _merk = " "
    _tipe = " "
    _kapasitasBBM = 0
    _jenisBahanBakar = " "

    def __init__(self, merk, tipe):
        self._merk = merk
        self._tipe = tipe
        self._kapasitasBBM = None
        self._jenisBahanBakar = None

    def setmerk(self, merk):
        self._merk = merk
    def settipe(self, tipe):
        self._tipe = tipe
    def setkapasitasBBM(self, liter):
        self._kapasitasBBM = liter
    def setjenisBahanBakar(self, tipebbm):
        self._jenisBahanBakar = tipebbm

    def getmerk(self):
        return self._merk
    def gettipe(self):
        return self._tipe
    def getkapasitasBBM(self):
        return self._kapasitasBBM
    def getjenisBahanBakar(self):
        return self._jenisBahanBakar
    
    def printInfo(self):
        return print("======INFO======\n",
        "Merk           :", self.getmerk(), "\n", 
        "Tipe           :", self.gettipe(), "\n",
        "Bahan Bakar    :", self.getjenisBahanBakar(), "\n",
        "Kapasitas BBM  :", self.getkapasitasBBM()
        )
    
    def isiBBM(self,harga):
        if self.getkapasitasBBM() is None or self.getjenisBahanBakar() is None:
            print('ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum diinputkan')
        else:
            print(f'Mengisi {self.getkapasitasBBM()} Liter')
            print(f'Total Harga : Rp{harga*self.getkapasitasBBM()}')

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()
    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setjenisBahanBakar("Bensin")
    mobil2.setkapasitasBBM(20)
    mobil2.printInfo()
    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)