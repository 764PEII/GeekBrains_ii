from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def culc(self):
        pass


class Suit(Dress):
    def __init__(self, name, h):
        self.h = h
        self.name = name

    @property
    def culc(self):
        return 2 * self.h + 0.3


class Coat(Dress):
    def __init__(self, name, v):
        self.v = v
        self.name = name

    @property
    def culc(self):
        return self.v / 6.5 + 0.5


suit = Suit('Костюм',5)
coat = Coat('Пальто',4)

print(f'{suit.culc:.3f}, {coat.culc:.3f}')
print(f'Общий расход ткани равен: {suit.culc + coat.culc:.3f}')
