#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_num(num):
    num_str = {0: "ling", 1: "yi", 2: "er", 3: "san", 4: "si", 5: "wu", 6: "liu", 7: "qi", 8: "ba", 9: "jiu"}  # 存储序列
    result = []
    while num != 0:
        result.insert(0, int(num % 10))
        num = int(num/10)

    length = len(result)

    for i in range(length):
        print(num_str[result[i]], end="")
        if (i+1) != 0:
            print(" ",  end="")


if __name__ == '__main__':
    number = int(input())
    total = 0

    while number != 0:
        total = total + int(number % 10)
        number = int(number / 10)

    print_num(total)
