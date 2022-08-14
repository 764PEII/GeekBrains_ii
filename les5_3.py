ff = open('text_3.txt', 'r', encoding='utf-8')
c = {}
list1 = []
a = [u.strip() for u in ff]
for i in range(len(a)):
    b = a[i].split()
    list1.append(float(b[1]))
    for t in b:
        if float(b[1]) < 20_000:
            z = {b[0]: b[1]}
            c.update(z)
# print(c)
# print(list1)
x = ', '.join(c.keys())
print(f'Всего сотрудников: {len(a)}\nСтвка меньше 20 000: {x}')
print('Средняя ставка сотрудников: ', f'{sum(list1) / len(list1):.4f}')

ff.close()