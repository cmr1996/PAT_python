N = int(input())
ID = []
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
Z_M = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
N_cnt = 0  # N_cnt作为校验错误计数器,计算校验错误出现次数

for k in range(N):
    tmp = input()
    error = 0  # error作为出现非数字错误标志位,当等于0是数据不正确
    i = 0
    j = 0
    while i != 17:
        if tmp[i]>='0' and tmp[i]<='9' :  # 不能想当然的使用tmp!='X'来当作判断条件
            j += int(tmp[i]) * weight[i]
        else:
            error = 1
        i += 1

    if error == 1:
        print(tmp)
    else:
        Z = int(j % 11)
        if str(Z_M[Z]) != tmp[17]:
            print(tmp)
        else:
            N_cnt += 1

if N_cnt == N:
    print("All passed")

# 各个测试点推测:
# 测试点1 答案正确 sample1等价，有不在范围内的字符, 有完全算错, 有没有最后取映射
# 测试点2 答案正确 sample2等价
# 测试点3 答案正确 N=100, 包含所有11种映射
# 测试点4 答案正确 最小N
