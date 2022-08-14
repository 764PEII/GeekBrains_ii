f = open('text5.txt', 'w+', encoding='utf-8')

a = input('Введите числа через пробел ')
x = []
f.write(a)
f.seek(0)
z = f.read().split()
x = [int(z[i]) for i in range(len(z))]
print(sum(x))
f.close()
