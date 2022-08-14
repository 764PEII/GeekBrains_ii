f1 = open('text_4.txt', 'r', encoding='utf-8')
f2 = open('texttext', 'w+', encoding='utf-8')

a = f1.read().split('\n')
for i in range(len(a)):
    l = a[i].split()
    for u in range(len(l)):
        if l[u] == 'One':
            l[u] = 'Один'
        elif l[u] == 'Two':
            l[u] = 'Три'
        elif l[u] == 'Three':
            l[u] = 'Три'
        elif l[u] == 'Four':
            l[u] = 'Четыре'
        f2.write(l[u])
    f2.write('\n')
f2.seek(0)
print(f2.read())
f1.close()
f2.close()