import math

def IsPrime(m):
    if m < 2:
        return False
    elif m == 2:
        return True
    else:
        i = 2
        temp = int(math.sqrt(m))
        while i <= temp:
            if m%i == 0:
                return False
            i += 1

        return True

n = input()
n = int(n)
prime = []
for i in range(n):
    if IsPrime(i):
        prime.append(i)

k = 0
prime_count = 0
while k+1 < len(prime):
    d = prime[k+1] - prime[k]
    if d == 2:
        prime_count += 1
    k += 1

print(prime_count)



