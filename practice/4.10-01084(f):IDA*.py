'''
描述
左图展示了一个由 24 根火柴棍组成的 3 * 3 的网格，所有火柴棍的长度都是 1。在这张网格图中有很多的正方形：边长为 1 的有 9 个，边长为 2 的有 4 个，边长为 3 的有 1 个。
每一根火柴棍都被编上了一个号码，编码的方式是从上到下：横着的第一行，竖着的第一行，横着的第二行一直到横着的最后一行。在同一行内部，编码的方式是从左到右。 其中对 3 * 3 的火柴网格编码的结果已经标在左图上了。
右图展示了一个不完整的 3 * 3 的网格，它被删去了编号为 12,17,23 的火柴棍。删去这些火柴棍后被摧毁了 5 个大小为 1 的正方形，3 个大小为 2 的正方形和 1 个大小为 3 的正方形。（一个正方形被摧毁当且仅当它的边界上有至少一个火柴棍被移走了）
可以把上述概念推广到 n * n 的火柴棍网格。在完整的 n * n 的网格中，使用了 2n(n+1) 根火柴棍，其中边长为 i(i ∈ [1,n]) 的正方形有 (n-i+1)2个。
现在给出一个 n * n 的火柴棍网格，最开始它被移走了 k 根火柴棍。问最少再移走多少根火柴棍，可以让所有的正方形都被摧毁。
输入
输入包含多组数据，第一行一个整数 T 表示数据组数。
对于每组数据，第一行输入一个整数 n 表示网格的大小( n <= 5)。第二行输入若干个空格隔开的整数，第一个整数 k 表示被移走的火柴棍个数，接下来 k 个整数表示被移走的火柴棍编号。
输出
对于每组数据，输出一行一个整数表示最少删除多少根火柴棍才能摧毁所有的正方形。
'''

#2200015507 王一粟
import copy
import sys
sys.setrecursionlimit(1 << 30)
found = False

def check1(x, tmp):
    for y in graph[x]:
        if tmp[y]:
            return False
    return True

def check2(x):
    for y in graph[x]:
        if judge[y]:
            return False
    return True

def estimate():
    cnt = 0
    tmp = copy.deepcopy(judge)
    for x in range(1, total+1):
        if check1(x, tmp):
            cnt += 1
            for u in graph[x]:
                tmp[u] = True
    return cnt

def dfs(t):
    global found
    if t + estimate() > limit:
        return
    for x in range(1, total+1):
        if check2(x):
            for y in graph[x]:
                judge[y] = True
                dfs(t+1)
                judge[y] = False
                if found:
                    return
            return
    found = True

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    d, m, nums, total = 2*n+1, lst[0], lst[1:], 0
    graph = {}
    for i in range(n):
        for j in range(n):
            for k in range(1, n+1):
                if i+k <= n and j+k <= n:
                    total += 1
                    graph[total] = []
                    for p in range(1, k+1):
                        graph[total] += [d*i+j+p, d*(i+p)+j-n, d*(i+p)+j-n+k, d*(i+k)+j+p]
    judge = [False for _ in range(2*n*(n+1)+1)]
    for num in nums:
        judge[num] = True
    limit = estimate()
    found = False
    while True:
        dfs(0)
        if found:
            print(limit)
            break
        limit += 1