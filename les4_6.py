from itertools import cycle,count
a = int(input('Введите нижнюю границу '))
b = int(input('Введите верхнюю границу '))
c = 1
d = []
if c == 1:
    for i in count(a):
        if i > b:
            c = 0
            print(d, '\n'*5)
            break
        else:
            d.append(i)
            print(i)

k = int(input('Введите количество повторений '))

if c == 0:
    for u in cycle(d):
        if c == k:
            break
        print(u)
        c+=1
