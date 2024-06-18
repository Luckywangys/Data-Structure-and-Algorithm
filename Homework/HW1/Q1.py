'''
Q1
泰波拿契数列 Tn 定义是
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
给定n请算出Tn
n的范围:1<=n<=30
'''

# 2200015507 王一粟
def t(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return t(n-1) + t(n-2) + t(n-3)
n = int(input())
print(t(n))

# 思路：定义序列函数，内嵌迭代
# 耗时：10min














