'''
描述
给定一张地图，人物只能走上下左右，给定入口与出口，但有个问题
要达到出口时，必须拿到钥匙，才能过关
钥匙掉落在迷宫中，你需要从中捡取
求拿钥匙并走出迷宫的最快路线
输入
输入分为两个部分
第一部分是两个整数X与Y，X<100,Y<100，表示迷宫的行与列
第二部分是迷宫地图，1表示障碍，0表入可走，R表示入口，C表示出口，Y表示钥匙
输出
拿到钥匙并走出迷宫的最快路线（最左上角坐标为1，1）
'''
#2200015507 王一粟
from collections import deque
m,n = [int(i) for i in input().split()]
graph = [[]]
for _ in range(1,m+1):
    s = [-1] + list(input())
    if "R" in s: start_x,start_y = _ , s.index("R")
    if "C" in s: end_x,end_y = _, s.index("C")
    if "Y" in s: key_x,key_y = _,s.index("Y")
    graph.append(s)
queue = deque([[start_x,start_y,[(start_x,start_y)]]])
visited = [[False for j in range(n+1)] for i in range(m+1)]
visited[start_x][start_y] = True
result = []
while queue:
    x,y,path = queue.popleft()
    if x == key_x and y == key_y:
        result = result + path
        break
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        if 1<=x+dx<=m and 1<=y+dy<=n and graph[x+dx][y+dy] != "1" and visited[x+dx][y+dy] is False:
            queue.append([x+dx,y+dy,path+[(x+dx,y+dy)]])
            visited[x+dx][y+dy] = True
queue = deque([[key_x,key_y,[]]])
visited = [[False for j in range(n+1)] for i in range(m+1)]
visited[key_x][key_y] = True
while queue:
    x,y,path = queue.popleft()
    if end_x == x and end_y == y:
        result = result + path
        break
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        if 1<=x+dx<=m and 1<=y+dy<=n and graph[x+dx][y+dy] != "1" and visited[x+dx][y+dy] is False:
            queue.append([x+dx,y+dy,path+[(x+dx,y+dy)]])
            visited[x + dx][y + dy] = True
for element in result:
    print(element[0],element[1])