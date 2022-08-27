def culc(arg_1, arg_2):
    if arg_2 == 0:
        raise MyError
    else:
        return print(f'{arg_1/arg_2:.3}')

class MyError(Exception):
    def __str__(self):
        return 'Делить на 0 нельзя'


try:
    culc(int(input('Введите делимое: ')) ,int(input('Введите делитель: ')))
except MyError:
    print(MyError())