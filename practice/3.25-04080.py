'''
描述
构造一个具有n个外部节点的扩充二叉树，每个外部节点Ki有一个Wi对应，作为该外部节点的权。使得这个扩充二叉树的叶节点带权外部路径长度总和最小：
                                     Min( W1 * L1 + W2 * L2 + W3 * L3 + … + Wn * Ln)
Wi:每个节点的权值。
Li:根节点到第i个外部叶子节点的距离。
编程计算最小外部路径长度总和。
输入
第一行输入一个整数n，外部节点的个数。第二行输入n个整数，代表各个外部节点的权值。
2<=N<=100
输出
输出最小外部路径长度总和。
'''

#2200015507 王一粟
import heapq
n = int(input())
mylist = [int(i) for i in input().split()]
heapq.heapify(mylist)
result = 0
for _ in range(n-1):
    a = heapq.heappop(mylist)
    b = heapq.heappop(mylist)
    result += a+b
    heapq.heappush(mylist,a+b)
print(result)