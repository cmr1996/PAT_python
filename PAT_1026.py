str = input().split(' ')
num1 = int(str[0])
num2 = int(str[1])
num = num2 - num1
num = round(num/100)
hour = int(num/3600)
minute = int((num-hour*3600)/60)
second = int(num-hour*3600-minute*60)
print('%02d:%02d:%02d' % (hour, minute, second))
