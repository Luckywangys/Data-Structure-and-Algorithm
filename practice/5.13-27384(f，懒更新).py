'''
描述
超大型偶像团体HIHO314159总选举刚刚结束了。制作人小Hi正在复盘分析投票过程。
小Hi获得了N条投票记录，每条记录都包含一个时间戳Ti以及候选人编号Ci，代表有一位粉丝在Ti时刻投了Ci一票。
给定一个包含K名候选人集合S={S1, S2, ... SK}，小Hi想知道从投票开始(0时刻)，到最后一张票投出的时刻(max{Ti})，期间有多少时间得票最多的前K名候选人恰好是S中的K名候选人。
注意这里对前K名的要求是"严格"的，换句话说，S中的每一名候选人得票都要大于任何一名S之外的候选人。S集合内名次先后不作要求。
注：HIHO314159这个团体有314159名团员，编号是1~314159。
输入
第一行包含两个整数N和K。
第二行包含2N个整数：T1, C1, T2, C2, ... TN, CN。
第三行包含K个整数：S1, S2, ... SK。
对于30%的数据，1 ≤ N, K ≤ 100
对于60%的数据，1 ≤ N, K ≤ 1000
对于100%的数据, 1 ≤ N, K ≤ 314159 1 ≤ Ti ≤ 1000000 1 ≤ Ci, SK ≤ 314159
输出
一个整数，表示前K名恰好是S一共持续了多少时间。
'''

#2200015507 王一粟
import heapq
maxn = 320000
cnt = [0]*maxn
vis = [False]*maxn
n,k = [int(i) for i in input().split()]
records = [int(i) for i in input().split()]
arr = [(records[i],records[i+1]) for i in range(0,2*n,2)]
Q = []
candidates = [int(i) for i in input().split()]
for i in range(k):
    heapq.heappush(Q,(0,candidates[i]))
    vis[candidates[i]] = True
arr = sorted(arr[:n])
if k == 314159:
    print(arr[n-1][0])
    exit()
rmx,rs = 0,0
for i in range(n):
    c = arr[i][1]
    cnt[c] += 1
    if vis[c]:
        while cnt[Q[0][1]]:
            f = heapq.heappop(Q)
            f = (f[0]+cnt[f[1]],f[1])
            heapq.heappush(Q,f)
            cnt[f[1]] = 0
    else:
        rmx = max(rmx,cnt[c])
    if i!=n-1 and arr[i+1][0] != arr[i][0] and Q[0][0] > rmx:
        rs += arr[i+1][0] - arr[i][0]
print(rs)











