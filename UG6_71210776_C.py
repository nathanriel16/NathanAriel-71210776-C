class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self._norekening = no_rekening
        self._nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self) :
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def kosong(self):
        return self._size == 0
    
    def insert_head(self, a):
        baru = NodeTabungan(a, None)
        if self.kosong() == True:
            self._head = baru
            self._tail = baru
            self._tail.next = None
            
        else:
            baru.next = self._head
            self._head = baru
        self._size += 1
        print("data masuk ke rekening!")
    
    def update(self,a):
        baru = NodeTabungan(a, None)
        if self._tail == None:
            self._head = baru
            self._tail = baru
            self._tail.next = None
        else:
            self._tail.next = baru
            self._tail = baru
        self._size +1
        print("data masuk tail!")

    def filter(self):
        if self.kosong() == False:
            d = None
            bantu = self._head
            if(self._head != self._tail):
                while bantu.next != self._tail:
                    bantu = bantu.next
                hapus = self._tail
                self._tail = bantu
                d = hapus.saldo
                del hapus
                self._tail.next = None
                print(d)
            else:
                d = self._tail.saldo
                self._head = tail = None
            self._size -= 1

    # def delete(self, post):
    #     if self._size == 0:
    #         return False
    #     elif post == 0:
    #         self.delete_head()
        



    # def printt(self):



#slnc = SLNC()
# slnc.insert_head(201,"Hanif", 250000)
# slnc.insert_head(110,"Yudha", 150000)
# slnc.print()
# slnc.filter(100)
# slnc.print()
# slnc.update(200)
# slnc.update(50)
# slnc.printt()