class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
       self._data = [None] * Kasir.DEFAULT_CAPACITY
       self._size = 0
       self._front = 0

       
    def __len__(self): #mengembalikan ukuran Queue
        return self._size

    def is_empty(self): #mengecek apakah Queue kosong ?
        return self._size == 0

    def dequeue(self): #menghapus data paling depan (front)
        if self.is_empty():
            print("Kosong")
        ngarep = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ngarep

    def enqueue(self, namaPelanggan): #menambah data ke list
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = namaPelanggan
        self._size += 1
        
    def resize(self, cap): #mengubah ukuran queue pada list
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        m = len(self._data) -1
        n = 1
        print("===Kasir===")
        for i in range (0, len(self._data)):
            if i <= m:
                print(n,".",self._data[i], end='')
                print()
            else:
                print(n,". Kosong")
            n += 1

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

