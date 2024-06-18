'''
描述
例题：给定一个无向图，判断是否连通，是否有回路。
输入
第一行两个整数n,m，分别表示顶点数和边数。顶点编号从0到n-1。 (1<=n<=110, 1<=m <= 10000)
接下来m行，每行两个整数u和v，表示顶点u和v之间有边。
输出
如果图是连通的，则在第一行输出“connected:yes",否则第一行输出“connected:no"。
如果图中有回路，则在第二行输出“loop:yes ",否则第二行输出“loop:no"。
'''

#2200015507 王一粟
def dfs(idx,prev):
    visited[idx] = True
    cnt = 0
    for neighbor in graph[idx]:
        if neighbor != prev:
            if visited[neighbor]:
                cnt += 1
            else:
                cnt += dfs(neighbor,idx)
    return cnt
n,m = [int(i) for i in input().split()]
graph = [[] for i in range(n)]
visited = [False for i in range(n)]
for _ in range(m):
    a1,a2 = [int(i) for i in input().split()]
    graph[a1].append(a2)
    graph[a2].append(a1)
result = dfs(0,-1)
connected = 1
for i in range(1,n):
    if visited[i] is False:
        connected = 0
        result += dfs(i,-1)

if connected == 1:
    print("connected:yes")
else:
    print("connected:no")
if result > 0:
    print("loop:yes")
else:
    print("loop:no")