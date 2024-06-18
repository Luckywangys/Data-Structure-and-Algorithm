'''
描述
将一个８*８的棋盘进行如下分割：将原棋盘割下一块矩形棋盘并使剩下部分也是矩形，再将剩下的部分继续如此分割，这样割了(n-1)次后，连同最后剩下的矩形棋盘共有n块矩形棋盘。(每次切割都只能沿着棋盘格子的边进行)
原棋盘上每一格有一个分值，一块矩形棋盘的总分为其所含各格分值之和。现在需要把棋盘按上述规则分割成n块矩形棋盘，并使各矩形棋盘总分的均方差最小。。
请编程对给出的棋盘及n，求出O'的最小值。
输入
第1行为一个整数n(1 < n < 15)。
第2行至第9行每行为8个小于100的非负整数，表示棋盘上相应格子的分值。每行相邻两数之间用一个空格分隔。
输出
仅一个数，为O'（四舍五入精确到小数点后三位）。
'''

#2200015507 王一粟
import sys
from functools import lru_cache
sys.setrecursionlimit(20000)
@lru_cache(maxsize=None)
def sum_graph(x1,x2,y1,y2):
    result = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            result += graph[i][j]
    return result**2
@lru_cache(maxsize=None)
def min_var(x1,x2,y1,y2,k):
    if k == 1:
        return sum_graph(x1,x2,y1,y2)
    result = sys.maxsize
    for i in range(x1,x2):
        if (i-x1+1)*(y2-y1+1) >= k-1:
            result = min(result,sum_graph(i+1,x2,y1,y2)+min_var(x1,i,y1,y2,k-1))
        if (x2-i)*(y2-y1+1) >= k-1:
            result = min(result,min_var(i+1,x2,y1,y2,k-1)+sum_graph(x1,i,y1,y2))
    for j in range(y1,y2):
        if (x2-x1+1)*(j-y1+1) >= k-1:
            result = min(result,min_var(x1,x2,y1,j,k-1)+sum_graph(x1,x2,j+1,y2))
        if (x2-x1+1)*(y2-j) >= k-1:
            result = min(result,min_var(x1,x2,j+1,y2,k-1)+sum_graph(x1,x2,y1,j))
    return result

n = int(input())
graph = []
sum_value = 0
for i in range(8):
    s = [int(i) for i in input().split()]
    sum_value += sum(s)
    graph.append(s)
result = min_var(0,7,0,7,n)
results = (-(sum_value/n)**2+result/n)**0.5
print(f"{results:.3f}")