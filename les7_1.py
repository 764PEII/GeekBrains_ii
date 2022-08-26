class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix0 = []
        self.matrix1 = []
        for i in range(len(self.matrix)):
            k = self.matrix[i]
            for t in range(len(k)):
                self.matrix0.append(k[t])

    def __str__(self):
        return f'{self.matrix1}'


    def __add__(self, other):
        for y in range(len(self.matrix0)):
            self.matrix1.append((self.matrix0[y]) + int(other.matrix0[y]))
        return Matrix(str(self.matrix1)), self.matrix1


obj_1 = Matrix([[1, 2], [3, 4], [5, 6]])
obj_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(obj_1+obj_2)
