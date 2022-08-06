b = []
c = 0
k = 1
while k == 1:
    a = input('Введите числа через пробел, для выхода нажмите q ')
    if a == 'q':
        break

    for i in range(len((a.split()))):
        if a.split()[i] == 'q':
            k = 0
            break

        b.append(int(a.split()[i]))

    print(sum(b))


