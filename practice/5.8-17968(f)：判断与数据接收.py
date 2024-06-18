'''
描述
给定一系列整型关键字和素数P，用除留余数法定义的散列函数H（key)=key%M，将关键字映射到长度为M的散列表中，用线性探查法解决冲突
输入
输入第一行首先给出两个正整数N（N<=1000）和M（>=N的最小素数），分别为待插入的关键字总数以及散列表的长度。
第二行给出N个整型的关键字。数字之间以空格分隔。
输出
在一行内输出每个整型关键字的在散列表中的位置。数字间以空格分隔。
'''
#注：false与true的判断用...is False，... is True，不要用==
#2200015507 王一粟
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
mylist = [False for i in range(m)]
num_list = [int(i) for i in data[index:index+n]]
result = []
for num in num_list:
    position = num%m
    cnt = position
    while True:
        if mylist[cnt] is False or mylist[cnt] == num:
            result.append(cnt)
            mylist[cnt] = num
            break
        cnt = (cnt+1)%m
print(" ".join(str(i) for i in result))

