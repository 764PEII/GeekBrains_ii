class Stationary():
    def __init__(self,title):
        self.t = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationary):
    def draw(self):
        print('Серые тонкие линии')
class Pencil(Stationary):
    def draw(self):
        print('Синие тонкие лини')
class Handle(Stationary):
    def draw(self):
        print(f'{self.t} толстые лини')
s1 = Pen('simple')
s2 = Pencil('auto')
s3 = Handle('фиолетовые')
s1.draw()
s2.draw()
s3.draw()