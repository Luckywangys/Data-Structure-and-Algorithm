'''
描述
小北邀请你做一道简单的数学题来活跃一下思维！在这个问题中，你要计算从1到n的所有整数的和，但是需要对2的所有次幂取负号。

例如，对于n = 4，和等于(-1) + (-2) + 3 + (-4) = -4，因为1、2和4分别是20, 21, 22。

你需要计算t组数据的答案。

输入
第一行为数据组数t

接下来的t行，每一行都为一个整数n
输出
输出t行，对于每一组数据计算的答案。
'''

#2200015507 王一粟
mylist = [i for i in range(1,10**6)]
for i in range(0,20):
    mylist[2**i-1] = -(2**i)
t = int(input())
for i in range(t):
    n = int(input())
    lst = mylist[0:n]
    print(sum(lst))