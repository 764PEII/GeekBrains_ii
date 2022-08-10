a = [5, 3, 2, 1]
print(a)
b = int(input('Введите число, которое займёт своё место в данном рейтинге '))
if b <= a[-1]:
    a.append(b)
elif b == max(a):
    a.reverse()
    a.append(b)
    a.reverse()
else:
    for i in range(len(a)-1):
        if b > a[i]:
            a.insert(i, b)
            break
print(a)