def fact(arg):
    a = 1
    for i in range(arg):
        a = (i+1)*a
        yield(a)

n = int(input('Число, которое нужно возвести в факториал '))
for u in fact(n):
    print(u)