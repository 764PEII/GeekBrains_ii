class Worker():
    def __init__(self, n, s, p, w, b):
        self.n = n
        self.s = s
        self.p = p
        self._i = {'wage': w, 'bonus': b}

class Position(Worker):
    def full_name(self):
        print(self.n,' ', self.s,' Занят на должности: ',self.p)
    def total_income(self):
        print('Доход: ',self._i['wage']+self._i['bonus'])
a = input('Введите имя, фамилию, должность, регулярный доход и премию: ').split()
peopl = Position(a[0],a[1],a[2],float(a[3]),float(a[4]))
peopl.full_name()
peopl.total_income()