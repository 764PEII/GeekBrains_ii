e = int(input('Введите номер месяца '))
b = [12, 2, 1]
a = [9, 10, 11]
c = [3, 4, 5]
d = [6, 7, 8]
dict = { 'a1' : 'autumn', 'b1' : 'winner', 'c1' : 'spring', 'd1' : 'summer' }
if e in b:
    print(dict['b1'])
if e in a:
    print(dict['a1'])
if e in c:
    print(dict['c1'])
if e in d:
    print(dict['d1'])
if e > 12 or e < 1:
    print('Вы должны ввести номер месяца')