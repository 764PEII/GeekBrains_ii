#сложное решение
def my_func(x, y):
    y = abs(y)*(-1)
    x = abs(x)
    c = 1
    for i in range(abs(y)):
        c = c*x
    print(x,'в степени',y , '=',1/c)

#лёгкое решение
# def my_func(x, y):
#     c = abs(x) ** (abs(y)*(-1))
#     print(abs(x),'в степени',abs(y)*(-1) , '=',c)


my_func(float(input('Введите действительное положительное число ')), int(input('введите целое отрицательное число ')))

