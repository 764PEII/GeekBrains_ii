import json
# Извините, форматирование не получилось :_)
a = open('text_7.txt', 'r', encoding='utf-8')
k = 0
l = []
z = {}
for i in a:
    b = i.split()
    c = int(b[2]) - int(b[3])
    z.update({b[0]: c})
    if c > 0:
        l.append(c)
p = {'average': float(sum(l)) / len(l)}
l1 = [z, p]
print(l1)
with open('first_json', '+w', encoding='utf-8') as obj_f:
    json.dump(l1, obj_f)
a.close()
