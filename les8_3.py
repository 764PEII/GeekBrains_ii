b = []
c = 0
k = 1
def Err(arg):
    if arg.isdigit():
        return 'OK'
    else:
        raise Ex
class Ex(Exception):
    def __str__(self):
        return 'Error'


while k == 1:
    a = input('Введите числа через пробел, для выхода нажмите q ')
    if a == 'q':
        break
    for i in range(len(a.split())):
        try:
            Err(a.split()[i])
        except Ex:
            print(Ex())
            break
        if a.split()[i] == 'q':
            k = 0
            break

        b.append(a.split()[i])
    print(b)
print(b)
