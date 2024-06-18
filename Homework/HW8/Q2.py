'''
描述
一个棋盘上有棋子的地方用（'W'）表示，没有的地方用点来表示，现在要找出其中的最大连通区域，一个格子被视作和它周围八个格子都相邻。
现在需要 找出最大的连通区域的面积是多少，一个格子代表面积为1。
输入
输入的第一行是一个整数，表示一共有 T 组数据。
每组第一行包含两个整数N和M。
接下来的N行，每行有M个字符('W'或者'.')，表示格子的当前状态。字符之间没有空格。
输出
每组数据对应一行，输出最大的连通域的面积，不包含任何空格。
'''

#2200015507 王一粟
def dfs(i,j,n,m):
    graph[i][j] = "."
    result = 1
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        if 0<=i+di<n and 0<=j+dj<m and graph[i+di][j+dj] == "W":
            result += dfs(i+di,j+dj,n,m)
    return result
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = []
    for i in range(n):
        graph.append(list(input()))
    max_result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "W":
                t = dfs(i,j,n,m)
                if t > max_result:
                    max_result = t
    print(max_result)