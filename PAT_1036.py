import math

tmp = input().split(' ')
n = int(tmp[0])
char = tmp[1]
print(n*char)
line = int(math.ceil(n/2))
k = line - 2
for i in range(k):
  print(char,(n-4)*' ',char)
print(n*char)
