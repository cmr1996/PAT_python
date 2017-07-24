Str = input().split(' ')
N = int(Str[0])
char = Str[1]
nlist = [n for n in range(N) if (2*n*n-1 <= N)]

if len(nlist) == 1:
    print(char)
    print("0")
else:
    nlist2 = [(2 * n - 1) for n in nlist[1:]]
    numLast = nlist2[-1]  # 最后一个数字

    nlist3 = nlist2[1:]
    nlist2.reverse()  # 倒置nlist2字符串
    nlist3 = nlist2 + nlist3

    for x in nlist3:
        if x == numLast:
            print(numLast * char)
        else:
            print(int((numLast - x) / 2 - 1) * " ", x * char)

    print(N - 2 * nlist[-1] * nlist[-1] + 1)