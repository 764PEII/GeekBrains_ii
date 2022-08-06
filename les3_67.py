int_func = lambda word: word.title()
k = 1
while k:
    a = input('Введите слова с маленькой буквы ')
    b = a.split()
    for i in range(len(b)):
        v = b[i-1]
        for n in range(len(v)):
            if ord(v[n]) < ord('a') or ord(v[n]) > ord('z'):
                print('Пожалуйста, используйте маленькие латинские буквы')
                b.pop(i-1)
                break
        else:
            k = 0
a = (' '.join(b))
print(int_func(a))