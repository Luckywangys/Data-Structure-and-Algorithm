'''
现有一个共n个顶点、m条边的无向图（假设顶点编号为从0到n-1），每个顶点有各自的权值。我们把一个连通块中所有顶点的权值之和称为这个连通块的权值。求图中所有连通块的最大权值。
第一行两个整数n、m分别表示顶点数和边数；
第二行n个用空格隔开的正整数（每个正整数不超过100），表示n个顶点的权值。接下来m行，每行两个整数u、v），表示一条边的两个端点的编号。数据保证不会有重边。
输出一个整数，表示连通块的最大权值。
'''

#2200015507 王一粟
def dfs(i):
    visited[i] = 1
    result = weight[i]
    for j in graph[i]:
        if visited[j] == 0:
            result += dfs(j)
    return result
n,m = [int(i) for i in input().split()]
weight = [int(i) for i in input().split()]
graph = {i: [] for i in range(n)}
visited = [0]*n
for _ in range(m):
    key1,key2 = [int(i) for i in input().split()]
    graph[key1].append(key2)
    graph[key2].append(key1)
max_result = 0
for i in range(n):
    if visited[i] == 0:
        t = dfs(i)
        if t > max_result:
            max_result = t
print(max_result)

