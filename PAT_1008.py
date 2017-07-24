# -*- coding=utf-8 -*-

seq1 = input().split(' ')
N1 = seq1[0]
N = int(N1)
M1 = seq1[1]
M = int(M1)
NUM = input().split(' ')
DFT = NUM[::]
M = int(M % N)  # 处理大于一个周期的移位
for i in range(N):
    if i+M < N:
        DFT[i+M] = NUM[i]
    else:
        DFT[i+M-N] = NUM[i]


for j in range(N):
    if j!=N-1 :
        print(DFT[j],end=' ')
    else:
        print(DFT[j],end='')



