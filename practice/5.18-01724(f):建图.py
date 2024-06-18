'''
描述
N cities named with numbers 1 ... N are connected with one-way roads. Each road has two parameters associated with it : the road length and the toll that needs to be paid for the road (expressed in the number of coins).
Bob and Alice used to live in the city 1. After noticing that Alice was cheating in the card game they liked to play, Bob broke up with her and decided to move away - to the city N. He wants to get there as quickly as possible, but he is short on cash.
We want to help Bob to find the shortest path from the city 1 to the city N that he can afford with the amount of money he has.
输入
The first line of the input contains the integer K, 0 <= K <= 10000, maximum number of coins that Bob can spend on his way.
The second line contains the integer N, 2 <= N <= 100, the total number of cities.
The third line contains the integer R, 1 <= R <= 10000, the total number of roads.
Each of the following R lines describes one road by specifying integers S, D, L and T separated by single blank characters :
S is the source city, 1 <= S <= N
D is the destination city, 1 <= D <= N
L is the road length, 1 <= L <= 100
T is the toll (expressed in the number of coins), 0 <= T <=100
Notice that different roads may have the same source and destination cities.
输出
The first and the only line of the output should contain the total length of the shortest path from the city 1 to the city N whose total toll is less than or equal K coins.
If such path does not exist, only number -1 should be written to the output.
'''

#2200015507 王一粟
import heapq
import sys
k = int(input())
n = int(input())
r = int(input())
graph = [[] for i in range(n+1)]
for i in range(r):
    s,d,l,t = [int(i) for i in input().split()]
    graph[s].append([d,l,t])
queue = [(0,1,k)]
visited = [[False for j in range(k+1)] for i in range(n+1)]
distance = [[sys.maxsize if i != 1 else 0 for j in range(k+1)] for i in range(n+1)]
cnt = 0
while queue:
    dis,spot,money = heapq.heappop(queue)
    if visited[spot][money] is True:
        continue
    visited[spot][money] = True
    if spot == n:
        cnt = 1
        print(dis)
        break
    for neighbor,inter_distance,cost in graph[spot]:
        if cost <= money and visited[neighbor][money-cost] is False:
            if dis + inter_distance < distance[neighbor][money-cost]:
                distance[neighbor][money-cost] = dis + inter_distance
                heapq.heappush(queue,(dis+inter_distance,neighbor,money-cost))
if cnt == 0:
    print(-1)










