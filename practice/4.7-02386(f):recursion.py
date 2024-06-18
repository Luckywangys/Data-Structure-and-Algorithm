'''
描述
Due to recent rains, water has pooled in various places in Farmer John's field, which is represented by a rectangle of N x M (1 <= N <= 100; 1 <= M <= 100) squares. Each square contains either water ('W') or dry land ('.'). Farmer John would like to figure out how many ponds have formed in his field. A pond is a connected set of squares with water in them, where a square is considered adjacent to all eight of its neighbors.
Given a diagram of Farmer John's field, determine how many ponds he has.
输入
* Line 1: Two space-separated integers: N and M
* Lines 2..N+1: M characters per line representing one row of Farmer John's field. Each character is either 'W' or '.'. The characters do not have spaces between them.
输出
* Line 1: The number of ponds in Farmer John's field.
'''

#2200015507 王一粟
#注：存在递归的情况下RE很有可能是因为recursion limit不够
import sys
sys.setrecursionlimit(100000)
def dfs(i,j):
    graph[i][j] = "."
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]:
        if 0<=i+di<n and 0<=j+dj<m and graph[i+di][j+dj] == "W":
            dfs(i+di,j+dj)
n,m = [int(i) for i in input().split()]
graph = []
for _ in range(n):
    s = list(input())
    graph.append(s)
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "W":
            result += 1
            dfs(i,j)
print(result)