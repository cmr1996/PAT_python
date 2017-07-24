str = input()
N = int(str[0])
length_str = int(len(str))
# 定义
A1=0
A2=0
A2_flag=1
A3_cnt=0
A4=0
for i in range(1:length_str):
  k = int(str[i])
  temp = k % 5
  if temp==0:
    if temp%2 == 0:
      A1 = A1 + temp
  elif temp==1:
    if A2_flag:
      A2 = A2 + temp
      A2_flag = -A2_flag
    else:
      A2 = A2 - temp
      A2_flag = -A2_flag
  elif temp==2:
    A3_cnt += 1
  elif temp==3: