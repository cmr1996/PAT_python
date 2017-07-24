n = input()
num = int(n)
a = int(num / 100)
b = int((int(num % 100)) / 10)
c = int(num % 10)
str = []
for i in range(a):
    str.append('B')

for i in range(b):
    str.append('S')

for i in range(c):
    str.append(i+1)

for i in range(len(str)):
    print(str[i],end='')