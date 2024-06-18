'''
描述
给定一棵二叉树，求该二叉树的深度
二叉树深度定义：从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的节点个数为树的深度
输入
第一行是一个整数n，表示二叉树的结点个数。二叉树结点编号从1到n，根结点为1，n <= 10
接下来有n行，依次对应二叉树的n个节点。
每行有两个整数，分别表示该节点的左儿子和右儿子的节点编号。如果第一个（第二个）数为-1则表示没有左（右）儿子
输出
输出一个整型数，表示树的深度
'''

#2200015507 王一粟
class Node:
    def __init__(self):
        self.left = -1
        self.right = -1

n = int(input())
mylist = [Node() for i in range(n)]
for k in range(n):
    leftnum,rightnum = [int(i) for i in input().split()]
    if leftnum != -1:
        mylist[k].left = mylist[leftnum - 1]
    if rightnum != -1:
        mylist[k].right = mylist[rightnum - 1]
def count(mynode):
    if mynode.left == -1:
        if mynode.right == -1:
            return 1
        else:
            return 1+count(mynode.right)
    else:
        if mynode.right == -1:
            return 1+count(mynode.left)
        else:
            return 1+max(count(mynode.left),count(mynode.right))

print(count(mylist[0]))