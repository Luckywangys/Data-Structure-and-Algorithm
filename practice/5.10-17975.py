'''
描述
给定一系列整型关键字和素数P，用除留余数法定义的散列函数H（key)=key%M，将关键字映射到长度为M的散列表中，用二次探查法解决冲突.
本题不涉及删除，且保证表长不小于关键字总数的2倍，即没有插入失败的可能。
输入
输入第一行首先给出两个正整数N（N<=1000）和M（一般为>=2N的最小素数），分别为待插入的关键字总数以及散列表的长度。
第二行给出N个整型的关键字。数字之间以空格分隔。
输出
在一行内输出每个整型关键字的在散列表中的位置。数字间以空格分隔。
'''

#2200015507 王一粟
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
mylist = [0.5 for i in range(m)]
result = []
for num in num_list:
    pos = num % m
    if mylist[pos] == 0.5 or mylist[pos] == num:
        mylist[pos] = num
        result.append(pos)
    else:
        sign = 1
        cnt = 1
        while True:
            now = pos + sign*(cnt**2)
            if mylist[now%m] == 0.5 or mylist[now%m] == num:
                mylist[now%m] = num
                result.append(now%m)
                break
            sign = sign * (-1)
            if sign == 1:
                cnt += 1
print(*result)