class Road():
    _length = 200
    _width = 50
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def math(self):
        a = float((self.length * self.width * 25 * 5)/1000)
        print(a,'тонн')
l = float(input('Введите длинну дороги в метрах '))
w =float(input('Введите ширину дороги в метрах '))
obj_1 = Road(l,w)
obj_1.math()