from functools import reduce

a = [u for u in range(100,1001) if u % 2 == 0]
c = 1
for i in range(len(a)):
    c = c * a[i]
print(c)

# Вариант методички
# def my_func(prev_el, el):
#     return prev_el * el
#
# x = reduce(my_func, a)
#print(x)

# проверка
# if x == c:
#     print('ok')