temp = input().split(' ')
i = 0
j = 0
ans = []
while i < len(temp):
    if temp[i] != '0' and temp[i + 1] != '0':
        ans.append(str(int(temp[i]) * int(temp[i + 1])))
        ans.append(str(int(temp[i + 1]) - 1))

    i += 2

if not len(ans):
    print('0 0')
else:
    print(' '.join(ans))