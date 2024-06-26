'''
描述
将正整数n 表示成一系列正整数之和，n=n1+n2+…+nk, 其中n1>=n2>=…>=nk>=1 ，k>=1 。
正整数n 的这种表示称为正整数n 的划分。正整数n 的不同的划分个数称为正整数n 的划分数。
输入
标准的输入包含若干组测试数据。每组测试数据是一个整数N(0 < N <= 50)。
输出
对于每组测试数据，输出N的划分数。
'''
from functools import lru_cache
@lru_cache(maxsize=None)
def f(n,m):
    if n == 1 or m == 1:
        return 1
    if n <= m:
        return 1 + f(n,n-1)
    return f(n,m-1) + f(n-m,m)
while True:
    try:
        n = int(input())
        result = f(n,n)
        print(result)
    except:
        break