'''
描述
你现在身处一个R*C 的迷宫中，你的位置用"S" 表示，迷宫的出口用"E" 表示。
迷宫中有一些石头，用"#" 表示，还有一些可以随意走动的区域，用"." 表示。
初始时间为0 时，你站在地图中标记为"S" 的位置上。你每移动一步（向上下左右方向移动）会花费一个单位时间。你必须一直保持移动，不能停留在原地不走。
当前时间是K 的倍数时，迷宫中的石头就会消失，此时你可以走到这些位置上。在其余的时间里，你不能走到石头所在的位置。
求你从初始位置走到迷宫出口最少需要花费多少个单位时间。
如果无法走到出口，则输出"Oop!"。
输入
第一行是一个正整数 T，表示有 T 组数据。
每组数据的第一行包含三个用空格分开的正整数，分别为 R、C、K。
接下来的 R 行中，每行包含了 C 个字符，分别可能是 "S"、"E"、"#" 或 "."。
其中，0 < T <= 20，0 < R, C <= 100，2 <= K <= 10。
输出
对于每组数据，如果能够走到迷宫的出口，则输出一个正整数，表示最少需要花费的单位时间，否则输出 "Oop!"。
'''

#2200015507 王一粟
from collections import deque
for _ in range(int(input())):
    m,n,k = [int(i) for i in input().split()]
    graph = []
    for i in range(m):
        s = list(input())
        if "S" in s:
            start_x,start_y = i,s.index("S")
        if "E" in s:
            end_x,end_y = i,s.index("E")
        graph.append(s)
    visited = [[[False for p in range(k)] for j in range(n)] for i in range(m)]
    queue = deque([[start_x,start_y,0]])
    cnt = 0
    while queue:
        x,y,time = queue.popleft()
        if x == end_x and y== end_y:
            cnt = 1
            print(time)
            break
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            if 0<=x+dx<m and 0<=y+dy<n and visited[x+dx][y+dy][(time+1)%k] is False:
                if graph[x+dx][y+dy] != "#" or (time+1)%k == 0:
                    visited[x+dx][y+dy][(time+1)%k] = True
                    queue.append([x+dx,y+dy,time+1])
    if cnt == 0:
        print("Oop!")