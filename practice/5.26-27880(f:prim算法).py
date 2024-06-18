'''
描述
城市 XM 是一个非常繁忙的大都市，城市中的道路十分的拥挤，于是市长决定对其中的道路进行改造。城市 XM 的道路是这样分布的：城市中有 n 个交叉路口，有些交叉路口之间有道路相连，两个交叉路口之间最多有一条道路相连接。这些道路是双向的，且把所有的交叉路口直接或间接的连接起来了。每条道路都有一个分值，分值越小表示这个道路越繁忙，越需要进行改造。但是市政府的资金有限，市长希望进行改造的道路越少越好，于是他提出下面的要求：
改造的那些道路能够把所有的交叉路口直接或间接的连通起来。
在满足要求 1 的情况下，改造的道路尽量少。
在满足要求 1、2 的情况下，改造的那些道路中分值最大的道路分值尽量小。
任务：作为市规划局的你，应当作出最佳的决策，选择哪些道路应当被修建。
输入
第一行有两个整数 n,m 表示城市有 n 个交叉路口，m 条道路。
接下来 m 行是对每条道路的描述，u,v,c 表示交叉路口 u 和 v 之间有道路相连，分值为 c。
输出
两个整数 s,max，表示你选出了几条道路，分值最大的那条道路的分值是多少。
'''

#2200015507 王一粟
import heapq
n,m = map(int,input().split())
graph = {i:{} for i in range(n)}
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
visited = [False for i in range(n)]
mylist = [(0,0)]
cnt = 0
result = []
while mylist:
    distance,node = heapq.heappop(mylist)
    if visited[node] is True:
        continue
    visited[node] = True
    result.append(distance)
    cnt += 1
    if cnt == n:
        print(n-1,max(result))
        break
    for neighbor,length in graph[node].items():
        if visited[neighbor] is True:
            continue
        heapq.heappush(mylist,(length,neighbor))

#prim算法不代表每次取出来的就是最小的，但是可以保证连通的边构成总和最小，且保证连通的情况下，最大的最小