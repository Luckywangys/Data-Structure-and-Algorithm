'''
描述
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
height = [0,1,0,2,1,0,1,3,2,1,2,1]
由数组表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
输入
第一行包含一个整数n。1 <= n <= 2 * 10^4
第二行包含n个整数，相邻整数间以空格隔开。0 <= ratings[i] <= 2 * 10^5
输出
一个整数
'''

#2200015507 王一粟
n = int(input())
mylist = [int(i) for i in input().split()]
total = 0
stack = []
current = 0
while current < n:
    while stack and mylist[stack[-1]] < mylist[current]:
        h = stack.pop()
        if stack:
            total += (min(mylist[stack[-1]],mylist[current]) - mylist[h])*(current-stack[-1]-1)
    stack.append(current)
    current += 1
print(total)