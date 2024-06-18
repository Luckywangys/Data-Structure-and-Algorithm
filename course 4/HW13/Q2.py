'''
描述
给出项数为 n 的整数数列 a1...an。
定义函数 f(i) 代表数列中第 i 个元素之后第一个大于 ai 的元素的下标，。若不存在，则 f(i)=0。
试求出 f(1...n)
输入
第一行一个正整数 n。
第二行 n 个正整数 a1...an
输出
一行 n 个整数表示 f(1), f(2), ..., f(n) 的值。
'''

#2200015507 王一粟
n = int(input())
mylist = [int(i) for i in input().split()]
stack = []
result = [0 for i in range(n)]
cnt = -1
for element in mylist:
    cnt += 1
    while stack and stack[-1][0] < element:
        num,i = stack.pop()
        result[i] = cnt+1
    stack.append((element,cnt))
#print(" ".join(map(str,result)))
print(*result)