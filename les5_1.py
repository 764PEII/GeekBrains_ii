f1 = open('text.txt', 'w', encoding='utf-8')

b = []
while True:
    a = input('Введите слова, для выхода оставьте строчку пустой ')
    c = a.split()
    if len(a) != 0:
        for i in range(len(c)):
            b.append(c[i])
            b.append('\n')
            # print(b)
    else:
        print(b)
        f1.writelines(b)
        break

f1.close()
