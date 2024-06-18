'''
描述
每年奶牛们都要举办各种特殊版本的跳房子比赛，包括在河里从一个岩石跳到另一个岩石。这项激动人心的活动在一条长长的笔直河道中进行，在起点和离起点L远 (1 ≤ L≤ 1,000,000,000) 的终点处均有一个岩石。在起点和终点之间，有N (0 ≤ N ≤ 50,000) 个岩石，每个岩石与起点的距离分别为Di (0 < Di < L)。
在比赛过程中，奶牛轮流从起点出发，尝试到达终点，每一步只能从一个岩石跳到另一个岩石。当然，实力不济的奶牛是没有办法完成目标的。
农夫约翰为他的奶牛们感到自豪并且年年都观看了这项比赛。但随着时间的推移，看着其他农夫的胆小奶牛们在相距很近的岩石之间缓慢前行，他感到非常厌烦。他计划移走一些岩石，使得从起点到终点的过程中，最短的跳跃距离最长。他可以移走除起点和终点外的至多M (0 ≤ M ≤ N) 个岩石。
请帮助约翰确定移走这些岩石后，最长可能的最短跳跃距离是多少？
输入
第一行包含三个整数L, N, M，相邻两个整数之间用单个空格隔开。
接下来N行，每行一个整数，表示每个岩石与起点的距离。岩石按与起点距离从近到远给出，且不会有两个岩石出现在同一个位置。
输出
一个整数，最长可能的最短跳跃距离。
'''

#2200015507 王一粟
def solution(mid,m):
    result = 0
    wait = 0
    for element in mylist:
        if wait + element < mid:
            wait += element
            result += 1
        else:
            wait = 0
    return result <= m
l,n,m = [int(i) for i in input().split()]
mylist = []
min_num = l+1
prev = 0
for i in range(n):
    num = int(input())
    dis = num - prev
    mylist.append(dis)
    min_num = min(min_num,dis)
    prev = num
mylist.append(l-prev)
min_num = min(min_num,l-prev)
start = min_num
end = l
mid = (start+end)//2
while start < mid:
    if solution(mid,m):
        start = mid
        mid = (start+end)//2
    else:
        end = mid
        mid = (start+end)//2
if solution(end,m):
    print(end)
else:
    print(start)