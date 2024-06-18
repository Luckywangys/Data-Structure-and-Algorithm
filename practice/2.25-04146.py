"""
描述
如上图，有3个方格，每个方格里面都有一个整数a1，a2，a3。已知0 <= a1, a2, a3 <= n，而且a1 + a2是2的倍数，a2 + a3是3的倍数， a1 + a2 + a3是5的倍数。你的任务是找到一组a1，a2，a3，使得a1 + a2 + a3最大。
输入
一行，包含一个整数n (0 <= n <= 100)。
输出
一个整数，即a1 + a2 + a3的最大值。
"""
# 2200015507 王一粟
def solution(n):
    maximum = 0
    for a1 in range(0,n+1):
        for a2 in range(0,n+1):
            for a3 in range(0,n+1):
                if (a1+a2)%2==0 and (a2+a3)%3==0 and (a1+a2+a3)%5==0 and a1+a2+a3>maximum:
                    maximum = a1 + a2 + a3
    return maximum
n = int(input())
print(solution(n))
