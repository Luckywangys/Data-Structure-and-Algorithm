'''
描述
某同学在一处山地里，地面起伏很大，他想从一个地方走到另一个地方，并且希望能尽量走平路。
现有一个m*n的地形图，图上是数字代表该位置的高度，"#"代表该位置不可以经过。
该同学每一次只能向上下左右移动，每次移动消耗的体力为移动前后该同学所处高度的差的绝对值。现在给出该同学出发的地点和目的地，需要你求出他最少要消耗多少体力。
输入
第一行是整数 m,n,p，m是行数，n是列数，p是测试数据组数。 0 <= m,n,p <= 100
接下来m行是地形图
再接下来n行每行前两个数是出发点坐标（前面是行，后面是列），后面两个数是目的地坐标（前面是行，后面是列）（出发点、目的地可以是任何地方，出发点和目的地如果有一个或两个在"#"处，则将被认为是无法达到目的地）
输出
n行，每一行为对应的所需最小体力，若无法达到，则输出"NO"
'''

#2200015507 王一粟
import heapq
import sys
m,n,p = [int(i) for i in input().split()]
graph = []
for i in range(m):
    graph.append([int(i) if i!="#" else "#" for i in input().split()])
edges = [[{} for _ in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        if graph[i][j] == "#":
            continue
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0<=i+dx<m and 0<=j+dy<n and graph[i+dx][j+dy] != "#":
                edges[i][j][(i+dx,j+dy)] = abs(graph[i][j] - graph[i+dx][j+dy])
for _ in range(p):
    start_x,start_y,end_x,end_y = [int(i) for i in input().split()]
    distance = [[sys.maxsize for j in range(n)] for i in range(m)]
    distance[start_x][start_y] = 0
    mylist = []
    heapq.heappush(mylist,(0,start_x,start_y))
    result = "NO"
    while mylist:
        dis,current_x,current_y = heapq.heappop(mylist)
        if dis > distance[current_x][current_y]:
            continue
        if current_x == end_x and current_y == end_y:
            result = dis
            break
        for position,ede_dis in edges[current_x][current_y].items():
            nei_x,nei_y = position[0],position[1]
            new_dis = dis+ede_dis
            if new_dis < distance[nei_x][nei_y]:
                distance[nei_x][nei_y] = new_dis
                heapq.heappush(mylist,(new_dis,nei_x,nei_y))
    print(result)