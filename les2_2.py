a = []
c = 0
print('введите числа, a для завершения работы программы введите end ')
while True:
    b = input()
    a.append(b)
    if b == 'end':
        a.pop(-1)
        print(a)
        for i in range(len(a)-1):
            if i % 2 == 0:
                c = a[i + 1]
                a[i + 1] = a[i]
                a[i] = c
            else:
                i += 1
        print(a)
        break
