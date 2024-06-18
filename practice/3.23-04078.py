'''
描述
定义一个数组，初始化为空。在数组上执行两种操作：
1、增添1个元素，把1个新的元素放入数组。
2、输出并删除数组中最小的数。
使用堆结构实现上述功能的高效算法。
输入
第一行输入一个整数n，代表操作的次数。
每次操作首先输入一个整数type。
当type=1，增添操作，接着输入一个整数u，代表要插入的元素。
当type=2，输出删除操作，输出并删除数组中最小的元素。
1<=n<=100000。
输出
每次删除操作输出被删除的数字。
'''
#2200015507 王一粟
import heapq
n = int(input())
mylist = []
for _ in range(n):
    s = [int(i) for i in input().split()]
    if s == [2]:
        print(heapq.heappop(mylist))
    else:
        heapq.heappush(mylist,int(s[-1]))