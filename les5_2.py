f = open('text3.txt', 'r', encoding='utf-8')
b = []
n = []
a = [i.strip() for i in f]
print(a)
for u in range(len(a)):
    k = 1
    l = a[u]
    for t in range(len(l)):
        if l[t] == ' ':
            k += 1
    n.append(k)
    c = ['str nomber ', u + 1, n[u], ' words']
    b.append(c)
print([b[g] for g in range(len(b))])
print('всего строк',len(a))
f.close()
