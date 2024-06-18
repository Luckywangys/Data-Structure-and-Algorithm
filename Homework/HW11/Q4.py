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
def dfs(node):
    visited[node] = True
    for element in graph[node]:
        if visited[element] is False:
            dfs(element)
def loop(node,prev):
    visit[node] = True
    for element in graph[node]:
        if element == prev:
            continue
        if visit[element] is True:
            return True
        else:
            if loop(element,node):
                return True
    return False

n,m = [int(i) for i in input().split()]
graph = [[] for i in range(n)]
for _ in range(m):
    a,b = [int(i) for i in input().split()]
    graph[a].append(b)
    graph[b].append(a)
#connected
visited = [False for i in range(n)]
dfs(0)
result = [i for i in visited if i==False]
if result == []:
    print('connected:yes')
else:
    print("connected:no")
#loop
visit = [False for i in range(n)]
cnt = 0
for node in range(n):
    if visit[node] is False:
        if loop(node,-1):
            cnt = 1
            break
if cnt == 0:
    print("loop:no")
else:
    print("loop:yes")