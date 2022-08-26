class Cell:
    def __init__(self,k):
        self.k = k
    def __add__(self, other):
        return self.k + other.k
    def __sub__(self, other):
        return self.k - other.k
    def __mul__(self, other):
        return self.k*other.k
    def __truediv__(self, other):
        return f'{self.k/other.k:.0f}'
    def make_order(self):
        if (self.k)%5 == 0:
            for u in range(int(self.k/5)):
                print('*****') # or print('*****\n')
        else:
            self.list = []
            if self.k // 5 == 0:
                for u in range(self.k):
                    self.list.append('*')
            else:
                for i in range(self.k//5):
                    self.list.append('*****\n')
                for t in range(self.k%5):
                    self.list.append('*')

            print(''.join(self.list))




cell_0 = Cell(14)
cell_1 = Cell(15)
cell_0.make_order()
print(cell_1-cell_0, cell_0+cell_1, cell_1*cell_0, cell_1/cell_0)