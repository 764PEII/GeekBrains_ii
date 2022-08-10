from random import randrange

a = [randrange(11) for u in range(20)]
b = []
c = []

for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
    else:
        b.append(a[i])

for u in range(len(c)):
    if c[u] in b:
        b.remove(c[u])

print(a)
print(b)
