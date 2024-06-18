'''
描述
作为一名海军提督，Pachi将指挥一支舰队向既定海域出击！
Pachi已经得到了海域的地图，地图上标识了一些既定目标和它们之间的一些单向航线。如果我们把既定目标看作点、航线看作边，那么海域就是一张有向图。不幸的是，Pachi是一个会迷路的提督QAQ，所以他在包含环(圈)的海域中必须小心谨慎，而在无环的海域中则可以大展身手。
受限于战时的消息传递方式，海域的地图只能以若干整数构成的数据的形式给出。作为舰队的通讯员，在出击之前，请你告诉提督海域中是否包含环。
输入
每个测试点包含多组数据，每组数据代表一片海域，各组数据之间无关。
第一行是数据组数T。
每组数据的第一行两个整数N，M，表示海域中既定目标数、航线数。
接下来M行每行2个不相等的整数x,y，表示从既定目标x到y有一条单向航线（所有既定目标使用1~N的整数表示）。
描述中的图片仅供参考，其顶点标记方式与本题数据无关。
1<=N<=100000，1<=M<=500000，1<=T<=5
注意：输入的有向图不一定是连通的。
输出
输出包含T行。
对于每组数据，输出Yes表示海域有环，输出No表示无环。
'''
#2200015507 王一粟
def dfs(node):
    visiting[node] = True
    for neighbor in graph[node]:
        if visiting[neighbor] is True:
            return True
        if visited[neighbor] is False and dfs(neighbor):
            return True
    visiting[node] = False
    visited[node] = True
    return False
for _ in range(int(input())):
    n,m = [int(i) for i in input().split()]
    graph = [0] + [[] for i in range(n)]
    for i in range(m):
        x,y = [int(i) for i in input().split()]
        graph[x].append(y)
    visited = [False for i in range(n+1)]
    visiting = [False for i in range(n+1)]
    cnt = 0
    for element in range(1,n+1):
        if visited[element] is False:
            if dfs(element) is True:
                cnt = 1
                print("Yes")
                break
    if cnt == 0:
        print("No")