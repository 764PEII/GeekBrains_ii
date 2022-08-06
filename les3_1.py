div = lambda a1, a2: round(a1 / a2, 3)

a = int(input('Введите делимое '))
b = int(input('Введите делитель '))
if b == 0:
    print('деление на ноль невозможно')
print(div(a, b))
