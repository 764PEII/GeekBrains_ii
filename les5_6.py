f = open('text_6.txt', 'r', encoding='utf-8')
c = []
l1 = []
b = f.read().split() # readline() для слабаков
print()
z = {}
for i in range(len(b)):
    if i%4 == 0:
        c.append(b[i])
for u in range(len(c)):
    for t in range(len(b)-1):
        if b[t] == c[u]:
            b.remove(b[t])
s = 1
for s in range((len(b))):
    if s%3 == 0:
        k = 0

    if b[s] == '-':
        s += 1
    else:
        try:
            m = int(b[s][:2])
            k += m
        except ValueError:
            m = int(b[s][:1])
            k += m
        s+=1
    if s%3 == 0:
        l1.append(k)

for i in range(len(c)):
    z.update({c[i]:l1[i]})
print(z)
f.close()