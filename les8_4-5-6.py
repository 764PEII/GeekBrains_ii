def Err(arg):
    if arg.isdigit():
        return 'OK'
    else:
        raise Ex


class Ex(Exception):
    def __str__(self):
        return 'Error'


class Room:
    def __init__(self):
        self.a = 50
        self.b = 100
        self.h = 3
        self.list = {'high_power': [], 'meed_power': [], 'low_power': []}

    @staticmethod
    def organ(obj, list):
        if obj.power >= 60:
            list['high_power'].append(f'{obj}*{obj.k}')
        elif obj.power >= 20:
            list['meed_power'].append(f'{obj}*{obj.k}')
        elif obj.power < 20:
            list['low_power'].append(f'{obj}*{obj.k}')
        return list


class OrgTec:
    def __init__(self, power, k):
        self.k = k
        self.power = power
        self.U = 220
        self.job = False

    def on(self):
        self.job = True

    def off(self):
        self.job = False


class Printer(OrgTec):
    def __init__(self, paper, power, k):
        self.k = k
        self.job = False
        self.paper = paper
        self.power = power
        try:
            Err(self.k)
        except Ex:
            print(Ex())

    def print(self):
        self.paper -= self.k
        return print(f' Осталось бумаги {self}')


class Copier(OrgTec):
    def __init__(self, location, size, power, k):
        self.k = k
        self.job = False
        self.location = location
        self.size = size
        self.power = power
        try:
            Err(self.k)
        except Ex:
            print(Ex())


class Scan(OrgTec):
    def __init__(self, laser, v, power, k):
        self.k = k
        self.job = False
        self.laser = laser
        self.v = v
        self.power = power
        try:
            Err(self.k)
        except Ex:
            print(Ex())


obj_1 = Scan(0.3, 'high', 30, input('Введите количество объектов '))
obj_2 = Copier('local disk C', 'A4', 70, input('Введите количество объектов '))
obj_3 = Printer(48, 90, input('Введите количество объектов '))
obj_4 = Copier('local disk D', 'A3', 40, input('Введите количество объектов '))
obj_5 = Printer(24, 60, input('Введите количество объектов '))
room = Room()
save_1 = Room.organ(obj_1, room.list)
save_2 = Room.organ(obj_2, room.list)
save_3 = Room.organ(obj_3, room.list)
save_4 = Room.organ(obj_4, room.list)
save_5 = Room.organ(obj_5, room.list)
print(room.list)
