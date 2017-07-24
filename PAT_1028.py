import re

N = int(input())
name = []
year = {}
month = {}
day = {}
for i in range(N):
    tmp = input().split(' ')
    name.append(tmp[0])
    #  tmp2 = tmp[1]
    ObjectMatch = re.match(r'\d{4}\/\d{1,2}\/\d{1,2}',tmp[1])
    print(ObjectMatch.group(1))
    year[tmp[0]] = ObjectMatch.group(1)
    month[tmp[0]] = ObjectMatch.group(2)
    day[tmp[0]] = ObjectMatch.group(3)

max_age_year = 0
max_age_month = 0
max_age_day = 0

min_age_year = int(year[name[0]])
min_age_month = int(month[name[0]])
min_age_day = int(day[name[0]])
for k in name:
    age_year = 2014 - int(year[k])
    age_month = 9 - int(month[k])
    age_day = 6 - int(day[k])
    if age_year >= 200 or age_year < 0:
        name.remove(k)
        break
    #  寻找最年长的人
    if age_year > max_age_year:
        max_age_year = age_year
        max_age_month = age_month
        max_age_day = age_day
        max_age_name = k
    elif age_year == max_age_year:
        if age_month > max_age_month:
            max_age_month = age_month
            max_age_day = age_day
            max_age_name = k
        elif age_month == max_age_month:
            if age_day > max_age_day:
                max_age_day = age_day
                max_age_name = k

    #  寻找最年轻的人
    if age_year < min_age_year:
        min_age_year = age_year
        min_age_month = age_month
        min_age_day = age_day
        min_age_name = k
    elif age_year == min_age_year:
        if age_month < min_age_month:
            min_age_month = age_month
            min_age_day = age_day
            min_age_name = k
        elif age_month == min_age_month:
            if age_day < min_age_day:
                min_age_day = age_day
                min_age_name = k

    print(len(name),' ',max_age_name,' ',min_age_name)

