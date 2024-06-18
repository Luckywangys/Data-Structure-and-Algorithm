'''
描述
输入n(0<n<50),输出一个n层的AVL树至少有多少个结点。
输入
n
输出
答案
'''

#2200015507 王一粟
from functools import lru_cache
@lru_cache(maxsize = None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n-1) + f(n-2) + 1
t = int(input())
print(f(t))