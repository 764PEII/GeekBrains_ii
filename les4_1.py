import sys
def zp():
    #print('Введите ставку на час и выработку')
    l, money, time, big_money = sys.argv
    print('Зарплата сотрудника составляет', int(time)*int(money)+int(big_money))
zp()