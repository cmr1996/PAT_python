str = input().split(' ')
A = str[0]
Pa = str[1]
B = str[2]
Pb = str[3]

temp_A = ' '
for i in range(len(A)):
    if Pa == A[i]:
        temp_A = temp_A + Pa

if temp_A != ' ':
    ans_A = int(temp_A)
else:
    ans_A = 0

temp_B = ' '
for i in range(len(B)):
    if Pb == B[i]:
        temp_B = temp_B + Pb

if temp_B != ' ':
    ans_B = int(temp_B)
else:
    ans_B = 0

ans = ans_A + ans_B
print(ans)