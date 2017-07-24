STR = input().split(' ')

num = []
for j in range(len(STR)):
  k = int(STR[j])
  for l in range(k):
    num.append(str(j))

flag = -1
for i in range(len(num)):
    if num[i] != '0':
        flag = i
        break

if flag == 0:
    print(''.join(num))
else:
    num[0] = num[flag]
    num[flag] = '0'
    print(''.join(num))