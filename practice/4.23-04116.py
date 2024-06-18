'''
描述
公主被恶人抓走，被关押在牢房的某个地方。牢房用N*M (N, M <= 200)的矩阵来表示。矩阵中的每项可以代表道路（@）、墙壁（#）、和守卫（x）。
英勇的骑士（r）决定孤身一人去拯救公主（a）。我们假设拯救成功的表示是“骑士到达了公主所在的位置”。由于在通往公主所在位置的道路中可能遇到守卫，骑士一旦遇到守卫，必须杀死守卫才能继续前进。
现假设骑士可以向上、下、左、右四个方向移动，每移动一个位置需要1个单位时间，杀死一个守卫需要花费额外的1个单位时间。同时假设骑士足够强壮，有能力杀死所有的守卫。
给定牢房矩阵，公主、骑士和守卫在矩阵中的位置，请你计算拯救行动成功需要花费最短时间。
输入
第一行为一个整数S，表示输入的数据的组数（多组输入）
随后有S组数据，每组数据按如下格式输入
1、两个整数代表N和M, (N, M <= 200).
2、随后N行，每行有M个字符。"@"代表道路，"a"代表公主，"r"代表骑士，"x"代表守卫, "#"代表墙壁。
输出
如果拯救行动成功，输出一个整数，表示行动的最短时间。
如果不可能成功，输出"Impossible"
'''

#2200015507 王一粟
from collections import deque
for _ in range(int(input())):
    n,m = [int(i) for i in input().split()]
    graph = []
    for i in range(n):
        s = list(input())
        if "r" in s:
            start_x,start_y = i, s.index("r")
        if "a" in s:
            end_x, end_y = i, s.index("a")
        graph.append(s)
    queue = deque([[start_x,start_y,0]])
    visited = [[False for j in range(m)] for i in range(n)]
    visited[start_x][start_y] = True
    cnt = 0
    defeat = [[False for j in range(m)] for i in range(n)]
    while queue:
        x,y,time = queue.popleft()
        if x == end_x and y== end_y:
            cnt = 1
            print(time)
            break
        if graph[x][y] == "x" and defeat[x][y] is False:
            defeat[x][y] = True
            queue.append([x,y,time+1])
            continue
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            if 0<=x+dx<n and 0<=y+dy<m and graph[x+dx][y+dy] != "#" and visited[x+dx][y+dy] is False:
                visited[x+dx][y+dy] = True
                queue.append([x+dx,y+dy,time+1])
    if cnt == 0:
        print("Impossible")




