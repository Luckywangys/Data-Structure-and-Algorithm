'''
描述
给出一个图的结构，输出其拓扑排序序列，要求在同等条件下，编号小的顶点在前。
输入
若干行整数，第一行有2个数，分别为顶点数v和弧数a，接下来有a行，每一行有2个数，分别是该条弧所关联的两个顶点编号。
v<=100, a<=500
输出
若干个空格隔开的顶点构成的序列(用小写字母)。
'''

#2200015507 王一粟
import heapq
v,a = map(int,input().split())
graph = [[] for i in range(v+1)]
degree = [0 for j in range(v+1)]
for _ in range(a):
    m,n = map(int,input().split())
    degree[n] += 1
    graph[m].append(n)
result = []
mylist = []
for idx,element in enumerate(degree[1:]):
    if element == 0:
        mylist.append(idx+1)
while mylist:
    node = heapq.heappop(mylist)
    result.append("v"+str(node))
    for neighbor in graph[node]:
        degree[neighbor] -= 1
        if degree[neighbor] == 0:
            heapq.heappush(mylist,neighbor)
print(" ".join(result))