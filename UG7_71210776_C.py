class PrefixConverter:
    def _init_(self):
        self.stackList = ['?']

    # method untuk menambahkan data baru
    def push(self,data):
        self.stackList.append(data)

    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    # method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"

    def cekValidExpression(self,expression):
        # tuliskan code anda disini

    def infixToPrefix(self,expression):
        # Tuliskan code anda disini

# Test Case
if _name_ == '_main_':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))