a = str(input('введите слова через пробел: '))
b = a.split()
for i in range(len(b)):
    print((i+1), '. ', f"{b[i]:.10}")