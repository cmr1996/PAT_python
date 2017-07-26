def cnt_length(args, MAX, MAX_index, p_cnt):  # 参数分别为保存数列的list、生成数列的最大值、传入最大值的下标、本题给定的参数
    index = 0
    for item in args:
        if item*p_cnt >= MAX:
            return MAX_index - index + 1
            break
        else:
            index += 1
    return NULL


str1 = input().split(' ')
N = int(str1[0])
P = int(str1[1])
str2 = input().split(' ')
num = [int(x) for x in str2]
num.sort()
ans = []

j = len(num) - 1
while j >= 0:
    l = cnt_length(num, MAX=num[j], MAX_index=j, p_cnt=P)
    ans.append(l)
    j -= 1

print(max(ans))
