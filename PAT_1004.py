import re

n = input()
b = []
d = {}
for i in range(int(n)):
    s = input()
    a = re.split(r'\s+',s)
    d[int(a[2])] = a[0] + ' ' + a[1]
    b.append(int(a[2]))

print(d[max(b)])
print(d[min(b)])