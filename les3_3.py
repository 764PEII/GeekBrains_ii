# Решение номер один
def my_func(arg1, arg2, arg3):
    a = [arg1, arg2, arg3]
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    print(max1, '+', max2, '=', max1 + max2)


my_func(int(input('Введите аргумент №1 ')), int(input('Введите аргумент №2 ')), int(input('Введите аргумент №3 ')))

# Решение номер два

# def my_func2(arg1, arg2, arg3):
#     a = [arg1, arg2, arg3]
#     minim = min(a)
#     a.remove(minim)
#     print(sum(a))
#
# my_func2(int(input('Введите аргумент №1 ')), int(input('Введите аргумент №2 ')), int(input('Введите аргумент №3 ')))
