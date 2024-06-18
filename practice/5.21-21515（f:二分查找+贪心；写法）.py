'''
描述
有N座通信基站，P条双向电缆，第i条电缆连接基站Ai和Bi。特别地，1号基站是通信公司的总站，N号基站位于一座农场中。现在，农场主希望对通信线路进行升级，其中升级第i条电缆需要花费Li。
电话公司正在举行优惠活动。农场主可以指定一条从1号基站到N号基站的路径，然后，农场主可以指定路径上不超过K条电缆，先由电话公司免费提供升级服务。农场主只需要支付在该路径上剩余的电缆中，升级价格最贵的那条电缆的花费即可。支付完成后，其余电缆也将由电话公司免费升级。求至少用多少钱能完成升级。
输入
第一行三个整数， N，P，K。
接下来P行，每行三个整数Ai，Bi，Li。
输出
若不存在从1到N的路径，输出-1。否则输出所需最小费用。
样例输入
'''

#2200015507 王一粟
from heapq import *
n,p,k = map(int,input().split())
graph = {i:{} for i in range(1,n+1)}
h = 0
for _ in range(p):
    a,b,l = map(int,input().split())
    graph[a][b] = graph[b][a] = l
    h = max(h,l)
l = 0

def search(lim):
    heap = [(-1,-k)]
    heapify(heap)
    vis = {}
    while heap:
        idx,free = heappop(heap)
        idx,free = -idx,-free
        if idx == n:
            return 1
        if idx not in vis or vis[idx] < free:
            vis[idx] = free
        else:
            continue
        for t,length in graph[idx].items():
            new_free = free
            if length > lim:
                if new_free > 0:
                    new_free -= 1
                else:
                    continue
            if t in vis and vis[t] > new_free:
                continue
            heappush(heap,(-t,-new_free))
    return 0
while l < h:
    if l +1 == h:
        ans_l,ans_h = search(l),search(h)
        if ans_l == ans_h == 0:
            print(-1)
        else:
            print(l if ans_l else h)
        exit()
    mid = (l+h)//2
    if search(mid):
        h = mid
    else:
        l = mid