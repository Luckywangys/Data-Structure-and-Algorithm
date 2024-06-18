'''
描述
栈是常用的一种数据结构，有n个元素在栈顶端一侧等待进栈，栈顶端另一侧是出栈序列。你已经知道栈的操作有两种：push和pop，前者是将一个元素进栈，后者是将栈顶元素弹出。现在要使用这两种操作，由一个操作序列可以得到一系列的输出序列。请你编程求出对于给定的n，计算并输出由操作数序列1，2，…，n，经过一系列操作可能得到的输出序列总数。
输入
就一个数n(1≤n≤15)。
输出
一个数，即可能输出序列的总数目。
'''

#2200015507 王一粟

#sol1: dfs(注：全局变量不可以使用lru,故本题不适用)
result = 0
stack = []
n = int(input())
wait_list = [i for i in range(n,0,-1)]
def dfs(k):
    global result
    if k == n:
        result += 1
        return
    if wait_list:
        stack.append(wait_list.pop())
        dfs(k)
        wait_list.append(stack.pop())
    if stack:
        x = stack.pop()
        dfs(k+1)
        stack.append(x)
dfs(0)
print(result)

#sol2: 递推法
n = int(input())
def f(n):
    result = 0
    if n==0:
        return 1
    for i in range(1,n+1):
        result += f(i-1) * f(n-i)
    return result
print(f(n))

#sol3: 公式法
n = int(input())
import math
result = int(math.comb(2*n,n)/(n+1))
print(result)

#sol4：dfs改进
from functools import lru_cache
def count_stack_sequences(n):
    @lru_cache(None)
    def backtrack(open_count, close_count):
        if open_count == n and close_count == n:
            return 1
        total_count = 0
        if open_count < n:
            total_count += backtrack(open_count + 1, close_count)
        if close_count < open_count:
            total_count += backtrack(open_count, close_count + 1)
        return total_count

    return backtrack(0, 0)
if __name__ == "__main__":
    n = int(input())
    result = count_stack_sequences(n)
    print(result)
#lru_cache:least recently used--cache（缓存）