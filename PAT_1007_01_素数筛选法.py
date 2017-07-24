n = int(input())
prime = [True]*(n+1)

for i in range(2,int(n/2+1)):
    s = 2*i
    while s <= n:
        prime[s] = False
        s += i
#  以上为素数筛选法
cnt = 0
for i in range(5,n+1):
    if prime[i] and prime[i-2]:
        cnt += 1

print(cnt)



