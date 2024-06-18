'''
描述
马在中国象棋以日字形规则移动。
请编写一段程序，给定n*m大小的棋盘，以及马的初始位置(x，y)，要求不能重复经过棋盘上的同一个点，计算马可以有多少途径遍历棋盘上的所有点。
输入
第一行为整数T(T < 10)，表示测试数据组数。
每一组测试数据包含一行，为四个整数，分别为棋盘的大小以及初始位置坐标n,m,x,y。(0<=x<=n-1,0<=y<=m-1, m < 10, n < 10)
输出
每组测试数据包含一行，为一个整数，表示马能遍历棋盘的途径总数，0为无法遍历一次。\
'''

#2200015507 王一粟
def dfs(n,m,x,y,p):
    if p == n*m:
        return 1
    result = 0
    visited[x][y] = True
    for x1,y1 in [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]:
        if 0<=x+x1<n and 0<=y+y1<m and not visited[x+x1][y+y1]:
            result += dfs(n,m,x+x1,y+y1,p+1)
    visited[x][y] = False
    return result
t = int(input())
for _ in range(t):
    n,m,x,y = [int(i) for i in input().split()]
    visited = [[False]*m for _ in range(n)]
    print(dfs(n,m,x,y,1))