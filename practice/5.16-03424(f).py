'''
描述
During the kindergarten days, flymouse was the monitor of his class. Occasionally the head-teacher brought the kids of flymouse’s class a large bag of candies and had flymouse distribute them. All the kids loved candies very much and often compared the numbers of candies they got with others. A kid A could had the idea that though it might be the case that another kid B was better than him in some aspect and therefore had a reason for deserving more candies than he did, he should never get a certain number of candies fewer than B did no matter how many candies he actually got, otherwise he would feel dissatisfied and go to the head-teacher to complain about flymouse’s biased distribution.
snoopy shared class with flymouse at that time. flymouse always compared the number of his candies with that of snoopy’s. He wanted to make the difference between the numbers as large as possible while keeping every kid satisfied. Now he had just got another bag of candies from the head-teacher, what was the largest difference he could make out of it?
输入
The input contains a single test cases. The test cases starts with a line with two integers N and M not exceeding 30 000 and 150 000 respectively. N is the number of kids in the class and the kids were numbered 1 through N. snoopy and flymouse were always numbered 1 and N. Then follow M lines each holding three integers A, B and c in order, meaning that kid A believed that kid B should never get over c candies more than he did.
输出
Output one line with only the largest difference desired. The difference is guaranteed to be finite.
'''

#2200015507 王一粟
import heapq
n,m = [int(i) for i in input().split()]
graph = [0] + [{} for i in range(n)]
for _ in range(m):
    a,b,c = [int(i) for i in input().split()]
    if b in graph[a]:
        graph[a][b] =  min(graph[a][b],c)
    else:
        graph[a][b] = c
queue = [(0,1)]
distance = [float("inf") for i in range(n+1)]
visited = [False for i in range(n+1)]
distance[1] = 0
while queue:
    dis,node = heapq.heappop(queue)
    if visited[node] is True:
        continue
    visited[node] = True
    if n == node:
        print(dis)
        break
    for neighbor,path in graph[node].items():
        if dis + path < distance[neighbor]:
            distance[neighbor] = path+dis
            heapq.heappush(queue,(dis+path,neighbor))