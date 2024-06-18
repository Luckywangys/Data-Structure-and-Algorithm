'''
描述
我们都知道，在中国象棋中，马是走日字步的。现给定马的起始坐标与终点坐标，求出马最快能到达的路线。如果有多条路线都是步数最少的，则输出路线的数目
注意，此时棋盘上可能会有一些其它的棋子，这些棋子是会憋马脚的，注意！
输入
前两行为起点坐标与终点坐标，第三行为一个数字M，之后的M行为棋盘上其它棋子的坐标(M<32,坐标行列值<=10)
输出
如果最快路线唯一，则输出路线。否则只输出一个数字，为最快路线的数目N
'''

#2200015507 王一粟
from collections import deque
start_x,start_y = map(int,input().split())
end_x,end_y = map(int,input().split())
block = set()
for i in range(int(input())):
    a,b = map(int,input().split())
    block.add((a,b))
queue = deque([(start_x,start_y,0,f"({start_x},{start_y})")])
i = 0
change = [(-2,-1),(-2,1),(-1,-2),(-1,2),(2,-1),(2,1),(1,-2),(1,2)]
foot = [(-1,0),(-1,0),(0,-1),(0,1),(1,0),(1,0),(0,-1),(0,1)]
while queue:
    x,y,cnt,path = queue.popleft()
    if x == end_x and y == end_y:
        result = path
        num = cnt
        total = 1
        i = 1
        break
    for i in range(8):
        chx,chy = change[i]
        fx,fy = foot[i]
        if (x+fx,y+fy) in block:
            continue
        queue.append((x+chx,y+chy,cnt+1,path+"-"+f"({x+chx},{y+chy})"))
if i == 1:
    while queue:
        x,y,cnt,q = queue.popleft()
        if cnt > num:
            break
        if x == end_x and y == end_y:
            total += 1
    if total == 1:
        print(path)
    else:
        print(total)