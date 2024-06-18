'''
描述
给一个由1跟0组成的方形地图，1代表土地，0代表水域
相邻(上下左右4个方位当作相邻)的1组成孤岛
现在你可以将0转成1，搭建出一个链接2个孤岛的桥
请问最少要将几个0转成1，才能建成链接孤岛的桥。
题目中恰好有2个孤岛(答案不会是0)
输入
一个正整数n，代表几行输入
n行0跟1字串
输出
一个正整数k，代表最短距离
'''
#2200015507 王一粟
from collections import deque
def dfs(i,j):
    queue.append([i,j,0])
    graph[i][j] = 0
    visited[i][j] = True
    for di,dj in [(-1,0),(1,0),(0,1),(0,-1)]:
        if 0<=i+di<n and 0<=j+dj<n and graph[i+di][j+dj] == 1:
            dfs(i+di,j+dj)
n = int(input())
graph = []
for _ in range(n):
    a = list(input())
    graph.append([int(i) for i in a])
visited = [[False for j in range(n)] for i in range(n)]
queue = deque()
p = 0
for i in range(n):
    if p == 1:
        break
    for j in range(n):
        if graph[i][j] == 1:
            p = 1
            dfs(i,j)
            break
cnt = 0
while True:
    x,y,time = queue.popleft()
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        if 0<=x+dx<n and 0<=y+dy<n and visited[x+dx][y+dy] is False:
            if graph[x+dx][y+dy] == 1:
                cnt = 1
                print(time)
                break
            visited[x+dx][y+dy] = True
            queue.append([x+dx,y+dy,time+1])
    if cnt == 1:
        break