'''
描述
给定一个长度为n和整数k的整数序列。请你打印出[1,10^9]范围内的最小整数x(即1≤x≤10^9)，使得给定序列中恰好有k个元素小于或等于x。
注意，序列可以包含相等的元素。
如果没有这样的x，打印"-1"(不带引号)。
输入
输入的第一行包含整数 n 和 k ( 1≤n≤2·10^5, 0≤k≤n)。
输入的第二行包含n个整数 a_1,a_2，…，a_n (1≤a_i≤10^9) ——序列本身。
输出
输出最小整数 x (1≤x≤10^9)，使得给定序列中恰好有k个元素小于或等于x。
如果没有这样的x，打印"-1"(不带引号)。
'''

#2200015507 王一粟
import heapq
n,k = [int(i) for i in input().split()]
mylist = [int(i) for i in input().split()]
heapq.heapify(mylist)
if k == 0:
    t = heapq.heappop(mylist)
    if t == 1:
        print(-1)
    else:
        print(1)
else:
    for element in range(k):
        t = heapq.heappop(mylist)
    if k == n:
        print(t)
    else:
        m = heapq.heappop(mylist)
        if m == t:
            print(-1)
        else:
            print(t)