class Car():
    def __init__(self,speed,color,name,is_polic):
        self.s = speed
        self.c = color
        self.n = name
        self.ip = is_polic
    def go(self):
        print('car is go')
    def stop(self):
        print('car is stop')
    def turn(self,direction):
        print('car is turn on', direction)
    def show_speed(self):
        print('speed: ', self.s)
class TownCar(Car):
    def control(self):
        if self.s > 60:
            print('the speed is higher than allowed')

class SportCar(Car):
    name = 'SportCar'
    is_police = False
    def control(self):
        if self.s > 60:
            print('the speed is higher than allowed')

class WorkCar(Car):
    name = 'WorkCar'
    is_police = False
    def control(self):
        if self.s > 40:
            print('the speed is higher than allowed')

class PoliceCar(Car):
    name = 'PoliceCar'
    is_police = True

my_car_1 = TownCar(56,'purple','Colt',False)
my_car_2 = SportCar(76,'red','Tesla',False)
my_car_3 = WorkCar(46,'blue','Lada',False)
my_car_4 = PoliceCar(96,'white','Jeep',True)
my_car_1.turn('right')
my_car_2.control()
print(my_car_1.n, my_car_2.c,my_car_3.s,my_car_4.ip)
