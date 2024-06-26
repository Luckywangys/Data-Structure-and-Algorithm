'''
已知一张地图（以二维矩阵的形式表示）以及佐助和鸣人的位置。地图上的每个位置都可以走到，只不过有些位置上有大蛇丸的手下，需要先打败大蛇丸的手下才能到这些位置。鸣人有一定数量的查克拉，每一个单位的查克拉可以打败一个大蛇丸的手下。假设鸣人可以往上下左右四个方向移动，每移动一个距离需要花费1个单位时间，打败大蛇丸的手下不需要时间。如果鸣人查克拉消耗完了，则只可以走到没有大蛇丸手下的位置，不可以再移动到有大蛇丸手下的位置。佐助在此期间不移动，大蛇丸的手下也不移动。请问，鸣人要追上佐助最少需要花费多少时间？
输入
输入的第一行包含三个整数：M，N，T。代表M行N列的地图和鸣人初始的查克拉数量T。0 < M,N < 200，0 ≤ T < 10
后面是M行N列的地图，其中@代表鸣人，+代表佐助。*代表通路，#代表大蛇丸的手下。
输出
输出包含一个整数R，代表鸣人追上佐助最少需要花费的时间。如果鸣人无法追上佐助，则输出-1。
'''

#2200015507 王一粟
from collections import deque
m,n,p = [int(i) for i in input().split()]
mylist = []
cnt1 = 0
cnt2 = 0
for _ in range(m):
    t = list(input())
    if cnt1 == 0 and "@" in t:
        start = (_,t.index("@"))
        cnt1 = 1
    if cnt2 == 0 and "+" in t:
        end = (_,t.index("+"))
        cnt2 = 1
    mylist.append(t)
visited = [[[0]*(p+1) for i in range(n)] for j in range(m)]
queue = deque([[start,p,0]])
while queue:
    position,num,cnt = queue.popleft()
    x,y = position
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=x+dx<m and 0<=y+dy<n:
            if mylist[x+dx][y+dy] == "+":
                print(cnt+1)
                exit(0)
            elif mylist[x+dx][y+dy] == "#":
                if num != 0:
                    if visited[x+dx][y+dy][num-1] == 0:
                        queue.append([(x+dx,y+dy),num-1,cnt+1])
                        visited[x+dx][y+dy][num-1] = 1
            else:
                if visited[x+dx][y+dy][num] == 0:
                    queue.append([(x+dx,y+dy),num,cnt+1])
                    visited[x + dx][y + dy][num] = 1
print(-1)