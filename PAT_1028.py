n = int(input())
max = '2014/09/06'
min = '1814/09/06'
maxday = min
minday = max

sum = 0
for i in range(n):
    str = input().split(' ')
    date = str[1]
    if min <= date <= max:
        sum += 1
        if date >= maxday:
            maxday = date  # 实际上日期越大年龄越小
                           # 代码中maxday指的概念是生日的最大日期
            mindayname = str[0]

        if date <= minday:
            minday = date
            maxdayname = str[0]

if sum!=0 :
    print(sum,maxdayname,mindayname)
else:
    print('0')

  # 思路可以借鉴,但无法解决最后一个测试点,猜测最后一个测试点为超大数据
  #  python字符串可以直接比较