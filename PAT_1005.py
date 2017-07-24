# -*- coding: utf-8 -*-
import re

seq = set([])  # 输入序列
overlap = set([])
n = input()
m = input().split(' ')
for i in range(int(n)):
    num = int(m[i])
    seq.add(num)   # 生成保存输入序列的list
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num + 1) / 2
        overlap.add(num)

ans = seq.difference(overlap)
ans_list = list(ans)
ans_list.sort(reverse=True)
m = len(ans_list)

for i in range(m):
    if i != m-1:
        print(ans_list[i], end=' ')
    else:
        print(ans_list[i], end='')

