n = int(input())
# 初始化
cj = [0 for x in range(n + 1)]

for j in range(n):
    tmp = input().split(' ')
    m = int(tmp[0])
    n = int(tmp[1])
    cj[m] += n

ans1 = cj.index(max(cj))
ans2 = max(cj)
print(ans1, ans2)

# 过不了最后一个测试点
# python还是太慢,考试的时候这种测试数据上千的还是用c++比较好
