from random import randrange
a = [randrange(101) for u in range(20)]
b = []
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        b.append(a[i+1])
print(a)
print(b)