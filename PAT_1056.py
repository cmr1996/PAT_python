inp = input().split(' ')
tmp = inp[1:]
lenth = len(tmp)
sum = 0
for i in range(lenth):
    for j in range(lenth):
        if tmp[i] != tmp[j]:
            m = tmp[i] + tmp[j]
            n = int(m)
            sum = sum + n

print(sum, end='')