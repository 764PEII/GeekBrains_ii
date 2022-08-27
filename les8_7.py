class ComplexChar:
    def __init__(self, integer, complex):
        self.integer = integer
        self.complex = complex

    def __str__(self):
        return f'real: {self.integer}, complex: {self.complex}i'

    def __add__(self, other):
        return ComplexChar((self.integer + other.integer), (self.complex + other.complex))

    def __mul__(self, other):
        return ComplexChar(((self.integer*other.integer)-(self.complex*other.complex)),((self.integer*other.integer)+(self.complex*other.complex)))
a = ComplexChar(3, 9)
b = ComplexChar(10, 3)
print(f'{a}\n{b}\n\n\n{a + b}\n{a * b}')
