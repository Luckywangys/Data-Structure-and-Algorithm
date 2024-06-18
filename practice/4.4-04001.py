'''
描述
农夫知道一头牛的位置，想要抓住它。农夫和牛都位于数轴上，农夫起始位于点N(0<=N<=100000)，牛位于点K(0<=K<=100000)。农夫有两种移动方式：
1、从X移动到X-1或X+1，每次移动花费一分钟
2、从X移动到2*X，每次移动花费一分钟
假设牛没有意识到农夫的行动，站在原地不动。农夫最少要花多少时间才能抓住牛？
输入
两个整数，N和K
输出
一个整数，农夫抓到牛所要花费的最小分钟数
'''

#2200015507 王一粟
from collections import deque
n,k = [int(i) for i in input().split()]
queue = deque([[n,0]])
mylist = [0]*200000
while queue:
    position,cnt = queue.popleft()
    if position == k:
        print(cnt)
        break
    if position > k:
        if mylist[position-1] == 0:
            mylist[position-1] = 1
            queue.append([position - 1, cnt + 1])
    else:
        if position > 3 and mylist[position-1] == 0:
            mylist[position-1] = 1
            queue.append([position-1,cnt+1])
        if mylist[position+1] == 0:
            mylist[position+1] = 1
            queue.append([position + 1, cnt + 1])
        if mylist[position*2] == 0:
            mylist[position*2] = 1
            queue.append([position*2,cnt+1])